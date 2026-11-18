"""Optional Sign in with Apple accounts. A signed-in account shares its bills across every device linked to it."""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request

import jwt
from fastapi import HTTPException

import config
from db import get_db

log = logging.getLogger(__name__)
_apple_keys = jwt.PyJWKClient(config.APPLE_KEYS_URL)


def verify_identity_token(identity_token: str) -> dict:
    """Check Apple's signature, issuer, audience and expiry. Returns the token claims."""
    try:
        key = _apple_keys.get_signing_key_from_jwt(identity_token)
        return jwt.decode(
            identity_token, key.key, algorithms=["RS256"],
            audience=config.APPLE_BUNDLE_ID, issuer=config.APPLE_ISSUER,
        )
    except (jwt.PyJWTError, jwt.PyJWKClientError) as exc:
        log.warning("Apple identity token rejected: %s", exc)
        raise HTTPException(401, "Apple sign-in could not be verified") from exc


def _client_secret() -> str | None:
    if not (config.APPLE_SIGNIN_KEY_ID and config.APPLE_SIGNIN_TEAM_ID and config.APPLE_SIGNIN_PRIVATE_KEY):
        return None
    now = int(time.time())
    claims = {"iss": config.APPLE_SIGNIN_TEAM_ID, "iat": now, "exp": now + config.APPLE_CLIENT_SECRET_TTL_SECONDS,
              "aud": config.APPLE_ISSUER, "sub": config.APPLE_BUNDLE_ID}
    return jwt.encode(claims, config.APPLE_SIGNIN_PRIVATE_KEY, algorithm="ES256",
                      headers={"kid": config.APPLE_SIGNIN_KEY_ID})


def _apple_post(url: str, form: dict) -> dict | None:
    request = urllib.request.Request(url, data=urllib.parse.urlencode(form).encode(), method="POST")
    try:
        with urllib.request.urlopen(request, timeout=config.APPLE_HTTP_TIMEOUT_SECONDS) as response:
            body = response.read()
            return json.loads(body) if body else {}
    except (urllib.error.URLError, ValueError) as exc:
        log.error("Apple request to %s failed: %s", url, exc)
        return None


def exchange_code_for_refresh_token(authorization_code: str) -> str | None:
    """Needed later to revoke the sign-in. None when the Apple key isn't configured or Apple refuses."""
    secret = _client_secret()
    if not secret or not authorization_code:
        return None
    result = _apple_post(config.APPLE_TOKEN_URL, {
        "client_id": config.APPLE_BUNDLE_ID, "client_secret": secret,
        "code": authorization_code, "grant_type": "authorization_code",
    })
    return (result or {}).get("refresh_token")


def revoke_refresh_token(refresh_token: str | None) -> None:
    secret = _client_secret()
    if not refresh_token or not secret:
        log.warning("Apple token not revoked: no refresh token or Apple key not configured")
        return
    _apple_post(config.APPLE_REVOKE_URL, {
        "client_id": config.APPLE_BUNDLE_ID, "client_secret": secret,
        "token": refresh_token, "token_type_hint": "refresh_token",
    })


def account_for_device(device_id: str) -> dict | None:
    with get_db() as db:
        row = db.execute(
            "SELECT a.* FROM mobile_accounts a JOIN mobile_devices d ON d.account_id = a.id WHERE d.device_id = ?",
            (device_id,),
        ).fetchone()
    return dict(row) if row else None


def sign_in(device_id: str, identity_token: str, authorization_code: str) -> dict:
    """Create or find the account for this Apple ID, link the device, and share bills across its devices."""
    claims = verify_identity_token(identity_token)
    email = claims.get("email")
    is_relay = int(str(claims.get("is_private_email", "")).lower() == "true")
    with get_db() as db:
        row = db.execute("SELECT id FROM mobile_accounts WHERE apple_sub = ?", (claims["sub"],)).fetchone()
        if row:
            account_id = row["id"]
        else:
            account_id = db.execute(
                "INSERT INTO mobile_accounts (apple_sub, email, email_is_relay) VALUES (?, ?, ?)",
                (claims["sub"], email, is_relay),
            ).lastrowid
        db.execute("UPDATE mobile_devices SET account_id = ? WHERE device_id = ?", (account_id, device_id))
    refresh_token = exchange_code_for_refresh_token(authorization_code)
    with get_db() as db:
        if refresh_token:
            db.execute("UPDATE mobile_accounts SET apple_refresh_token = ? WHERE id = ?", (refresh_token, account_id))
        if email:
            db.execute("UPDATE mobile_accounts SET email = ?, email_is_relay = ? WHERE id = ?", (email, is_relay, account_id))
    share_bills_across_account(account_id)
    return account_for_device(device_id)


def _account_device_ids(account_id: int) -> list[str]:
    with get_db() as db:
        rows = db.execute("SELECT device_id FROM mobile_devices WHERE account_id = ?", (account_id,)).fetchall()
    return [row["device_id"] for row in rows]


def share_bills_across_account(account_id: int) -> None:
    """Every device on the account gets access to every bill any of its devices can open."""
    devices = _account_device_ids(account_id)
    placeholders = ",".join("?" * len(devices))
    with get_db() as db:
        bills = [r["bill_id"] for r in db.execute(
            f"SELECT DISTINCT bill_id FROM bill_access_sessions WHERE session_id IN ({placeholders})", devices
        ).fetchall()]
        for device in devices:
            for bill_id in bills:
                db.execute("INSERT OR IGNORE INTO bill_access_sessions (session_id, bill_id) VALUES (?, ?)", (device, bill_id))


def share_bill_with_account(device_id: str, bill_id: int) -> None:
    """A bill scanned on a signed-in device appears on the account's other devices too."""
    account = account_for_device(device_id)
    if not account:
        return
    with get_db() as db:
        for other in _account_device_ids(account["id"]):
            db.execute("INSERT OR IGNORE INTO bill_access_sessions (session_id, bill_id) VALUES (?, ?)", (other, bill_id))


def delete_account(account: dict, delete_bill) -> None:
    """Remove the account, every linked device with its bills, events and entitlements, and revoke the Apple token."""
    for device_id in _account_device_ids(account["id"]):
        with get_db() as db:
            bill_ids = [r["bill_id"] for r in db.execute(
                "SELECT bill_id FROM bill_access_sessions WHERE session_id = ?", (device_id,)).fetchall()]
        for bill_id in bill_ids:
            delete_bill(bill_id)
        with get_db() as db:
            db.execute("DELETE FROM mobile_events WHERE device_id = ?", (device_id,))
            db.execute("DELETE FROM mobile_entitlements WHERE device_id = ?", (device_id,))
            db.execute("DELETE FROM mobile_devices WHERE device_id = ?", (device_id,))
    with get_db() as db:
        db.execute("DELETE FROM mobile_accounts WHERE id = ?", (account["id"],))
    revoke_refresh_token(account.get("apple_refresh_token"))
