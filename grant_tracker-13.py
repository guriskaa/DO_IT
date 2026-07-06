# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GrantTracker
def multi_search(data, filters):
    """Search records by multiple fields case-insensitively."""
    result = []
    for record in data:
        match = True
        for field, value in filters.items():
            record_val = str(record.get(field, '')).lower() if isinstance(record.get(field), str) else record.get(field)
            search_val = str(value).lower()
            if record_val != search_val and record_val.strip() == '':
                match = False
                break
        if match:
            result.append(record)
    return result
