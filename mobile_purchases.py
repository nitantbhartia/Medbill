"""In-app purchase unlocks for the iOS app, verified with RevenueCat.

A paid unlock is a `report_unlocks` row, so report.is_unlocked() works for web and mobile alike.
IAP rows use stripe_session_id = "iap:<store transaction id>" (UNIQUE, so one purchase unlocks one bill).
Plus rows use "plus:<device>:<bill>".
"""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.parse
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
V2_MAX_PAGES = 10


def _fetch_subscriber(device_id: str) -> dict:
    """The device's purchases as {"entitlements": {key: {"expires_date"}}, "non_subscriptions": {product: [..]}}."""
    try:
        if config.REVENUECAT_API_VERSION == "2":
            return _fetch_subscriber_v2(device_id)
        return _get_json(f"{config.REVENUECAT_API_URL}/{device_id}")["subscriber"]
    except (urllib.error.URLError, ValueError, KeyError, TypeError) as exc:
        log.error("RevenueCat lookup failed for device %s: %s", device_id, exc)
        raise HTTPException(503, "Could not verify your purchase right now. Please try again.") from exc


def _get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {config.REVENUECAT_SECRET_API_KEY}"})
    try:
        with urllib.request.urlopen(request, timeout=REVENUECAT_TIMEOUT_SECONDS) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        # Name the endpoint: a 403 here means the key lacks read permission for that part of the API.
        exc.msg = f"{exc.msg} from {url.split('?')[0]}"
        raise


_v2_names: dict[tuple[str, str], str] = {}  # (kind, RevenueCat id) -> our identifier; these never change
_v2_project: list[str] = []


def _v2_project_url() -> str:
    project = config.REVENUECAT_PROJECT_ID or (_v2_project[0] if _v2_project else "")
    if not project:
        project = _get_json(f"{config.REVENUECAT_V2_URL}/projects")["items"][0]["id"]
        _v2_project.append(project)
    return f"{config.REVENUECAT_V2_URL}/projects/{project}"


def _v2_items(path: str) -> list[dict]:
    """Every item of a V2 list. A customer RevenueCat has never seen has bought nothing."""
    items: list[dict] = []
    url = _v2_project_url() + path
    for _ in range(V2_MAX_PAGES):
        try:
            page = _get_json(url)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return items
            raise
        items += page.get("items") or []
        if not page.get("next_page"):
            break
        url = urllib.parse.urljoin(config.REVENUECAT_V2_URL, page["next_page"])
    return items


def _v2_name(kind: str, revenuecat_id: str, field: str) -> str:
    """V2 lists carry RevenueCat's own ids; look up the store product id or entitlement key once."""
    if (kind, revenuecat_id) not in _v2_names:
        _v2_names[(kind, revenuecat_id)] = _get_json(f"{_v2_project_url()}/{kind}/{revenuecat_id}")[field]
    return _v2_names[(kind, revenuecat_id)]


def _fetch_subscriber_v2(device_id: str) -> dict:
    customer = f"/customers/{urllib.parse.quote(device_id, safe='')}"
    entitlements = {}
    for item in _v2_items(f"{customer}/active_entitlements"):
        expires_ms = item.get("expires_at")
        expires = datetime.fromtimestamp(expires_ms / 1000, timezone.utc).isoformat() if expires_ms else None
        entitlements[_v2_name("entitlements", item["entitlement_id"], "lookup_key")] = {"expires_date": expires}
    purchases: dict[str, list[dict]] = {}
    for item in _v2_items(f"{customer}/purchases"):
        if item.get("status") != "owned":
            continue
        product = _v2_name("products", item["product_id"], "store_identifier")
        purchases.setdefault(product, []).append({"store_transaction_id": item.get("store_purchase_identifier")})
    return {"entitlements": entitlements, "non_subscriptions": purchases}


def _in_mock_mode() -> bool:
    return config.ENV != "production" and not config.REVENUECAT_SECRET_API_KEY


def _transaction_is_genuine(device_id: str, transaction_id: str, products: tuple = REPORT_PRODUCTS) -> bool:
    if _in_mock_mode():
        return transaction_id.startswith(TEST_TRANSACTION_PREFIX)
    purchases = _fetch_subscriber(device_id).get("non_subscriptions", {})
    for product_id in products:
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
