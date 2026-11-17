import os
import sys
from datetime import date, timedelta
from unittest.mock import MagicMock, patch

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import config  # noqa: E402
import dispute_service  # noqa: E402
from analyzer import analyze_bill, save_bill_and_findings  # noqa: E402
from db import get_db  # noqa: E402
from main import app  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402

client = TestClient(app)


def _paid_bill() -> tuple[int, int]:
    bill_id = save_bill_and_findings(None, SAMPLE_BILL, analyze_bill(SAMPLE_BILL, "33021"), "33021")
    with get_db() as db:
        payment_id = db.execute(
            "INSERT INTO dispute_payments (bill_id, amount_cents, status, patient_email) VALUES (?, 4900, 'paid', ?)",
            (bill_id, "maria.lopez@example.com"),
        ).lastrowid
    return bill_id, payment_id


def _activate(hospital_email: str) -> int:
    bill_id, payment_id = _paid_bill()
    return dispute_service.activate_dispute(
        bill_id, payment_id, "Maria Lopez", "maria.lopez@example.com",
        "812 Hollywood Blvd, Hollywood, FL 33021", "MRH-2026-44817", hospital_email,
    )


def _case(case_id):
    with get_db() as db:
        return dict(db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone())


@patch("dispute_service.email_service")
def test_without_billing_email_case_waits_and_is_not_marked_sent(mock_email):
    case_id = _activate("")
    case = _case(case_id)
    assert case["status"] == "needs_delivery"
    assert case["initial_sent_at"] is None
    mock_email.send_dispute_to_hospital.assert_not_called()


@patch("dispute_service.email_service")
def test_failed_send_is_not_marked_sent(mock_email):
    mock_email.send_dispute_to_hospital.side_effect = RuntimeError("Resend returned unexpected status 500")
    case = _case(_activate("billing@memorialregional.org"))
    assert case["status"] == "needs_delivery"


@patch("dispute_service.email_service")
def test_successful_send_marks_sent(mock_email):
    mock_email.send_dispute_to_hospital.return_value = True
    case = _case(_activate("billing@memorialregional.org"))
    assert case["status"] == "sent"
    assert case["initial_sent_at"] == date.today().isoformat()


@patch("dispute_service.email_service")
def test_delivering_later_sends_and_restarts_follow_up_clock(mock_email):
    case_id = _activate("")
    with get_db() as db:
        db.execute("UPDATE followup_queue SET scheduled_for = '2026-01-01' WHERE case_id = ?", (case_id,))
    mock_email.send_dispute_to_hospital.return_value = True
    r = client.post(f"/api/dispute/{case_id}/delivery", json={"hospital_billing_email": "billing@memorialregional.org"})
    assert r.status_code == 200
    assert _case(case_id)["status"] == "sent"
    first = dispute_service.get_followups_for_case(case_id)[0]
    assert first["scheduled_for"] == (date.today() + timedelta(days=config.DISPUTE_FOLLOWUP_DAYS[0])).isoformat()


@patch("dispute_service.email_service")
def test_delivery_rejects_bad_email(mock_email):
    case_id = _activate("")
    r = client.post(f"/api/dispute/{case_id}/delivery", json={"hospital_billing_email": "billing"})
    assert r.status_code == 400


@patch("dispute_service.email_service")
def test_failed_follow_up_is_retried_not_counted(mock_email):
    mock_email.send_dispute_to_hospital.return_value = True
    case_id = _activate("billing@memorialregional.org")
    mock_email.send_followup_to_hospital.return_value = False
    queue_id = dispute_service.get_followups_for_case(case_id)[0]["id"]
    dispute_service._send_followup(case_id, 1, queue_id)
    assert dispute_service.get_followups_for_case(case_id)[0]["sent_at"] is None
    assert _case(case_id)["followups_sent"] == 0


@patch("dispute_service.email_service")
def test_dashboard_tells_the_truth_about_delivery_and_refund_date(mock_email):
    case_id = _activate("")
    html = client.get(f"/dispute/dashboard?case={case_id}").text
    assert "Your letter is ready to send" in html
    assert "Letter not sent yet" in html
    assert "Letter emailed to the billing office" not in html
    refund_on = (date.today() + timedelta(days=config.DISPUTE_MAX_DAYS)).isoformat()
    assert f"isn&rsquo;t reduced by <strong>{refund_on}</strong>" in html
    assert "Formal" in html or "dispute" in html.lower()
    assert "submitted a financial assistance application" not in html


def test_strategy_and_checkout_quote_the_same_fee():
    bill_id, _ = _paid_bill()
    strategy = client.get(f"/autopilot/strategy/{bill_id}").text
    activate = client.get(f"/dispute/activate/{bill_id}").text
    assert "for $49" in strategy and "$49" in activate
    assert "$99" not in strategy


def _add_hospital():
    with get_db() as db:
        db.execute(
            "INSERT OR REPLACE INTO hospital_directory (facility_id, name, address, city, state, zip)"
            " VALUES ('100001', ?, '3501 Johnson St', 'Hollywood', 'FL', '33021')",
            (SAMPLE_BILL["provider_name"],),
        )


@patch("dispute_service.send_certified_letter", return_value={"lob_id": "ltr_1", "tracking_number": "9407TRACK"})
@patch("dispute_service.email_service")
def test_dispute_is_also_mailed_certified_when_addresses_known(mock_email, mock_lob, monkeypatch):
    monkeypatch.setattr(config, "LOB_API_KEY", "test_key")
    _add_hospital()
    case = _case(_activate("billing@memorialregional.org"))
    assert case["status"] == "sent"
    assert case["certified_tracking"] == "9407TRACK"
    kwargs = mock_lob.call_args.kwargs
    assert kwargs["to_address"] == "3501 Johnson St, Hollywood, FL 33021"
    assert kwargs["from_address"] == "812 Hollywood Blvd, Hollywood, FL 33021"


@patch("dispute_service.send_certified_letter", side_effect=RuntimeError("Lob error 422"))
@patch("dispute_service.email_service")
def test_lob_failure_does_not_block_the_email(mock_email, mock_lob, monkeypatch):
    monkeypatch.setattr(config, "LOB_API_KEY", "test_key")
    _add_hospital()
    case = _case(_activate("billing@memorialregional.org"))
    assert case["status"] == "sent"
    assert case["certified_tracking"] is None


@patch("dispute_service.send_certified_letter")
@patch("dispute_service.email_service")
def test_no_lob_key_means_no_mail(mock_email, mock_lob, monkeypatch):
    monkeypatch.setattr(config, "LOB_API_KEY", "")
    _add_hospital()
    _activate("billing@memorialregional.org")
    mock_lob.assert_not_called()


@patch("dispute_service.email_service")
def test_patient_is_told_when_a_follow_up_goes_out(mock_email):
    mock_email.send_dispute_to_hospital.return_value = True
    mock_email.send_followup_to_hospital.return_value = True
    case_id = _activate("billing@memorialregional.org")
    queue_id = dispute_service.get_followups_for_case(case_id)[0]["id"]
    dispute_service._send_followup(case_id, 1, queue_id)
    kwargs = mock_email.send_followup_notice_to_patient.call_args.kwargs
    assert kwargs["to"] == "maria.lopez@example.com"
    assert kwargs["followup_number"] == 1
    assert kwargs["days_until_refund"] == config.DISPUTE_MAX_DAYS
