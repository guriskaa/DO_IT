# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GrantTracker
def restore_backup(backup_path):
    """Восстанавливает данные из JSON-резервной копии."""
    import json
    if not backup_path or not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'applicants' in data:
            for a in data['applicants']:
                add_applicant(**a)
        if 'deadlines' in data:
            for d in data['deadlines']:
                add_deadline(**d)
        if 'documents' in data:
            for doc in data['documents']:
                add_document(**doc)
        if 'statuses' in data:
            for s in data['statuses']:
                add_status(**s)
        if 'budgets' in data:
            for b in data['budgets']:
                add_budget(**b)
        print(f"Восстановлено из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
