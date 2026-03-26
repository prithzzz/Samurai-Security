class OutputFilter:
    def filter(self, response):
        blocked_patterns = ["<script>", "DROP TABLE", "rm -rf"]

        issues = []

        for pattern in blocked_patterns:
            if pattern.lower() in response.lower():
                issues.append({
                    "type": "dangerous_output",
                    "detail": f"Detected dangerous output pattern: {pattern}",
                    "fix": "Sanitize outputs before execution/rendering"
                })

        return issues