"""Send a plain-text fax through Phaxio."""

import base64
import json
import logging
import re
import urllib.error
import urllib.parse
import urllib.request

import config

log = logging.getLogger(__name__)

PHAXIO_FAXES_URL = "https://api.phaxio.com/v2.1/faxes"
US_NUMBER_DIGITS = 10


def to_e164(number: str) -> str:
    """Return +1XXXXXXXXXX for a US fax number, or '' if it isn't one."""
    digits = re.sub(r"\D", "", number or "")
    if len(digits) == US_NUMBER_DIGITS + 1 and digits.startswith("1"):
        digits = digits[1:]
    return f"+1{digits}" if len(digits) == US_NUMBER_DIGITS else ""


def fax_configured() -> bool:
    return bool(config.PHAXIO_API_KEY and config.PHAXIO_API_SECRET)


def send_fax(to_number: str, text: str) -> str:
    """Fax the text. Returns the Phaxio fax id. Raises ValueError for a bad number and
    RuntimeError if Phaxio refuses the fax."""
    to = to_e164(to_number)
    if not to:
        raise ValueError(f"Not a US fax number: {to_number!r}")
    body = urllib.parse.urlencode({"to": to, "string_data": text, "string_data_type": "text"}).encode()
    credentials = base64.b64encode(f"{config.PHAXIO_API_KEY}:{config.PHAXIO_API_SECRET}".encode()).decode()
    req = urllib.request.Request(
        PHAXIO_FAXES_URL, data=body, method="POST",
        headers={"Authorization": f"Basic {credentials}", "Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        log.error("Phaxio error %s sending fax to %s: %s", exc.code, to, detail)
        raise RuntimeError(f"Phaxio error {exc.code}: {detail}") from exc
    return str(result["data"]["id"])
