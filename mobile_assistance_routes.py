"""iOS app API: financial assistance check + letter (free, works on locked bills) and the user's wins.

Household income is financial data, so it never reaches the server: the phone computes the poverty-level
percentage from /assistance/guidelines and sends only that percentage and the household size."""

from __future__ import annotations

import logging
from datetime import date

from fastapi import APIRouter, Depends, HTTPException

import assistance_policies
import config
import debt_fighter
import mobile_auth
from compliance import log_audit
from db import get_db
from mobile_routes import ok

router = APIRouter(prefix="/api/m")
log = logging.getLogger(__name__)

CALIFORNIA_RULE = (
    "Under California law, if you are uninsured or your medical costs are high and your income is at or below "
    "400% of the federal poverty level, you are eligible to apply for the hospital's charity care or discount payment policy."
)
CALIFORNIA_LIMIT = 400
OTHER_STATES_NOTE = "Each hospital sets its own limits."
RURAL_CA_NOTE = "Starting July 1, 2027, rural California hospitals may set lower income limits."

if date.today().year > config.FPL_YEAR:
    log.warning("Federal poverty guidelines in config.py are for %s. Update FPL_* from HHS ASPE.", config.FPL_YEAR)


def _bill_state(bill_id: int) -> str | None:
    """The hospital's state, matched by name first and then by the bill's zip code."""
    with get_db() as db:
        row = db.execute(
            "SELECT h.state FROM bills b JOIN hospitals h ON lower(h.name) = lower(b.provider_name) "
            "WHERE b.id = ? LIMIT 1", (bill_id,)).fetchone()
        if not row:
            row = db.execute(
                "SELECT h.state FROM bills b JOIN hospitals h ON h.zip = b.zip_code WHERE b.id = ? LIMIT 1",
                (bill_id,)).fetchone()
    return row["state"] if row else None


def _household(payload: dict) -> tuple[int, int]:
    percent, size = payload.get("fpl_percentage"), payload.get("household_size")
    if not isinstance(percent, int) or isinstance(percent, bool) or not 0 <= percent <= config.MAX_FPL_PERCENT:
        raise HTTPException(400, f"fpl_percentage must be a whole number from 0 to {config.MAX_FPL_PERCENT}")
    if not isinstance(size, int) or isinstance(size, bool) or not 1 <= size <= config.MAX_HOUSEHOLD_SIZE:
        raise HTTPException(400, f"household_size must be between 1 and {config.MAX_HOUSEHOLD_SIZE}")
    return percent, size


@router.get("/assistance/guidelines")
async def guidelines(device_id: str = Depends(mobile_auth.device_from_request)):
    return ok({"year": config.FPL_YEAR, "one_person": config.FPL_ONE_PERSON,
               "each_additional": config.FPL_EACH_ADDITIONAL_PERSON})


@router.post("/bills/{bill_id}/assistance")
async def assistance_check(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    percent, size = _household(payload)
    result = debt_fighter.charity_care_for_percent(percent, size)
    in_california = _bill_state(bill_id) == "CA"
    state_rule = CALIFORNIA_RULE if in_california and percent <= CALIFORNIA_LIMIT else None
    note = f"{OTHER_STATES_NOTE} {RURAL_CA_NOTE}" if in_california else OTHER_STATES_NOTE
    return ok({"fpl_percentage": percent, "eligibility": result["eligibility"], "message": result["message"],
               "state_rule": state_rule, "note": note, "documents_needed": result["documents_needed"]})


@router.post("/bills/{bill_id}/assistance-letter")
async def assistance_letter(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    percent, size = _household(payload)
    name = str(payload.get("name") or "[Your Name]")[: config.MAX_NAME_LEN]
    address = str(payload.get("address") or "[Your Address]")[: config.MAX_ADDRESS_LEN]
    account = str(payload.get("account_number") or "[Account Number]")[: config.MAX_ACCOUNT_NUMBER_LEN]
    with get_db() as db:
        bill = db.execute("SELECT provider_name, total_patient_owes, total_charged, bill_date FROM bills WHERE id = ?",
                          (bill_id,)).fetchone()
    if not bill:
        raise HTTPException(404, "Bill not found")
    owed = bill["total_patient_owes"] or bill["total_charged"] or 0
    people = f"{size} person{'s' if size > 1 else ''}"
    letter = f"""{name}
{address}

{date.today():%B %d, %Y}

{bill["provider_name"] or "[Hospital]"}
Financial Assistance / Patient Financial Services

Re: Financial Assistance Application, Account #{account}

Dear Financial Assistance Department:

I am requesting consideration under your hospital's Financial Assistance Program for the balance of ${owed:,.2f} on the account above{f" for services on {bill['bill_date']}" if bill["bill_date"] else ""}.

My household has {people}, and our income is approximately {percent}% of the {config.FPL_YEAR} Federal Poverty Level. I can provide proof of income on request.

Please send me your Financial Assistance Application and a list of the documents you require. I ask that collection activity on this account be paused while my application is under review.

Sincerely,
{name}"""
    log_audit(action="mobile_assistance_letter", resource_type="bill", resource_id=str(bill_id))
    return ok({"letter": letter, "bill_id": bill_id})


@router.get("/wins")
async def wins(device_id: str = Depends(mobile_auth.device_from_request)):
    """Verified savings only: the best verified result per bill, and only when money came off."""
    with get_db() as db:
        row = db.execute(
            "SELECT COUNT(*) AS reports, COALESCE(SUM(saved), 0) AS total FROM ("
            "SELECT MAX(o.actual_savings) AS saved FROM dispute_outcomes o "
            "JOIN bill_access_sessions bas ON bas.bill_id = o.bill_id WHERE bas.session_id = ? AND o.verified = 1 "
            "GROUP BY o.bill_id HAVING MAX(o.actual_savings) > 0)", (device_id,),
        ).fetchone()
    return ok({"reports": row["reports"], "total_saved": round(row["total"], 2)})


POLICY_FIELDS = ("free_care_max_fpl", "discount_max_fpl", "discount_rule", "asset_test", "presumptive_programs",
                 "required_documents", "application_deadline", "contact_phone")


@router.get("/assistance/policy/{facility_id}")
async def hospital_policy(facility_id: str, device_id: str = Depends(mobile_auth.device_from_request)):
    """One hospital's own charity care terms, each with the sentence it came from. No income is sent or stored."""
    policy = assistance_policies.get_policy(facility_id)
    if not policy:
        raise HTTPException(404, "No policy on file for this hospital")
    reviewed = policy["review_status"] == "reviewed"
    return ok({
        "hospital_name": policy["hospital_name"], "source_url": policy["source_url"],
        "effective_date": policy["effective_date"], "review_status": policy["review_status"],
        "label": f"From {policy['hospital_name']}'s policy" + ("" if reviewed else " (not yet checked by BillKarma)"),
        "application_form_url": policy["application_form_url"],
        "terms": {field: {"value": policy[field], "quote": policy["evidence"].get(field)}
                  for field in POLICY_FIELDS if policy[field] not in (None, [], "")},
        "floor_note": policy["evidence"].get("discount_max_fpl_floor"),
    })
