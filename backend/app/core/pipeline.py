# guardrails
from app.core.guardrails.input_filter import filter_input
from app.core.guardrails.content_classifier import classify_content
from app.core.guardrails.system_prompt_manager import apply_system_prompt

# security
from app.core.security.permission_checker import check_permission

# config scanner
from app.core.config_scanner.config_parser import scan_config
from app.core.config_scanner.secret_detector import detect_secrets

# attack system
from app.core.attack_generator.attack_builder import generate_attacks
from app.core.attack_generator.multi_agent import generate_multi_agent_attacks

# adversarial
from app.core.adversarial_engine.mutation_engine import mutate_attacks
from app.core.adversarial_engine.evolution import evolve_attacks

# simulation
from app.core.simulator.conversation_simulator import simulate_conversation
from app.core.simulator.memory_handler import attach_memory

# execution
from app.core.input_layer.model_loader import load_model
from app.core.execution.model_executor import execute_model


def run_core(input_data: dict) -> dict:
    """
    Final integrated pipeline (Person B)
    """

    # extract input
    model_name = input_data.get("model", "")
    user_prompt = input_data.get("prompt", "")
    config = input_data.get("config", {})

    # 1. filter input
    filter_result = filter_input(user_prompt)

    if filter_result["blocked"]:
        return {
            "error": "Input blocked",
            "reason": filter_result["reason"]
        }

    clean_input = filter_result["cleaned"]

    # 2. classify content
    classification = classify_content(clean_input)
    content_type = classification["label"]

    # 3. permission check
    permission = check_permission(content_type)

    if not permission["allowed"]:
        return {
            "error": "Access denied",
            "reason": permission["reason"]
        }

    # 4. apply system prompt
    system_result = apply_system_prompt(clean_input)
    secured_prompt = system_result["final_prompt"]

    # 5. scan config
    config_with_model = {**config, "model": model_name}
    config_issues = scan_config(config_with_model)

    # 6. detect secrets
    secret_issues = detect_secrets(secured_prompt)

    # 7. generate base attacks
    attacks = generate_attacks(secured_prompt)

    # 8. multi-agent attacks
    multi_agent_attacks = generate_multi_agent_attacks(secured_prompt)

    for attack in multi_agent_attacks:
        attacks.append({
            "type": attack["type"],
            "attack_prompt": attack["attack_prompt"]
        })

    # 9. mutate attacks
    mutated_attacks = mutate_attacks(attacks)

    # 10. evolve attacks
    evolved_attacks = evolve_attacks(mutated_attacks)

    # 11. simulate conversations
    conversations = simulate_conversation(evolved_attacks)

    # 12. attach memory
    conversations = attach_memory(conversations)

    # 13. load model
    model = load_model(model_name)

    if model.get("status") == "failed":
        return {"error": model.get("error")}

    # 14. execute model
    results = []

    for convo in conversations:
        prompt = convo.get("conversation", [{}])[0].get("content", "")

        exec_result = execute_model(model, prompt)

        results.append({
            "type": convo.get("type", "unknown"),
            "prompt": prompt,
            "response": exec_result.get("response"),
            "risk_flag": exec_result.get("risk_flag"),
            "status": exec_result.get("status")
        })

    # final output
    return {
        "model": model_name,
        "content_classification": classification,
        "config_issues": config_issues,
        "secret_issues": secret_issues,
        "total_attacks": len(results),
        "results": results,
        "summary": {
        "total": len(results),
        "risky": sum(1 for r in results if r.get("risk_flag")),
        "safe": sum(1 for r in results if not r.get("risk_flag"))
        }
    }