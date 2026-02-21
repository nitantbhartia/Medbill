"""Stripe payment integration for flat-fee dispute service."""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request

import config
from db import get_db

log = logging.getLogger(__name__)

STRIPE_API = "https://api.stripe.com/v1"


def _stripe_post(path: str, params: dict) -> dict:
    """POST to Stripe REST API with form-encoded params."""
    if not config.STRIPE_SECRET_KEY:
        raise RuntimeError("STRIPE_SECRET_KEY not configured")
    body = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(
        f"{STRIPE_API}/{path}",
        data=body,
        headers={
            "Authorization": f"Bearer {config.STRIPE_SECRET_KEY}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")
        log.error("Stripe error %s: %s", e.code, body_text)
        raise RuntimeError(f"Stripe error {e.code}: {body_text}") from e


def _stripe_get(path: str) -> dict:
    req = urllib.request.Request(
        f"{STRIPE_API}/{path}",
        headers={"Authorization": f"Bearer {config.STRIPE_SECRET_KEY}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")
        log.error("Stripe GET error %s: %s", e.code, body_text)
        raise RuntimeError(f"Stripe error {e.code}: {body_text}") from e


def calculate_fee(bill_total: float) -> int:
    """Return the dispute fee in cents based on bill total.

    Under $1k: $29 | $1k-$5k: $49 | $5k-$20k: $99 | Over $20k: $149
    """
    for threshold, fee_cents in config.DISPUTE_FEE_TIERS:
        if bill_total < threshold:
            return fee_cents
    return config.DISPUTE_FEE_TIERS[-1][1]


def create_checkout_session(bill_id: int, email: str, amount_cents: int) -> dict:
    """Create a Stripe Checkout session for dispute payment.

    Returns the session object with id and url.
    """
    success_url = config.STRIPE_SUCCESS_URL.replace("{CHECKOUT_SESSION_ID}", "{CHECKOUT_SESSION_ID}")
    cancel_url = config.STRIPE_CANCEL_URL.replace("{bill_id}", str(bill_id))

    params = {
        "mode": "payment",
        "customer_email": email,
        "line_items[0][price_data][currency]": "usd",
        "line_items[0][price_data][unit_amount]": str(amount_cents),
        "line_items[0][price_data][product_data][name]": "BillKarma Dispute Service",
        "line_items[0][price_data][product_data][description]": (
            "AI-powered medical bill dispute. No savings = full refund."
        ),
        "line_items[0][quantity]": "1",
        "metadata[bill_id]": str(bill_id),
        "success_url": success_url,
        "cancel_url": cancel_url,
        "payment_intent_data[metadata][bill_id]": str(bill_id),
    }

    session = _stripe_post("checkout/sessions", params)

    with get_db() as db:
        db.execute(
            """
            INSERT INTO dispute_payments (bill_id, stripe_session_id, amount_cents, status, patient_email)
            VALUES (?, ?, ?, 'pending', ?)
            """,
            (bill_id, session["id"], amount_cents, email),
        )

    return session


def get_session(session_id: str) -> dict:
    """Retrieve a Stripe Checkout session."""
    return _stripe_get(f"checkout/sessions/{session_id}")


def verify_webhook_signature(payload: bytes, sig_header: str, secret: str) -> bool:
    """Verify Stripe webhook signature using HMAC-SHA256.

    Returns True if valid. Does not raise — caller should check return value.
    """
    try:
        parts = {k: v for part in sig_header.split(",") for k, v in [part.split("=", 1)]}
        ts = int(parts["t"])
        sigs = [v for k, v in [p.split("=", 1) for p in sig_header.split(",")] if k == "v1"]
    except (KeyError, ValueError):
        return False

    # Reject timestamps more than 5 minutes old
    if abs(time.time() - ts) > 300:
        return False

    signed_payload = f"{ts}.{payload.decode()}".encode()
    expected = hmac.new(secret.encode(), signed_payload, hashlib.sha256).hexdigest()
    return any(hmac.compare_digest(expected, sig) for sig in sigs)


def record_payment_success(session_id: str) -> int | None:
    """Mark a payment as paid and return bill_id. Returns None if already processed."""
    with get_db() as db:
        row = db.execute(
            "SELECT id, bill_id, status FROM dispute_payments WHERE stripe_session_id = ?",
            (session_id,),
        ).fetchone()
        if not row or row["status"] == "paid":
            return None
        db.execute(
            "UPDATE dispute_payments SET status = 'paid' WHERE id = ?",
            (row["id"],),
        )
        return row["bill_id"]


def get_payment_for_bill(bill_id: int) -> dict | None:
    """Get the most recent payment record for a bill."""
    with get_db() as db:
        row = db.execute(
            "SELECT * FROM dispute_payments WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
    return dict(row) if row else None


def issue_refund(payment_id: int) -> bool:
    """Issue a Stripe refund for a dispute payment.

    Returns True on success. Raises RuntimeError on Stripe failure.
    """
    with get_db() as db:
        row = db.execute(
            "SELECT stripe_payment_intent_id, amount_cents, status FROM dispute_payments WHERE id = ?",
            (payment_id,),
        ).fetchone()

    if not row:
        raise ValueError(f"Payment {payment_id} not found")
    if row["status"] == "refunded":
        return True  # Already refunded

    # Get payment intent ID if not stored — retrieve from session
    pi_id = row["stripe_payment_intent_id"]
    if not pi_id:
        with get_db() as db:
            sess_row = db.execute(
                "SELECT stripe_session_id FROM dispute_payments WHERE id = ?",
                (payment_id,),
            ).fetchone()
        if sess_row:
            session = get_session(sess_row["stripe_session_id"])
            pi_id = session.get("payment_intent")

    if not pi_id:
        raise RuntimeError("Cannot issue refund: payment intent ID not found")

    _stripe_post("refunds", {"payment_intent": pi_id})

    with get_db() as db:
        db.execute(
            "UPDATE dispute_payments SET status = 'refunded', refunded_at = CURRENT_TIMESTAMP WHERE id = ?",
            (payment_id,),
        )

    return True
