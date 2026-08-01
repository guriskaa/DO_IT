# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GrantTracker
class Profile:
    def __init__(self, name: str, role: str = "user"):
        self.name = name
        self.role = role  # user, admin, viewer

    def can_view(self):
        return True

    def can_edit(self):
        return self.role in ("user", "admin")

    def can_manage_users(self):
        return self.role == "admin"


class ProfilesManager:
    _profiles = {}
    _current_profile = None

    @classmethod
    def create(cls, name: str, role: str = "user"):
        cls._profiles[name] = Profile(name, role)
        if not cls._current_profile:
            cls.set_current(name)
        return cls._profiles[name]

    @classmethod
    def set_current(cls, name):
        if name in cls._profiles:
            cls._current_profile = cls._profiles[name]
        else:
            raise ValueError(f"Profile '{name}' does not exist")

    @classmethod
    def get_current(cls) -> Profile | None:
        return cls._current_profile

    @classmethod
    def list_all(cls):
        return dict(cls._profiles)
