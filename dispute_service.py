"""Core service for BillKarma paid dispute activation and management."""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta

import config
import email_service
import payment as payment_module
from db import get_db
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
                hospital_billing_fax, status, is_nonprofit, preferred_channels
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'active', ?, ?)
            """,
            (
                bill_id, payment_id, patient_name, patient_email,
                patient_address, account_number, hospital_billing_email,
                hospital_billing_fax, 1 if is_nonprofit else 0,
                preferred_channels or "email",
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
        _file_financial_assistance(case_id, bill_id, patient_name, patient_address)

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
    if not sent:
        with get_db() as db:
            db.execute("UPDATE dispute_cases SET status = 'needs_delivery' WHERE id = ?", (case_id,))
        return False

    log.info("Dispute letter sent to %s for case %d", hospital_email, case_id)
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


def _file_financial_assistance(
    case_id: int,
    bill_id: int,
    patient_name: str,
    patient_address: str,
) -> None:
    """Generate and log a 501(r) financial assistance application."""
    with get_db() as db:
        bill = db.execute(
            """
            SELECT b.provider_name, hf.financial_assistance_url, hf.fa_application_url
            FROM bills b
            LEFT JOIN hospital_directory hd ON hd.name LIKE '%' || b.provider_name || '%'
            LEFT JOIN hospital_financials hf ON hf.facility_id = hd.facility_id
            WHERE b.id = ?
            LIMIT 1
            """,
            (bill_id,),
        ).fetchone()

    if not bill:
        return

    fa_url = (bill["fa_application_url"] or bill["financial_assistance_url"] or "") if bill else ""
    log.info(
        "Financial assistance noted for case %d (nonprofit hospital). FA URL: %s",
        case_id,
        fa_url or "not found",
    )

    with get_db() as db:
        db.execute(
            "UPDATE dispute_cases SET financial_assistance_filed = 1 WHERE id = ?",
            (case_id,),
        )


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
    if not sent:
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
