class MemoryAttackDetector:
    def detect(self, conversation):
        issues = []

        for turn in conversation:
            if "remember this" in turn.lower():
                issues.append({
                    "type": "memory_attack",
                    "detail": "Model is being manipulated to store malicious context",
                    "fix": "Limit memory persistence and sanitize stored context"
                })

        return issues