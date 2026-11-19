"""Weekly scan-quality numbers: how often a scan needs the user, and how often the user changes what we read."""

from __future__ import annotations

import json

import code_lookup
import config
from accuracy_gate import measure
from db import get_db


def weekly_numbers() -> dict:
    window = f"-{config.OCR_QUALITY_WINDOW_DAYS} days"
    with get_db() as db:
        scans = db.execute("SELECT COUNT(*) FROM bills WHERE created_at >= datetime('now', ?)", (window,)).fetchone()[0]
        asked = db.execute(
            "SELECT COUNT(DISTINCT bill_id) FROM extraction_corrections WHERE created_at >= datetime('now', ?) "
            "AND issue_kind != 'web_edit'", (window,)).fetchone()[0]
        confirmed = db.execute(
            "SELECT COUNT(*) FROM extraction_corrections WHERE created_at >= datetime('now', ?) AND issue_kind != 'web_edit'",
            (window,)).fetchone()[0]
        changed = db.execute(
            "SELECT COUNT(*) FROM extraction_corrections WHERE created_at >= datetime('now', ?) AND issue_kind != 'web_edit' "
            "AND extracted_value != confirmed_value", (window,)).fetchone()[0]
    by_kind = {}
    with get_db() as db:
        for kind in config.INPUT_KINDS:
            total = db.execute("SELECT COUNT(*) FROM bills WHERE input_kind = ? AND created_at >= datetime('now', ?)", (kind, window)).fetchone()[0]
            asked_kind = db.execute("SELECT COUNT(DISTINCT c.bill_id) FROM extraction_corrections c JOIN bills b ON b.id = c.bill_id "
                                    "WHERE b.input_kind = ? AND c.created_at >= datetime('now', ?) AND c.issue_kind != 'web_edit'", (kind, window)).fetchone()[0]
            by_kind[kind] = {"scans": total, "share_needing_confirmation": round(asked_kind / total, 4) if total else None}
    return {
        "by_input_kind": by_kind,
        **{f"code_{key}": value for key, value in code_lookup.coverage().items()},
        "scans": scans,
        "share_of_scans_needing_confirmation": round(asked / scans, 4) if scans else None,
        # The real-world error rate: of the lines users confirmed, how many they had to change.
        "share_of_confirmed_lines_changed": round(changed / confirmed, 4) if confirmed else None,
    }


def record_weekly() -> int:
    """Save this week's numbers (plus the benchmark accuracy) as a data_quality_runs row. Once per window."""
    with get_db() as db:
        recent = db.execute("SELECT 1 FROM data_quality_runs WHERE status = ? AND run_date >= datetime('now', ?)",
                            (config.OCR_QUALITY_RUN_STATUS, f"-{config.OCR_QUALITY_WINDOW_DAYS} days")).fetchone()
        if recent:
            return 0
        numbers = weekly_numbers()
        for name, manifest, _ in config.OCR_GATE_SUITES:
            try:
                numbers[f"{name}_accuracy"] = measure(manifest)
            except FileNotFoundError:
                continue
        db.execute("INSERT INTO data_quality_runs (status, coverage_json, checks_json, notes) VALUES (?, '[]', ?, 'weekly OCR quality')",
                   (config.OCR_QUALITY_RUN_STATUS, json.dumps(numbers)))
    return 1
