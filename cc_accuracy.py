"""Score ClaimCoach denial-letter reading on the golden set. Used by accuracy_gate before a deploy."""

from __future__ import annotations

import json
import logging
from datetime import date
from pathlib import Path

import appeal_rules
import cc_extract
import config

log = logging.getLogger(__name__)

MIME_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".pdf": "application/pdf"}
REAL_SUBDIR = "real"  # real letters live here, git-ignored, with their own expected.jsonl


def golden_paths() -> list[Path]:
    """expected.jsonl of the synthetic set, plus the real set when it exists."""
    root = Path(config.CC_GOLDEN_DIR)
    return [path for path in (root / "expected.jsonl", root / REAL_SUBDIR / "expected.jsonl") if path.exists()]


def load_cases(paths: list[Path]) -> list[dict]:
    """Every expected line, with the letter's path added as `path`."""
    cases = []
    for expected_path in paths:
        for line in expected_path.read_text().splitlines():
            if line.strip():
                case = json.loads(line)
                case["path"] = expected_path.parent / case["file"]
                cases.append(case)
    return cases


def _claim(value) -> str:
    return "".join(str(value or "").split()).upper()


def _extract(case: dict) -> dict:
    path = case["path"]
    try:
        return cc_extract.read_denial_letter([(path.read_bytes(), MIME_TYPES[path.suffix.lower()])])
    except Exception:
        log.exception("Golden set: could not read %s", case["file"])
        return {}


def _file_by(case: dict, extracted: dict) -> date | None:
    notice = extracted.get("notice_date")
    notice_date = date.fromisoformat(notice) if notice else None
    return appeal_rules.route(case["plan_type"], "post_service", notice_date, cc_extract.printed_deadline(extracted))["file_by"]


def score(expected_path: str | None = None) -> dict:
    """Read every letter and compare. Accuracies are exact-match shares; `late` lists cases whose file-by date is too late."""
    cases = load_cases([Path(expected_path)] if expected_path else golden_paths())
    hits = dict.fromkeys(("claim_number", "notice_date", "printed_deadline"), 0)
    late = []
    for case in cases:
        extracted = _extract(case)
        deadline = cc_extract.printed_deadline(extracted)
        hits["claim_number"] += _claim(extracted.get("claim_number")) == _claim(case["claim_number"])
        hits["notice_date"] += extracted.get("notice_date") == case["notice_date"]
        hits["printed_deadline"] += (deadline.isoformat() if deadline else None) == case["printed_deadline"]
        file_by = _file_by(case, extracted)
        if case["printed_deadline"] and file_by and file_by.isoformat() > case["printed_deadline"]:
            late.append(f"{case['file']}: file_by {file_by.isoformat()} is later than the printed deadline {case['printed_deadline']}")
    total = len(cases)
    return {"cases": total, "late": late, **{field: count / total if total else 0.0 for field, count in hits.items()}}


def cc_gate() -> list[str]:
    """Failure messages (empty = pass or skipped). Skips without a Gemini key or with too few golden cases."""
    if not config.GEMINI_API_KEY or len(load_cases(golden_paths())) < config.CC_GOLDEN_MIN_CASES:
        return []
    result = score()
    failures = [
        f"cc_golden: {field} accuracy {result[field]:.2f} is below {config.CC_GOLDEN_MIN_ACCURACY}"
        for field in ("claim_number", "notice_date", "printed_deadline")
        if result[field] < config.CC_GOLDEN_MIN_ACCURACY
    ]
    return failures + [f"cc_golden: {message}" for message in result["late"]]
