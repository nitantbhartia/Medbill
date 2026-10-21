"""Daily concierge reminders. Run once a day (e.g. a Railway cron): python3 scripts/send_concierge_reminders.py

- Emails ops a digest of appeals whose filing deadline or insurer decision date is near or past.
- Reminds customers whose appeal draft has waited 3 or 7 days for their approval.
"""

import os
import sys
from datetime import date, datetime, timedelta
from html import escape

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import appeals  # noqa: E402
import config  # noqa: E402
import email_service  # noqa: E402

DRAFT_NUDGE_DAYS = (3, 7)  # days after payment to remind about an unapproved draft


def build_digest(cases: list[dict], today: date) -> list[str]:
    """One line per appeal that needs attention within the reminder window."""
    window = today + timedelta(days=config.APPEAL_REMINDER_WINDOW_DAYS)
    lines = []
    for case in cases:
        dates = appeals.deadlines(case)
        label = f"#{case['id']} {case['patient_name']} / {case['insurer_name']}"
        if case["status"] in ("drafted", "approved") and dates["file_by"] and dates["file_by"] <= window:
            lines.append(f"{label}: not sent yet, must be filed by {dates['file_by']}")
        if case["status"] == "sent" and dates["decision_due"] and dates["decision_due"] <= today:
            lines.append(f"{label}: insurer decision was due {dates['decision_due']}, follow up")
    return lines


def stale_drafts(cases: list[dict], today: date) -> list[dict]:
    return [
        c for c in cases
        if c["status"] == "drafted" and c["paid_at"]
        and (today - datetime.fromisoformat(str(c["paid_at"])).date()).days in DRAFT_NUDGE_DAYS
    ]


def main() -> None:
    today = date.today()
    cases = appeals.list_open_cases()
    digest = build_digest(cases, today)
    if digest and config.OPS_NOTIFY_EMAIL:
        html = "<ul>" + "".join(f"<li>{escape(line)}</li>" for line in digest) + "</ul>"
        email_service.send_email(config.OPS_NOTIFY_EMAIL, f"[Concierge] {len(digest)} appeal deadlines", html)
    drafts = stale_drafts(cases, today)
    for case in drafts:
        link = f"{config.APP_URL.rstrip('/')}/appeal/case/{case['token']}"
        email_service.send_email(
            case["email"],
            "BillKarma: your appeal is waiting for your approval",
            f"<p>Your appeal letter is ready. Approve it so we can send it before your deadline.</p><p><a href=\"{link}\">Review your appeal</a></p>",
        )
    print(f"digest lines={len(digest)} draft reminders={len(drafts)}")


if __name__ == "__main__":
    main()
