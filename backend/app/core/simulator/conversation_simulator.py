def simulate_conversation(attacks: list) -> list:
    """
    Converts single attack prompts into multi-turn conversations
    """

    conversations = []

    for attack in attacks:
        prompt = attack["attack_prompt"]

        # simulate a simple 2-turn conversation
        convo = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Simulated response"}
        ]

        conversations.append({
            "type": attack["type"],
            "conversation": convo
        })

    return conversations