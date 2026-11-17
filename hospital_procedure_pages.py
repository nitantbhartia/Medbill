"""Hospital x procedure pages: one hospital's charge for one CPT code, compared with Medicare and the state."""

import json

import config
from db import get_db
from hospital_seo import _display_city, _display_name, state_display_name

PRICE_COLUMNS = """
    hp.cpt_code, hp.gross_charge, hp.cash_price, hp.medicare_rate, hp.markup_vs_medicare,
    COALESCE(
        NULLIF(TRIM(hp.description), ''),
        (SELECT mr.description FROM medicare_rates mr
         WHERE mr.cpt_code = hp.cpt_code AND TRIM(COALESCE(mr.description, '')) != ''
         ORDER BY mr.effective_year DESC LIMIT 1)
    ) AS description
"""
HAS_COMPARABLE_PRICE = "hp.gross_charge > 0 AND hp.medicare_rate > 0 AND hp.markup_vs_medicare IS NOT NULL"


def _json_ld(data: dict) -> str:
    return json.dumps(data).replace("</", "<\\/")


def _fair_ceiling(medicare_rate: float) -> float:
    return round(medicare_rate * config.MEDICARE_MARKUP_THRESHOLD, 2)


def _faq(hospital_name: str, description: str, cpt_code: str, price: dict) -> list[tuple[str, str]]:
    charge = f"${price['gross_charge']:,.2f}"
    medicare = f"${price['medicare_rate']:,.2f}"
    return [
        (
            f"How much does {hospital_name} charge for {description} (CPT {cpt_code})?",
            f"The hospital's posted charge is {charge}. Medicare pays hospitals about {medicare} for the same code, "
            f"so the charge is {price['markup_vs_medicare']:.1f} times the Medicare rate.",
        ),
        (
            "What is a fair price for this service?",
            f"A common benchmark is up to {config.MEDICARE_MARKUP_THRESHOLD:g} times the Medicare rate, "
            f"which is ${price['fair_ceiling']:,.2f} here. Insurers and financial-assistance programs often pay far less than the posted charge.",
        ),
    ]


def get_hospital_procedure_page(state_slug: str, city_slug: str, hospital_slug: str, cpt_code: str) -> dict | None:
    cpt_code = cpt_code.upper()
    with get_db() as db:
        hospital = db.execute(
            "SELECT facility_id, name, city, state, state_slug, city_slug, slug FROM hospitals "
            "WHERE state_slug = ? AND city_slug = ? AND slug = ?",
            (state_slug, city_slug, hospital_slug),
        ).fetchone()
        if not hospital:
            return None
        price = db.execute(
            f"SELECT {PRICE_COLUMNS} FROM hospital_prices hp "
            f"WHERE hp.facility_id = ? AND hp.cpt_code = ? AND {HAS_COMPARABLE_PRICE} "
            "ORDER BY hp.data_year DESC LIMIT 1",
            (hospital["facility_id"], cpt_code),
        ).fetchone()
        if not price:
            return None
        state_avg = db.execute(
            "SELECT avg_markup_vs_medicare FROM benchmark_averages WHERE scope = ? AND cpt_code = ?",
            (hospital["state"], cpt_code),
        ).fetchone()
        alternatives = db.execute(
            "SELECT h.name, h.city, h.state_slug, h.city_slug, h.slug, hp.gross_charge, hp.cash_price "
            "FROM hospital_prices hp JOIN hospitals h ON h.facility_id = hp.facility_id "
            f"WHERE hp.cpt_code = ? AND h.state = ? AND hp.facility_id != ? AND {HAS_COMPARABLE_PRICE} "
            "ORDER BY hp.gross_charge ASC LIMIT ?",
            (cpt_code, hospital["state"], hospital["facility_id"], config.HOSPITAL_PROCEDURE_ALTERNATIVES),
        ).fetchall()

    price = dict(price)
    price["fair_ceiling"] = _fair_ceiling(price["medicare_rate"])
    price["above_fair"] = max(0.0, round(price["gross_charge"] - price["fair_ceiling"], 2))
    description = price["description"] or f"CPT {cpt_code}"
    name = _display_name(hospital["name"], hospital["facility_id"])
    city = _display_city(hospital["city"])
    state = state_display_name(hospital["state"])
    base = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/{hospital_slug}/"
    faq = _faq(name, description, cpt_code, price)

    return {
        "hospital": {"name": name, "city": city, "state": state, "state_slug": state_slug, "city_slug": city_slug, "slug": hospital_slug},
        "price": price,
        "description": description,
        "state_avg_markup": state_avg["avg_markup_vs_medicare"] if state_avg else None,
        "alternatives": [
            {**dict(a), "name": _display_name(a["name"]), "city": _display_city(a["city"])} for a in alternatives
        ],
        "fair_multiple": f"{config.MEDICARE_MARKUP_THRESHOLD:g}",
        "faq": faq,
        "faq_schema_json": _json_ld({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
            ],
        }),
        "page_title": f"{description} Cost at {name} | BillKarma",
        "meta_description": (
            f"{name} in {city}, {state} charges ${price['gross_charge']:,.0f} for {description.lower()} "
            f"(CPT {cpt_code}), {price['markup_vs_medicare']:.1f}x the Medicare rate. See a fair price and how to dispute it."
        ),
        "canonical_url": f"{base}{cpt_code}/",
        "hospital_url": base,
    }


def get_hospital_procedure_sitemap_paths() -> list[str]:
    with get_db() as db:
        rows = db.execute(
            "SELECT h.state_slug, h.city_slug, h.slug, hp.cpt_code "
            "FROM hospital_prices hp JOIN hospitals h ON h.facility_id = hp.facility_id "
            f"WHERE h.state_slug IS NOT NULL AND h.city_slug IS NOT NULL AND h.slug IS NOT NULL AND {HAS_COMPARABLE_PRICE} "
            "GROUP BY h.state_slug, h.city_slug, h.slug, hp.cpt_code "
            "ORDER BY MAX(hp.markup_vs_medicare) DESC LIMIT ?",
            (config.HOSPITAL_PROCEDURE_SITEMAP_MAX,),
        ).fetchall()
    return [f"/hospitals/{r['state_slug']}/{r['city_slug']}/{r['slug']}/{r['cpt_code']}/" for r in rows]
