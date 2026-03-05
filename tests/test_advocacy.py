"""Tests for Advocacy Workspace: auth, orgs, cases, documents, analysis, letters, notes."""

import sys
import json
import pytest
from unittest.mock import MagicMock, patch

# Mock google.genai before importing anything
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

import os  # noqa: E402
os.environ["DB_PATH"] = ":memory:"
os.environ["DEBUG"] = "true"

from fastapi.testclient import TestClient  # noqa: E402
import db as _db  # noqa: E402
from main import app  # noqa: E402
from tests.conftest import SAMPLE_BILL  # noqa: E402


@pytest.fixture(autouse=True)
def fresh_db():
    """Override conftest fresh_db to also clear client cookies."""
    _db._connection = None
    _db.init_db()
    from seed_data import seed_if_empty
    seed_if_empty()
    client.cookies.clear()
    yield
    if _db._connection:
        _db._connection.close()
        _db._connection = None


client = TestClient(app)


def register_user(email="advocate@test.org", password="testpass123", name="Test Advocate"):
    resp = client.post("/api/advocacy/auth/register", json={
        "email": email, "password": password, "name": name,
    })
    # Persist auth cookie for subsequent requests
    token = resp.cookies.get("bk_auth")
    if token:
        client.cookies.set("bk_auth", token)
    return resp


def login_user(email="advocate@test.org", password="testpass123"):
    resp = client.post("/api/advocacy/auth/login", json={
        "email": email, "password": password,
    })
    token = resp.cookies.get("bk_auth")
    if token:
        client.cookies.set("bk_auth", token)
    return resp


def create_org(name="Test Advocates"):
    resp = client.post("/api/advocacy/orgs", json={
        "name": name, "contact_email": "org@test.org", "org_type": "nonprofit",
    })
    return resp


def create_case(org_id):
    resp = client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
        "patient_label": "Jane Doe",
        "hospital_name": "Memorial Hospital",
        "insurance_carrier": "Blue Cross",
        "date_of_service": "2026-01-10",
        "bill_amount": 12847.00,
        "tags": "ER, high markup",
        "patient_consent": True,
    })
    return resp


class TestAuth:
    def test_register(self):
        resp = register_user()
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert data["data"]["user"]["email"] == "advocate@test.org"
        assert data["data"]["user"]["name"] == "Test Advocate"
        assert "bk_auth" in resp.cookies

    def test_register_duplicate(self):
        register_user()
        resp = register_user()
        assert resp.status_code == 409

    def test_register_bad_password(self):
        resp = client.post("/api/advocacy/auth/register", json={
            "email": "x@test.org", "password": "short", "name": "X",
        })
        assert resp.status_code == 400

    def test_login(self):
        register_user()
        resp = login_user()
        assert resp.status_code == 200
        assert resp.json()["data"]["user"]["email"] == "advocate@test.org"

    def test_login_wrong_password(self):
        register_user()
        resp = client.post("/api/advocacy/auth/login", json={
            "email": "advocate@test.org", "password": "wrongpass",
        })
        assert resp.status_code == 401

    def test_me_unauthenticated(self):
        resp = client.get("/api/advocacy/auth/me")
        assert resp.status_code == 200
        assert resp.json()["data"]["user"] is None

    def test_me_authenticated(self):
        register_user()
        resp = client.get("/api/advocacy/auth/me")
        assert resp.status_code == 200
        assert resp.json()["data"]["user"]["email"] == "advocate@test.org"

    def test_logout(self):
        register_user()
        resp = client.post("/api/advocacy/auth/logout")
        assert resp.status_code == 200
        resp = client.get("/api/advocacy/auth/me")
        assert resp.json()["data"]["user"] is None


class TestOrgs:
    def test_create_org(self):
        register_user()
        resp = create_org()
        assert resp.status_code == 200
        assert resp.json()["data"]["name"] == "Test Advocates"

    def test_create_org_unauthenticated(self):
        resp = client.post("/api/advocacy/orgs", json={
            "name": "X", "contact_email": "x@test.org",
        })
        assert resp.status_code == 401

    def test_list_members(self):
        register_user()
        org = create_org().json()["data"]
        resp = client.get(f"/api/advocacy/orgs/{org['id']}/members")
        assert resp.status_code == 200
        members = resp.json()["data"]
        assert len(members) == 1
        assert members[0]["role"] == "admin"

    def test_invite_member(self):
        register_user()
        org = create_org().json()["data"]
        resp = client.post(f"/api/advocacy/orgs/{org['id']}/members", json={
            "email": "newuser@test.org", "role": "advocate",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["status"] == "invited"

    def test_invite_existing_user(self):
        register_user()
        org = create_org().json()["data"]
        register_user(email="second@test.org", name="Second User")
        # Log back in as admin
        login_user()
        resp = client.post(f"/api/advocacy/orgs/{org['id']}/members", json={
            "email": "second@test.org", "role": "advocate",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["status"] == "active"


class TestCases:
    def _setup(self):
        register_user()
        org = create_org().json()["data"]
        return org["id"]

    def test_create_case(self):
        org_id = self._setup()
        resp = create_case(org_id)
        assert resp.status_code == 200
        case = resp.json()["data"]
        assert case["patient_label"] == "Jane Doe"
        assert case["status"] == "new"
        assert case["patient_consent"] == 1

    def test_list_cases(self):
        org_id = self._setup()
        create_case(org_id)
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases")
        assert resp.status_code == 200
        assert resp.json()["data"]["total"] == 1

    def test_list_cases_filter_status(self):
        org_id = self._setup()
        create_case(org_id)
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases?status=new")
        assert resp.json()["data"]["total"] == 1
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases?status=analyzed")
        assert resp.json()["data"]["total"] == 0

    def test_list_cases_search(self):
        org_id = self._setup()
        create_case(org_id)
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases?search=Jane")
        assert resp.json()["data"]["total"] == 1
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases?search=nonexistent")
        assert resp.json()["data"]["total"] == 0

    def test_update_case(self):
        org_id = self._setup()
        case = create_case(org_id).json()["data"]
        resp = client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case['id']}", json={
            "status": "sent",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["status"] == "sent"

    def test_update_case_invalid_status(self):
        org_id = self._setup()
        case = create_case(org_id).json()["data"]
        resp = client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case['id']}", json={
            "status": "fake_status",
        })
        assert resp.status_code == 400

    def test_case_not_found(self):
        org_id = self._setup()
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/999")
        assert resp.status_code == 404

    def test_wrong_org_access(self):
        org_id = self._setup()
        case = create_case(org_id).json()["data"]
        # Create second org
        org2 = create_org("Other Org").json()["data"]
        resp = client.get(f"/api/advocacy/orgs/{org2['id']}/cases/{case['id']}")
        assert resp.status_code == 404


class TestNotes:
    def _setup_case(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        return org_id, case_id

    def test_add_note(self):
        org_id, case_id = self._setup_case()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={
            "content": "Called hospital billing, they need 48 hours to review.",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["content"] == "Called hospital billing, they need 48 hours to review."

    def test_list_notes(self):
        org_id, case_id = self._setup_case()
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={"content": "Note 1"})
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={"content": "Note 2"})
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes")
        assert len(resp.json()["data"]) == 2

    def test_empty_note_rejected(self):
        org_id, case_id = self._setup_case()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={"content": ""})
        assert resp.status_code == 400


class TestOverrides:
    def _setup_case(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        return org_id, case_id

    def test_set_and_get_override(self):
        org_id, case_id = self._setup_case()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/overrides", json={
            "field_name": "account_number", "field_value": "ACC-12345",
        })
        assert resp.status_code == 200

        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/overrides")
        assert resp.json()["data"]["account_number"] == "ACC-12345"

    def test_override_upsert(self):
        org_id, case_id = self._setup_case()
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/overrides", json={
            "field_name": "total_charged", "field_value": "5000",
        })
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/overrides", json={
            "field_name": "total_charged", "field_value": "7500",
        })
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/overrides")
        assert resp.json()["data"]["total_charged"] == "7500"


class TestLetterGeneration:
    def _setup_with_bill(self):
        """Create a case with an associated bill for letter generation."""
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]

        # Insert a bill directly and link it to the case
        from analyzer import save_bill_and_findings, analyze_bill
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis, "33021")

        with _db.get_db() as db:
            db.execute("UPDATE advocacy_cases SET bill_id = ? WHERE id = ?", (bill_id, case_id))

        return org_id, case_id

    def test_generate_hospital_dispute(self):
        org_id, case_id = self._setup_with_bill()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        })
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert "content" in data
        assert len(data["content"]) > 100
        assert data["disclaimer"]

    def test_generate_insurance_appeal(self):
        org_id, case_id = self._setup_with_bill()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "insurance_appeal", "fields": {"policy_number": "POL-999"},
        })
        assert resp.status_code == 200
        assert "appeal" in resp.json()["data"]["content"].lower() or "Appeal" in resp.json()["data"]["content"]

    def test_generate_debt_validation(self):
        org_id, case_id = self._setup_with_bill()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "debt_validation",
            "fields": {"collector_name": "ABC Collections", "collector_address": "123 Main St", "amount": "5000"},
        })
        assert resp.status_code == 200
        assert "validation" in resp.json()["data"]["content"].lower() or "Validation" in resp.json()["data"]["content"]

    def test_invalid_letter_type(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "fake_type",
        })
        assert resp.status_code == 400

    def test_list_letters(self):
        org_id, case_id = self._setup_with_bill()
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        })
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters")
        assert len(resp.json()["data"]) == 1

    def test_update_letter_content(self):
        org_id, case_id = self._setup_with_bill()
        letter = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        }).json()["data"]

        resp = client.patch(
            f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter['id']}",
            json={"content": "Updated letter content here."},
        )
        assert resp.status_code == 200

    def test_mark_letter_reviewed(self):
        org_id, case_id = self._setup_with_bill()
        letter = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        }).json()["data"]

        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter['id']}/review")
        assert resp.status_code == 200
        assert resp.json()["data"]["reviewed"]

    def test_mark_letter_sent(self):
        org_id, case_id = self._setup_with_bill()
        letter = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        }).json()["data"]

        resp = client.post(
            f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter['id']}/sent",
            json={"sent_date": "2026-03-05"},
        )
        assert resp.status_code == 200
        assert resp.json()["data"]["marked_sent"]


class TestRecommendations:
    def test_recommendations_with_findings(self):
        """Test that analysis produces actionable recommendations."""
        from advocacy import _build_recommendations

        analysis = {
            "findings": [
                {"type": "price_markup", "severity": "high", "message": "CPT 99285 charged 8.2x Medicare rate", "potential_savings": 3500},
                {"type": "duplicate_charge", "severity": "high", "message": "Duplicate CPT 80053", "potential_savings": 350},
            ],
            "total_findings": 2,
            "total_potential_savings": 3850,
        }
        case = {"tags": "", "status": "analyzed"}

        recs = _build_recommendations(analysis, {"line_items": []}, case)
        types = [r["letter_type"] for r in recs]
        assert "hospital_dispute" in types
        assert all(r.get("reason") for r in recs)
        assert all(r.get("based_on") for r in recs)

    def test_recommendations_collections(self):
        """Collections-tagged case recommends debt validation."""
        from advocacy import _build_recommendations

        analysis = {"findings": [], "total_findings": 0, "total_potential_savings": 0}
        case = {"tags": "collections", "status": "new"}

        recs = _build_recommendations(analysis, {"line_items": [{"cpt_code": "99283"}]}, case)
        types = [r["letter_type"] for r in recs]
        assert "debt_validation" in types

    def test_no_recommendations_no_findings(self):
        """No findings but has line items -> suggest itemized bill."""
        from advocacy import _build_recommendations

        analysis = {"findings": [], "total_findings": 0, "total_potential_savings": 0}
        case = {"tags": "", "status": "analyzed"}

        recs = _build_recommendations(analysis, {"line_items": [{"cpt_code": "99283"}]}, case)
        assert len(recs) >= 1
        assert recs[0]["action"] == "Request itemized bill"


class TestPages:
    def test_login_page(self):
        resp = client.get("/advocacy/login")
        assert resp.status_code == 200
        assert "Sign In" in resp.text or "Sign in" in resp.text

    def test_cases_page(self):
        resp = client.get("/advocacy/cases")
        assert resp.status_code == 200

    def test_new_case_page(self):
        resp = client.get("/advocacy/cases/new")
        assert resp.status_code == 200

    def test_case_detail_page(self):
        resp = client.get("/advocacy/cases/1")
        assert resp.status_code == 200

    def test_team_page(self):
        resp = client.get("/advocacy/team")
        assert resp.status_code == 200

    def test_setup_page(self):
        resp = client.get("/advocacy/setup")
        assert resp.status_code == 200

    def test_shared_case_page(self):
        resp = client.get("/advocacy/shared/some-token-here")
        assert resp.status_code == 200


# ── V2 Feature Tests ────────────────────────────────────────────────────────

class TestActivityTimeline:
    def _setup_case(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        return org_id, case_id

    def test_activity_logged_on_case_create(self):
        org_id, case_id = self._setup_case()
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/activity")
        assert resp.status_code == 200
        activities = resp.json()["data"]
        assert any(a["action"] == "case_created" for a in activities)

    def test_activity_logged_on_note(self):
        org_id, case_id = self._setup_case()
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={"content": "test note"})
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/activity")
        activities = resp.json()["data"]
        assert any(a["action"] == "note_added" for a in activities)

    def test_activity_logged_on_status_change(self):
        org_id, case_id = self._setup_case()
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}", json={"status": "sent"})
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/activity")
        activities = resp.json()["data"]
        assert any(a["action"] == "case_updated" for a in activities)


class TestShareLinks:
    def _setup_case(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        return org_id, case_id

    def test_create_share_link(self):
        org_id, case_id = self._setup_case()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share", json={
            "label": "For patient",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["token"]

    def test_list_share_links(self):
        org_id, case_id = self._setup_case()
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share", json={"label": "Link 1"})
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share", json={"label": "Link 2"})
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share")
        assert len(resp.json()["data"]) == 2

    def test_access_shared_case(self):
        org_id, case_id = self._setup_case()
        link = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share", json={}).json()["data"]
        # Access shared case (no auth needed)
        client.cookies.clear()
        resp = client.get(f"/api/advocacy/shared/{link['token']}")
        assert resp.status_code == 200
        case = resp.json()["data"]
        assert case["patient_label"] == "Jane Doe"
        # Sensitive fields should be stripped
        assert "created_by" not in case
        assert "assigned_to" not in case

    def test_revoke_share_link(self):
        org_id, case_id = self._setup_case()
        link = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share", json={}).json()["data"]
        # Revoke
        resp = client.delete(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/share/{link['id']}")
        assert resp.status_code == 200
        # Access should fail
        client.cookies.clear()
        resp = client.get(f"/api/advocacy/shared/{link['token']}")
        assert resp.status_code == 410

    def test_invalid_share_token(self):
        resp = client.get("/api/advocacy/shared/nonexistent-token")
        assert resp.status_code == 404


class TestViewerRole:
    def _setup_with_viewer(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        # Create viewer
        register_user(email="viewer@test.org", name="Viewer User")
        login_user()  # log back as admin
        client.post(f"/api/advocacy/orgs/{org_id}/members", json={
            "email": "viewer@test.org", "role": "viewer",
        })
        return org_id, case_id

    def test_viewer_can_read_cases(self):
        org_id, case_id = self._setup_with_viewer()
        login_user(email="viewer@test.org")
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases")
        assert resp.status_code == 200

    def test_viewer_cannot_create_case(self):
        org_id, _ = self._setup_with_viewer()
        login_user(email="viewer@test.org")
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
            "patient_label": "New Patient",
        })
        assert resp.status_code == 403

    def test_viewer_cannot_add_note(self):
        org_id, case_id = self._setup_with_viewer()
        login_user(email="viewer@test.org")
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={
            "content": "This should fail",
        })
        assert resp.status_code == 403

    def test_viewer_can_read_notes(self):
        org_id, case_id = self._setup_with_viewer()
        # Admin adds a note
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes", json={"content": "Admin note"})
        # Viewer reads notes
        login_user(email="viewer@test.org")
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/notes")
        assert resp.status_code == 200
        assert len(resp.json()["data"]) == 1


class TestLetterVersionHistory:
    def _setup_with_letter(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        from analyzer import save_bill_and_findings, analyze_bill
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis, "33021")
        with _db.get_db() as db:
            db.execute("UPDATE advocacy_cases SET bill_id = ? WHERE id = ?", (bill_id, case_id))
        letter = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters", json={
            "letter_type": "hospital_dispute", "fields": {},
        }).json()["data"]
        return org_id, case_id, letter["id"]

    def test_version_created_on_edit(self):
        org_id, case_id, letter_id = self._setup_with_letter()
        # Edit the letter
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}", json={
            "content": "Updated content v1",
        })
        # Check versions
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions")
        assert resp.status_code == 200
        versions = resp.json()["data"]
        assert len(versions) == 1  # One previous version saved

    def test_multiple_versions(self):
        org_id, case_id, letter_id = self._setup_with_letter()
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}", json={"content": "v1"})
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}", json={"content": "v2"})
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions")
        assert len(resp.json()["data"]) == 2

    def test_restore_version(self):
        org_id, case_id, letter_id = self._setup_with_letter()
        # Get original content
        original = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters").json()["data"][0]["content"]
        # Edit
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}", json={"content": "New content"})
        # Get version ID
        versions = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions").json()["data"]
        version_id = versions[0]["id"]
        # Restore
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters/{letter_id}/versions/{version_id}/restore")
        assert resp.status_code == 200
        # Verify content restored
        letters = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}/letters").json()["data"]
        assert letters[0]["content"] == original


class TestBulkOperations:
    def _setup_cases(self, count=3):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_ids = []
        for i in range(count):
            resp = client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
                "patient_label": f"Patient {i}",
                "hospital_name": "Memorial Hospital",
                "patient_consent": True,
            })
            case_ids.append(resp.json()["data"]["id"])
        return org_id, case_ids

    def test_bulk_status_update(self):
        org_id, case_ids = self._setup_cases()
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/status", json={
            "case_ids": case_ids,
            "status": "sent",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["updated"] == 3

        # Verify all cases updated
        for cid in case_ids:
            case = client.get(f"/api/advocacy/orgs/{org_id}/cases/{cid}").json()["data"]
            assert case["status"] == "sent"

    def test_bulk_status_invalid(self):
        org_id, case_ids = self._setup_cases(1)
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/status", json={
            "case_ids": case_ids,
            "status": "invalid_status",
        })
        assert resp.status_code == 400

    def test_bulk_assign(self):
        org_id, case_ids = self._setup_cases()
        # Get user ID (the creator)
        me = client.get("/api/advocacy/auth/me").json()["data"]["user"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/assign", json={
            "case_ids": case_ids,
            "assigned_to": me["id"],
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["updated"] == 3

    def test_bulk_export(self):
        org_id, case_ids = self._setup_cases()
        # Add a note to one case
        client.post(f"/api/advocacy/orgs/{org_id}/cases/{case_ids[0]}/notes", json={"content": "Test note"})
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/export", json={
            "case_ids": case_ids,
        })
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert len(data) == 3
        assert data[0].get("notes_list") is not None

    def test_bulk_empty_case_ids(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/status", json={
            "case_ids": [],
            "status": "sent",
        })
        assert resp.status_code == 400


class TestDashboard:
    def test_dashboard_empty(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.get(f"/api/advocacy/orgs/{org_id}/dashboard")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert data["total_cases"] == 0
        assert data["total_billed"] == 0
        assert data["total_saved"] == 0

    def test_dashboard_with_cases(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        # Create cases with different statuses and amounts
        client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
            "patient_label": "A", "bill_amount": 5000, "patient_consent": True,
        })
        client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
            "patient_label": "B", "bill_amount": 8000, "patient_consent": True,
        })
        resp = client.get(f"/api/advocacy/orgs/{org_id}/dashboard")
        data = resp.json()["data"]
        assert data["total_cases"] == 2
        assert data["total_billed"] == 13000
        assert data["by_status"]["new"] == 2

    def test_dashboard_page(self):
        resp = client.get("/advocacy/dashboard")
        assert resp.status_code == 200

    def test_dashboard_overdue_deadlines(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_resp = client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
            "patient_label": "Urgent", "patient_consent": True,
        })
        case_id = case_resp.json()["data"]["id"]
        # Set an overdue appeal deadline
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}", json={
            "appeal_deadline": "2025-01-01",
        })
        resp = client.get(f"/api/advocacy/orgs/{org_id}/dashboard")
        data = resp.json()["data"]
        assert len(data["overdue_deadlines"]) == 1
        assert data["overdue_deadlines"][0]["patient_label"] == "Urgent"


class TestDeadlineTracking:
    def test_set_appeal_deadline(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        resp = client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}", json={
            "appeal_deadline": "2026-06-01",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["appeal_deadline"] == "2026-06-01"

    def test_set_follow_up_date(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        resp = client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}", json={
            "follow_up_date": "2026-04-15",
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["follow_up_date"] == "2026-04-15"

    def test_deadline_persists_in_get(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        case_id = create_case(org_id).json()["data"]["id"]
        client.patch(f"/api/advocacy/orgs/{org_id}/cases/{case_id}", json={
            "appeal_deadline": "2026-06-01",
            "follow_up_date": "2026-04-15",
        })
        resp = client.get(f"/api/advocacy/orgs/{org_id}/cases/{case_id}")
        data = resp.json()["data"]
        assert data["appeal_deadline"] == "2026-06-01"
        assert data["follow_up_date"] == "2026-04-15"


class TestCSVExport:
    def test_csv_export(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        create_case(org_id)
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/export-csv", json={})
        assert resp.status_code == 200
        assert resp.headers["content-type"] == "text/csv; charset=utf-8"
        content = resp.text
        assert "Patient" in content
        assert "Jane Doe" in content

    def test_csv_export_selected(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        c1 = create_case(org_id).json()["data"]["id"]
        client.post(f"/api/advocacy/orgs/{org_id}/cases", json={
            "patient_label": "Other Patient", "patient_consent": True,
        })
        resp = client.post(f"/api/advocacy/orgs/{org_id}/cases/bulk/export-csv", json={
            "case_ids": [c1],
        })
        assert resp.status_code == 200
        assert "Jane Doe" in resp.text
        assert "Other Patient" not in resp.text


class TestCaseTemplates:
    def test_list_builtin_templates(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.get(f"/api/advocacy/orgs/{org_id}/templates")
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert len(data) >= 4  # 4 builtins
        names = [t["name"] for t in data]
        assert "Hospital Billing Dispute" in names
        assert "Insurance Denial Appeal" in names

    def test_create_custom_template(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/templates", json={
            "name": "Workers Comp",
            "template_type": "workers_comp",
            "default_fields": {"tags": "workers comp", "notes": "Work injury case."},
        })
        assert resp.status_code == 200
        assert resp.json()["data"]["name"] == "Workers Comp"

        # Verify it shows in list
        resp = client.get(f"/api/advocacy/orgs/{org_id}/templates")
        names = [t["name"] for t in resp.json()["data"]]
        assert "Workers Comp" in names

    def test_delete_custom_template(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/templates", json={
            "name": "Temp", "template_type": "temp", "default_fields": {},
        })
        tid = resp.json()["data"]["id"]
        resp = client.delete(f"/api/advocacy/orgs/{org_id}/templates/{tid}")
        assert resp.status_code == 200

    def test_create_template_empty_name(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.post(f"/api/advocacy/orgs/{org_id}/templates", json={
            "name": "", "template_type": "test", "default_fields": {},
        })
        assert resp.status_code == 400

    def test_builtin_templates_have_default_fields(self):
        register_user()
        org_id = create_org().json()["data"]["id"]
        resp = client.get(f"/api/advocacy/orgs/{org_id}/templates")
        for t in resp.json()["data"]:
            if t.get("builtin"):
                assert "tags" in t["default_fields"]
                assert "notes" in t["default_fields"]
