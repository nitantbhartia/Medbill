"""Where to send a dispute letter: contact details printed on the bill first, then the hospital directory."""

from __future__ import annotations

import re

import config
from analyzer import find_hospital_match
from db import get_db

EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}")


def _clean_phone(value) -> str | None:
    digits = re.sub(r"\D", "", str(value or ""))
    return str(value).strip() if len(digits) in range(config.BILLING_PHONE_DIGITS[0], config.BILLING_PHONE_DIGITS[1] + 1) else None


def _clean_email(value) -> str | None:
    text = str(value or "").strip()
    return text if EMAIL.fullmatch(text) else None


def _clean_address(value) -> str | None:
    text = str(value or "").strip()
    return text[: config.MAX_BILLING_ADDRESS_LEN] if len(text) >= 8 else None


def store_from_extraction(bill_id: int, extracted: dict) -> None:
    """Keep only contact details that look real. Nothing is filled in when the bill doesn't print them."""
    with get_db() as db:
        db.execute("UPDATE bills SET billing_phone = ?, billing_email = ?, billing_address = ? WHERE id = ?",
                   (_clean_phone(extracted.get("billing_phone")), _clean_email(extracted.get("billing_email")),
                    _clean_address(extracted.get("billing_address")), bill_id))


def contact_for(bill: dict) -> dict:
    """Phone, email and address, each from the bill when printed, otherwise from the hospital directory.
    Email only ever comes from the bill."""
    contact = {"provider_name": bill.get("provider_name"), "phone": bill.get("billing_phone"),
               "email": bill.get("billing_email"), "address": bill.get("billing_address"), "source": "bill"}
    if contact["phone"] and contact["address"]:
        return contact
    match = find_hospital_match(bill.get("provider_name") or "", bill.get("zip_code"))
    if not match:
        contact["source"] = "bill" if (contact["phone"] or contact["address"]) else None
        return contact
    with get_db() as db:
        row = db.execute("SELECT phone, address, city, state, zip FROM hospitals WHERE facility_id = ?",
                         (match["facility_id"],)).fetchone()
    if row:
        from_directory = (not contact["phone"] and row["phone"]) or (not contact["address"] and row["address"])
        contact["phone"] = contact["phone"] or row["phone"]
        if not contact["address"] and row["address"]:
            contact["address"] = ", ".join(part for part in (row["address"], row["city"], f"{row['state']} {row['zip'] or ''}".strip()) if part)
        if from_directory:
            contact["source"] = "directory"
    return contact


def mark_sent(bill_id: int, channel: str) -> None:
    with get_db() as db:
        db.execute("UPDATE bills SET sent_at = CURRENT_TIMESTAMP, sent_channel = ? WHERE id = ?", (channel, bill_id))
