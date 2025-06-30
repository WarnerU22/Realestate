import json

DEFAULT_CONFIG = {
    "regions": ["30058"],
    "discount_threshold": 0.1,
    "output_csv": "leads.csv",
    "mailjet_api_key": "",
    "mailjet_api_secret": "",
    "mailjet_sender": "",
    "mailjet_recipient": "",
}


def load_config(path="config.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = DEFAULT_CONFIG.copy()
        save_config(data, path)
        return data

    updated = False
    for key, value in DEFAULT_CONFIG.items():
        if key not in data:
            data[key] = value
            updated = True
    if updated:
        save_config(data, path)
    return data


def save_config(data, path="config.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
