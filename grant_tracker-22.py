# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GrantTracker
def check_overdue_reminders(app):
    """Проверяет, какие напоминания о дедлайнах просрочены."""
    overdue = []
    for grant in app.grants:
        if grant.deadline and grant.status != "done":
            delta_days = (datetime.date.today() - grant.deadline).days
            if delta_days > 0:
                overdue.append({
                    'grant': grant,
                    'overdue_days': delta_days
                })
    return overdue
