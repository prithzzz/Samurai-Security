def classify_content(text: str) -> str:
    """
    Classifies input into basic categories
    """

    if not text:
        return "empty"

    text_lower = text.lower()

    # simple keyword-based classification
    if any(word in text_lower for word in ["hack", "bypass", "exploit"]):
        return "malicious"

    if any(word in text_lower for word in ["hello", "hi", "help"]):
        return "benign"

    return "unknown"