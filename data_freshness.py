"""Data freshness monitoring and stale data alerts."""

from datetime import datetime, date, timedelta

from db import get_db


def get_data_freshness() -> dict:
    """
    Check the freshness of all data sources.
    Returns a dict with source names, status, and any warnings.
    """
    sources = {}

    with get_db() as db:
        # Medicare PFS rates
        row = db.execute("SELECT MAX(effective_year) as yr FROM medicare_rates").fetchone()
        latest_pfs_year = row["yr"] if row else None
        current_year = date.today().year
        pfs_fresh = latest_pfs_year is not None and latest_pfs_year >= current_year
        sources["medicare_pfs"] = {
            "name": "Medicare Physician Fee Schedule",
            "latest_year": latest_pfs_year,
            "expected_frequency": "Annual (January 1)",
            "fresh": pfs_fresh,
            "warning": None if pfs_fresh else (
                f"Medicare rates are from {latest_pfs_year or 'N/A'}. "
                f"Current year is {current_year}. Rates may be outdated."
            ),
        }

        # NCCI edits
        row = db.execute("SELECT MAX(effective_date) as dt FROM ncci_edits").fetchone()
        latest_ncci = row["dt"] if row else None
        ncci_fresh = False
        ncci_days_old = None
        if latest_ncci:
            try:
                ncci_date = datetime.strptime(latest_ncci, "%Y-%m-%d").date()
                ncci_days_old = (date.today() - ncci_date).days
                ncci_fresh = ncci_days_old < 100
            except ValueError:
                pass
        sources["ncci_edits"] = {
            "name": "NCCI Unbundling Edits",
            "latest_date": latest_ncci,
            "days_old": ncci_days_old,
            "expected_frequency": "Quarterly (Jan/Apr/Jul/Oct)",
            "fresh": ncci_fresh,
            "warning": None if ncci_fresh else (
                "NCCI edits were last updated over 3 months ago. "
                "Some recent coding changes may not be reflected."
            ),
        }

        # Hospital profiles
        row = db.execute("SELECT COUNT(*) as cnt FROM hospital_profiles").fetchone()
        profile_count = row["cnt"] if row else 0
        sources["hospital_profiles"] = {
            "name": "Hospital Profiles",
            "count": profile_count,
            "expected_frequency": "Annual (chargemaster) + crowdsourced",
            "fresh": profile_count > 0,
            "warning": None if profile_count > 0 else "No hospital profiles loaded.",
        }

        # Rate row counts for general health
        row = db.execute("SELECT COUNT(*) as cnt FROM medicare_rates").fetchone()
        sources["medicare_row_count"] = row["cnt"] if row else 0

        row = db.execute("SELECT COUNT(*) as cnt FROM ncci_edits").fetchone()
        sources["ncci_row_count"] = row["cnt"] if row else 0

    return sources


def get_data_freshness_warnings(date_of_service: date | str) -> list[str]:
    """
    Return user-facing warnings about data freshness relative to a bill's date of service.
    """
    if isinstance(date_of_service, str):
        try:
            date_of_service = datetime.strptime(date_of_service, "%Y-%m-%d").date()
        except ValueError:
            return ["Could not parse date of service for freshness check."]

    warnings = []

    with get_db() as db:
        row = db.execute("SELECT MAX(effective_year) as yr FROM medicare_rates").fetchone()
        latest_pfs = row["yr"] if row else None

        row = db.execute("SELECT MAX(effective_date) as dt FROM ncci_edits").fetchone()
        latest_ncci_str = row["dt"] if row else None

    if latest_pfs and date_of_service.year > latest_pfs:
        warnings.append(
            f"Your bill is from {date_of_service.year} but our Medicare rates "
            f"are from {latest_pfs}. Rates may differ slightly."
        )

    if latest_pfs and date_of_service.year < latest_pfs:
        warnings.append(
            f"Your bill is from {date_of_service.year}. We're using {latest_pfs} rates, "
            f"which may differ slightly from {date_of_service.year} rates."
        )

    if latest_ncci_str:
        try:
            latest_ncci = datetime.strptime(latest_ncci_str, "%Y-%m-%d").date()
            if (date.today() - latest_ncci).days > 100:
                warnings.append(
                    "Our bundling rules were last updated over 3 months ago. "
                    "Some recent coding changes may not be reflected."
                )
        except ValueError:
            pass

    return warnings
