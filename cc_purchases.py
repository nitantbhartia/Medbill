"""ClaimCoach unlocks: one paid appeal kit per case, or ClaimCoach Plus. Verified with RevenueCat like BillKarma."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import HTTPException

import config
import mobile_purchases
from db import get_db


def is_unlocked(case_id: int) -> bool:
    with get_db() as db:
        row = db.execute("SELECT 1 FROM cc_case_unlocks WHERE case_id = ? AND status = 'paid'", (case_id,)).fetchone()
    return row is not None


def _insert_unlock(case_id: int, source: str, product_id: str) -> None:
    with get_db() as db:
        db.execute(
            "INSERT OR IGNORE INTO cc_case_unlocks (case_id, source, product_id, status) VALUES (?, ?, ?, 'paid')",
            (case_id, source, product_id),
        )


def unlock_with_purchase(device_id: str, case_id: int, transaction_id: str) -> None:
    """Unlock one case with a verified purchase. 409 if the purchase already unlocked another case."""
    source = f"iap:{transaction_id}"
    with get_db() as db:
        existing = db.execute("SELECT case_id FROM cc_case_unlocks WHERE source = ?", (source,)).fetchone()
    if existing and existing["case_id"] == case_id:
        return
    if existing:
        raise HTTPException(409, "This purchase was already used for another appeal")
    if not mobile_purchases._transaction_is_genuine(device_id, transaction_id, (config.CC_APPEAL_KIT_PRODUCT_ID,)):
        raise HTTPException(402, "We couldn't verify that purchase")
    _insert_unlock(case_id, source, config.CC_APPEAL_KIT_PRODUCT_ID)


def _plus_active(device_id: str) -> bool:
    with get_db() as db:
        row = db.execute("SELECT plus_active FROM mobile_entitlements WHERE device_id = ?", (device_id,)).fetchone()
    if row and row["plus_active"]:
        return True
    if mobile_purchases._in_mock_mode():
        return False
    entitlement = mobile_purchases._fetch_subscriber(device_id).get("entitlements", {}).get(config.CC_PLUS_ENTITLEMENT)
    expires = entitlement.get("expires_date") if entitlement else None
    active = bool(entitlement) and (expires is None or expires > datetime.now(timezone.utc).isoformat())
    mobile_purchases._set_plus(device_id, active, expires)
    return active


def unlock_with_plus(device_id: str, case_id: int) -> bool:
    """Unlock with ClaimCoach Plus. The row is permanent, so the case stays unlocked if Plus later lapses."""
    if not _plus_active(device_id):
        return False
    _insert_unlock(case_id, f"plus:{device_id}:{case_id}", config.CC_PLUS_ENTITLEMENT)
    return True


def handle_webhook_event(event: dict) -> None:
    """Apply a RevenueCat webhook event to ClaimCoach Plus and to refunded appeal kits."""
    kind = event.get("type")
    device_id = event.get("app_user_id")
    if not device_id:
        return
    has_plus = config.CC_PLUS_ENTITLEMENT in (event.get("entitlement_ids") or [])
    expires_ms = event.get("expiration_at_ms")
    expires = datetime.fromtimestamp(expires_ms / 1000, timezone.utc).isoformat() if expires_ms else None
    if kind in mobile_purchases.ACTIVATING_EVENTS and has_plus:
        mobile_purchases._set_plus(device_id, True, expires)
    elif kind == "EXPIRATION" and has_plus:
        mobile_purchases._set_plus(device_id, False, expires)
    elif kind == "CANCELLATION" and event.get("product_id") == config.CC_APPEAL_KIT_PRODUCT_ID:
        transaction_id = event.get("transaction_id") or event.get("original_transaction_id")
        if transaction_id:
            with get_db() as db:
                db.execute("UPDATE cc_case_unlocks SET status = 'refunded' WHERE source = ?", (f"iap:{transaction_id}",))
