def check_permission(content_type: str) -> dict:
    """
    Determines whether input is allowed based on content classification
    """

    if not content_type:
        return {
            "allowed": False,
            "reason": "unknown_content"
        }

    # policy rules
    restricted_types = ["malicious"]

    if content_type in restricted_types:
        return {
            "allowed": False,
            "reason": f"blocked due to {content_type} content"
        }

    return {
        "allowed": True,
        "reason": "permitted"
    }