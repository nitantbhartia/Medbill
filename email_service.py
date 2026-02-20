import json
import logging
import re
import urllib.error
import urllib.request

import config

log = logging.getLogger(__name__)

SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"


def send_email(to: str, subject: str, html_body: str, text_body: str = "") -> bool:
    """
    Send an email via SendGrid.
    Returns True on success, False if SendGrid is not configured.
    Raises RuntimeError if configured but delivery fails.
    """
    if not config.SENDGRID_API_KEY:
        log.warning("SENDGRID_API_KEY not set — email to %s not sent", to)
        return False

    payload = {
        "personalizations": [{"to": [{"email": to}]}],
        "from": {"email": config.EMAIL_FROM_ADDRESS, "name": config.EMAIL_FROM_NAME},
        "subject": subject,
        "content": [
            {"type": "text/plain", "value": text_body or _strip_tags(html_body)},
            {"type": "text/html", "value": html_body},
        ],
    }

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        SENDGRID_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {config.SENDGRID_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 202:
                return True
            raise RuntimeError(f"SendGrid returned unexpected status {resp.status}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        log.error("SendGrid HTTP error %s: %s", e.code, body)
        raise RuntimeError(f"SendGrid error {e.code}: {body}") from e
    except OSError as e:
        log.error("SendGrid network error: %s", e)
        raise RuntimeError(f"Email delivery failed: {e}") from e


def _strip_tags(html: str) -> str:
    """Minimal HTML tag stripper for plain-text fallback."""
    return re.sub(r"<[^>]+>", "", html).strip()
