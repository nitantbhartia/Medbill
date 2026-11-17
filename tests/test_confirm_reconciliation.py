"""Regression tests for confirm-page reconciliation basis selection."""

import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import db as _db  # noqa: E402
from main import app  # noqa: E402


client = TestClient(app)


def _insert_bill(total_charged: float, total_patient_owes: float | None) -> int:
    with _db.get_db() as db:
        cur = db.execute(
            """
            INSERT INTO bills (provider_name, bill_date, zip_code, total_charged, total_patient_owes, status)
            VALUES (?, ?, ?, ?, ?, 'scanned')
            """,
            ("Test Provider", "2026-02-24", "10001", total_charged, total_patient_owes),
        )
        return int(cur.lastrowid)


def _insert_line_item(bill_id: int, charged: float, patient_resp: float | None) -> None:
    with _db.get_db() as db:
        db.execute(
            """
            INSERT INTO line_items (bill_id, cpt_code, description, quantity, charged_amount, patient_responsibility, extraction_confidence)
            VALUES (?, ?, ?, 1, ?, ?, 'high')
            """,
            (bill_id, "99214", "Office visit", charged, patient_resp),
        )


def test_confirm_reconciliation_prefers_patient_responsibility_basis_for_insured_bill():
    bill_id = _insert_bill(740.62, 102.09)
    _insert_line_item(bill_id, 331.00, 50.00)
    _insert_line_item(bill_id, 409.62, 52.09)

    resp = client.get(f"/confirm/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert "Compared using patient responsibility." in html
    assert "Lines add up to <strong>$102.09</strong>" in html
    assert "Bill total: <strong>$102.09</strong>" in html
    assert "The lines match the bill total." in html


def test_confirm_reconciliation_uses_billed_basis_when_patient_fields_missing():
    bill_id = _insert_bill(740.62, None)
    _insert_line_item(bill_id, 331.00, None)
    _insert_line_item(bill_id, 409.62, None)

    resp = client.get(f"/confirm/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert "Compared using billed charges." in html
    assert "Lines add up to <strong>$740.62</strong>" in html
    assert "Bill total: <strong>$740.62</strong>" in html


def test_confirm_asks_for_zip_when_the_bill_has_none_and_analyze_saves_it():
    bill_id = _insert_bill(740.62, None)
    with _db.get_db() as conn:
        conn.execute("UPDATE bills SET zip_code = '00000' WHERE id = ?", (bill_id,))
    assert 'id="confirm-zip"' in client.get(f"/confirm/{bill_id}").text

    items = [{"cpt_code": "99285", "description": "Emergency visit, level 5", "billed_amount": 740.62, "patient_responsibility": None}]
    assert client.post(f"/api/analyze/{bill_id}", json={"line_items": items, "zip_code": "33021"}).status_code == 200
    with _db.get_db() as conn:
        assert conn.execute("SELECT zip_code FROM bills WHERE id = ?", (bill_id,)).fetchone()["zip_code"] == "33021"
    assert 'id="confirm-zip"' not in client.get(f"/confirm/{bill_id}").text
