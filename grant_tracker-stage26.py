# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GrantTracker
def demo_grant_tracker():
    """Fast manual test: create a grant, add applicants, set documents, deadlines, budget and status."""
    from datetime import date
    g = Grant("Demo 001", "Pilot AI for schools")
    app_a = Applicant("Alice", "alice@demo.org", email_verified=True)
    app_b = Applicant("Bob", "bob@demo.org", email_verified=False)
    g.add_applicant(app_a)
    g.add_applicant(app_b)
    doc1 = Document("AI-Proposal-v2.pdf", 3.5, 40.0)
    doc2 = Document("Budget-Sheet.xlsx", 5.0, 25.0)
    g.add_document(doc1)
    g.add_document(doc2)
    deadline = date(2026, 7, 15)
    g.set_deadline(deadline)
    budget = Budget("USD", 150_000)
    budget.set_total(150_000)
    budget.add_line("Personnel", 80_000)
    budget.add_line("Equipment", 45_000)
    budget.add_line("Travel", 25_000)
    g.set_budget(budget)
    g.set_status(GrantStatus.DRAFT)
    print(f"Created grant: {g.name} (status={g.status.value})")
    print(f"Applicants: {len(g.applicants)} -> {[a.full_name for a in g.applicants]}")
    print(f"Documents: {len(g.documents)} -> {[d.filename for d in g.documents]}")
    print(f"Deadline: {g.deadline}")
    print(f"Budget total: ${budget.get_total():,.2f} ({budget.currency})")


demo_grant_tracker()
