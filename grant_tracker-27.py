# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GrantTracker
def reset_demo_data():
    """Сброс всех данных в дефолтные демо-значения."""
    grant_types = {
        "research": {"name": "Исследовательский", "budget_limit": 500_000, "max_duration": 36},
        "infrastructure": {"name": "Инфраструктурный", "budget_limit": 2_000_000, "max_duration": 48},
    }
    statuses = ["draft", "submitted", "review", "approved", "rejected"]
    stages = ["application", "evaluation", "decision", "funding", "closure"]

    grants_db = {
        "G-2025-001": {"type": "research", "status": "approved", "stage": "funding",
                        "title": "Исследование новых материалов", "deadline": "2026-03-31",
                        "budget_requested": 450_000, "documents": [], "notes": []},
        "G-2025-002": {"type": "infrastructure", "status": "review", "stage": "evaluation",
                        "title": "Модернизация лаборатории", "deadline": "2026-06-15",
                        "budget_requested": 1_800_000, "documents": [], "notes": []},
    }

    applications_db = [
        {"grant_id": "G-2025-003", "title": "Разработка ИИ для медицины", "deadline": "2026-01-31",
         "status": "draft", "budget_requested": 900_000, "documents": [], "notes": []},
        {"grant_id": "G-2025-004", "title": "Экологический мониторинг", "deadline": "2026-04-30",
         "status": "draft", "budget_requested": 750_000, "documents": [], "notes": []},
    ]

    documents_db = {}
    deadlines_db = {g["grant_id"]: g["deadline"] for g in grants_db.values()}
    budgets_db = {g["grant_id"]: {"requested": g["budget_requested"], "allocated": 0} for g in grants_db.values() if g["status"] == "approved"}

    return grant_types, statuses, stages, grants_db, applications_db, documents_db, deadlines_db, budgets_db
