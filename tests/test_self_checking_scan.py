"""Self-checking scans: math checks, the one-time re-read, the confirm sheet and its saved corrections."""

import copy

import pytest
from fastapi.testclient import TestClient

import api
import config
import scan_pipeline
from db import get_db
from main import app
from tests.conftest import SAMPLE_BILL
from validators.extraction import find_extraction_issues, validate_extraction

client = TestClient(app, follow_redirects=False)
PAGE = ("pages", ("bill.jpg", b"fake-image", "image/jpeg"))


def bill_with_bad_line():
    bill = copy.deepcopy(SAMPLE_BILL)
    bill["line_items"][1].update(quantity=3, unit_price=45.0, charged_amount=1350.0,
                                 insurance_paid=None, insurance_adjustment=None, patient_responsibility=None)
    return bill


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    monkeypatch.setattr(config, "SLIM_LAUNCH", True)
    monkeypatch.setattr(scan_pipeline.scanner, "reread_line", lambda *args: None)
    api._rate_buckets.clear()


def scan_with(monkeypatch, bill):
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: copy.deepcopy(bill))
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    headers = {"Authorization": f"Bearer {data['token']}"}
    response = client.post("/api/m/scan", files=[PAGE], data={"zip_code": "33021"}, headers=headers)
    assert response.status_code == 200, response.text
    return response.json()["data"], headers


def test_structured_issues_keep_the_old_messages():
    issues = find_extraction_issues(bill_with_bad_line())
    assert [i["kind"] for i in issues if i["line_index"] == 1] == ["line_math"]
    assert validate_extraction(bill_with_bad_line()) == [i["message"] for i in issues]


def test_a_bill_whose_lines_add_up_needs_no_confirmation(monkeypatch):
    view, _ = scan_with(monkeypatch, SAMPLE_BILL)
    assert view["confirm_lines"] == []


def test_three_times_forty_five_printed_as_1350_needs_one_confirmation(monkeypatch):
    view, _ = scan_with(monkeypatch, bill_with_bad_line())
    assert [(l["line_index"], l["field"], l["kind"], l["read_value"]) for l in view["confirm_lines"]] == [
        (1, "charged_amount", "line_math", 1350.0)]


def test_a_reread_that_clears_the_problem_is_kept(monkeypatch):
    monkeypatch.setattr(scan_pipeline.scanner, "reread_line", lambda *args: {"charged_amount": 135.0})
    monkeypatch.setattr(scan_pipeline.scanner, "process_bill_with_verification", lambda *a: bill_with_bad_line())
    extracted = scan_pipeline.extraction_selfcheck.check_lines(bill_with_bad_line(), [(b"x", "image/jpeg")])
    assert extracted["line_items"][1]["charged_amount"] == 135.0
    assert not extracted["line_items"][1].get("needs_confirm")


def test_rereads_are_capped_per_bill(monkeypatch):
    calls = []
    monkeypatch.setattr(scan_pipeline.scanner, "reread_line", lambda *args: calls.append(1))
    bill = copy.deepcopy(SAMPLE_BILL)
    bill["line_items"] = [{**copy.deepcopy(SAMPLE_BILL["line_items"][1]), "quantity": 3, "unit_price": 45.0, "charged_amount": 1350.0}
                          for _ in range(6)]
    scan_pipeline.extraction_selfcheck.check_lines(bill, [(b"x", "image/jpeg")])
    assert len(calls) == config.OCR_MAX_LINE_REREADS


def test_skipped_lines_are_marked_not_checked_and_left_out_of_totals(monkeypatch):
    view, _ = scan_with(monkeypatch, bill_with_bad_line())
    from analyzer import get_bill_results
    from charge_summary import group_findings_by_charge
    summary = group_findings_by_charge(get_bill_results(view["bill_id"])["findings"])
    unchecked = [row for row in summary["charges"] if row["not_checked"]]
    assert unchecked and all(row["code"] == "71046" and not row["strong"] for row in unchecked)
    checked_savings = sum(row["savings"] for row in summary["charges"] if not row["not_checked"] and row["charged"])
    assert summary["total_savings"] <= checked_savings


def test_confirming_saves_corrections_and_reruns_the_analysis(monkeypatch):
    view, headers = scan_with(monkeypatch, bill_with_bad_line())
    bill_id = view["bill_id"]
    answer = client.post(f"/api/m/bills/{bill_id}/confirm",
                         json={"lines": [{"line_index": 1, "field": "charged_amount", "value": 135.0}]}, headers=headers)
    assert answer.status_code == 200 and answer.json()["data"]["confirm_lines"] == []
    with get_db() as db:
        row = db.execute("SELECT * FROM extraction_corrections WHERE bill_id = ?", (bill_id,)).fetchone()
        charged = db.execute("SELECT charged_amount FROM line_items WHERE bill_id = ? ORDER BY id LIMIT 1 OFFSET 1", (bill_id,)).fetchone()[0]
    assert (row["field"], row["extracted_value"], row["confirmed_value"], row["issue_kind"]) == ("charged_amount", "1350.0", "135.0", "line_math")
    assert charged == 135.0


def test_confirm_rejects_lines_that_are_not_waiting_and_bad_values(monkeypatch):
    view, headers = scan_with(monkeypatch, bill_with_bad_line())
    url = f"/api/m/bills/{view['bill_id']}/confirm"
    assert client.post(url, json={"lines": [{"line_index": 0, "field": "charged_amount", "value": 1.0}]}, headers=headers).status_code == 400
    assert client.post(url, json={"lines": [{"line_index": 1, "field": "charged_amount", "value": -5}]}, headers=headers).status_code == 400
    assert client.post(url, json={"lines": [{"line_index": 1, "field": "description", "value": "x"}]}, headers=headers).status_code == 400
