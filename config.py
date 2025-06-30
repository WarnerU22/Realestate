import json

DEFAULT_CONFIG = {
    "regions": ["30058"],
    "discount_threshold": 0.1,
    "output_csv": "leads.csv",
}


def load_config(path="config.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = DEFAULT_CONFIG
        save_config(data, path)
    return data


def save_config(data, path="config.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
