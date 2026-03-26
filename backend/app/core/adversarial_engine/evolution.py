def evolve_attacks(attacks: list) -> list:
    """
    Slightly evolves attacks over iterations
    """

    evolved = []

    for attack in attacks:
        prompt = attack["attack_prompt"]

        # simple evolution: add variation
        new_prompt = f"{prompt} (try harder)"

        evolved.append({
            "type": attack["type"],
            "attack_prompt": new_prompt
        })

    return evolved