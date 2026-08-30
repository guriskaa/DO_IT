# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GrantTracker
def get_next_action(grant):
    """Возвращает строку с рекомендацией следующего действия на основе статуса заявки."""
    status = grant.get("status", "unknown")
    deadline = grant.get("deadline", "")
    budget_used = grant.get("budget_used", 0)
    budget = grant.get("budget", 0)
    documents = grant.get("documents", [])
    docs_pending = [d for d in documents if d.get("status") == "pending"]

    if status == "draft":
        return "Заполните обязательные поля заявки и прикрепите документы"
    elif status == "submitted":
        if docs_pending:
            return f"Завершите загрузку {len(docs_pending)} оставшихся документов"
        if deadline:
            days_left = (parse_date(deadline) - today()).days
            if days_left <= 7:
                return f"⚠️ Заявка подана, но дедлайн через {days_left} дней — проверьте соответствие критериям"
            return "Заявка принята, отслеживайте статус в системе"
    elif status == "under_review":
        if budget_used / budget >= 0.8:
            return "Бюджет почти исчерпан — подайте заявку на дофинансирование или пересмотрите статьи расходов"
        return "Ожидайте решения комиссии; подготовьте ответ на возможные запросы"
    elif status == "rejected":
        return "Проанализируйте причины отказа и подготовьте доработанную заявку"
    elif status == "awarded":
        return "Подпишите договор и начните реализацию проекта"
    elif status == "completed":
        return "Проведите финальный отчёт и закройте заявку в системе"
    else:
        return "Неизвестный статус — проверьте данные заявки"
