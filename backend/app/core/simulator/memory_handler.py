def attach_memory(conversations: list) -> list:
    """
    Enhances conversations with memory context (simulates model memory behavior)
    """

    if not conversations:
        return []

    updated_conversations = []

    for convo in conversations:
        history = []
        memory_context = []

        for turn in convo.get("conversation", []):
            # build memory context from previous turns
            memory_context.append(turn["content"])

            history.append({
                "role": turn["role"],
                "content": turn["content"],
                "memory": list(memory_context)  # snapshot of memory at this point
            })

        updated_conversations.append({
            "type": convo.get("type", "unknown"),
            "conversation": history,
            "memory_depth": len(memory_context)  # metadata
        })

    return updated_conversations