from datetime import datetime, timezone
from unittest.mock import patch

import config
import daily_jobs


def test_next_run_is_today_if_the_hour_has_not_passed():
    now = datetime(2026, 11, 17, config.DAILY_JOBS_HOUR_UTC - 2, 0, tzinfo=timezone.utc)
    assert daily_jobs.seconds_until_next_run(now) == 2 * 3600


def test_next_run_rolls_to_tomorrow_after_the_hour():
    now = datetime(2026, 11, 17, config.DAILY_JOBS_HOUR_UTC, 30, tzinfo=timezone.utc)
    assert daily_jobs.seconds_until_next_run(now) == 23.5 * 3600


def test_a_failing_follow_up_run_does_not_stop_the_reminders():
    with patch("daily_jobs.dispute_service.process_due_followups", side_effect=RuntimeError("db down")), \
         patch("daily_jobs.runpy.run_path") as run_reminders:
        daily_jobs.run_daily_jobs()
    run_reminders.assert_called_once()
