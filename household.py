"""Concierge household bill plan: membership, uploaded bills and EOBs, bill-vs-EOB check, help requests."""

import logging
from html import escape

import config
import email_service
import scanner
from db import get_db

log = logging.getLogger(__name__)

PLANS = {
    "yearly": {"cents": config.HOUSEHOLD_PRICE_YEARLY_CENTS, "interval": "year", "label": "$199 a year"},
    "monthly": {"cents": config.HOUSEHOLD_PRICE_MONTHLY_CENTS, "interval": "month", "label": "$20 a month"},
}
ACTIVE_STATUSES = ("active", "trialing")
DOC_TYPES = {"bill": "Bill from a provider", "eob": "Explanation of benefits (EOB) from your insurer"}


def get_membership(user_id: int) -> dict | None:
    with get_db() as db:
        row = db.execute("SELECT * FROM household_members WHERE user_id = ?", (user_id,)).fetchone()
    return dict(row) if row else None


def is_active(user_id: int) -> bool:
    membership = get_membership(user_id)
    return bool(membership and membership["status"] in ACTIVE_STATUSES)


def record_checkout(user_id: int, plan: str, session_id: str) -> None:
    with get_db() as db:
        db.execute(
            """
            INSERT INTO household_members (user_id, plan, status, stripe_session_id) VALUES (?, ?, 'pending', ?)
            ON CONFLICT(user_id) DO UPDATE SET plan = excluded.plan, stripe_session_id = excluded.stripe_session_id,
                updated_at = CURRENT_TIMESTAMP
            """,
            (user_id, plan, session_id),
        )


def activate_from_session(session: dict) -> bool:
    """Activate the member a completed subscription checkout belongs to. Returns False if none matches."""
    user_id = int((session.get("metadata") or {}).get("user_id") or 0)
    if not user_id or session.get("mode") != "subscription":
        return False
    with get_db() as db:
        updated = db.execute(
            """
            UPDATE household_members SET status = 'active', stripe_customer_id = ?, stripe_subscription_id = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ?
            """,
            (session.get("customer"), session.get("subscription"), user_id),
        ).rowcount
    if updated:
        _notify_ops(f"New household member: user #{user_id}")
    return bool(updated)


def sync_subscription(subscription: dict) -> None:
    """Mirror a Stripe subscription's status (active, past_due, canceled, ...) onto the member."""
    with get_db() as db:
        db.execute(
            "UPDATE household_members SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE stripe_subscription_id = ?",
            (subscription.get("status") or "canceled", subscription.get("id")),
        )


def add_document(user_id: int, doc_type: str, file_path: str, content_type: str, data: bytes, form: dict) -> int:
    """Store an uploaded bill or EOB, filling any amounts the member left blank from the scanned document."""
    values = {
        "provider_name": (form.get("provider_name") or "").strip() or None,
        "service_date": form.get("service_date") or None,
        "amount_due": _to_amount(form.get("amount_due")),
        "amount_paid": _to_amount(form.get("amount_paid")),
        "patient_responsibility": _to_amount(form.get("patient_responsibility")),
    }
    status = "manual"
    amount_key = "amount_due" if doc_type == "bill" else "patient_responsibility"
    if values[amount_key] is None:
        status = _fill_from_scan(values, doc_type, content_type, data)
    with get_db() as db:
        cursor = db.execute(
            """
            INSERT INTO household_documents (user_id, doc_type, provider_name, service_date, amount_due, amount_paid,
                patient_responsibility, file_path, original_filename, extraction_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, doc_type, values["provider_name"], values["service_date"], values["amount_due"],
             values["amount_paid"], values["patient_responsibility"], file_path, form.get("original_filename"), status),
        )
        doc_id = cursor.lastrowid
    _auto_link(user_id, doc_id)
    return doc_id


def link_eob(user_id: int, bill_id: int, eob_id: int | None) -> None:
    with get_db() as db:
        db.execute(
            "UPDATE household_documents SET eob_document_id = ? WHERE id = ? AND user_id = ? AND doc_type = 'bill'",
            (eob_id, bill_id, user_id),
        )


def check_bill(bill: dict, eob: dict | None) -> dict:
    """Compare a bill with its EOB and say what to do: wait, pay, dispute the difference, or ask for a refund."""
    tolerance = config.HOUSEHOLD_MATCH_TOLERANCE
    if not eob:
        return {"verdict": "wait", "message": "Don't pay yet. Upload the EOB from your insurer for this visit so we can check the amount."}
    owed = eob.get("patient_responsibility")
    due = bill.get("amount_due")
    if owed is None or due is None:
        return {"verdict": "review", "message": "We couldn't read the amounts. We'll check this one by hand."}
    paid = bill.get("amount_paid") or 0
    if paid > owed + tolerance:
        return {"verdict": "overpaid", "message": f"You paid ${paid - owed:,.2f} more than your insurer says you owe. Ask the provider for a refund."}
    if due > owed + tolerance:
        return {"verdict": "overbilled", "message": f"The bill asks for ${due - owed:,.2f} more than your insurer says you owe. Pay only ${owed:,.2f} and dispute the rest."}
    return {"verdict": "ok", "message": f"Matches your EOB. You owe ${owed:,.2f}."}


def dashboard(user_id: int) -> dict:
    """The member's bills with their check result, and their EOBs."""
    with get_db() as db:
        docs = [dict(r) for r in db.execute(
            "SELECT * FROM household_documents WHERE user_id = ? ORDER BY created_at DESC", (user_id,)
        )]
        requested = {r["document_id"] for r in db.execute(
            "SELECT document_id FROM concierge_requests WHERE user_id = ? AND status = 'open'", (user_id,)
        )}
    eobs = {d["id"]: d for d in docs if d["doc_type"] == "eob"}
    bills = []
    for doc in docs:
        if doc["doc_type"] != "bill":
            continue
        doc["check"] = check_bill(doc, eobs.get(doc["eob_document_id"]))
        doc["help_requested"] = doc["id"] in requested
        bills.append(doc)
    return {"bills": bills, "eobs": list(eobs.values())}


def request_help(user_id: int, document_id: int | None, note: str) -> None:
    with get_db() as db:
        db.execute(
            "INSERT INTO concierge_requests (user_id, document_id, note) VALUES (?, ?, ?)",
            (user_id, document_id, note.strip()[:2000]),
        )
    _notify_ops(f"Household member #{user_id} asked for help" + (f" with document #{document_id}" if document_id else ""))


def open_requests() -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT r.*, u.email, u.name, d.provider_name, d.doc_type
            FROM concierge_requests r
            JOIN users u ON u.id = r.user_id
            LEFT JOIN household_documents d ON d.id = r.document_id
            WHERE r.status = 'open' ORDER BY r.created_at
            """
        ).fetchall()
    return [dict(r) for r in rows]


def resolve_request(request_id: int, resolution: str) -> None:
    """Close a help request and email the member what was done."""
    with get_db() as db:
        db.execute(
            "UPDATE concierge_requests SET status = 'resolved', resolution = ?, resolved_at = CURRENT_TIMESTAMP WHERE id = ?",
            (resolution.strip(), request_id),
        )
        row = db.execute(
            "SELECT u.email FROM concierge_requests r JOIN users u ON u.id = r.user_id WHERE r.id = ?", (request_id,)
        ).fetchone()
    if not row:
        return
    link = f"{config.APP_URL.rstrip('/')}/household/dashboard"
    html = f"<p>We handled your request: {escape(resolution.strip())}</p><p><a href=\"{link}\">See your bills</a></p>"
    try:
        email_service.send_email(row["email"], "BillKarma: we handled your request", html)
    except RuntimeError as exc:
        log.error("Resolution email for request #%s failed: %s", request_id, exc)


def _fill_from_scan(values: dict, doc_type: str, content_type: str, data: bytes) -> str:
    """Fill blank fields from the scanned document. Returns the extraction status."""
    if not config.GEMINI_API_KEY:
        return "needs_review"
    try:
        extracted = scanner.process_bill_with_verification(data, content_type)
    except Exception as exc:  # the scanner can fail many ways (API, parsing); a person reviews instead
        log.error("Household %s scan failed: %s", doc_type, exc)
        return "needs_review"
    values["provider_name"] = values["provider_name"] or extracted.get("provider_name")
    items = extracted.get("line_items") or []
    values["service_date"] = values["service_date"] or next((i.get("date_of_service") for i in items if i.get("date_of_service")), None)
    if doc_type == "bill":
        values["amount_due"] = _to_amount(extracted.get("total_patient_owes"))
    else:
        owed = [_to_amount(i.get("patient_responsibility")) for i in items]
        values["patient_responsibility"] = round(sum(o for o in owed if o is not None), 2) if any(o is not None for o in owed) else _to_amount(extracted.get("total_patient_owes"))
    amount_key = "amount_due" if doc_type == "bill" else "patient_responsibility"
    return "extracted" if values[amount_key] is not None else "needs_review"


def _auto_link(user_id: int, doc_id: int) -> None:
    """Link a new bill to an unlinked EOB (or a new EOB to an unlinked bill) for the same provider and date."""
    with get_db() as db:
        doc = db.execute("SELECT * FROM household_documents WHERE id = ?", (doc_id,)).fetchone()
        if not doc["provider_name"] or not doc["service_date"]:
            return
        other_type = "eob" if doc["doc_type"] == "bill" else "bill"
        match = db.execute(
            """
            SELECT id FROM household_documents
            WHERE user_id = ? AND doc_type = ? AND UPPER(provider_name) = UPPER(?) AND service_date = ?
              AND (doc_type = 'eob' OR eob_document_id IS NULL)
            ORDER BY created_at DESC LIMIT 1
            """,
            (user_id, other_type, doc["provider_name"], doc["service_date"]),
        ).fetchone()
    if not match:
        return
    bill_id, eob_id = (doc_id, match["id"]) if doc["doc_type"] == "bill" else (match["id"], doc_id)
    link_eob(user_id, bill_id, eob_id)


def _to_amount(value) -> float | None:
    try:
        return round(float(str(value).replace("$", "").replace(",", "")), 2) if value not in (None, "") else None
    except ValueError:
        return None


def _notify_ops(message: str) -> None:
    if not config.OPS_NOTIFY_EMAIL:
        return
    try:
        email_service.send_email(config.OPS_NOTIFY_EMAIL, f"[Concierge] {message}", f"<p>{escape(message)}</p>")
    except RuntimeError as exc:
        log.error("Ops notification failed (%s): %s", message, exc)
