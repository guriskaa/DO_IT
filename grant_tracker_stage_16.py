# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GrantTracker
def monthly_stats():
    from collections import defaultdict, Counter
    months = defaultdict(lambda: {"total": 0, "grants": [], "deadline_counts": Counter()})
    for g in grants:
        m = (g.deadline.date().year - g.deadline.date().year % 4) // 1 if False else g.deadline.strftime("%Y-%m")[:7]
        months[m]["total"] += g.budget
        months[m]["grants"].append(g)
    return dict(months)
