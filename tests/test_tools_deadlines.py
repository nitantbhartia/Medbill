import os
import sys
from datetime import date
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from main import app  # noqa: E402
from tools_deadlines import (  # noqa: E402
    collection_timeline,
    latest_application_date,
    month_start,
    retro_window_start,
    run_financial_assistance_deadline,
    run_medicaid_retro_checker,
)

client = TestClient(app)
TODAY = date(2026, 11, 20)
FA_SLUG = "hospital-financial-assistance-deadline"
MEDICAID_SLUG = "medicaid-retroactive-coverage-checker"


# --- 501(r) timeline ---

def test_collection_timeline_counts_days_across_year_end():
    earliest_action, application_end = collection_timeline(date(2026, 11, 3))
    assert earliest_action == date(2027, 3, 3)
    assert application_end == date(2027, 7, 1)


def test_collection_timeline_leap_day():
    earliest_action, application_end = collection_timeline(date(2028, 1, 15))
    assert earliest_action == date(2028, 5, 14)
    assert application_end == date(2028, 9, 11)


def test_nonprofit_window_open():
    state, summary, details = run_financial_assistance_deadline(
        {"first_bill_date": "2026-10-01", "hospital_nonprofit": "yes"}, today=TODAY
    )
    assert state == "window_open"
    assert "January 29, 2027" in summary
    assert "May 29, 2027" in summary
    assert details["earliest_collection_action_date"] == "January 29, 2027 (70 days from today)"
    assert any("Apply for financial assistance by May 29, 2027" in s for s in details["next_steps"])


def test_last_day_of_application_period_is_still_open():
    state, _, _ = run_financial_assistance_deadline({"first_bill_date": "2026-03-25", "hospital_nonprofit": "yes"}, today=TODAY)
    assert state == "window_open"
    state, _, _ = run_financial_assistance_deadline({"first_bill_date": "2026-03-24", "hospital_nonprofit": "yes"}, today=TODAY)
    assert state == "window_closed"


def test_unsure_nonprofit_hedges_summary():
    state, summary, _ = run_financial_assistance_deadline({"first_bill_date": "11/01/2026", "hospital_nonprofit": "unsure"}, today=TODAY)
    assert state == "window_open"
    assert summary.startswith("If the hospital is a nonprofit")


def test_for_profit_points_to_state_law():
    state, summary, details = run_financial_assistance_deadline({"first_bill_date": "2026-10-01", "hospital_nonprofit": "no"}, today=TODAY)
    assert state == "for_profit"
    assert "state's law" in summary
    assert "earliest_collection_action_date" not in details


@pytest.mark.parametrize("bad", ["", None, "2026-02-30", "next week"])
def test_fa_invalid_or_missing_date_raises(bad):
    with pytest.raises(ValueError):
        run_financial_assistance_deadline({"first_bill_date": bad, "hospital_nonprofit": "yes"}, today=TODAY)


# --- Medicaid retroactive window ---

def test_month_start_crosses_year_boundary():
    assert month_start(date(2027, 1, 31), 3) == date(2026, 10, 1)
    assert month_start(date(2026, 11, 20), -2) == date(2027, 1, 1)


def test_window_before_2027_is_three_months():
    assert retro_window_start(date(2026, 12, 31), expansion_adult=True) == date(2026, 9, 1)


def test_window_from_2027_depends_on_group():
    assert retro_window_start(date(2027, 1, 1), expansion_adult=True) == date(2026, 12, 1)
    assert retro_window_start(date(2027, 1, 1), expansion_adult=False) == date(2026, 11, 1)


def test_latest_application_date_spans_the_2027_switch():
    assert latest_application_date(date(2026, 11, 15), expansion_adult=True) == date(2026, 12, 31)
    assert latest_application_date(date(2026, 11, 15), expansion_adult=False) == date(2027, 1, 31)
    assert latest_application_date(date(2026, 8, 15), expansion_adult=True) == date(2026, 11, 30)


def _medicaid(care, application, group="no"):
    return run_medicaid_retro_checker({"care_date": care, "application_date": application, "expansion_adult": group}, today=TODAY)


def test_first_day_of_window_is_inside_and_day_before_is_outside():
    assert _medicaid("2026-09-01", "2026-12-15")[0] == "inside_window"
    state, _, details = _medicaid("2026-08-31", "2026-12-15")
    assert state == "outside_window"
    assert details["retroactive_coverage_can_start"] == "September 1, 2026"


def test_same_care_date_flips_at_2027_switch():
    assert _medicaid("2026-10-10", "2026-12-31", "yes")[0] == "inside_window"
    assert _medicaid("2026-10-10", "2027-01-01", "yes")[0] == "outside_window"
    assert _medicaid("2026-10-10", "2027-01-01", "no")[0] == "outside_window"
    assert _medicaid("2026-11-10", "2027-01-01", "no")[0] == "inside_window"


def test_unsure_group_after_2027_depends():
    state, summary, details = _medicaid("2026-11-10", "2027-01-05", "unsure")
    assert state == "depends_on_group"
    assert "expansion" in summary
    assert details["retroactive_coverage_can_start"] == "November 1, 2026"
    assert any("filed by December 31, 2026" in s for s in details["next_steps"])


def test_care_in_application_month_is_not_retroactive():
    assert _medicaid("2026-12-01", "2026-12-15")[0] == "current_coverage"
    assert _medicaid("2026-12-20", "2026-12-15")[0] == "current_coverage"


def test_pre_2027_application_mentions_switch():
    _, _, details = _medicaid("2026-10-10", "2026-12-01")
    assert any("keeps the 3-month window" in s for s in details["next_steps"])


@pytest.mark.parametrize("payload", [
    {"application_date": "2026-12-01"},
    {"care_date": "2026-10-01", "application_date": "2026-13-01"},
    {"care_date": "garbage", "application_date": "2026-12-01"},
])
def test_medicaid_invalid_or_missing_date_raises(payload):
    with pytest.raises(ValueError):
        run_medicaid_retro_checker(payload, today=TODAY)


# --- pages, API, sitemap ---

@pytest.mark.parametrize("slug", [FA_SLUG, MEDICAID_SLUG])
def test_tool_pages_index_and_sitemap(slug):
    assert client.get(f"/tools/{slug}/").status_code == 200
    assert f"/tools/{slug}/" in client.get("/tools/").text
    assert f"/tools/{slug}/" in client.get("/sitemap-tools.xml").text


def test_api_runs_medicaid_tool_with_guide_cta():
    resp = client.post(f"/api/tools/{MEDICAID_SLUG}/run", json={"care_date": "2020-01-01", "application_date": "2020-03-15", "expansion_adult": "yes"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["result_state"] == "inside_window"
    assert data["cta"]["primary_url"] == "/scan"
    assert data["cta"]["secondary_url"] == "/guides/hospital-bill-medicaid-pending/"
    assert "$" not in data["cta"]["footnote"]


def test_api_rejects_bad_date_with_400():
    resp = client.post(f"/api/tools/{FA_SLUG}/run", json={"first_bill_date": "2026-02-30", "hospital_nonprofit": "yes"})
    assert resp.status_code == 400
    assert "date" in resp.json()["detail"]
