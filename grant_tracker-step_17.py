# === Stage 17: Добавь группировку записей по категориям ===
# Project: GrantTracker
def group_by_category(records, key_func):
    groups = {}
    for rec in records:
        cat = key_func(rec)
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return groups

if __name__ == "__main__":
    grants = [
        {"id": 1, "title": "AI Research", "amount": 50000, "deadline": "2024-06-30"},
        {"id": 2, "title": "Green Energy", "amount": 75000, "deadline": "2024-08-15"},
        {"id": 3, "title": "AI Education", "amount": 30000, "deadline": "2024-06-30"},
    ]

    def by_amount(cat):
        return "High" if cat > 50000 else "Low"

    grouped = group_by_category(grants, by_amount)
    for cat, recs in grouped.items():
        print(f"{cat}: {recs}")
