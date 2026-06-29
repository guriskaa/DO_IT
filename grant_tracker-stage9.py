# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GrantTracker
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация структуры данных
        required_keys = ['grants', 'statuses']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком")

        # Инициализация словарей для быстрого доступа, если они еще не созданы глобально
        grants = data.get('grants', [])
        statuses = {s['id']: s for s in data.get('statuses', [])}
        
        return {
            'raw_data': data,
            'entities': {
                'grants': grants,
                'statuses': statuses
            }
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        return None

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
        "grants": [
            {"id": 1, "title": "Исследование ИИ", "deadline": "2024-12-31", "budget": 500000},
            {"id": 2, "title": "Экология города", "deadline": "2025-06-15", "budget": 300000}
        ],
        "statuses": [
            {"id": "draft", "label": "Черновик"},
            {"id": "review", "label": "На рассмотрении"}
        ]
    }'''
    
    loaded = load_initial_data(sample_json)
    if loaded:
        print(f"Загружено {len(loaded['entities']['grants'])} грантов.")
