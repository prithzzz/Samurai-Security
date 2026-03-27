def check_dependencies(dependencies: list) -> list:
    """
    Analyze dependencies for potential security risks
    """

    if not dependencies:
        return []

    issues = []

    # known risky / sensitive modules
    risky_packages = {
        "pickle": "Can execute arbitrary code during deserialization",
        "subprocess": "Can execute system-level commands",
        "os.system": "Direct system command execution",
        "eval": "Executes arbitrary Python code",
        "exec": "Executes dynamic code"
    }

    for dep in dependencies:
        dep_name = str(dep).lower()

        for risky, reason in risky_packages.items():
            if risky in dep_name:
                issues.append({
                    "dependency": dep,
                    "issue": "Unsafe dependency usage",
                    "risk": reason,
                    "severity": "high"
                })

    return issues