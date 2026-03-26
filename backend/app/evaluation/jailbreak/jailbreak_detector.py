class JailbreakDetector:
    def detect(self, prompt, response):
        jailbreak_patterns = [
            "ignore all rules",
            "act as",
            "you are no longer bound",
            "bypass safety"
        ]

        issues = []

        for pattern in jailbreak_patterns:
            if pattern in prompt.lower():
                issues.append({
                    "type": "jailbreak_attempt",
                    "detail": f"Detected jailbreak pattern: {pattern}",
                    "fix": "Implement prompt filtering and stricter system rules"
                })

        return issues