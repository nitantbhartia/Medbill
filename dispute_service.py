"""Core service for BillKarma paid dispute activation and management."""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta

import config
import email_service
from email_service import followup_body
import payment as payment_module
from db import get_db
from complaints import build_complaint_letter, file_attorney_general_complaint
from debt_fighter import generate_charity_care_letter, send_certified_letter
from fax import fax_configured, send_fax
from dispute_workflow import build_dispute_letter

log = logging.getLogger(__name__)


def calculate_fee(bill_total: float) -> int:
    """Return dispute fee in cents based on bill total."""
    for threshold, fee_cents in config.DISPUTE_FEE_TIERS:
        if bill_total < threshold:
            return fee_cents
    return config.DISPUTE_FEE_TIERS[-1][1]


def activate_dispute(
    bill_id: int,
    payment_id: int,
    patient_name: str,
    patient_email: str,
    patient_address: str,
    account_number: str,
    hospital_billing_email: str,
    hospital_billing_fax: str = "",
    preferred_channels: str = "email",
    household_income: float = 0,
    household_size: int = 0,
) -> int:
    """Create an active dispute case after payment is confirmed.

    Returns the new case_id.
    """
    with get_db() as db:
        # Check if dispute case already exists for this bill
        existing = db.execute(
            "SELECT id FROM dispute_cases WHERE bill_id = ? AND status != 'refunded'",
            (bill_id,),
        ).fetchone()
        if existing:
            return existing["id"]

        # Check if hospital is nonprofit (for 501(r) financial assistance)
        bill = db.execute("SELECT provider_name FROM bills WHERE id = ?", (bill_id,)).fetchone()
        provider_name = bill["provider_name"] if bill else ""
        is_nonprofit = _check_nonprofit(db, provider_name)

        db.execute(
            """
            INSERT INTO dispute_cases (
                bill_id, payment_id, patient_name, patient_email,
                patient_address, account_number, hospital_billing_email,
                hospital_billing_fax, status, is_nonprofit, preferred_channels,
                household_income, household_size
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'active', ?, ?, ?, ?)
            """,
            (
                bill_id, payment_id, patient_name, patient_email,
                patient_address, account_number, hospital_billing_email,
                hospital_billing_fax, 1 if is_nonprofit else 0,
                preferred_channels or "email", household_income or None, household_size or None,
            ),
        )
        case_id = db.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]

        # Schedule follow-ups
        today = date.today()
        for i, days in enumerate(config.DISPUTE_FOLLOWUP_DAYS, start=1):
            scheduled = today + timedelta(days=days)
            db.execute(
                """
                INSERT INTO followup_queue (case_id, followup_number, scheduled_for)
                VALUES (?, ?, ?)
                """,
                (case_id, i, scheduled.isoformat()),
            )

    # Send initial dispute letter
    delivered = _send_dispute(case_id, patient_name, account_number, hospital_billing_email)

    # Send confirmation to patient
    _notify_patient_activated(patient_email, patient_name, case_id, provider_name)

    # File financial assistance if nonprofit
    if is_nonprofit:
        _file_financial_assistance(case_id)

    if delivered:
        add_strategy_note(case_id, "Dispute letter emailed to the billing department.")
    else:
        add_strategy_note(case_id, "Dispute letter written. Waiting for the billing department's email address to send it.")

    return case_id


def _check_nonprofit(db, provider_name: str) -> bool:
    """Check if provider is a nonprofit hospital using our database."""
    if not provider_name:
        return False
    row = db.execute(
        """
        SELECT hf.nonprofit_status FROM hospital_financials hf
        JOIN hospital_directory hd ON hd.facility_id = hf.facility_id
        WHERE hd.name LIKE ? LIMIT 1
        """,
        (f"%{provider_name[:20]}%",),
    ).fetchone()
    return bool(row and row["nonprofit_status"])


def _hospital_mailing_address(provider_name: str) -> str:
    """Return 'Street, City, ST 12345' for the hospital from our directory, or '' if unknown."""
    if not provider_name:
        return ""
    with get_db() as db:
        row = db.execute(
            "SELECT address, city, state, zip FROM hospital_directory WHERE name LIKE ? LIMIT 1",
            (f"%{provider_name[:20]}%",),
        ).fetchone()
    if not row or not (row["address"] and row["city"] and row["state"] and row["zip"]):
        return ""
    return f"{row['address']}, {row['city']}, {row['state']} {row['zip']}"


def _mail_certified(
    case, provider_name: str, letter_text: str, description: str, department: str = "Billing Department"
) -> str:
    """Mail the letter to the hospital by Lob certified mail. Returns the tracking number,
    or '' if it was not mailed (no Lob key, or no address for either side)."""
    if not config.LOB_API_KEY or not case["patient_address"]:
        return ""
    hospital_address = _hospital_mailing_address(provider_name)
    if not hospital_address:
        log.warning("No mailing address for %r; case %d not mailed", provider_name, case["id"])
        return ""
    try:
        result = send_certified_letter(
            description=description,
            from_name=case["patient_name"],
            from_address=case["patient_address"],
            to_name=f"{provider_name} {department}",
            to_address=hospital_address,
            letter_text=letter_text,
            api_key=config.LOB_API_KEY,
        )
    except RuntimeError as exc:
        log.error("Certified mail failed for case %d: %s", case["id"], exc)
        return ""
    return result["tracking_number"]


def _fill_letter(letter: str, case, hospital_address: str) -> str:
    """Replace the template placeholders in a dispute letter with the case's real details."""
    reply_to = f"{config.EMAIL_FROM_ADDRESS}, referencing case #{case['id']}, or by mail to {case['patient_address']}"
    return (
        letter.replace("[Your Address]", case["patient_address"] or "")
        .replace("[Your Email / Phone]", case["patient_email"])
        .replace("[Hospital Address]", hospital_address)
        .replace("[Your Email / Mailing Address]", reply_to)
        .replace("[Your Signature]", case["patient_name"])
    )


def _complaint_authorized(bill_id: int) -> bool:
    """True if the patient signed a representative designation that covers filing complaints."""
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM esign_records WHERE bill_id = ? AND rep_signed_at >= ?",
            (bill_id, config.COMPLAINT_AUTHORIZATION_START),
        ).fetchone()
    return bool(row)


def _file_complaint(case, provider_name: str) -> None:
    """After the last follow-up, file a complaint with the hospital's state Attorney General."""
    hospital_address = _hospital_mailing_address(provider_name)
    if not hospital_address or not case["patient_address"] or not _complaint_authorized(case["bill_id"]):
        return
    state = hospital_address.rsplit(",", 1)[1].split()[0]
    dispute = build_dispute_letter(
        case["bill_id"], requestor_name=case["patient_name"], account_number=case["account_number"] or "[Account Number]"
    )
    if not dispute:
        return
    dispute["letter"] = _fill_letter(dispute["letter"], case, hospital_address)
    letter = build_complaint_letter(
        case["patient_name"], case["patient_address"], provider_name, case["account_number"],
        case["initial_sent_at"] or "an earlier date", len(config.DISPUTE_FOLLOWUP_DAYS),
        dispute["letter"],
    )
    tracking = file_attorney_general_complaint(state, case["patient_name"], case["patient_address"], letter, case["id"])
    if not tracking:
        return
    with get_db() as db:
        db.execute("UPDATE dispute_cases SET complaint_tracking = ? WHERE id = ?", (tracking, case["id"]))
    add_strategy_note(case["id"], f"Complaint filed with the {state} Attorney General by certified mail.")


def _fax_hospital(case, letter_text: str) -> str:
    """Fax the letter to the hospital billing office. Returns the fax id, or '' if not faxed."""
    if not fax_configured() or not case["hospital_billing_fax"]:
        return ""
    try:
        return send_fax(case["hospital_billing_fax"], letter_text)
    except (ValueError, RuntimeError) as exc:
        log.error("Fax failed for case %d: %s", case["id"], exc)
        return ""


def _send_dispute(case_id: int, patient_name: str, account_number: str, hospital_email: str) -> bool:
    """Email the dispute letter to the billing department. Marks the case sent only if it went out;
    otherwise the case waits in 'needs_delivery' until the patient gives us an address."""
    with get_db() as db:
        case = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
        if not case:
            return False
        bill_id = case["bill_id"]
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()

    if not bill:
        log.error("Cannot send dispute for case %d: bill not found", case_id)
        return False

    letter_data = build_dispute_letter(
        bill_id,
        requestor_name=patient_name,
        account_number=account_number or "[Account Number]",
    )
    if not letter_data:
        log.warning("No dispute letter generated for case %d (no findings)", case_id)
        return False

    provider = bill["provider_name"] or "the billing department"
    letter_data["letter"] = _fill_letter(letter_data["letter"], case, _hospital_mailing_address(provider))
    subject = f"Formal Billing Dispute — Account {account_number or 'N/A'} — {patient_name}"

    sent = False
    if hospital_email:
        try:
            sent = bool(email_service.send_dispute_to_hospital(
                to=hospital_email,
                subject=subject,
                letter_text=letter_data["letter"],
                patient_name=patient_name,
            ))
        except Exception as exc:
            log.error("Failed to send dispute for case %d to %s: %s", case_id, hospital_email, exc)
    tracking = _mail_certified(case, provider, letter_data["letter"], f"Billing dispute, case {case_id}")
    if tracking:
        with get_db() as db:
            db.execute("UPDATE dispute_cases SET certified_tracking = ? WHERE id = ?", (tracking, case_id))
    faxed = _fax_hospital(case, letter_data["letter"])
    if not (sent or tracking or faxed):
        with get_db() as db:
            db.execute("UPDATE dispute_cases SET status = 'needs_delivery' WHERE id = ?", (case_id,))
        return False

    log.info("Dispute letter sent for case %d (email=%s, certified=%s)", case_id, sent, bool(tracking))
    today = date.today().isoformat()
    with get_db() as db:
        db.execute(
            "UPDATE dispute_cases SET initial_sent_at = ?, status = 'sent' WHERE id = ?",
            (today, case_id),
        )
    return True


def deliver_dispute(case_id: int, hospital_email: str) -> bool:
    """Save the billing office email for a waiting case, send the letter, and restart the
    follow-up clock from today. Returns True if the letter went out."""
    hospital_email = (hospital_email or "").strip()
    if "@" not in hospital_email or "." not in hospital_email.split("@")[-1]:
        raise ValueError("Enter the billing office's email address.")
    with get_db() as db:
        case = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
        if not case:
            raise ValueError("Case not found.")
        if case["status"] != "needs_delivery":
            raise ValueError("This dispute has already been sent.")
        db.execute("UPDATE dispute_cases SET hospital_billing_email = ? WHERE id = ?", (hospital_email, case_id))

    if not _send_dispute(case_id, case["patient_name"], case["account_number"] or "", hospital_email):
        return False
    today = date.today()
    with get_db() as db:
        for number, days in enumerate(config.DISPUTE_FOLLOWUP_DAYS, start=1):
            db.execute(
                "UPDATE followup_queue SET scheduled_for = ? WHERE case_id = ? AND followup_number = ? AND sent_at IS NULL",
                ((today + timedelta(days=days)).isoformat(), case_id, number),
            )
    add_strategy_note(case_id, f"Dispute letter emailed to {hospital_email}.")
    return True


def _notify_patient_activated(
    patient_email: str,
    patient_name: str,
    case_id: int,
    hospital_name: str,
) -> None:
    """Send a confirmation email to the patient that the dispute has been filed."""
    try:
        email_service.send_dispute_confirmation(
            to=patient_email,
            patient_name=patient_name,
            case_id=case_id,
            hospital_name=hospital_name,
        )
    except Exception as exc:
        log.warning("Could not send patient confirmation for case %d: %s", case_id, exc)


def _file_financial_assistance(case_id: int) -> None:
    """Mail a 501(r) financial assistance request to a nonprofit hospital. Needs the patient's
    income and household size; without them nothing is filed and the case isn't marked filed."""
    case = get_case(case_id)
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (case["bill_id"],)).fetchone()
    provider = bill["provider_name"] if bill else ""
    hospital_address = _hospital_mailing_address(provider)
    amount = bill["total_patient_owes"] or bill["total_charged"]
    if not (amount and case["household_income"] and case["household_size"] and case["patient_address"] and hospital_address):
        return
    try:
        letter = generate_charity_care_letter(
            user_name=case["patient_name"],
            user_address=case["patient_address"],
            hospital_name=provider,
            hospital_address=hospital_address,
            account_number=case["account_number"] or "N/A",
            bill_amount=str(amount),
            income=case["household_income"],
            household_size=case["household_size"],
            date_of_service=bill["bill_date"] or "",
            with_enclosures=False,
        )
    except ValueError as exc:
        log.error("Could not build financial assistance letter for case %d: %s", case_id, exc)
        return
    tracking = _mail_certified(
        case, provider, letter["letter_text"], f"Financial assistance request, case {case_id}",
        department="Financial Assistance Department",
    )
    if not tracking:
        return
    with get_db() as db:
        db.execute("UPDATE dispute_cases SET financial_assistance_filed = 1 WHERE id = ?", (case_id,))
    add_strategy_note(case_id, "Financial assistance request mailed to the hospital by certified mail.")


def add_strategy_note(case_id: int, note_text: str) -> None:
    """Append an AI strategy note to a dispute case."""
    with get_db() as db:
        row = db.execute(
            "SELECT strategy_notes FROM dispute_cases WHERE id = ?", (case_id,)
        ).fetchone()
        if not row:
            return
        notes = json.loads(row["strategy_notes"] or "[]")
        notes.append({"date": date.today().isoformat(), "text": note_text})
        db.execute(
            "UPDATE dispute_cases SET strategy_notes = ? WHERE id = ?",
            (json.dumps(notes), case_id),
        )


def pause_dispute(case_id: int) -> None:
    """Pause follow-ups for a dispute case."""
    with get_db() as db:
        db.execute(
            "UPDATE dispute_cases SET status = 'paused' WHERE id = ?", (case_id,)
        )
    add_strategy_note(case_id, "Follow-ups paused by patient request.")


def escalate_dispute(case_id: int) -> None:
    """Mark a dispute case as escalated."""
    with get_db() as db:
        db.execute(
            "UPDATE dispute_cases SET status = 'escalated' WHERE id = ?", (case_id,)
        )
    add_strategy_note(
        case_id,
        "Case escalated. Consider filing a complaint with your state insurance commissioner "
        "or Attorney General's office if the hospital remains unresponsive.",
    )


def get_case(case_id: int) -> dict | None:
    """Get a dispute case by ID."""
    with get_db() as db:
        row = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
    return dict(row) if row else None


def cases_needing_attention() -> dict:
    """Disputes a person should look at: ones that couldn't be sent, and open ones where the hospital
    replied without settling (denied, asked for information, offered a payment plan, or unreadable)."""
    with get_db() as db:
        waiting = db.execute(
            "SELECT c.id, c.bill_id, c.patient_name, c.patient_email, b.provider_name, c.created_at"
            " FROM dispute_cases c JOIN bills b ON b.id = c.bill_id"
            " WHERE c.status = 'needs_delivery' ORDER BY c.created_at"
        ).fetchall()
        replies = db.execute(
            "SELECT r.case_id, r.bill_id, r.outcome, r.summary, r.body, r.created_at, r.patient_name, r.provider_name FROM ("
            "  SELECT r.*, c.bill_id, c.patient_name, c.status, b.provider_name"
            "  FROM dispute_replies r JOIN dispute_cases c ON c.id = r.case_id JOIN bills b ON b.id = c.bill_id"
            "  WHERE r.outcome IN ('denied', 'needs_info', 'payment_plan', 'unclear')"
            "  AND c.status IN ('active', 'sent', 'refund_pending')"
            ") r ORDER BY r.created_at DESC LIMIT ?",
            (config.OPS_QUEUE_REPLY_LIMIT,),
        ).fetchall()
    return {"waiting": [dict(row) for row in waiting], "replies": [dict(row) for row in replies]}


def get_case_for_bill(bill_id: int) -> dict | None:
    """Get the active dispute case for a bill."""
    with get_db() as db:
        row = db.execute(
            "SELECT * FROM dispute_cases WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
    return dict(row) if row else None


def get_followups_for_case(case_id: int) -> list[dict]:
    """Get all follow-up records for a case."""
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM followup_queue WHERE case_id = ? ORDER BY followup_number",
            (case_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def process_due_followups() -> int:
    """Send any overdue follow-ups. Returns count of follow-ups sent."""
    today = date.today().isoformat()
    with get_db() as db:
        due = db.execute(
            """
            SELECT fq.id, fq.case_id, fq.followup_number
            FROM followup_queue fq
            JOIN dispute_cases dc ON dc.id = fq.case_id
            WHERE fq.sent_at IS NULL
              AND fq.scheduled_for <= ?
              AND dc.status IN ('active', 'sent')
            ORDER BY fq.scheduled_for
            """,
            (today,),
        ).fetchall()

    sent_count = 0
    for row in due:
        try:
            _send_followup(row["case_id"], row["followup_number"], row["id"])
            sent_count += 1
        except Exception as exc:
            log.error("Failed to send follow-up %d for case %d: %s", row["followup_number"], row["case_id"], exc)

    return sent_count


def _send_followup(case_id: int, followup_number: int, queue_id: int) -> None:
    """Send a single follow-up and mark it sent."""
    with get_db() as db:
        case = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
        if not case or case["status"] not in ("active", "sent"):
            return
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (case["bill_id"],)).fetchone()

    if not bill:
        return

    hospital_email = case["hospital_billing_email"]
    patient_name = case["patient_name"]
    account_number = case["account_number"] or "N/A"
    provider = bill["provider_name"] or "the provider"

    subject = (
        f"Follow-Up #{followup_number}: Billing Dispute — Account {account_number} — {patient_name}"
    )

    sent = False
    if hospital_email:
        try:
            sent = bool(email_service.send_followup_to_hospital(
                to=hospital_email,
                subject=subject,
                patient_name=patient_name,
                account_number=account_number,
                hospital_name=provider,
                followup_number=followup_number,
                case_id=case_id,
            ))
        except Exception as exc:
            log.error("Failed to send follow-up email for case %d: %s", case_id, exc)
    body = followup_body(patient_name, account_number, followup_number, case_id)
    mailed = _mail_certified(case, provider, body, f"Dispute follow-up {followup_number}, case {case_id}")
    faxed = _fax_hospital(case, body)
    if not (sent or mailed or faxed):
        log.error("Follow-up %d for case %d not sent; will retry on the next run", followup_number, case_id)
        return

    with get_db() as db:
        db.execute(
            "UPDATE followup_queue SET sent_at = CURRENT_TIMESTAMP WHERE id = ?",
            (queue_id,),
        )
        db.execute(
            "UPDATE dispute_cases SET followups_sent = followups_sent + 1 WHERE id = ?",
            (case_id,),
        )

    add_strategy_note(case_id, f"Follow-up #{followup_number} emailed. No reply recorded yet.")

    # If this is the last follow-up, check if we should auto-refund
    if followup_number >= len(config.DISPUTE_FOLLOWUP_DAYS):
        _file_complaint(case, provider)
        _check_auto_refund(case_id)


def _check_auto_refund(case_id: int) -> None:
    """After final follow-up, mark unresolved cases for refund review."""
    with get_db() as db:
        case = db.execute(
            "SELECT status FROM dispute_cases WHERE id = ?", (case_id,)
        ).fetchone()
        if case and case["status"] in ("active", "sent"):
            db.execute(
                "UPDATE dispute_cases SET status = 'refund_pending' WHERE id = ?",
                (case_id,),
            )
    log.info("Case %d marked refund_pending after final follow-up", case_id)


def mark_resolved(case_id: int, outcome: str, actual_savings: float | None = None) -> None:
    """Mark a dispute case as resolved with an outcome."""
    with get_db() as db:
        db.execute(
            """
            UPDATE dispute_cases
            SET status = 'resolved', outcome = ?, actual_savings = ?,
                resolved_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (outcome, actual_savings, case_id),
        )


def issue_refund_for_case(case_id: int) -> bool:
    """Issue a refund for a dispute case. Returns True if refund was processed."""
    with get_db() as db:
        case = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
        if not case:
            raise ValueError(f"Case {case_id} not found")
        payment_row = db.execute(
            "SELECT * FROM dispute_payments WHERE id = ?",
            (case["payment_id"],),
        ).fetchone()

    if not payment_row:
        log.warning("No payment found for case %d", case_id)
        return False

    refunded = payment_module.issue_refund(payment_row["id"])
    if refunded:
        with get_db() as db:
            db.execute(
                "UPDATE dispute_cases SET status = 'refunded', refunded_at = CURRENT_TIMESTAMP WHERE id = ?",
                (case_id,),
            )
        patient_email = case["patient_email"]
        patient_name = case["patient_name"]
        try:
            email_service.send_refund_confirmation(
                to=patient_email,
                patient_name=patient_name,
                case_id=case_id,
                amount_cents=payment_row["amount_cents"],
            )
        except Exception as exc:
            log.warning("Could not send refund confirmation for case %d: %s", case_id, exc)

    return refunded


def get_dispute_summary(bill_id: int) -> dict:
    """Return a summary dict for the dispute dashboard."""
    with get_db() as db:
        case = db.execute(
            "SELECT * FROM dispute_cases WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
        payment = db.execute(
            "SELECT * FROM dispute_payments WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()

    if not case:
        return {"has_case": False}

    case = dict(case)
    followups = get_followups_for_case(case["id"])

    strategy_notes = []
    try:
        strategy_notes = json.loads(case.get("strategy_notes") or "[]")
    except (ValueError, TypeError):
        pass

    created = date.fromisoformat(str(case["created_at"])[:10]) if case.get("created_at") else date.today()
    next_followup = next((f["scheduled_for"] for f in followups if not f.get("sent_at")), None)
    letter = build_dispute_letter(
        bill_id, requestor_name=case["patient_name"], account_number=case.get("account_number") or "[Account Number]",
    )

    return {
        "has_case": True,
        "case_id": case["id"],
        "bill_id": bill_id,
        "hospital_billing_email": case.get("hospital_billing_email") or "",
        "account_number": case.get("account_number") or "",
        "next_followup": next_followup,
        "refund_eligible_on": (created + timedelta(days=config.DISPUTE_MAX_DAYS)).isoformat(),
        "resolved_at": case.get("resolved_at"),
        "letter": (letter or {}).get("letter", ""),
        "status": case["status"],
        "patient_name": case["patient_name"],
        "hospital_name": dict(bill)["provider_name"] if bill else "",
        "amount_cents": dict(payment)["amount_cents"] if payment else 0,
        "initial_sent_at": case["initial_sent_at"],
        "followups_sent": case["followups_sent"],
        "outcome": case["outcome"],
        "actual_savings": case["actual_savings"],
        "refunded_at": case["refunded_at"],
        "is_nonprofit": bool(case["is_nonprofit"]),
        "financial_assistance_filed": bool(case["financial_assistance_filed"]),
        "followups": followups,
        "created_at": case["created_at"],
        "preferred_channels": case.get("preferred_channels") or "email",
        "strategy_notes": strategy_notes,
    }
