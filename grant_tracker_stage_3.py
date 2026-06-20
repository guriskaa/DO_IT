# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GrantTracker
class GrantTracker:
    def __init__(self):
        self.records = []

    def add_application(self, name, deadline, budget, status="draft", documents=None):
        record = {
            "id": len(self.records) + 1,
            "name": name,
            "deadline": deadline,
            "budget": float(budget),
            "status": status,
            "documents": documents or []
        }
        self.records.append(record)
        return record

    def add_document(self, app_id, filename):
        for rec in self.records:
            if rec["id"] == app_id and filename not in [d.get("name") for d in rec["documents"]]:
                rec["documents"].append({"name": filename})
                return True
        return False

    def update_status(self, app_id, new_status):
        for rec in self.records:
            if rec["id"] == app_id:
                rec["status"] = new_status
                return True
        return False
