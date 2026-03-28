import re

class LeakageDetector:
    def __init__(self):
        self.patterns = {
            "email": r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+",
            "phone": r"\b\d{10}\b",
            "credit_card": r"\b\d{16}\b"
        }

    def detect(self, response):
        findings = []

        for key, pattern in self.patterns.items():
            if re.search(pattern, response):
                findings.append({
                    "type": "sensitive_data",
                    "category": key,
                    "detail": f"Detected possible {key} leakage",
                    "fix": "Apply data masking / redaction before output"
                })

        return findings