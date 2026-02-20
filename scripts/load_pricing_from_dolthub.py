"""Load hospital pricing from DoltHub hospital-price-transparency dataset.

This is a fallback ingestion path when CMS transparency-index access is unavailable.
It maps hospitals by normalized name/city/state and ingests target CPT/HCPCS rows.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import config
import db
from hospital_etl import TARGET_PROCEDURES, parse_float, upsert_hospital_price
from hospital_seo import log_refresh


API_BASE = "https://www.dolthub.com/api/v1alpha1/dolthub/hospital-price-transparency/master"


def api_query(sql: str, retries: int = 3) -> list[dict]:
    params = urllib.parse.urlencode({"q": sql})
    url = f"{API_BASE}?{params}"
    last_err: Exception | None = None
    for _ in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=90) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            return payload.get("rows", [])
        except Exception as err:  # pragma: no cover - network variance
            last_err = err
            time.sleep(1)
    if last_err:
        raise last_err
    return []


def norm_name(value: str | None) -> str:
    txt = (value or "").lower()
    txt = txt.replace("&", " and ")
    txt = re.sub(r"[^a-z0-9 ]+", " ", txt)
    words = txt.split()
    stopwords = {
        "the",
        "hospital",
        "medical",
        "center",
        "centre",
        "health",
        "system",
        "inc",
        "llc",
        "corp",
        "corporation",
        "co",
        "company",
    }
    words = [w for w in words if w not in stopwords]
    return " ".join(words)


def norm_city(value: str | None) -> str:
    txt = (value or "").lower()
    txt = re.sub(r"[^a-z0-9 ]+", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def load_dolthub_hospitals() -> list[dict]:
    rows: list[dict] = []
    offset = 0
    page = 500
    while True:
        batch = api_query(
            f"SELECT npi_number, name, city, state, url, publish_date FROM hospitals LIMIT {page} OFFSET {offset}"
        )
        if not batch:
            break
        rows.extend(batch)
        offset += page
        if len(batch) < page:
            break
    return rows


def match_hospitals(limit: int) -> tuple[dict[str, dict], list[dict]]:
    with sqlite3.connect(config.DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        ours = conn.execute(
            """
            SELECT facility_id, name, city, state
            FROM hospitals
            ORDER BY COALESCE(bed_count, 0) DESC, name
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    ours = [dict(r) for r in ours]
    dolt = load_dolthub_hospitals()

    by_exact: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    by_name_state: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in dolt:
        key_exact = (norm_name(row.get("name")), norm_city(row.get("city")), (row.get("state") or "").upper())
        key_name_state = (norm_name(row.get("name")), (row.get("state") or "").upper())
        by_exact[key_exact].append(row)
        by_name_state[key_name_state].append(row)

    facility_matches: dict[str, dict] = {}
    for h in ours:
        key_exact = (norm_name(h.get("name")), norm_city(h.get("city")), (h.get("state") or "").upper())
        cands = by_exact.get(key_exact, [])
        if len(cands) == 1:
            facility_matches[h["facility_id"]] = {
                "npi": cands[0]["npi_number"],
                "method": "exact_name_city_state",
                "confidence": 1.0,
            }
            continue

        key_name_state = (norm_name(h.get("name")), (h.get("state") or "").upper())
        cands = by_name_state.get(key_name_state, [])
        if len(cands) == 1:
            facility_matches[h["facility_id"]] = {
                "npi": cands[0]["npi_number"],
                "method": "name_state_single_candidate",
                "confidence": 0.7,
            }

    return facility_matches, dolt


def _chunks(values: list[str], size: int) -> list[list[str]]:
    return [values[i : i + size] for i in range(0, len(values), size)]


def load_prices_for_matches(facility_matches: dict[str, dict], year: int) -> dict[str, int]:
    npi_to_facility = {m["npi"]: fid for fid, m in facility_matches.items()}
    npis = list(npi_to_facility.keys())
    if not npis:
        return {"rows": 0, "facilities": 0}

    code_list = sorted(TARGET_PROCEDURES)
    code_sql = ",".join(f"'{c}'" for c in code_list)
    total_rows = 0
    facility_hits: set[str] = set()

    with sqlite3.connect(config.DB_PATH) as conn:
        for npi_batch in _chunks(npis, 30):
            npi_sql = ",".join(f"'{n}'" for n in npi_batch)
            rows = api_query(
                "SELECT npi_number, code, payer, price "
                f"FROM prices WHERE npi_number IN ({npi_sql}) AND code IN ({code_sql})"
            )
            grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
            for row in rows:
                grouped[(row["npi_number"], row["code"])].append(row)

            for (npi, code), items in grouped.items():
                facility_id = npi_to_facility.get(npi)
                if not facility_id:
                    continue

                gross_candidates = []
                cash_candidates = []
                negotiated = []
                for item in items:
                    payer = (item.get("payer") or "").lower()
                    price = parse_float(item.get("price"))
                    if price is None:
                        continue
                    if any(k in payer for k in ("gross", "standard", "list", "charge")):
                        gross_candidates.append(price)
                    elif any(k in payer for k in ("cash", "self", "uninsured")):
                        cash_candidates.append(price)
                    else:
                        negotiated.append(price)

                if not gross_candidates and (negotiated or cash_candidates):
                    gross_candidates = negotiated[:] or cash_candidates[:]

                gross = max(gross_candidates) if gross_candidates else None
                cash = min(cash_candidates) if cash_candidates else None
                if negotiated:
                    avg_neg = sum(negotiated) / len(negotiated)
                    min_neg = min(negotiated)
                    max_neg = max(negotiated)
                else:
                    avg_neg = min_neg = max_neg = None

                if gross is None and avg_neg is None:
                    continue

                upsert_hospital_price(
                    facility_id,
                    {
                        "cpt_code": code,
                        "description": None,
                        "gross_charge": gross,
                        "cash_price": cash,
                        "avg_negotiated_rate": avg_neg,
                        "min_negotiated_rate": min_neg,
                        "max_negotiated_rate": max_neg,
                    },
                    data_year=year,
                )
                facility_hits.add(facility_id)
                total_rows += 1

        for facility_id, match in facility_matches.items():
            npi = match["npi"]
            parsed = facility_id in facility_hits
            conn.execute(
                """
                INSERT INTO transparency_files (
                    facility_id, file_url, file_format, parse_status, parse_notes,
                    procedures_extracted, row_count, last_parsed
                ) VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_DATE)
                ON CONFLICT(facility_id) DO UPDATE SET
                    file_url=excluded.file_url,
                    file_format='api',
                    parse_status=excluded.parse_status,
                    parse_notes=excluded.parse_notes,
                    procedures_extracted=excluded.procedures_extracted,
                    row_count=excluded.row_count,
                    last_parsed=CURRENT_DATE
                """,
                (
                    facility_id,
                    f"https://www.dolthub.com/repositories/dolthub/hospital-price-transparency?q=npi_number%3A{npi}",
                    "api",
                    "parsed" if parsed else "partial",
                    "Loaded via DoltHub fallback",
                    1 if parsed else 0,
                    1 if parsed else 0,
                ),
            )
            conn.execute(
                """
                INSERT INTO data_source_crosswalk (
                    source_name, source_entity_id, facility_id,
                    match_method, match_confidence, last_verified_at
                ) VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(source_name, source_entity_id) DO UPDATE SET
                    facility_id=excluded.facility_id,
                    match_method=excluded.match_method,
                    match_confidence=excluded.match_confidence,
                    last_verified_at=CURRENT_TIMESTAMP
                """,
                (
                    "dolthub_hospital_price_transparency",
                    npi,
                    facility_id,
                    match.get("method"),
                    match.get("confidence"),
                ),
            )
        conn.commit()

    return {"rows": total_rows, "facilities": len(facility_hits)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Load pricing from DoltHub fallback source")
    parser.add_argument("--limit", type=int, default=300, help="Top hospitals to match by bed-count ordering")
    parser.add_argument("--year", type=int, default=2026, help="Data year for hospital_prices rows")
    args = parser.parse_args()

    db.init_db()
    facility_matches, _ = match_hospitals(limit=args.limit)
    loaded = load_prices_for_matches(facility_matches, year=args.year)
    log_refresh(
        "dolthub_pricing",
        loaded["rows"],
        "success" if loaded["rows"] else "partial",
        f"matched_facilities={len(facility_matches)} loaded_facilities={loaded['facilities']}",
    )
    print(
        {
            "matched_facilities": len(facility_matches),
            "loaded_facilities": loaded["facilities"],
            "rows_loaded": loaded["rows"],
        }
    )


if __name__ == "__main__":
    main()
