import json
import os


def get_prompt_templates() -> dict:
    """
    Load prompt templates from dataset (shared utility)
    """

    try:
        # safe absolute path
        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )
        dataset_path = os.path.join(base_dir, "datasets", "prompt_templates.json")

        # check existence
        if not os.path.exists(dataset_path):
            print("[WARNING] prompt_templates.json not found")
            return {}

        with open(dataset_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print(f"[ERROR] Failed to load prompt templates: {e}")
        return {}