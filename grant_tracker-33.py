# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GrantTracker
# grant_tracker v0.33 - Added undo mechanism for the last action

class GrantTracker:
    def __init__(self):
        self.applications = []
        self.deadlines = []
        self.documents = []
        self.statuses = []
        self.budget = []
        self.undo_stack = []

    def add_application(self, title, description, amount, deadline, status="pending"):
        application = {
            "title": title,
            "description": description,
            "amount": amount,
            "deadline": deadline,
            "status": status
        }
        self.applications.append(application)
        self.undo_stack.append("add_application")
        return application

    def add_deadline(self, date, title, description):
        deadline = {
            "date": date,
            "title": title,
            "description": description
        }
        self.deadlines.append(deadline)
        self.undo_stack.append("add_deadline")
        return deadline

    def add_document(self, name, url, application_id, deadline_id):
        document = {
            "name": name,
            "url": url,
            "application_id": application_id,
            "deadline_id": deadline_id
        }
        self.documents.append(document)
        self.undo_stack.append("add_document")
        return document

    def add_status(self, name, description):
        status = {
            "name": name,
            "description": description
        }
        self.statuses.append(status)
        self.undo_stack.append("add_status")
        return status

    def add_budget(self, amount, title, description):
        budget = {
            "amount": amount,
            "title": title,
            "description": description
        }
        self.budget.append(budget)
        self.undo_stack.append("add_budget")
        return budget

    def undo(self):
        if not self.undo_stack:
            print("No action to undo.")
            return
        action = self.undo_stack.pop()
        if action == "add_application":
            self.applications.pop()
        elif action == "add_deadline":
            self.deadlines.pop()
        elif action == "add_document":
            self.documents.pop()
        elif action == "add_status":
            self.statuses.pop()
        elif action == "add_budget":
            self.budget.pop()
        print(f"Successfully undone {action}.")

    def get_all_applications(self):
        return self.applications

    def get_all_deadlines(self):
        return self.deadlines

    def get_all_documents(self):
        return self.documents

    def get_all_statuses(self):
        return self.statuses

    def get_all_budget(self):
        return self.budget
