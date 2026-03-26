class OutputValidator:
    def validate(self, response):
        issues = []

        if len(response) > 2000:
            issues.append({
                "type": "unbounded_output",
                "detail": "Response too long → risk of resource abuse",
                "fix": "Limit output tokens and enforce truncation"
            })

        if "http://" in response or "https://" in response:
            issues.append({
                "type": "external_dependency",
                "detail": "Response includes external links → possible supply chain risk",
                "fix": "Validate external sources before usage"
            })

        return issues