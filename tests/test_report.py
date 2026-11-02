import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from report import build_report

class SalesReportTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "deals": [
                {"name":"Example A","stage":"proposal","value_gbp":20000,"days_since_activity":9},
                {"name":"Example B","stage":"won","value_gbp":99000,"days_since_activity":1},
                {"name":"Example C","stage":"lost","value_gbp":11000,"days_since_activity":2},
                {"name":"Example D","stage":"discovery","value_gbp":7000,"days_since_activity":2},
            ],
            "leads": [{"name":"Lead A","days_since_activity":6},{"name":"Lead B","days_since_activity":1}],
            "reps": [{"name":"Alex","calls":10,"emails":8,"meetings":4}],
        }

    def test_excludes_closed_deals_from_pipeline(self):
        report = build_report(self.data)
        self.assertIn("Open pipeline: £27,000", report)
        self.assertIn("Open opportunities: 2", report)

    def test_flags_stale_open_deals(self):
        report = build_report(self.data)
        self.assertIn("Deals needing attention: 1", report)
        self.assertIn("Example A", report)
        self.assertNotIn("Example B", report)

    def test_flags_leads_without_recent_activity(self):
        report = build_report(self.data)
        self.assertIn("Leads needing follow-up: 1", report)
        self.assertIn("Lead A", report)
        self.assertNotIn("Lead B", report)

    def test_rep_activity_summary(self):
        report = build_report(self.data)
        self.assertIn("Alex: 10 calls, 8 emails, 4 meetings", report)

if __name__ == "__main__":
    unittest.main()
