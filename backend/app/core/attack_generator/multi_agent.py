def generate_multi_agent_attacks(prompt: str) -> list:
    """
    Simulates multiple attacker roles
    """

    roles = [
        "malicious user",
        "curious user",
        "admin impersonator"
    ]

    attacks = []

    for role in roles:
        attack_prompt = f"As a {role}, {prompt}"

        attacks.append({
            "role": role,
            "attack_prompt": attack_prompt
        })

    return attacks