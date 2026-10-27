from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_plan  # noqa: E402


class MiniTestPlanValidatorTests(unittest.TestCase):
    def test_repository_plan_and_artifacts_are_consistent(self) -> None:
        self.assertEqual(validate_plan.validate_plan(), [])
        case_errors, rows = validate_plan.validate_cases()
        self.assertEqual(case_errors, [])
        self.assertEqual(validate_plan.validate_bug_reports(), [])
        self.assertEqual(validate_plan.validate_report(rows), [])
        self.assertEqual(len(rows), 10)

    def test_rejects_duplicate_case_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.csv"
            fields = sorted(validate_plan.CASE_COLUMNS)
            row = {
                "id": "TC-001",
                "feature": "Cart",
                "title": "Add product",
                "priority": "P1",
                "precondition": "Product page open",
                "steps": "Add product",
                "expected": "Product appears",
                "status": "Not executed",
            }
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerow(row)
                writer.writerow(row)
            with patch.object(validate_plan, "CASES_PATH", path):
                errors, _ = validate_plan.validate_cases()

        self.assertTrue(any("duplicate ID" in error for error in errors))

    def test_rejects_a_report_that_claims_execution_before_testing(self) -> None:
        rows = [{"status": "Not executed"}]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            path.write_text(
                "- Casos diseñados: 1\n- Casos ejecutados: 0\n"
                "Estado global: **PASS**\n",
                encoding="utf-8",
            )
            with patch.object(validate_plan, "REPORT_PATH", path):
                errors = validate_plan.validate_report(rows)

        self.assertTrue(any("No evaluado" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
