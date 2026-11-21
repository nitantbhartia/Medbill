"""ClaimCoach API: scan the insurer's decision letter after an upheld appeal."""

from __future__ import annotations

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

import cc_cases
import cc_decision
import cc_purchases
import cc_view
import config
import mobile_auth
import scanner
from api import _check_rate_limit
from compliance import log_audit
from mobile_bill_routes import _read_pages
from mobile_routes import ok

router = APIRouter(prefix="/api/cc")


@router.post("/cases/{case_id}/decision-letter")
async def scan_decision_letter(
    case_id: int,
    pages: list[UploadFile] = File(...),
    device_id: str = Depends(mobile_auth.device_from_request),
):
    case = cc_cases.require_case(device_id, case_id)
    if not cc_purchases.is_unlocked(case_id):
        raise HTTPException(402, "Unlock this appeal to scan the decision letter")
    if case["outcome"] != "upheld":
        raise HTTPException(409, "Record that your insurer kept its decision before scanning its letter")
    if not pages or len(pages) > config.CC_SCAN_MAX_PAGES:
        raise HTTPException(400, f"Send between 1 and {config.CC_SCAN_MAX_PAGES} pages.")
    if not _check_rate_limit(f"cc-decision:{device_id}", config.CC_SCAN_LIMIT_PER_HOUR):
        raise HTTPException(429, "Too many letters scanned. Try again in a bit.")
    images = await _read_pages(pages)
    try:
        decision = cc_decision.read_decision_letter(images)
    except scanner.ScannerNotConfigured as exc:
        raise HTTPException(503, "Letter reading is unavailable right now. Please try again later.") from exc
    except ValueError as exc:
        raise HTTPException(400, "We couldn't read that letter. Try clearer photos.") from exc
    cc_cases.record_decision_letter(case_id, decision)
    log_audit("cc_decision_scan", "cc_case", str(case_id), metadata={"pages": len(images)})
    return ok(cc_view.build_case_view(case_id))
