"""High-value procedure cost content page helpers."""

from __future__ import annotations

from dataclasses import dataclass

from db import get_db
from procedure_pages import _classify_cpt, get_procedure_profile

_SLUG_TO_CPT = {
    "mri-cost": "70553",
    "colonoscopy-cost": "45378",
    "knee-replacement-cost": "27447",
    "hip-replacement-cost": "27130",
    "ct-scan-cost": "74178",
    "x-ray-cost": "71045",
    "ultrasound-cost": "76700",
}


@dataclass
class ProcedureContentConfig:
    slug: str
    cpt_code: str
    heading: str
    default_facility_type: str


def _config_for_slug(slug: str) -> ProcedureContentConfig | None:
    cpt = _SLUG_TO_CPT.get(slug)
    if not cpt:
        return None
    profile = get_procedure_profile(cpt)
    name = (profile or {}).get("name") or f"CPT {cpt}"
    if slug == "mri-cost":
        heading = "How Much Does an MRI Cost?"
        default_type = "imaging_center"
    elif slug == "colonoscopy-cost":
        heading = "How Much Does a Colonoscopy Cost?"
        default_type = "asc"
    else:
        heading = f"How Much Does {name} Cost?"
        default_type = "hospital"
    return ProcedureContentConfig(slug=slug, cpt_code=cpt, heading=heading, default_facility_type=default_type)


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
        rows = db.execute(
            """
            SELECT
                COALESCE(f.facility_type, p.facility_type, 'hospital') AS facility_type,
                COUNT(*) AS providers,
                MIN(p.gross_charge) AS min_charge,
                MAX(p.gross_charge) AS max_charge,
                AVG(p.gross_charge) AS avg_charge,
                AVG(p.markup_vs_medicare) AS avg_markup
            FROM (
                SELECT facility_id, cpt_code, gross_charge, markup_vs_medicare, facility_type FROM hospital_prices
                UNION ALL
                SELECT facility_id, cpt_code, gross_charge, markup_vs_medicare, facility_type FROM procedure_prices
            ) p
            LEFT JOIN facilities f ON f.facility_id = p.facility_id
            WHERE p.cpt_code = ?
              AND p.gross_charge IS NOT NULL
            GROUP BY COALESCE(f.facility_type, p.facility_type, 'hospital')
            ORDER BY avg_charge
            """,
            (cfg.cpt_code,),
        ).fetchall()

        state_rows = db.execute(
            """
            SELECT
                COALESCE(f.state, h.state) AS state,
                AVG(p.gross_charge) AS avg_charge
            FROM (
                SELECT facility_id, cpt_code, gross_charge FROM hospital_prices
                UNION ALL
                SELECT facility_id, cpt_code, gross_charge FROM procedure_prices
            ) p
            LEFT JOIN facilities f ON f.facility_id = p.facility_id
            LEFT JOIN hospitals h ON h.facility_id = p.facility_id
            WHERE p.cpt_code = ?
              AND p.gross_charge IS NOT NULL
              AND COALESCE(f.state, h.state) IS NOT NULL
            GROUP BY COALESCE(f.state, h.state)
            ORDER BY avg_charge ASC
            LIMIT 20
            """,
            (cfg.cpt_code,),
        ).fetchall()

    by_type = []
    for row in rows:
        d = dict(row)
        d["label"] = _facility_type_label(d["facility_type"] or "hospital")
        by_type.append(d)

    profile["content_heading"] = cfg.heading
    profile["content_slug"] = slug
    profile["default_facility_type"] = cfg.default_facility_type
    profile["by_facility_type"] = by_type
    profile["state_averages"] = [dict(r) for r in state_rows]
    profile["is_imaging_content"] = procedure_type == "imaging"
    profile["is_colonoscopy_content"] = cfg.cpt_code == "45378"
    return profile
