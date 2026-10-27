"""Validate the mini test plan and its supporting QA artifacts."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "02-plan" / "test-plan.md"
CASES_PATH = ROOT / "03-work" / "test-cases.csv"
BUG_DIR = ROOT / "03-work" / "bug-reports"
REPORT_PATH = ROOT / "05-results" / "report.md"
PLAN_SECTIONS = (
    "## 1. Objetivo",
    "## 2. Sistema y ambiente",
    "## 3. Estrategia",
    "## 4. Alcance",
    "## 5. Datos de prueba",
    "## 6. Riesgos y mitigación",
    "## 7. Entrada",
    "## 8. Salida",
    "## 9. Entregables",
    "## 10. Estado actual",
)
CASE_COLUMNS = {
    "id", "feature", "title", "priority", "precondition", "steps", "expected", "status"
}
STATUSES = {"Not executed", "Pass", "Fail", "Blocked", "Not applicable"}
PRIORITIES = {"P0", "P1", "P2", "P3"}


def validate_plan() -> list[str]:
    if not PLAN_PATH.is_file():
        return ["Test plan is missing."]
    content = PLAN_PATH.read_text(encoding="utf-8")
    return [f"Test plan is missing section: {section}" for section in PLAN_SECTIONS if section not in content]


def validate_cases() -> tuple[list[str], list[dict[str, str]]]:
    try:
        with CASES_PATH.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            columns = set(reader.fieldnames or [])
            if not CASE_COLUMNS.issubset(columns):
                return [f"CSV is missing columns: {', '.join(sorted(CASE_COLUMNS - columns))}"], []
            rows = list(reader)
    except OSError as error:
        return [f"Unable to read test cases: {error}"], []

    errors: list[str] = []
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        case_id = (row.get("id") or "").strip()
        if not case_id or case_id in seen:
            errors.append(f"CSV line {line}: missing or duplicate ID {case_id!r}.")
        seen.add(case_id)
        if (row.get("priority") or "").strip() not in PRIORITIES:
            errors.append(f"CSV line {line}: invalid priority.")
        if (row.get("status") or "").strip() not in STATUSES:
            errors.append(f"CSV line {line}: invalid status.")
        for field in ("feature", "title", "precondition", "steps", "expected"):
            if not (row.get(field) or "").strip():
                errors.append(f"CSV line {line}: {field} is empty.")
        if (row.get("title") or "").strip().lower().startswith("validar escenario"):
            errors.append(f"CSV line {line}: generic placeholder remains.")
    if not rows:
        errors.append("CSV contains no test cases.")
    return errors, rows


def validate_bug_reports() -> list[str]:
    errors: list[str] = []
    reports = sorted(BUG_DIR.glob("BR-*.md"))
    if not reports:
        return ["No sample bug reports found."]
    for path in reports:
        content = path.read_text(encoding="utf-8")
        if path.stem not in content:
            errors.append(f"{path.name}: ID does not match filename.")
        if not re.search(r"\*\*Estado:\*\*\s*\S", content):
            errors.append(f"{path.name}: verification status is missing.")
        if "no confirmado" not in content.lower():
            errors.append(f"{path.name}: sample finding must be labelled unverified.")
    return errors


def validate_report(rows: list[dict[str, str]]) -> list[str]:
    if not REPORT_PATH.is_file():
        return ["Results report is missing."]
    report = REPORT_PATH.read_text(encoding="utf-8")
    executed = sum(
        (row.get("status") or "").strip() not in {"Not executed", "Not applicable"}
        for row in rows
    )
    errors: list[str] = []
    if f"- Casos diseñados: {len(rows)}" not in report:
        errors.append("Results report case count does not match the CSV.")
    if f"- Casos ejecutados: {executed}" not in report:
        errors.append("Results report execution count does not match the CSV.")
    if executed == 0 and "Estado global: **No evaluado**" not in report:
        errors.append("Results report must remain No evaluado until cases are executed.")
    return errors


def main() -> int:
    errors = validate_plan()
    case_errors, rows = validate_cases()
    errors.extend(case_errors)
    errors.extend(validate_bug_reports())
    errors.extend(validate_report(rows))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated plan, {len(rows)} cases, {len(list(BUG_DIR.glob('BR-*.md')))} bug reports, and results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
