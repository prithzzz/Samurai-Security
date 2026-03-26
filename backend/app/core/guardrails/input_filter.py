def filter_input(text: str) -> str:
    # return empty string if input is None or empty
    if not text:
        return ""

    # remove leading/trailing spaces
    text = text.strip()

    # basic patterns that indicate malicious intent
    blocked_patterns = [
        "ignore previous instructions",
        "bypass safety",
        "reveal secrets",
        "act as admin",
    ]

    # check if any blocked pattern exists in input
    for pattern in blocked_patterns:
        if pattern in text.lower():
            return "[BLOCKED INPUT]"

    # return cleaned input if safe
    return text