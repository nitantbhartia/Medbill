"""iOS app API: scan a bill, read bills, dispute letter, phone script, delete a bill."""

from __future__ import annotations

import re

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

import config
import mobile_auth
import mobile_purchases
import mobile_view
import scan_pipeline
import scanner
from access_control import grant_bill_access
from api import ALLOWED_MIME_TYPES, _check_rate_limit
from compliance import log_audit
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


@router.post("/scan")
async def scan(
    pages: list[UploadFile] = File(...),
    zip_code: str = Form(...),
    device_id: str = Depends(mobile_auth.device_from_request),
):
    if not pages or len(pages) > config.MOBILE_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.MOBILE_SCAN_MAX_PAGES} pages.")
    if not re.fullmatch(r"\d{5}", zip_code.strip()):
        raise HTTPException(400, "zip_code must be a 5-digit US ZIP code")
    if not _check_rate_limit(f"m-scan:{device_id}"):
        raise HTTPException(429, f"Too many scans. Max {config.RATE_LIMIT_REQUESTS} per hour.")
    images = await _read_pages(pages)
    try:
        bill_id, extracted, analysis = scan_pipeline.run_scan(images, zip_code.strip(), None, None)
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Bill reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, f"We couldn't read that bill: {exc}") from exc
    except scan_pipeline.AnalysisFailed as exc:
        raise HTTPException(500, "We couldn't analyze that bill.") from exc
    grant_bill_access(device_id, bill_id)
    log_audit(
        action="mobile_scan", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id,
        metadata={"findings": analysis.get("total_findings", 0), "pages": len(images)},
    )
    view = mobile_view.build_bill_view(bill_id, device_id)
    view["extraction_quality"] = (extracted.get("_extraction_meta") or {}).get("quality_score")
    return ok(view)


@router.get("/bills")
async def list_bills(device_id: str = Depends(mobile_auth.device_from_request)):
    return ok({"bills": mobile_view.list_bill_summaries(device_id)})


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
