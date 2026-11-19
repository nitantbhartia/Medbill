"""B14.8: email a bill to your private BillKarma address and it appears in My bills."""

import logging
import re
import secrets

import config
import mobile_accounts
import reply_reader
import scan_pipeline
from access_control import grant_bill_access
from db import get_db

log = logging.getLogger(__name__)
TOKEN_IN_ADDRESS = re.compile(r"bills\+([a-z0-9]{8,32})@", re.IGNORECASE)


def address_for(device_id: str) -> str:
    with get_db() as db:
        row = db.execute("SELECT inbound_token FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()
        token = row["inbound_token"] if row else None
        if not token:
            token = secrets.token_hex(6)
            db.execute("UPDATE mobile_devices SET inbound_token = ? WHERE device_id = ?", (token, device_id))
    return f"bills+{token}@{config.INBOUND_DOMAIN}"


def token_from(addresses: list[str]) -> str | None:
    for address in addresses:
        match = TOKEN_IN_ADDRESS.search(address or "")
        if match:
            return match.group(1).lower()
    return None


def _over_daily_limit(device_id: str) -> bool:
    with get_db() as db:
        count = db.execute("SELECT COUNT(*) AS n FROM inbound_mail_log WHERE device_id = ? AND created_at >= datetime('now', '-1 day')",
                           (device_id,)).fetchone()["n"]
        if count < config.INBOUND_MAX_PER_DAY:
            db.execute("INSERT INTO inbound_mail_log (device_id) VALUES (?)", (device_id,))
    return count >= config.INBOUND_MAX_PER_DAY


def process(email_id: str, to_addresses: list[str]) -> str:
    """Make a bill from an email's attachments. Returns 'created', 'dropped' (unknown address), 'rate_limited' or 'no_attachment'."""
    token = token_from(to_addresses)
    with get_db() as db:
        device = db.execute("SELECT device_id, zip_code FROM mobile_devices WHERE inbound_token = ?", (token,)).fetchone() if token else None
    if not device:
        log.warning("Dropped inbound email %s: no device has that address", email_id)
        return "dropped"
    if _over_daily_limit(device["device_id"]):
        log.warning("Dropped inbound email %s: device is over %d bills a day", email_id, config.INBOUND_MAX_PER_DAY)
        return "rate_limited"
    email = reply_reader.fetch_inbound_email(email_id)
    wanted = [a for a in email["attachments"] if a.get("content_type") in config.UPLOAD_MIME_TYPES][:config.MOBILE_SCAN_MAX_PAGES]
    images = [(reply_reader.fetch_attachment(email_id, a["id"]), a["content_type"]) for a in wanted]
    max_bytes = config.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    images = [(data, mime) for data, mime in images if len(data) <= max_bytes]
    if not images:
        return "no_attachment"
    bill_id, _, _ = scan_pipeline.run_scan(images, device["zip_code"] or "", None, None, input_kind="email")
    grant_bill_access(device["device_id"], bill_id)
    mobile_accounts.share_bill_with_account(device["device_id"], bill_id)
    return "created"
