"""Concierge denied-claim appeals: intake, payment, letter, approval, sending and outcome."""

import logging
import secrets
from datetime import date, datetime, timedelta
from html import escape

import config
import email_service
from appeal_letter import DENIAL_REASONS, PLAN_TYPES, SERVICE_TIMINGS, build_appeal_letter
from db import get_db
from debt_fighter import send_certified_letter

log = logging.getLogger(__name__)

STATUS_LABELS = {
    "awaiting_payment": "Waiting for payment",
    "drafted": "Draft ready for your review",
    "approved": "Approved, being sent",
    "sent": "Sent to your insurer",
    "decided": "Decision received",
}
OUTCOMES = {"overturned": "Denial overturned", "partial": "Partly overturned", "upheld": "Denial upheld"}


def price_for_amount(amount_denied: float) -> int:
    if amount_denied >= config.APPEAL_LARGE_CLAIM_THRESHOLD:
        return config.APPEAL_PRICE_LARGE_CENTS
    return config.APPEAL_PRICE_CENTS


def validate_intake(form: dict) -> list[str]:
    """Return the problems with an intake form; an empty list means it can be saved."""
    errors = []
    for field, label in (
        ("patient_name", "Your name"),
        ("email", "Email"),
        ("insurer_name", "Insurance company"),
        ("authorization_name", "Your typed name authorizing us"),
    ):
        if not (form.get(field) or "").strip():
            errors.append(f"{label} is required.")
    if "@" not in (form.get("email") or ""):
        errors.append("Enter a valid email.")
    if form.get("denial_reason") not in DENIAL_REASONS:
        errors.append("Choose the reason the claim was denied.")
    if form.get("plan_type") not in PLAN_TYPES:
        errors.append("Choose your type of plan.")
    if form.get("service_timing") not in SERVICE_TIMINGS:
        errors.append("Tell us whether you already had the care.")
    try:
        denial = date.fromisoformat(form.get("denial_date") or "")
        if denial > date.today():
            errors.append("The denial date can't be in the future.")
    except ValueError:
        errors.append("Enter the date on the denial letter.")
    try:
        if float(form.get("amount_denied") or 0) <= 0:
            errors.append("Enter the amount denied.")
    except ValueError:
        errors.append("Enter the amount denied as a number.")
    return errors


def create_case(form: dict, denial_letter_path: str | None) -> dict:
    """Save a validated intake as a case awaiting payment. Returns the case."""
    amount = float(form["amount_denied"])
    fields = {
        "token": secrets.token_urlsafe(24),
        "patient_name": form["patient_name"].strip(),
        "email": form["email"].strip().lower(),
        "phone": (form.get("phone") or "").strip(),
        "mailing_address": (form.get("mailing_address") or "").strip(),
        "insurer_name": form["insurer_name"].strip(),
        "plan_type": form["plan_type"],
        "member_id": (form.get("member_id") or "").strip(),
        "claim_number": (form.get("claim_number") or "").strip(),
        "provider_name": (form.get("provider_name") or "").strip(),
        "service_description": (form.get("service_description") or "").strip(),
        "service_date": form.get("service_date") or None,
        "denial_date": form["denial_date"],
        "service_timing": form["service_timing"],
        "denial_reason": form["denial_reason"],
        "amount_denied": amount,
        "insurer_appeal_address": (form.get("insurer_appeal_address") or "").strip(),
        "insurer_appeal_fax": (form.get("insurer_appeal_fax") or "").strip(),
        "notes": (form.get("notes") or "").strip(),
        "denial_letter_path": denial_letter_path,
        "authorization_name": form["authorization_name"].strip(),
        "price_cents": price_for_amount(amount),
    }
    columns = ", ".join(fields)
    placeholders = ", ".join("?" for _ in fields)
    with get_db() as db:
        cursor = db.execute(f"INSERT INTO appeal_cases ({columns}) VALUES ({placeholders})", tuple(fields.values()))
        fields["id"] = cursor.lastrowid
    return fields


def get_case(case_id: int) -> dict | None:
    with get_db() as db:
        row = db.execute("SELECT * FROM appeal_cases WHERE id = ?", (case_id,)).fetchone()
    return dict(row) if row else None


def get_case_by_token(token: str) -> dict | None:
    with get_db() as db:
        row = db.execute("SELECT * FROM appeal_cases WHERE token = ?", (token,)).fetchone()
    return dict(row) if row else None


def get_case_by_session(session_id: str) -> dict | None:
    with get_db() as db:
        row = db.execute("SELECT * FROM appeal_cases WHERE stripe_session_id = ?", (session_id,)).fetchone()
    return dict(row) if row else None


def set_checkout_session(case_id: int, session_id: str) -> None:
    with get_db() as db:
        db.execute("UPDATE appeal_cases SET stripe_session_id = ? WHERE id = ?", (session_id, case_id))


def mark_paid(case_id: int) -> bool:
    """Record payment and draft the letter. Returns False if the case was already paid (safe to repeat)."""
    case = get_case(case_id)
    if not case or case["status"] != "awaiting_payment":
        return False
    letter = build_appeal_letter(case)
    with get_db() as db:
        db.execute(
            "UPDATE appeal_cases SET status = 'drafted', letter_text = ?, paid_at = CURRENT_TIMESTAMP WHERE id = ?",
            (letter, case_id),
        )
    _notify(case, "Your appeal draft is ready to review", "Your appeal letter is drafted. Please review it and approve it so we can send it.")
    _notify_ops(f"New paid appeal #{case_id}: {case['insurer_name']}, ${case['amount_denied']:,.0f}")
    return True


def approve(case: dict, letter_text: str) -> None:
    """The customer approves the letter, with any edits they made."""
    with get_db() as db:
        db.execute(
            "UPDATE appeal_cases SET status = 'approved', letter_text = ?, approved_at = CURRENT_TIMESTAMP"
            " WHERE id = ? AND status = 'drafted'",
            (letter_text.strip(), case["id"]),
        )
    _notify_ops(f"Appeal #{case['id']} approved by the customer and ready to send")


def mail_by_lob(case: dict) -> dict:
    """Send an approved appeal to the insurer's appeals address by certified mail."""
    if not config.LOB_API_KEY:
        raise RuntimeError("LOB_API_KEY is not configured")
    if not case.get("insurer_appeal_address") or not case.get("mailing_address"):
        raise ValueError("Both the insurer appeals address and the customer's mailing address are needed to mail")
    result = send_certified_letter(
        description=f"Insurance appeal #{case['id']}",
        from_name=case["patient_name"],
        from_address=case["mailing_address"],
        to_name=f"{case['insurer_name']} Appeals Department",
        to_address=case["insurer_appeal_address"],
        letter_text=case["letter_text"],
        api_key=config.LOB_API_KEY,
    )
    record_sent(case, "certified_mail", result["tracking_number"])
    return result


def record_sent(case: dict, method: str, tracking_number: str = "") -> None:
    with get_db() as db:
        db.execute(
            "UPDATE appeal_cases SET status = 'sent', sent_method = ?, tracking_number = ?, sent_at = CURRENT_TIMESTAMP"
            " WHERE id = ?",
            (method, tracking_number, case["id"]),
        )
    _notify(case, "Your appeal was sent", "We sent your appeal to your insurer. We'll tell you when their decision is due.")


def record_outcome(case: dict, outcome: str, amount_recovered: float | None) -> None:
    if outcome not in OUTCOMES:
        raise ValueError(f"Unknown outcome {outcome!r}")
    with get_db() as db:
        db.execute(
            "UPDATE appeal_cases SET status = 'decided', outcome = ?, amount_recovered = ?, decided_at = CURRENT_DATE"
            " WHERE id = ?",
            (outcome, amount_recovered, case["id"]),
        )


def deadlines(case: dict) -> dict:
    """Key dates for the case: when to file by, when the insurer must decide, when external review closes."""
    denial = date.fromisoformat(case["denial_date"])
    filing_days = config.APPEAL_FILING_DAYS.get(case.get("plan_type") or "")
    result = {"file_by": denial + timedelta(days=filing_days) if filing_days else None, "decision_due": None, "external_review_by": None}
    if case.get("sent_at"):
        sent = datetime.fromisoformat(str(case["sent_at"])).date()
        result["decision_due"] = sent + timedelta(days=config.APPEAL_DECISION_DAYS[case["service_timing"]])
    if case.get("outcome") == "upheld" and case.get("decided_at"):
        result["external_review_by"] = date.fromisoformat(str(case["decided_at"])) + timedelta(days=config.APPEAL_EXTERNAL_REVIEW_DAYS)
    return result


def list_open_cases() -> list[dict]:
    """Paid cases that still need work, for the ops queue."""
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM appeal_cases WHERE status IN ('drafted', 'approved', 'sent') ORDER BY created_at"
        ).fetchall()
    return [dict(row) for row in rows]


def _notify(case: dict, subject: str, message: str) -> None:
    link = f"{config.APP_URL.rstrip('/')}/appeal/case/{case['token']}"
    html = f"<p>{escape(message)}</p><p><a href=\"{link}\">View your appeal</a></p>"
    _send(case["email"], f"BillKarma: {subject}", html)


def _notify_ops(message: str) -> None:
    if config.OPS_NOTIFY_EMAIL:
        _send(config.OPS_NOTIFY_EMAIL, f"[Concierge] {message}", f"<p>{escape(message)}</p>")


def _send(to: str, subject: str, html: str) -> None:
    try:
        email_service.send_email(to, subject, html)
    except RuntimeError as exc:
        log.error("Concierge email to %s failed (%s): %s", to, subject, exc)
