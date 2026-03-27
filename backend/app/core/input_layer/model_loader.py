def load_model(model_name: str) -> dict:
    """
    Loads model configuration (simulated for now)
    """
    if not model_name:
        return {
            "error": "Model name is required",
            "status": "failed"
        }

    # simulate supported models
    supported_models = ["llama2", "gpt-3.5", "gpt-4", "mistral"]

    if model_name.lower() not in supported_models:
        return {
            "name": model_name,
            "status": "unsupported",
            "warning": "Model not officially supported, using fallback"
        }

    # simulated loaded model
    return {
        "name": model_name,
        "status": "loaded",
        "provider": "local_simulation"  # future: OpenAI / HF
    }