# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GrantTracker
import unittest


class TestGrantTracker(unittest.TestCase):
    def setUp(self):
        from grant_tracker import GrantTracker
        self.gt = GrantTracker()

    def test_create_grant(self):
        g = self.gt.create_grant("G001", "AI Research", "2025-03-31", 10000)
        self.assertEqual(g.id, "G001")
        self.assertEqual(g.status, "draft")

    def test_add_funding_round(self):
        g = self.gt.create_grant("G002", "Bio Lab", "2025-06-30", 5000)
        self.gt.add_funding_round(g, "seed", 2000)
        self.assertEqual(g.funding_rounds[0].amount, 2000)

    def test_add_applicant(self):
        g = self.gt.create_grant("G003", "Eco Study", "2025-01-15", 3000)
        self.gt.add_applicant(g, "Applicant A", "a@b.com")
        self.assertEqual(len(g.applicants), 1)

    def test_add_document(self):
        g = self.gt.create_grant("G004", "Tech Project", "2025-09-30", 7500)
        self.gt.add_document(g, "proposal.pdf", "Proposal doc")
        self.assertEqual(g.documents[0].name, "proposal.pdf")

    def test_update_status(self):
        g = self.gt.create_grant("G005", "Math Study", "2025-04-30", 4000)
        self.gt.update_status(g, "submitted")
        self.assertEqual(g.status, "submitted")

    def test_add_deadline(self):
        g = self.gt.create_grant("G006", "Physics Lab", "2025-02-28", 6000)
        self.gt.add_deadline(g, "review_due", "2025-02-15")
        self.assertEqual(len(g.deadlines), 1)

    def test_add_budget_item(self):
        g = self.gt.create_grant("G007", "Chem Lab", "2025-05-31", 8000)
        self.gt.add_budget_item(g, "equipment", 1500)
        self.assertEqual(g.budget[0].name, "equipment")

    def test_get_summary(self):
        g = self.gt.create_grant("G008", "Summary Test", "2025-07-31", 9000)
        self.gt.add_funding_round(g, "initial", 3000)
        self.gt.add_applicant(g, "User X", "x@y.com")
        self.gt.update_status(g, "review")
        summary = self.gt.get_grant_summary(g)
        self.assertEqual(summary["status"], "review")
        self.assertEqual(summary["total_funding"], 3000)
        self.assertEqual(len(summary["applicants"]), 1)


if __name__ == "__main__":
    unittest.main()
