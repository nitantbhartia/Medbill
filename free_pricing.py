"""Free-data benchmark engine for hospital fair-price estimates.

Builds percentile bands from:
- Hospital MRF-derived rates in `hospital_prices`
- User bill observations in `line_items`

No paid API sources required.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

from db import get_db
from hospital_etl import TARGET_PROCEDURES


DEFAULT_METHOD = "no_api_v1"


@dataclass
class RefreshSummary:
    inserted_mrf: int = 0
    inserted_user_bills: int = 0
    total_observations: int = 0


@dataclass
class BandSummary:
    inserted_rows: int = 0
    zip_rows: int = 0
    city_rows: int = 0
    state_rows: int = 0
    national_rows: int = 0


def _zip5(value: str | None) -> str | None:
    if not value:
        return None
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return digits[:5] if len(digits) >= 5 else None


def _norm_code(code: str | None) -> str | None:
    if not code:
        return None
    txt = str(code).strip().upper()
    return txt if len(txt) == 5 else None


def _pct(sorted_vals: list[float], q: float) -> float | None:
    if not sorted_vals:
        return None
    if len(sorted_vals) == 1:
        return float(sorted_vals[0])
    pos = (len(sorted_vals) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(sorted_vals) - 1)
    frac = pos - lo
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * frac


def load_target_codes(path: str | None = None, limit: int | None = 50) -> set[str]:
    """Load scoped shoppable CPT/HCPCS set.

    Order of precedence:
    1) Caller file (txt/csv, first token each line)
    2) data/config/shoppable_codes_top50.txt
    3) TARGET_PROCEDURES fallback from hospital_etl
    """
    candidate_paths: list[Path] = []
    if path:
        candidate_paths.append(Path(path))
    candidate_paths.append(Path("data/config/shoppable_codes_top50.txt"))

    for p in candidate_paths:
        if p.exists():
            codes: list[str] = []
            for raw in p.read_text(encoding="utf-8").splitlines():
                txt = raw.strip()
                if not txt or txt.startswith("#"):
                    continue
                code = _norm_code(txt.split(",")[0])
                if code:
                    codes.append(code)
            if codes:
                deduped = list(dict.fromkeys(codes))
                return set(deduped[:limit] if limit else deduped)

    fallback = sorted(TARGET_PROCEDURES)
    return set(fallback[:limit] if limit else fallback)


def _lookup_zip_city_state_map() -> dict[str, tuple[str | None, str | None]]:
    with get_db() as db:
        rows = db.execute("SELECT zip, city, state FROM zip_latlon").fetchall()
    out: dict[str, tuple[str | None, str | None]] = {}
    for r in rows:
        z = _zip5(r["zip"])
        if z and z not in out:
            city = str(r["city"]).strip().upper() if r["city"] else None
            state = str(r["state"]).strip().upper() if r["state"] else None
            out[z] = (city, state)
    return out


def refresh_price_observations(
    *,
    codes: set[str],
    data_year: int | None = None,
    include_user_bills: bool = True,
) -> RefreshSummary:
    """Rebuild canonical observations from free sources."""
    summary = RefreshSummary()
    zip_map = _lookup_zip_city_state_map()
    today_year = date.today().year

    with get_db() as db:
        placeholders = ",".join("?" * len(codes))
        params: list[object] = list(sorted(codes))

        q = f"""
            SELECT hp.id, hp.facility_id, hp.cpt_code, hp.gross_charge, hp.cash_price,
                   hp.avg_negotiated_rate, hp.medicare_rate, hp.data_year,
                   h.zip, h.city, h.state
            FROM hospital_prices hp
            LEFT JOIN hospitals h ON h.facility_id = hp.facility_id
            WHERE hp.cpt_code IN ({placeholders})
        """
        if data_year is not None:
            q += " AND hp.data_year = ?"
            params.append(data_year)

        for row in db.execute(q, params).fetchall():
            code = _norm_code(row["cpt_code"])
            if not code:
                continue
            avg_neg = row["avg_negotiated_rate"]
            cash = row["cash_price"]
            gross = row["gross_charge"]
            allowed = avg_neg if avg_neg is not None else cash
            if allowed is None and gross is None:
                continue

            zip5 = _zip5(row["zip"])
            city = str(row["city"]).strip().upper() if row["city"] else None
            state = str(row["state"]).strip().upper() if row["state"] else None
            if zip5 and (not city or not state):
                z_city, z_state = zip_map.get(zip5, (None, None))
                city = city or z_city
                state = state or z_state

            confidence = 0.82 if avg_neg is not None else (0.62 if cash is not None else 0.40)
            year = int(row["data_year"] or data_year or today_year)

            db.execute(
                """
                INSERT INTO price_observations (
                    source_type, source_ref, code_type, code, facility_id,
                    geo_zip5, geo_city, geo_state,
                    billed_amount, allowed_amount, cash_price, gross_charge, medicare_rate,
                    effective_year, confidence
                ) VALUES (?, ?, 'CPT', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_type, source_ref) DO UPDATE SET
                    code=excluded.code,
                    facility_id=excluded.facility_id,
                    geo_zip5=excluded.geo_zip5,
                    geo_city=excluded.geo_city,
                    geo_state=excluded.geo_state,
                    billed_amount=excluded.billed_amount,
                    allowed_amount=excluded.allowed_amount,
                    cash_price=excluded.cash_price,
                    gross_charge=excluded.gross_charge,
                    medicare_rate=excluded.medicare_rate,
                    effective_year=excluded.effective_year,
                    confidence=excluded.confidence
                """,
                (
                    "mrf",
                    f"hp:{row['id']}",
                    code,
                    row["facility_id"],
                    zip5,
                    city,
                    state,
                    gross,
                    allowed,
                    cash,
                    gross,
                    row["medicare_rate"],
                    year,
                    confidence,
                ),
            )
            summary.inserted_mrf += 1

        if include_user_bills:
            bill_rows = db.execute(
                f"""
                SELECT li.id, li.cpt_code, li.charged_amount, li.insurance_paid, li.insurance_adjustment,
                       li.patient_responsibility, b.zip_code, b.bill_date
                FROM line_items li
                JOIN bills b ON b.id = li.bill_id
                WHERE li.cpt_code IN ({placeholders})
                """,
                tuple(sorted(codes)),
            ).fetchall()

            for row in bill_rows:
                code = _norm_code(row["cpt_code"])
                if not code:
                    continue

                charged = row["charged_amount"]
                insurance_paid = row["insurance_paid"]
                insurance_adj = row["insurance_adjustment"]
                patient_resp = row["patient_responsibility"]

                allowed: float | None = None
                confidence = 0.55

                if insurance_paid is not None and patient_resp is not None:
                    allowed = float(insurance_paid) + float(patient_resp)
                    confidence = 0.93
                elif insurance_paid is not None and insurance_adj is not None:
                    allowed = float(insurance_paid) + max(float(insurance_adj), 0.0)
                    confidence = 0.86
                elif charged is not None and insurance_adj is not None:
                    allowed = max(float(charged) - max(float(insurance_adj), 0.0), 0.0)
                    confidence = 0.72
                elif patient_resp is not None:
                    allowed = float(patient_resp)
                    confidence = 0.60

                if allowed is not None and allowed <= 0:
                    allowed = None

                zip5 = _zip5(row["zip_code"])
                city = None
                state = None
                if zip5 and zip5 in zip_map:
                    city, state = zip_map[zip5]

                event_year = today_year
                if row["bill_date"]:
                    txt = str(row["bill_date"])[:4]
                    if txt.isdigit():
                        event_year = int(txt)

                db.execute(
                    """
                    INSERT INTO price_observations (
                        source_type, source_ref, code_type, code, geo_zip5, geo_city, geo_state,
                        billed_amount, allowed_amount, event_date, effective_year, confidence
                    ) VALUES (?, ?, 'CPT', ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(source_type, source_ref) DO UPDATE SET
                        code=excluded.code,
                        geo_zip5=excluded.geo_zip5,
                        geo_city=excluded.geo_city,
                        geo_state=excluded.geo_state,
                        billed_amount=excluded.billed_amount,
                        allowed_amount=excluded.allowed_amount,
                        event_date=excluded.event_date,
                        effective_year=excluded.effective_year,
                        confidence=excluded.confidence
                    """,
                    (
                        "user_bill",
                        f"line_item:{row['id']}",
                        code,
                        zip5,
                        city,
                        state,
                        charged,
                        allowed,
                        row["bill_date"],
                        event_year,
                        confidence,
                    ),
                )
                summary.inserted_user_bills += 1

        summary.total_observations = db.execute(
            "SELECT COUNT(*) AS n FROM price_observations WHERE code IN ({})".format(placeholders),
            tuple(sorted(codes)),
        ).fetchone()["n"]

    return summary


def recompute_fair_price_bands(
    *,
    codes: set[str],
    method: str = DEFAULT_METHOD,
    min_sample_zip: int = 8,
    min_sample_city: int = 12,
    min_sample_state: int = 20,
    min_sample_national: int = 40,
) -> BandSummary:
    thresholds = {
        "zip": min_sample_zip,
        "city": min_sample_city,
        "state": min_sample_state,
        "national": min_sample_national,
    }
    summary = BandSummary()

    placeholders = ",".join("?" * len(codes))
    with get_db() as db:
        db.execute("DELETE FROM fair_price_bands WHERE method = ?", (method,))
        rows = db.execute(
            f"""
            SELECT code, geo_zip5, geo_city, geo_state, allowed_amount, confidence
            FROM price_observations
            WHERE code IN ({placeholders})
              AND allowed_amount IS NOT NULL
              AND allowed_amount > 0
              AND allowed_amount < 1000000
            """,
            tuple(sorted(codes)),
        ).fetchall()

        grouped: dict[tuple[str, str, str], list[tuple[float, float]]] = defaultdict(list)
        for r in rows:
            code = _norm_code(r["code"])
            if not code:
                continue
            amount = float(r["allowed_amount"])
            conf = float(r["confidence"] if r["confidence"] is not None else 0.5)

            grouped[("national", "US", code)].append((amount, conf))

            if r["geo_state"]:
                state = str(r["geo_state"]).strip().upper()
                grouped[("state", state, code)].append((amount, conf))

            if r["geo_city"] and r["geo_state"]:
                city_key = f"{str(r['geo_city']).strip().upper()}|{str(r['geo_state']).strip().upper()}"
                grouped[("city", city_key, code)].append((amount, conf))

            if r["geo_zip5"]:
                zip5 = _zip5(r["geo_zip5"])
                if zip5:
                    grouped[("zip", zip5, code)].append((amount, conf))

        for (scope, geo_value, code), vals in grouped.items():
            n = len(vals)
            if n < thresholds[scope]:
                continue
            amounts = sorted(v[0] for v in vals)
            conf_mean = sum(v[1] for v in vals) / n if n else None

            db.execute(
                """
                INSERT INTO fair_price_bands (
                    geo_scope, geo_value, code_type, code, sample_size,
                    p25, p50, p75, p90, confidence_mean, method, updated_at
                ) VALUES (?, ?, 'CPT', ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (
                    scope,
                    geo_value,
                    code,
                    n,
                    _pct(amounts, 0.25),
                    _pct(amounts, 0.50),
                    _pct(amounts, 0.75),
                    _pct(amounts, 0.90),
                    conf_mean,
                    method,
                ),
            )
            summary.inserted_rows += 1
            if scope == "zip":
                summary.zip_rows += 1
            elif scope == "city":
                summary.city_rows += 1
            elif scope == "state":
                summary.state_rows += 1
            elif scope == "national":
                summary.national_rows += 1

    return summary


def resolve_fair_price(
    code: str,
    *,
    zip_code: str | None = None,
    city: str | None = None,
    state: str | None = None,
    method: str = DEFAULT_METHOD,
) -> dict | None:
    """Resolve best available band with ZIP->CITY->STATE->NATIONAL fallback."""
    norm_code = _norm_code(code)
    if not norm_code:
        return None

    zip5 = _zip5(zip_code)
    city_key = None
    if city and state:
        city_key = f"{city.strip().upper()}|{state.strip().upper()}"
    st = state.strip().upper() if state else None

    candidates: list[tuple[str, str]] = []
    if zip5:
        candidates.append(("zip", zip5))
    if city_key:
        candidates.append(("city", city_key))
    if st:
        candidates.append(("state", st))
    candidates.append(("national", "US"))

    with get_db() as db:
        for scope, value in candidates:
            row = db.execute(
                """
                SELECT geo_scope, geo_value, code, sample_size, p25, p50, p75, p90, confidence_mean, method
                FROM fair_price_bands
                WHERE geo_scope = ? AND geo_value = ? AND code = ? AND method = ?
                LIMIT 1
                """,
                (scope, value, norm_code, method),
            ).fetchone()
            if row:
                return dict(row)

    return None


def summarize_scope_coverage(codes: Iterable[str], method: str = DEFAULT_METHOD) -> dict[str, int]:
    code_list = [c for c in codes]
    if not code_list:
        return {"zip": 0, "city": 0, "state": 0, "national": 0}
    placeholders = ",".join("?" * len(code_list))
    with get_db() as db:
        rows = db.execute(
            f"""
            SELECT geo_scope, COUNT(*) AS n
            FROM fair_price_bands
            WHERE method = ?
              AND code IN ({placeholders})
            GROUP BY geo_scope
            """,
            (method, *code_list),
        ).fetchall()
    out = {"zip": 0, "city": 0, "state": 0, "national": 0}
    for r in rows:
        out[str(r["geo_scope"])] = int(r["n"])
    return out
