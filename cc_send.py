"""ClaimCoach "send for me": fax or certified mail of the letter the user approved. Off unless CC_SEND_FOR_ME_ENABLED."""

from __future__ import annotations

import hashlib
from datetime import date

from fastapi import HTTPException

import cc_cases
import config
import debt_fighter
import fax
from db import get_db

PROVIDER_ERROR = "We couldn't send your letter right now. Please try again."
MAIL_DESCRIPTION = "ClaimCoach appeal letter"
MAIL_RECIPIENT = "Appeals Department"


def _fax(extracted: dict, letter_text: str) -> tuple[str, str | None]:
    if not extracted.get("appeal_fax"):
        raise HTTPException(400, "We don't have a fax number for this appeal")
    try:
        return fax.send_fax(extracted["appeal_fax"], letter_text), None
    except ValueError as exc:
        raise HTTPException(400, "The fax number on this appeal isn't one we can send to") from exc
    except RuntimeError as exc:
        raise HTTPException(502, PROVIDER_ERROR) from exc


def _mail(extracted: dict, letter_text: str, mailing_address: str) -> tuple[str, str | None]:
    if not extracted.get("appeal_address"):
        raise HTTPException(400, "We don't have a mailing address for this appeal")
    if not mailing_address.strip():
        raise HTTPException(400, "Add your mailing address so the letter has a return address")
    if not extracted.get("patient_name"):
        raise HTTPException(400, "We need the patient's name for the return address")
    try:
        result = debt_fighter.send_certified_letter(
            MAIL_DESCRIPTION, extracted["patient_name"], mailing_address.strip(),
            MAIL_RECIPIENT, extracted["appeal_address"], letter_text, config.LOB_API_KEY,
        )
    except RuntimeError as exc:
        raise HTTPException(502, PROVIDER_ERROR) from exc
    return result["lob_id"], result["tracking_number"]


def send_for_me(case: dict, channel: str, approved_text_hash: str, mailing_address: str = "") -> dict:
    """Send the stored letter. Only text whose SHA-256 matches what the user approved goes out."""
    letter_text = case["letter_text"]
    if not letter_text:
        raise HTTPException(400, "Build your letter before sending it")
    if hashlib.sha256(letter_text.encode()).hexdigest() != approved_text_hash:
        raise HTTPException(400, "The letter changed since you approved it. Review it again")
    if channel == "fax":
        provider_ref, tracking_number = _fax(case["extracted"], letter_text)
    else:
        provider_ref, tracking_number = _mail(case["extracted"], letter_text, mailing_address)
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO cc_sends (case_id, channel, provider_ref, tracking_number, status, approved_text_hash) "
            "VALUES (?, ?, ?, ?, 'submitted', ?)",
            (case["id"], channel, provider_ref, tracking_number, approved_text_hash),
        )
    cc_cases.record_sent(case, channel, date.today())
    return {"send_id": cursor.lastrowid, "status": "submitted"}
