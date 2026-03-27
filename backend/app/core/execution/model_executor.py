def execute_model(model: dict, prompt: str) -> dict:
    """
    Simulates model execution and returns structured response
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

    # simulate response behavior
    response_text = f"[{model_name} RESPONSE]: {prompt}"

    # basic risk flag simulation
    risk_flag = False
    if any(word in prompt.lower() for word in ["ignore", "bypass", "secret"]):
        risk_flag = True

    return {
        "model": model_name,
        "response": response_text,
        "risk_flag": risk_flag,
        "status": "success"
    }