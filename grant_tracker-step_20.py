# === Stage 20: Добавь восстановление записей из архива ===
# Project: GrantTracker
def load_archive(path):
    with open(path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            parts = line.split(',')
            if len(parts) != 6: continue
            try:
                deadline = datetime.fromisoformat(parts[1].strip())
            except ValueError:
                deadline = None
            record = Record(
                id=parts[0].strip(),
                applicant=parts[2].strip(),
                title=parts[3].strip(),
                amount=int(parts[4].strip()),
                status=parts[5].strip(),
                deadline=deadline,
            )
            records.append(record)
    print(f"Loaded {len(records)} records from archive")
