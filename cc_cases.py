"""ClaimCoach case storage and state. Every case belongs to one anonymous device."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta

from fastapi import HTTPException

import appeal_rules
import cc_extract
import config
from appeal_letter import DENIAL_REASONS, PLAN_TYPES, SERVICE_TIMINGS
from db import get_db

EXTRACTED_FIELDS = ("insurer_name", "claim_number", "service_description", "notice_date", "printed_appeal_deadline")
DATE_FIELDS = ("notice_date", "printed_appeal_deadline")
CHOICE_FIELDS = {"denial_reason": DENIAL_REASONS, "plan_type": PLAN_TYPES, "service_timing": SERVICE_TIMINGS}
SEND_TO_FIELDS = {"send_to_address": "appeal_address", "send_to_fax": "appeal_fax", "send_to_phone": "appeal_phone"}


def _case_from_row(row) -> dict:
    case = dict(row)
    case["extracted"] = json.loads(case.pop("extracted_json") or "{}")
    case["needs_confirmation"] = json.loads(case["needs_confirmation"] or "[]")
    return case


def create_case(device_id: str, for_whom: str, extracted: dict, plan_type: str, service_timing: str,
                reason_key: str, plain_reason: str, confirm: list[str]) -> int:
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO cc_cases (device_id, for_whom, plan_type, service_timing, denial_reason, extracted_json, "
            "schema_version, notice_date, amount_denied, plain_reason, needs_confirmation, updated_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)",
            (device_id, for_whom, plan_type, service_timing, reason_key, json.dumps(extracted),
             extracted.get("schema_version"), extracted.get("notice_date"), extracted.get("amount_denied"),
             plain_reason, json.dumps(confirm)),
        )
        return cursor.lastrowid


def get_case(case_id: int) -> dict | None:
    with get_db() as db:
        row = db.execute("SELECT * FROM cc_cases WHERE id = ?", (case_id,)).fetchone()
    return _case_from_row(row) if row else None


def require_case(device_id: str, case_id: int) -> dict:
    case = get_case(case_id)
    if not case:
        raise HTTPException(404, "Case not found")
    if case["device_id"] != device_id:
        raise HTTPException(403, "Access denied for this case")
    return case


def list_cases(device_id: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM cc_cases WHERE device_id = ? ORDER BY created_at DESC, id DESC", (device_id,)
        ).fetchall()
    return [_case_from_row(row) for row in rows]


def clean_text(name: str, value, limit: int) -> str:
    """Trimmed text of 1 to `limit` characters, or a 400."""
    text = value.strip() if isinstance(value, str) else ""
    if not text or len(text) > limit:
        raise HTTPException(400, f"{name} must be text of 1 to {limit} characters")
    return text


def _clean_extracted_value(name: str, value) -> str:
    text = clean_text(name, value, config.CC_CONFIRMED_FIELD_MAX_CHARS)
    if name in DATE_FIELDS:
        try:
            return date.fromisoformat(text).isoformat()
        except ValueError as exc:
            raise HTTPException(400, f"{name} must be a date like 2026-10-12") from exc
    return text


def update_confirmed(case: dict, fields: dict) -> None:
    """Apply what the user confirmed or corrected. No fields at all means "Looks right"."""
    extracted = dict(case["extracted"])
    choices = {name: case[name] for name in CHOICE_FIELDS}
    confirmed = set()
    for name, value in fields.items():
        if name == "printed_appeal_deadline" and value in (None, ""):
            extracted.pop("printed_appeal_deadline", None)  # "Not on my letter": drop the date and any window counted from it
            extracted.pop("printed_appeal_window_text", None)
        elif name in SEND_TO_FIELDS:
            if value in (None, ""):
                extracted.pop(SEND_TO_FIELDS[name], None)
            else:
                extracted[SEND_TO_FIELDS[name]] = clean_text(name, value, config.CC_SEND_TO_MAX_CHARS)
            continue  # where the appeal goes is not one of the fields the user was asked to confirm
        elif name in EXTRACTED_FIELDS:
            extracted[name] = _clean_extracted_value(name, value)
        elif name in CHOICE_FIELDS:
            if value not in CHOICE_FIELDS[name]:
                raise HTTPException(400, f"Unknown value for {name}")
            choices[name] = value
        else:
            continue
        confirmed.add(name)
    remaining = [name for name in case["needs_confirmation"] if confirmed and name not in confirmed]
    with get_db() as db:
        db.execute(
            "UPDATE cc_cases SET extracted_json = ?, notice_date = ?, denial_reason = ?, plan_type = ?, "
            "service_timing = ?, needs_confirmation = ?, status = CASE WHEN status = 'draft' THEN 'ready' ELSE status END, "
            "updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (json.dumps(extracted), extracted.get("notice_date"), choices["denial_reason"], choices["plan_type"],
             choices["service_timing"], json.dumps(remaining), case["id"]),
        )
    reroute(case["id"])


def reroute(case_id: int) -> None:
    """Recompute level, file-by date and where the date came from."""
    case = get_case(case_id)
    notice = date.fromisoformat(case["notice_date"]) if case["notice_date"] else None
    route = appeal_rules.route(case["plan_type"], case["service_timing"], notice, cc_extract.printed_deadline(case["extracted"]))
    with get_db() as db:
        db.execute(
            "UPDATE cc_cases SET level = ?, file_by = ?, deadline_source = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (route["level"], route["file_by"].isoformat() if route["file_by"] else None, route["deadline_source"], case_id),
        )


def record_sent(case: dict, channel: str, sent_on: date) -> None:
    due = appeal_rules.decision_due(case["plan_type"], case["service_timing"], sent_on)
    with get_db() as db:
        db.execute(
            "UPDATE cc_cases SET status = 'sent', sent_at = ?, sent_channel = ?, decision_due = ?, "
            "updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (sent_on.isoformat(), channel, due.isoformat() if due else None, case["id"]),
        )


def parse_decision_letter_date(value, case: dict) -> date | None:
    """The date on the insurer's decision letter: a real date, not in the future, not before the denial notice."""
    if value in (None, ""):
        return None
    try:
        decided = date.fromisoformat(str(value))
    except ValueError as exc:
        raise HTTPException(400, "decision_letter_date must be a date like 2026-10-12") from exc
    if decided > date.today():
        raise HTTPException(400, "decision_letter_date can't be in the future")
    if case["notice_date"] and decided < date.fromisoformat(case["notice_date"]):
        raise HTTPException(400, "decision_letter_date can't be before the denial notice")
    return decided


def record_outcome(case: dict, outcome: str, amount_recovered: float | None, decision_letter_date: date | None) -> None:
    with get_db() as db:
        db.execute(
            "UPDATE cc_cases SET status = 'decided', outcome = ?, amount_recovered = ?, decided_at = ?, "
            "decision_letter_date = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (outcome, amount_recovered, date.today().isoformat(),
             decision_letter_date.isoformat() if decision_letter_date else None, case["id"]),
        )


def save_letter(case_id: int, letter_text: str, case_paragraph: str | None = None, first_level: bool = True) -> None:
    """Keep the last generated letter. A next-level letter leaves the round-one personal paragraph in place."""
    with get_db() as db:
        db.execute(
            "UPDATE cc_cases SET letter_text = ?, case_paragraph = CASE WHEN ? THEN ? ELSE case_paragraph END, "
            "updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (letter_text, first_level, case_paragraph, case_id),
        )


def letter_case(case: dict, name: str, member_id: str, details: dict | None = None) -> dict:
    """The case in the shape appeal_letter.build_appeal_letter and appeal_kit expect.
    `details` are the optional letter-form fields the user typed (see cc_case_routes.letter_details)."""
    details = details or {}
    extracted = case["extracted"]
    route = appeal_rules.route(case["plan_type"], case["service_timing"], None, None)
    return {
        "patient_name": details.get("patient_name") or name,
        "representative_name": details.get("representative_name"),
        "relationship": details.get("relationship"),
        "for_whom": case["for_whom"],
        "member_id": member_id or extracted.get("member_id"),
        "claim_number": extracted.get("claim_number"),
        "provider_name": extracted.get("provider_name"),
        "service_description": extracted.get("service_description"),
        "service_date": extracted.get("service_date"),
        "insurer_name": extracted.get("insurer_name") or "[INSURER NAME]",
        "denial_date": case["notice_date"] or "[DATE OF DENIAL]",
        "amount_denied": case["amount_denied"],
        "insurer_appeal_address": extracted.get("appeal_address"),
        "insurer_appeal_fax": extracted.get("appeal_fax"),
        "denial_reason_text": extracted.get("denial_reason_text"),
        "criteria_cited": extracted.get("criteria_cited"),
        "service_timing": case["service_timing"],
        "denial_reason": case["denial_reason"],
        "plan_type": case["plan_type"],
        "level_label": route["level_label"],
        "file_by": case["file_by"],
        "deadline_source": case["deadline_source"],
        "case_paragraph": case["case_paragraph"],
        "decision_letter_date": details.get("decision_letter_date") or case["decision_letter_date"],
        "next_level_address": details.get("next_level_address"),
        "mailing_address": details.get("mailing_address"),
        "phone": details.get("phone"),
        "has_doctor_letter": details.get("has_doctor_letter", False),
        "email": None,
    }


def delete_case(case_id: int) -> None:
    with get_db() as db:
        db.execute("DELETE FROM cc_sends WHERE case_id = ?", (case_id,))
        db.execute("DELETE FROM cc_case_unlocks WHERE case_id = ?", (case_id,))
        db.execute("DELETE FROM cc_cases WHERE id = ?", (case_id,))


def delete_device_cases(device_id: str) -> None:
    with get_db() as db:
        case_ids = [row["id"] for row in db.execute("SELECT id FROM cc_cases WHERE device_id = ?", (device_id,)).fetchall()]
    for case_id in case_ids:
        delete_case(case_id)


def purge_old(days: int) -> int:
    """Delete cases created before the cutoff, with their unlocks and sends. Returns how many."""
    cutoff = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    with get_db() as db:
        case_ids = [row["id"] for row in db.execute("SELECT id FROM cc_cases WHERE created_at < ?", (cutoff,)).fetchall()]
    for case_id in case_ids:
        delete_case(case_id)
    return len(case_ids)
