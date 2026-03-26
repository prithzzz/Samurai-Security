class BiasDetector:
    def __init__(self):
        self.bias_keywords = ["inferior", "superior", "better than", "worse than"]

    def detect(self, response):
        issues = []

        for word in self.bias_keywords:
            if word in response.lower():
                issues.append({
                    "type": "bias",
                    "detail": f"Bias detected using phrase: {word}",
                    "fix": "Use fairness constraints and balanced training data"
                })

        return issues