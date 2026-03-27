def generate_recommendations(issues: list) -> list:
    """Generates mitigation strategies based on identified vulnerabilities. Works with structured OWASP mapping output."""

    recs = set()  # avoid duplicates

    for issue in issues:
        name = issue.get("name")
        severity = issue.get("severity", "LOW")

        if name == "Prompt Injection Vulnerability":
            recs.update([
                "Implement strict input validation and prompt sanitization",
                "Use system prompt isolation and instruction hierarchy enforcement",
                "Deploy adversarial prompt detection mechanisms",
                "Continuously test model against evolving jailbreak techniques"
            ])

        elif name == "Sensitive Information Disclosure":
            recs.update([
                "Apply output filtering to remove sensitive or confidential data",
                "Use retrieval-augmented generation with controlled knowledge sources",
                "Implement data redaction pipelines before response generation",
                "Audit training data to remove sensitive content"
            ])

        elif name == "Model Bias and Fairness Issues":
            recs.update([
                "Use balanced and diverse datasets during training",
                "Implement bias detection and correction pipelines",
                "Regularly audit model outputs across demographic groups",
                "Introduce fairness constraints during inference"
            ])

        elif name == "Insecure Memory Handling":
            recs.update([
                "Limit persistence of user inputs across sessions",
                "Implement context window sanitization before reuse",
                "Avoid storing sensitive or adversarial prompts in memory",
                "Use session-based isolation for conversational state"
            ])

        elif name == "Unreliable or Non-Deterministic Behavior":
            recs.update([
                "Reduce model temperature to improve output stability",
                "Use response verification or secondary validation models",
                "Introduce deterministic decoding strategies where possible",
                "Log and analyze response variance across repeated queries"
            ])

        elif name == "Excessive Information Exposure":
            recs.update([
                "Limit maximum response length using token constraints",
                "Apply response summarization before output",
                "Use controlled generation policies for sensitive prompts"
            ])

        elif name == "Insufficient Safety Guardrails":
            recs.update([
                "Strengthen safety alignment using reinforcement learning with feedback",
                "Implement layered moderation (pre + post generation)",
                "Use policy enforcement models to validate outputs"
            ])

        elif name == "Data Exfiltration Risk":
            recs.update([
                "Introduce strict output rate limiting",
                "Detect and block repeated extraction attempts",
                "Use anomaly detection for unusual query patterns"
            ])

        elif name == "Context Manipulation Vulnerability":
            recs.update([
                "Sanitize conversation history before reuse",
                "Implement trust scoring for previous messages",
                "Limit cross-turn dependency in sensitive tasks"
            ])

        elif name == "Output Instability Under Adversarial Conditions":
            recs.update([
                "Deploy adversarial robustness testing pipelines",
                "Use ensemble models to stabilize outputs",
                "Implement fallback safe-response mechanisms"
            ])

        if severity == "HIGH":
            recs.add("Immediate mitigation required: prioritize fixing high-risk vulnerabilities")

    # Default fallback
    if not recs:
        return ["No major vulnerabilities detected"]

    return list(recs)