# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GrantTracker
APP_CONFIG = {
    "app_name": "GrantTracker",
    "version": "0.29",
    "db_path": "grants.db",
    "max_budget_per_applicant": 10_000,
    "default_status": "pending",
    "allowed_statuses": ["pending", "under_review", "approved", "rejected"],
}


def get_config(key: str = None) -> dict | str:
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key, f"Unknown config key '{key}'")
