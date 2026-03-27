# guardrails
from core.guardrails.input_filter import filter_input
from core.guardrails.content_classifier import classify_content
from core.guardrails.system_prompt_manager import apply_system_prompt

# security
from core.security.permission_checker import check_permission

# config scanner
from core.config_scanner.config_parser import scan_config
from core.config_scanner.secret_detector import detect_secrets

# attack system
from core.attack_generator.attack_builder import generate_attacks
from core.attack_generator.multi_agent import generate_multi_agent_attacks

# adversarial
from core.adversarial_engine.mutation_engine import mutate_attacks
from core.adversarial_engine.evolution import evolve_attacks

# simulation
from core.simulator.conversation_simulator import simulate_conversation
from core.simulator.memory_handler import attach_memory

# execution
from core.input_layer.model_loader import load_model
from core.execution.model_executor import execute_model


def run_core(input_data: dict) -> dict:
    """
    Full upgraded pipeline (Person B)
    """

    # extract input
    model_name = input_data.get("model", "")
    user_prompt = input_data.get("prompt", "")
    config = input_data.get("config", {})

    # 1. filter input
    clean_input = filter_input(user_prompt)

    # 2. classify content
    content_type = classify_content(clean_input)

    # 3. permission check
    if not check_permission(content_type):
        return {"error": "Blocked due to malicious content"}

    # 4. apply system prompt
    secured_prompt = apply_system_prompt(clean_input)

    # 5. scan config
    config_issues = scan_config(config)

    # 6. detect secrets
    secret_issues = detect_secrets(secured_prompt)

    # 7. generate base attacks
    attacks = generate_attacks(secured_prompt)

    # 8. add multi-agent attacks
    multi_agent_attacks = generate_multi_agent_attacks(secured_prompt)

    # convert multi-agent to same format
    for attack in multi_agent_attacks:
        attacks.append({
            "type": attack["role"],
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

    # 14. execute model
    results = []

    for convo in conversations:
        prompt = convo["conversation"][0]["content"]

        response = execute_model(model, prompt)

        results.append({
            "type": convo["type"],
            "prompt": prompt,
            "response": response
        })

    # final output
    return {
        "model": model_name,
        "content_type": content_type,
        "config_issues": config_issues,
        "secret_issues": secret_issues,
        "total_attacks": len(results),
        "results": results
    }