"""iOS app API: unlock a bill with an in-app purchase, and the RevenueCat webhook."""

from __future__ import annotations

import secrets

from fastapi import APIRouter, Depends, HTTPException, Request

import cc_purchases
import config
import mobile_auth
import mobile_purchases
import mobile_view
from mobile_routes import ok

router = APIRouter(prefix="/api/m")


@router.post("/bills/{bill_id}/unlock")
async def unlock_bill(bill_id: int, payload: dict, device_id: str = Depends(mobile_auth.device_from_request)):
    mobile_auth.require_device_bill_access(device_id, bill_id)
    transaction_id = str(payload.get("transaction_id") or "").strip()
    if transaction_id:
        mobile_purchases.unlock_with_purchase(device_id, bill_id, transaction_id)
    elif not mobile_purchases.unlock_with_plus(device_id, bill_id, force_refresh=True):
        raise HTTPException(402, "BillKarma Plus is not active on this device")
    return ok(mobile_view.build_bill_view(bill_id, device_id))


@router.post("/revenuecat/webhook")
async def revenuecat_webhook(request: Request, payload: dict):
    expected = config.REVENUECAT_WEBHOOK_AUTH
    presented = request.headers.get("authorization", "")
    if not expected or not secrets.compare_digest(presented, expected):
        raise HTTPException(401, "Invalid webhook authorization")
    event = payload.get("event") or {}
    mobile_purchases.handle_webhook_event(event)
    cc_purchases.handle_webhook_event(event)
    return ok({"ok": True})
