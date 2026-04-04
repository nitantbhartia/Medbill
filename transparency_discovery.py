"""Automatic discovery of hospital transparency file URLs.

This is a lightweight, public-web fallback for hospitals missing a
`transparency_files.file_url` or stuck on broken transparency links.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
import html
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import parse_qs, urljoin, urlparse

from db import get_db


USER_AGENT = "Mozilla/5.0 (compatible; BillKarmaBot/1.0; +https://billkarma.app)"
SEARCH_BASES = (
    "https://html.duckduckgo.com/html/",
    "https://lite.duckduckgo.com/lite/",
)
FILE_EXTS = (".csv", ".json", ".xlsx", ".xls", ".zip", ".dot")
KEYWORD_PATTERNS = (
    "price transparency",
    "price-transparency",
    "pricing transparency",
    "standard charges",
    "standard-charges",
    "chargemaster",
    "machine readable",
    "machine-readable",
    "cms required file",
    "file of standard charges",
)
COMMON_PATHS = (
    "/price-transparency/",
    "/pricing-transparency/",
    "/standard-charges/",
    "/chargemaster/",
    "/financial-information-price-transparency/",
    "/financial-information/price-transparency/",
    "/patients-visitors/price-transparency/",
    "/for-patients/price-transparency/",
)


@dataclass
class DiscoveryResult:
    facility_id: str
    discovered_url: str | None
    discovery_method: str | None
    confidence: float
    notes: str


def _fetch_text(url: str, timeout: int = 10) -> tuple[str, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("Content-Type")
        body = resp.read().decode("utf-8", "ignore")
    return body, content_type


def _head_or_get(url: str, timeout: int = 8) -> tuple[bool, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, resp.headers.get("Content-Type")
    except Exception:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return True, resp.headers.get("Content-Type")
        except Exception:
            return False, None


def decode_ddg_redirect(url: str) -> str:
    if "duckduckgo.com/l/?" not in url:
        return url
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    uddg = qs.get("uddg", [url])[0]
    return urllib.parse.unquote(uddg)


def _looks_transparency_url(url: str) -> bool:
    lower = url.lower()
    return any(ext in lower for ext in FILE_EXTS) or any(token in lower for token in KEYWORD_PATTERNS)


def probe_existing_domain(file_url: str | None) -> tuple[str | None, str | None, float]:
    if not file_url or not str(file_url).startswith(("http://", "https://")):
        return None, None, 0.0
    parsed = urlparse(str(file_url))
    root = f"{parsed.scheme}://{parsed.netloc}"
    for path in COMMON_PATHS:
        probe = urljoin(root, path)
        ok, _ = _head_or_get(probe)
        if ok:
            return probe, "existing_domain_probe", 0.72
    return None, None, 0.0


def extract_candidate_links(html_text: str, base_url: str) -> list[str]:
    links: list[str] = []
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html_text, flags=re.I)
    for href in hrefs:
        href = html.unescape(href.strip())
        if href.startswith(("javascript:", "mailto:", "#")):
            continue
        abs_url = urljoin(base_url, href)
        if _looks_transparency_url(abs_url):
            links.append(abs_url)
    return list(dict.fromkeys(links))


def search_candidate_urls(name: str, city: str, state: str, max_results: int = 3) -> list[str]:
    query = f'{name} {city} {state} ("price transparency" OR "standard charges" OR chargemaster)'
    for base in SEARCH_BASES:
        url = base + "?" + urllib.parse.urlencode({"q": query})
        try:
            body, _ = _fetch_text(url)
        except Exception:
            continue
        raw_links = re.findall(r'result__a[^>]+href="([^"]+)"', body, flags=re.I)
        if not raw_links:
            raw_links = re.findall(r'<a rel="nofollow" href="([^"]+)"', body, flags=re.I)
        decoded = [decode_ddg_redirect(link) for link in raw_links]
        links = [u for u in decoded if u.startswith(("http://", "https://"))][:max_results]
        if links:
            return links
    return []


def discover_transparency_url(name: str, city: str, state: str) -> tuple[str | None, str | None, float]:
    candidates = search_candidate_urls(name, city, state)
    if not candidates:
        return None, None, 0.0

    # Direct result hit.
    for cand in candidates:
        if _looks_transparency_url(cand):
            return cand, "search_result", 0.90

    # Prefer well-known transparency paths on the candidate domains before
    # downloading full result pages.
    probed_roots: set[str] = set()
    for cand in candidates:
        parsed = urlparse(cand)
        root = f"{parsed.scheme}://{parsed.netloc}"
        if root in probed_roots:
            continue
        probed_roots.add(root)
        for path in COMMON_PATHS:
            probe = urljoin(root, path)
            ok, _ = _head_or_get(probe)
            if ok:
                return probe, "common_path_probe", 0.66

    # Last fallback: inspect a small number of result pages for direct links.
    for cand in candidates[:2]:
        try:
            body, _ = _fetch_text(cand, timeout=6)
        except Exception:
            continue
        links = extract_candidate_links(body, cand)
        if links:
            return links[0], "page_link", 0.78

    return None, None, 0.0


def discover_missing_hospital_urls(
    limit: int | None = None,
    sleep_seconds: float = 0.25,
    max_workers: int = 6,
) -> dict[str, int]:
    limit_sql = "LIMIT ?" if limit else ""
    params: tuple[object, ...] = (limit,) if limit else ()

    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT h.facility_id, h.name, h.city, h.state, tf.file_url, tf.parse_status
            FROM hospitals h
            LEFT JOIN transparency_files tf ON tf.facility_id = h.facility_id
            WHERE tf.facility_id IS NULL
               OR tf.file_url IS NULL
               OR tf.file_url = ''
               OR tf.parse_status IN ('not_found', 'failed')
            ORDER BY COALESCE(h.bed_count, 0) DESC, h.name
            {limit_sql}
            """,
            params,
        ).fetchall()

        scanned = len(rows)
        discovered = 0
        futures = {}
        with ThreadPoolExecutor(max_workers=max(1, max_workers)) as pool:
            for row in rows:
                futures[
                    pool.submit(
                        discover_transparency_url_for_row,
                        dict(row),
                    )
                ] = row

            for future in as_completed(futures):
                row = futures[future]
                try:
                    url, method, confidence = future.result()
                except Exception:
                    url, method, confidence = None, None, 0.0
                if url:
                    db.execute(
                        """
                        INSERT INTO transparency_files (
                            facility_id, file_url, parse_status, parse_notes, last_downloaded
                        ) VALUES (?, ?, 'pending', ?, CURRENT_DATE)
                        ON CONFLICT(facility_id) DO UPDATE SET
                            file_url=excluded.file_url,
                            parse_status=CASE
                                WHEN transparency_files.parse_status IN ('parsed', 'partial') THEN transparency_files.parse_status
                                ELSE 'pending'
                            END,
                            parse_notes=excluded.parse_notes,
                            last_downloaded=CURRENT_DATE
                        """,
                        (
                            row["facility_id"],
                            url,
                            f"Discovered via site search ({method}, confidence={confidence:.2f})",
                        ),
                    )
                    discovered += 1
                    if sleep_seconds > 0:
                        time.sleep(sleep_seconds)

    return {"scanned": scanned, "discovered": discovered}


def discover_transparency_url_for_row(row: dict) -> tuple[str | None, str | None, float]:
    existing_url = row.get("file_url")
    existing_status = (row.get("parse_status") or "").strip().lower()
    if existing_url and existing_status in {"not_found", "failed"}:
        url, method, confidence = probe_existing_domain(existing_url)
        if url:
            return url, method, confidence
    return discover_transparency_url(row["name"], row["city"], row["state"])


def select_newly_discovered_hospitals(limit: int | None = None) -> list[dict]:
    limit_sql = "LIMIT ?" if limit else ""
    params: tuple[object, ...] = (limit,) if limit else ()
    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT h.facility_id, h.slug
            FROM hospitals h
            JOIN transparency_files tf ON tf.facility_id = h.facility_id
            WHERE tf.parse_status = 'pending'
              AND tf.parse_notes LIKE 'Discovered via%'
            ORDER BY COALESCE(h.bed_count, 0) DESC, h.name
            {limit_sql}
            """,
            params,
        ).fetchall()
    return [{"facility_id": r["facility_id"], "facility_type": "hospital", "slug": r["slug"]} for r in rows]
