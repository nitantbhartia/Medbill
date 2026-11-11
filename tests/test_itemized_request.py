import os
import sys
from datetime import date
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import itemized_request  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)

TAMPA_GENERAL = {
    "facility_id": "100128", "name": "Tampa General Hospital", "address": "1 Tampa General Circle",
    "city": "Tampa", "state": "FL", "zip": "33606", "phone": "(813) 844-7000", "slug": "tampa-general-hospital",
}

LETTER_FORM = {
    "your_name": "Dana Whitfield",
    "your_address": "4410 Bayshore Blvd, Apt 3, Tampa, FL 33611",
    "hospital_name": "Tampa General Hospital",
    "hospital_address": "1 Tampa General Circle",
    "hospital_city_line": "Tampa, FL 33606",
    "account_number": "TGH-20260303-7781",
    "service_dates": "March 3, 2026",
}


def test_lookup_returns_billing_address_and_phone():
    upsert_hospital_row(TAMPA_GENERAL)
    r = client.get("/api/billing-contacts?q=Tampa Gen")
    [hit] = r.json()["data"]
    assert hit["address"] == "1 Tampa General Circle"
    assert hit["phone"] == "(813) 844-7000"
    assert hit["zip"] == "33606"


def test_letter_lists_codes_cites_hipaa_and_sets_due_date():
    data = itemized_request.build_request_letter(LETTER_FORM, today=date(2026, 11, 11))
    letter = data["letter"]
    assert letter.startswith("November 11, 2026")
    assert "CPT or HCPCS code" in letter and "revenue code" in letter and "NDC" in letter
    assert "45 CFR 164.524" in letter
    assert "Account number: TGH-20260303-7781" in letter
    assert "by mail to the address above" in letter
    assert "about me" in letter
    assert data["response_due"] == "2026-12-11"


def test_letter_for_someone_else_asks_about_authorization():
    form = {**LETTER_FORM, "patient_name": "Ruth Whitfield", "reply_email": "dana@example.com"}
    letter = itemized_request.build_request_letter(form)["letter"]
    assert "on behalf of Ruth Whitfield" in letter
    assert "about the patient" in letter
    assert "by email to dana@example.com" in letter


def test_letter_endpoint_explains_what_is_missing():
    r = client.post("/api/itemized-bill/letter", json={"your_name": "Dana Whitfield"})
    assert r.status_code == 400
    assert "mailing address" in r.json()["detail"]
    assert "account number or the date of service" in r.json()["detail"]


def test_letter_endpoint_does_not_store_input():
    from db import get_db
    client.post("/api/itemized-bill/letter", json=LETTER_FORM)
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) FROM tool_runs").fetchone()[0] == 0
        assert db.execute("SELECT COUNT(*) FROM itemized_requests").fetchone()[0] == 0


def test_reminder_is_due_after_thirty_days_and_sent_once():
    remind_on = itemized_request.save_reminder("dana@example.com", "Tampa General Hospital", sent_on=date(2026, 11, 11))
    assert remind_on == "2026-12-11"
    assert itemized_request.due_reminders(date(2026, 12, 10)) == []
    [due] = itemized_request.due_reminders(date(2026, 12, 11))
    itemized_request.mark_reminded(due["id"])
    assert itemized_request.due_reminders(date(2026, 12, 12)) == []


def test_reminder_endpoint_rejects_bad_email():
    r = client.post("/api/itemized-bill/reminder", json={"email": "dana", "hospital_name": "Tampa General Hospital"})
    assert r.status_code == 400


def test_page_prefills_hospital_from_directory():
    upsert_hospital_row(TAMPA_GENERAL)
    html = client.get("/itemized-bill?facility=100128").text
    assert "Tampa General Hospital" in html and "1 Tampa General Circle" in html


def test_reminder_email_points_back_to_upload():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts"))
    from send_concierge_reminders import itemized_reminder_email
    subject, body = itemized_reminder_email("Tampa General Hospital")
    assert "Tampa General Hospital" in subject
    assert "/scan" in body and "30-day deadline" in body


def test_confirm_page_routes_summary_bills_to_the_request():
    from db import get_db
    with get_db() as db:
        bill_id = db.execute(
            "INSERT INTO bills (provider_name, bill_date, total_charged) VALUES (?, ?, ?)",
            ("Tampa General Hospital", "2026-03-03", 18400.0),
        ).lastrowid
    html = client.get(f"/confirm/{bill_id}").text
    assert "This looks like a summary bill" in html
    assert "/itemized-bill?provider=Tampa%20General%20Hospital" in html


def test_request_page_is_in_sitemap_and_footer():
    assert "/itemized-bill</loc>" in client.get("/sitemap-core.xml").text
    assert 'href="/itemized-bill"' in client.get("/").text.split("<footer")[1]
