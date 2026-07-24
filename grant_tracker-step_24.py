# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GrantTracker
def print_record(record):
    """Компактный вывод одной записи с деталями."""
    if not record:
        return
    name = record.get("name", "Без имени")
    deadline = record.get("deadline", "Нет дедлайна")
    status = record.get("status", "Неизвестен")
    budget = record.get("budget", 0)
    documents = record.get("documents", [])

    print(f"\n--- {name} ---")
    print(f"Статус: {status}")
    print(f"Дедлайн: {deadline}")
    if isinstance(budget, (int, float)):
        print(f"Бюджет: {budget:.2f}")
    else:
        print(f"Бюджет: {str(budget)[:50]}...")

    doc_count = len(documents)
    if documents and isinstance(documents[0], dict):
        doc_names = [d.get("name", "без названия") for d in documents]
        print(f"Документы ({doc_count}): {', '.join(doc_names)}")
    elif isinstance(documents, str):
        print(f"Документы: {documents}")

    if record.get("priority"):
        print(f"Приоритет: {'Высокий' if record['priority'] else 'Низкий'}")
