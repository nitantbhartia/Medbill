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
    assert "Basis: patient responsibility" in html
    assert "Itemized sum: <strong>$102.09</strong>" in html
    assert "Bill total: <strong>$102.09</strong>" in html
    assert "Reconciliation looks good" in html


def test_confirm_reconciliation_uses_billed_basis_when_patient_fields_missing():
    bill_id = _insert_bill(740.62, None)
    _insert_line_item(bill_id, 331.00, None)
    _insert_line_item(bill_id, 409.62, None)

    resp = client.get(f"/confirm/{bill_id}")
    assert resp.status_code == 200
    html = resp.text
    assert "Basis: billed charges" in html
    assert "Itemized sum: <strong>$740.62</strong>" in html
    assert "Bill total: <strong>$740.62</strong>" in html
