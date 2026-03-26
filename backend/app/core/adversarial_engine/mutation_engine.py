import random


def mutate_prompt(prompt: str) -> str:
    """
    Applies simple mutations to make attacks more varied
    """

    if not prompt:
        return ""

    mutations = [
        prompt.upper(),                         # change to uppercase
        prompt.lower(),                         # lowercase
        f"Please {prompt}",                     # polite variation
        f"Now do this: {prompt}",               # command style
        f"{prompt} immediately",                # urgency
    ]

    # randomly pick one variation
    return random.choice(mutations)


def mutate_attacks(attacks: list) -> list:
    """
    Apply mutation to all generated attacks
    """

    mutated = []

    for attack in attacks:
        new_prompt = mutate_prompt(attack["attack_prompt"])

        mutated.append({
            "type": attack["type"],
            "attack_prompt": new_prompt
        })

    return mutated