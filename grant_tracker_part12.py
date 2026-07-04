# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GrantTracker
import json, os, sys

def load_grants_from_file(file_path: str) -> list[dict]:
    if not file_path or not isinstance(file_path, str):
        raise ValueError("Файл должен быть указан как строка")
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'grants' in data:
                return data['grants']
            else:
                print("Ошибка: неверный формат JSON (ожидался список или объект с ключом 'grants').")
                return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON из '{file_path}': {e}")
        return []
    except IOError as e:
        print(f"Ошибка доступа к файлу '{file_path}': {e}")
        return []

if __name__ == "__main__":
    file_to_load = sys.argv[1] if len(sys.argv) > 1 else "data/grants.json"
    grants = load_grants_from_file(file_to_load)
    print(f"Загружено грантов: {len(grants)}")
