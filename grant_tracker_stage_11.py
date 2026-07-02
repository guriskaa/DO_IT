# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GrantTracker
import json, os

DATA_FILE = "grant_data.json"

def save_to_json(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('grants', [])
    except (json.JSONDecodeError, IOError):
        return []

def get_data():
    existing = load_from_json()
    if not existing:
        save_to_json({'grants': [], 'settings': {'currency': 'RUB'}})
    return existing
