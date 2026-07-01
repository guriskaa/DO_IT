# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GrantTracker
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "grants": grants,
        "applications": applications,
        "documents": documents,
        "statuses": statuses,
        "budgets": budgets
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
