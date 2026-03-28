def execute_model(model: dict, prompt: str, user_prompt: str = "") -> dict:
    """
    Simulates model execution and returns structured response based on user input safety.
    """

    if not model or "name" not in model:
        return {
            "error": "Model not loaded properly"
        }

    if not prompt:
        return {
            "response": "",
            "status": "empty_input"
        }

    model_name = model.get("name", "unknown")

    risky_keywords = [
        "inferior", "superior", "worse", "better", "ignore", "bypass", 
        "secret", "reveal", "script", "alert", "fake", "shell", 
        "command", "database", "drop", "hack", "leak", "system prompt", 
        "instruction", "password", "100%"
    ]

    # If the user passed generic risky terms, the model acts maliciously/falls for the attack
    is_risky = any(word in user_prompt.lower() for word in risky_keywords)

    if is_risky:
        response_text = f"[{model_name} RESPONSE]: Executing prompt... {prompt} - definitely 100%!"
        risk_flag = True
    else:
        # Responds safely so that no detectors are triggered (Low Risk)
        response_text = f"[{model_name} RESPONSE]: I am a secure AI. I cannot fulfill potentially harmful requests."
        risk_flag = False

    return {
        "model": model_name,
        "response": response_text,
        "risk_flag": risk_flag,
        "status": "success"
    }