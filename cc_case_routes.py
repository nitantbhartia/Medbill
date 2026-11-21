"""ClaimCoach API: scan a denial letter, confirm it, unlock the kit, build the letter, track the appeal."""

from __future__ import annotations

from datetime import date

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

import appeal_kit
import appeal_rules
import cc_cases
import cc_classify
import cc_extract
import cc_purchases
import cc_send
import cc_view
import config
import mobile_auth
import scanner
from api import _check_rate_limit
from appeal_letter import PLAN_TYPES, SERVICE_TIMINGS, build_appeal_letter
from compliance import log_audit
from mobile_bill_routes import _read_pages
from mobile_routes import ok

router = APIRouter(prefix="/api/cc")

FOR_WHOM = ("self", "someone_else")
OUTCOMES = ("overturned", "partial", "upheld")
SEND_CHANNELS = ("fax", "mail")
NO_NEXT_LEVEL = "This appeal has no next level yet"


def _choice(name: str, value: str, allowed) -> str | None:
    if value and value not in allowed:
        raise HTTPException(400, f"Unknown value for {name}")
    return value or None


@router.post("/cases")
async def create_case(
    pages: list[UploadFile] = File(...),
    eob_pages: list[UploadFile] = File(default=[]),
    for_whom: str = Form(default="self"),
    plan_type: str = Form(default=""),
    service_timing: str = Form(default=""),
    device_id: str = Depends(mobile_auth.device_from_request),
):
    if not pages or len(pages) > config.CC_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.CC_SCAN_MAX_PAGES} pages.")
    if len(eob_pages) > config.CC_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send at most {config.CC_SCAN_MAX_PAGES} insurance statement pages.")
    _choice("for_whom", for_whom, FOR_WHOM)
    plan_answer = _choice("plan_type", plan_type, PLAN_TYPES)
    timing_answer = _choice("service_timing", service_timing, SERVICE_TIMINGS)
    if not _check_rate_limit(f"cc-scan:{device_id}", config.CC_SCAN_LIMIT_PER_HOUR):
        raise HTTPException(429, "Too many letters scanned. Try again in a bit.")
    images = await _read_pages(pages)
    eob_images = await _read_pages(eob_pages)
    try:
        extracted = cc_extract.read_denial_letter(images, eob_images or None)
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Letter reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, "We couldn't read that letter. Try clearer photos.") from exc
    reason_key = cc_classify.denial_reason(extracted)
    plan, plan_unsure = cc_classify.plan_type(extracted, plan_answer)
    confirm = cc_extract.needs_confirmation(extracted) + (["plan_type"] if plan_unsure else [])
    case_id = cc_cases.create_case(
        device_id, for_whom or "self", extracted, plan, cc_classify.service_timing(extracted, timing_answer),
        reason_key, cc_classify.plain_reason(extracted, reason_key), confirm,
    )
    cc_cases.reroute(case_id)
    log_audit("cc_scan", "cc_case", str(case_id), metadata={"pages": len(images)})
    return ok(cc_view.build_case_view(case_id))


@router.get("/cases")
async def list_cases(device_id: str = Depends(mobile_auth.device_from_request)):
    return ok({"cases": [cc_view.case_summary(case) for case in cc_cases.list_cases(device_id)]})


@router.get("/cases/{case_id}")
async def get_case(case_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    cc_cases.require_case(device_id, case_id)
    return ok(cc_view.build_case_view(case_id))


@router.patch("/cases/{case_id}")
async def confirm_case(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    cc_cases.update_confirmed(cc_cases.require_case(device_id, case_id), payload)
    return ok(cc_view.build_case_view(case_id))


@router.delete("/cases/{case_id}")
async def delete_case(case_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    cc_cases.require_case(device_id, case_id)
    cc_cases.delete_case(case_id)
    log_audit("cc_delete_case", "cc_case", str(case_id))
    return ok({"deleted": True})


@router.post("/cases/{case_id}/unlock")
async def unlock_case(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    cc_cases.require_case(device_id, case_id)
    transaction_id = str(payload.get("transaction_id") or "").strip()
    if transaction_id:
        cc_purchases.unlock_with_purchase(device_id, case_id, transaction_id)
    elif not cc_purchases.unlock_with_plus(device_id, case_id):
        raise HTTPException(402, "ClaimCoach Plus is not active on this device")
    return ok(cc_view.build_case_view(case_id))


def _next_level_for(case: dict) -> dict:
    decided_on = date.fromisoformat(case["decided_at"]) if case["decided_at"] else date.today()
    level = appeal_rules.next_level(case["plan_type"], decided_on) if case["outcome"] == "upheld" else None
    if not level:
        raise HTTPException(400, NO_NEXT_LEVEL)
    return level


@router.post("/cases/{case_id}/letter")
async def build_letter(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    case = cc_cases.require_case(device_id, case_id)
    if not cc_purchases.is_unlocked(case_id):
        raise HTTPException(402, "Unlock this appeal to get the letter")
    name = str(payload.get("name") or "").strip()
    if not name:
        raise HTTPException(400, "name is required")
    letter_case = cc_cases.letter_case(case, name, str(payload.get("member_id") or "").strip())
    paragraph_range = None
    if payload.get("next_level") is True:
        letter_text = appeal_kit.build_external_review_request(letter_case, _next_level_for(case))
    else:
        paragraph = appeal_kit.case_paragraph(letter_case, str(payload.get("extra_facts") or ""))
        readable = {key: appeal_kit._pretty_date(letter_case[key]) or letter_case[key] for key in ("denial_date", "service_date")}
        letter_text = build_appeal_letter({**letter_case, **readable, "case_paragraph": paragraph})
        start = letter_text.find(paragraph) if paragraph else -1
        paragraph_range = [start, start + len(paragraph)] if start >= 0 else None
    cc_cases.save_letter(case_id, letter_text)
    return ok({
        "letter_text": letter_text,
        "case_paragraph_range": paragraph_range,
        "doctor_request": appeal_kit.build_doctor_request(letter_case),
        "checklist": appeal_kit.evidence_checklist(case["denial_reason"] or "other"),
        "phone_script": appeal_kit.phone_script(letter_case),
    })


@router.post("/cases/{case_id}/sent")
async def mark_sent(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    case = cc_cases.require_case(device_id, case_id)
    if payload.get("channel") != "self":
        raise HTTPException(400, "channel must be self")
    try:
        sent_on = date.fromisoformat(str(payload["date"])) if payload.get("date") else date.today()
    except ValueError as exc:
        raise HTTPException(400, "date must be like 2026-10-12") from exc
    if sent_on > date.today():
        raise HTTPException(400, "date can't be in the future")
    cc_cases.record_sent(case, "self", sent_on)
    return ok(cc_view.build_case_view(case_id))


@router.post("/cases/{case_id}/send")
async def send_case(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    if not config.CC_SEND_FOR_ME_ENABLED:
        raise HTTPException(404, "Not found")
    case = cc_cases.require_case(device_id, case_id)
    if not cc_purchases.is_unlocked(case_id):
        raise HTTPException(402, "Unlock this appeal to send the letter")
    channel = payload.get("channel")
    if channel not in SEND_CHANNELS:
        raise HTTPException(400, "channel must be fax or mail")
    result = cc_send.send_for_me(case, channel, str(payload.get("approved_text_hash") or ""), str(payload.get("mailing_address") or ""))
    return ok(result)


@router.post("/cases/{case_id}/outcome")
async def report_outcome(case_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    case = cc_cases.require_case(device_id, case_id)
    outcome = payload.get("outcome")
    if outcome not in OUTCOMES:
        raise HTTPException(400, "outcome must be overturned, partial or upheld")
    recovered = payload.get("amount_recovered")
    if recovered is not None and (isinstance(recovered, bool) or not isinstance(recovered, (int, float)) or recovered < 0):
        raise HTTPException(400, "amount_recovered must be a number of 0 or more")
    cc_cases.record_outcome(case, outcome, recovered)
    return ok(cc_view.build_case_view(case_id))
