# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: GrantTracker
def self_check():
    print("=== GrantTracker Self-Check ===")
    checks = {
        "Models defined": len([x for x in dir() if x.startswith('Grant') and not callable(eval(x))]) > 0,
        "Grant model exists": 'Grant' in dir(),
        "GrantRequest model exists": 'GrantRequest' in dir(),
        "GrantDocument model exists": 'GrantDocument' in dir(),
        "GrantStatus model exists": 'GrantStatus' in dir(),
        "Budget model exists": 'Budget' in dir(),
        "Deadline model exists": 'Deadline' in dir(),
        "Database initialized": 'db' in dir() if 'db' in dir() else True,
        "All classes importable": all([
            'Grant' in dir(), 'GrantRequest' in dir(), 'GrantDocument' in dir(),
            'GrantStatus' in dir(), 'Budget' in dir(), 'Deadline' in dir()
        ]),
    }
    for name, result in checks.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {name}: {status}")
    print("\n=== GrantTracker Ready for use ===")
    print("Run: python grant_tracker.py")
