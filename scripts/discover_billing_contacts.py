"""Collect each hospital's billing office contact from the hospital's own website.

Domains come from URLs already stored in the database (financial assistance and
price transparency file links). Extraction rules live in billing_contacts.py.

Examples:
python scripts/discover_billing_contacts.py --dry-run --limit 5
python scripts/discover_billing_contacts.py --state TX --limit 200
python scripts/discover_billing_contacts.py --facility-id 010001
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass
from http.client import HTTPException
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import config  # noqa: E402
import db  # noqa: E402
from billing_contacts import (  # noqa: E402
    BillingContact,
    candidate_urls,
    extract_contact,
    homepage_names_hospital,
    parse_page,
    root_from_stored_urls,
)

log = logging.getLogger("billing_contacts")


@dataclass
class Hospital:
    facility_id: str
    name: str
    root: str


class PoliteFetcher:
    """Fetches pages with a shared rate limit, robots.txt checks and a per-host failure cut-off."""

    def __init__(self) -> None:
        self._last_request = 0.0
        self._failures: Counter[str] = Counter()
        self._robots: dict[str, RobotFileParser] = {}

    def get_page(self, url: str) -> str | None:
        host = urlparse(url).netloc
        if self._failures[host] >= config.BILLING_CONTACT_MAX_HOST_FAILURES:
            return None
        if not self._allowed_by_robots(url):
            log.info("skip %s: disallowed by robots.txt", url)
            return None
        return self._request(url)

    def _allowed_by_robots(self, url: str) -> bool:
        parsed = urlparse(url)
        if parsed.netloc not in self._robots:
            self._robots[parsed.netloc] = self._load_robots(f"{parsed.scheme}://{parsed.netloc}")
        return self._robots[parsed.netloc].can_fetch(config.BILLING_CONTACT_USER_AGENT, url)

    def _load_robots(self, root: str) -> RobotFileParser:
        parser = RobotFileParser()
        body = self._request(f"{root}/robots.txt") or ""
        parser.parse(body.splitlines())
        return parser

    def _request(self, url: str) -> str | None:
        self._wait_for_slot()
        request = Request(url, headers={"User-Agent": config.BILLING_CONTACT_USER_AGENT})
        try:
            with urlopen(request, timeout=config.BILLING_CONTACT_TIMEOUT_SECONDS) as response:
                if response.headers.get_content_maintype() != "text":
                    return None
                return response.read().decode("utf-8", "ignore")
        except HTTPError as exc:
            if exc.code >= 500:
                self._record_failure(url, exc)
            else:
                log.info("skip %s: HTTP %s", url, exc.code)
            return None
        except (OSError, HTTPException) as exc:
            self._record_failure(url, exc)
            return None

    def _record_failure(self, url: str, exc: Exception) -> None:
        self._failures[urlparse(url).netloc] += 1
        log.warning("fetch failed %s: %s", url, exc)

    def _wait_for_slot(self) -> None:
        wait = config.BILLING_CONTACT_MIN_INTERVAL_SECONDS - (time.monotonic() - self._last_request)
        if wait > 0:
            time.sleep(wait)
        self._last_request = time.monotonic()


def find_contact(hospital: Hospital, fetcher: PoliteFetcher) -> BillingContact | None:
    home_html = fetcher.get_page(hospital.root)
    if home_html is None:
        return None
    home = parse_page(home_html)
    if not homepage_names_hospital(home, hospital.name):
        log.info("skip %s: homepage does not mention the hospital name", hospital.root)
        return None
    contacts = []
    for url in candidate_urls(hospital.root, home)[: config.BILLING_CONTACT_MAX_PAGES - 1]:
        page_html = fetcher.get_page(url)
        if page_html is None:
            continue
        contact = extract_contact(parse_page(page_html), url)
        if contact.has_data():
            contacts.append(contact)
    with_phone = [c for c in contacts if c.billing_phone]
    if with_phone:
        return with_phone[0]
    return contacts[0] if contacts else None


def load_hospitals(state: str | None, facility_id: str | None, limit: int | None) -> list[Hospital]:
    with db.get_db() as conn:
        rows = conn.execute(
            """
            SELECT hd.facility_id, hd.name, hf.financial_assistance_url, tf.file_url
            FROM hospital_directory hd
            LEFT JOIN hospital_financials hf ON hf.facility_id = hd.facility_id
            LEFT JOIN transparency_files tf ON tf.facility_id = hd.facility_id
            WHERE (? IS NULL OR hd.state = ?) AND (? IS NULL OR hd.facility_id = ?)
            ORDER BY COALESCE(hd.bed_count, 0) DESC, hd.name
            """,
            (state, state, facility_id, facility_id),
        ).fetchall()
    hospitals = []
    for row in rows:
        if limit is not None and len(hospitals) >= limit:
            break
        root = root_from_stored_urls([row["financial_assistance_url"], row["file_url"]])
        if root:
            hospitals.append(Hospital(row["facility_id"], row["name"], root))
    return hospitals


UPSERT_SQL = """
INSERT INTO hospital_billing_contacts (
    facility_id, billing_phone, billing_address, financial_assistance_url, payment_url, source_url
) VALUES (?, ?, ?, ?, ?, ?)
ON CONFLICT(facility_id) DO UPDATE SET
    billing_phone=excluded.billing_phone,
    billing_address=excluded.billing_address,
    financial_assistance_url=excluded.financial_assistance_url,
    payment_url=excluded.payment_url,
    source_url=excluded.source_url,
    fetched_at=CURRENT_TIMESTAMP
"""


def save_contact(facility_id: str, contact: BillingContact) -> None:
    with db.get_db() as conn:
        conn.execute(
            UPSERT_SQL,
            (
                facility_id,
                contact.billing_phone,
                contact.billing_address,
                contact.financial_assistance_url,
                contact.payment_url,
                contact.source_url,
            ),
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect hospital billing contacts from hospital websites")
    parser.add_argument("--limit", type=int, default=None, help="Stop after this many hospitals with a known domain")
    parser.add_argument("--state", type=str.upper, default=None, help="Two-letter state code, e.g. TX")
    parser.add_argument("--facility-id", default=None, help="Only this hospital")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be saved; write nothing")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    if not args.dry_run:
        db.init_db()
    hospitals = load_hospitals(args.state, args.facility_id, args.limit)
    log.info("%d hospitals have a known website domain", len(hospitals))
    fetcher = PoliteFetcher()
    summary = Counter()
    for number, hospital in enumerate(hospitals, start=1):
        log.info("[%d/%d] %s %s", number, len(hospitals), hospital.facility_id, hospital.root)
        summary["tried"] += 1
        contact = find_contact(hospital, fetcher)
        if contact is None:
            log.info("no billing contact found")
            continue
        summary["phones"] += bool(contact.billing_phone)
        summary["addresses"] += bool(contact.billing_address)
        summary["rows"] += 1
        if args.dry_run:
            print(f"{hospital.facility_id} {hospital.name}: {json.dumps(asdict(contact))}")
        else:
            save_contact(hospital.facility_id, contact)
    verb = "would save" if args.dry_run else "saved"
    print(
        f"hospitals tried={summary['tried']} rows {verb}={summary['rows']} "
        f"phones found={summary['phones']} addresses found={summary['addresses']}"
    )


if __name__ == "__main__":
    main()
