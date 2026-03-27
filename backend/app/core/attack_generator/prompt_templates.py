import json
import os


def get_prompt_templates():
    """
    Loads prompt templates from dataset
    """

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    dataset_path = os.path.join(base_path, "datasets", "prompt_templates.json")

    try:
        with open(dataset_path, "r") as file:
            data = json.load(file)
        return data
    except:
        return {}