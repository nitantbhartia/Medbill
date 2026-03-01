"""Consumer-friendly 'How Much Does X Cost?' landing pages."""

from __future__ import annotations

from db import get_db
from procedure_pages import get_procedure_profile


# Maps consumer-friendly slugs to CPT codes and display data
COST_PAGE_SPECS = {
    "mri": {
        "cpt": "70551",
        "title": "How Much Does an MRI Cost?",
        "subtitle": "National average prices, Medicare rates, and tips to pay less.",
        "description": "MRI (Magnetic Resonance Imaging) scan",
        "alt_facility": "imaging_center",
        "tips": [
            "Independent imaging centers charge 40&ndash;60% less than hospitals for the same scan.",
            "Ask if contrast dye is required. Non-contrast MRIs (CPT 70551) cost less than contrast (70553).",
            "Hospital-owned imaging centers often bill at hospital rates. Ask about ownership.",
            "Request a Good Faith Estimate before scheduling. It&rsquo;s your right under the No Surprises Act.",
            "If uninsured, ask for the cash/self-pay rate &mdash; it&rsquo;s often significantly less.",
        ],
    },
    "mri-brain": {
        "cpt": "70551",
        "title": "How Much Does a Brain MRI Cost?",
        "subtitle": "Compare hospital vs. imaging center prices near you.",
        "description": "Brain MRI without contrast",
        "alt_facility": "imaging_center",
        "tips": [
            "A brain MRI without contrast (CPT 70551) is the most common type. With contrast costs more.",
            "Independent imaging centers charge 40&ndash;60% less than hospitals.",
            "If your doctor orders it, your insurance must cover it (subject to deductible).",
            "Request a Good Faith Estimate &mdash; it&rsquo;s your right under the No Surprises Act.",
        ],
    },
    "ct-scan": {
        "cpt": "74177",
        "title": "How Much Does a CT Scan Cost?",
        "subtitle": "Average prices by facility type and ways to save.",
        "description": "CT scan of abdomen and pelvis with contrast",
        "alt_facility": "imaging_center",
        "tips": [
            "Independent imaging centers charge 40&ndash;60% less than hospitals for CT scans.",
            "Ask whether contrast is truly needed. Non-contrast CTs are coded differently and cost less.",
            "Hospital-owned imaging centers often charge hospital-level facility fees.",
            "A CT abdomen/pelvis with contrast (CPT 74177) is one of the most common CT orders.",
            "If uninsured, ask for the self-pay rate before your appointment.",
        ],
    },
    "colonoscopy": {
        "cpt": "45378",
        "title": "How Much Does a Colonoscopy Cost?",
        "subtitle": "Preventive vs. diagnostic pricing and how to avoid surprise bills.",
        "description": "Diagnostic colonoscopy",
        "alt_facility": "asc",
        "tips": [
            "Preventive colonoscopies are 100% covered by insurance with no copay (ACA mandate).",
            "If a polyp is removed, billing may switch from preventive to diagnostic &mdash; ask in advance.",
            "Ambulatory surgery centers (ASCs) charge 30&ndash;50% less than hospitals.",
            "The anesthesiologist often bills separately. Confirm they&rsquo;re in-network.",
            "Ask for a bundled quote covering facility, physician, and anesthesia fees.",
        ],
    },
    "knee-replacement": {
        "cpt": "27447",
        "title": "How Much Does a Knee Replacement Cost?",
        "subtitle": "Hospital vs. surgery center prices and saving strategies.",
        "description": "Total knee replacement (arthroplasty)",
        "alt_facility": "asc",
        "tips": [
            "Surgery centers (ASCs) charge 30&ndash;60% less than hospitals for knee replacements.",
            "Implant costs vary widely ($2k&ndash;$12k). Ask what brand/model will be used.",
            "Get a bundled price estimate covering surgeon, facility, anesthesia, and implant.",
            "Physical therapy is usually billed separately. Clarify how many sessions are included.",
            "Request a Good Faith Estimate under the No Surprises Act.",
        ],
    },
    "hip-replacement": {
        "cpt": "27130",
        "title": "How Much Does a Hip Replacement Cost?",
        "subtitle": "Compare hospital vs. surgery center prices.",
        "description": "Total hip replacement (arthroplasty)",
        "alt_facility": "asc",
        "tips": [
            "Surgery centers charge significantly less than hospitals for hip replacements.",
            "The implant itself can cost $2k&ndash;$15k. Ask about the specific device and its cost.",
            "Many hospitals offer bundled payment programs for joint replacements.",
            "Post-operative rehab is usually billed separately. Ask what&rsquo;s included.",
            "If uninsured, nonprofit hospitals must offer financial assistance under IRS 501(r).",
        ],
    },
    "er-visit": {
        "cpt": "99284",
        "title": "How Much Does an ER Visit Cost?",
        "subtitle": "ER billing levels, facility fees, and how to dispute overcharges.",
        "description": "Level 4 emergency department visit",
        "alt_facility": "",
        "tips": [
            "ER visits are billed at 5 levels (99281&ndash;99285). Level 4&ndash;5 cost 2&ndash;4x more than Level 1&ndash;2.",
            "You can request a billing level review if you think you were upcoded.",
            "The ER physician bills separately from the hospital facility fee.",
            "Specialists seen in the ER (radiology, etc.) each bill separately too.",
            "Under the No Surprises Act, out-of-network ER providers cannot balance bill you.",
        ],
    },
    "x-ray": {
        "cpt": "71045",
        "title": "How Much Does an X-Ray Cost?",
        "subtitle": "Average prices and where to get the best deal.",
        "description": "Chest X-ray (single view)",
        "alt_facility": "imaging_center",
        "tips": [
            "X-rays are one of the cheapest imaging tests. Don&rsquo;t overpay at a hospital.",
            "Independent imaging centers and urgent care clinics often have the lowest X-ray prices.",
            "The radiologist reading fee is usually billed separately from the facility fee.",
            "If you&rsquo;re uninsured, many clinics offer flat cash-pay rates for X-rays.",
        ],
    },
    "ultrasound": {
        "cpt": "76700",
        "title": "How Much Does an Ultrasound Cost?",
        "subtitle": "Average prices by facility type and money-saving tips.",
        "description": "Abdominal ultrasound (complete)",
        "alt_facility": "imaging_center",
        "tips": [
            "Independent imaging centers typically charge 40&ndash;60% less than hospitals.",
            "Hospital-owned imaging centers often apply hospital-level facility fees.",
            "Obstetric ultrasounds (CPT 76805) are coded differently and may cost more.",
            "Ask for the cash/self-pay rate if you&rsquo;re uninsured.",
        ],
    },
    "mammogram": {
        "cpt": "77067",
        "title": "How Much Does a Mammogram Cost?",
        "subtitle": "Screening mammograms should be free. Here&rsquo;s what to watch for.",
        "description": "Screening mammography (bilateral)",
        "alt_facility": "imaging_center",
        "tips": [
            "Screening mammograms are covered at 100% (no copay) under the ACA for women 40+.",
            "If the radiologist finds something and orders additional views, those may be billed as diagnostic.",
            "Independent imaging centers charge less than hospitals for diagnostic mammograms.",
            "If you&rsquo;re billed for a screening mammogram, your insurer may have miscoded it. Dispute it.",
        ],
    },
}


def get_cost_page_data(slug: str) -> dict | None:
    """Return all data needed to render a /cost/<slug> page."""
    spec = COST_PAGE_SPECS.get(slug)
    if not spec:
        return None

    profile = get_procedure_profile(spec["cpt"])
    if not profile:
        return None

    header = profile.get("header") or {}
    ranges = profile.get("ranges_by_type") or []

    # Build facility type price ranges
    facility_prices = []
    for r in ranges:
        d = dict(r)
        ftype = d.get("facility_type", "hospital")
        d["label"] = {"hospital": "Hospital", "asc": "Surgery Center", "imaging_center": "Imaging Center"}.get(ftype, ftype.title())
        facility_prices.append(d)

    # National price range
    national_low = header.get("p25") or header.get("min_charge")
    national_high = header.get("p75") or header.get("max_charge")
    national_median = header.get("median_charge")
    medicare_rate = header.get("medicare_rate") or header.get("facility_rate")

    # State averages from raw data
    state_averages = _get_state_averages(spec["cpt"])

    return {
        "slug": slug,
        "cpt_code": spec["cpt"],
        "title": spec["title"],
        "subtitle": spec["subtitle"],
        "description": spec["description"],
        "alt_facility": spec["alt_facility"],
        "tips": spec["tips"],
        "national_low": national_low,
        "national_high": national_high,
        "national_median": national_median,
        "medicare_rate": medicare_rate,
        "facility_prices": facility_prices,
        "state_averages": state_averages,
        "provider_count": header.get("provider_count", 0),
        "name": profile.get("name", ""),
        "seo": {
            "meta_description": f"{spec['title'].rstrip('?')} in 2026. National average: ${int(national_median or 0):,}. Compare hospital vs. imaging center prices and find cheaper options near you."
            if national_median
            else f"{spec['title'].rstrip('?')} in 2026. Compare prices by facility type, check Medicare rates, and find savings tips.",
        },
    }


def _get_state_averages(cpt_code: str, limit: int = 15) -> list[dict]:
    """Return average charges by state for a CPT code."""
    with get_db() as db:
        rows = db.execute(
            """
            WITH all_prices AS (
                SELECT facility_id, cpt_code, gross_charge FROM hospital_prices
                UNION ALL
                SELECT facility_id, cpt_code, gross_charge FROM procedure_prices
            )
            SELECT
                COALESCE(f.state, h.state) AS state,
                AVG(ap.gross_charge) AS avg_charge,
                MIN(ap.gross_charge) AS min_charge,
                MAX(ap.gross_charge) AS max_charge,
                COUNT(*) AS provider_count
            FROM all_prices ap
            LEFT JOIN facilities f ON f.facility_id = ap.facility_id
            LEFT JOIN hospitals h ON h.facility_id = ap.facility_id
            WHERE ap.cpt_code = ?
              AND ap.gross_charge IS NOT NULL
              AND ap.gross_charge > 0
              AND ap.gross_charge < 500000
              AND COALESCE(f.state, h.state) IS NOT NULL
            GROUP BY COALESCE(f.state, h.state)
            HAVING COUNT(*) >= 3
            ORDER BY avg_charge ASC
            LIMIT ?
            """,
            (cpt_code, limit),
        ).fetchall()
    return [dict(r) for r in rows]


def get_all_cost_slugs() -> list[str]:
    """Return all available cost page slugs for sitemap generation."""
    return list(COST_PAGE_SPECS.keys())
