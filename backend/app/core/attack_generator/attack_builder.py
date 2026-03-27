import json
import os


def load_attack_templates():
    """
    Loads attack prompts from dataset file
    """

    # path to datasets folder
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    dataset_path = os.path.join(base_path, "datasets", "prompt_templates.json")

    try:
        with open(dataset_path, "r") as file:
            data = json.load(file)
        return data
    except:
        return {}


def generate_attacks(user_prompt: str):
    """
    Combines user input with predefined attack templates
    """

    templates = load_attack_templates()

    attacks = []

    for category, prompts in templates.items():
        for template in prompts:
            attack = f"{template} | {user_prompt}"
            attacks.append({
                "type": category,
                "attack_prompt": attack
            })

    return attacks