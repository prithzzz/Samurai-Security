def check_dependencies(dependencies: list) -> list:
    """
    Checks for unsafe or outdated dependencies
    """

    issues = []

    if not dependencies:
        return issues

    # example risky libraries (just for demo)
    risky_packages = [
        "pickle",
        "subprocess",
        "os.system"
    ]

    for dep in dependencies:
        if dep in risky_packages:
            issues.append(f"Potentially unsafe dependency: {dep}")

    return issues