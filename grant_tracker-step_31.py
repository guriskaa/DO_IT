# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GrantTracker
class ProfileManager:
    def __init__(self):
        self._active = None
    
    @property
    def active_profile(self):
        return self._active
    
    def set_active(self, profile_name):
        if not isinstance(profile_name, str) or not profile_name.strip():
            raise ValueError("Profile name must be a non-empty string")
        self._active = Profile(profile_name.strip())
    
    def __repr__(self):
        return f"ProfileManager(active={self._active})"

def main():
    pm = ProfileManager()
    print(f"Active profile: {pm.active_profile}")
    pm.set_active("researcher")
    print(f"After switch: {pm.active_profile}")
