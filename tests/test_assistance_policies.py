import pytest
from fastapi.testclient import TestClient

import api
import assistance_policies as ap
from db import get_db
from main import app

client = TestClient(app, follow_redirects=False)

POLICY = ("Patients at or below 200% of the federal poverty level receive free care. "
          "Patients with income up to 350% of the federal poverty level receive a discount, capped at what Medicare pays. "
          "Please bring a recent pay stub and a photo ID. Patients on Medi-Cal are presumed eligible. ")


def raw(**overrides):
    base = {
        "free_care_max_fpl": {"value": 200, "quote": "Patients at or below 200% of the federal poverty level receive free care."},
        "discount_max_fpl": {"value": 350, "quote": "Patients with income up to 350% of the federal poverty level receive a discount, capped at what Medicare pays."},
        "discount_rule": {"value": "capped at what Medicare pays", "quote": "Patients with income up to 350% of the federal poverty level receive a discount, capped at what Medicare pays."},
        "required_documents": {"value": ["pay stub", "photo ID"], "quote": "Please bring a recent pay stub and a photo ID."},
        "application_deadline": None,
    }
    return {**base, **overrides}


def test_limits_and_documents_come_with_their_quotes():
    terms, evidence = ap.verify_terms(raw(), POLICY)
    assert (terms["free_care_max_fpl"], terms["discount_max_fpl"]) == (200, 350)
    assert terms["required_documents"] == ["pay stub", "photo ID"]
    assert "200%" in evidence["free_care_max_fpl"]


def test_a_field_the_policy_does_not_state_is_null_not_a_guess():
    terms, _ = ap.verify_terms(raw(application_deadline={"value": "30 days", "quote": "Apply within 30 days of discharge."}), POLICY)
    assert "application_deadline" not in terms


def test_an_income_limit_must_appear_in_its_quote_and_the_quote_in_the_policy():
    wrong_number = raw(free_care_max_fpl={"value": 300, "quote": "Patients at or below 200% of the federal poverty level receive free care."})
    assert "free_care_max_fpl" not in ap.verify_terms(wrong_number, POLICY)[0]
    invented = raw(free_care_max_fpl={"value": 100, "quote": "Patients at or below 100% of the poverty level get free care."})
    assert "free_care_max_fpl" not in ap.verify_terms(invented, POLICY)[0]


def test_california_discount_limit_below_400_is_shown_as_400_for_non_rural_hospitals():
    terms, evidence = ap.verify_terms(raw(), POLICY)
    assert ap.apply_legal_floors(dict(terms), dict(evidence))["discount_max_fpl"] == 400
    assert ap.apply_legal_floors(dict(terms), dict(evidence), rural=True)["discount_max_fpl"] == 350


def test_endpoint_returns_terms_with_quotes_and_an_unchecked_label():
    api._rate_buckets.clear()
    terms, evidence = ap.verify_terms(raw(), POLICY)
    ap.save_policy({"name": "Harbor View", "city": "San Diego", "zip": "92101", "license": "1", "facility_id": "050001",
                    "application_form_url": "https://example.org/form.pdf"}, "https://example.org/p.pdf", "abc", "06/12/2026",
                   ap.apply_legal_floors(terms, evidence), evidence)
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    headers = {"Authorization": f"Bearer {data['token']}"}
    body = client.get("/api/m/assistance/policy/050001", headers=headers).json()["data"]
    assert body["label"].endswith("(not yet checked by BillKarma)")
    assert body["terms"]["free_care_max_fpl"]["quote"].startswith("Patients at or below 200%")
    assert body["terms"]["discount_max_fpl"]["value"] == 400 and "California law" in body["floor_note"]
    assert client.get("/api/m/assistance/policy/none", headers=headers).status_code == 404
