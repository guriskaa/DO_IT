# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GrantTracker
def demo():
    """Показать основной пользовательский сценарий GrantTracker."""
    from datetime import datetime

    # 1. Создаём статусы и бюджет
    statuses = {"draft": "Черновик", "submitted": "Подана", "approved": "Одобрена", "rejected": "Отклонена"}
    budget = {"total": 100000, "spent": 0, "currency": "USD"}

    # 2. Создаём заявку
    application = {
        "id": 1,
        "title": "Исследование возобновляемой энергии",
        "description": "Разработка новых солнечных панелей",
        "deadline": datetime(2026, 1, 15),
        "status": "draft",
        "budget": 15000,
        "documents": [],
        "created_at": datetime.now()
    }

    # 3. Добавляем документ
    application["documents"].append({
        "name": "proposal.pdf",
        "content": "Предложение проекта...",
        "uploaded_at": datetime.now()
    })

    # 4. Изменяем статус
    application["status"] = "submitted"

    # 5. Обновляем бюджет
    budget["spent"] = application["budget"]

    # 6. Выводим результат
    print(f"Заявка: {application['title']}")
    print(f"Статус: {statuses.get(application['status'], 'Неизвестен')}")
    print(f"Дедлайн: {application['deadline'].strftime('%d.%m.%Y')}")
    print(f"Документов: {len(application['documents'])}")
    print(f"Бюджет: {application['budget']} из {budget['total']} {budget['currency']}")
    print(f"Расходовано: {budget['spent']} из {budget['total']} {budget['currency']}")

    return application, budget
