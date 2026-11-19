"""B17.1: BillKarma calls a billing office, gets through the phone menu, waits on hold and rings the patient when a person
picks up. It never speaks for the patient, and nothing is transcribed or kept after a person answers."""

from __future__ import annotations

import hashlib
import logging
import re
from datetime import datetime, timedelta, timezone
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

import config
import mobile_purchases
import report
import twilio_client
from analyzer import find_hospital_match
from db import get_db

log = logging.getLogger(__name__)

ACTIVE_STATUSES = ("queued", "dialing", "menu", "holding", "human", "connecting", "connected")
STATE_TIMEZONES = {"CA": "America/Los_Angeles", "WA": "America/Los_Angeles", "OR": "America/Los_Angeles", "NV": "America/Los_Angeles",
                   "AZ": "America/Phoenix", "UT": "America/Denver", "CO": "America/Denver", "NM": "America/Denver", "ID": "America/Boise",
                   "MT": "America/Denver", "WY": "America/Denver", "TX": "America/Chicago", "IL": "America/Chicago",
                   "NY": "America/New_York", "FL": "America/New_York", "PA": "America/New_York", "OH": "America/New_York",
                   "GA": "America/New_York", "NC": "America/New_York", "MA": "America/New_York", "NJ": "America/New_York",
                   "MI": "America/Detroit", "WI": "America/Chicago", "MN": "America/Chicago", "MO": "America/Chicago",
                   "TN": "America/Chicago", "AL": "America/Chicago", "LA": "America/Chicago", "AK": "America/Anchorage", "HI": "Pacific/Honolulu"}
DEFAULT_TIMEZONE = "America/Los_Angeles"


class HoldCallError(Exception):
    """A request we refuse, with the HTTP status the route should answer."""

    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status, self.message = status, message


def to_e164(number: str) -> str:
    digits = re.sub(r"\D", "", number or "")
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return f"+1{digits}" if len(digits) == 10 else ""


def phone_hash(number: str) -> str:
    return hashlib.sha256(f"{config.SECRET_KEY}:{to_e164(number)}".encode()).hexdigest()


def log_status(call_id: int, status: str, detail: str = "") -> None:
    with get_db() as db:
        db.execute("UPDATE hold_calls SET status = ? WHERE id = ?", (status, call_id))
        db.execute("INSERT INTO hold_call_events (call_id, status, detail) VALUES (?, ?, ?)", (call_id, status, detail))
    log.info("hold call %s: %s %s", call_id, status, detail)


# ── Rules before a call is placed ──────────────────────────────────────────────

def hospital_timezone(bill_id: int) -> str:
    with get_db() as db:
        row = db.execute("SELECT h.state FROM bills b JOIN hospitals h ON lower(h.name) = lower(b.provider_name) "
                         "WHERE b.id = ? LIMIT 1", (bill_id,)).fetchone()
    return STATE_TIMEZONES.get(row["state"], DEFAULT_TIMEZONE) if row else DEFAULT_TIMEZONE


def next_opening(now: datetime, tz_name: str) -> datetime:
    """Now if the billing office is open (weekdays, HOLD_CALL_OPEN to HOLD_CALL_CLOSE local time), else the next opening. UTC."""
    local = now.astimezone(ZoneInfo(tz_name))
    open_at = local.replace(hour=config.HOLD_CALL_OPEN[0], minute=config.HOLD_CALL_OPEN[1], second=0, microsecond=0)
    close_at = local.replace(hour=config.HOLD_CALL_CLOSE[0], minute=config.HOLD_CALL_CLOSE[1], second=0, microsecond=0)
    if local.weekday() < 5 and open_at <= local < close_at:
        return now
    day = local if (local.weekday() < 5 and local < open_at) else local + timedelta(days=1)
    day = day.replace(hour=config.HOLD_CALL_OPEN[0], minute=config.HOLD_CALL_OPEN[1], second=0, microsecond=0)
    while day.weekday() >= 5:
        day += timedelta(days=1)
    return day.astimezone(timezone.utc)


def connected_calls(bill_id: int) -> int:
    """Calls that used up an allowance: only one that connected the patient to a person counts."""
    with get_db() as db:
        return db.execute("SELECT COUNT(*) FROM hold_calls WHERE bill_id = ? AND status = 'connected'", (bill_id,)).fetchone()[0]


def credits_available(device_id: str) -> int:
    with get_db() as db:
        return db.execute("SELECT COUNT(*) FROM hold_call_credits WHERE device_id = ? AND used = 0", (device_id,)).fetchone()[0]


def entitlement(device_id: str, bill_id: int) -> str | None:
    """Which allowance a call would use: the one included with the unlock, a Plus allowance, or a purchased call."""
    if not report.is_paid(bill_id) and not mobile_purchases.plus_is_active(device_id):
        return None
    used = connected_calls(bill_id)
    if used == 0:
        return "included"
    if mobile_purchases.plus_is_active(device_id) and used < config.PLUS_HOLD_CALLS_PER_BILL:
        return "plus"
    return "purchased" if credits_available(device_id) else None


def phone_is_verified(device_id: str, number: str) -> bool:
    oldest = (datetime.now(timezone.utc) - timedelta(days=config.PHONE_VERIFY_VALID_DAYS)).strftime("%Y-%m-%d %H:%M:%S")
    with get_db() as db:
        return db.execute("SELECT 1 FROM phone_verifications WHERE device_id = ? AND phone_hash = ? AND verified_at >= ?",
                          (device_id, phone_hash(number), oldest)).fetchone() is not None


def todays_estimated_spend_cents() -> int:
    with get_db() as db:
        return db.execute("SELECT COALESCE(SUM(MAX(cost_cents, ?)), 0) FROM hold_calls WHERE date(created_at) = date('now') "
                          "AND status != 'failed'", (config.HOLD_CALL_COST_ESTIMATE_CENTS,)).fetchone()[0]


def request_call(device_id: str, bill_id: int, hospital_number: str, user_number: str, now: datetime | None = None) -> dict:
    """Check everything, then queue the call (dialing now if the office is open). Raises HoldCallError with the reason."""
    now = now or datetime.now(timezone.utc)
    if not config.HOLD_CALLS_ENABLED or not twilio_client.configured():
        raise HoldCallError(503, "Waiting on hold isn't available yet.")
    hospital, user = to_e164(hospital_number), to_e164(user_number)
    if not hospital or not user:
        raise HoldCallError(400, "Enter 10-digit US phone numbers.")
    if not phone_is_verified(device_id, user):
        raise HoldCallError(403, "Verify your phone number first.")
    allowance = entitlement(device_id, bill_id)
    if not allowance:
        raise HoldCallError(402, "A hold call comes with your unlocked report. Unlock it or buy a call.")
    with get_db() as db:
        if db.execute("SELECT 1 FROM hold_calls WHERE device_id = ? AND status IN (?, ?, ?, ?, ?, ?, ?)",
                      (device_id, *ACTIVE_STATUSES)).fetchone():
            raise HoldCallError(409, "You already have a call in progress.")
    if todays_estimated_spend_cents() + config.HOLD_CALL_COST_ESTIMATE_CENTS > config.HOLD_CALL_DAILY_BUDGET_CENTS:
        raise HoldCallError(503, "We're at our call limit for today. Please try again tomorrow.")
    opening = next_opening(now, hospital_timezone(bill_id))
    with get_db() as db:
        bill = db.execute("SELECT provider_name, zip_code FROM bills WHERE id = ?", (bill_id,)).fetchone()
        match = find_hospital_match(bill["provider_name"] or "", bill["zip_code"]) if bill else None
        call_id = db.execute("INSERT INTO hold_calls (bill_id, device_id, hospital_number, user_number, status, scheduled_for, facility_id) "
                             "VALUES (?, ?, ?, ?, 'queued', ?, ?)",
                             (bill_id, device_id, hospital, user, opening.strftime("%Y-%m-%d %H:%M:%S"),
                              match["facility_id"] if match else None)).lastrowid
    if allowance == "purchased":
        _spend_credit(device_id)
    if opening <= now:
        dial(call_id)
    return {"call_id": call_id, "status": "dialing" if opening <= now else "queued", "starts_at": opening.isoformat(), "allowance": allowance}


def _spend_credit(device_id: str) -> None:
    with get_db() as db:
        db.execute("UPDATE hold_call_credits SET used = 1 WHERE transaction_id = (SELECT transaction_id FROM hold_call_credits "
                   "WHERE device_id = ? AND used = 0 LIMIT 1)", (device_id,))


def refund_credit(device_id: str) -> None:
    """A missed or failed call gives a purchased credit back."""
    with get_db() as db:
        db.execute("UPDATE hold_call_credits SET used = 0 WHERE transaction_id = (SELECT transaction_id FROM hold_call_credits "
                   "WHERE device_id = ? AND used = 1 ORDER BY created_at DESC LIMIT 1)", (device_id,))


# ── The call ───────────────────────────────────────────────────────────────────

def webhook_url(call_id: int, kind: str) -> str:
    return f"{config.APP_URL.rstrip('/')}/api/hold/{kind}/{call_id}"


def dial(call_id: int) -> None:
    with get_db() as db:
        call = dict(db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone())
    try:
        sid = twilio_client.create_call(call["hospital_number"], webhook_url(call_id, "twiml"), webhook_url(call_id, "status"),
                                        time_limit_seconds=config.HOLD_CALL_MAX_MINUTES * 60)
    except twilio_client.TwilioError:
        return finish(call_id, "failed", "dial_error")
    with get_db() as db:
        db.execute("UPDATE hold_calls SET hospital_call_sid = ?, started_at = CURRENT_TIMESTAMP WHERE id = ?", (sid, call_id))
    log_status(call_id, "dialing")


def listen_twiml(call_id: int) -> str:
    """What the hospital's line does when it connects: listen for speech (transcription events, no audio is kept)."""
    return ('<?xml version="1.0" encoding="UTF-8"?><Response><Start>'
            f'<Transcription statusCallbackUrl="{escape(webhook_url(call_id, "transcript"))}" track="inbound_track" partialResults="false"/>'
            '</Start><Pause length="3600"/></Response>')


def handle_utterance(call_id: int, text: str, classify_menu, classify_person) -> None:
    """One finished sentence from the hospital's line. Menus get a digit, hold audio is ignored, a person starts the connect.
    classify_menu(text) returns a digit or "WAIT"; classify_person(text) returns True for a live person starting a conversation."""
    with get_db() as db:
        call = db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone()
    if not call or call["status"] not in ("dialing", "menu", "holding"):
        return  # after a person answers, nothing is read or stored
    digit = classify_menu(text)
    if digit and digit != "WAIT" and re.fullmatch(r"[0-9*#]", digit) and call["status"] in ("dialing", "menu"):
        path = ((call["menu_path"] + ",") if call["menu_path"] else "") + digit
        with get_db() as db:
            db.execute("UPDATE hold_calls SET menu_path = ? WHERE id = ?", (path, call_id))
        log_status(call_id, "menu", f"pressed {digit}")
        twilio_client.update_call(call["hospital_call_sid"], f'<Response><Play digits="w{digit}"/><Redirect>{escape(webhook_url(call_id, "twiml"))}</Redirect></Response>')
        return
    if call["status"] != "holding":
        log_status(call_id, "holding")
    if classify_person(text):
        connect_user(call_id)


def connect_user(call_id: int) -> None:
    """A person answered: say the fixed disclosure, stop listening for good, and ring the patient into a conference."""
    log_status(call_id, "human")
    with get_db() as db:
        db.execute("UPDATE hold_calls SET human_at = CURRENT_TIMESTAMP, hold_seconds = CAST((julianday('now') - julianday(started_at)) * 86400 AS INTEGER) "
                   "WHERE id = ?", (call_id,))
        call = dict(db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone())
    room = f"bk-hold-{call_id}"
    twilio_client.update_call(call["hospital_call_sid"], f'<Response><Stop><Transcription/></Stop><Say>{escape(config.HOLD_DISCLOSURE)}</Say>'
                                                       f'<Dial><Conference endConferenceOnExit="true">{room}</Conference></Dial></Response>')
    log_status(call_id, "connecting")
    try:
        sid = twilio_client.create_call(call["user_number"], webhook_url(call_id, "user-twiml"), webhook_url(call_id, "user-status"),
                                        timeout_seconds=config.HOLD_CALL_USER_RING_SECONDS, events="answered completed")
    except twilio_client.TwilioError:
        return user_missed(call_id)
    with get_db() as db:
        db.execute("UPDATE hold_calls SET user_call_sid = ? WHERE id = ?", (sid, call_id))


def user_twiml(call_id: int) -> str:
    return ('<?xml version="1.0" encoding="UTF-8"?><Response><Say>Your billing office is on the line.</Say>'
            f'<Dial><Conference>bk-hold-{call_id}</Conference></Dial></Response>')


def user_answered(call_id: int) -> None:
    log_status(call_id, "connected")


def user_missed(call_id: int) -> None:
    """The patient didn't pick up in time: tell the person at the hospital, hang up, and keep the allowance."""
    with get_db() as db:
        call = dict(db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone())
    try:
        twilio_client.update_call(call["hospital_call_sid"], f"<Response><Say>{escape(config.HOLD_USER_MISSED_MESSAGE)}</Say><Hangup/></Response>")
    except twilio_client.TwilioError:
        log.error("Could not play the missed-call message for hold call %s", call_id)
    finish(call_id, "missed", "user_no_answer")


def finish(call_id: int, status: str, reason: str) -> None:
    """End a call. Only a call that connected counts against an allowance; the numbers are then replaced by hashes."""
    with get_db() as db:
        call = dict(db.execute("SELECT * FROM hold_calls WHERE id = ?", (call_id,)).fetchone())
        db.execute("UPDATE hold_calls SET ended_at = CURRENT_TIMESTAMP, end_reason = ?, cost_cents = ? WHERE id = ?",
                   (reason, config.HOLD_CALL_COST_ESTIMATE_CENTS, call_id))
    log_status(call_id, status, reason)
    if status in ("missed", "failed"):
        refund_credit(call["device_id"])
    _save_learning(call)
    with get_db() as db:
        db.execute("UPDATE hold_calls SET user_number = ?, hospital_number = ? WHERE id = ?",
                   (phone_hash(call["user_number"]), phone_hash(call["hospital_number"]), call_id))


def _save_learning(call: dict) -> None:
    """A menu path that reached a person is kept for that hospital and tried first next time."""
    if not call["menu_path"] or not call.get("facility_id"):
        return
    with get_db() as db:
        if db.execute("SELECT status FROM hold_calls WHERE id = ?", (call["id"],)).fetchone()["status"] in ("connected", "missed"):
            db.execute("INSERT OR REPLACE INTO hospital_menu_paths (facility_id, menu_path) VALUES (?, ?)", (call["facility_id"], call["menu_path"]))


def call_ended(call_id: int, call_status: str) -> None:
    """Twilio says the hospital's line ended. Before a person answered, that is a failure (or the hold limit)."""
    with get_db() as db:
        row = db.execute("SELECT status FROM hold_calls WHERE id = ?", (call_id,)).fetchone()
    if not row or row["status"] in ("connected", "missed", "failed", "ended"):
        return
    if row["status"] in ("dialing", "menu", "holding"):
        finish(call_id, "failed", "hold_timeout" if call_status == "completed" else call_status)
    else:
        finish(call_id, "ended", "hospital_hung_up")


def cancel(call_id: int, device_id: str) -> bool:
    with get_db() as db:
        call = db.execute("SELECT * FROM hold_calls WHERE id = ? AND device_id = ?", (call_id, device_id)).fetchone()
    if not call or call["status"] not in ("queued", "dialing", "menu", "holding"):
        return False
    if call["hospital_call_sid"]:
        try:
            twilio_client.hang_up(call["hospital_call_sid"])
        except twilio_client.TwilioError:
            log.error("Could not hang up hold call %s", call_id)
    finish(call_id, "ended", "cancelled")
    return True


def typical_hold(facility_id: str) -> dict | None:
    """Typical hold time at a hospital, once enough calls (from people who allowed data use) back it up."""
    with get_db() as db:
        rows = db.execute("SELECT hold_seconds FROM hold_calls c JOIN mobile_devices d ON d.device_id = c.device_id "
                          "WHERE c.facility_id = ? AND c.hold_seconds IS NOT NULL AND d.data_improvement = 1", (facility_id,)).fetchall()
    if len(rows) < config.OUTCOME_MIN_SAMPLE:
        return None
    seconds = sorted(r["hold_seconds"] for r in rows)
    return {"median_minutes": round(seconds[len(seconds) // 2] / 60), "calls": len(seconds)}


def reap_stale_calls() -> int:
    """A call that never reported an end (a dropped webhook) is failed and its numbers hashed once it outlives the hold limit."""
    limit = f"-{config.HOLD_CALL_MAX_MINUTES + 10} minutes"
    with get_db() as db:
        stale = [row["id"] for row in db.execute(
            "SELECT id FROM hold_calls WHERE status IN (?, ?, ?, ?, ?, ?, ?) AND created_at < datetime('now', ?)",
            (*ACTIVE_STATUSES, limit)).fetchall()]
    for call_id in stale:
        finish(call_id, "failed", "stale")
    return len(stale)
