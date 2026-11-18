"""iOS app API: financial assistance check + letter (free, works on locked bills) and the user's wins."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

import config
import debt_fighter
import mobile_auth
from compliance import log_audit
from db import get_db
from mobile_routes import ok

router = APIRouter(prefix="/api/m")


def _household(payload: dict) -> tuple[float, int]:
    income, size = payload.get("income"), payload.get("household_size")
    if not isinstance(income, (int, float)) or isinstance(income, bool) or income <= 0:
        raise HTTPException(400, "income must be a positive number")
    if not isinstance(size, int) or isinstance(size, bool) or not 1 <= size <= config.MAX_HOUSEHOLD_SIZE:
        raise HTTPException(400, f"household_size must be between 1 and {config.MAX_HOUSEHOLD_SIZE}")
    return float(income), size


@router.post("/bills/{bill_id}/assistance")
async def assistance_check(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    income, size = _household(payload)
    result = debt_fighter.check_charity_care(income, size)
    return ok({key: result[key] for key in ("fpl_percentage", "eligibility", "message", "documents_needed")})


@router.post("/bills/{bill_id}/assistance-letter")
async def assistance_letter(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    income, size = _household(payload)
    name = str(payload.get("name") or "[Your Name]")[: config.MAX_NAME_LEN]
    address = str(payload.get("address") or "[Your Address]")[: config.MAX_ADDRESS_LEN]
    account = str(payload.get("account_number") or "[Account Number]")[: config.MAX_ACCOUNT_NUMBER_LEN]
    with get_db() as db:
        bill = db.execute("SELECT provider_name, total_patient_owes, total_charged, bill_date FROM bills WHERE id = ?",
                          (bill_id,)).fetchone()
    if not bill:
        raise HTTPException(404, "Bill not found")
    owed = bill["total_patient_owes"] or bill["total_charged"] or 0
    result = debt_fighter.generate_charity_care_letter(
        user_name=name, user_address=address, hospital_name=bill["provider_name"] or "[Hospital]",
        hospital_address="[Hospital billing address]", account_number=account, bill_amount=f"{owed:.2f}",
        income=income, household_size=size, date_of_service=bill["bill_date"] or "", with_enclosures=False,
    )
    log_audit(action="mobile_assistance_letter", resource_type="bill", resource_id=str(bill_id))
    return ok({"letter": result["letter_text"], "fpl_percentage": result["fpl_percentage"], "bill_id": bill_id})


@router.get("/wins")
async def wins(device_id: str = Depends(mobile_auth.device_from_request)):
    with get_db() as db:
        row = db.execute(
            "SELECT COUNT(*) AS reports, COALESCE(SUM(o.actual_savings), 0) AS saved "
            "FROM dispute_outcomes o JOIN bill_access_sessions bas ON bas.bill_id = o.bill_id "
            "WHERE bas.session_id = ?", (device_id,),
        ).fetchone()
    return ok({"reports": row["reports"], "total_saved": round(row["saved"], 2)})
