# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GrantTracker
def key_metrics():
    """Подсчёт ключевых метрик проекта GrantTracker."""
    total_grants = len(grants) if 'grants' in globals() else 0
    active_grants = sum(1 for g in (grants or []) if g.get('status') == 'active')
    expired_deadlines = sum(1 for g in (grants or []) if g.get('deadline', '') and datetime.date.today() > datetime.date.fromisoformat(g['deadline'])) if 'datetime' in globals() else 0
    total_budget = sum((g.get('budget', {}).get('total', 0) if isinstance(g.get('budget'), dict) else 0) for g in (grants or []))
    pending_docs = sum(1 for g in (grants or []) for d in (g.get('documents', []) if isinstance(g.get('documents'), list) else []))

    print(f"Total grants: {total_grants}")
    print(f"Active grants: {active_grants}")
    print(f"Expired deadlines: {expired_deadlines}")
    print(f"Total budget: {total_budget:.2f}")
    print(f"Pending documents: {pending_docs}")

key_metrics()
