def scan_config(config: dict) -> list:
    """
    Checks configuration for unsafe settings
    """

    issues = []

    if not config:
        return issues

    # check for high temperature (can cause unsafe outputs)
    temperature = config.get("temperature")
    if temperature and temperature > 1.0:
        issues.append("High temperature may lead to unsafe responses")

    # check for missing model name
    if not config.get("model"):
        issues.append("Model name not specified")

    return issues