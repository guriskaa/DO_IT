# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GrantTracker
def backup_data_file(source_path, backup_dir=None):
    """Создаёт резервную копию данных в архиве с датой."""
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"granttracker_backup_{timestamp}.csv")
    with open(source_path, "r") as src, open(backup_path, "w") as dst:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(reader)
    return backup_path
