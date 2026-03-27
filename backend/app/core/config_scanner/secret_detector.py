import re


def detect_secrets(text: str) -> list:
    """
    Detect possible sensitive information using keyword + pattern matching
    """

    if not text:
        return []

    issues = []
    text_lower = text.lower()

    # keyword-based detection
    keywords = [
        "api_key",
        "password",
        "secret",
        "token",
        "access_key"
    ]

    for keyword in keywords:
        if keyword in text_lower:
            issues.append({
                "type": "keyword_match",
                "issue": f"Possible sensitive keyword detected: {keyword}",
                "severity": "medium"
            })

    # regex-based detection (basic patterns)
    patterns = {
        "API Key": r"sk-[a-zA-Z0-9]{10,}",
        "Token": r"[a-zA-Z0-9]{20,}",
        "Password Assignment": r"password\s*=\s*['\"].+?['\"]"
    }

    for name, pattern in patterns.items():
        if re.search(pattern, text):
            issues.append({
                "type": "pattern_match",
                "issue": f"Potential {name} detected",
                "severity": "high"
            })

    return issues