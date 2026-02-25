"""Pre-Care Price Shopper — find the cheapest provider for a procedure near you."""

import math

from db import get_db

FACILITY_TYPE_LABELS = {
    "hospital": "Hospital",
    "asc": "Surgery Center",
    "imaging_center": "Imaging Center",
}


def _haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 3958.8  # Earth radius in miles
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def shop_for_procedure(
    cpt_code: str,
    zip_code: str,
    radius_miles: int = 50,
    limit: int = 20,
    facility_type: str = "all",
    sort_by: str = "price",
) -> dict:
    """Find providers near zip_code for a procedure, ranked by price.

    Returns: {procedure, zip_center, providers: [...], savings_opportunity}
    """
    if not cpt_code or not zip_code:
        return {"procedure": None, "providers": [], "savings_opportunity": None}

    with get_db() as db:
        # Get zip centroid
        zip_row = db.execute(
            "SELECT lat, lon, city, state FROM zip_latlon WHERE zip = ?",
            (zip_code,),
        ).fetchone()
        if not zip_row:
            return {"procedure": None, "providers": [], "savings_opportunity": None}

        center_lat = float(zip_row["lat"])
        center_lon = float(zip_row["lon"])
        center_city = zip_row["city"]
        center_state = zip_row["state"]

        # Get procedure description from medicare_rates
        proc_row = db.execute(
            "SELECT description FROM medicare_rates WHERE cpt_code = ? LIMIT 1",
            (cpt_code,),
        ).fetchone()
        proc_name = dict(proc_row)["description"] if proc_row else f"CPT {cpt_code}"

        # Get medicare rate for reference
        medicare_row = db.execute(
            "SELECT facility_rate, non_facility_rate FROM medicare_rates "
            "WHERE cpt_code = ? ORDER BY effective_year DESC LIMIT 1",
            (cpt_code,),
        ).fetchone()
        medicare_rate = None
        if medicare_row:
            medicare_rate = float(medicare_row["facility_rate"] or medicare_row["non_facility_rate"] or 0)

        # Find providers with prices for this CPT
        type_clause = ""
        params = [cpt_code]
        if facility_type and facility_type != "all":
            type_clause = "AND f.facility_type = ?"
            params.append(facility_type)

        rows = db.execute(
            f"""
            SELECT
                f.facility_id,
                f.name,
                f.city,
                f.state,
                f.state_slug,
                f.city_slug,
                f.slug,
                f.facility_type,
                f.lat,
                f.lon,
                f.phone,
                COALESCE(hp.gross_charge, pp.gross_charge) AS gross_charge,
                COALESCE(hp.cash_price, pp.cash_price) AS cash_price,
                COALESCE(hp.avg_negotiated_rate, pp.avg_negotiated_rate) AS avg_negotiated_rate,
                COALESCE(fbm.billing_grade, bm.billing_grade) AS billing_grade,
                COALESCE(fbm.avg_markup, bm.avg_markup_vs_medicare) AS avg_markup
            FROM facilities f
            LEFT JOIN hospital_prices hp ON hp.facility_id = f.facility_id AND hp.cpt_code = ?
            LEFT JOIN procedure_prices pp ON pp.facility_id = f.facility_id AND pp.cpt_code = ?
            LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = f.facility_id
            LEFT JOIN billing_metrics bm ON bm.facility_id = f.facility_id
            WHERE (hp.gross_charge IS NOT NULL OR pp.gross_charge IS NOT NULL)
              AND f.lat IS NOT NULL AND f.lon IS NOT NULL
              {type_clause}
            """,
            [cpt_code, cpt_code, *params[1:]],
        ).fetchall()

    # Filter by distance and sort
    providers = []
    for row in rows:
        row = dict(row)
        if not row.get("lat") or not row.get("lon"):
            continue

        distance = _haversine_miles(center_lat, center_lon, float(row["lat"]), float(row["lon"]))
        if distance > radius_miles:
            continue

        gross = float(row.get("gross_charge") or 0)
        cash = float(row.get("cash_price") or 0) if row.get("cash_price") else None
        negotiated = float(row.get("avg_negotiated_rate") or 0) if row.get("avg_negotiated_rate") else None
        best_price = cash or negotiated or gross

        # Compute savings vs Medicare
        markup_vs_medicare = None
        if medicare_rate and medicare_rate > 0 and gross > 0:
            markup_vs_medicare = round(gross / medicare_rate, 1)

        ftype = (row.get("facility_type") or "hospital").strip().lower()
        if ftype == "asc":
            url = f"/surgery-centers/{row['state_slug']}/{row['city_slug']}/{row['slug']}/"
        elif ftype == "imaging_center":
            url = f"/imaging/{row['state_slug']}/{row['city_slug']}/{row['slug']}/"
        else:
            url = f"/hospitals/{row['state_slug']}/{row['city_slug']}/{row['slug']}/"

        providers.append({
            "facility_id": row["facility_id"],
            "name": row["name"],
            "city": row["city"],
            "state": row["state"],
            "facility_type": ftype,
            "facility_type_label": FACILITY_TYPE_LABELS.get(ftype, "Facility"),
            "url": url,
            "distance_miles": round(distance, 1),
            "gross_charge": gross,
            "cash_price": cash,
            "avg_negotiated_rate": negotiated,
            "best_price": round(best_price, 2),
            "medicare_rate": medicare_rate,
            "markup_vs_medicare": markup_vs_medicare,
            "billing_grade": row.get("billing_grade"),
            "phone": row.get("phone"),
        })

    # Sort
    if sort_by == "distance":
        providers.sort(key=lambda p: p["distance_miles"])
    elif sort_by == "grade":
        grade_order = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4, None: 5}
        providers.sort(key=lambda p: (grade_order.get(p["billing_grade"], 5), p["best_price"]))
    else:
        providers.sort(key=lambda p: p["best_price"])

    providers = providers[:limit]

    # Calculate savings opportunity
    savings_opportunity = None
    if len(providers) >= 2:
        prices = [p["best_price"] for p in providers if p["best_price"] > 0]
        if prices:
            cheapest = min(prices)
            most_expensive = max(prices)
            savings_opportunity = {
                "cheapest": round(cheapest, 2),
                "most_expensive": round(most_expensive, 2),
                "max_savings": round(most_expensive - cheapest, 2),
                "cheapest_provider": next(p["name"] for p in providers if p["best_price"] == cheapest),
            }

    return {
        "procedure": {
            "cpt_code": cpt_code,
            "name": proc_name,
            "medicare_rate": medicare_rate,
        },
        "zip_center": {
            "zip": zip_code,
            "city": center_city,
            "state": center_state,
            "lat": center_lat,
            "lon": center_lon,
        },
        "radius_miles": radius_miles,
        "providers": providers,
        "total_found": len(providers),
        "savings_opportunity": savings_opportunity,
    }
