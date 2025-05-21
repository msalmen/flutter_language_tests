# config/lang_config.py

import json

def load_lang_config(path="config/lang_config.json"):
    with open(path, encoding='utf-8') as f:
        config = json.load(f)
    return config["languages"]
