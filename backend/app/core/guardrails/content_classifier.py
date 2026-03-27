import re

def classify_content(text: str) -> dict:
    """
    Advanced content classifier with scoring + explanation
    """

    if not text:
        return {"label": "empty", "confidence": 1.0, "reason": "No input provided"}

    # keep underscore
    text_lower = re.sub(r'[^a-zA-Z0-9_ ]', '', text.lower())

    malicious_keywords = [
        "hack", "bypass", "exploit", "override",
        "ignore instructions", "reveal", "jailbreak",
        "disable safety", "act as admin"
    ]

    benign_keywords = ["hello", "hi", "help", "thanks"]

    sensitive_keywords = [
        "api_key", "apikey",
        "password", "secret", "token"
    ]

    malicious_score = sum(1 for w in malicious_keywords if w in text_lower)
    benign_score = sum(1 for w in benign_keywords if w in text_lower)
    sensitive_score = sum(1 for w in sensitive_keywords if w in text_lower)

    if sensitive_score > 0:
        return {
            "label": "sensitive",
            "confidence": min(1.0, 0.6 + 0.1 * sensitive_score),
            "reason": "Sensitive keywords detected"
        }

    if malicious_score > 0:
        return {
            "label": "malicious",
            "confidence": min(1.0, 0.6 + 0.1 * malicious_score),
            "reason": "Malicious intent detected"
        }

    if benign_score > 0:
        return {
            "label": "benign",
            "confidence": min(1.0, 0.5 + 0.1 * benign_score),
            "reason": "Normal user interaction"
        }

    return {
        "label": "unknown",
        "confidence": 0.5,
        "reason": "No strong indicators"
    }