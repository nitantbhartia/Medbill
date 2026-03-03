"""Tests for public-web transparency URL discovery."""

import transparency_discovery
from db import get_db
from hospital_seo import upsert_hospital_row


def test_decode_ddg_redirect_extracts_target_url():
    redirected = (
        "https://duckduckgo.com/l/?uddg="
        "https%3A%2F%2Fexample.org%2Fprice-transparency%2Fstandard-charges.csv"
    )
    resolved = transparency_discovery.decode_ddg_redirect(redirected)
    assert resolved == "https://example.org/price-transparency/standard-charges.csv"


def test_extract_candidate_links_filters_to_transparency_urls():
    html_text = """
    <html><body>
      <a href="/price-transparency/">Price transparency</a>
      <a href="https://example.org/files/standard-charges.csv">CSV</a>
      <a href="https://example.org/about">About</a>
    </body></html>
    """
    links = transparency_discovery.extract_candidate_links(html_text, "https://example.org")
    assert links == [
        "https://example.org/price-transparency/",
        "https://example.org/files/standard-charges.csv",
    ]


def test_discover_missing_hospital_urls_inserts_pending_record(monkeypatch):
    upsert_hospital_row(
        {
            "facility_id": "12345",
            "name": "Discovery General Hospital",
            "city": "Tampa",
            "state": "FL",
            "slug": "discovery-general-hospital-tampa",
            "bed_count": 250,
        }
    )

    monkeypatch.setattr(
        transparency_discovery,
        "discover_transparency_url",
        lambda name, city, state: (  # noqa: ARG005
            "https://example.org/price-transparency/",
            "search_result",
            0.9,
        ),
    )

    summary = transparency_discovery.discover_missing_hospital_urls(limit=10, sleep_seconds=0)
    assert summary["scanned"] >= 1
    assert summary["discovered"] == 1

    with get_db() as conn:
        row = conn.execute(
            "SELECT file_url, parse_status, parse_notes FROM transparency_files WHERE facility_id = ?",
            ("012345",),
        ).fetchone()
    assert row is not None
    assert row["file_url"] == "https://example.org/price-transparency/"
    assert row["parse_status"] == "pending"
    assert "Discovered via site search" in row["parse_notes"]


def test_select_newly_discovered_hospitals_returns_pending_discoveries():
    upsert_hospital_row(
        {
            "facility_id": "22222",
            "name": "Pending Discovery Hospital",
            "city": "Orlando",
            "state": "FL",
            "slug": "pending-discovery-hospital-orlando",
            "bed_count": 150,
        }
    )
    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO transparency_files (facility_id, file_url, parse_status, parse_notes)
            VALUES (?, ?, 'pending', ?)
            """,
            ("022222", "https://example.org/standard-charges.csv", "Discovered via site search (page_link, confidence=0.78)"),
        )

    selected = transparency_discovery.select_newly_discovered_hospitals(limit=10)
    assert any(item["facility_id"] == "022222" for item in selected)
