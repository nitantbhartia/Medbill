"""iOS app API: Sign in with Apple, account status, email a letter copy, delete the account."""

from __future__ import annotations

import html

from fastapi import APIRouter, Depends, HTTPException

import config
import email_service
import mobile_accounts
import mobile_auth
import mobile_purchases
from api import _check_rate_limit
from compliance import log_audit
from dispute_workflow import build_dispute_letter
from mobile_routes import delete_bill_everywhere, ok

router = APIRouter(prefix="/api/m")


def _account_view(account: dict | None) -> dict:
    if not account:
        return {"signed_in": False, "email": None}
    return {"signed_in": True, "email": account.get("email")}


@router.post("/auth/apple")
async def sign_in_with_apple(payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    identity_token = str(payload.get("identity_token") or "")
    if not identity_token:
        raise HTTPException(400, "identity_token is required")
    account = mobile_accounts.sign_in(device_id, identity_token, str(payload.get("authorization_code") or ""))
    return ok(_account_view(account))


@router.get("/account")
async def get_account(device_id: str = Depends(mobile_auth.device_from_request)):
    return ok(_account_view(mobile_accounts.account_for_device(device_id)))


@router.delete("/account")
async def delete_account(device_id: str = Depends(mobile_auth.device_from_request)):
    account = mobile_accounts.account_for_device(device_id)
    if not account:
        raise HTTPException(403, "Sign in with Apple first")
    mobile_accounts.delete_account(account, delete_bill_everywhere)
    log_audit(action="mobile_delete_account", resource_type="account", resource_id=str(account["id"]))
    return ok({"deleted": True})


@router.post("/bills/{bill_id}/email-letter")
async def email_letter(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    account = mobile_accounts.account_for_device(device_id)
    if not account or not account.get("email"):
        raise HTTPException(403, "Sign in with Apple to email your letter.")
    mobile_purchases.ensure_unlocked(device_id, bill_id)
    if not _check_rate_limit(f"m-email:{device_id}"):
        raise HTTPException(429, "Too many emails. Try again in a bit.")
    letter = build_dispute_letter(
        bill_id, finding_ids=payload.get("finding_ids") or None,
        requestor_name=str(payload.get("requestor_name") or "[Your Name]")[: config.MAX_NAME_LEN],
        account_number=str(payload.get("account_number") or "[Account Number]")[: config.MAX_ACCOUNT_NUMBER_LEN],
    )
    if not letter:
        raise HTTPException(404, "Bill not found or no findings available")
    body = html.escape(letter["letter"])
    sent = email_service.send_email(
        to=account["email"], subject=f"Your dispute letter for {letter['provider']}",
        html_body=f"<p>Your BillKarma dispute letter is below. Fill in anything in [brackets] before you send it.</p>"
                  f"<pre style='font-family:serif;white-space:pre-wrap;'>{body}</pre>",
        text_body=letter["letter"],
    )
    if not sent:
        raise HTTPException(503, "Email isn't available right now. Use Share as PDF instead.")
    return ok({"sent": True})
