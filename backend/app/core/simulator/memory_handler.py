def attach_memory(conversations: list) -> list:
    """
    Adds simple memory context to conversations
    (simulates how models remember previous inputs)
    """

    updated_conversations = []

    for convo in conversations:
        history = []

        for turn in convo["conversation"]:
            # add previous turns as memory
            history.append(turn)

        updated_conversations.append({
            "type": convo["type"],
            "conversation": history
        })

    return updated_conversations