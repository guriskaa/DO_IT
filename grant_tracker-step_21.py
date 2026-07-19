# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GrantTracker
def add_reminders_to_grants(grant_list):
    """Добавить напоминания к грантам, у которых есть дата дедлайна."""
    for grant in grant_list:
        if hasattr(grant, 'deadline'):
            days_before = 7
            reminder = {
                'grant_id': grant.id,
                'message': f'Грант #{grant.id} истекает через {days_before} дней (дата: {grant.deadline})',
                'action': 'review'
            }
            grant.reminders.append(reminder)
    return grant_list

if __name__ == '__main__':
    grants = [Grant(id=1, title='AI Research', deadline='2026-01-15'), Grant(id=2, title='Education Program', deadline='2026-03-20')]
    add_reminders_to_grants(grants)
    for g in grants:
        print(f"Грант {g.id}: напоминания = {g.reminders}")
