"""High-value procedure cost content page helpers."""

from __future__ import annotations

from dataclasses import dataclass, field

from db import get_db
from procedure_pages import _ALL_PRICES_CTE, _classify_cpt, _trim_outlier_rows, get_procedure_profile

_SLUG_TO_CPT = {
    "mri-cost": "70551",
    "colonoscopy-cost": "45378",
    "knee-replacement-cost": "27447",
    "hip-replacement-cost": "27130",
    "ct-scan-cost": "74177",
    "er-visit-cost": "99284",
    "x-ray-cost": "71045",
    "ultrasound-cost": "76700",
}

_WHAT_TO_ASK: dict[str, list[str]] = {
    "mri-cost": [
        "Can this MRI be done at an independent imaging center instead of the hospital?",
        "Does my insurance require prior authorization for this scan?",
        "Will the radiologist bill separately from the facility?",
        "Is contrast dye required, or can a non-contrast scan be done?",
        "Is the imaging center hospital-owned or independently operated?",
        "Can I get a Good Faith Estimate under the No Surprises Act?",
    ],
    "colonoscopy-cost": [
        "Is this being billed as a preventive or diagnostic colonoscopy? (Preventive is usually 100% covered.)",
        "Will the anesthesiologist bill separately? Are they in-network with my insurance?",
        "Can this procedure be done at an ambulatory surgery center instead of a hospital?",
        "What is the facility fee separately from the physician fee?",
        "If a polyp is removed, will the billing change from preventive to diagnostic?",
        "Can I get a Good Faith Estimate before I schedule?",
    ],
    "ct-scan-cost": [
        "Does this CT scan require prior authorization from my insurance?",
        "Can this scan be done at an independent imaging center instead of the hospital?",
        "Will the radiologist fee be billed separately from the facility fee?",
        "Is contrast dye required, or can a non-contrast scan (different CPT) be done?",
        "Is the imaging center hospital-owned or independently operated?",
        "Can I get a Good Faith Estimate under the No Surprises Act?",
    ],
    "er-visit-cost": [
        "What level of ER service is being billed and how was that determined?",
        "Will the ER physician bill separately from the facility?",
        "Will any specialists seen in the ER also bill separately?",
        "Does the hospital have a charity care or financial assistance program?",
        "Can I request a fully itemized bill before making any payment?",
        "Can I request a review of the billing level assigned to my visit?",
    ],
    "knee-replacement-cost": [
        "Can this surgery be done at an ambulatory surgery center instead of a hospital?",
        "Will my surgeon and the facility bill separately?",
        "What implant brand and model will be used, and what does it cost?",
        "Are post-operative physical therapy sessions included, or billed separately?",
        "Can I get a bundled payment estimate covering the full episode of care?",
        "Can I get a Good Faith Estimate under the No Surprises Act?",
    ],
}

_DEFAULT_WHAT_TO_ASK = [
    "What is the CPT code for this procedure?",
    "Can I get a Good Faith Estimate before I schedule?",
    "Will any providers bill separately from the facility (e.g., anesthesiologist, radiologist)?",
    "Does my insurance require prior authorization?",
    "Does the facility have a financial assistance or charity care program?",
]


@dataclass
class ProcedureContentConfig:
    slug: str
    cpt_code: str
    heading: str
    default_facility_type: str
    what_to_ask: list[str] = field(default_factory=list)


def _config_for_slug(slug: str) -> ProcedureContentConfig | None:
    cpt = _SLUG_TO_CPT.get(slug)
    if not cpt:
        return None
    profile = get_procedure_profile(cpt)
    name = (profile or {}).get("name") or f"CPT {cpt}"
    what_to_ask = _WHAT_TO_ASK.get(slug, _DEFAULT_WHAT_TO_ASK)

    headings = {
        "mri-cost": ("MRI Cost: What You Should Pay in 2026", "imaging_center"),
        "colonoscopy-cost": ("Colonoscopy Cost: What You Should Pay in 2026", "asc"),
        "ct-scan-cost": ("CT Scan Cost: What You Should Pay in 2026", "imaging_center"),
        "er-visit-cost": ("ER Visit Cost: What Different Levels Cost in 2026", "hospital"),
        "knee-replacement-cost": ("Knee Replacement Cost: Hospital vs. Surgery Center", "asc"),
        "hip-replacement-cost": ("Hip Replacement Cost: Hospital vs. Surgery Center", "asc"),
        "x-ray-cost": ("X-Ray Cost: What You Should Pay in 2026", "imaging_center"),
        "ultrasound-cost": ("Ultrasound Cost: What You Should Pay in 2026", "imaging_center"),
    }

    heading, default_type = headings.get(slug, (f"{name} Cost: What You Should Pay in 2026", "hospital"))
    return ProcedureContentConfig(
        slug=slug, cpt_code=cpt, heading=heading,
        default_facility_type=default_type, what_to_ask=what_to_ask,
    )


def _facility_type_label(ftype: str) -> str:
    return {
        "hospital": "Hospitals",
        "asc": "Surgery Centers",
        "imaging_center": "Imaging Centers",
    }.get(ftype, ftype.title())


def get_content_page_data(slug: str) -> dict | None:
    cfg = _config_for_slug(slug)
    if not cfg:
        return None
    profile = get_procedure_profile(cfg.cpt_code)
    if not profile:
        return None
    procedure_type = _classify_cpt(cfg.cpt_code)

    with get_db() as db:
        state_price_rows = db.execute(
            f"""
            {_ALL_PRICES_CTE}
            SELECT
                COALESCE(f.state, h.state) AS state,
                hp.gross_charge
            FROM all_prices hp
            LEFT JOIN facilities f ON f.facility_id = hp.facility_id
            LEFT JOIN hospitals h ON h.facility_id = hp.facility_id
            WHERE hp.cpt_code = ?
              AND hp.gross_charge IS NOT NULL
              AND COALESCE(f.state, h.state) IS NOT NULL
            """,
            (cfg.cpt_code,),
        ).fetchall()

    grouped: dict[str, list[dict]] = {}
    for row in state_price_rows:
        state = (row["state"] or "").strip().upper()
        if not state:
            continue
        grouped.setdefault(state, []).append({"gross_charge": row["gross_charge"]})

    state_rows = []
    for state, rows in grouped.items():
        trimmed, _ = _trim_outlier_rows(rows, "gross_charge")
        usable = trimmed or rows
        charges = [float(r["gross_charge"]) for r in usable if r.get("gross_charge") is not None]
        if not charges:
            continue
        state_rows.append({"state": state, "avg_charge": sum(charges) / len(charges)})
    state_rows.sort(key=lambda r: r["avg_charge"])
    state_rows = state_rows[:20]

    by_type = []
    for row in (profile.get("ranges_by_type") or []):
        d = dict(row)
        d["providers"] = d.get("provider_count")
        d["label"] = _facility_type_label(d.get("facility_type") or "hospital")
        by_type.append(d)

    profile["content_heading"] = cfg.heading
    profile["content_slug"] = slug
    profile["default_facility_type"] = cfg.default_facility_type
    profile["by_facility_type"] = by_type
    profile["state_averages"] = state_rows
    profile["excluded_outliers"] = (profile.get("header") or {}).get("excluded_outliers", 0)
    profile["is_imaging_content"] = procedure_type == "imaging"
    profile["is_colonoscopy_content"] = cfg.cpt_code == "45378"
    profile["is_er_content"] = cfg.cpt_code == "99284"
    profile["what_to_ask"] = cfg.what_to_ask
    return profile
