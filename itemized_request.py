"""Itemized-bill requests: find a hospital's billing contact, write the request letter,
and remember when to remind the patient that the hospital's response is due."""

from __future__ import annotations

import re
from datetime import date, timedelta

import config
from db import get_db
from hospital_seo import _display_city, _display_name

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_FIELD_MAX_CHARS = 300

_CONTACT_SQL = """
    SELECT facility_id, name, address, city, state, zip, phone, slug, state_slug, city_slug
    FROM hospitals
"""


def _contact(row) -> dict:
    item = dict(row)
    item["name"] = _display_name(item["name"], item["facility_id"])
    item["city"] = _display_city(item["city"])
    return item


def find_billing_contacts(query: str) -> list[dict]:
    """Hospitals whose name or city matches, with the address and phone a letter needs."""
    q = (query or "").strip()
    if len(q) < 2:
        return []
    like = f"%{q}%"
    with get_db() as db:
        rows = db.execute(
            _CONTACT_SQL + """
            WHERE name LIKE ? OR city LIKE ?
            ORDER BY CASE WHEN lower(name) LIKE lower(?) THEN 0 ELSE 1 END, name
            LIMIT ?
            """,
            (like, like, f"{q}%", config.ITEMIZED_LOOKUP_LIMIT),
        ).fetchall()
    return [_contact(row) for row in rows]


def get_billing_contact(facility_id: str) -> dict | None:
    with get_db() as db:
        row = db.execute(_CONTACT_SQL + " WHERE facility_id = ?", (facility_id,)).fetchone()
    return _contact(row) if row else None


def _clean(payload: dict, key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        return ""
    return value.strip()[:_FIELD_MAX_CHARS]


def validate_letter_request(payload: dict) -> list[str]:
    """Problems that stop a letter from being written, in the user's terms."""
    problems = []
    if not _clean(payload, "your_name"):
        problems.append("Add your name.")
    if not _clean(payload, "your_address"):
        problems.append("Add your mailing address so the hospital knows where to send the bill.")
    if not _clean(payload, "hospital_name"):
        problems.append("Choose or type the hospital.")
    if not (_clean(payload, "account_number") or _clean(payload, "service_dates")):
        problems.append("Add the account number or the date of service so billing can find the account.")
    return problems


def build_request_letter(payload: dict, today: date | None = None) -> dict:
    """Plain-text request letter plus the date the hospital's 30 days run out."""
    today = today or date.today()
    your_name = _clean(payload, "your_name")
    patient = _clean(payload, "patient_name")
    account = _clean(payload, "account_number")
    dates = _clean(payload, "service_dates")
    reply_email = _clean(payload, "reply_email")
    hospital_lines = [
        line for line in (
            _clean(payload, "hospital_name"),
            _clean(payload, "hospital_address"),
            _clean(payload, "hospital_city_line"),
        ) if line
    ]

    reference = [f"Patient: {patient or your_name}"]
    if account:
        reference.append(f"Account number: {account}")
    if dates:
        reference.append(f"Date(s) of service: {dates}")

    on_behalf = (
        f"I am requesting these records on behalf of {patient}. "
        "Please tell me if you need a signed authorization or proof that I am their personal representative.\n\n"
        if patient and patient != your_name else ""
    )
    delivery = f"by email to {reply_email}" if reply_email else "by mail to the address above"
    due = today + timedelta(days=config.ITEMIZED_RESPONSE_DAYS)

    letter = "\n".join([
        f"{today:%B} {today.day}, {today.year}",
        "",
        your_name,
        _clean(payload, "your_address"),
        "",
        "Billing Department",
        *hospital_lines,
        "",
        "Re: Request for an itemized bill",
        *reference,
        "",
        "Dear Billing Department,",
        "",
        "Please send me a complete itemized bill for the account above. For every charge, please include:",
        "",
        "- the date of service",
        "- the CPT or HCPCS code and any modifiers",
        "- the revenue code",
        "- a description of the service or item",
        "- the number of units and the charge per unit",
        "- the NDC number for any drug",
        "",
        "Please also include every payment and adjustment applied to the account, and a copy of the claim "
        "(UB-04) sent to any insurer.",
        "",
        on_behalf + f"These are billing records about {'the patient' if on_behalf else 'me'}. "
        "I am requesting them under the HIPAA right of access "
        "(45 CFR 164.524), which requires a response within 30 days of receiving this request. "
        f"Please send them {delivery}.",
        "",
        "While I review the itemized bill, please put the account on hold and do not send it to a collection "
        "agency or report it to a credit bureau.",
        "",
        "Thank you,",
        "",
        your_name,
    ])
    return {"letter": letter, "response_due": due.isoformat()}


def save_reminder(email: str, hospital_name: str, sent_on: date | None = None) -> str:
    """Store one reminder for the day the hospital's response is due. Returns that date."""
    email = (email or "").strip()
    if not _EMAIL_RE.match(email):
        raise ValueError("Enter a valid email address.")
    hospital_name = (hospital_name or "").strip()[:_FIELD_MAX_CHARS]
    if not hospital_name:
        raise ValueError("Choose the hospital first.")
    remind_on = (sent_on or date.today()) + timedelta(days=config.ITEMIZED_RESPONSE_DAYS)
    with get_db() as db:
        db.execute(
            "INSERT INTO itemized_requests (email, hospital_name, remind_on) VALUES (?, ?, ?)",
            (email, hospital_name, remind_on.isoformat()),
        )
    return remind_on.isoformat()


def due_reminders(today: date) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT id, email, hospital_name, remind_on FROM itemized_requests "
            "WHERE remind_on <= ? AND reminded_at IS NULL ORDER BY id",
            (today.isoformat(),),
        ).fetchall()
    return [dict(row) for row in rows]


def mark_reminded(request_id: int) -> None:
    with get_db() as db:
        db.execute("UPDATE itemized_requests SET reminded_at = CURRENT_TIMESTAMP WHERE id = ?", (request_id,))
