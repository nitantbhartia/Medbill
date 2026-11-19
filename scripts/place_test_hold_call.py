"""Place ONE real hold call to a number you choose, to test detection before turning HOLD_CALLS_ENABLED on.

Twilio must reach this machine's web server, so run the server with a public URL (for example `ngrok http 8000`),
then start both with the same database and these variables set:

  APP_URL=https://<your-ngrok-host>  HOLD_CALLS_ENABLED=true  TWILIO_ACCOUNT_SID=...  TWILIO_AUTH_TOKEN=...
  TWILIO_FROM_NUMBER=+1...  GEMINI_API_KEY=...  uvicorn main:app --port 8000
  python scripts/place_test_hold_call.py --hospital "(619) 555-0142" --me "(619) 555-0100"

It makes a test device and an unlocked test bill, marks your number verified (no SMS), and calls. It polls until the call ends
and prints each status. Every call costs money: Twilio bills the minutes on hold."""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hold_calls
import report
from db import get_db, init_db

TEST_DEVICE = "hold-call-test-device"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hospital", required=True, help="the billing office number to call")
    parser.add_argument("--me", required=True, help="your phone: it rings when a person answers")
    args = parser.parse_args()
    init_db()
    with get_db() as db:
        bill_id = db.execute("INSERT INTO bills (provider_name, total_patient_owes, status) VALUES ('Test Hospital', 100, 'analyzed')").lastrowid
        db.execute("INSERT OR IGNORE INTO bill_access_sessions (session_id, bill_id) VALUES (?, ?)", (TEST_DEVICE, bill_id))
        db.execute("INSERT OR REPLACE INTO phone_verifications (device_id, phone_hash, verified_at) VALUES (?, ?, datetime('now'))",
                   (TEST_DEVICE, hold_calls.phone_hash(args.me)))
    report.record_pending(bill_id, f"iap:test-{bill_id}", "")
    report.mark_paid(f"iap:test-{bill_id}")
    result = hold_calls.request_call(TEST_DEVICE, bill_id, args.hospital, args.me)
    print(f"Call {result['call_id']}: {result['status']} (starts {result['starts_at']})")
    seen = None
    while True:
        with get_db() as db:
            row = db.execute("SELECT status, menu_path, end_reason FROM hold_calls WHERE id = ?", (result["call_id"],)).fetchone()
        if row["status"] != seen:
            seen = row["status"]
            print(f"  {seen}  menu path: {row['menu_path'] or '-'}  {row['end_reason'] or ''}")
        if seen in ("connected", "missed", "failed", "ended"):
            break
        time.sleep(5)


if __name__ == "__main__":
    main()
