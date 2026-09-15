# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GrantTracker
class DataMigration:
    """Миграция структуры данных: добавляет поле version в конфигурацию."""
    
    def __init__(self, config_file="grant_config.json", version=1):
        self.config_file = config_file
        self.version = version
    
    def migrate(self):
        """Выполняет миграцию: добавляет поле version в конфигурацию, если его нет."""
        import json
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
        except FileNotFoundError:
            config = {}
        
        if 'version' not in config:
            config['version'] = self.version
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"Миграция выполнена: версия установлена на {self.version}")
        else:
            print(f"Миграция не нужна: версия уже установлена на {config['version']}")
