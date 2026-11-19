"""iOS app API: device registration, onboarding profile, events, hospital lookup, data deletion."""

from __future__ import annotations

import json
import re

from fastapi import APIRouter, Depends, HTTPException, Request

import config
import mobile_auth
from api import _check_rate_limit, _request_client_key
from compliance import delete_bill_data, log_audit, record_consent
from db import get_db
from hospital_seo import _display_city, _display_name, state_display_name

router = APIRouter(prefix="/api/m")

ZIP_PATTERN = re.compile(r"\d{5}")
PROFILE_CHOICES = {
    "bill_type": config.MOBILE_BILL_TYPES,
    "amount_band": config.MOBILE_AMOUNT_BANDS,
    "insurance_status": config.MOBILE_INSURANCE_STATUSES,
    "due_band": config.MOBILE_DUE_BANDS,
    "attribution_source": config.MOBILE_ATTRIBUTION_SOURCES,
    "onboarding_variant": config.MOBILE_ONBOARDING_VARIANTS,
}


def ok(data) -> dict:
    return {"status": "ok", "data": data}


@router.post("/device")
async def register_device(request: Request, payload: dict):
    if not _check_rate_limit(f"m-register:{_request_client_key(request)}", config.MOBILE_REGISTER_LIMIT_PER_HOUR):
        raise HTTPException(429, "Too many new devices from this network. Try again later.")
    return ok(mobile_auth.register_device(str(payload.get("app_version", ""))))


def _validated_profile(payload: dict) -> dict:
    """Keep only known onboarding answers, rejecting unknown values with 400."""
    fields = {}
    for name, allowed in PROFILE_CHOICES.items():
        value = payload.get(name)
        if value is None:
            continue
        if value not in allowed:
            raise HTTPException(400, f"Unknown value for {name}")
        fields[name] = value
    zip_code = payload.get("zip_code")
    if zip_code is not None:
        if not ZIP_PATTERN.fullmatch(str(zip_code)):
            raise HTTPException(400, "zip_code must be a 5-digit US ZIP code")
        fields["zip_code"] = str(zip_code)
    situations = payload.get("situations")
    if situations is not None:
        if not isinstance(situations, list) or not set(situations) <= config.MOBILE_SITUATIONS:
            raise HTTPException(400, "Unknown value for situations")
        fields["situations_json"] = json.dumps(sorted(set(situations)))
    facility_id = payload.get("hospital_facility_id")
    if facility_id is not None:
        fields["hospital_facility_id"] = str(facility_id)[:20]
    return fields


@router.post("/profile")
async def save_profile(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    fields = _validated_profile(payload)
    if fields:
        assignments = ", ".join(f"{name} = ?" for name in fields)
        with get_db() as db:
            db.execute(f"UPDATE mobile_devices SET {assignments} WHERE device_id = ?", (*fields.values(), device_id))
    return ok({"saved": True})


@router.post("/events")
async def record_event(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    name = payload.get("name")
    props = json.dumps(payload.get("props") or {})
    if name in config.MOBILE_EVENT_NAMES and len(props) <= config.MOBILE_EVENT_PROPS_MAX_BYTES:
        with get_db() as db:
            db.execute(
                "INSERT INTO mobile_events (device_id, name, props_json) VALUES (?, ?, ?)", (device_id, name, props)
            )
    return ok({"ok": True})


@router.get("/hospitals/search")
async def search_hospitals(q: str = "", device_id: str = Depends(mobile_auth.device_from_request)):
    if not _check_rate_limit(f"m-search:{device_id}"):
        raise HTTPException(429, "Too many searches. Try again in a bit.")
    query = q.strip()
    if len(query) < 2:
        return ok({"hospitals": []})
    token = f"%{query}%"
    with get_db() as db:
        rows = db.execute(
            "SELECT facility_id, name, city, state FROM hospitals "
            "WHERE name LIKE ? OR city LIKE ? "
            "ORDER BY CASE WHEN lower(name) LIKE lower(?) THEN 0 ELSE 1 END, name LIMIT ?",
            (token, token, f"{query}%", config.MOBILE_HOSPITAL_SEARCH_LIMIT),
        ).fetchall()
    hospitals = [
        {
            "facility_id": row["facility_id"],
            "name": _display_name(row["name"], row["facility_id"]),
            "city": _display_city(row["city"]),
            "state": state_display_name(row["state"]),
        }
        for row in rows
    ]
    return ok({"hospitals": hospitals})


@router.get("/hospital-insight")
async def hospital_insight(facility_id: str, device_id: str = Depends(mobile_auth.device_from_request)):
    """Real CMS-based markup for one hospital, or null when too few procedures were compared."""
    with get_db() as db:
        row = db.execute(
            "SELECT h.name, h.facility_id, h.city, h.state, m.avg_markup_vs_medicare, m.billing_grade, "
            "m.procedures_compared, m.computed_at FROM hospitals h "
            "JOIN billing_metrics m ON m.facility_id = h.facility_id "
            "WHERE h.facility_id = ? AND m.avg_markup_vs_medicare > 0 AND m.procedures_compared >= ?",
            (facility_id, config.RANKING_MIN_PROCEDURES),
        ).fetchone()
    if not row:
        return ok(None)
    return ok({
        "name": _display_name(row["name"], row["facility_id"]),
        "city": _display_city(row["city"]),
        "state": state_display_name(row["state"]),
        "avg_markup": round(row["avg_markup_vs_medicare"], 1),
        "billing_grade": row["billing_grade"],
        "procedures_compared": row["procedures_compared"],
        "as_of": str(row["computed_at"] or "")[:10] or None,
    })


def delete_bill_everywhere(bill_id: int) -> None:
    """Remove a bill and every row that points at it, including access and purchase records."""
    with get_db() as db:
        db.execute("DELETE FROM bill_access_sessions WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM report_unlocks WHERE bill_id = ?", (bill_id,))
        db.execute("DELETE FROM evidence_uploads WHERE bill_id = ?", (bill_id,))
    delete_bill_data(bill_id)


@router.delete("/device")
async def delete_device(device_id: str = Depends(mobile_auth.device_from_request)):
    """'Delete my data': every bill this device scanned, plus its events, entitlement and registration."""
    with get_db() as db:
        bill_ids = [r["bill_id"] for r in db.execute(
            "SELECT bill_id FROM bill_access_sessions WHERE session_id = ?", (device_id,)
        ).fetchall()]
    for bill_id in bill_ids:
        delete_bill_everywhere(bill_id)
    with get_db() as db:
        db.execute("DELETE FROM mobile_events WHERE device_id = ?", (device_id,))
        db.execute("DELETE FROM mobile_entitlements WHERE device_id = ?", (device_id,))
        db.execute("DELETE FROM mobile_devices WHERE device_id = ?", (device_id,))
    log_audit(action="mobile_delete_device", resource_type="device", resource_id=device_id)
    return ok({"deleted": True})


@router.post("/consent")
async def data_improvement_consent(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    """The opt-in "Help improve BillKarma" choice. Off unless the user says yes; logged either way."""
    granted = payload.get("granted")
    if not isinstance(granted, bool):
        raise HTTPException(400, "granted must be true or false")
    with get_db() as db:
        db.execute("UPDATE mobile_devices SET data_improvement = ? WHERE device_id = ?", (int(granted), device_id))
    record_consent(None, None, "data_improvement" if granted else "data_improvement_withdrawn",
                   config.DATA_IMPROVEMENT_CONSENT_VERSION)
    return ok({"granted": granted})
