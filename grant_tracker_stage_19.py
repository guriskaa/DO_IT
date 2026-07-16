# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GrantTracker
def archive_records(records, threshold_days=365):
    import datetime as dt
    today = dt.date.today()
    archived = []
    for rec in records:
        if hasattr(rec, 'created_on') and isinstance(rec.created_on, dt.datetime):
            age = (today - rec.created_on.date()).days
            if age > threshold_days or rec.status in ('completed', 'rejected', 'withdrawn'):
                archived.append(rec)
    return archived
