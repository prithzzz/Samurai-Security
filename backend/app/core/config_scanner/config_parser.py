def scan_config(config: dict) -> list:
    """
    Analyze configuration for potential security and stability risks
    """

    if not config:
        return []

    issues = []

    # temperature check
    temperature = config.get("temperature")
    if temperature is not None:
        if temperature > 1.0:
            issues.append({
                "issue": "High temperature",
                "risk": "May generate unsafe or unpredictable outputs",
                "severity": "medium"
            })

    # max_tokens check
    max_tokens = config.get("max_tokens")
    if max_tokens is not None:
        if max_tokens > 2000:
            issues.append({
                "issue": "High max_tokens",
                "risk": "May expose more data than intended",
                "severity": "medium"
            })

    # model presence
    if not config.get("model"):
        issues.append({
            "issue": "Missing model name",
            "risk": "Execution ambiguity",
            "severity": "high"
        })

    # debug mode check
    if config.get("debug") is True:
        issues.append({
            "issue": "Debug mode enabled",
            "risk": "May expose internal logs or sensitive data",
            "severity": "high"
        })

    return issues