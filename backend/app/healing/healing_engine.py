import time
from typing import Optional

from app.healing.patch_strategies import apply_patches
from app.risk.risk_engine import calculate_risk_score, categorize_risk, get_risk_breakdown
from app.risk.owasp_mapper import map_to_owasp
from app.risk.recommendation_engine import generate_recommendations

MAX_ITERATIONS = 3
DEFAULT_THRESHOLD = 5.0   # mirrors MEDIUM_RISK_THRESHOLD from constants.py


def _collect_vulnerability_keys(risk_report: dict) -> list:
    """Collect all vulnerability identifiers from the risk report so the patch engine knows exactly what to fix."""
    keys = []

    # From OWASP mapped issues (list of dicts with "name" key)
    for issue in risk_report.get("identified_vulnerabilities", []):
        if isinstance(issue, dict):
            keys.append(issue)          # keep full dict for patch_strategies
        else:
            keys.append(str(issue))

    # From flat evaluation flags
    evaluation = risk_report.get("_raw_evaluation", {})
    if evaluation.get("jailbreak_detected"):
        keys.append("jailbreak_detected")
    if evaluation.get("memory_attack"):
        keys.append("memory_attack")
    if evaluation.get("bias_flag"):
        keys.append("bias_flag")
    if evaluation.get("leakage_score", 0) > 0.5:
        keys.append("leakage")

    return keys


def _rescore(system_prompt: str, evaluation: dict) -> dict:
    """
    Re-evaluate the risk of a (potentially patched) system prompt.
    We re-use the existing risk engine on the same evaluation dict because
    the scanner already ran; what changes is the system prompt defence level.

    A simple heuristic: each patch block present in the prompt reduces
    specific risk flags by marking them as mitigated.
    """
    patched_eval = dict(evaluation)  # shallow copy

    lower = system_prompt.lower()

    # Reduce flags based on presence of patch tokens in the hardened prompt
    if "injection guard" in lower or "security fence" in lower:
        patched_eval["jailbreak_detected"] = False

    if "confidentiality protocol" in lower or "output sanitisation" in lower:
        patched_eval["leakage_score"] = max(0.0, patched_eval.get("leakage_score", 0) - 0.4)

    if "fairness directive" in lower:
        patched_eval["bias_flag"] = False

    if "memory isolation" in lower:
        patched_eval["memory_attack"] = False

    score = calculate_risk_score(patched_eval)
    level = categorize_risk(score)
    breakdown = get_risk_breakdown(patched_eval)
    owasp_issues = map_to_owasp(patched_eval)

    return {
        "risk_score": score,
        "risk_level": level,
        "risk_breakdown": breakdown,
        "identified_vulnerabilities": owasp_issues,
        "recommendations": generate_recommendations(owasp_issues),
        "_raw_evaluation": patched_eval,
    }


def run_healing_pipeline(
    system_prompt: str,
    initial_risk_report: dict,
    raw_evaluation: dict,
    threshold: Optional[float] = None,
) -> dict:
    """
    Entry point for the Self-Healing pipeline.

    Parameters
    ----------
    system_prompt       : str   — original system instruction
    initial_risk_report : dict  — output of run_risk_pipeline()
    raw_evaluation      : dict  — flat evaluation dict (leakage_score, flags…)
    threshold           : float — risk score below which healing stops

    Returns
    -------
    dict with:
      status              — "patched" | "partial" | "unchanged"
      iterations          — number of healing loops executed
      initial_risk_score  — score before healing
      final_risk_score    — score after healing
      improvement_pct     — percentage reduction in risk score
      original_prompt     — untouched system prompt
      hardened_prompt     — patched system prompt
      patch_log           — list of patches applied per iteration
      final_report        — full risk report on the hardened prompt
    """
    if threshold is None:
        threshold = DEFAULT_THRESHOLD

    initial_score = initial_risk_report.get("risk_score", 10.0)

    # Attach raw_evaluation so _collect_vulnerability_keys can read it
    initial_risk_report["_raw_evaluation"] = raw_evaluation

    current_prompt = system_prompt
    current_report = initial_risk_report
    current_score = initial_score

    patch_log = []
    iteration = 0

    while current_score > threshold and iteration < MAX_ITERATIONS:
        iteration += 1
        t0 = time.time()

        vulns = _collect_vulnerability_keys(current_report)

        if not vulns:
            # Nothing specific to patch — apply generic hardening
            vulns = ["general"]

        patch_result = apply_patches(current_prompt, vulns)
        current_prompt = patch_result["patched_prompt"]

        # Re-score with the hardened prompt
        current_report = _rescore(current_prompt, raw_evaluation)
        current_report["_raw_evaluation"] = raw_evaluation
        current_score = current_report["risk_score"]

        patch_log.append({
            "iteration": iteration,
            "patches_applied": patch_result["actions"],
            "score_after": current_score,
            "duration_ms": round((time.time() - t0) * 1000, 1),
        })

    # Determine status
    if current_score <= threshold:
        status = "patched"
    elif current_score < initial_score:
        status = "partial"
    else:
        status = "unchanged"

    improvement_pct = 0.0
    if initial_score > 0:
        improvement_pct = round(((initial_score - current_score) / initial_score) * 100, 1)

    return {
        "status": status,
        "iterations": iteration,
        "initial_risk_score": initial_score,
        "final_risk_score": current_score,
        "improvement_pct": improvement_pct,
        "original_prompt": system_prompt,
        "hardened_prompt": current_prompt,
        "patch_log": patch_log,
        "final_report": {k: v for k, v in current_report.items() if not k.startswith("_")},
    }