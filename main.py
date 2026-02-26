import logging
import re

from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, Response, JSONResponse

import config
import db
import dispute_service
import esign as esign_module
import payment as payment_module
from api import router as api_router
from analyzer import compute_case_summary, get_bill_results, get_stats
from compliance import log_audit
from hospital_seo import (
    find_hospitals,
    get_cities_for_state,
    get_grade_distribution,
    get_hospital_profile,
    get_hospital_sitemap_paths,
    get_sample_hospitals,
    get_state_hospitals,
    get_state_index_stats,
    resolve_hospital_slug,
    slugify,
    state_display_name,
)
from compare_pages import get_comparison_data, search_hospitals_for_compare
from dispute_workflow import build_phone_script, get_outcome_stats
from facility_pages import get_facility_profile, get_facilities_in_scope, get_facility_state_index, get_landing_stats
from procedure_pages import (
    get_hospitals_near_zip_for_cpt,
    get_providers_near_zip_for_cpt,
    get_procedure_profile,
    get_top_cpt_codes,
)
from procedure_content import get_content_page_data
from tools_catalog import list_tools, get_tool
from access_control import require_bill_access, require_case_access

logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

app = FastAPI(title=config.APP_NAME)
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    if not config.DEBUG:
        response.headers.setdefault("Strict-Transport-Security", "max-age=63072000; includeSubDomains; preload")
    return response

templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config

HOME_PROCEDURE_CARD_SPECS = [
    {"cpt_code": "70551", "name": "MRI of Brain (w/o contrast)", "category": "Imaging", "secondary_type": "imaging_center"},
    {"cpt_code": "45378", "name": "Colonoscopy (Diagnostic)", "category": "Surgery", "secondary_type": "asc"},
    {"cpt_code": "99284", "name": "Level 4 ER Visit", "category": "Emergency", "secondary_type": ""},
    {"cpt_code": "44970", "name": "Appendectomy (Laparoscopic)", "category": "Surgery", "secondary_type": "asc"},
    {"cpt_code": "74177", "name": "CT Abdomen/Pelvis w/ contrast", "category": "Imaging", "secondary_type": "imaging_center"},
    {"cpt_code": "27447", "name": "Knee Replacement (Total)", "category": "Surgery", "secondary_type": "asc"},
    {"cpt_code": "77067", "name": "Mammography (Screening)", "category": "Preventive", "secondary_type": "imaging_center"},
    {"cpt_code": "80048", "name": "Basic Metabolic Panel", "category": "Lab Tests", "secondary_type": ""},
]

FACILITY_TYPE_LABELS = {
    "hospital": "Hospital",
    "asc": "Surgery Center",
    "imaging_center": "Imaging Center",
}

PROCEDURE_KEYWORD_CPTS = {
    "mri": ["70551", "70553", "72141", "72148", "73221", "73721", "74183"],
    "ct": ["74176", "74177"],
    "ct scan": ["74176", "74177"],
    "xray": ["71045", "71046"],
    "x-ray": ["71045", "71046"],
    "ultrasound": ["76805", "76856"],
    "mammogram": ["77067"],
    "mammography": ["77067"],
    "colonoscopy": ["45378", "45385"],
    "knee replacement": ["27447"],
    "hip replacement": ["27130"],
}


def _facility_profile_url(item: dict) -> str:
    ftype = (item.get("facility_type") or "hospital").strip().lower()
    state_slug = item.get("state_slug") or slugify(item.get("state") or "")
    city_slug = item.get("city_slug") or slugify(item.get("city") or "")
    slug = item.get("slug") or slugify(item.get("name") or item.get("facility_id") or "")
    if ftype == "asc":
        return f"/surgery-centers/{state_slug}/{city_slug}/{slug}/"
    if ftype == "imaging_center":
        return f"/imaging/{state_slug}/{city_slug}/{slug}/"
    return f"/hospitals/{state_slug}/{city_slug}/{slug}/"


def _search_procedures(query: str, limit: int = 5, exact_only: bool = False) -> list[dict]:
    token = (query or "").strip()
    if not token:
        return []
    like = f"%{token}%"
    with db.get_db() as conn:
        all_prices_cte = """
            WITH all_prices AS (
                SELECT cpt_code, description, gross_charge, COALESCE(facility_type, 'hospital') AS facility_type
                FROM procedure_prices
                UNION ALL
                SELECT hp.cpt_code, hp.description, hp.gross_charge, COALESCE(hp.facility_type, 'hospital') AS facility_type
                FROM hospital_prices hp
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM procedure_prices pp
                    WHERE pp.facility_id = hp.facility_id
                      AND pp.cpt_code = hp.cpt_code
                      AND COALESCE(pp.data_year, -1) = COALESCE(hp.data_year, -1)
                      AND COALESCE(pp.facility_type, 'hospital') = COALESCE(hp.facility_type, 'hospital')
                )
            )
        """
        if exact_only:
            rows = conn.execute(
                f"""
                {all_prices_cte}
                SELECT
                    ap.cpt_code,
                    MIN(ap.description) AS description,
                    AVG(CASE WHEN ap.facility_type = 'hospital' THEN ap.gross_charge END) AS hospital_avg,
                    AVG(CASE WHEN ap.facility_type = 'asc' THEN ap.gross_charge END) AS asc_avg,
                    AVG(CASE WHEN ap.facility_type = 'imaging_center' THEN ap.gross_charge END) AS imaging_avg
                FROM all_prices ap
                WHERE (
                    lower(trim(ap.cpt_code)) = lower(trim(?))
                    OR lower(trim(ap.description)) = lower(trim(?))
                )
                  AND ap.gross_charge IS NOT NULL
                  AND ap.gross_charge > 0
                  AND ap.gross_charge <= 1000000
                GROUP BY ap.cpt_code
                LIMIT ?
                """,
                (token, token, max(1, min(limit, 20))),
            ).fetchall()
        else:
            rows = conn.execute(
                f"""
                {all_prices_cte}
                SELECT
                    ap.cpt_code,
                    MIN(ap.description) AS description,
                    AVG(CASE WHEN ap.facility_type = 'hospital' THEN ap.gross_charge END) AS hospital_avg,
                    AVG(CASE WHEN ap.facility_type = 'asc' THEN ap.gross_charge END) AS asc_avg,
                    AVG(CASE WHEN ap.facility_type = 'imaging_center' THEN ap.gross_charge END) AS imaging_avg
                FROM all_prices ap
                WHERE (ap.cpt_code LIKE ? OR ap.description LIKE ?)
                  AND ap.gross_charge IS NOT NULL
                  AND ap.gross_charge > 0
                  AND ap.gross_charge <= 1000000
                GROUP BY ap.cpt_code
                ORDER BY
                    CASE
                        WHEN lower(ap.cpt_code) = lower(?) THEN 0
                        WHEN lower(ap.cpt_code) LIKE lower(?) THEN 1
                        WHEN lower(MIN(ap.description)) = lower(?) THEN 2
                        WHEN lower(MIN(ap.description)) LIKE lower(?) THEN 3
                        ELSE 4
                    END,
                    MIN(ap.description) ASC
                LIMIT ?
                """,
                (like, like, token, f"{token}%", token, f"{token}%", max(1, min(limit, 20))),
            ).fetchall()
        if not rows and not exact_only:
            keyword = token.lower()
            cpts = PROCEDURE_KEYWORD_CPTS.get(keyword)
            if not cpts:
                for k, vals in PROCEDURE_KEYWORD_CPTS.items():
                    if keyword in k:
                        cpts = vals
                        break
            if cpts:
                placeholders = ",".join("?" for _ in cpts)
                rows = conn.execute(
                    f"""
                    {all_prices_cte}
                    SELECT
                        ap.cpt_code,
                        MIN(ap.description) AS description,
                        AVG(CASE WHEN ap.facility_type = 'hospital' THEN ap.gross_charge END) AS hospital_avg,
                        AVG(CASE WHEN ap.facility_type = 'asc' THEN ap.gross_charge END) AS asc_avg,
                        AVG(CASE WHEN ap.facility_type = 'imaging_center' THEN ap.gross_charge END) AS imaging_avg
                    FROM all_prices ap
                    WHERE ap.cpt_code IN ({placeholders})
                      AND ap.gross_charge IS NOT NULL
                      AND ap.gross_charge > 0
                      AND ap.gross_charge <= 1000000
                    GROUP BY ap.cpt_code
                    ORDER BY ap.cpt_code
                    LIMIT ?
                    """,
                    tuple(cpts + [max(1, min(limit, 20))]),
                ).fetchall()
    out = []
    for row in rows:
        d = dict(row)
        d["url"] = f"/procedures/{d['cpt_code']}/"
        out.append(d)
    return out


def _search_facilities(query: str, limit: int = 4, exact_only: bool = False) -> list[dict]:
    token = (query or "").strip()
    if not token:
        return []
    like = f"%{token}%"
    with db.get_db() as conn:
        if exact_only:
            rows = conn.execute(
                """
                SELECT
                    f.facility_id,
                    f.name,
                    f.city,
                    f.state,
                    f.state_slug,
                    f.city_slug,
                    f.slug,
                    f.facility_type,
                    f.is_hospital_owned,
                    COALESCE(fbm.billing_grade, bm.billing_grade) AS billing_grade,
                    COALESCE(fbm.avg_markup, bm.avg_markup_vs_medicare) AS avg_markup
                FROM facilities f
                LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = f.facility_id
                LEFT JOIN billing_metrics bm ON bm.facility_id = f.facility_id
                WHERE lower(trim(f.name)) = lower(trim(?))
                ORDER BY f.name
                LIMIT ?
                """,
                (token, max(1, min(limit, 20))),
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT
                    f.facility_id,
                    f.name,
                    f.city,
                    f.state,
                    f.state_slug,
                    f.city_slug,
                    f.slug,
                    f.facility_type,
                    f.is_hospital_owned,
                    COALESCE(fbm.billing_grade, bm.billing_grade) AS billing_grade,
                    COALESCE(fbm.avg_markup, bm.avg_markup_vs_medicare) AS avg_markup
                FROM facilities f
                LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = f.facility_id
                LEFT JOIN billing_metrics bm ON bm.facility_id = f.facility_id
                WHERE f.name LIKE ? OR f.city LIKE ? OR f.state LIKE ? OR f.zip LIKE ?
                ORDER BY
                    CASE
                        WHEN f.zip = ? THEN 0
                        WHEN f.zip LIKE ? THEN 1
                        WHEN lower(f.name) = lower(?) THEN 0
                        WHEN lower(f.name) LIKE lower(?) THEN 2
                        ELSE 3
                    END,
                    f.name ASC
                LIMIT ?
                """,
                (
                    like,
                    like,
                    like,
                    like,
                    token,
                    f"{token}%",
                    token,
                    f"{token}%",
                    max(1, min(limit, 20)),
                ),
            ).fetchall()
    out = []
    for row in rows:
        d = dict(row)
        d["url"] = _facility_profile_url(d)
        d["facility_type_label"] = FACILITY_TYPE_LABELS.get(d.get("facility_type") or "hospital", "Facility")
        out.append(d)
    return out


def _build_home_procedure_cards() -> list[dict]:
    cards = []
    for spec in HOME_PROCEDURE_CARD_SPECS:
        secondary_type = spec.get("secondary_type") or ""
        profile = get_procedure_profile(spec["cpt_code"])
        by_type = {(r.get("facility_type") or "").strip().lower(): r for r in (profile or {}).get("ranges_by_type", [])}
        hospital = by_type.get("hospital", {})
        secondary = by_type.get(secondary_type, {})
        secondary_avg = secondary.get("avg_charge")
        secondary_markup = secondary.get("avg_markup")
        national = (profile or {}).get("header", {}).get("national_avg_charge")
        hospital_avg = hospital.get("avg_charge")
        vs_hosp = ((hospital_avg - national) / national * 100) if national and hospital_avg else None
        vs_secondary = ((secondary_avg - national) / national * 100) if national and secondary_avg else None
        cards.append(
            {
                "category": spec["category"],
                "name": (profile or {}).get("name") or spec["name"],
                "cpt_code": spec["cpt_code"],
                "hospital_avg": hospital_avg,
                "hospital_markup": hospital.get("avg_markup"),
                "secondary_type": secondary_type,
                "secondary_label": FACILITY_TYPE_LABELS.get(secondary_type, ""),
                "secondary_avg": secondary_avg,
                "secondary_markup": secondary_markup,
                "vs_hospital": vs_hosp,
                "vs_secondary": vs_secondary,
                "url": f"/procedures/{spec['cpt_code']}/",
            }
        )
    return cards


def _build_home_sample_facilities(limit: int = 6) -> list[dict]:
    with db.get_db() as conn:
        def _fetch_rows(min_procedures: int):
            return conn.execute(
                """
            SELECT
                f.facility_id, f.name, f.city, f.state, f.state_slug, f.city_slug, f.slug,
                f.facility_type, f.is_hospital_owned,
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.billing_grade
                    ELSE fbm.billing_grade
                END AS billing_grade,
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.avg_markup_vs_medicare
                    ELSE fbm.avg_markup
                END AS avg_markup,
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.procedures_compared
                    ELSE fbm.procedures_compared
                END AS procedures_compared
            FROM facilities f
            LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = f.facility_id
            LEFT JOIN billing_metrics bm ON bm.facility_id = f.facility_id
            WHERE f.facility_type IN ('hospital', 'asc', 'imaging_center')
              AND (
                (f.facility_type = 'hospital' AND bm.billing_grade IN ('A','B','C','D','F') AND bm.avg_markup_vs_medicare IS NOT NULL)
                OR
                (f.facility_type != 'hospital' AND fbm.billing_grade IN ('A','B','C','D','F') AND fbm.avg_markup IS NOT NULL)
              )
              AND (
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.avg_markup_vs_medicare
                    ELSE fbm.avg_markup
                END
              ) BETWEEN 0.5 AND 150.0
              AND (
                CASE
                    WHEN f.facility_type = 'hospital' THEN bm.procedures_compared
                    ELSE fbm.procedures_compared
                END
              ) >= ?
            ORDER BY
              CASE
                  WHEN f.facility_type = 'hospital' THEN bm.avg_markup_vs_medicare
                  ELSE fbm.avg_markup
              END DESC
            LIMIT 300
            """,
                (min_procedures,),
            ).fetchall()
        rows = _fetch_rows(20)
        if not rows:
            rows = _fetch_rows(10)
        if not rows:
            rows = _fetch_rows(5)
    items = [dict(r) for r in rows]
    for item in items:
        item["url"] = _facility_profile_url(item)
        item["facility_type_label"] = FACILITY_TYPE_LABELS.get(item.get("facility_type") or "hospital", "Facility")

    def pick(pool: list[dict], predicate) -> dict | None:
        for i, row in enumerate(pool):
            if predicate(row):
                return pool.pop(i)
        return None

    hospitals = [x for x in items if x.get("facility_type") == "hospital"]
    ascs = [x for x in items if x.get("facility_type") == "asc"]
    imaging = [x for x in items if x.get("facility_type") == "imaging_center"]
    selected: list[dict] = []

    h_good = pick(hospitals, lambda x: (x.get("billing_grade") or "") in {"A", "B", "C"})
    h_bad = pick(hospitals, lambda x: (x.get("billing_grade") or "") == "F")
    if h_good:
        selected.append(h_good)
    if h_bad:
        selected.append(h_bad)

    asc_ind = pick(ascs, lambda x: not bool(x.get("is_hospital_owned")))
    asc_owned = pick(ascs, lambda x: bool(x.get("is_hospital_owned")))
    if asc_ind:
        selected.append(asc_ind)
    if asc_owned:
        selected.append(asc_owned)

    img_ind = pick(imaging, lambda x: not bool(x.get("is_hospital_owned")))
    img_owned = pick(imaging, lambda x: bool(x.get("is_hospital_owned")))
    if img_ind:
        selected.append(img_ind)
    if img_owned:
        selected.append(img_owned)

    remaining = [*hospitals, *ascs, *imaging]
    for row in remaining:
        if len(selected) >= limit:
            break
        if row not in selected:
            selected.append(row)
    return selected[:limit]


@app.on_event("startup")
def startup():
    if config.ENV == "production":
        if config.DEBUG:
            raise RuntimeError("DEBUG must be false in production")
        if not config.SECRET_KEY or config.SECRET_KEY == "change-me-in-production":
            raise RuntimeError("SECRET_KEY must be configured in production")
        if not config.ADMIN_API_TOKEN:
            raise RuntimeError("ADMIN_API_TOKEN must be configured in production")

    db.init_db()
    if config.AUTO_BOOTSTRAP_HOSPITAL_DATA:
        from hospital_bootstrap import ensure_hospital_data_bootstrap
        ensure_hospital_data_bootstrap()
    # Seed data if database is empty
    from seed_data import seed_if_empty
    seed_if_empty()


# --- Page routes ---


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/"
    sample_facilities = _build_home_sample_facilities(6)
    procedure_cards = _build_home_procedure_cards()

    with db.get_db() as conn:
        graded_facility_count = conn.execute(
            """
            SELECT COUNT(DISTINCT facility_id) AS n
            FROM facility_billing_metrics
            WHERE facility_type IN ('hospital', 'asc', 'imaging_center')
              AND billing_grade IS NOT NULL
            """
        ).fetchone()["n"]

    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "sample_facilities": sample_facilities,
            "procedure_cards": procedure_cards,
            "graded_facility_count": graded_facility_count,
            "og_title": "BillKarma — Find Fair Procedure Costs & Check Hospital Billing Grades",
            "og_description": "Search any medical procedure to see what hospitals, surgery centers, and imaging centers charge vs. Medicare rates. Grade A-F for 6,798+ facilities. Scan your bill to catch overcharges.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/scan", response_class=HTMLResponse)
async def scan_page(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request, "outcome_stats": get_outcome_stats()})


@app.get("/confirm/{bill_id}", response_class=HTMLResponse)
async def confirm_page(request: Request, bill_id: int):
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    log_audit(action="view_confirm", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return templates.TemplateResponse("confirm.html", {"request": request, "data": results})


@app.get("/results/{bill_id}", response_class=HTMLResponse)
async def results_page(request: Request, bill_id: int):
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    log_audit(action="view_results_page", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)

    from negotiation import generate_phone_script
    phone_script = build_phone_script(bill_id) or generate_phone_script(bill_id)
    outcome_stats = get_outcome_stats()

    bill = results.get("bill") or {}
    bill_total = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0)
    fee_cents = payment_module.calculate_fee(bill_total)

    # Evidence types for this bill
    with db.get_db() as dbconn:
        evidence_rows = dbconn.execute(
            "SELECT DISTINCT evidence_type FROM evidence_uploads WHERE bill_id = ?", (bill_id,)
        ).fetchall()
    evidence_types = {r["evidence_type"] for r in evidence_rows}
    has_eob = "eob_page" in evidence_types
    has_portal = "portal_screenshot" in evidence_types

    # Case summary with win probability + confidence
    findings = results.get("findings") or []
    case_summary = compute_case_summary(findings, has_eob=has_eob, has_portal=has_portal)

    # Build evidence chips for each finding
    import json as _json
    for f in findings:
        chips = []
        evidence = {}
        try:
            evidence = _json.loads(f.get("evidence_json") or "{}") if isinstance(f.get("evidence_json"), str) else (f.get("evidence_json") or {})
        except (ValueError, TypeError):
            pass
        source = f.get("evidence_source") or evidence.get("source", "")
        anchor = evidence.get("source_anchor") or {}

        if anchor.get("line_index") is not None:
            chips.append({"type": "bill", "label": f"Bill line {anchor['line_index'] + 1}", "index": anchor["line_index"], "snippet": anchor.get("snippet", "")})
        if "medicare" in source.lower() or "cms" in source.lower():
            chips.append({"type": "bill", "label": "Medicare rate", "index": 0, "snippet": source})
        if f.get("finding_type") == "eob_reconciliation" or "eob" in source.lower():
            chips.append({"type": "eob", "label": "EOB mismatch", "index": 0, "snippet": ""})
        if "benchmark" in source.lower():
            chips.append({"type": "bill", "label": "Regional benchmark", "index": 0, "snippet": source})
        f["evidence_chips"] = chips

    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "data": results,
            "phone_script": phone_script,
            "outcome_stats": outcome_stats,
            "dispute_fee_dollars": fee_cents / 100,
            "case_summary": case_summary,
        },
    )


@app.get("/calculator", response_class=HTMLResponse)
async def calculator_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/calculator"
    return templates.TemplateResponse(
        "calculator.html",
        {
            "request": request,
            "canonical_url": canonical_url,
        },
    )


@app.get("/calculator/embed", response_class=HTMLResponse)
async def calculator_embed(
    request: Request,
    mode: str = "cost",
    cpt: str = "",
    zip: str = "",
    title: str = "",
    subtitle: str = "",
    btn_text: str = "",
    cta_text: str = "",
    cta_url: str = "",
):
    """Embeddable calculator widget for iframes in articles."""
    return templates.TemplateResponse(
        "calculator_embed.html",
        {
            "request": request,
            "mode": mode,
            "prefill_cpt": cpt,
            "prefill_zip": zip,
            "title": title,
            "subtitle": subtitle,
            "btn_text": btn_text or ("Check Markup" if mode == "markup" else "Look Up"),
            "cta_text": cta_text,
            "cta_url": cta_url,
            "base_url": "",
        },
    )


@app.get("/guides/{slug}", response_class=HTMLResponse)
async def guide_page(request: Request, slug: str):
    """Serve a guide article by slug."""
    from guides import get_guide
    guide = get_guide(slug)
    if not guide:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Guide not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/{slug}"
    return templates.TemplateResponse(
        "guide.html",
        {
            "request": request,
            "guide": guide,
            "canonical_url": canonical_url,
            "og_title": guide["title"] + " | BillKarma",
            "og_description": guide["meta_description"],
            "meta_description": guide["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/guides/", response_class=HTMLResponse)
async def guides_index(request: Request):
    """List all published guides."""
    from guides import list_guides
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/"
    return templates.TemplateResponse(
        "guides_index.html",
        {
            "request": request,
            "guides": list_guides(),
            "canonical_url": canonical_url,
            "og_title": "Medical Billing Guides | BillKarma",
            "og_description": "Free guides on how to read, dispute, and reduce medical bills.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/tools/", response_class=HTMLResponse)
async def tools_index(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/tools/"
    tools = list_tools()
    return templates.TemplateResponse(
        "tools_index.html",
        {
            "request": request,
            "tools": tools,
            "canonical_url": canonical_url,
            "og_title": "BillKarma Free Medical Billing Tools",
            "og_description": "Free calculators and generators to check billing errors, rights, and dispute options.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/tools/{slug}/", response_class=HTMLResponse)
async def tool_detail(request: Request, slug: str):
    tool = get_tool(slug)
    if not tool:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Tool not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/tools/{slug}/"
    return templates.TemplateResponse(
        "tool_page.html",
        {
            "request": request,
            "tool": tool,
            "canonical_url": canonical_url,
            "og_title": f"{tool['title']} | BillKarma",
            "og_description": tool.get("description"),
            "meta_description": tool.get("description"),
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital")
async def hospital_index_redirect():
    return RedirectResponse(url="/hospitals/", status_code=301)


@app.get("/hospitals/", response_class=HTMLResponse)
async def hospital_index_page(request: Request, q: str = ""):
    states = get_state_index_stats()
    results = find_hospitals(q) if q else []
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/"
    return templates.TemplateResponse(
        "hospitals_index.html",
        {
            "request": request,
            "states": states,
            "search_query": q,
            "search_results": results,
            "canonical_url": canonical_url,
            "og_title": "Hospital Billing Report Card Directory | BillKarma",
            "og_description": "Search US hospital billing report cards by state, city, and hospital name.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital/{state_slug}")
async def hospital_state_redirect(state_slug: str):
    return RedirectResponse(url=f"/hospitals/{state_slug}/", status_code=301)


@app.get("/hospitals/{state_slug}/", response_class=HTMLResponse)
async def hospital_state_page(
    request: Request,
    state_slug: str,
    sort: str = "grade",
    ownership: str = "",
    page: int = 1,
):
    hospitals, total = get_state_hospitals(state_slug, sort=sort, ownership=ownership, page=page)
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    cities = get_cities_for_state(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/"
    return templates.TemplateResponse(
        "hospitals_state.html",
        {
            "request": request,
            "hospitals": hospitals,
            "state_name": state_name,
            "state_slug": state_slug,
            "cities": cities,
            "sort": sort,
            "ownership": ownership,
            "page": page,
            "per_page": 50,
            "total": total,
            "canonical_url": canonical_url,
            "og_title": f"{state_name} Hospital Billing Report Cards | BillKarma",
            "og_description": f"Compare billing grades and markup ratios for hospitals in {state_name}.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospitals/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def hospital_city_page(
    request: Request,
    state_slug: str,
    city_slug: str,
    sort: str = "grade",
    page: int = 1,
):
    from hospital_seo import get_city_hospitals

    hospitals, total = get_city_hospitals(state_slug, city_slug, sort=sort, page=page)
    city_name = hospitals[0]["city"] if hospitals else city_slug.replace("-", " ").title()
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/"
    return templates.TemplateResponse(
        "hospitals_city.html",
        {
            "request": request,
            "hospitals": hospitals,
            "city_name": city_name,
            "city_slug": city_slug,
            "state_name": state_name,
            "state_slug": state_slug,
            "sort": sort,
            "page": page,
            "per_page": 50,
            "total": total,
            "canonical_url": canonical_url,
            "og_title": f"{city_name}, {state_name} Hospital Billing Comparison | BillKarma",
            "og_description": f"Compare billing grades and markup ratios across hospitals in {city_name}, {state_name}.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/hospital/{state_slug}/{hospital_slug}")
async def hospital_profile_redirect_legacy(state_slug: str, hospital_slug: str):
    from db import get_db

    with get_db() as db_conn:
        row = db_conn.execute(
            "SELECT city_slug FROM hospitals WHERE state_slug = ? AND slug = ? LIMIT 1",
            (state_slug, hospital_slug),
        ).fetchone()
    if not row:
        return RedirectResponse(url=f"/hospitals/{state_slug}/", status_code=301)
    return RedirectResponse(url=f"/hospitals/{state_slug}/{row['city_slug']}/{hospital_slug}/", status_code=301)


@app.get("/hospitals/{state_slug}/{city_slug}/{hospital_slug}/", response_class=HTMLResponse)
async def hospital_profile_page(request: Request, state_slug: str, city_slug: str, hospital_slug: str):
    canonical_slug = resolve_hospital_slug(state_slug, city_slug, hospital_slug)
    if canonical_slug and canonical_slug != hospital_slug:
        return RedirectResponse(url=f"/hospitals/{state_slug}/{city_slug}/{canonical_slug}/", status_code=301)

    profile = get_hospital_profile(state_slug, city_slug, canonical_slug or hospital_slug)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Hospital not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/{canonical_slug or hospital_slug}/"

    seo = profile["seo"]
    return templates.TemplateResponse(
        "hospitals_detail.html",
        {
            "request": request,
            "data": profile,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
            "enable_affiliate_slots": config.ENABLE_AFFILIATE_SLOTS,
            "affiliate_url": config.AFFILIATE_URL,
            "enable_hospital_claim": config.ENABLE_HOSPITAL_CLAIM,
            "claim_hospital_url": config.CLAIM_HOSPITAL_URL,
        },
    )


@app.get("/surgery-centers/", response_class=HTMLResponse)
async def surgery_centers_index(request: Request):
    states = get_facility_state_index("asc")
    stats = get_landing_stats("asc")
    return templates.TemplateResponse(
        "facilities_index.html",
        {
            "request": request,
            "states": states,
            "title": "Find Ambulatory Surgery Centers Near You",
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
            "stats": stats,
        },
    )


@app.get("/surgery-centers/{state_slug}/", response_class=HTMLResponse)
async def surgery_centers_state(request: Request, state_slug: str):
    facilities = get_facilities_in_scope("asc", state_slug=state_slug)
    return templates.TemplateResponse(
        "facilities_state.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
        },
    )


@app.get("/surgery-centers/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def surgery_centers_city(request: Request, state_slug: str, city_slug: str):
    facilities = get_facilities_in_scope("asc", state_slug=state_slug, city_slug=city_slug)
    return templates.TemplateResponse(
        "facilities_city.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "city_slug": city_slug,
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
        },
    )


@app.get("/surgery-centers/{state_slug}/{city_slug}/{slug}/", response_class=HTMLResponse)
async def surgery_centers_detail(request: Request, state_slug: str, city_slug: str, slug: str):
    data = get_facility_profile("asc", state_slug, city_slug, slug)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Facility not found"})
    return templates.TemplateResponse(
        "facilities_detail.html",
        {
            "request": request,
            "data": data,
            "label": "Ambulatory Surgery Center",
            "base_path": "/surgery-centers/",
            "canonical_url": f"{config.APP_URL.rstrip('/')}/surgery-centers/{state_slug}/{city_slug}/{slug}/",
            "meta_description": data["seo"]["meta_description"],
            "og_title": data["seo"]["page_title"],
            "og_description": data["seo"]["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/imaging/", response_class=HTMLResponse)
async def imaging_index(request: Request):
    states = get_facility_state_index("imaging_center")
    stats = get_landing_stats("imaging_center")
    return templates.TemplateResponse(
        "facilities_index.html",
        {
            "request": request,
            "states": states,
            "title": "Find Imaging Centers Near You",
            "label": "Imaging Centers",
            "base_path": "/imaging/",
            "stats": stats,
        },
    )


@app.get("/imaging/{state_slug}/", response_class=HTMLResponse)
async def imaging_state(request: Request, state_slug: str):
    facilities = get_facilities_in_scope("imaging_center", state_slug=state_slug)
    return templates.TemplateResponse(
        "facilities_state.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "label": "Imaging Centers",
            "base_path": "/imaging/",
        },
    )


@app.get("/imaging/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def imaging_city(request: Request, state_slug: str, city_slug: str):
    facilities = get_facilities_in_scope("imaging_center", state_slug=state_slug, city_slug=city_slug)
    return templates.TemplateResponse(
        "facilities_city.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "city_slug": city_slug,
            "label": "Imaging Centers",
            "base_path": "/imaging/",
        },
    )


@app.get("/imaging/{state_slug}/{city_slug}/{slug}/", response_class=HTMLResponse)
async def imaging_detail(request: Request, state_slug: str, city_slug: str, slug: str):
    data = get_facility_profile("imaging_center", state_slug, city_slug, slug)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Facility not found"})
    return templates.TemplateResponse(
        "facilities_detail.html",
        {
            "request": request,
            "data": data,
            "label": "Imaging Center",
            "base_path": "/imaging/",
            "canonical_url": f"{config.APP_URL.rstrip('/')}/imaging/{state_slug}/{city_slug}/{slug}/",
            "meta_description": data["seo"]["meta_description"],
            "og_title": data["seo"]["page_title"],
            "og_description": data["seo"]["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/procedures/", response_class=HTMLResponse)
async def procedure_index_page(request: Request):
    procedures = get_top_cpt_codes(100)
    # Group by body system
    groups: dict[str, list] = {}
    for p in procedures:
        groups.setdefault(p["body_system"], []).append(p)
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/"
    return templates.TemplateResponse(
        "procedures_index.html",
        {
            "request": request,
            "groups": groups,
            "total": len(procedures),
            "canonical_url": canonical_url,
            "og_title": "Procedure Cost Directory: Medicare Rates & Hospital Grades | BillKarma",
            "og_description": "See Medicare rates, national average charges, and billing grades for 100 common procedures. Find the best-priced hospital near you.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/procedures/{slug}-cost/", response_class=HTMLResponse)
async def procedure_content_page(request: Request, slug: str):
    data = get_content_page_data(f"{slug}-cost")
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure page not found"})
    return templates.TemplateResponse(
        "procedure_cost_guide.html",
        {
            "request": request,
            "data": data,
            "canonical_url": f"{config.APP_URL.rstrip('/')}/procedures/{slug}-cost/",
            "meta_description": data["seo"]["meta_description"],
            "og_title": data["content_heading"] + " | BillKarma",
            "og_description": data["seo"]["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/procedures/{cpt_code}/", response_class=HTMLResponse)
async def procedure_detail_page(request: Request, cpt_code: str):
    profile = get_procedure_profile(cpt_code)
    if not profile:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure not found"})
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/{cpt_code}/"
    seo = profile["seo"]
    return templates.TemplateResponse(
        "procedures_detail.html",
        {
            "request": request,
            "data": profile,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/api/procedures/{cpt_code}/hospitals")
async def procedure_hospitals_by_zip(cpt_code: str, zip: str = ""):
    """Return hospitals near a zip code with data for this CPT code (AJAX)."""
    if not zip or len(zip) < 5:
        return JSONResponse({"error": "zip required"}, status_code=400)
    results = get_hospitals_near_zip_for_cpt(cpt_code, zip)
    if not results:
        return JSONResponse({"hospitals": [], "found": False})
    return JSONResponse({"hospitals": results, "found": True})


@app.get("/api/procedures/{cpt_code}/providers")
async def procedure_providers_by_zip(
    cpt_code: str,
    zip: str = "",
    facility_type: str = "all",
    sort: str = "patient_cost",
    grade_ab_only: int = 0,
    radius_miles: int = 75,
    limit: int = 10,
):
    """Return providers near zip for this CPT code across facility types."""
    if not zip or len(zip) < 5:
        return JSONResponse({"error": "zip required"}, status_code=400)
    results = get_providers_near_zip_for_cpt(
        cpt_code=cpt_code,
        zip_code=zip,
        limit=max(1, min(limit, 50)),
        facility_type=facility_type,
        grade_ab_only=bool(int(grade_ab_only)),
        sort_by=sort,
        radius_miles=radius_miles,
    )
    if not results:
        return JSONResponse({"providers": [], "found": False})
    return JSONResponse({"providers": results, "found": True})


@app.get("/api/hospitals/search")
async def hospital_search_api(q: str = ""):
    """JSON hospital autocomplete for comparison tool."""
    results = search_hospitals_for_compare(q) if len(q.strip()) >= 2 else []
    return JSONResponse({"results": results})


@app.get("/api/providers/search")
async def provider_search_api(q: str = ""):
    """JSON autocomplete across hospitals + ASC + imaging for compare/deep links."""
    token = (q or "").strip()
    if len(token) < 2:
        return JSONResponse({"results": []})
    like = f"%{token}%"
    with db.get_db() as conn:
        rows = conn.execute(
            """
            SELECT facility_id, name, city, state, state_slug, city_slug, slug, facility_type
            FROM facilities
            WHERE name LIKE ? OR city LIKE ? OR state LIKE ?
            ORDER BY
                CASE WHEN lower(name) LIKE lower(?) THEN 0 ELSE 1 END,
                name
            LIMIT 20
            """,
            (like, like, like, f"{token.lower()}%"),
        ).fetchall()
    return JSONResponse({"results": [dict(r) for r in rows]})


@app.get("/api/procedures/search")
async def procedure_search_api(q: str = "", limit: int = 5):
    """JSON autocomplete for procedures."""
    token = (q or "").strip()
    if len(token) < 2:
        return JSONResponse({"results": []})
    results = _search_procedures(token, limit=max(1, min(limit, 10)))
    return JSONResponse({"results": results})


@app.get("/api/search/unified")
async def unified_search_api(q: str = "", procedure_limit: int = 5, facility_limit: int = 4):
    """Unified autocomplete payload: procedures + facilities + exact-match routing hints."""
    token = (q or "").strip()
    if len(token) < 2:
        return JSONResponse(
            {
                "query": token,
                "procedures": [],
                "facilities": [],
                "exact_procedure": None,
                "exact_facility": None,
                "is_zip": bool(re.fullmatch(r"\d{5}", token or "")),
            }
        )
    procedures = _search_procedures(token, limit=max(1, min(procedure_limit, 10)))
    facilities = _search_facilities(token, limit=max(1, min(facility_limit, 10)))
    exact_procedure = _search_procedures(token, limit=1, exact_only=True)
    exact_facility = _search_facilities(token, limit=1, exact_only=True)
    return JSONResponse(
        {
            "query": token,
            "procedures": procedures,
            "facilities": facilities,
            "exact_procedure": exact_procedure[0] if exact_procedure else None,
            "exact_facility": exact_facility[0] if exact_facility else None,
            "is_zip": bool(re.fullmatch(r"\d{5}", token)),
        }
    )


@app.get("/search", response_class=HTMLResponse)
async def unified_search_page(request: Request, q: str = ""):
    token = (q or "").strip()
    procedures = _search_procedures(token, limit=25) if len(token) >= 2 else []
    facilities = _search_facilities(token, limit=25) if len(token) >= 2 else []
    canonical_url = f"{config.APP_URL.rstrip('/')}/search?q={token}" if token else f"{config.APP_URL.rstrip('/')}/search"
    return templates.TemplateResponse(
        "search_results.html",
        {
            "request": request,
            "query": token,
            "procedures": procedures,
            "facilities": facilities,
            "canonical_url": canonical_url,
            "title": "Search Results | BillKarma",
            "og_title": "Search Medical Procedure and Facility Prices | BillKarma",
            "og_description": "Search procedures, hospitals, surgery centers, and imaging centers with pricing context from Medicare benchmarks.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/find/", response_class=HTMLResponse)
async def unified_find_page(request: Request, q: str = "", zip: str = "", type: str = "all"):
    token = (q or "").strip() or (zip or "").strip()
    facilities = _search_facilities(token, limit=50) if len(token) >= 2 else []
    normalized = (type or "all").strip().lower()
    if normalized in {"hospital", "asc", "imaging_center"}:
        facilities = [f for f in facilities if f.get("facility_type") == normalized]
    canonical_url = f"{config.APP_URL.rstrip('/')}/find/"
    return templates.TemplateResponse(
        "search_results.html",
        {
            "request": request,
            "query": token,
            "procedures": [],
            "facilities": facilities,
            "canonical_url": canonical_url,
            "title": "Find Facilities | BillKarma",
            "og_title": "Find Hospitals, Surgery Centers, and Imaging Centers | BillKarma",
            "og_description": "Find and compare graded facilities near you across hospitals, surgery centers, and imaging centers.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/compare/", response_class=HTMLResponse)
async def compare_index(
    request: Request,
    facility_a: str = Query("", alias="facility-a"),
    facility_b: str = Query("", alias="facility-b"),
    hospital: str = "",
):
    # Deep-link support from ASC/imaging pages.
    if facility_a and facility_b:
        return RedirectResponse(url=f"/compare/{facility_a}/vs/{facility_b}/", status_code=302)
    if hospital:
        return RedirectResponse(url=f"/compare/?facility-a={hospital}", status_code=302)
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/"
    return templates.TemplateResponse(
        "compare_index.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Hospital Comparison Tool | BillKarma",
            "og_description": "Compare any two hospitals side-by-side: billing grade, markup vs Medicare, CMS stars, and procedure prices.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/compare/{fid_a}/vs/{fid_b}/", response_class=HTMLResponse)
async def compare_detail(request: Request, fid_a: str, fid_b: str):
    data = get_comparison_data(fid_a, fid_b)
    if not data:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "One or both hospitals not found."},
        )
    name_a = data["a"]["name"]
    name_b = data["b"]["name"]
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/{fid_a}/vs/{fid_b}/"
    return templates.TemplateResponse(
        "compare_detail.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": f"{name_a} vs {name_b} | BillKarma",
            "og_description": (
                f"Compare billing grades and procedure prices: {name_a} vs {name_b}. "
                "See which hospital charges less relative to Medicare."
            ),
            "meta_robots": "index, follow",
        },
    )


@app.get("/sitemap.xml")
async def sitemap_index():
    base = config.APP_URL.rstrip("/")
    hospital_paths = get_hospital_sitemap_paths()
    core_urls = [
        (f"{base}/", "2026-02-01", "1.0"),
        (f"{base}/guides/", "2026-02-01", "0.8"),
        (f"{base}/tools/", "2026-02-01", "0.8"),
        (f"{base}/fight-debt", "2026-02-24", "0.9"),
        (f"{base}/savings", "2026-02-25", "0.8"),
        (f"{base}/shop", "2026-02-25", "0.8"),
        (f"{base}/watch", "2026-02-25", "0.7"),
        (f"{base}/sitemap-guides.xml", "2026-02-24", "0.5"),
        (f"{base}/sitemap-hospitals.xml", "2026-02-24", "0.5"),
    ]
    core_entries = "".join(
        f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>"
        for loc, lastmod, priority in core_urls
    )
    hospital_entries = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-01-01</lastmod><priority>0.5</priority></url>"
        for path in hospital_paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{core_entries}{hospital_entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-guides.xml")
async def guides_sitemap():
    from guides import get_guides_for_sitemap

    base = config.APP_URL.rstrip("/")
    static_urls = [
        (f"{base}/", "2026-02-01", "1.0"),
        (f"{base}/fight-debt", "2026-02-24", "0.9"),
        (f"{base}/collection-notice", "2026-02-24", "0.9"),
        (f"{base}/statute-of-limitations", "2026-02-24", "0.9"),
        (f"{base}/charity-care", "2026-02-24", "0.9"),
        (f"{base}/settle-debt", "2026-02-24", "0.8"),
        (f"{base}/guides/", "2026-02-01", "0.8"),
        (f"{base}/tools/", "2026-02-01", "0.8"),
        (f"{base}/calculator", "2026-02-01", "0.7"),
    ]
    static_entries = "".join(
        f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>"
        for loc, lastmod, priority in static_urls
    )
    guide_entries = "".join(
        f"<url><loc>{base}/guides/{slug}</loc><lastmod>{published}</lastmod><priority>0.8</priority></url>"
        for slug, published in get_guides_for_sitemap()
    )
    tool_entries = "".join(
        f"<url><loc>{base}/tools/{tool['slug']}/</loc><lastmod>2026-02-01</lastmod><priority>0.8</priority></url>"
        for tool in list_tools()
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{static_entries}{guide_entries}{tool_entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-hospitals.xml")
async def hospital_sitemap_v2():
    base = config.APP_URL.rstrip("/")
    core_entries = "".join(
        [
            f"<url><loc>{base}/</loc><lastmod>2026-02-01</lastmod><priority>1.0</priority></url>",
            f"<url><loc>{base}/tools/</loc><lastmod>2026-02-01</lastmod><priority>0.8</priority></url>",
        ]
    )
    tool_entries = "".join(
        f"<url><loc>{base}/tools/{tool['slug']}/</loc><lastmod>2026-02-01</lastmod><priority>0.8</priority></url>"
        for tool in list_tools()
    )
    hospital_paths = get_hospital_sitemap_paths()
    urlset = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-01-01</lastmod><priority>0.5</priority></url>"
        for path in hospital_paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{core_entries}{tool_entries}{urlset}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/hospitals/sitemap.xml")
async def hospital_sitemap_legacy():
    return RedirectResponse(url="/sitemap-hospitals.xml", status_code=301)


@app.get("/robots.txt")
async def robots_txt():
    body = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap.xml\n"
    )
    return Response(content=body, media_type="text/plain")


@app.get("/ops/data-quality")
async def ops_data_quality():
    with db.get_db() as conn:
        hospitals_total = conn.execute("SELECT COUNT(*) AS n FROM hospitals").fetchone()["n"]
        metrics_with_avg = conn.execute(
            "SELECT COUNT(*) AS n FROM billing_metrics WHERE avg_markup_vs_medicare IS NOT NULL"
        ).fetchone()["n"]
        hcahps_rows = conn.execute("SELECT COUNT(*) AS n FROM hcahps_scores").fetchone()["n"]
        hcahps_recommend_yes = conn.execute(
            "SELECT COUNT(*) AS n FROM hcahps_scores WHERE recommend_yes IS NOT NULL"
        ).fetchone()["n"]
        transparency_parsed = conn.execute(
            "SELECT COUNT(*) AS n FROM transparency_files WHERE parse_status IN ('parsed', 'partial')"
        ).fetchone()["n"]
        prices_rows = conn.execute("SELECT COUNT(*) AS n FROM hospital_prices").fetchone()["n"]
        grade_rows = conn.execute(
            """
            SELECT billing_grade, COUNT(*) AS n
            FROM billing_metrics
            GROUP BY billing_grade
            """
        ).fetchall()
        markup_rows = conn.execute(
            """
            SELECT avg_markup_vs_medicare
            FROM billing_metrics
            WHERE avg_markup_vs_medicare IS NOT NULL
            ORDER BY avg_markup_vs_medicare
            """
        ).fetchall()
        refreshes = conn.execute(
            """
            SELECT source, MAX(refresh_date) AS last_refresh
            FROM data_refresh_log
            GROUP BY source
            ORDER BY source
            """
        ).fetchall()

    markups = [r["avg_markup_vs_medicare"] for r in markup_rows]
    def _quantile(p: float) -> float | None:
        if not markups:
            return None
        idx = int((len(markups) - 1) * p)
        return float(markups[idx])

    payload = {
        "hospitals_total": hospitals_total,
        "metrics_with_avg": metrics_with_avg,
        "metrics_coverage_pct": round((metrics_with_avg / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "hcahps_rows": hcahps_rows,
        "hcahps_recommend_yes": hcahps_recommend_yes,
        "hcahps_recommend_coverage_pct": round((hcahps_recommend_yes / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "transparency_parsed": transparency_parsed,
        "transparency_parsed_pct": round((transparency_parsed / hospitals_total * 100), 2) if hospitals_total else 0.0,
        "hospital_prices_rows": prices_rows,
        "grade_distribution": {r["billing_grade"]: r["n"] for r in grade_rows},
        "markup_quantiles": {
            "p50": _quantile(0.50),
            "p75": _quantile(0.75),
            "p90": _quantile(0.90),
            "p95": _quantile(0.95),
        },
        "last_refresh_by_source": {r["source"]: r["last_refresh"] for r in refreshes},
    }
    return JSONResponse(payload)


@app.get("/dispute/activate/{bill_id}", response_class=HTMLResponse)
async def dispute_activate_page(request: Request, bill_id: int):
    """Show the dispute activation page with e-sign + payment flow."""
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})

    bill = results.get("bill") or {}
    findings = results.get("findings") or []
    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)
    bill_total = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0)
    fee_cents = payment_module.calculate_fee(bill_total)

    return templates.TemplateResponse(
        "dispute_activate.html",
        {
            "request": request,
            "bill_id": bill_id,
            "provider_name": bill.get("provider_name") or "",
            "potential_savings": total_savings,
            "finding_count": len(findings),
            "fee_dollars": fee_cents / 100,
            "hipaa_text": esign_module.get_hipaa_text(
                patient_name="[Your Name]",
                provider_name=bill.get("provider_name") or "the provider",
            ),
            "rep_text": esign_module.get_rep_designation_text(
                patient_name="[Your Name]",
                provider_name=bill.get("provider_name") or "the provider",
            ),
            "tos_text": esign_module.get_tos_text(),
        },
    )


@app.get("/dispute/payment-success", response_class=HTMLResponse)
async def dispute_payment_success(request: Request, session_id: str = ""):
    """Post-payment success page. JS activates the dispute."""
    return templates.TemplateResponse(
        "payment_success.html",
        {
            "request": request,
            "session_id": session_id,
        },
    )


@app.get("/dispute/dashboard", response_class=HTMLResponse)
async def dispute_dashboard_page(
    request: Request,
    case: int = 0,
    bill: int = 0,
):
    """Show dispute status dashboard for a case or bill."""
    summary: dict = {"has_case": False}

    if case:
        require_case_access(request, case)
        case_data = dispute_service.get_case(case)
        if case_data:
            summary = dispute_service.get_dispute_summary(case_data["bill_id"])
    elif bill:
        require_bill_access(request, bill)
        summary = dispute_service.get_dispute_summary(bill)

    return templates.TemplateResponse(
        "dispute_dashboard.html",
        {
            "request": request,
            "summary": summary,
        },
    )


# --- Debt Fighter pages ---


@app.get("/fight-debt", response_class=HTMLResponse)
async def fight_debt_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/fight-debt"
    return templates.TemplateResponse(
        "fight_debt.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Fight Your Medical Debt | BillKarma",
            "og_description": "Got a medical bill or collection notice? Generate FDCPA letters, check charity care eligibility, and negotiate settlements.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/statute-of-limitations", response_class=HTMLResponse)
async def sol_page(request: Request):
    from debt_fighter import SOL_BY_STATE, STATE_NAMES
    states = [{"code": k, "name": STATE_NAMES[k]} for k in sorted(STATE_NAMES.keys())]
    canonical_url = f"{config.APP_URL.rstrip('/')}/statute-of-limitations"
    return templates.TemplateResponse(
        "statute_of_limitations.html",
        {
            "request": request,
            "states": states,
            "canonical_url": canonical_url,
            "og_title": "Medical Debt Statute of Limitations Calculator | BillKarma",
            "og_description": "Check if your medical debt is past the statute of limitations in your state. Free calculator.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/collection-notice", response_class=HTMLResponse)
async def collection_notice_page(request: Request):
    from debt_fighter import STATE_NAMES
    states = [{"code": k, "name": STATE_NAMES[k]} for k in sorted(STATE_NAMES.keys())]
    canonical_url = f"{config.APP_URL.rstrip('/')}/collection-notice"
    return templates.TemplateResponse(
        "collection_notice.html",
        {
            "request": request,
            "states": states,
            "canonical_url": canonical_url,
            "og_title": "Fight Your Collection Notice — FDCPA Letter Generator | BillKarma",
            "og_description": "Generate a legally correct FDCPA debt validation letter and mail it certified. Takes 10 minutes.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/charity-care", response_class=HTMLResponse)
async def charity_care_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/charity-care"
    return templates.TemplateResponse(
        "charity_care_eligibility.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Do You Qualify for Hospital Charity Care? | BillKarma",
            "og_description": "IRS law requires nonprofit hospitals to forgive or reduce bills for patients who can't afford them. Check if you qualify — free.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/charity-care/hospital", response_class=HTMLResponse)
async def charity_care_hospital_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/charity-care/hospital"
    return templates.TemplateResponse(
        "charity_care_hospital.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Find Your Hospital's Financial Assistance Program | BillKarma",
            "og_description": "Search our hospital database to see if your hospital is nonprofit and find their financial assistance application.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/charity-care/apply", response_class=HTMLResponse)
async def charity_care_apply_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/charity-care/apply"
    return templates.TemplateResponse(
        "charity_care_apply.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Generate Your Charity Care Application Packet | BillKarma",
            "og_description": "Generate a cover letter and document checklist for your hospital financial assistance application.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/charity-care/send-success", response_class=HTMLResponse)
async def charity_care_send_success_page(request: Request):
    return templates.TemplateResponse("charity_care_send_success.html", {"request": request})


@app.get("/collection-notice/send-success", response_class=HTMLResponse)
async def collection_notice_send_success_page(request: Request):
    return templates.TemplateResponse("collection_notice_send_success.html", {"request": request})


@app.get("/settle-debt", response_class=HTMLResponse)
async def settle_debt_page(request: Request):
    from debt_fighter import STATE_NAMES
    states = [{"code": k, "name": STATE_NAMES[k]} for k in sorted(STATE_NAMES.keys())]
    canonical_url = f"{config.APP_URL.rstrip('/')}/settle-debt"
    return templates.TemplateResponse(
        "settle_debt.html",
        {
            "request": request,
            "states": states,
            "canonical_url": canonical_url,
            "og_title": "Negotiate a Medical Debt Settlement | BillKarma",
            "og_description": "Generate a settlement offer letter for medical debt. Collectors often accept 20-40% of the balance.",
            "meta_robots": "index, follow",
        },
    )


# --- Bill Health Score ---


@app.get("/score/{bill_id}", response_class=HTMLResponse)
async def bill_score_page(request: Request, bill_id: int):
    """Show the Bill Health Score for a scanned bill."""
    require_bill_access(request, bill_id)
    from bill_score import compute_bill_score
    score = compute_bill_score(bill_id)
    if not score:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"})
    share_url = f"{config.APP_URL.rstrip('/')}/score/share/{score['share_token']}"
    return templates.TemplateResponse(
        "bill_score.html",
        {
            "request": request,
            "score": score,
            "share_url": share_url,
            "is_public": False,
            "og_title": f"Bill Health Score: {score['score']}/100 — Grade {score['grade']} | BillKarma",
            "og_description": f"This medical bill scored {score['score']}/100 with {score['finding_count']} issue(s) and ${score['potential_savings']:,.0f} in potential savings.",
            "meta_robots": "noindex",
        },
    )


@app.get("/score/share/{share_token}", response_class=HTMLResponse)
async def bill_score_public(request: Request, share_token: str):
    """Public shareable Bill Health Score page."""
    from bill_score import get_score_by_token
    score = get_score_by_token(share_token)
    if not score:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Score not found"})
    share_url = f"{config.APP_URL.rstrip('/')}/score/share/{share_token}"
    return templates.TemplateResponse(
        "bill_score.html",
        {
            "request": request,
            "score": score,
            "share_url": share_url,
            "is_public": True,
            "canonical_url": share_url,
            "og_title": f"Bill Health Score: {score['score']}/100 — Grade {score['grade']} | BillKarma",
            "og_description": f"This medical bill scored {score['score']}/100 with ${score['potential_savings']:,.0f} in potential overcharges found.",
            "meta_robots": "index, follow",
        },
    )


# --- Community Savings Feed ---


@app.get("/savings", response_class=HTMLResponse)
async def savings_feed_page(request: Request):
    """Community savings feed showing anonymized recent savings."""
    from savings_feed import get_recent_savings, get_aggregate_stats
    feed = get_recent_savings(30)
    stats = get_aggregate_stats()
    canonical_url = f"{config.APP_URL.rstrip('/')}/savings"
    return templates.TemplateResponse(
        "savings_feed.html",
        {
            "request": request,
            "feed": feed,
            "stats": stats,
            "canonical_url": canonical_url,
            "og_title": "Community Savings Feed | BillKarma",
            "og_description": f"BillKarma users have found ${stats.get('total_savings_found', 0):,.0f} in billing errors. See real-time savings.",
            "meta_robots": "index, follow",
        },
    )


# --- Pre-Care Price Shopper ---


@app.get("/shop", response_class=HTMLResponse)
async def price_shopper_page(
    request: Request,
    cpt: str = "",
    zip: str = "",
    sort: str = "price",
    radius: int = 50,
    type: str = "all",
):
    """Pre-care price shopper — find cheapest providers for a procedure."""
    from price_shopper import shop_for_procedure
    data = {"procedure": None, "providers": [], "savings_opportunity": None}
    if cpt and zip:
        data = shop_for_procedure(
            cpt_code=cpt.strip(),
            zip_code=zip.strip(),
            radius_miles=max(10, min(radius, 200)),
            facility_type=type,
            sort_by=sort,
        )
    proc_name = (data.get("procedure") or {}).get("name") or "Medical Procedure"
    zip_city = (data.get("zip_center") or {}).get("city") or ""
    zip_state = (data.get("zip_center") or {}).get("state") or ""
    canonical_url = f"{config.APP_URL.rstrip('/')}/shop"
    return templates.TemplateResponse(
        "price_shopper.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": f"Find Best Price for {proc_name} | BillKarma" if cpt else "Pre-Care Price Shopper | BillKarma",
            "og_description": f"Compare prices for {proc_name} near {zip_city}, {zip_state}. Find the cheapest provider." if cpt else "Compare procedure prices across hospitals, surgery centers, and imaging centers before scheduling.",
            "meta_robots": "index, follow",
        },
    )


# --- Bill Watch / Price Alerts ---


@app.get("/watch", response_class=HTMLResponse)
async def bill_watch_page(request: Request):
    """Price watch subscription page."""
    canonical_url = f"{config.APP_URL.rstrip('/')}/watch"
    return templates.TemplateResponse(
        "bill_watch.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Price Watch — Get Hospital Pricing Alerts | BillKarma",
            "og_description": "Set alerts for hospitals, procedures, or ZIP codes. Get notified when pricing data changes.",
            "meta_robots": "index, follow",
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)
