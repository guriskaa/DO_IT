# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: GrantTracker
class TestEdgeCasesAndErrors(unittest.TestCase):
    def test_invalid_status_transition(self):
        grant = Grant(id="e1")
        grant.status = "submitted"
        self.assertEqual(grant.status, "submitted")
        with self.assertRaises(ValueError):
            grant.status = "approved"

    def test_budget_exceeds_total(self):
        grant = Grant(id="e2", total_budget=1000)
        with self.assertRaises(ValueError):
            grant.add_budget_item("item", 600)
        grant.add_budget_item("item", 600)
        with self.assertRaises(ValueError):
            grant.add_budget_item("item", 100)

    def test_empty_deadline(self):
        grant = Grant(id="e3")
        deadline = Deadline(grant_id="e3", due_date=None)
        self.assertIsNone(deadline.due_date)
        self.assertFalse(deadline.is_overdue())

    def test_overdue_deadline(self):
        grant = Grant(id="e4")
        deadline = Deadline(grant_id="e4", due_date="2020-01-01")
        self.assertTrue(deadline.is_overdue())

    def test_invalid_document_type(self):
        with self.assertRaises(ValueError):
            Document("e5", "report", "invalid_type")

    def test_invalid_file_extension(self):
        with self.assertRaises(ValueError):
            Document("e5", "report", "invalid.pdf")

    def test_invalid_grant_id(self):
        with self.assertRaises(ValueError):
            Document("invalid_id", "report", "pdf")

    def test_invalid_deadline_grant_id(self):
        with self.assertRaises(ValueError):
            Deadline("invalid_id", "2025-12-31")

    def test_invalid_grant_id_for_deadline(self):
        with self.assertRaises(ValueError):
            Deadline("e6", "2025-12-31")

    def test_invalid_grant_id_for_application(self):
        with self.assertRaises(ValueError):
            Application("e7", "2025-12-31", "submitted")

    def test_invalid_grant_id_for_budget(self):
        with self.assertRaises(ValueError):
            Budget("e8", 5000)

    def test_invalid_grant_id_for_status(self):
        with self.assertRaises(ValueError):
            Status("e9")
