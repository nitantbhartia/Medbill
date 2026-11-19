"""With every B16 rule flag on, the whole mobile flow still works and the numbers stay defensible."""

import pytest
from fastapi.testclient import TestClient

import api
import config
import scan_pipeline
from main import app
from tests.conftest import RULE_FLAGS, SAMPLE_BILL

client = TestClient(app, follow_redirects=False)
PAGE = ("pages", ("bill.jpg", b"x", "image/jpeg"))


@pytest.fixture(autouse=True)
def flags_on(monkeypatch):
    for flag in RULE_FLAGS:
        monkeypatch.setattr(config, flag, True)
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: dict(SAMPLE_BILL))
    api._rate_buckets.clear()


def test_scan_view_letter_and_phone_script_all_work_with_every_flag_on():
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    headers = {"Authorization": f"Bearer {data['token']}"}
    scanned = client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers)
    assert scanned.status_code == 200
    view = scanned.json()["data"]
    assert view["teaser"] is not None and view["teaser"]["total_savings"] >= 0
    owed = SAMPLE_BILL["total_patient_owes"]
    assert view["teaser"]["total_savings"] <= owed
    assert client.get(f"/api/m/bills/{view['bill_id']}", headers=headers).status_code == 200
    assert client.get("/api/m/bills", headers=headers).status_code == 200


def test_an_er_level_is_never_strong_and_adds_no_dollars_with_the_flag_on():
    from charge_summary import group_findings_by_charge
    import analyzer
    extracted = {"provider_name": "Test Hospital", "bill_date": "2026-03-04", "total_charged": 3000.0, "total_patient_owes": 3000.0,
                 "line_items": [{"cpt_code": "99285", "description": "ER visit", "quantity": 1, "charged_amount": 3000.0,
                                 "date_of_service": "2026-03-03"}]}
    findings = analyzer.analyze_bill(extracted, "92103")["findings"]
    rows = [{"id": i, "finding_type": f["type"], "rule_id": f.get("rule_id"), "severity": f["severity"],
             "potential_savings": f["potential_savings"], "message": f["message"], "parsed_details": f} for i, f in enumerate(findings)]
    summary = group_findings_by_charge(rows, 3000.0)
    upcoding_rows = [r for r in summary["charges"] if any(x["type"] == "upcoding" for x in r["reasons"])]
    assert upcoding_rows and all(not r["strong"] for r in upcoding_rows)
    assert summary["error_savings"] == 0
