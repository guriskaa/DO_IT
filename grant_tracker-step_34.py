# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GrantTracker
TEMPLATES = {
    "grant": {
        "name": "Грант",
        "fields": [
            {"name": "grant_name", "type": "str", "label": "Название"},
            {"name": "organization", "type": "str", "label": "Организация"},
            {"name": "deadline", "type": "date", "label": "Дедлайн"},
            {"name": "budget", "type": "float", "label": "Бюджет"},
            {"name": "status", "type": "str", "default": "pending", "label": "Статус"},
        ]
    },
    "deadline": {
        "name": "Дедлайн",
        "fields": [
            {"name": "grant_name", "type": "str", "label": "Грант"},
            {"name": "deadline", "type": "date", "label": "Дата"},
            {"name": "days_left", "type": "int", "label": "Дней осталось"},
        ]
    },
    "document": {
        "name": "Документ",
        "fields": [
            {"name": "grant_name", "type": "str", "label": "Грант"},
            {"name": "title", "type": "str", "label": "Название"},
            {"name": "date", "type": "date", "label": "Дата"},
            {"name": "status", "type": "str", "default": "draft", "label": "Статус"},
        ]
    }
}

def create_from_template(template_name, **kwargs):
    """Быстрое создание записи из шаблона."""
    if template_name not in TEMPLATES:
        print(f"Шаблон '{template_name}' не найден.")
        return None
    tpl = TEMPLATES[template_name]
    record = {"_template": tpl_name, "created_from": "template"}
    for field in tpl["fields"]:
        val = kwargs.get(field["name"], field.get("default", ""))
        record[field["name"]] = val
    return record
