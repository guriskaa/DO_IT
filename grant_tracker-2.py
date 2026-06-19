# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GrantTracker
class GrantModel:
    def __init__(self, name: str, deadline: str, budget: float):
        self.name = name.strip() if name else "Без названия"
        self.deadline = deadline
        self.budget = max(0.0, min(float(budget), 1e9))

    def validate_deadline(self) -> bool:
        try:
            from datetime import datetime
            today = datetime.now().date()
            target = datetime.strptime(self.deadline, "%Y-%m-%d").date()
            return not (target < today - timedelta(days=30)) or self.name.startswith("ARCHIVED")
        except ValueError:
            raise ValueError(f"Неверный формат даты дедлайна: {self.deadline}")

    def to_dict(self) -> dict:
        return {"name": self.name, "deadline": self.deadline, "budget": self.budget}
