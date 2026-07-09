# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GrantTracker
def weekly_grant_stats(grants):
    """Return a dict mapping week start date (YYYY-MM-DD) to {applied, active, avg_budget}."""
    stats = {}  # week -> applied_count, budget_sum, week_map
    for g in grants:
        if not isinstance(g.get("deadline"), datetime.date): continue
        deadline = g["deadline"]
        week_start = deadline - timedelta(days=deadline.weekday())
        key = week_start.strftime("%Y-%W")  # ISO week number
        if key not in stats:
            stats[key] = {"applied": 0, "budget_sum": 0}
        stats[key]["applied"] += 1
        budget = g.get("budget", 0)
        if isinstance(budget, (int, float)):
            stats[key]["budget_sum"] += budget
    return stats
