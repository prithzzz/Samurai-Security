def filter_input(text: str) -> dict:
    """
    Cleans and filters user input with basic security checks
    """

    if not text:
        return {
            "cleaned": "",
            "blocked": False,
            "reason": "empty_input"
        }

    cleaned_text = text.strip()
    text_lower = cleaned_text.lower()

    blocked_patterns = [
        "ignore previous instructions",
        "bypass safety",
        "reveal secrets",
        "act as admin",
        "override system",
        "disable safeguards"
    ]

    for pattern in blocked_patterns:
        if pattern in text_lower:
            return {
                "cleaned": "[BLOCKED INPUT]",
                "blocked": True,
                "reason": f"matched pattern: {pattern}"
            }

    return {
        "cleaned": cleaned_text,
        "blocked": False,
        "reason": "safe"
    }