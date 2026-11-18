"""Anonymous device tokens for the iOS app. No accounts: the device_id doubles as the bill-access session id."""

from __future__ import annotations

import hashlib
import secrets

from fastapi import HTTPException, Request

import config
from access_control import has_bill_access
from db import get_db


def _hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def register_device(app_version: str) -> dict:
    """Create an anonymous device. The raw token is returned once and never stored."""
    device_id = secrets.token_hex(16)
    token = secrets.token_urlsafe(config.MOBILE_TOKEN_BYTES)
    with get_db() as db:
        db.execute(
            "INSERT INTO mobile_devices (device_id, token_hash, app_version, last_seen_at) "
            "VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
            (device_id, _hash(token), (app_version or "")[:20]),
        )
    return {"device_id": device_id, "token": token}


def device_from_request(request: Request) -> str:
    """FastAPI dependency: the device_id for the bearer token, or 401."""
    header = request.headers.get("authorization", "")
    scheme, _, token = header.partition(" ")
    if scheme.lower() != "bearer" or not token.strip():
        raise HTTPException(401, "Missing device token")
    with get_db() as db:
        row = db.execute(
            "SELECT device_id FROM mobile_devices WHERE token_hash = ?", (_hash(token.strip()),)
        ).fetchone()
        if not row:
            raise HTTPException(401, "Unknown device token")
        db.execute(
            "UPDATE mobile_devices SET last_seen_at = CURRENT_TIMESTAMP WHERE device_id = ?", (row["device_id"],)
        )
    return row["device_id"]


def require_device_bill_access(device_id: str, bill_id: int) -> None:
    if not has_bill_access(device_id, bill_id):
        raise HTTPException(403, "Access denied for this bill")
