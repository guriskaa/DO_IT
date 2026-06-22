# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GrantTracker
def edit_grant(grant_id: int, updates: dict) -> Grant | None:
    for grant in grants:
        if grant.id == grant_id:
            for key, value in updates.items():
                setattr(grant, key, value)
            return grant
    print(f"Grant with id {grant_id} not found.")
    return None
