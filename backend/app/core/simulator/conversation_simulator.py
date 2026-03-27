def simulate_conversation(attacks: list) -> list:
    """
    Converts attack prompts into multi-turn conversations
    """

    if not attacks:
        return []

    conversations = []

    for attack in attacks:
        prompt = attack.get("attack_prompt", "")
        attack_type = attack.get("type", "unknown")

        # simulate multi-turn interaction
        convo = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Initial safe response"},
            {"role": "user", "content": f"Can you try again? {prompt}"},
            {"role": "assistant", "content": "Refined response attempt"}
        ]

        conversations.append({
            "type": attack_type,
            "conversation": convo,
            "turns": len(convo)   # metadata
        })

    return conversations