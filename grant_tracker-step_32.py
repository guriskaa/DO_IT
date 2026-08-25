# === Stage 32: Добавь журнал действий пользователя ===
# Project: GrantTracker
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, user, action, target, details=""):
        self._entries.append({
            "user": user,
            "action": action,
            "target": target,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })

    def get_recent(self, count=10):
        return self._entries[-count:]
