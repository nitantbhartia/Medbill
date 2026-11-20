"""ClaimCoach API: device registration, data deletion and analytics events."""

from __future__ import annotations

import json
import re

from fastapi import APIRouter, Depends, HTTPException, Request

import cc_cases
import config
import mobile_auth
from api import _check_rate_limit, _request_client_key
from compliance import log_audit
from db import get_db
from mobile_routes import ok

router = APIRouter(prefix="/api/cc")

EVENT_TEXT = re.compile(config.CC_EVENT_PROP_PATTERN)


@router.post("/device")
async def register_device(request: Request, payload: dict):
    if not _check_rate_limit(f"cc-register:{_request_client_key(request)}", config.MOBILE_REGISTER_LIMIT_PER_HOUR):
        raise HTTPException(429, "Too many new devices from this network. Try again later.")
    device = mobile_auth.register_device(str(payload.get("app_version", "")))
    with get_db() as db:
        db.execute("UPDATE mobile_devices SET app = 'claimcoach' WHERE device_id = ?", (device["device_id"],))
    return ok(device)


@router.delete("/device")
async def delete_device(device_id: str = Depends(mobile_auth.device_from_request)):
    """'Delete my data': every case on this device (unlocked or not), its events, entitlement and registration."""
    cc_cases.delete_device_cases(device_id)
    with get_db() as db:
        db.execute("DELETE FROM mobile_events WHERE device_id = ?", (device_id,))
        db.execute("DELETE FROM mobile_entitlements WHERE device_id = ?", (device_id,))
        db.execute("DELETE FROM mobile_devices WHERE device_id = ?", (device_id,))
    log_audit("cc_delete_device", "device", device_id)
    return ok({"deleted": True})


def _safe_props(props) -> dict:
    """Keep only props that cannot hold free text: a bool, an int, or a short code-like string."""
    if not isinstance(props, dict):
        return {}
    return {
        key: value for key, value in props.items()
        if EVENT_TEXT.fullmatch(str(key)) and (isinstance(value, (bool, int))
                                               or (isinstance(value, str) and EVENT_TEXT.fullmatch(value)))
    }


@router.post("/events")
async def record_event(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    name = payload.get("name")
    props = payload.get("props") or {}
    if name in config.CC_EVENT_NAMES and len(json.dumps(props)) <= config.MOBILE_EVENT_PROPS_MAX_BYTES:
        with get_db() as db:
            db.execute(
                "INSERT INTO mobile_events (device_id, name, props_json) VALUES (?, ?, ?)",
                (device_id, name, json.dumps(_safe_props(props))),
            )
    return ok({"ok": True})
