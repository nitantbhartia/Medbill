import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

from db import get_db  # noqa: E402
from main import app  # noqa: E402
from tools_catalog import list_tools, get_tool  # noqa: E402


client = TestClient(app)


def test_tools_registry_complete_and_unique():
    tools = list_tools()
    assert len(tools) == 16
    slugs = [t["slug"] for t in tools]
    assert len(set(slugs)) == 16
    for tool in tools:
        assert tool["title"]
        assert tool["description"]
        assert tool["form_fields"]
        assert tool["lead_magnet"]["title"]


def test_tools_index_renders():
    resp = client.get("/tools/")
    assert resp.status_code == 200
    assert "BillKarma Free Tools" in resp.text


def test_tool_detail_renders():
    resp = client.get("/tools/medical-bill-error-checker/")
    assert resp.status_code == 200
    assert "Medical Bill Error Checker" in resp.text
    assert "Run Tool" in resp.text


def test_tool_detail_404():
    resp = client.get("/tools/not-a-tool/")
    assert resp.status_code == 200
    assert "Tool not found" in resp.text


def test_tools_in_sitemap():
    resp = client.get("/sitemap-hospitals.xml")
    assert resp.status_code == 200
    text = resp.text
    assert "/tools/" in text
    assert "/tools/medical-bill-error-checker/" in text


def test_tool_run_response_contract():
    payload = {
        "state": "FL",
        "date_of_service": "2018-01-01",
    }
    resp = client.post("/api/tools/medical-debt-statute-of-limitations-checker/run", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["tool_slug"] == "medical-debt-statute-of-limitations-checker"
    assert "result_state" in data
    assert "summary" in data
    assert "details" in data
    assert "cta" in data
    assert "lead_magnet" in data


def test_tool_lead_capture_persists():
    resp = client.post(
        "/api/tools/lead-capture",
        json={
            "email": "person@example.com",
            "tool_slug": "medical-bill-error-checker",
            "lead_magnet_key": "audit_checklist",
            "context": {"source": "test"},
        },
    )
    assert resp.status_code == 200

    with get_db() as db:
        row = db.execute(
            "SELECT email, tool_slug, lead_magnet_key FROM tool_leads WHERE email = ?",
            ("person@example.com",),
        ).fetchone()
    assert row is not None
    assert row["tool_slug"] == "medical-bill-error-checker"


def test_financial_assistance_branch_likely_eligible():
    resp = client.post(
        "/api/tools/hospital-financial-assistance-calculator/run",
        json={"hospital_name": "", "income": 30000, "household_size": 3},
    )
    assert resp.status_code == 200
    assert resp.json()["result_state"] == "likely_eligible"


def test_denial_appeal_reason_mapping_fallback():
    resp = client.post(
        "/api/tools/insurance-denial-appeal-letter-generator/run",
        json={
            "patient_name": "Pat",
            "insurance_company": "Insurer",
            "denial_reason_code": "ZZ-999",
            "procedure": "MRI",
            "date_of_denial": "2026-01-01",
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["result_state"] == "generated"
    assert "not mapped" in data["details"]["reason_mapping"].lower()


def test_hospital_grade_lookup_found_branch():
    with get_db() as db:
        db.execute(
            """
            INSERT OR REPLACE INTO hospitals (facility_id, name, city, state, slug, state_slug, city_slug, is_nonprofit)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ("123456", "Demo Medical Center", "Miami", "FL", "demo-medical-center", "fl", "miami", 1),
        )
        db.execute(
            """
            INSERT OR REPLACE INTO billing_metrics (facility_id, avg_markup_vs_medicare, billing_grade, procedures_compared)
            VALUES (?, ?, ?, ?)
            """,
            ("123456", 6.2, "F", 10),
        )

    resp = client.post(
        "/api/tools/hospital-billing-grade-lookup/run",
        json={"hospital_name": "Demo Medical"},
    )
    assert resp.status_code == 200
    assert resp.json()["result_state"] in {"found", "found_f"}


def test_get_tool_interface():
    tool = get_tool("medicare-rate-lookup")
    assert tool is not None
    assert tool["slug"] == "medicare-rate-lookup"
