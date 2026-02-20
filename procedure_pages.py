"""Procedure cost page helpers — data queries and deterministic content generation."""

from __future__ import annotations

import math

from db import get_db

_PROCEDURE_RADIUS_MILES = 75.0
_EARTH_RADIUS_MILES = 3958.8

# Friendly consumer names for common CPT codes
_FRIENDLY_NAMES: dict[str, str] = {
    "10060": "Abscess Drainage",
    "11042": "Wound Debridement",
    "20610": "Joint Injection",
    "22551": "Cervical Spine Fusion",
    "23472": "Shoulder Replacement",
    "27130": "Total Hip Replacement",
    "27236": "Hip Fracture Repair",
    "27447": "Total Knee Replacement",
    "29881": "Knee Arthroscopy",
    "43239": "Upper GI Endoscopy with Biopsy",
    "45378": "Colonoscopy",
    "70450": "Head CT Scan",
    "70553": "Brain MRI with Contrast",
    "71045": "Chest X-Ray",
    "71250": "Chest CT Scan",
    "73221": "Wrist MRI",
    "73223": "Shoulder MRI",
    "73721": "Knee MRI",
    "74178": "Abdominal CT Scan",
    "74177": "Abdominal CT with Contrast",
    "74183": "Abdominal MRI with Contrast",
    "76700": "Abdominal Ultrasound",
    "76805": "Obstetric Ultrasound",
    "80053": "Comprehensive Metabolic Panel",
    "80061": "Lipid Panel",
    "85025": "Complete Blood Count",
    "93000": "Electrocardiogram (ECG)",
}

_GRADE_COLORS = {
    "A": "#22c55e", "B": "#84cc16", "C": "#f59e0b", "D": "#f97316", "F": "#ef4444",
}
_GRADE_BADGE_CLASSES = {
    "A": "bg-green-100 text-green-700",
    "B": "bg-lime-100 text-lime-700",
    "C": "bg-yellow-100 text-yellow-700",
    "D": "bg-orange-100 text-orange-700",
    "F": "bg-red-100 text-red-700",
}
_BODY_SYSTEMS: list[tuple[int, int, str]] = [
    (10000, 19999, "Skin & Soft Tissue"),
    (20000, 29999, "Musculoskeletal"),
    (30000, 39999, "Respiratory"),
    (40000, 49999, "Digestive"),
    (50000, 59999, "Urinary"),
    (60000, 69999, "Endocrine & Nervous"),
    (70000, 79999, "Radiology & Imaging"),
    (80000, 89999, "Laboratory"),
    (90000, 99999, "Medicine"),
]


def _body_system(cpt_code: str) -> str:
    try:
        n = int(cpt_code)
    except (ValueError, TypeError):
        return "Other"
    for lo, hi, name in _BODY_SYSTEMS:
        if lo <= n <= hi:
            return name
    return "Other"


def _classify_cpt(cpt_code: str) -> str:
    """Return 'imaging', 'surgical', or 'outpatient'."""
    try:
        n = int(cpt_code)
    except (ValueError, TypeError):
        return "outpatient"
    if 70000 <= n <= 79999:
        return "imaging"
    if 10000 <= n <= 69999:
        return "surgical"
    return "outpatient"


def _friendly_name(cpt_code: str, raw_description: str) -> str:
    if cpt_code in _FRIENDLY_NAMES:
        return _FRIENDLY_NAMES[cpt_code]
    desc = (raw_description or "").strip()
    if not desc:
        return f"CPT {cpt_code}"
    # Truncate to 60 chars at word boundary
    if len(desc) <= 60:
        return desc.title()
    return desc[:57].rsplit(" ", 1)[0].title() + "..."


def _procedure_description(name: str, cpt_code: str, procedure_type: str) -> str:
    if procedure_type == "imaging":
        return (
            f"{name} (CPT {cpt_code}) is a diagnostic imaging scan that gives physicians "
            f"detailed views of internal structures without surgery. It is typically ordered "
            f"to evaluate an injury, disease, or condition that cannot be fully assessed through "
            f"a physical exam alone. The scan usually takes 15 to 60 minutes to complete."
        )
    if procedure_type == "surgical":
        return (
            f"{name} (CPT {cpt_code}) is a surgical procedure typically performed in a hospital "
            f"or accredited outpatient surgical center. It is usually recommended after more "
            f"conservative treatments—such as medication or physical therapy—have not resolved "
            f"the underlying problem. Recovery time ranges from a few days to several weeks "
            f"depending on patient health and procedure complexity."
        )
    return (
        f"{name} (CPT {cpt_code}) is an outpatient procedure or diagnostic test performed in "
        f"a hospital, clinic, or ambulatory care setting. It is typically completed in a single "
        f"visit, and most patients return to normal activities the same day or within 24 hours."
    )


def _grade_badge_class(grade: str | None) -> str:
    return _GRADE_BADGE_CLASSES.get(grade or "", "bg-gray-100 text-gray-600")


def _haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return 2 * _EARTH_RADIUS_MILES * math.asin(math.sqrt(a))


def get_zip_latlon(zip_code: str) -> tuple[float, float] | None:
    clean = (zip_code or "").strip()[:5]
    if not clean.isdigit():
        return None
    with get_db() as db:
        try:
            row = db.execute(
                "SELECT lat, lon FROM zip_latlon WHERE zip = ? LIMIT 1", (clean,)
            ).fetchone()
        except Exception:
            return None
    return (float(row["lat"]), float(row["lon"])) if row else None


def get_top_cpt_codes(limit: int = 100) -> list[dict]:
    """Return top CPT codes ranked by hospital coverage, with basic stats."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT
                hp.cpt_code,
                COUNT(DISTINCT hp.facility_id) AS hospital_count,
                AVG(hp.gross_charge) AS avg_charge,
                AVG(hp.medicare_rate) AS avg_medicare_rate,
                AVG(hp.markup_vs_medicare) AS avg_markup,
                (AVG(hp.markup_vs_medicare * hp.markup_vs_medicare)
                 - AVG(hp.markup_vs_medicare) * AVG(hp.markup_vs_medicare)) AS markup_variance,
                COALESCE(
                    NULLIF(TRIM(hp.description), ''),
                    (SELECT mr.description FROM medicare_rates mr
                     WHERE mr.cpt_code = hp.cpt_code
                       AND mr.description IS NOT NULL
                     ORDER BY mr.effective_year DESC LIMIT 1)
                ) AS description
            FROM hospital_prices hp
            WHERE hp.gross_charge IS NOT NULL
              AND hp.medicare_rate IS NOT NULL
              AND hp.medicare_rate > 0
              AND hp.markup_vs_medicare IS NOT NULL
            GROUP BY hp.cpt_code
            ORDER BY hospital_count DESC, markup_variance DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    result = []
    for row in rows:
        d = dict(row)
        cpt = d["cpt_code"]
        name = _friendly_name(cpt, d.get("description") or "")
        result.append({
            **d,
            "name": name,
            "body_system": _body_system(cpt),
            "procedure_type": _classify_cpt(cpt),
        })
    return result


def get_procedure_profile(cpt_code: str) -> dict | None:
    """Return full data dict for a procedure detail page."""
    with get_db() as db:
        header_row = db.execute(
            """
            SELECT
                COUNT(DISTINCT hp.facility_id) AS hospital_count,
                AVG(hp.gross_charge) AS avg_charge,
                AVG(hp.medicare_rate) AS avg_medicare_rate,
                MIN(hp.gross_charge) AS min_charge,
                MAX(hp.gross_charge) AS max_charge,
                AVG(hp.markup_vs_medicare) AS avg_markup,
                COALESCE(
                    NULLIF(TRIM(hp.description), ''),
                    (SELECT mr.description FROM medicare_rates mr
                     WHERE mr.cpt_code = hp.cpt_code
                       AND mr.description IS NOT NULL
                     ORDER BY mr.effective_year DESC LIMIT 1)
                ) AS description
            FROM hospital_prices hp
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND hp.medicare_rate IS NOT NULL
              AND hp.medicare_rate > 0
            """,
            (cpt_code,),
        ).fetchone()

        if not header_row or not header_row["hospital_count"]:
            return None

        grade_rows = db.execute(
            """
            SELECT
                m.billing_grade,
                AVG(hp.gross_charge) AS avg_charge,
                AVG(hp.medicare_rate) AS avg_medicare_rate,
                COUNT(*) AS hospital_count
            FROM hospital_prices hp
            JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND m.billing_grade IS NOT NULL
            GROUP BY m.billing_grade
            ORDER BY m.billing_grade
            """,
            (cpt_code,),
        ).fetchall()

        cheapest = db.execute(
            """
            SELECT
                h.name, h.city, h.state, h.state_slug, h.city_slug, h.slug,
                m.billing_grade,
                hp.gross_charge, hp.medicare_rate, hp.markup_vs_medicare
            FROM hospital_prices hp
            JOIN hospitals h ON h.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND hp.markup_vs_medicare IS NOT NULL
            ORDER BY hp.markup_vs_medicare ASC
            LIMIT 10
            """,
            (cpt_code,),
        ).fetchall()

        try:
            cpt_n = int(cpt_code)
            related_rows = db.execute(
                """
                SELECT
                    hp.cpt_code,
                    COUNT(DISTINCT hp.facility_id) AS hospital_count,
                    AVG(hp.gross_charge) AS avg_charge,
                    COALESCE(
                        NULLIF(TRIM(hp.description), ''),
                        (SELECT mr.description FROM medicare_rates mr
                         WHERE mr.cpt_code = hp.cpt_code
                           AND mr.description IS NOT NULL
                         ORDER BY mr.effective_year DESC LIMIT 1)
                    ) AS description
                FROM hospital_prices hp
                WHERE hp.cpt_code != ?
                  AND CAST(hp.cpt_code AS INTEGER) BETWEEN ? AND ?
                  AND hp.gross_charge IS NOT NULL
                GROUP BY hp.cpt_code
                ORDER BY hospital_count DESC
                LIMIT 3
                """,
                (cpt_code, cpt_n - 5000, cpt_n + 5000),
            ).fetchall()
        except (ValueError, TypeError):
            related_rows = []

    header = dict(header_row)
    desc_raw = header.get("description") or ""
    name = _friendly_name(cpt_code, desc_raw)
    procedure_type = _classify_cpt(cpt_code)
    medicare_rate = header.get("avg_medicare_rate")
    avg_charge = header.get("avg_charge")

    by_grade = [
        {
            **dict(gr),
            "patient_cost": round(gr["avg_charge"] * 0.20, 2) if gr["avg_charge"] else None,
            "color": _GRADE_COLORS.get(gr["billing_grade"] or "", "#9ca3af"),
            "badge_class": _grade_badge_class(gr["billing_grade"]),
        }
        for gr in grade_rows
    ]

    cheapest_list = [
        {**dict(r), "badge_class": _grade_badge_class(r["billing_grade"])}
        for r in cheapest
    ]

    related = [
        {
            "cpt_code": r["cpt_code"],
            "name": _friendly_name(r["cpt_code"], r["description"] or ""),
            "hospital_count": r["hospital_count"],
            "avg_charge": r["avg_charge"],
        }
        for r in related_rows
    ]

    # SVG range bar: positions as 0.0–1.0 fractions within min–max span
    min_c = header.get("min_charge") or 0.0
    max_c = header.get("max_charge") or 1.0
    span = max(max_c - min_c, 1.0)

    def _pos(v: float | None) -> float | None:
        if v is None:
            return None
        return max(0.0, min(1.0, (v - min_c) / span))

    range_bar = {
        "min_charge": min_c,
        "max_charge": max_c,
        "avg_charge": avg_charge,
        "medicare_rate": medicare_rate,
        "medicare_pos": _pos(medicare_rate),
        "avg_pos": _pos(avg_charge),
        "zone_a_end": _pos(medicare_rate * 2.0) if medicare_rate else None,
        "zone_b_end": _pos(medicare_rate * 3.0) if medicare_rate else None,
        "zone_c_end": _pos(medicare_rate * 5.0) if medicare_rate else None,
        "zone_d_end": _pos(medicare_rate * 8.0) if medicare_rate else None,
    }

    return {
        "cpt_code": cpt_code,
        "name": name,
        "description": _procedure_description(name, cpt_code, procedure_type),
        "procedure_type": procedure_type,
        "body_system": _body_system(cpt_code),
        "header": {
            "medicare_rate": medicare_rate,
            "national_avg_charge": avg_charge,
            "hospital_count": header["hospital_count"],
            "avg_markup": header.get("avg_markup"),
        },
        "by_grade": by_grade,
        "range_bar": range_bar,
        "cheapest_hospitals": cheapest_list,
        "faq": _build_procedure_faq(name, cpt_code, procedure_type, medicare_rate, avg_charge),
        "related": related,
        "seo": _build_procedure_seo(name, cpt_code, medicare_rate, avg_charge, header["hospital_count"]),
    }


def get_hospitals_near_zip_for_cpt(cpt_code: str, zip_code: str, limit: int = 10) -> list[dict]:
    """Return up to `limit` hospitals within 75 miles of zip with data for this CPT code."""
    coords = get_zip_latlon(zip_code)
    if not coords:
        return []
    zip_lat, zip_lon = coords
    lat_delta = _PROCEDURE_RADIUS_MILES / 69.0
    lon_delta = _PROCEDURE_RADIUS_MILES / max(69.17 * math.cos(math.radians(zip_lat)), 0.1)

    with get_db() as db:
        candidates = db.execute(
            """
            SELECT
                h.name, h.city, h.state, h.state_slug, h.city_slug, h.slug,
                h.lat, h.lon,
                m.billing_grade,
                hp.gross_charge, hp.medicare_rate, hp.markup_vs_medicare
            FROM hospital_prices hp
            JOIN hospitals h ON h.facility_id = hp.facility_id
            LEFT JOIN billing_metrics m ON m.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND hp.markup_vs_medicare IS NOT NULL
              AND h.lat BETWEEN ? AND ?
              AND h.lon BETWEEN ? AND ?
            ORDER BY hp.gross_charge ASC
            LIMIT 50
            """,
            (
                cpt_code,
                zip_lat - lat_delta, zip_lat + lat_delta,
                zip_lon - lon_delta, zip_lon + lon_delta,
            ),
        ).fetchall()

    results = []
    for row in candidates:
        if row["lat"] is None or row["lon"] is None:
            continue
        dist = _haversine_miles(zip_lat, zip_lon, row["lat"], row["lon"])
        if dist <= _PROCEDURE_RADIUS_MILES:
            results.append({
                **dict(row),
                "distance_miles": round(dist, 1),
                "badge_class": _grade_badge_class(row["billing_grade"]),
            })

    results.sort(key=lambda r: r["gross_charge"] or 0)
    return results[:limit]


def _build_procedure_faq(
    name: str,
    cpt_code: str,
    procedure_type: str,
    medicare_rate: float | None,
    avg_charge: float | None,
) -> list[dict]:
    rate_str = f"${medicare_rate:,.0f}" if medicare_rate else "the Medicare rate"
    avg_str = f"${avg_charge:,.0f}" if avg_charge else "the national average"
    two_x_str = f"${medicare_rate * 2:,.0f}" if medicare_rate else "two times Medicare"
    patient_cost_str = f"${avg_charge * 0.20:,.0f}" if avg_charge else "a significant portion"

    if procedure_type == "imaging":
        return [
            {
                "q": f"Why does {name} cost so much more at some hospitals than others?",
                "a": (
                    f"Hospital charges for {name} (CPT {cpt_code}) vary dramatically—sometimes "
                    f"by 10x or more—because hospitals set their own gross charges independently. "
                    f"Medicare pays {rate_str} for this procedure based on actual delivery costs, "
                    f"but hospitals are not required to match that rate. The national average charge "
                    f"is {avg_str}. Using a price transparency tool helps you find a fairly priced facility."
                ),
            },
            {
                "q": f"Can I shop around for {name} if my doctor ordered it?",
                "a": (
                    f"Yes. As long as the same CPT code ({cpt_code}) is billed, the ordering physician "
                    f"does not need to be at the same facility that performs the scan. You can call "
                    f"hospitals and freestanding imaging centers to ask for their cash price or "
                    f"expected out-of-pocket cost before scheduling. Freestanding imaging centers "
                    f"typically charge significantly less than hospital outpatient departments."
                ),
            },
            {
                "q": f"What should I do if I received a bill for {name} that seems high?",
                "a": (
                    f"Compare the charge on your bill to the Medicare reference rate of {rate_str}. "
                    f"If the hospital billed more than {two_x_str} (two times Medicare), you may be "
                    f"able to negotiate. Request an itemized bill, check for duplicate charges, and "
                    f"ask whether a prompt-pay or financial hardship discount applies. You can also "
                    f"upload your bill to BillKarma for a free automated review."
                ),
            },
        ]

    if procedure_type == "surgical":
        return [
            {
                "q": f"How much does {name} cost with insurance?",
                "a": (
                    f"With insurance, your out-of-pocket cost for {name} (CPT {cpt_code}) depends "
                    f"on your deductible, coinsurance rate, and in-network status. Medicare pays "
                    f"{rate_str} for this procedure; the national average hospital charge is {avg_str}. "
                    f"Under standard 20% coinsurance after deductible, a patient at an average-charging "
                    f"hospital would owe approximately {patient_cost_str}. Always verify your benefits "
                    f"before scheduling."
                ),
            },
            {
                "q": f"Does where I have {name} done affect my recovery?",
                "a": (
                    f"Hospital quality and surgical volume can influence outcomes for procedures like "
                    f"{name}. High-volume centers tend to have lower complication rates for complex "
                    f"surgeries. However, billing grade is separate from quality ratings—some highly "
                    f"graded billing hospitals also have strong clinical outcomes. Review both the "
                    f"BillKarma billing grade and CMS quality stars when choosing a facility."
                ),
            },
            {
                "q": f"How do I negotiate the cost of {name} if I'm on a high-deductible plan?",
                "a": (
                    f"If you're paying a significant portion out-of-pocket, ask the hospital for their "
                    f"cash price before scheduling. Many hospitals offer 10–40% discounts for self-pay "
                    f"patients. Medicare pays {rate_str} for this procedure—use that as your negotiating "
                    f"anchor. Also ask the billing department about payment plans or charity care if "
                    f"the cost poses a financial hardship."
                ),
            },
        ]

    # outpatient / diagnostic
    return [
        {
            "q": f"Is {name} covered by insurance?",
            "a": (
                f"{name} (CPT {cpt_code}) is generally covered by most insurance plans when medically "
                f"necessary, but coverage varies by plan type and medical necessity criteria. Medicare "
                f"pays {rate_str} for this procedure. Always confirm your benefit coverage and any "
                f"prior authorization requirements with your insurer before scheduling."
            ),
        },
        {
            "q": f"Why might I be billed separately for {name} by multiple providers?",
            "a": (
                f"When {name} is performed at a hospital outpatient facility, you may receive separate "
                f"bills from the hospital (facility fee) and from the physician or specialist who "
                f"performed or interpreted the procedure. This split billing—professional fee plus "
                f"facility fee—is common. The national average hospital charge is {avg_str}, so make "
                f"sure each individual bill reflects only the services that were actually provided."
            ),
        },
        {
            "q": f"How can I find out what my insurance will pay for {name} before I go?",
            "a": (
                f"Call the member services number on your insurance card and ask for a cost estimate "
                f"or Explanation of Benefits preview for CPT {cpt_code}. Also confirm whether the "
                f"facility you're considering is in-network. Medicare's reference rate for this "
                f"procedure is {rate_str}—if a hospital charges significantly more, you may owe more "
                f"out-of-pocket than expected even with insurance."
            ),
        },
    ]


def _build_procedure_seo(
    name: str,
    cpt_code: str,
    medicare_rate: float | None,
    avg_charge: float | None,
    hospital_count: int,
) -> dict:
    rate_str = f"${medicare_rate:,.0f}" if medicare_rate else "N/A"
    avg_str = f"${avg_charge:,.0f}" if avg_charge else "N/A"
    title = f"{name}: Cost, Grade & Prices | BillKarma"
    if len(title) > 60:
        short = name[:28].rsplit(" ", 1)[0] if len(name) > 28 else name
        title = f"{short}: Cost & Fair Prices | BillKarma"
    desc = (
        f"CPT {cpt_code} · Medicare rate {rate_str} · National avg {avg_str}. "
        f"Compare {hospital_count:,} hospitals by billing grade and see if your bill is fair."
    )
    if len(desc) > 155:
        desc = desc[:152].rsplit(" ", 1)[0] + "..."
    return {"page_title": title, "meta_description": desc}
