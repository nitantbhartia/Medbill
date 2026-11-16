import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)

# (facility_id, name, city, avg markup vs Medicare, grade)
FLORIDA_HOSPITALS = [
    ("100001", "Bayfront Health St Petersburg", "St Petersburg", 9.8, "F"),
    ("100002", "Memorial Regional Hospital", "Hollywood", 6.2, "D"),
    ("100003", "Tampa General Hospital", "Tampa", 4.1, "C"),
    ("100004", "Baptist Hospital of Miami", "Miami", 3.6, "C"),
    ("100005", "Lee Memorial Hospital", "Fort Myers", 2.9, "B"),
    ("100006", "Sacred Heart Hospital", "Pensacola", 2.2, "A"),
]


def _seed(hospitals, state="FL", procedures=12):
    for facility_id, name, city, markup, grade in hospitals:
        upsert_hospital_row({
            "facility_id": facility_id, "name": name, "city": city, "state": state,
            "slug": name.lower().replace(" ", "-"), "address": "1 Main St", "zip": "33000",
        })
        with get_db() as db:
            db.execute(
                "INSERT INTO billing_metrics (facility_id, avg_markup_vs_medicare, procedures_compared, billing_grade) "
                "VALUES (?, ?, ?, ?)",
                (facility_id, markup, procedures, grade),
            )


def test_state_ranking_lists_highest_markup_first():
    _seed(FLORIDA_HOSPITALS)
    r = client.get("/hospitals/fl/most-expensive/")
    assert r.status_code == 200
    assert "Most expensive hospitals in Florida" in r.text
    assert r.text.index("Bayfront Health") < r.text.index("Sacred Heart Hospital")
    assert "9.8x" in r.text and "median across 6 ranked" in r.text


def test_state_with_too_few_ranked_hospitals_is_404():
    _seed(FLORIDA_HOSPITALS[:3])
    assert client.get("/hospitals/fl/most-expensive/").status_code == 404


def test_hospitals_with_few_procedures_are_not_ranked():
    _seed(FLORIDA_HOSPITALS, procedures=2)
    assert client.get("/hospitals/fl/most-expensive/").status_code == 404


def test_ranking_page_is_in_sitemap_and_linked_from_state_page():
    _seed(FLORIDA_HOSPITALS)
    assert "/hospitals/fl/most-expensive/" in client.get("/sitemap-hospitals.xml").text
    assert "/hospitals/fl/most-expensive/" in client.get("/hospitals/fl/").text
