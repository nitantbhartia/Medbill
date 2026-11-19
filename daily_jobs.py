"""Daily follow-up and reminder jobs, run inside the web process (the service runs one replica)."""

import logging
import runpy
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import config
import dispute_service
import ocr_quality

log = logging.getLogger(__name__)
REMINDER_SCRIPT = Path(__file__).parent / "scripts" / "send_concierge_reminders.py"


def seconds_until_next_run(now: datetime) -> float:
    next_run = now.replace(hour=config.DAILY_JOBS_HOUR_UTC, minute=0, second=0, microsecond=0)
    if next_run <= now:
        next_run += timedelta(days=1)
    return (next_run - now).total_seconds()


def run_daily_jobs() -> None:
    try:
        log.info("Daily jobs: %d hospital follow-ups sent", dispute_service.process_due_followups())
    except Exception:
        log.exception("Daily jobs: hospital follow-ups failed")
    try:
        ocr_quality.record_weekly()
    except Exception:
        log.exception("Daily jobs: weekly OCR quality numbers failed")
    try:
        runpy.run_path(str(REMINDER_SCRIPT), run_name="__main__")
    except Exception:
        log.exception("Daily jobs: reminders failed")


def _loop() -> None:
    while True:
        time.sleep(seconds_until_next_run(datetime.now(timezone.utc)))
        run_daily_jobs()


def start_daily_jobs() -> None:
    threading.Thread(target=_loop, daemon=True, name="daily-jobs").start()
