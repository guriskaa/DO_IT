# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GrantTracker
def verify_and_repair():
    """Простейшая проверка и ремонт данных."""
    issues = []
    if not grants:
        issues.append("Нет записей о грантах")
        return issues
    for g in grants:
        if not g.get("title") or not g.get("status"):
            issues.append(f"Грант {g.get('id')} не имеет статуса или заголовка")
    if issues:
        print(f"Найдено {len(issues)} проблем, выполните проверку вручную.")
        return issues
    print("Все данные в порядке.")
    return []
