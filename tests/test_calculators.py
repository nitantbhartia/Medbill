"""Tests for calculator API endpoints and page routes."""

import sys
from unittest.mock import MagicMock

# Mock google.genai before importing main/scanner
sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())

import os  # noqa: E402
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


class TestCostLookupAPI:
    def test_cost_lookup_known_cpt(self):
        r = client.get("/api/calculator/cost?cpt_code=99285&zip_code=33021")
        assert r.status_code == 200
        d = r.json()["data"]
        assert d["cpt_code"] == "99285"
        assert d["medicare_rate"] is not None
        assert d["medicare_rate"] > 0

    def test_cost_lookup_with_opps(self):
        r = client.get("/api/calculator/cost?cpt_code=99285")
        d = r.json()["data"]
        if d["opps_rate"]:
            assert d["total_medicare"] == round(d["medicare_rate"] + d["opps_rate"], 2)

    def test_cost_lookup_unknown_cpt(self):
        r = client.get("/api/calculator/cost?cpt_code=ZZZZZ")
        assert r.status_code == 200
        d = r.json()["data"]
        assert d["medicare_rate"] is None

    def test_cost_lookup_missing_cpt(self):
        r = client.get("/api/calculator/cost?cpt_code=")
        assert r.status_code == 400

    def test_cost_lookup_no_zip(self):
        r = client.get("/api/calculator/cost?cpt_code=99285")
        assert r.status_code == 200
        assert r.json()["data"]["zip_code"] is None


class TestMarkupCheckerAPI:
    def test_markup_check_known_cpt(self):
        r = client.get("/api/calculator/markup?cpt_code=99285&charged=2500&zip_code=33021")
        assert r.status_code == 200
        d = r.json()["data"]
        assert d["charged"] == 2500
        assert "medicare" in d
        assert d["medicare"]["markup"] > 0
        assert d["medicare"]["assessment"] in ("fair", "elevated", "high")

    def test_markup_high_charge(self):
        r = client.get("/api/calculator/markup?cpt_code=99285&charged=50000")
        d = r.json()["data"]
        if d.get("medicare"):
            assert d["medicare"]["assessment"] == "high"

    def test_markup_fair_charge(self):
        r = client.get("/api/calculator/markup?cpt_code=99285&charged=100")
        d = r.json()["data"]
        if d.get("medicare"):
            assert d["medicare"]["assessment"] == "fair"

    def test_markup_missing_charged(self):
        r = client.get("/api/calculator/markup?cpt_code=99285&charged=0")
        assert r.status_code == 400

    def test_markup_missing_cpt(self):
        r = client.get("/api/calculator/markup?cpt_code=&charged=100")
        assert r.status_code == 400

    def test_markup_potential_savings(self):
        r = client.get("/api/calculator/markup?cpt_code=99285&charged=2500")
        d = r.json()["data"]
        if d.get("medicare"):
            assert d["medicare"]["potential_savings"] >= 0


class TestCalculatorPages:
    def test_calculator_page_loads(self):
        r = client.get("/calculator")
        assert r.status_code == 200
        assert "Procedure Cost Lookup" in r.text
        assert "Markup Checker" in r.text

    def test_embed_cost_mode(self):
        r = client.get("/calculator/embed?mode=cost&cpt=99285")
        assert r.status_code == 200
        assert "embed-card" in r.text
        assert "99285" in r.text

    def test_embed_markup_mode(self):
        r = client.get("/calculator/embed?mode=markup")
        assert r.status_code == 200
        assert "Amount Charged" in r.text


class TestGuidePages:
    def test_guides_index_loads(self):
        r = client.get("/guides/")
        assert r.status_code == 200
        assert "how-to-read" in r.text

    def test_guide_article_loads(self):
        r = client.get("/guides/how-to-read-your-medical-bill")
        assert r.status_code == 200
        assert "CPT" in r.text
        assert "iframe" in r.text
        assert "schema.org" in r.text

    def test_guide_article_has_sources(self):
        r = client.get("/guides/how-to-read-your-medical-bill")
        assert "cms.gov" in r.text
        assert "healthaffairs.org" in r.text

    def test_guide_not_found(self):
        r = client.get("/guides/nonexistent-guide")
        assert r.status_code == 200
        assert "not found" in r.text.lower()
