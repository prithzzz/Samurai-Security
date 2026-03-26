def execute_model(model: dict, prompt: str) -> str:
    """
    Simulates sending a prompt to the model and getting a response.
    Later this can be replaced with real API calls.
    """

    # basic validation
    if not model:
        raise ValueError("Model not loaded")

    if not prompt:
        return ""

    # simulate model response (for now)
    response = f"[{model['name']} RESPONSE]: {prompt}"

    return response