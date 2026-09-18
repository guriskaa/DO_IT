# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: GrantTracker
def _validate_grant(grant):
    if not isinstance(grant, dict):
        raise TypeError("grant must be a dict")
    required = ["id", "title", "status", "deadline"]
    for key in required:
        if key not in grant:
            raise KeyError(f"missing required field: {key}")
    if grant["status"] not in GRANT_STATUSES:
        raise ValueError(f"invalid status: {grant['status']}")
    if not isinstance(grant["deadline"], datetime.datetime):
        raise TypeError("deadline must be a datetime")
    if grant["deadline"] <= datetime.datetime.now(datetime.timezone.utc):
        raise ValueError("deadline must be in the future")
    return grant

def _validate_application(app):
    if not isinstance(app, dict):
        raise TypeError("app must be a dict")
    required = ["grant_id", "applicant", "amount"]
    for key in required:
        if key not in app:
            raise KeyError(f"missing required field: {key}")
    if not isinstance(app["applicant"], str) or not app["applicant"].strip():
        raise ValueError("applicant name must be a non-empty string")
    if not isinstance(app["amount"], (int, float)) or app["amount"] <= 0:
        raise ValueError("amount must be a positive number")
    return app
