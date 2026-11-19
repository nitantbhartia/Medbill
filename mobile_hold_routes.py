"""iOS app API for hold calls, plus the Twilio webhooks. Webhooks are checked against Twilio's signature."""

from __future__ import annotations

import json
import logging

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import Response

from api import _check_rate_limit
import config
import hold_call_ai
import hold_calls
import mobile_auth
import mobile_purchases
import twilio_client
from db import get_db
from mobile_routes import ok

router = APIRouter()
log = logging.getLogger(__name__)
XML = "application/xml"


# ── The app ────────────────────────────────────────────────────────────────────

@router.post("/api/m/phone/verify")
async def start_phone_verification(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    number = hold_calls.to_e164(str(payload.get("phone") or ""))
    if not number:
        raise HTTPException(400, "Enter a 10-digit US phone number.")
    if not config.HOLD_CALLS_ENABLED or not config.TWILIO_VERIFY_SERVICE_SID:
        raise HTTPException(503, "Waiting on hold isn't available yet.")
    if not _check_rate_limit(f"m-sms:{device_id}", config.SMS_CODES_PER_DEVICE_PER_HOUR) or \
            not _check_rate_limit(f"m-sms-number:{hold_calls.phone_hash(number)}", config.SMS_CODES_PER_NUMBER_PER_HOUR):
        raise HTTPException(429, "Too many codes requested. Try again later.")
    try:
        twilio_client.start_verification(number)
    except twilio_client.TwilioError as exc:
        raise HTTPException(502, "We couldn't send the code. Try again.") from exc
    return ok({"sent": True})


@router.post("/api/m/phone/verify/check")
async def check_phone_verification(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    number, code = hold_calls.to_e164(str(payload.get("phone") or "")), str(payload.get("code") or "")
    if not number or not code.isdigit() or len(code) != 6:
        raise HTTPException(400, "Enter the 6-digit code.")
    if not _check_rate_limit(f"m-sms-check:{device_id}", config.SMS_CHECKS_PER_DEVICE_PER_HOUR):
        raise HTTPException(429, "Too many attempts. Try again later.")
    try:
        approved = twilio_client.check_verification(number, code)
    except twilio_client.TwilioError as exc:
        raise HTTPException(502, "We couldn't check the code. Try again.") from exc
    if not approved:
        raise HTTPException(400, "That code isn't right.")
    with get_db() as db:
        db.execute("INSERT OR REPLACE INTO phone_verifications (device_id, phone_hash, verified_at) VALUES (?, ?, datetime('now'))",
                   (device_id, hold_calls.phone_hash(number)))
    return ok({"verified": True})


@router.get("/api/m/bills/{bill_id}/hold-call-info")
async def hold_call_info(bill_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    from datetime import datetime, timezone
    opening = hold_calls.next_opening(datetime.now(timezone.utc), hold_calls.hospital_timezone(bill_id))
    allowance = hold_calls.entitlement(device_id, bill_id)
    return ok({"enabled": config.HOLD_CALLS_ENABLED, "allowance": allowance,
               "open_now": opening <= datetime.now(timezone.utc), "next_opening": opening.isoformat(),
               "price_product_id": config.HOLD_CALL_PRODUCT_ID})


@router.post("/api/m/bills/{bill_id}/hold-call")
async def request_hold_call(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    if not _check_rate_limit(f"m-hold:{device_id}", config.HOLD_CALL_REQUESTS_PER_DEVICE_PER_HOUR):
        raise HTTPException(429, "Too many call requests. Try again later.")
    try:
        return ok(hold_calls.request_call(device_id, bill_id, str(payload.get("hospital_number") or ""),
                                          str(payload.get("user_number") or "")))
    except hold_calls.HoldCallError as exc:
        raise HTTPException(exc.status, exc.message) from exc


@router.get("/api/m/hold-calls/{call_id}")
async def hold_call_status(call_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    with get_db() as db:
        call = db.execute("SELECT * FROM hold_calls WHERE id = ? AND device_id = ?", (call_id, device_id)).fetchone()
    if not call:
        raise HTTPException(404, "Call not found")
    with get_db() as db:
        hold = db.execute("SELECT CAST((julianday(COALESCE(human_at, ended_at, 'now')) - julianday(started_at)) * 86400 AS INTEGER) AS s "
                          "FROM hold_calls WHERE id = ? AND started_at IS NOT NULL", (call_id,)).fetchone()
    return ok({"status": call["status"], "hold_seconds": hold["s"] if hold else None, "end_reason": call["end_reason"],
               "human_at": call["human_at"], "scheduled_for": call["scheduled_for"],
               "included_call_used": call["status"] == "connected"})


@router.post("/api/m/hold-calls/{call_id}/cancel")
async def cancel_hold_call(call_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    return ok({"cancelled": hold_calls.cancel(call_id, device_id)})


@router.post("/api/m/hold-credits")
async def redeem_hold_credit(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    """A purchased `bk_hold_call` becomes one call credit. The same store transaction counts once."""
    transaction_id = str(payload.get("transaction_id") or "")
    if not transaction_id or not mobile_purchases._transaction_is_genuine(device_id, transaction_id, (config.HOLD_CALL_PRODUCT_ID,)):
        raise HTTPException(402, "We couldn't verify that purchase")
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO hold_call_credits (transaction_id, device_id) VALUES (?, ?)", (transaction_id, device_id))
    return ok({"credits": hold_calls.credits_available(device_id)})


# ── Twilio webhooks ────────────────────────────────────────────────────────────

async def _verified_params(request: Request) -> dict:
    """The webhook's form fields, after checking Twilio signed them with our auth token."""
    params = dict((await request.form()).items())
    url = f"{config.APP_URL.rstrip('/')}{request.url.path}"
    if not twilio_client.signature_is_valid(url, params, request.headers.get("X-Twilio-Signature", "")):
        raise HTTPException(403, "Bad signature")
    return params


@router.post("/api/hold/twiml/{call_id}")
async def hospital_twiml(call_id: int, request: Request):
    await _verified_params(request)
    return Response(hold_calls.listen_twiml(call_id), media_type=XML)


@router.post("/api/hold/transcript/{call_id}")
async def transcript(call_id: int, request: Request):
    params = await _verified_params(request)
    if params.get("TranscriptionEvent") == "transcription-content" and params.get("Final", "true") == "true":
        try:
            text = json.loads(params.get("TranscriptionData") or "{}").get("transcript", "")
        except ValueError:
            text = ""
        if text.strip():
            hold_calls.handle_utterance(call_id, text, hold_call_ai.classify_menu, hold_call_ai.classify_person)
    return Response(status_code=204)


@router.post("/api/hold/status/{call_id}")
async def hospital_status(call_id: int, request: Request):
    params = await _verified_params(request)
    if params.get("CallStatus") in ("completed", "failed", "busy", "no-answer", "canceled"):
        hold_calls.call_ended(call_id, params["CallStatus"])
    return Response(status_code=204)


@router.post("/api/hold/user-twiml/{call_id}")
async def user_twiml(call_id: int, request: Request):
    await _verified_params(request)
    return Response(hold_calls.user_twiml(call_id), media_type=XML)


@router.post("/api/hold/user-status/{call_id}")
async def user_status(call_id: int, request: Request):
    params = await _verified_params(request)
    status = params.get("CallStatus")
    if status in ("in-progress", "answered"):
        hold_calls.user_answered(call_id)
    elif status in ("no-answer", "busy", "failed", "canceled"):
        with get_db() as db:
            row = db.execute("SELECT status FROM hold_calls WHERE id = ?", (call_id,)).fetchone()
        if row and row["status"] == "connecting":
            hold_calls.user_missed(call_id)
    return Response(status_code=204)
