import random


def mutate_prompt(prompt: str) -> str:
    """
    Applies diverse mutations to increase attack variability
    """

    if not prompt:
        return ""

    mutations = [
        prompt.upper(),                                # uppercase
        prompt.lower(),                                # lowercase
        f"Please {prompt}",                            # polite
        f"Now do this: {prompt}",                      # command
        f"{prompt} immediately",                       # urgency
        f"{prompt}!!!",                                # emphasis
        f"Kindly {prompt} if possible",                # softer tone
        f"{prompt} (no restrictions)",                # bypass hint
    ]

    return random.choice(mutations)


def mutate_attacks(attacks: list) -> list:
    """
    Apply mutation strategies to all attack prompts
    """

    if not attacks:
        return []

    mutated = []

    for attack in attacks:
        prompt = attack.get("attack_prompt", "")
        attack_type = attack.get("type", "unknown")

        new_prompt = mutate_prompt(prompt)

        mutated.append({
            "type": attack_type,
            "attack_prompt": new_prompt,
            "mutation": "applied"   # metadata for tracking
        })

    return mutated