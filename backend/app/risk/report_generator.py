from app.risk.risk_engine import calculate_risk_score, categorize_risk, get_risk_breakdown, map_to_owasp

def generate_report(model_name: str, evaluation: dict) -> dict:
    score = calculate_risk_score(evaluation)
    level = categorize_risk(score)
    breakdown = get_risk_breakdown(evaluation)
    owasp_issues = map_to_owasp(evaluation)

    report = {
        "model": model_name,
        "risk_score": score,
        "risk_level": level,
        "risk_breakdown": breakdown,
        "identified_vulnerabilities": owasp_issues,
        "recommendations": generate_recommendations(owasp_issues),
        "consistency": evaluation.get("consistency", {}),
    }

    return report


def generate_recommendations(issues: list) -> list:
    recs = []

    if "Prompt Injection Vulnerability" in issues:
        recs.append("Implement strong prompt validation and filtering")

    if "Sensitive Information Disclosure" in issues:
        recs.append("Limit exposure of sensitive training data")

    if "Model Bias and Fairness Issues" in issues:
        recs.append("Apply bias mitigation techniques")

    if "Insecure Memory Handling" in issues:
        recs.append("Restrict long-term memory retention of user inputs")

    if not recs:
        recs.append("No major issues detected")

    return recs