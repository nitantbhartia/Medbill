"""iOS app API: scan a bill, read bills, dispute letter, phone script, delete a bill."""

from __future__ import annotations

import re

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

import bill_contact
import config
import line_confirmation
import eob_observations
import inbound_bills
import outcome_verification
import mobile_accounts
import mobile_auth
import mobile_purchases
import mobile_view
import scan_pipeline
import scanner
from access_control import grant_bill_access
from analyzer import infer_bill_type
from api import ALLOWED_MIME_TYPES, VALID_OUTCOMES, _check_rate_limit
from compliance import log_audit
from db import get_db
from dispute_workflow import build_dispute_letter, build_phone_script, split_script_sections
from mobile_routes import delete_bill_everywhere, ok

router = APIRouter(prefix="/api/m")


async def _read_pages(pages: list[UploadFile]) -> list[tuple[bytes, str]]:
    max_bytes = config.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    images = []
    for page in pages:
        mime = page.content_type or ""
        if mime not in ALLOWED_MIME_TYPES:
            raise HTTPException(400, f"Unsupported file type '{mime}'. Upload photos or a PDF.")
        data = await page.read()
        if len(data) > max_bytes:
            raise HTTPException(400, f"A page is larger than {config.MAX_UPLOAD_SIZE_MB} MB.")
        images.append((data, mime))
    return images


def _input_kind(images: list[tuple[bytes, str]], text_layer: str) -> str:
    if any(mime == "application/pdf" for _, mime in images):
        return "pdf_text" if text_layer.strip() else "pdf_image"
    return "photo"


@router.get("/inbound-address")
async def inbound_address(device_id: str = Depends(mobile_auth.device_from_request)):
    """The private address this device can email bills to. Created the first time it is asked for."""
    return ok({"address": inbound_bills.address_for(device_id)})


USER_FACING_PREFIXES = ("That file", "That photo", "Unsupported", "Could not decode", "The scan could not be read")


def _read_error(what: str, exc: Exception) -> str:
    """Show the reason only when we wrote it for the user; anything else stays in the logs."""
    text = str(exc)
    return f"We couldn't read that {what}: {text}" if text.startswith(USER_FACING_PREFIXES) else f"We couldn't read that {what}. Try clearer photos."


def _remember_bill_type(device_id: str, extracted: dict) -> None:
    """Bill type is no longer asked: it comes from the codes, and never overwrites an answer the user gave."""
    with get_db() as db:
        db.execute("UPDATE mobile_devices SET bill_type = ? WHERE device_id = ? AND bill_type IS NULL",
                   (infer_bill_type(extracted.get("line_items") or []), device_id))


@router.post("/scan")
async def scan(
    pages: list[UploadFile] = File(...),
    zip_code: str = Form(...),
    eob_pages: list[UploadFile] = File(default=[]),
    text_layer: str = Form(default=""),
    device_id: str = Depends(mobile_auth.device_from_request),
):
    if not pages or len(pages) > config.MOBILE_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.MOBILE_SCAN_MAX_PAGES} pages.")
    if not re.fullmatch(r"\d{5}", zip_code.strip()):
        raise HTTPException(400, "zip_code must be a 5-digit US ZIP code")
    if not _check_rate_limit(f"m-scan:{device_id}"):
        raise HTTPException(429, f"Too many scans. Max {config.RATE_LIMIT_REQUESTS} per hour.")
    if len(eob_pages) > config.MOBILE_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send at most {config.MOBILE_SCAN_MAX_PAGES} insurance statement pages.")
    images = await _read_pages(pages)
    eob_images = await _read_pages(eob_pages)
    try:
        bill_id, extracted, analysis = scan_pipeline.run_scan(images, zip_code.strip(), None, None, eob_images or None, eob_observations.consented(device_id),
                                                           text_layer, _input_kind(images, text_layer))
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Bill reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, _read_error("bill", exc)) from exc
    except scan_pipeline.AnalysisFailed as exc:
        raise HTTPException(500, "We couldn't analyze that bill.") from exc
    grant_bill_access(device_id, bill_id)
    _remember_bill_type(device_id, extracted)
    mobile_accounts.share_bill_with_account(device_id, bill_id)
    log_audit(
        action="mobile_scan", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id,
        metadata={"findings": analysis.get("total_findings", 0), "pages": len(images)},
    )
    view = mobile_view.build_bill_view(bill_id, device_id)
    view["extraction_quality"] = (extracted.get("_extraction_meta") or {}).get("quality_score")
    return ok(view)


@router.get("/bills")
async def list_bills(device_id: str = Depends(mobile_auth.device_from_request)):
    return ok({"bills": mobile_view.list_bill_summaries(device_id),
               "free_checks_remaining": mobile_view.free_checks_remaining(device_id)})


@router.get("/bills/{bill_id}")
async def get_bill(bill_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    return ok(mobile_view.build_bill_view(bill_id, device_id))


@router.post("/bills/{bill_id}/letter")
async def make_letter(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    mobile_purchases.ensure_unlocked(device_id, bill_id)
    finding_ids = payload.get("finding_ids") or []
    name = str(payload.get("requestor_name") or "[Your Name]")
    account = str(payload.get("account_number") or "[Account Number]")
    if not isinstance(finding_ids, list):
        raise HTTPException(400, "finding_ids must be an array")
    if len(name) > config.MAX_NAME_LEN:
        raise HTTPException(400, f"requestor_name exceeds {config.MAX_NAME_LEN} characters")
    if len(account) > config.MAX_ACCOUNT_NUMBER_LEN:
        raise HTTPException(400, f"account_number exceeds {config.MAX_ACCOUNT_NUMBER_LEN} characters")
    result = build_dispute_letter(bill_id, finding_ids=finding_ids or None, requestor_name=name, account_number=account)
    if not result:
        raise HTTPException(404, "Bill not found or no findings available")
    return ok({**result, "bill_id": bill_id})


@router.get("/bills/{bill_id}/phone-script")
async def phone_script(bill_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    mobile_purchases.ensure_unlocked(device_id, bill_id)
    script = build_phone_script(bill_id)
    if not script:
        raise HTTPException(404, "Bill not found or no findings")
    return ok({"script": script, "sections": split_script_sections(script)})


@router.delete("/bills/{bill_id}")
async def delete_bill(bill_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    delete_bill_everywhere(bill_id)
    log_audit(action="mobile_delete_bill", resource_type="bill", resource_id=str(bill_id))
    return ok({"deleted": True})


@router.post("/bills/{bill_id}/outcome")
async def report_outcome(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    """The user tells us what the hospital did. Self-reported until they verify it with the new statement."""
    mobile_auth.require_device_bill_access(device_id, bill_id)
    outcome = payload.get("outcome")
    final_owed = payload.get("final_patient_owes", 0)
    if outcome not in VALID_OUTCOMES:
        raise HTTPException(400, f"outcome must be one of: {', '.join(sorted(VALID_OUTCOMES))}")
    if not isinstance(final_owed, (int, float)) or isinstance(final_owed, bool) or final_owed < 0:
        raise HTTPException(400, "final_patient_owes must be a non-negative number")
    reason = payload.get("reason_category")
    if reason is not None and reason not in config.REJECTION_REASONS:
        raise HTTPException(400, f"reason_category must be one of: {', '.join(config.REJECTION_REASONS)}")
    bill = _bill_row(bill_id)
    saved = outcome_verification.record_reported(bill_id, bill, outcome, final_owed, reason)
    log_audit(action="mobile_report_outcome", resource_type="bill", resource_id=str(bill_id),
              metadata={"outcome": outcome, "actual_savings": saved})
    return ok({"actual_savings": saved})


@router.post("/bills/{bill_id}/outcome/verify")
async def verify_outcome(bill_id: int, pages: list[UploadFile] = File(...),
                         device_id: str = Depends(mobile_auth.device_from_request)):
    """The new statement from the hospital. If its balance is lower, the saving is verified and earns free Plus."""
    mobile_auth.require_device_bill_access(device_id, bill_id)
    if not pages or len(pages) > config.MOBILE_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.MOBILE_SCAN_MAX_PAGES} pages.")
    if not _check_rate_limit(f"m-scan:{device_id}"):
        raise HTTPException(429, f"Too many scans. Max {config.RATE_LIMIT_REQUESTS} per hour.")
    images = await _read_pages(pages)
    try:
        result = outcome_verification.verify_with_statement(bill_id, device_id, images)
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Bill reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, _read_error("statement", exc)) from exc
    log_audit(action="mobile_verify_outcome", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id,
              metadata={"verified": result["verified"]})
    return ok(result)


@router.post("/bills/{bill_id}/eob")
async def add_eob(bill_id: int, eob_pages: list[UploadFile] = File(...),
                  device_id: str = Depends(mobile_auth.device_from_request)):
    """Add an insurance statement to a bill already scanned."""
    mobile_auth.require_device_bill_access(device_id, bill_id)
    if not eob_pages or len(eob_pages) > config.MOBILE_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.MOBILE_SCAN_MAX_PAGES} pages.")
    if not _check_rate_limit(f"m-scan:{device_id}"):
        raise HTTPException(429, f"Too many scans. Max {config.RATE_LIMIT_REQUESTS} per hour.")
    images = await _read_pages(eob_pages)
    try:
        scan_pipeline.add_eob(bill_id, images, eob_observations.consented(device_id))
    except scan_pipeline.CannotRebuild as exc:
        raise HTTPException(409, "Rescan the bill together with the statement.") from exc
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Bill reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, _read_error("statement", exc)) from exc
    except scan_pipeline.AnalysisFailed as exc:
        raise HTTPException(500, "We couldn't check that statement.") from exc
    log_audit(action="mobile_add_eob", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return ok(mobile_view.build_bill_view(bill_id, device_id))


def _bill_row(bill_id: int) -> dict:
    with get_db() as db:
        row = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
    if not row:
        raise HTTPException(404, "Bill not found")
    return dict(row)


@router.get("/bills/{bill_id}/contact")
async def contact(bill_id: int, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    mobile_purchases.ensure_unlocked(device_id, bill_id)
    return ok(bill_contact.contact_for(_bill_row(bill_id)))


@router.post("/bills/{bill_id}/sent")
async def sent(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    channel = payload.get("channel")
    if channel not in config.SENT_CHANNELS:
        raise HTTPException(400, f"channel must be one of: {', '.join(sorted(config.SENT_CHANNELS))}")
    bill_contact.mark_sent(bill_id, channel)
    return ok({"sent_at": _bill_row(bill_id)["sent_at"], "channel": channel})


@router.post("/bills/{bill_id}/confirm")
async def confirm_lines(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    """The user confirms or fixes lines the scan couldn't read clearly. Lines left out stay unchecked."""
    mobile_auth.require_device_bill_access(device_id, bill_id)
    try:
        line_confirmation.apply_confirmations(bill_id, payload.get("lines"))
    except line_confirmation.InvalidConfirmation as exc:
        raise HTTPException(400, str(exc)) from exc
    except scan_pipeline.CannotRebuild as exc:
        raise HTTPException(409, "This bill can't be rechecked. Rescan it.") from exc
    log_audit(action="mobile_confirm_lines", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id,
              metadata={"lines": len(payload.get("lines") or [])})
    return ok(mobile_view.build_bill_view(bill_id, device_id))
