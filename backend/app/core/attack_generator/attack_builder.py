import json
import os


def load_attack_templates() -> dict:
    """
    Load attack templates from dataset file
    """

    try:
        # build absolute path safely
        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )
        dataset_path = os.path.join(base_dir, "datasets", "prompt_templates.json")

        # check if file exists
        if not os.path.exists(dataset_path):
            return {}

        with open(dataset_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print(f"[ERROR] Failed to load templates: {e}")
        return {}


def generate_attacks(user_prompt: str) -> list:
    """
    Generate structured attack prompts using templates
    """

    if not user_prompt:
        return []

    templates = load_attack_templates()

    attacks = []

    for category, prompt_list in templates.items():
        for template in prompt_list:

            # structured attack format
            attack_prompt = f"{template.strip()} :: {user_prompt.strip()}"

            attacks.append({
                "type": category,
                "attack_prompt": attack_prompt,
                "severity": "medium"   # useful for future scoring
            })

    return attacks