"""Read California hospitals' charity care policies from HCAI. A policy whose file hasn't changed is skipped."""

import logging
import threading
import time

import assistance_policies
import config
import hcai_policies
from db import get_db

log = logging.getLogger(__name__)


def refresh_one(hospital: dict) -> str:
    """Returns what happened: new, unchanged, or why it was skipped."""
    if not hospital["charity_policy"]:
        return "skipped: no charity care policy on the page"
    url, effective = hospital["charity_policy"]
    try:
        sha256, text = assistance_policies.fetch_policy(url)
        if hospital["discount_policy"] and hospital["discount_policy"][0] != url:
            sha2, text2 = assistance_policies.fetch_policy(hospital["discount_policy"][0])
            sha256, text = sha256 + sha2, text + "\n\n" + text2
    except Exception as exc:
        return f"skipped: could not read the policy file ({exc})"
    if len(text.strip()) < 200:
        return "skipped: the file has no readable text (scanned image)"
    if assistance_policies.latest_hash(hospital["license"]) == sha256:
        return "unchanged"
    hospital["facility_id"] = assistance_policies.match_facility_id(hospital["name"], hospital["zip"], hospital["city"])
    terms, evidence = assistance_policies.extract_policy_terms(text)
    terms = assistance_policies.apply_legal_floors(terms, evidence)
    assistance_policies.save_policy(hospital, url, sha256, effective, terms, evidence)
    return f"new: {len(terms)} terms with quotes"


def run(cities: list[str], limit: int = 0) -> int:
    """Refresh the hospitals in these cities (all of California when empty). Returns how many were looked at."""
    done = 0
    wanted = {city.lower() for city in cities}
    for url in hcai_policies.hospital_page_urls():
        hospital = hcai_policies.fetch_hospital(url)
        time.sleep(config.POLICY_FETCH_DELAY_SECONDS)
        if wanted and (hospital["city"] or "").lower() not in wanted:
            continue
        log.info("%s (%s): %s", hospital["name"], hospital["city"], refresh_one(hospital))
        done += 1
        if limit and done >= limit:
            break
    with get_db() as db:
        db.execute("INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, 'ok', ?)",
                   ("hcai_assistance_policies", done, f"cities={cities}"))
    return done


def start_first_read_if_needed() -> None:
    """In production, read the first batch of policies in the background once, when none are stored and Gemini is set up."""
    if config.ENV != "production" or not config.ASSISTANCE_POLICY_AUTO_REFRESH or not config.GEMINI_API_KEY:
        return
    if assistance_policies.policies_exist():
        return

    def work():
        try:
            run(list(config.ASSISTANCE_POLICY_AUTO_CITIES), config.ASSISTANCE_POLICY_AUTO_LIMIT)
        except Exception:
            log.exception("First read of charity care policies failed")

    threading.Thread(target=work, daemon=True, name="policy-first-read").start()
