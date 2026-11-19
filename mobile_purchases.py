"""In-app purchase unlocks for the iOS app, verified with RevenueCat.

A paid unlock is a `report_unlocks` row, so report.is_unlocked() works for web and mobile alike.
IAP rows use stripe_session_id = "iap:<store transaction id>" (UNIQUE, so one purchase unlocks one bill).
Plus rows use "plus:<device>:<bill>".
"""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
from datetime import datetime, timezone

from fastapi import HTTPException

import config
import report
from db import get_db

log = logging.getLogger(__name__)

TEST_TRANSACTION_PREFIX = "test_"
REPORT_PRODUCTS = (config.REVENUECAT_REPORT_PRODUCT_ID, config.REVENUECAT_REPORT_OFFER_PRODUCT_ID)
ACTIVATING_EVENTS = {"INITIAL_PURCHASE", "RENEWAL", "PRODUCT_CHANGE", "UNCANCELLATION"}
REVENUECAT_TIMEOUT_SECONDS = 15


def _fetch_subscriber(device_id: str) -> dict:
    request = urllib.request.Request(
        f"{config.REVENUECAT_API_URL}/{device_id}",
        headers={"Authorization": f"Bearer {config.REVENUECAT_SECRET_API_KEY}"},
    )
    try:
        with urllib.request.urlopen(request, timeout=REVENUECAT_TIMEOUT_SECONDS) as response:
            return json.loads(response.read())["subscriber"]
    except (urllib.error.URLError, ValueError, KeyError) as exc:
        log.error("RevenueCat lookup failed for device %s: %s", device_id, exc)
        raise HTTPException(503, "Could not verify your purchase right now. Please try again.") from exc


def _in_mock_mode() -> bool:
    return config.ENV != "production" and not config.REVENUECAT_SECRET_API_KEY


def _transaction_is_genuine(device_id: str, transaction_id: str) -> bool:
    if _in_mock_mode():
        return transaction_id.startswith(TEST_TRANSACTION_PREFIX)
    purchases = _fetch_subscriber(device_id).get("non_subscriptions", {})
    for product_id in REPORT_PRODUCTS:
        if any(p.get("store_transaction_id") == transaction_id for p in purchases.get(product_id, [])):
            return True
    return False


def _insert_unlock(bill_id: int, key: str) -> bool:
    """Insert a paid unlock. False when this key already exists."""
    with get_db() as db:
        cursor = db.execute(
            "INSERT OR IGNORE INTO report_unlocks (bill_id, stripe_session_id, amount_cents, status, paid_at) "
            "VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)",
            (bill_id, key, config.REPORT_PRICE_CENTS, report.PAID),
        )
        return cursor.rowcount == 1


def unlock_with_purchase(device_id: str, bill_id: int, transaction_id: str) -> None:
    """Unlock one bill with a verified consumable purchase. 409 if the purchase already unlocked another bill."""
    key = f"iap:{transaction_id}"
    existing = report.bill_for_session(key)
    if existing == bill_id:
        return
    if existing is not None:
        raise HTTPException(409, "This purchase was already used for another bill")
    if not _transaction_is_genuine(device_id, transaction_id):
        raise HTTPException(402, "We couldn't verify that purchase")
    _insert_unlock(bill_id, key)


def _set_plus(device_id: str, active: bool, expires_at: str | None) -> None:
    with get_db() as db:
        db.execute(
            "INSERT INTO mobile_entitlements (device_id, plus_active, plus_expires_at, updated_at) "
            "VALUES (?, ?, ?, CURRENT_TIMESTAMP) "
            "ON CONFLICT(device_id) DO UPDATE SET plus_active = excluded.plus_active, "
            "plus_expires_at = excluded.plus_expires_at, updated_at = CURRENT_TIMESTAMP",
            (device_id, int(active), expires_at),
        )


def _refresh_plus_from_revenuecat(device_id: str) -> None:
    entitlement = _fetch_subscriber(device_id).get("entitlements", {}).get(config.REVENUECAT_PLUS_ENTITLEMENT)
    expires = entitlement.get("expires_date") if entitlement else None
    active = bool(entitlement) and (expires is None or expires > datetime.now(timezone.utc).isoformat())
    _set_plus(device_id, active, expires)


def grant_reward_plus(device_id: str, days: int) -> None:
    """Free Plus as a reward, kept apart from the paid status so a RevenueCat refresh can't erase it."""
    with get_db() as db:
        db.execute(
            "INSERT INTO mobile_entitlements (device_id, plus_active, reward_plus_until) "
            "VALUES (?, 0, datetime('now', ?)) ON CONFLICT(device_id) DO UPDATE SET "
            "reward_plus_until = MAX(COALESCE(reward_plus_until, ''), excluded.reward_plus_until)",
            (device_id, f"+{days} days"))


def _reward_plus_active(device_id: str) -> bool:
    with get_db() as db:
        row = db.execute("SELECT 1 FROM mobile_entitlements WHERE device_id = ? AND reward_plus_until > datetime('now')",
                         (device_id,)).fetchone()
    return row is not None


def plus_is_active(device_id: str, force_refresh: bool = False) -> bool:
    """Cached Plus status; refreshed from RevenueCat when older than MOBILE_PLUS_CACHE_SECONDS or when forced."""
    if _reward_plus_active(device_id):
        return True
    with get_db() as db:
        row = db.execute(
            "SELECT plus_active, strftime('%s', 'now') - strftime('%s', updated_at) AS age "
            "FROM mobile_entitlements WHERE device_id = ?",
            (device_id,),
        ).fetchone()
    if row and (row["plus_active"] or not force_refresh) and (row["age"] <= config.MOBILE_PLUS_CACHE_SECONDS or _in_mock_mode()):
        return bool(row["plus_active"])
    if _in_mock_mode():
        return False
    _refresh_plus_from_revenuecat(device_id)
    return plus_is_active(device_id)


def unlock_with_plus(device_id: str, bill_id: int, force_refresh: bool = False) -> bool:
    """Unlock with Plus. The row is permanent, so the bill stays unlocked if Plus later lapses."""
    if not plus_is_active(device_id, force_refresh):
        return False
    _insert_unlock(bill_id, f"plus:{device_id}:{bill_id}")
    return True


def ensure_unlocked(device_id: str, bill_id: int) -> None:
    """Raise 402 unless the bill is unlocked, granting a Plus unlock first when the device has Plus."""
    if report.is_unlocked(bill_id):
        return
    unlock_with_plus(device_id, bill_id)
    report.require_unlocked(bill_id)


def handle_webhook_event(event: dict) -> None:
    """Apply a RevenueCat webhook event to entitlements and refunds."""
    kind = event.get("type")
    device_id = event.get("app_user_id")
    if not device_id:
        return
    has_plus = config.REVENUECAT_PLUS_ENTITLEMENT in (event.get("entitlement_ids") or [])
    expires_ms = event.get("expiration_at_ms")
    expires = datetime.fromtimestamp(expires_ms / 1000, timezone.utc).isoformat() if expires_ms else None
    if kind in ACTIVATING_EVENTS and has_plus:
        _set_plus(device_id, True, expires)
    elif kind == "EXPIRATION" and has_plus:
        _set_plus(device_id, False, expires)
    elif kind == "CANCELLATION" and event.get("product_id") in REPORT_PRODUCTS:
        _mark_refunded(event.get("transaction_id") or event.get("original_transaction_id"))
    else:
        log.info("Ignoring RevenueCat event %s for %s", kind, device_id)


def _mark_refunded(transaction_id: str | None) -> None:
    if not transaction_id:
        return
    with get_db() as db:
        db.execute(
            "UPDATE report_unlocks SET status = 'refunded' WHERE stripe_session_id = ?", (f"iap:{transaction_id}",)
        )
