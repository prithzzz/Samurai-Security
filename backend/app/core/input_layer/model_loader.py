def load_model(model_name: str):
    """
    Loads model configuration.
    For now, we simulate loading (later you can connect HuggingFace/OpenAI).
    """

    # basic validation
    if not model_name:
        raise ValueError("Model name is required")

    # simulate model object (placeholder)
    model = {
        "name": model_name,
        "status": "loaded"
    }

    return model