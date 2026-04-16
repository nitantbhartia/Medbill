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
from advocacy_api import router as advocacy_router
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
from compare_pages import build_comparison_seo, get_comparison_data, search_hospitals_for_compare
from dispute_workflow import build_phone_script, get_outcome_stats
from facility_pages import get_facility_profile, get_facilities_in_scope, get_facility_sitemap_paths, get_facility_state_index, get_landing_stats
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
app.include_router(advocacy_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def security_headers(request: Request, call_next):
    # Force HTTPS — proxy (Railway/Render) sets X-Forwarded-Proto
    if not config.DEBUG:
        proto = request.headers.get("x-forwarded-proto", "https")
        if proto == "http":
            https_url = str(request.url).replace("http://", "https://", 1)
            return RedirectResponse(url=https_url, status_code=301)

    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    if not request.url.path.startswith("/embed/"):
        response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    if not config.DEBUG:
        response.headers.setdefault("Strict-Transport-Security", "max-age=63072000; includeSubDomains; preload")
    # Propagate noindex from template to X-Robots-Tag header so crawlers see it
    # even before rendering — pick it up from the meta_robots context value if set
    return response

templates = Jinja2Templates(directory="templates")
templates.env.globals["config"] = config


def _clean_fid(value):
    """Strip trailing .0 from facility IDs rendered in URLs."""
    s = str(value or "")
    if s.endswith(".0") and s[:-2].isdigit():
        return s[:-2]
    return s


templates.env.filters["clean_fid"] = _clean_fid

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


# ── Advocacy Workspace pages ─────────────────────────────────────────────────

@app.get("/advocacy/login", response_class=HTMLResponse)
async def advocacy_login_page(request: Request):
    return templates.TemplateResponse("advocacy_login.html", {"request": request})


@app.get("/advocacy/setup", response_class=HTMLResponse)
async def advocacy_setup_page(request: Request):
    return templates.TemplateResponse("advocacy_setup.html", {"request": request})


@app.get("/advocacy/dashboard", response_class=HTMLResponse)
async def advocacy_dashboard_page(request: Request):
    return templates.TemplateResponse("advocacy_dashboard.html", {"request": request})


@app.get("/advocacy/cases", response_class=HTMLResponse)
async def advocacy_cases_page(request: Request):
    return templates.TemplateResponse("advocacy_cases.html", {"request": request})


@app.get("/advocacy/cases/new", response_class=HTMLResponse)
async def advocacy_new_case_page(request: Request):
    return templates.TemplateResponse("advocacy_new_case.html", {"request": request})


@app.get("/advocacy/cases/{case_id}", response_class=HTMLResponse)
async def advocacy_case_detail_page(request: Request, case_id: int):
    return templates.TemplateResponse("advocacy_case_detail.html", {"request": request, "case_id": case_id})


@app.get("/advocacy/team", response_class=HTMLResponse)
async def advocacy_team_page(request: Request):
    return templates.TemplateResponse("advocacy_team.html", {"request": request})


@app.get("/advocacy/shared/{token}", response_class=HTMLResponse)
async def advocacy_shared_case_page(request: Request, token: str):
    return templates.TemplateResponse("advocacy_shared_case.html", {"request": request, "share_token": token})


@app.get("/scan", response_class=HTMLResponse)
async def scan_page(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request, "outcome_stats": get_outcome_stats()})


@app.get("/confirm/{bill_id}", response_class=HTMLResponse)
async def confirm_page(request: Request, bill_id: int):
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"}, status_code=404)
    log_audit(action="view_confirm", resource_type="bill", resource_id=str(bill_id), bill_id=bill_id)
    return templates.TemplateResponse("confirm.html", {"request": request, "data": results, "meta_robots": "noindex, nofollow"})


@app.get("/results/{bill_id}", response_class=HTMLResponse)
async def results_page(request: Request, bill_id: int):
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"}, status_code=404)
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
            "meta_robots": "noindex, nofollow",
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


def _extract_howto_schema(guide: dict) -> str | None:
    """Build HowTo JSON-LD for any guide with a numbered step sequence (3+ steps)."""
    import re, json, html as html_mod
    title = guide.get("title", "")
    body = guide.get("body", "")

    # Find the largest <ol> block — prefer sections with "step" or "how" context
    ol_blocks = re.findall(r'<ol[^>]*>(.*?)</ol>', body, re.DOTALL)
    if not ol_blocks:
        return None
    # Pick the block with the most <li> items
    best_block = max(ol_blocks, key=lambda b: len(re.findall(r'<li', b)))
    items = re.findall(r'<li[^>]*>(.*?)</li>', best_block, re.DOTALL)
    if len(items) < 3:
        return None

    steps = []
    for i, item in enumerate(items[:12], 1):
        # Try to get name from <strong> tag first, fall back to plain text
        strong = re.search(r'<strong[^>]*>(.*?)</strong>', item, re.DOTALL)
        name_raw = strong.group(1) if strong else item
        name = html_mod.unescape(re.sub(r'<[^>]+>', '', name_raw).strip())[:80]
        text = html_mod.unescape(re.sub(r'<[^>]+>', '', item).strip())[:250]
        if not text or len(text) < 10:
            continue
        steps.append({
            "@type": "HowToStep",
            "position": i,
            "name": name or text[:60],
            "text": text,
        })
    if len(steps) < 3:
        return None

    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": title,
        "description": guide.get("meta_description", ""),
        "step": steps,
    }
    return json.dumps(schema)


@app.get("/guides/{slug}", response_class=RedirectResponse)
async def guide_page_redirect(slug: str):
    """Redirect no-slash guide URLs to canonical trailing-slash version."""
    return RedirectResponse(url=f"/guides/{slug}/", status_code=301)


@app.get("/guides/{slug}/", response_class=HTMLResponse)
async def guide_page(request: Request, slug: str):
    """Serve a guide article by slug."""
    import re
    from guides import get_guide, get_related_guides, inject_internal_links, inject_scan_cta
    guide = get_guide(slug)
    if not guide:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Guide not found"}, status_code=404)
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/{slug}/"
    word_count = len(re.sub(r"<[^>]+>", "", guide["body"]).split())
    reading_time = max(1, round(word_count / 250))
    linked_body = inject_scan_cta(inject_internal_links(guide["body"], slug))
    return templates.TemplateResponse(
        "guide.html",
        {
            "request": request,
            "guide": {**guide, "body": linked_body},
            "canonical_url": canonical_url,
            "og_title": guide["title"] + " | BillKarma",
            "og_description": guide["meta_description"],
            "meta_description": guide["meta_description"],
            "meta_robots": "index, follow",
            "related_guides": get_related_guides(slug),
            "reading_time": reading_time,
            "howto_schema": _extract_howto_schema({**guide, "slug": slug}),
        },
    )


@app.get("/guides/", response_class=HTMLResponse)
async def guides_index(request: Request):
    """List all published guides."""
    from guides import list_guides, get_all_categories
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/"
    return templates.TemplateResponse(
        "guides_index.html",
        {
            "request": request,
            "guides": list_guides(),
            "all_categories": get_all_categories(),
            "canonical_url": canonical_url,
            "og_title": "Medical Billing Guides | BillKarma",
            "og_description": "Free guides on how to read, dispute, and reduce medical bills.",
            "meta_robots": "index, follow",
        },
    )


_CATEGORY_META = {
    "procedure-costs": {
        "icon": "🏥",
        "intro": "Medical procedures can cost anywhere from a few hundred to tens of thousands of dollars depending on where you go. Our procedure cost guides break down what hospitals actually charge, what Medicare pays, and how to find fair prices before you book.",
        "stat": {"value": "4.2x", "label": "average hospital markup over Medicare"},
        "faqs": [
            {"question": "Why do hospitals charge so much more than Medicare rates?", "answer": "Hospitals set their own chargemaster prices, which can be 3–10x the Medicare-approved rate. Medicare rates represent what the government considers fair payment. The difference is negotiable — and BillKarma helps you do exactly that."},
            {"question": "How do I find out what a procedure costs before I have it?", "answer": "Under the Hospital Price Transparency Rule (effective 2021), hospitals must publish their prices online. BillKarma aggregates this data so you can compare costs across providers before you schedule."},
            {"question": "Can I negotiate a medical bill after the fact?", "answer": "Yes — most hospitals will negotiate. Ask for an itemized bill, compare it to Medicare rates, and request a reduction. Hospital billing departments expect negotiation, especially for self-pay or high-deductible patients."},
            {"question": "What is the Medicare rate and why does it matter?", "answer": "The Medicare rate is what the federal government pays for a procedure. It's the closest thing to a 'fair market price' for medical care. Anything above 2–3x Medicare is worth questioning."},
        ],
    },
    "state-guides": {
        "icon": "🗺️",
        "intro": "Your state determines much of what protections you have against surprise billing, aggressive debt collection, and unaffordable hospital charges. These state-by-state guides explain your specific rights and what to do when hospitals don't follow the rules.",
        "stat": {"value": "51", "label": "states covered"},
        "faqs": [
            {"question": "Do state laws protect me from surprise medical bills?", "answer": "The federal No Surprises Act (2022) covers most out-of-network situations, but many states have additional protections. Some states cap what providers can charge, require more charity care, or limit medical debt collection."},
            {"question": "What state has the best medical billing protections?", "answer": "California, New York, and Colorado consistently rank highest for patient billing protections, with strong charity care laws, low statute of limitations on medical debt, and robust surprise billing rules."},
            {"question": "Can a hospital sue me for an unpaid medical bill?", "answer": "Yes, but the statute of limitations varies by state — from 2 years (some states) to 10+ years. Many states also prohibit wage garnishment for medical debt. Check your state's guide for specifics."},
        ],
    },
    "insurance-coverage": {
        "icon": "📋",
        "intro": "Health insurance is designed to protect you — but the fine print often works against you. These guides decode the jargon, explain your rights when insurers deny coverage, and show you how to fight back when you're wrongly billed.",
        "stat": {"value": "30%", "label": "of insurance denials are overturned on appeal"},
        "faqs": [
            {"question": "What can I do if my insurance denies a claim?", "answer": "You have the right to appeal any denial. First request the denial reason in writing, then file an internal appeal with your insurer. If that fails, request an external review — an independent organization reviews the denial. Roughly 30% of externally appealed denials are reversed."},
            {"question": "Am I protected from surprise out-of-network bills?", "answer": "The federal No Surprises Act protects you from surprise out-of-network bills for emergency care and from certain providers at in-network facilities (like anesthesiologists). Your cost share is limited to in-network amounts."},
            {"question": "What is prior authorization and when is it required?", "answer": "Prior authorization is approval your insurer requires before you receive certain services. If you skip it, your claim may be denied. Always verify auth requirements before elective procedures, specialty visits, or high-cost imaging."},
        ],
    },
    "insurance-basics": {
        "icon": "📘",
        "intro": "Health insurance has its own language — deductibles, copays, coinsurance, networks — and misunderstanding one term can cost you thousands. These guides explain every concept in plain English so you can choose the right plan and use it wisely.",
        "stat": {"value": "60%", "label": "of patients don't understand their EOB"},
        "faqs": [
            {"question": "What is the difference between a deductible and an out-of-pocket maximum?", "answer": "Your deductible is what you pay before insurance kicks in. Your out-of-pocket maximum is the most you'll pay in a year — after that, insurance covers 100%. Premiums don't count toward either."},
            {"question": "What does coinsurance mean?", "answer": "Coinsurance is your share of costs after you've met your deductible, expressed as a percentage. If your coinsurance is 20% and a procedure costs $1,000, you pay $200 and insurance pays $800."},
            {"question": "Is an HMO or PPO better?", "answer": "HMOs generally have lower premiums but require referrals and restrict you to a network. PPOs cost more but give flexibility to see any provider. If you have a preferred specialist or travel frequently, a PPO may be worth the higher premium."},
        ],
    },
    "understanding-your-bill": {
        "icon": "🧾",
        "intro": "Medical bills are among the most confusing documents Americans receive. Studies show 1 in 5 contains errors. These guides teach you to read an itemized bill, spot overcharges, and understand the codes that determine what you owe.",
        "stat": {"value": "1 in 5", "label": "medical bills contains an error"},
        "faqs": [
            {"question": "How do I get an itemized medical bill?", "answer": "You have the legal right to an itemized bill. Call the hospital billing department and request one specifically — the summary bill you receive by default doesn't show individual charges. Review each line item and CPT code."},
            {"question": "What are CPT codes?", "answer": "CPT (Current Procedural Terminology) codes are 5-digit numbers that identify every medical service. Each code has a Medicare-set price. If you're billed for a CPT code you don't recognize, look it up — you may have been charged for a service you didn't receive."},
            {"question": "What is upcoding?", "answer": "Upcoding is when a provider bills for a more expensive service than was actually performed. For example, billing a Level 5 ER visit when only a Level 3 was warranted. It's one of the most common billing errors and is worth disputing."},
        ],
    },
    "appeals-disputes": {
        "icon": "⚖️",
        "intro": "Disputing a medical bill or insurance denial feels overwhelming — but the process is more straightforward than you think. These guides walk you through every step, from writing a dispute letter to requesting an external review.",
        "stat": {"value": "40%", "label": "of disputed bills are reduced or eliminated"},
        "faqs": [
            {"question": "How do I dispute a medical bill?", "answer": "Start by getting an itemized bill and comparing each charge to the Medicare rate. For errors, write a formal dispute letter to the billing department citing the specific codes and discrepancies. Follow up in writing and keep copies of everything."},
            {"question": "How long do I have to dispute a medical bill?", "answer": "There's no federal deadline for disputing billing errors, but do it quickly — ideally within 30–60 days of receiving the bill. Your insurer typically has 30-day deadlines for claim appeals from the date of denial."},
            {"question": "Can I dispute a bill that's already in collections?", "answer": "Yes. Under the Fair Debt Collection Practices Act, you can request debt validation within 30 days of first contact from a collector. You can also dispute billing errors with the original provider even after the account has been sent to collections."},
        ],
    },
    "medical-debt": {
        "icon": "💳",
        "intro": "Medical debt is the leading cause of personal bankruptcy in the US. But it's also one of the most negotiable forms of debt — with options ranging from payment plans to charity care to debt settlement. These guides show you every path out.",
        "stat": {"value": "#1", "label": "cause of US personal bankruptcy"},
        "faqs": [
            {"question": "Does medical debt affect my credit score?", "answer": "Medical debt under $500 is excluded from credit reports (as of 2023). The three major bureaus now remove paid medical collections immediately. Unpaid medical debt over $500 can still appear after 1 year, but new rules have significantly reduced medical debt's credit impact."},
            {"question": "Can a hospital sue me over unpaid medical debt?", "answer": "Yes, but this is rare for smaller debts. Hospitals more commonly sell debt to collectors. You have legal rights under the FDCPA, and many states have additional protections against wage garnishment for medical debt."},
            {"question": "What is a medical debt settlement?", "answer": "You negotiate to pay less than the full balance — often 20–60 cents on the dollar for older debt. Hospitals and collection agencies expect this. Offer a lump sum payment and get any agreement in writing before paying."},
        ],
    },
    "negotiating-bills": {
        "icon": "🤝",
        "intro": "Every medical bill is negotiable. Hospital billing departments have discretion to reduce charges, set up payment plans, and apply discounts — but they almost never volunteer it. These guides give you the scripts and strategies to get a lower bill.",
        "stat": {"value": "35%", "label": "average reduction when patients negotiate"},
        "faqs": [
            {"question": "Is it really possible to negotiate a hospital bill?", "answer": "Yes — hospital billing staff expect negotiation, especially from self-pay patients or those with high deductibles. Hospitals typically accept 30–60% of billed charges from commercial payers, so there's significant room to negotiate."},
            {"question": "What's the best negotiation strategy for a medical bill?", "answer": "Get an itemized bill, look up Medicare rates for each CPT code, and offer to pay 1.5–2x the Medicare rate as a lump sum. Be polite but persistent. Ask specifically for the 'prompt pay discount' or 'self-pay rate.'"},
            {"question": "Should I hire a medical billing advocate?", "answer": "For bills over $5,000, a professional advocate often pays for themselves — they typically charge 20–35% of savings achieved. For smaller bills, use BillKarma's free guides and dispute tools first."},
        ],
    },
    "financial-assistance": {
        "icon": "🏦",
        "intro": "Nonprofit hospitals are required by the IRS to offer charity care programs, but most don't advertise them. Many patients who qualify never apply. These guides show you how to access hospital financial assistance, Medicaid, and other programs.",
        "stat": {"value": "$42B", "label": "in charity care provided annually"},
        "faqs": [
            {"question": "What is hospital charity care?", "answer": "Nonprofit hospitals must provide free or discounted care to low-income patients to maintain their tax-exempt status. Income eligibility typically ranges from 200% to 400% of the federal poverty level, depending on the hospital."},
            {"question": "How do I apply for hospital financial assistance?", "answer": "Ask the billing department for a 'financial assistance application' or 'charity care application.' You'll typically need to provide income documentation (pay stubs, tax returns) and proof of expenses. Apply before the bill goes to collections."},
            {"question": "Can I get financial assistance if I have insurance?", "answer": "Yes — many hospitals offer assistance for the portion not covered by insurance, especially for patients with high deductibles or copays. Don't assume having insurance disqualifies you."},
        ],
    },
    "patient-rights": {
        "icon": "🛡️",
        "intro": "Patients have more legal rights than most realize — from the right to an itemized bill, to protections against balance billing, to the right to appeal any insurance denial. These guides document exactly what you're entitled to under federal and state law.",
        "stat": {"value": "80%", "label": "of patients don't know their full billing rights"},
        "faqs": [
            {"question": "What are my rights under the No Surprises Act?", "answer": "The No Surprises Act (2022) protects you from unexpected out-of-network bills for emergency care and from certain providers at in-network facilities. Your cost share can't exceed your in-network rate. Disputes go to independent arbitration."},
            {"question": "Do I have the right to see my medical records?", "answer": "Yes — under HIPAA, you have the right to access your medical records within 30 days of request. Providers can charge a reasonable copying fee but cannot deny access. Electronic records must be provided electronically if requested."},
            {"question": "Can a hospital discharge me while I'm still sick?", "answer": "You have the right to appeal a discharge decision before leaving the hospital. If Medicare-insured, request a written 'Notice of Medicare Non-Coverage' and appeal to your Quality Improvement Organization (QIO) — the discharge is paused during review."},
        ],
    },
    "prior-authorization": {
        "icon": "📝",
        "intro": "Prior authorization — the requirement to get insurer approval before receiving care — causes treatment delays and denials that harm patients. These guides explain when auth is required, how to get it approved, and what to do when it's denied.",
        "stat": {"value": "93%", "label": "of physicians say prior auth delays necessary care"},
        "faqs": [
            {"question": "What is prior authorization?", "answer": "Prior authorization (PA) is your insurer's requirement to approve certain procedures, medications, or specialist visits before you receive them. Without approval, the claim may be denied. PAs are most common for specialty drugs, imaging, surgery, and mental health services."},
            {"question": "How long does prior authorization take?", "answer": "Standard PA requests must be decided within 15 days under federal rules (or 72 hours for urgent cases). Many states have faster requirements. If your insurer takes longer, escalate to your HR department or state insurance commissioner."},
            {"question": "What do I do if prior authorization is denied?", "answer": "Request the specific denial reason and clinical criteria in writing. Your doctor can submit a peer-to-peer review (doctor calls the insurer's medical director directly) — this reverses roughly 50% of denials. If that fails, file a formal appeal."},
        ],
    },
}

_CITY_DATA = {
    "new-york": {"name": "New York", "state": "NY", "zip": "10001", "state_slug": "new-york"},
    "los-angeles": {"name": "Los Angeles", "state": "CA", "zip": "90001", "state_slug": "california"},
    "chicago": {"name": "Chicago", "state": "IL", "zip": "60601", "state_slug": "illinois"},
    "houston": {"name": "Houston", "state": "TX", "zip": "77001", "state_slug": "texas"},
    "phoenix": {"name": "Phoenix", "state": "AZ", "zip": "85001", "state_slug": "arizona"},
    "philadelphia": {"name": "Philadelphia", "state": "PA", "zip": "19101", "state_slug": "pennsylvania"},
    "san-antonio": {"name": "San Antonio", "state": "TX", "zip": "78201", "state_slug": "texas"},
    "san-diego": {"name": "San Diego", "state": "CA", "zip": "92101", "state_slug": "california"},
    "dallas": {"name": "Dallas", "state": "TX", "zip": "75201", "state_slug": "texas"},
    "san-jose": {"name": "San Jose", "state": "CA", "zip": "95101", "state_slug": "california"},
    "austin": {"name": "Austin", "state": "TX", "zip": "78701", "state_slug": "texas"},
    "jacksonville": {"name": "Jacksonville", "state": "FL", "zip": "32099", "state_slug": "florida"},
    "fort-worth": {"name": "Fort Worth", "state": "TX", "zip": "76101", "state_slug": "texas"},
    "columbus": {"name": "Columbus", "state": "OH", "zip": "43085", "state_slug": "ohio"},
    "charlotte": {"name": "Charlotte", "state": "NC", "zip": "28201", "state_slug": "north-carolina"},
    "indianapolis": {"name": "Indianapolis", "state": "IN", "zip": "46201", "state_slug": "indiana"},
    "san-francisco": {"name": "San Francisco", "state": "CA", "zip": "94102", "state_slug": "california"},
    "seattle": {"name": "Seattle", "state": "WA", "zip": "98101", "state_slug": "washington"},
    "denver": {"name": "Denver", "state": "CO", "zip": "80201", "state_slug": "colorado"},
    "nashville": {"name": "Nashville", "state": "TN", "zip": "37201", "state_slug": "tennessee"},
    "oklahoma-city": {"name": "Oklahoma City", "state": "OK", "zip": "73101", "state_slug": "oklahoma"},
    "el-paso": {"name": "El Paso", "state": "TX", "zip": "79901", "state_slug": "texas"},
    "washington-dc": {"name": "Washington", "state": "DC", "zip": "20001", "state_slug": "district-of-columbia"},
    "las-vegas": {"name": "Las Vegas", "state": "NV", "zip": "89101", "state_slug": "nevada"},
    "louisville": {"name": "Louisville", "state": "KY", "zip": "40201", "state_slug": "kentucky"},
    "memphis": {"name": "Memphis", "state": "TN", "zip": "38101", "state_slug": "tennessee"},
    "portland": {"name": "Portland", "state": "OR", "zip": "97201", "state_slug": "oregon"},
    "baltimore": {"name": "Baltimore", "state": "MD", "zip": "21201", "state_slug": "maryland"},
    "milwaukee": {"name": "Milwaukee", "state": "WI", "zip": "53201", "state_slug": "wisconsin"},
    "albuquerque": {"name": "Albuquerque", "state": "NM", "zip": "87101", "state_slug": "new-mexico"},
    "tucson": {"name": "Tucson", "state": "AZ", "zip": "85701", "state_slug": "arizona"},
    "fresno": {"name": "Fresno", "state": "CA", "zip": "93701", "state_slug": "california"},
    "mesa": {"name": "Mesa", "state": "AZ", "zip": "85201", "state_slug": "arizona"},
    "sacramento": {"name": "Sacramento", "state": "CA", "zip": "95814", "state_slug": "california"},
    "atlanta": {"name": "Atlanta", "state": "GA", "zip": "30301", "state_slug": "georgia"},
    "kansas-city": {"name": "Kansas City", "state": "MO", "zip": "64101", "state_slug": "missouri"},
    "omaha": {"name": "Omaha", "state": "NE", "zip": "68101", "state_slug": "nebraska"},
    "raleigh": {"name": "Raleigh", "state": "NC", "zip": "27601", "state_slug": "north-carolina"},
    "miami": {"name": "Miami", "state": "FL", "zip": "33101", "state_slug": "florida"},
    "minneapolis": {"name": "Minneapolis", "state": "MN", "zip": "55401", "state_slug": "minnesota"},
    "cleveland": {"name": "Cleveland", "state": "OH", "zip": "44101", "state_slug": "ohio"},
    "wichita": {"name": "Wichita", "state": "KS", "zip": "67201", "state_slug": "kansas"},
    "tampa": {"name": "Tampa", "state": "FL", "zip": "33601", "state_slug": "florida"},
    "new-orleans": {"name": "New Orleans", "state": "LA", "zip": "70112", "state_slug": "louisiana"},
    "pittsburgh": {"name": "Pittsburgh", "state": "PA", "zip": "15201", "state_slug": "pennsylvania"},
    "cincinnati": {"name": "Cincinnati", "state": "OH", "zip": "45201", "state_slug": "ohio"},
    "st-louis": {"name": "St. Louis", "state": "MO", "zip": "63101", "state_slug": "missouri"},
    "richmond": {"name": "Richmond", "state": "VA", "zip": "23218", "state_slug": "virginia"},
    "orlando": {"name": "Orlando", "state": "FL", "zip": "32801", "state_slug": "florida"},
    "boston": {"name": "Boston", "state": "MA", "zip": "02101", "state_slug": "massachusetts"},
}

_PROCEDURE_SLUGS = {
    "knee-replacement": {"cpt": "27447", "name": "Knee Replacement"},
    "hip-replacement": {"cpt": "27130", "name": "Hip Replacement"},
    "colonoscopy": {"cpt": "45378", "name": "Colonoscopy"},
    "appendectomy": {"cpt": "44970", "name": "Appendectomy"},
    "mri-brain": {"cpt": "70551", "name": "MRI of the Brain"},
    "ct-abdomen": {"cpt": "74177", "name": "CT Scan Abdomen/Pelvis"},
    "mammogram": {"cpt": "77067", "name": "Mammogram (Screening)"},
    "cataract-surgery": {"cpt": "66984", "name": "Cataract Surgery"},
    "gallbladder-removal": {"cpt": "47562", "name": "Gallbladder Removal"},
    "spinal-fusion": {"cpt": "22612", "name": "Spinal Fusion"},
    "hernia-repair": {"cpt": "49505", "name": "Hernia Repair"},
    "tonsillectomy": {"cpt": "42821", "name": "Tonsillectomy"},
    "echocardiogram": {"cpt": "93306", "name": "Echocardiogram"},
    "sleep-study": {"cpt": "95810", "name": "Sleep Study"},
    "basic-metabolic-panel": {"cpt": "80048", "name": "Basic Metabolic Panel"},
    "er-visit": {"cpt": "99284", "name": "ER Visit (Level 4)"},
}

# CMS Medicare facility rates (2026) + national average hospital charges.
# Source: CMS Physician Fee Schedule and OPPS data (public).
# avg_charge = national chargemaster average across reporting hospitals (approx 4-6x Medicare).
_CPT_STATIC_RATES: dict[str, dict] = {
    "27447": {"medicare_rate": 1916, "avg_charge": 30500, "description": "Total Knee Replacement"},
    "27130": {"medicare_rate": 1975, "avg_charge": 32000, "description": "Total Hip Replacement"},
    "45378": {"medicare_rate": 341,  "avg_charge": 3100,  "description": "Colonoscopy (diagnostic)"},
    "44970": {"medicare_rate": 629,  "avg_charge": 22500, "description": "Laparoscopic Appendectomy"},
    "70551": {"medicare_rate": 278,  "avg_charge": 2400,  "description": "MRI Brain without contrast"},
    "74177": {"medicare_rate": 294,  "avg_charge": 5200,  "description": "CT Abdomen/Pelvis with contrast"},
    "77067": {"medicare_rate": 133,  "avg_charge": 620,   "description": "Bilateral Screening Mammogram"},
    "66984": {"medicare_rate": 661,  "avg_charge": 4200,  "description": "Cataract Surgery with IOL"},
    "47562": {"medicare_rate": 576,  "avg_charge": 16000, "description": "Laparoscopic Cholecystectomy"},
    "22612": {"medicare_rate": 2418, "avg_charge": 62000, "description": "Lumbar Spinal Fusion"},
    "49505": {"medicare_rate": 408,  "avg_charge": 11500, "description": "Open Inguinal Hernia Repair"},
    "42821": {"medicare_rate": 286,  "avg_charge": 8200,  "description": "Tonsillectomy/Adenoidectomy"},
    "93306": {"medicare_rate": 264,  "avg_charge": 2100,  "description": "Echocardiogram with Doppler"},
    "95810": {"medicare_rate": 376,  "avg_charge": 3800,  "description": "Polysomnography (Sleep Study)"},
    "80048": {"medicare_rate": 12,   "avg_charge": 225,   "description": "Basic Metabolic Panel (BMP)"},
    "99284": {"medicare_rate": 181,  "avg_charge": 2800,  "description": "Emergency Dept Visit Level 4"},
}

# State-level cost multipliers derived from CMS Geographic Adjustment Factors.
# Applied to national average charge to estimate local costs.
_STATE_COST_MULTIPLIER: dict[str, float] = {
    "CA": 1.22, "NY": 1.25, "MA": 1.20, "CT": 1.18, "NJ": 1.20, "HI": 1.25, "WA": 1.15,
    "IL": 1.10, "PA": 1.08, "MD": 1.12, "VA": 1.08, "CO": 1.10, "MN": 1.05, "OR": 1.08,
    "TX": 1.00, "FL": 1.00, "OH": 0.98, "MI": 0.98, "GA": 0.97, "NC": 0.96, "WI": 0.97,
    "AZ": 1.00, "NV": 1.02, "DC": 1.28, "AK": 1.22,
    "AL": 0.90, "AR": 0.88, "ID": 0.90, "IN": 0.93, "IA": 0.91, "KS": 0.91,
    "KY": 0.91, "LA": 0.92, "ME": 0.93, "MS": 0.87, "MO": 0.93, "MT": 0.90,
    "NE": 0.92, "NH": 0.96, "NM": 0.92, "ND": 0.91, "OK": 0.89, "SC": 0.92,
    "SD": 0.90, "TN": 0.92, "UT": 0.95, "VT": 0.96, "WV": 0.89, "WY": 0.91,
}


def _get_static_procedure_profile(cpt_code: str, state_abbr: str) -> dict:
    """Return Medicare rate + adjusted average charge when DB has no data."""
    ref = _CPT_STATIC_RATES.get(cpt_code)
    if not ref:
        return {}
    multiplier = _STATE_COST_MULTIPLIER.get(state_abbr.upper(), 1.0)
    avg_charge = round(ref["avg_charge"] * multiplier)
    medicare_rate = ref["medicare_rate"]
    return {
        "avg_charge": avg_charge,
        "medicare_rate": medicare_rate,
        "markup_ratio": round(avg_charge / medicare_rate, 1) if medicare_rate else None,
        "hospital_count": None,
        "description": ref["description"],
        "data_source": "cms_static",
    }


# ── State data derived from _CITY_DATA ──────────────────────────────────────

def _build_state_data() -> dict:
    states: dict = {}
    name_fixes = {"district-of-columbia": "District of Columbia", "new-mexico": "New Mexico",
                  "new-york": "New York", "north-carolina": "North Carolina"}
    for city_slug, city in _CITY_DATA.items():
        s = city["state_slug"]
        if s not in states:
            states[s] = {
                "name": name_fixes.get(s, s.replace("-", " ").title()),
                "abbr": city["state"],
                "state_slug": s,
                "cities": [],
            }
        states[s]["cities"].append({"slug": city_slug, **city})
    return states


_STATE_DATA = _build_state_data()


def _procedure_city_costs(cpt_code: str) -> list[dict]:
    """Return per-city cost estimates for a procedure, sorted cheapest first."""
    ref = _CPT_STATIC_RATES.get(cpt_code)
    if not ref:
        return []
    rows = []
    for city_slug, city in _CITY_DATA.items():
        m = _STATE_COST_MULTIPLIER.get(city["state"], 1.0)
        charge = round(ref["avg_charge"] * m)
        rows.append({
            "slug": city_slug,
            "name": city["name"],
            "state": city["state"],
            "state_slug": city["state_slug"],
            "avg_charge": charge,
            "medicare_rate": ref["medicare_rate"],
            "markup_ratio": round(charge / ref["medicare_rate"], 1),
        })
    rows.sort(key=lambda r: r["avg_charge"])
    return rows


@app.get("/guides/category/{slug}/", response_class=HTMLResponse)
async def guides_category(request: Request, slug: str):
    """List guides in a specific category."""
    from guides import get_guides_by_category, get_all_categories
    guides_in_cat = get_guides_by_category(slug)
    all_cats = get_all_categories()
    matched = next((c for c in all_cats if c["slug"] == slug), None)
    if not matched or not guides_in_cat:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Category not found"}, status_code=404)
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/category/{slug}/"
    category_meta = _CATEGORY_META.get(slug)
    return templates.TemplateResponse(
        "guides_category.html",
        {
            "request": request,
            "category": matched,
            "guides": guides_in_cat,
            "all_categories": all_cats,
            "canonical_url": canonical_url,
            "og_title": f"{matched['name']} Guides | BillKarma",
            "meta_description": f"BillKarma's {matched['name'].lower()} guides — {matched['count']} free articles on how to understand, dispute, and reduce your medical bills.",
            "category_meta": category_meta,
        },
    )


@app.get("/procedures/", response_class=HTMLResponse)
async def procedures_index(request: Request):
    """Index of all procedure cost hub pages."""
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/"
    procs = [
        {
            "slug": slug,
            "name": info["name"],
            "cpt": info["cpt"],
            "medicare_rate": _CPT_STATIC_RATES.get(info["cpt"], {}).get("medicare_rate"),
            "avg_charge": _CPT_STATIC_RATES.get(info["cpt"], {}).get("avg_charge"),
        }
        for slug, info in _PROCEDURE_SLUGS.items()
    ]
    procs.sort(key=lambda p: p["name"])
    return templates.TemplateResponse("procedures_index.html", {
        "request": request,
        "procedures": procs,
        "canonical_url": canonical_url,
        "og_title": "Hospital Procedure Cost Guide | BillKarma",
        "meta_description": "Compare what hospitals charge vs Medicare rates for 16 common procedures. Free data for every major US city.",
    })


@app.get("/procedures/{slug}/", response_class=HTMLResponse)
async def procedure_hub(request: Request, slug: str):
    """National procedure cost hub — aggregates all city + state data."""
    proc = _PROCEDURE_SLUGS.get(slug)
    if not proc:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure not found"}, status_code=404)
    ref = _CPT_STATIC_RATES.get(proc["cpt"], {})
    city_costs = _procedure_city_costs(proc["cpt"])
    # State-level summary: average the city costs within each state
    state_map: dict = {}
    for c in city_costs:
        s = c["state_slug"]
        state_map.setdefault(s, {"charges": [], "state": c["state"]})
        state_map[s]["charges"].append(c["avg_charge"])
    state_costs = sorted(
        [
            {
                "state_slug": s,
                "state_name": _STATE_DATA[s]["name"] if s in _STATE_DATA else s.replace("-", " ").title(),
                "state": v["state"],
                "avg_charge": round(sum(v["charges"]) / len(v["charges"])),
                "medicare_rate": ref.get("medicare_rate"),
            }
            for s, v in state_map.items()
        ],
        key=lambda x: x["avg_charge"],
    )
    national_avg = ref.get("avg_charge", 0)
    medicare_rate = ref.get("medicare_rate", 0)
    canonical_url = f"{config.APP_URL.rstrip('/')}/procedures/{slug}/"
    meta_description = (
        f"{proc['name']} cost: national average ${national_avg:,}, Medicare rate ${medicare_rate:,}. "
        f"Compare prices by city and state. Find fair prices with BillKarma."
    )
    related_procedures = [{"slug": k, "name": v["name"]} for k, v in _PROCEDURE_SLUGS.items() if k != slug]
    return templates.TemplateResponse("procedure_hub.html", {
        "request": request,
        "procedure": {"slug": slug, "name": proc["name"], "cpt_code": proc["cpt"]},
        "ref": ref,
        "city_costs": city_costs,
        "state_costs": state_costs,
        "related_procedures": related_procedures,
        "canonical_url": canonical_url,
        "og_title": f"{proc['name']} Cost: What Hospitals Charge vs Medicare | BillKarma",
        "meta_description": meta_description,
    })


@app.get("/costs/{proc_slug}/{location_slug}/", response_class=HTMLResponse)
async def procedure_location_page(request: Request, proc_slug: str, location_slug: str):
    """Procedure cost page — handles both city slugs and state slugs."""
    proc = _PROCEDURE_SLUGS.get(proc_slug)
    if not proc:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Page not found"}, status_code=404)

    # City takes priority (handles new-york → NYC)
    city = _CITY_DATA.get(location_slug)
    if city:
        canonical_url = f"{config.APP_URL.rstrip('/')}/costs/{proc_slug}/{location_slug}/"
        profile = get_procedure_profile(proc["cpt"]) or _get_static_procedure_profile(proc["cpt"], city["state"])
        hospitals = get_hospitals_near_zip_for_cpt(proc["cpt"], city["zip"], limit=10)
        nearby_procedures = [{"name": v["name"], "slug": k, "cpt": v["cpt"]} for k, v in _PROCEDURE_SLUGS.items() if k != proc_slug][:8]
        nearby_cities = [{"name": v["name"], "state": v["state"], "slug": k} for k, v in _CITY_DATA.items() if k != location_slug][:10]
        avg_charge = profile.get("avg_charge") if profile else None
        medicare_rate = profile.get("medicare_rate") if profile else None
        avg_str = f"${avg_charge:,.0f}" if avg_charge else "varies"
        meta_description = (
            f"{proc['name']} cost in {city['name']}, {city['state']}: average {avg_str}. "
            f"Compare prices vs Medicare rate ${medicare_rate:,.0f}. Find fair prices with BillKarma."
            if medicare_rate else
            f"{proc['name']} cost in {city['name']}, {city['state']}. Compare hospital prices with BillKarma."
        )
        return templates.TemplateResponse("procedure_city.html", {
            "request": request,
            "procedure": {"name": proc["name"], "cpt_code": proc["cpt"], "slug": proc_slug},
            "city": city, "profile": profile or {}, "hospitals": hospitals,
            "canonical_url": canonical_url,
            "og_title": f"{proc['name']} Cost in {city['name']}, {city['state']} | BillKarma",
            "meta_description": meta_description, "meta_robots": "index, follow",
            "nearby_procedures": nearby_procedures, "nearby_cities": nearby_cities,
        })

    # State page
    state = _STATE_DATA.get(location_slug)
    if not state:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Page not found"}, status_code=404)
    ref = _CPT_STATIC_RATES.get(proc["cpt"], {})
    multiplier = _STATE_COST_MULTIPLIER.get(state["abbr"], 1.0)
    state_avg = round(ref.get("avg_charge", 0) * multiplier)
    medicare_rate = ref.get("medicare_rate", 0)
    city_costs = [
        {
            "slug": c["slug"], "name": c["name"], "state": c["state"],
            "avg_charge": round(ref.get("avg_charge", 0) * multiplier),
            "medicare_rate": medicare_rate,
            "markup_ratio": round((ref.get("avg_charge", 0) * multiplier) / medicare_rate, 1) if medicare_rate else None,
        }
        for c in state["cities"]
    ]
    canonical_url = f"{config.APP_URL.rstrip('/')}/costs/{proc_slug}/{location_slug}/"
    meta_description = (
        f"{proc['name']} cost in {state['name']}: average ${state_avg:,} vs Medicare rate ${medicare_rate:,}. "
        f"Compare prices across {len(city_costs)} cities. Find fair prices with BillKarma."
    )
    return templates.TemplateResponse("procedure_state.html", {
        "request": request,
        "procedure": {"slug": proc_slug, "name": proc["name"], "cpt_code": proc["cpt"]},
        "state": state, "state_avg": state_avg, "medicare_rate": medicare_rate,
        "markup_ratio": round(state_avg / medicare_rate, 1) if medicare_rate else None,
        "city_costs": city_costs,
        "national_avg": ref.get("avg_charge", 0),
        "canonical_url": canonical_url,
        "og_title": f"{proc['name']} Cost in {state['name']} | BillKarma",
        "meta_description": meta_description, "meta_robots": "index, follow",
        "nearby_procedures": [{"name": v["name"], "slug": k} for k, v in _PROCEDURE_SLUGS.items() if k != proc_slug][:8],
    })


@app.get("/guides/cheapest-cities-{proc_slug}-2026/", response_class=HTMLResponse)
async def cheapest_cities_guide(request: Request, proc_slug: str):
    """Data-driven guide: cheapest and most expensive cities for a given procedure."""
    proc = _PROCEDURE_SLUGS.get(proc_slug)
    if not proc:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure not found"}, status_code=404)
    ref = _CPT_STATIC_RATES.get(proc["cpt"], {})
    city_costs = _procedure_city_costs(proc["cpt"])  # already sorted cheapest→most expensive
    cheapest = city_costs[:10]
    most_expensive = list(reversed(city_costs[-10:]))
    savings = most_expensive[0]["avg_charge"] - cheapest[0]["avg_charge"] if city_costs else 0
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/cheapest-cities-{proc_slug}-2026/"
    title = f"Cheapest Cities for {proc['name']} in 2026"
    meta_description = (
        f"The cheapest city for {proc['name']} averages ${cheapest[0]['avg_charge']:,} vs ${most_expensive[0]['avg_charge']:,} "
        f"in the most expensive — a ${savings:,} difference. See all 50 cities ranked by cost."
    ) if city_costs else f"Compare {proc['name']} costs across 50 US cities."
    return templates.TemplateResponse("cheapest_cities_guide.html", {
        "request": request,
        "procedure": {"slug": proc_slug, "name": proc["name"], "cpt_code": proc["cpt"]},
        "ref": ref,
        "cheapest": cheapest,
        "most_expensive": most_expensive,
        "all_cities": city_costs,
        "savings": savings,
        "canonical_url": canonical_url,
        "og_title": f"{title} | BillKarma",
        "meta_description": meta_description,
        "other_procedures": [{"slug": k, "name": v["name"]} for k, v in _PROCEDURE_SLUGS.items() if k != proc_slug],
    })


@app.get("/guides/most-expensive-states-healthcare-2026/", response_class=HTMLResponse)
async def state_cost_comparison_guide(request: Request):
    """Data journalism: all US states ranked by healthcare cost index."""
    # Build state rankings using average multiplier across all tracked procedures
    # Use knee replacement (27447) as representative anchor — largest ticket item
    anchor_cpt = "27447"
    anchor_ref = _CPT_STATIC_RATES.get(anchor_cpt, {})
    anchor_nat = anchor_ref.get("avg_charge", 30500)
    states = []
    for abbr, mult in sorted(_STATE_COST_MULTIPLIER.items(), key=lambda x: -x[1]):
        # Find state name from _STATE_DATA
        state_name = next(
            (v["name"] for v in _STATE_DATA.values() if v["abbr"] == abbr),
            abbr
        )
        state_slug = next(
            (k for k, v in _STATE_DATA.items() if v["abbr"] == abbr),
            abbr.lower()
        )
        states.append({
            "abbr": abbr,
            "name": state_name,
            "slug": state_slug,
            "multiplier": mult,
            "knee_avg": round(anchor_nat * mult),
            "vs_national_pct": round((mult - 1.0) * 100),
        })
    national_avg = anchor_nat
    canonical_url = f"{config.APP_URL.rstrip('/')}/guides/most-expensive-states-healthcare-2026/"
    meta_description = (
        f"DC, NY, CA, and MA have the highest hospital costs — up to 28% above the national average. "
        f"MS and WV are the cheapest, 13% below average. Full state-by-state ranking for 2026."
    )
    return templates.TemplateResponse("state_cost_comparison.html", {
        "request": request,
        "states": states,
        "national_avg": national_avg,
        "anchor_procedure": "Knee Replacement",
        "canonical_url": canonical_url,
        "og_title": "Most Expensive States for Healthcare in 2026 | BillKarma",
        "meta_description": meta_description,
        "procedures": [{"slug": k, "name": v["name"]} for k, v in _PROCEDURE_SLUGS.items()],
    })


@app.get("/press/", response_class=HTMLResponse)
async def press_page(request: Request):
    """Press and media kit page."""
    from guides import list_guides
    canonical_url = f"{config.APP_URL.rstrip('/')}/press/"
    guide_count = len(list_guides())
    stats = {
        "hospitals_tracked": 6000,
        "guides_published": guide_count,
        "avg_markup": 4.2,
        "states_covered": 51,
        "data_year": "2026",
    }
    return templates.TemplateResponse(
        "press.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Press & Research | BillKarma",
            "meta_description": "Data, research assets, and media contact for journalists covering US hospital pricing, medical billing errors, and patient rights.",
            "stats": stats,
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


@app.get("/chargemaster/", response_class=HTMLResponse)
async def chargemaster_page(request: Request):
    """Hospital chargemaster database — what hospitals charge vs actual cost."""
    canonical_url = f"{config.APP_URL.rstrip('/')}/chargemaster/"
    return templates.TemplateResponse("chargemaster.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "Hospital Chargemaster Database: What Your Hospital Charges for Tylenol | BillKarma",
        "meta_description": "Search 6,800+ hospitals to see what they charge for common items like Tylenol, saline bags, and gauze — vs. what they actually cost. The markups will shock you.",
        "meta_robots": "index, follow",
    })


@app.get("/tools/{slug}/", response_class=HTMLResponse)
async def tool_detail(request: Request, slug: str):
    tool = get_tool(slug)
    if not tool:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Tool not found"}, status_code=404)
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


# Extra SOL context: (partial_payment_resets, contract_type, garnish_note)
_SOL_EXTRA = {
    "AL": (True,  "Written contract", "25% of disposable income"),
    "AK": (True,  "Written contract", "25% of disposable income"),
    "AZ": (True,  "Written contract", "25% of disposable income"),
    "AR": (True,  "Written contract", "25% of disposable income"),
    "CA": (True,  "Written contract", "25% of disposable income; 180-day collections delay"),
    "CO": (True,  "Written contract", "25% of disposable income"),
    "CT": (True,  "Written contract", "25% of disposable income; facility fee ban"),
    "DE": (True,  "Written contract", "15% of disposable income — lower than most states"),
    "FL": (True,  "Written contract", "Wages exempt for heads of household"),
    "GA": (True,  "Written contract", "25% of disposable income"),
    "HI": (True,  "Written contract", "Only 5% of disposable income — best in US"),
    "ID": (True,  "Written contract", "25% of disposable income"),
    "IL": (True,  "Written contract", "15% of disposable income"),
    "IN": (True,  "Written contract", "25% of disposable income"),
    "IA": (True,  "Written contract", "25% of disposable income"),
    "KS": (True,  "Written contract", "25% of disposable income"),
    "KY": (True,  "Written contract", "25% of disposable income"),
    "LA": (True,  "Prescriptive period", "25% of disposable income"),
    "ME": (True,  "Written contract", "25% of disposable income"),
    "MD": (True,  "Written contract", "25% of disposable income; all-payer rate system"),
    "MA": (True,  "Written contract", "25% of disposable income"),
    "MI": (True,  "Written contract", "25% of disposable income"),
    "MN": (True,  "Written contract", "25% of disposable income"),
    "MS": (True,  "Written contract", "25% of disposable income"),
    "MO": (True,  "Written contract", "25% of disposable income"),
    "MT": (True,  "Written contract", "25% of disposable income"),
    "NE": (True,  "Written contract", "25% of disposable income"),
    "NV": (True,  "Written contract", "25% of disposable income"),
    "NH": (True,  "Written contract", "25% of disposable income"),
    "NJ": (True,  "Written contract", "Only 10% of disposable income"),
    "NM": (True,  "Written contract", "25% of disposable income; credit report ban"),
    "NY": (True,  "Written contract", "Only 10% of disposable income; 180-day protection"),
    "NC": (True,  "Written contract", "NO wage garnishment for consumer debt — huge win"),
    "ND": (True,  "Written contract", "25% of disposable income"),
    "OH": (True,  "Written contract", "25% of disposable income"),
    "OK": (True,  "Written contract", "25% of disposable income"),
    "OR": (True,  "Written contract", "25% of disposable income; free patient advocates"),
    "PA": (True,  "Written contract", "NO wage garnishment for most consumer debt"),
    "RI": (True,  "Written contract", "25% of disposable income"),
    "SC": (True,  "Written contract", "25% of disposable income"),
    "SD": (True,  "Written contract", "20% of disposable income"),
    "TN": (True,  "Written contract", "25% of disposable income"),
    "TX": (True,  "Written contract", "NO wage garnishment for most consumer debt"),
    "UT": (True,  "Written contract", "25% of disposable income"),
    "VT": (True,  "Written contract", "15% of disposable income"),
    "VA": (True,  "Written contract", "25% of disposable income"),
    "WA": (True,  "Written contract", "25% of disposable income; BBPA strongest surprise billing law"),
    "WV": (True,  "Written contract", "20% of disposable income"),
    "WI": (True,  "Written contract", "20% of disposable income"),
    "WY": (True,  "Written contract", "25% of disposable income"),
    "DC": (True,  "Written contract", "25% of disposable income"),
}

_SOL_DATA = {
    "AL": (6, "AL Code § 6-2-34"), "AK": (3, "AS § 09.10.053"),
    "AZ": (6, "ARS § 12-548"), "AR": (5, "Ark. Code § 16-56-111"),
    "CA": (4, "CCP § 337"), "CO": (6, "CRS § 13-80-103.5"),
    "CT": (6, "CGS § 52-576"), "DE": (3, "10 Del. C. § 8106"),
    "FL": (5, "Fla. Stat. § 95.11"), "GA": (6, "OCGA § 9-3-24"),
    "HI": (6, "HRS § 657-1"), "ID": (5, "Idaho Code § 5-216"),
    "IL": (5, "735 ILCS 5/13-206"), "IN": (6, "IC 34-11-2-9"),
    "IA": (5, "Iowa Code § 614.1"), "KS": (5, "KSA § 60-512"),
    "KY": (5, "KRS § 413.120"), "LA": (3, "LA Civ. Code Art. 3494"),
    "ME": (6, "14 MRS § 752"), "MD": (3, "Md. Code § 5-101"),
    "MA": (6, "MGL c. 260 § 2"), "MI": (6, "MCL § 600.5807"),
    "MN": (6, "Minn. Stat. § 541.05"), "MS": (3, "Miss. Code § 15-1-29"),
    "MO": (5, "RSMo § 516.120"), "MT": (8, "MCA § 27-2-202"),
    "NE": (5, "Neb. Rev. Stat. § 25-205"), "NV": (6, "NRS § 11.190"),
    "NH": (3, "RSA 508:4"), "NJ": (6, "NJSA 2A:14-1"),
    "NM": (6, "NMSA § 37-1-3"), "NY": (6, "CPLR § 213"),
    "NC": (3, "NCGS § 1-52"), "ND": (6, "NDCC § 28-01-16"),
    "OH": (6, "ORC § 2305.07"), "OK": (5, "12 Okla. Stat. § 95"),
    "OR": (6, "ORS § 12.080"), "PA": (4, "42 Pa.C.S. § 5525"),
    "RI": (10, "RIGL § 9-1-13"), "SC": (3, "SC Code § 15-3-530"),
    "SD": (6, "SDCL § 15-2-13"), "TN": (6, "TCA § 28-3-109"),
    "TX": (4, "Tex. Civ. Prac. § 16.004"), "UT": (6, "UCA § 78B-2-309"),
    "VT": (6, "12 VSA § 511"), "VA": (5, "Va. Code § 8.01-246"),
    "WA": (6, "RCW 4.16.040"), "WV": (10, "WV Code § 55-2-6"),
    "WI": (6, "Wis. Stat. § 893.43"), "WY": (8, "Wyo. Stat. § 1-3-105"),
    "DC": (3, "DC Code § 12-301"),
}

_STATE_NAMES = {
    "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California",
    "CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia",
    "HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas",
    "KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts",
    "MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana",
    "NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico",
    "NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma",
    "OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina",
    "SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont",
    "VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin",
    "WY":"Wyoming","DC":"Washington D.C.",
}

_FPL_BASE = 15650   # 2026 federal poverty level, 1 person
_FPL_ADD  =  5380   # each additional person

# State billing protection scores for the interactive map
# Score 0-100 based on: Medicaid expansion, surprise billing law, charity care FPL, debt protections, garnishment
_STATE_SCORES = {
    "AL": {"score": 22, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "No Medicaid expansion. Voluntary charity care. Few state protections beyond federal law."},
    "AK": {"score": 38, "grade": "D", "medicaid": True, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 3, "garnish": "25%", "highlight": "Medicaid expanded but no state surprise billing law. Highest healthcare costs in the US."},
    "AZ": {"score": 44, "grade": "D+", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded. Limited state billing protections beyond federal baseline."},
    "AR": {"score": 46, "grade": "C-", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "ARHOME Medicaid expansion. ACE Act adds some debt collection limits."},
    "CA": {"score": 95, "grade": "A+", "medicaid": True, "surprise": "Strong (AB 72)", "charity_fpl": "350%", "sol": 4, "garnish": "25%", "highlight": "Best patient protections in the US. AB 1020 free care to 250% FPL, discounts to 350%. 180-day billing delay before collections."},
    "CO": {"score": 72, "grade": "B+", "medicaid": True, "surprise": "Strong", "charity_fpl": "250%", "sol": 6, "garnish": "25%", "highlight": "Strong Medicaid and surprise billing protections. Charity care up to 250% FPL."},
    "CT": {"score": 78, "grade": "A-", "medicaid": True, "surprise": "Strong", "charity_fpl": "300%", "sol": 6, "garnish": "25%", "highlight": "Charity care up to 300% FPL. Bans facility fees at hospital-owned offices. Strong consumer protections."},
    "DE": {"score": 65, "grade": "B", "medicaid": True, "surprise": "SB 125", "charity_fpl": "~200%", "sol": 3, "garnish": "15%", "highlight": "Lower garnishment limit (15%) than most states. Medicaid expanded. SB 125 surprise billing protections."},
    "FL": {"score": 30, "grade": "D-", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 5, "garnish": "Exempt*", "highlight": "Did not expand Medicaid. No state surprise billing law. Voluntary charity care only. Head-of-household wage garnishment exemption."},
    "GA": {"score": 28, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 6, "garnish": "25%", "highlight": "Did not fully expand Medicaid (limited waiver). Voluntary charity care. Weak state protections."},
    "HI": {"score": 88, "grade": "A", "medicaid": True, "surprise": "HRS 432E", "charity_fpl": "~200%", "sol": 6, "garnish": "5%", "highlight": "Near-universal coverage via employer mandate (Prepaid Health Care Act). Very low garnishment limit (5%). Medicaid expanded."},
    "ID": {"score": 42, "grade": "D+", "medicaid": True, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 5, "garnish": "25%", "highlight": "Expanded Medicaid in 2020. No state surprise billing law. Voluntary charity care."},
    "IL": {"score": 82, "grade": "A-", "medicaid": True, "surprise": "Strong", "charity_fpl": "600%", "sol": 5, "garnish": "15%", "highlight": "Most generous charity care law in the US — free care up to 600% FPL. Lower garnishment limit. Strong surprise billing law."},
    "IN": {"score": 48, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "HB 1004 bans certain facility fees. Medicaid expanded (HIP 2.0). Limited state surprise billing protections."},
    "IA": {"score": 55, "grade": "C+", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "Medicaid expanded. Iowa Consumer Credit Code provides some debt protections. No state surprise billing law."},
    "KS": {"score": 25, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 5, "garnish": "25%", "highlight": "Did not expand Medicaid. Voluntary charity care. Few state protections."},
    "KY": {"score": 60, "grade": "B-", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "Full Medicaid expansion via kynect (1.6M enrolled). No state surprise billing law. KRS 311.372 charity care."},
    "LA": {"score": 52, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 3, "garnish": "25%", "highlight": "Medicaid expanded. Charity hospital legacy system. Short 3-year SOL (Louisiana uses prescriptive periods)."},
    "ME": {"score": 62, "grade": "B-", "medicaid": True, "surprise": "LD 1472", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded in 2019. LD 1472 surprise billing protections. DHHS charity care rules."},
    "MD": {"score": 70, "grade": "B+", "medicaid": True, "surprise": "Strong", "charity_fpl": "300%", "sol": 3, "garnish": "25%", "highlight": "Charity care to 300% FPL. Strong surprise billing law. All-payer rate setting system keeps hospital prices lower."},
    "MA": {"score": 85, "grade": "A", "medicaid": True, "surprise": "Strong (Ch. 288)", "charity_fpl": "400%", "sol": 6, "garnish": "25%", "highlight": "Near-universal coverage since 2006. Charity care up to 400% FPL. Strong surprise billing protections."},
    "MI": {"score": 58, "grade": "C+", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded (Healthy Michigan). No state surprise billing law. Federal NSA applies."},
    "MN": {"score": 75, "grade": "A-", "medicaid": True, "surprise": "62Q.556", "charity_fpl": "300%", "sol": 6, "garnish": "25%", "highlight": "Charity care up to 300% FPL. Strong surprise billing law (62Q.556). Medical Assistance (Medicaid) well-funded."},
    "MS": {"score": 18, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 3, "garnish": "25%", "highlight": "Did not expand Medicaid. Highest uninsured rate in US. Voluntary charity care only. Weakest state protections in the nation."},
    "MO": {"score": 45, "grade": "C-", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "Medicaid expansion passed 2021 (Amendment 2). Hospitals charge 5.2× Medicare rates on average. No state surprise billing law."},
    "MT": {"score": 58, "grade": "C+", "medicaid": True, "surprise": "MCA 33-22-2001", "charity_fpl": "~200%", "sol": 8, "garnish": "25%", "highlight": "Medicaid expanded (HELP Act). State surprise billing law. Longest SOL among expanded states (8 years)."},
    "NE": {"score": 50, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "Medicaid expanded in 2020 (Initiative 427). LB 1105 limits collection practices. No state surprise billing law."},
    "NV": {"score": 72, "grade": "B+", "medicaid": True, "surprise": "NRS 695B", "charity_fpl": "300%", "sol": 6, "garnish": "25%", "highlight": "Charity care up to 300% FPL. Strong surprise billing law. Medicaid expanded. Good consumer protections."},
    "NH": {"score": 60, "grade": "B-", "medicaid": True, "surprise": "RSA 420-J", "charity_fpl": "~200%", "sol": 3, "garnish": "25%", "highlight": "Medicaid expanded (Granite Advantage). RSA 420-J surprise billing protections. Short 3-year SOL."},
    "NJ": {"score": 74, "grade": "B+", "medicaid": True, "surprise": "Strong", "charity_fpl": "~200%", "sol": 6, "garnish": "10%", "highlight": "Very low garnishment limit (10%). Medicaid expanded. Strong surprise billing protections. Good consumer laws."},
    "NM": {"score": 80, "grade": "A-", "medicaid": True, "surprise": "Federal+", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "HB 372 (2023) bans medical debt from credit reports — one of only a few states. High Medicaid enrollment (~40% of population)."},
    "NY": {"score": 88, "grade": "A", "medicaid": True, "surprise": "Strong (PHL 24)", "charity_fpl": "400%", "sol": 6, "garnish": "10%", "highlight": "Charity care up to 400% FPL. Very low garnishment limit (10%). Strongest surprise billing law in US alongside CA. 180-day billing protection."},
    "NC": {"score": 48, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 3, "garnish": "No wage garnishment for consumer debt", "highlight": "Expanded Medicaid 2023. North Carolina is one of very few states with NO wage garnishment for consumer medical debt — huge protection."},
    "ND": {"score": 58, "grade": "C+", "medicaid": True, "surprise": "NDCC 26.1-36", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded. State surprise billing law (NDCC 26.1-36). Required hospital charity care."},
    "OH": {"score": 52, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded. No state surprise billing law. Federal NSA applies. ORC § 2305.07 SOL."},
    "OK": {"score": 45, "grade": "C-", "medicaid": True, "surprise": "HB 2846", "charity_fpl": "Voluntary", "sol": 5, "garnish": "25%", "highlight": "Medicaid expanded in 2021 (SQ 802). HB 2846 surprise billing. Voluntary charity care only — no state mandate."},
    "OR": {"score": 82, "grade": "A-", "medicaid": True, "surprise": "ORS 743B", "charity_fpl": "400%", "sol": 6, "garnish": "25%", "highlight": "Charity care up to 400% FPL. Strong surprise billing law. Free patient advocates. Medicaid covers ~25% of population."},
    "PA": {"score": 62, "grade": "B-", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 4, "garnish": "No wage garnishment*", "highlight": "Pennsylvania does not allow wage garnishment for most consumer debt — major protection. Medicaid expanded. 4-year SOL."},
    "RI": {"score": 68, "grade": "B", "medicaid": True, "surprise": "OHIC regs", "charity_fpl": "~200%", "sol": 10, "garnish": "25%", "highlight": "Longest SOL in US (10 years). Medicaid expanded. OHIC surprise billing regulations. Required charity care."},
    "SC": {"score": 40, "grade": "D+", "medicaid": True, "surprise": "SB 1072", "charity_fpl": "~200%", "sol": 3, "garnish": "25%", "highlight": "Medicaid expanded. SB 1072 surprise billing. Charity care required under § 44-7-3410. Short 3-year SOL."},
    "SD": {"score": 35, "grade": "D", "medicaid": True, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 6, "garnish": "20%", "highlight": "Medicaid expanded 2023 (Amendment D). No state surprise billing law. Voluntary charity care. Late Medicaid expansion."},
    "TN": {"score": 28, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "~200%*", "sol": 6, "garnish": "25%", "highlight": "Did not expand Medicaid (300,000+ uninsured). Nonprofit hospitals must provide charity care. No state surprise billing law."},
    "TX": {"score": 25, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 4, "garnish": "No wage garnishment*", "highlight": "Largest uninsured population in US. Did not expand Medicaid. Voluntary charity care. Texas does not allow wage garnishment for most consumer debt — one bright spot."},
    "UT": {"score": 52, "grade": "C", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "25%", "highlight": "Medicaid expanded. UT Code § 26B-2-224 charity care (covers for-profit hospitals too). HB 228 debt protections. No state surprise billing law."},
    "VT": {"score": 80, "grade": "A-", "medicaid": True, "surprise": "8 V.S.A. 4089h", "charity_fpl": "~200%", "sol": 6, "garnish": "15%", "highlight": "Near-universal coverage via Green Mountain Care. Very low garnishment limit (15%). Strong surprise billing law. Medicaid well-funded."},
    "VA": {"score": 65, "grade": "B", "medicaid": True, "surprise": "HB 1251", "charity_fpl": "~200%", "sol": 5, "garnish": "25%", "highlight": "Medicaid expanded 2019. HB 1251 bans surprise balance bills. VHHA charity care standards."},
    "WA": {"score": 90, "grade": "A+", "medicaid": True, "surprise": "Strong (BBPA)", "charity_fpl": "400%", "sol": 6, "garnish": "25%", "highlight": "Second best patient protections in US after CA. Charity care up to 400% FPL. BBPA is strongest surprise billing law in US. Medicaid covers ~20% of population."},
    "WV": {"score": 45, "grade": "C-", "medicaid": True, "surprise": "WV Code 33-25A", "charity_fpl": "~200%", "sol": 10, "garnish": "20%", "highlight": "Longest SOL in US (10 years, tied with RI). Medicaid expanded. Highest medical debt burden in US despite some state protections."},
    "WI": {"score": 55, "grade": "C+", "medicaid": True, "surprise": "Federal only", "charity_fpl": "~200%", "sol": 6, "garnish": "20%", "highlight": "Medicaid expanded (BadgerCare+). 7 key patient billing rights. No state surprise billing law. 20% garnishment limit."},
    "WY": {"score": 20, "grade": "F", "medicaid": False, "surprise": "Federal only", "charity_fpl": "Voluntary", "sol": 8, "garnish": "25%", "highlight": "Did not expand Medicaid. Voluntary charity care only. Highest hospital charge-to-Medicare ratio in rural US. No state consumer protections."},
    "DC": {"score": 85, "grade": "A", "medicaid": True, "surprise": "Strong", "charity_fpl": "400%", "sol": 3, "garnish": "25%", "highlight": "Near-universal coverage. Charity care up to 400% FPL. Strong surprise billing protections. DC Health Benefit Exchange."},
}


@app.get("/map/", response_class=HTMLResponse)
async def state_protections_map(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/map/"
    import json
    return templates.TemplateResponse("state_map.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "Interactive Medical Billing Protections Map by State | BillKarma",
        "meta_description": "See how your state ranks on medical billing protections — charity care, surprise billing laws, Medicaid expansion, and debt limits. Color-coded for all 50 states.",
        "meta_robots": "index, follow",
        "state_data_json": json.dumps(_STATE_SCORES),
    })


@app.get("/research/2026-medical-billing-report/", response_class=HTMLResponse)
async def annual_report_2026(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/research/2026-medical-billing-report/"
    return templates.TemplateResponse("annual_report_2026.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "2026 Medical Billing Errors Report | BillKarma Research",
        "meta_description": "BillKarma analyzed thousands of medical bills in 2026. Key findings: 1 in 3 bills contain errors, average overcharge $1,300, cardiac bills have highest error rate.",
        "meta_robots": "index, follow",
    })


async def sol_lookup(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/tools/sol-lookup/"
    rows = []
    for abbr, (years, statute) in sorted(_SOL_DATA.items(), key=lambda x: _STATE_NAMES[x[0]]):
        extra = _SOL_EXTRA.get(abbr, (True, "Written contract", "25% of disposable income"))
        score_data = _STATE_SCORES.get(abbr, {})
        rows.append({
            "abbr": abbr,
            "name": _STATE_NAMES[abbr],
            "years": years,
            "statute": statute,
            "resets": extra[0],
            "contract_type": extra[1],
            "garnish": extra[2],
            "surprise": score_data.get("surprise", "Federal only"),
            "charity_fpl": score_data.get("charity_fpl", "~200%"),
            "medicaid": score_data.get("medicaid", False),
        })
    return templates.TemplateResponse("sol_lookup.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "Medical Debt Statute of Limitations by State (2026) | BillKarma",
        "meta_description": "Look up your state's medical debt statute of limitations. Most states are 3–6 years. After the deadline, collectors can't win a lawsuit against you.",
        "meta_robots": "index, follow",
        "sol_rows": rows,
    })


@app.get("/tools/charity-care/", response_class=HTMLResponse)
async def charity_care_tool(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/tools/charity-care/"
    return templates.TemplateResponse("charity_care_tool.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "Charity Care Eligibility Checker — Free Hospital Care (2026) | BillKarma",
        "meta_description": "Find out if you qualify for free or reduced hospital care. Enter your state, household size, and income to check your charity care eligibility instantly.",
        "meta_robots": "index, follow",
        "fpl_base": _FPL_BASE,
        "fpl_add": _FPL_ADD,
    })


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
    if page == 1 and (str(request.query_params) != ""):
        return RedirectResponse(url=f"/hospitals/{state_slug}/", status_code=301)
    hospitals, total = get_state_hospitals(state_slug, sort=sort, ownership=ownership, page=page)
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    cities = get_cities_for_state(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/"
    has_params = page > 1 or sort != "grade" or ownership
    robots = "noindex, follow" if has_params else "index, follow"
    resp = templates.TemplateResponse(
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
            "meta_robots": robots,
        },
    )
    if has_params:
        resp.headers["X-Robots-Tag"] = "noindex, follow"
    return resp


@app.get("/hospitals/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def hospital_city_page(
    request: Request,
    state_slug: str,
    city_slug: str,
    sort: str = "grade",
    page: int = 1,
):
    from hospital_seo import get_city_hospitals

    if page == 1 and (str(request.query_params) != ""):
        return RedirectResponse(url=f"/hospitals/{state_slug}/{city_slug}/", status_code=301)
    hospitals, total = get_city_hospitals(state_slug, city_slug, sort=sort, page=page)
    city_name = hospitals[0]["city"] if hospitals else city_slug.replace("-", " ").title()
    state_name = hospitals[0]["state"] if hospitals else state_display_name(state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/hospitals/{state_slug}/{city_slug}/"
    has_params = page > 1 or sort != "grade"
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
            "meta_robots": "noindex, follow" if has_params else "index, follow",
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
        return templates.TemplateResponse("error.html", {"request": request, "message": "Hospital not found"}, status_code=404)
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
    canonical_url = f"{config.APP_URL.rstrip('/')}/surgery-centers/"
    return templates.TemplateResponse(
        "facilities_index.html",
        {
            "request": request,
            "states": states,
            "title": "Find Ambulatory Surgery Centers Near You",
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
            "stats": stats,
            "canonical_url": canonical_url,
        },
    )


@app.get("/surgery-centers/{state_slug}/", response_class=HTMLResponse)
async def surgery_centers_state(request: Request, state_slug: str):
    facilities = get_facilities_in_scope("asc", state_slug=state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/surgery-centers/{state_slug}/"
    return templates.TemplateResponse(
        "facilities_state.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
            "canonical_url": canonical_url,
        },
    )


@app.get("/surgery-centers/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def surgery_centers_city(request: Request, state_slug: str, city_slug: str):
    facilities = get_facilities_in_scope("asc", state_slug=state_slug, city_slug=city_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/surgery-centers/{state_slug}/{city_slug}/"
    return templates.TemplateResponse(
        "facilities_city.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "city_slug": city_slug,
            "label": "Surgery Centers",
            "base_path": "/surgery-centers/",
            "canonical_url": canonical_url,
        },
    )


@app.get("/surgery-centers/{state_slug}/{city_slug}/{slug}/", response_class=HTMLResponse)
async def surgery_centers_detail(request: Request, state_slug: str, city_slug: str, slug: str):
    data = get_facility_profile("asc", state_slug, city_slug, slug)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Facility not found"}, status_code=404)
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
    canonical_url = f"{config.APP_URL.rstrip('/')}/imaging/"
    return templates.TemplateResponse(
        "facilities_index.html",
        {
            "request": request,
            "states": states,
            "title": "Find Imaging Centers Near You",
            "label": "Imaging Centers",
            "base_path": "/imaging/",
            "stats": stats,
            "canonical_url": canonical_url,
        },
    )


@app.get("/imaging/{state_slug}/", response_class=HTMLResponse)
async def imaging_state(request: Request, state_slug: str):
    facilities = get_facilities_in_scope("imaging_center", state_slug=state_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/imaging/{state_slug}/"
    return templates.TemplateResponse(
        "facilities_state.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "label": "Imaging Centers",
            "base_path": "/imaging/",
            "canonical_url": canonical_url,
        },
    )


@app.get("/imaging/{state_slug}/{city_slug}/", response_class=HTMLResponse)
async def imaging_city(request: Request, state_slug: str, city_slug: str):
    facilities = get_facilities_in_scope("imaging_center", state_slug=state_slug, city_slug=city_slug)
    canonical_url = f"{config.APP_URL.rstrip('/')}/imaging/{state_slug}/{city_slug}/"
    return templates.TemplateResponse(
        "facilities_city.html",
        {
            "request": request,
            "facilities": facilities,
            "state_slug": state_slug,
            "city_slug": city_slug,
            "label": "Imaging Centers",
            "base_path": "/imaging/",
            "canonical_url": canonical_url,
        },
    )


@app.get("/imaging/{state_slug}/{city_slug}/{slug}/", response_class=HTMLResponse)
async def imaging_detail(request: Request, state_slug: str, city_slug: str, slug: str):
    data = get_facility_profile("imaging_center", state_slug, city_slug, slug)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Facility not found"}, status_code=404)
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
            "og_title": "Medical Procedure Costs: Medicare Rates vs What Hospitals Actually Charge (2026)",
            "og_description": "Compare what Medicare pays vs what hospitals charge for 100+ procedures. See which hospitals overcharge and find fair prices near you.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/procedures/{slug}-cost/", response_class=HTMLResponse)
async def procedure_content_page(request: Request, slug: str):
    data = get_content_page_data(f"{slug}-cost")
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure page not found"}, status_code=404)
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
        return templates.TemplateResponse("error.html", {"request": request, "message": "Procedure not found"}, status_code=404)
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


@app.get("/compare", response_class=HTMLResponse)
async def compare_index_noslash(request: Request):
    # Redirect no-trailing-slash variant to canonical /compare/ — eliminates duplicate URL
    qs = str(request.query_params)
    dest = "/compare/?" + qs if qs else "/compare/"
    return RedirectResponse(url=dest, status_code=301)


@app.get("/compare/", response_class=HTMLResponse)
async def compare_index(
    request: Request,
    facility_a: str = Query("", alias="facility-a"),
    facility_b: str = Query("", alias="facility-b"),
    hospital: str = "",
):
    # Normalize float-parsed facility IDs (e.g. "1659325629.0" → "1659325629")
    facility_a = _clean_fid(facility_a)
    facility_b = _clean_fid(facility_b)
    hospital = _clean_fid(hospital)
    # Deep-link support from ASC/imaging pages.
    if facility_a and facility_b:
        return RedirectResponse(url=f"/compare/{facility_a}/vs/{facility_b}/", status_code=301)
    if hospital:
        facility_a = hospital
    # Parameter URLs are just the empty form — don't let Google index them
    has_params = facility_a or facility_b
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/"
    robots = "noindex, follow" if has_params else "index, follow"
    resp = templates.TemplateResponse(
        "compare_index.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "Hospital Comparison Tool | BillKarma",
            "og_description": "Compare any two hospitals side-by-side: billing grade, markup vs Medicare, CMS stars, and procedure prices.",
            "meta_robots": robots,
        },
    )
    if has_params:
        resp.headers["X-Robots-Tag"] = "noindex, follow"
    return resp


@app.get("/compare/{fid_a}/vs/{fid_b}/", response_class=HTMLResponse)
async def compare_detail(request: Request, fid_a: str, fid_b: str):
    # Redirect .0-suffixed IDs to clean URLs
    clean_a, clean_b = _clean_fid(fid_a), _clean_fid(fid_b)
    if clean_a != fid_a or clean_b != fid_b:
        return RedirectResponse(url=f"/compare/{clean_a}/vs/{clean_b}/", status_code=301)
    data = get_comparison_data(fid_a, fid_b)
    if not data:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "One or both hospitals not found."},
        )
    # Redirect to canonical slug-based URL so Google only indexes one version
    if data["a"].get("slug") and data["b"].get("slug"):
        return RedirectResponse(
            url=f"/compare/{data['a']['slug']}-vs-{data['b']['slug']}/",
            status_code=301,
        )
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/{fid_a}/vs/{fid_b}/"
    seo = data.get("seo") or build_comparison_seo(
        data["a"],
        data["b"],
        data.get("common_procedures", []),
        data.get("distance_miles"),
    )
    return templates.TemplateResponse(
        "compare_detail.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/sitemap.xml")
async def sitemap_index():
    base = config.APP_URL.rstrip("/")
    hospital_paths = get_hospital_sitemap_paths()
    from compare_seo import get_comparison_sitemap_paths

    comparison_paths = get_comparison_sitemap_paths()
    core_urls = [
        (f"{base}/", "2026-02-01", "1.0"),
        (f"{base}/guides/", "2026-02-01", "0.8"),
        (f"{base}/tools/", "2026-02-01", "0.8"),
        (f"{base}/fight-debt", "2026-02-24", "0.9"),
        (f"{base}/savings", "2026-02-25", "0.8"),
        (f"{base}/shop", "2026-02-25", "0.8"),
        (f"{base}/watch", "2026-02-25", "0.7"),
        (f"{base}/estimate", "2026-03-01", "0.9"),
        (f"{base}/rights/", "2026-03-01", "0.8"),
        (f"{base}/quiz", "2026-03-01", "0.9"),
        (f"{base}/glossary/", "2026-03-01", "0.8"),
        (f"{base}/cost/mri/", "2026-03-01", "0.8"),
        (f"{base}/cost/colonoscopy/", "2026-03-01", "0.8"),
        (f"{base}/cost/ct-scan/", "2026-03-01", "0.8"),
        (f"{base}/cost/knee-replacement/", "2026-03-01", "0.8"),
        (f"{base}/cost/er-visit/", "2026-03-01", "0.8"),
        (f"{base}/about/", "2026-04-10", "0.7"),
        (f"{base}/press/", "2026-04-01", "0.7"),
        (f"{base}/chargemaster/", "2026-04-01", "0.9"),
        (f"{base}/procedures/", "2026-04-10", "0.9"),
        (f"{base}/sitemap-guides.xml", "2026-02-24", "0.5"),
        (f"{base}/sitemap-procedures.xml", "2026-04-10", "0.5"),
        (f"{base}/sitemap-hospitals.xml", "2026-02-24", "0.5"),
        (f"{base}/sitemap-facilities.xml", "2026-03-01", "0.5"),
        (f"{base}/sitemap-costs.xml", "2026-04-01", "0.5"),
        (f"{base}/sitemap-data-guides.xml", "2026-04-10", "0.5"),
        (f"{base}/guides/most-expensive-states-healthcare-2026/", "2026-04-10", "0.8"),
    ]
    core_entries = "".join(
        f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>"
        for loc, lastmod, priority in core_urls
    )
    hospital_entries = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-01-01</lastmod><priority>0.5</priority></url>"
        for path in hospital_paths
    )
    comparison_entries = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-03-03</lastmod><priority>0.6</priority></url>"
        for path in comparison_paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{core_entries}{hospital_entries}{comparison_entries}</urlset>"
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
        (f"{base}/estimate", "2026-03-01", "0.9"),
        (f"{base}/rights/", "2026-03-01", "0.8"),
    ]
    static_entries = "".join(
        f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><priority>{priority}</priority></url>"
        for loc, lastmod, priority in static_urls
    )
    guide_entries = "".join(
        f"<url><loc>{base}/guides/{slug}/</loc><lastmod>{published}</lastmod><priority>0.8</priority></url>"
        for slug, published in get_guides_for_sitemap()
    )
    from guides import get_all_categories as _get_all_cats
    category_entries = "".join(
        f"<url><loc>{base}/guides/category/{c['slug']}/</loc><lastmod>2026-04-05</lastmod><priority>0.7</priority></url>"
        for c in _get_all_cats()
    )
    tool_entries = "".join(
        f"<url><loc>{base}/tools/{tool['slug']}/</loc><lastmod>2026-02-01</lastmod><priority>0.8</priority></url>"
        for tool in list_tools()
    )
    from state_rights import get_all_states as _get_all_states_sitemap
    rights_entries = "".join(
        f"<url><loc>{base}/rights/{s['slug']}/</loc><lastmod>2026-03-01</lastmod><priority>0.7</priority></url>"
        for s in _get_all_states_sitemap()
    )
    from cost_pages import get_all_cost_slugs
    cost_entries = "".join(
        f"<url><loc>{base}/cost/{slug}/</loc><lastmod>2026-03-01</lastmod><priority>0.8</priority></url>"
        for slug in get_all_cost_slugs()
    )
    procedure_entries = "".join(
        f"<url><loc>{base}/procedures/{p['cpt_code']}/</loc><lastmod>2026-03-01</lastmod><priority>0.6</priority></url>"
        for p in get_top_cpt_codes()
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{static_entries}{guide_entries}{category_entries}{tool_entries}{rights_entries}{cost_entries}{procedure_entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-hospitals.xml")
async def hospital_sitemap_v2():
    base = config.APP_URL.rstrip("/")
    from compare_seo import get_comparison_sitemap_paths

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
    comparison_entries = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-03-03</lastmod><priority>0.6</priority></url>"
        for path in get_comparison_sitemap_paths()
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{core_entries}{tool_entries}{urlset}{comparison_entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/hospitals/sitemap.xml")
async def hospital_sitemap_legacy():
    return RedirectResponse(url="/sitemap-hospitals.xml", status_code=301)


@app.get("/sitemap-facilities.xml")
async def facilities_sitemap():
    base = config.APP_URL.rstrip("/")
    facility_paths = get_facility_sitemap_paths()
    entries = "".join(
        f"<url><loc>{base}{path}</loc><lastmod>2026-03-01</lastmod><priority>0.5</priority></url>"
        for path in facility_paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-costs.xml")
async def costs_sitemap():
    """Sitemap for procedure × city AND procedure × state cost pages."""
    base = config.APP_URL.rstrip("/")
    city_entries = "".join(
        f"<url><loc>{base}/costs/{proc_slug}/{city_slug}/</loc><lastmod>2026-04-10</lastmod><priority>0.7</priority></url>"
        for proc_slug in _PROCEDURE_SLUGS
        for city_slug in _CITY_DATA
    )
    state_entries = "".join(
        f"<url><loc>{base}/costs/{proc_slug}/{state_slug}/</loc><lastmod>2026-04-10</lastmod><priority>0.7</priority></url>"
        for proc_slug in _PROCEDURE_SLUGS
        for state_slug in _STATE_DATA
        if state_slug not in _CITY_DATA  # exclude new-york (served as city)
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{city_entries}{state_entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-procedures.xml")
async def procedures_sitemap():
    """Sitemap for procedure hub pages."""
    base = config.APP_URL.rstrip("/")
    entries = (
        f'<url><loc>{base}/procedures/</loc><lastmod>2026-04-10</lastmod><priority>0.9</priority></url>'
        + "".join(
            f"<url><loc>{base}/procedures/{slug}/</loc><lastmod>2026-04-10</lastmod><priority>0.8</priority></url>"
            for slug in _PROCEDURE_SLUGS
        )
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get("/sitemap-data-guides.xml")
async def data_guides_sitemap():
    """Sitemap for data-driven guide pages (cheapest cities + state comparison)."""
    base = config.APP_URL.rstrip("/")
    entries = (
        f'<url><loc>{base}/guides/most-expensive-states-healthcare-2026/</loc><lastmod>2026-04-10</lastmod><priority>0.8</priority></url>'
        + "".join(
            f"<url><loc>{base}/guides/cheapest-cities-{slug}-2026/</loc><lastmod>2026-04-10</lastmod><priority>0.8</priority></url>"
            for slug in _PROCEDURE_SLUGS
        )
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>"
    )
    return Response(content=xml, media_type="application/xml")


@app.get(f"/{config.INDEXNOW_KEY}.txt")
async def indexnow_key_file():
    """Serve IndexNow key verification file."""
    return Response(content=config.INDEXNOW_KEY, media_type="text/plain")


async def _ping_indexnow(urls: list[str]) -> bool:
    """Submit URLs to IndexNow (Bing, Yandex). Returns True on success."""
    import httpx
    host = config.APP_URL.rstrip("/").replace("https://", "").replace("http://", "")
    payload = {
        "host": host,
        "key": config.INDEXNOW_KEY,
        "keyLocation": f"{config.APP_URL.rstrip('/')}/{config.INDEXNOW_KEY}.txt",
        "urlList": urls[:10000],
    }
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post("https://api.indexnow.org/indexnow", json=payload)
            return r.status_code in (200, 202)
    except Exception as e:
        logging.warning("IndexNow ping failed: %s", e)
        return False


@app.post("/newsletter/subscribe")
async def newsletter_subscribe(request: Request):
    """Store email for newsletter / checklist delivery. Simple opt-in."""
    from fastapi import Form
    form = await request.form()
    email = str(form.get("email", "")).strip().lower()
    source = str(form.get("source", "unknown"))[:100]
    if not email or "@" not in email or len(email) > 254:
        return JSONResponse({"status": "error", "message": "Invalid email"}, status_code=400)
    try:
        with db.get_db() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS newsletter_subscribers "
                "(id INTEGER PRIMARY KEY, email TEXT UNIQUE, source TEXT, subscribed_at TEXT)",
            )
            conn.execute(
                "INSERT OR IGNORE INTO newsletter_subscribers (email, source, subscribed_at) VALUES (?, ?, datetime('now'))",
                (email, source),
            )
    except Exception as e:
        logging.warning("Newsletter subscribe error: %s", e)
    return JSONResponse({"status": "ok"})


@app.post("/admin/ping-indexnow")
async def admin_ping_indexnow(request: Request):
    """Ping IndexNow with all procedure + cost pages. Requires ADMIN_API_TOKEN."""
    token = request.headers.get("X-Admin-Token", "")
    if config.ADMIN_API_TOKEN and token != config.ADMIN_API_TOKEN:
        return JSONResponse({"status": "error", "message": "Unauthorized"}, status_code=401)
    base = config.APP_URL.rstrip("/")
    urls = (
        [f"{base}/procedures/", f"{base}/guides/"]
        + [f"{base}/procedures/{s}/" for s in _PROCEDURE_SLUGS]
        + [f"{base}/costs/{p}/{c}/" for p in _PROCEDURE_SLUGS for c in _CITY_DATA]
        + [f"{base}/costs/{p}/{s}/" for p in _PROCEDURE_SLUGS for s in _STATE_DATA if s not in _CITY_DATA]
    )
    ok = await _ping_indexnow(urls)
    return JSONResponse({"status": "ok" if ok else "error", "urls_submitted": len(urls)})


@app.get("/og/{slug}.svg")
async def og_image_svg(slug: str):
    """Return a branded SVG social preview image for a guide."""
    import textwrap
    from guides import get_guide
    guide = get_guide(slug)
    title = guide["title"] if guide else "BillKarma Medical Billing Guide"
    category = guide.get("category", "") if guide else ""

    # Wrap title text to fit SVG width (~42 chars per line at font-size 52)
    lines = textwrap.wrap(title, width=28)[:3]
    # Build SVG text elements, each line 68px apart
    text_y_start = 260 - (len(lines) - 1) * 34
    text_els = "".join(
        f'<text x="60" y="{text_y_start + i * 68}" font-family="system-ui,-apple-system,sans-serif" '
        f'font-size="52" font-weight="800" fill="#ffffff" letter-spacing="-1">{line}</text>'
        for i, line in enumerate(lines)
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#1a5c38"/>
  <rect width="1200" height="630" fill="url(#grad)"/>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a5c38;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0d3d24;stop-opacity:1"/>
    </linearGradient>
  </defs>
  <!-- BillKarma wordmark -->
  <text x="60" y="90" font-family="system-ui,-apple-system,sans-serif" font-size="32" font-weight="800" fill="#a3e4b8" letter-spacing="0">BillKarma</text>
  <!-- Category badge -->
  {f'<rect x="58" y="112" width="{len(category) * 13 + 28}" height="36" rx="18" fill="rgba(255,255,255,0.15)"/><text x="72" y="136" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="700" fill="#ffffff" letter-spacing="1" text-transform="uppercase">{category.upper()}</text>' if category else ''}
  <!-- Title -->
  {text_els}
  <!-- Bottom tagline -->
  <text x="60" y="570" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="500" fill="rgba(255,255,255,0.65)">billkarma.app/guides/{slug}/</text>
</svg>"""
    return Response(content=svg, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=86400"})


@app.get("/robots.txt")
async def robots_txt():
    body = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-guides.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-hospitals.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-facilities.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-costs.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-procedures.xml\n"
        f"Sitemap: {config.APP_URL.rstrip('/')}/sitemap-data-guides.xml\n"
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
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"}, status_code=404)

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
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"}, status_code=404)
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
        return templates.TemplateResponse("error.html", {"request": request, "message": "Score not found"}, status_code=404)
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


# --- Savings Estimator ---


@app.get("/estimate", response_class=HTMLResponse)
async def estimate_page(request: Request):
    """Savings estimator — instant overcharge estimate."""
    canonical_url = f"{config.APP_URL.rstrip('/')}/estimate"
    return templates.TemplateResponse(
        "estimate.html",
        {
            "request": request,
            "canonical_url": canonical_url,
            "og_title": "How Much Could I Save on My Medical Bill? | BillKarma",
            "og_description": "Enter your bill amount and hospital name for a free savings estimate based on Medicare benchmarks and hospital billing data.",
            "meta_robots": "index, follow",
        },
    )


# --- My Bills Dashboard ---


@app.get("/my-bills", response_class=HTMLResponse)
async def my_bills_page(request: Request):
    """Dashboard showing all bills the user has scanned."""
    from access_control import get_session_id
    from my_bills import get_session_bills, get_session_summary

    sid = get_session_id(request)
    bills = get_session_bills(sid) if sid else []
    summary = get_session_summary(bills)
    canonical_url = f"{config.APP_URL.rstrip('/')}/my-bills"
    return templates.TemplateResponse(
        "my_bills.html",
        {
            "request": request,
            "bills": bills,
            "summary": summary,
            "canonical_url": canonical_url,
            "og_title": "My Bills | BillKarma",
            "og_description": "Track all your scanned medical bills and savings in one place.",
            "meta_robots": "noindex, nofollow",
        },
    )


# --- State Medical Billing Rights ---


@app.get("/rights/", response_class=HTMLResponse)
async def rights_index_page(request: Request):
    """State-by-state medical billing rights index."""
    from state_rights import get_all_states

    states = get_all_states()
    canonical_url = f"{config.APP_URL.rstrip('/')}/rights/"
    return templates.TemplateResponse(
        "rights_index.html",
        {
            "request": request,
            "states": states,
            "canonical_url": canonical_url,
            "og_title": "Medical Billing Rights by State | BillKarma",
            "og_description": "Know your medical billing rights. State-by-state guide to statute of limitations, balance billing, charity care, and debt collection laws.",
            "meta_robots": "index, follow",
        },
    )


@app.get("/rights/{state_slug}/", response_class=HTMLResponse)
async def rights_state_page(request: Request, state_slug: str):
    """Individual state medical billing rights page."""
    from state_rights import get_state_rights

    state = get_state_rights(state_slug)
    if not state:
        return HTMLResponse(status_code=404, content="State not found")
    canonical_url = f"{config.APP_URL.rstrip('/')}/rights/{state_slug}/"
    return templates.TemplateResponse(
        "rights_state.html",
        {
            "request": request,
            "state": state,
            "canonical_url": canonical_url,
            "og_title": f"{state['name']} Medical Billing Rights & Protections | BillKarma",
            "og_description": f"Medical billing rights in {state['name']}: {state['sol_years']}-year statute of limitations, balance billing protections, charity care rules, and more.",
            "meta_robots": "index, follow",
        },
    )


# --- Quick Triage Quiz ---


@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request):
    """Quick triage quiz — 4 questions to personalized action plan."""
    from quiz import QUESTIONS

    canonical_url = f"{config.APP_URL.rstrip('/')}/quiz"
    return templates.TemplateResponse(
        "quiz.html",
        {
            "request": request,
            "questions": QUESTIONS,
            "canonical_url": canonical_url,
            "og_title": "What Should I Do About My Medical Bill? — Free Quiz | BillKarma",
            "og_description": "Answer 4 quick questions and get a personalized action plan for your medical bill situation.",
            "meta_robots": "index, follow",
        },
    )


# --- Medical Billing Glossary ---


@app.get("/glossary/", response_class=HTMLResponse)
async def glossary_page(request: Request):
    """Medical billing glossary with 50+ terms."""
    from glossary import get_all_terms, get_terms_by_category

    canonical_url = f"{config.APP_URL.rstrip('/')}/glossary/"
    return templates.TemplateResponse(
        "glossary.html",
        {
            "request": request,
            "all_terms": get_all_terms(),
            "categories": get_terms_by_category(),
            "canonical_url": canonical_url,
            "og_title": "Medical Billing Glossary — 50+ Terms Explained | BillKarma",
            "og_description": "Plain-English definitions for every term on your medical bill, insurance statement, and collection notice.",
            "meta_robots": "index, follow",
        },
    )


# --- Autopilot Agent ---


@app.get("/autopilot/strategy/{bill_id}", response_class=HTMLResponse)
async def autopilot_strategy_page(request: Request, bill_id: int):
    """Show AI-generated dispute strategy before activation."""
    require_bill_access(request, bill_id)
    from autopilot import generate_strategy

    strategy = generate_strategy(bill_id)
    if strategy.get("error"):
        return templates.TemplateResponse("error.html", {"request": request, "message": strategy["error"]}, status_code=404)

    bill_total = float(strategy.get("total_charged") or 0)
    fee_cents = payment_module.calculate_fee(bill_total)

    return templates.TemplateResponse(
        "autopilot_strategy.html",
        {
            "request": request,
            "strategy": strategy,
            "fee_dollars": fee_cents // 100,
            "meta_robots": "noindex, nofollow",
        },
    )


@app.get("/autopilot/dashboard/{case_id}", response_class=HTMLResponse)
async def autopilot_dashboard_page(request: Request, case_id: int):
    """Real-time autopilot dispute dashboard."""
    require_case_access(request, case_id)
    from autopilot import get_autopilot_status

    data = get_autopilot_status(case_id)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Case not found"}, status_code=404)

    return templates.TemplateResponse(
        "autopilot.html",
        {
            "request": request,
            "data": data,
            "meta_robots": "noindex, nofollow",
        },
    )


# --- AI Bill Advisor ---


@app.get("/advisor/{bill_id}", response_class=HTMLResponse)
async def advisor_page(request: Request, bill_id: int):
    """AI-powered chat advisor with full bill context."""
    require_bill_access(request, bill_id)
    results = get_bill_results(bill_id)
    if not results:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Bill not found"}, status_code=404)

    bill = results["bill"]
    findings = results.get("findings") or []
    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)

    return templates.TemplateResponse(
        "advisor.html",
        {
            "request": request,
            "bill_id": bill_id,
            "provider_name": bill.get("provider_name", ""),
            "total_savings": total_savings,
            "finding_count": len(findings),
            "meta_robots": "noindex, nofollow",
        },
    )


# --- Embeddable Savings Calculator Widget ---


@app.get("/embed/estimate", response_class=HTMLResponse)
async def embed_estimate(request: Request):
    """Lightweight embeddable savings calculator for iframes."""
    response = templates.TemplateResponse(
        "embed_estimate.html",
        {
            "request": request,
            "app_url": config.APP_URL.rstrip("/"),
            "api_base": config.APP_URL.rstrip("/"),
        },
    )
    response.headers["X-Frame-Options"] = "ALLOWALL"
    response.headers["Content-Security-Policy"] = "frame-ancestors *"
    return response


# --- How Much Does X Cost? Landing Pages ---


@app.get("/cost/{slug}/", response_class=HTMLResponse)
async def cost_page(request: Request, slug: str):
    """Consumer-friendly procedure cost landing page."""
    from cost_pages import get_cost_page_data

    data = get_cost_page_data(slug)
    if not data:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Cost page not found"}, status_code=404)
    canonical_url = f"{config.APP_URL.rstrip('/')}/cost/{slug}/"
    return templates.TemplateResponse(
        "cost_page.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": data["seo"]["page_title"],
            "og_description": data["seo"]["meta_description"],
            "meta_description": data["seo"]["meta_description"],
            "meta_robots": "index, follow",
        },
    )


# --- Hospital vs Hospital SEO Comparison Pages ---


@app.get("/compare/{slug_a}-vs-{slug_b}/", response_class=HTMLResponse)
async def compare_seo_page(request: Request, slug_a: str, slug_b: str):
    """Auto-generated hospital comparison page using human-readable slugs."""
    from compare_seo import resolve_comparison_slugs

    result = resolve_comparison_slugs(slug_a, slug_b)
    if not result:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "One or both hospitals not found."},
        )
    fid_a, fid_b = result
    data = get_comparison_data(fid_a, fid_b)
    if not data:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "Comparison data not available."},
        )
    canonical_url = f"{config.APP_URL.rstrip('/')}/compare/{slug_a}-vs-{slug_b}/"
    seo = data.get("seo") or build_comparison_seo(
        data["a"],
        data["b"],
        data.get("common_procedures", []),
        data.get("distance_miles"),
    )
    return templates.TemplateResponse(
        "compare_detail.html",
        {
            "request": request,
            "data": data,
            "canonical_url": canonical_url,
            "og_title": seo["page_title"],
            "og_description": seo["meta_description"],
            "meta_description": seo["meta_description"],
            "meta_robots": "index, follow",
        },
    )


@app.get("/about/", response_class=HTMLResponse)
async def about_page(request: Request):
    canonical_url = f"{config.APP_URL.rstrip('/')}/about/"
    return templates.TemplateResponse("about.html", {
        "request": request,
        "canonical_url": canonical_url,
        "og_title": "About BillKarma — Medical Billing Transparency for Patients",
        "meta_description": "BillKarma helps patients understand and dispute hospital bills using CMS price transparency data, Medicare rates, and billing error detection tools. Free for everyone.",
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)
