# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GrantTracker
import copy

def simulate_changes(changes, data, dry_run=False):
    """
    Выполняет операции изменения данных. Если dry_run=True,
    операции выполняются в копии данных, оригинал не меняется.
    Возвращает результат операции и обновлённые данные.
    """
    if dry_run:
        data = copy.deepcopy(data)
    for op, target, value in changes:
        if op == "add":
            data[target].append(value)
        elif op == "remove":
            if target in data and value in data[target]:
                data[target].remove(value)
            else:
                return {"status": "error", "message": f"remove failed: {target}={value} not found"}
        elif op == "update":
            data[target] = value
        elif op == "set":
            if target not in data:
                data[target] = []
            data[target].append(value)
    return {"status": "ok", "data": data}
