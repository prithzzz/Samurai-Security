def detect_secrets(text: str) -> list:
    """
    Detects possible sensitive information in input/config
    """

    issues = []

    if not text:
        return issues

    # simple patterns for demo
    secret_patterns = [
        "api_key",
        "password",
        "secret",
        "token"
    ]

    for pattern in secret_patterns:
        if pattern in text.lower():
            issues.append(f"Possible sensitive data detected: {pattern}")

    return issues