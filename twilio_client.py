"""Twilio over plain HTTPS (urllib), the same way fax.py talks to Phaxio. No Twilio SDK."""

import base64
import hashlib
import hmac
import json
import logging
import urllib.error
import urllib.parse
import urllib.request

import config

log = logging.getLogger(__name__)
API = "https://api.twilio.com/2010-04-01/Accounts"
VERIFY_API = "https://verify.twilio.com/v2/Services"
TIMEOUT_SECONDS = 20


class TwilioError(RuntimeError):
    """Twilio refused or did not answer."""


def configured() -> bool:
    return bool(config.TWILIO_ACCOUNT_SID and config.TWILIO_AUTH_TOKEN and config.TWILIO_FROM_NUMBER)


def _post(url: str, data: dict) -> dict:
    credentials = base64.b64encode(f"{config.TWILIO_ACCOUNT_SID}:{config.TWILIO_AUTH_TOKEN}".encode()).decode()
    request = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(), method="POST",
                                     headers={"Authorization": f"Basic {credentials}"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return json.loads(response.read())
    except (urllib.error.URLError, ValueError) as exc:
        log.error("Twilio request to %s failed: %s", url.split("/")[-1], exc)
        raise TwilioError(str(exc)) from exc


def create_call(to: str, twiml_url: str, status_url: str, time_limit_seconds: int | None = None,
                timeout_seconds: int | None = None, events: str = "completed") -> str:
    """Dial a number. Returns the call SID."""
    data = {"To": to, "From": config.TWILIO_FROM_NUMBER, "Url": twiml_url, "StatusCallback": status_url,
            "StatusCallbackEvent": events}
    if time_limit_seconds:
        data["TimeLimit"] = time_limit_seconds
    if timeout_seconds:
        data["Timeout"] = timeout_seconds
    return _post(f"{API}/{config.TWILIO_ACCOUNT_SID}/Calls.json", data)["sid"]


def update_call(call_sid: str, twiml: str) -> None:
    """Give a live call new instructions (send digits, play a message, join a conference, hang up)."""
    _post(f"{API}/{config.TWILIO_ACCOUNT_SID}/Calls/{call_sid}.json", {"Twiml": twiml})


def hang_up(call_sid: str) -> None:
    _post(f"{API}/{config.TWILIO_ACCOUNT_SID}/Calls/{call_sid}.json", {"Status": "completed"})


def start_verification(phone: str) -> None:
    _post(f"{VERIFY_API}/{config.TWILIO_VERIFY_SERVICE_SID}/Verifications", {"To": phone, "Channel": "sms"})


def check_verification(phone: str, code: str) -> bool:
    return _post(f"{VERIFY_API}/{config.TWILIO_VERIFY_SERVICE_SID}/VerificationCheck",
                 {"To": phone, "Code": code}).get("status") == "approved"


def signature_is_valid(url: str, params: dict, signature: str) -> bool:
    """Twilio signs each webhook: base64(HMAC-SHA1(auth token, url + sorted key+value pairs))."""
    payload = url + "".join(f"{key}{params[key]}" for key in sorted(params))
    expected = base64.b64encode(hmac.new(config.TWILIO_AUTH_TOKEN.encode(), payload.encode(), hashlib.sha1).digest()).decode()
    return hmac.compare_digest(expected, signature or "")
