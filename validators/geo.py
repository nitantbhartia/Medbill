"""Geographic helpers for locality and benchmark region selection."""

import re

from db import get_db

# Conservative fallback when no mapping exists in DB.
ZIP_DIGIT_TO_REGION = {
    "0": "northeast",
    "1": "northeast",
    "2": "southeast",
    "3": "southeast",
    "4": "midwest",
    "5": "midwest",
    "6": "midwest",
    "7": "southeast",
    "8": "west",
    "9": "west",
}


def extract_zip(text: str | None) -> str | None:
    """Extract a 5-digit ZIP code from free text."""
    if not text:
        return None
    match = re.search(r"\b(\d{5})\b", text)
    return match.group(1) if match else None


def _lookup_zip_mapping(zip_code: str | None) -> dict | None:
    """Lookup best zip prefix match: 5-digit, then 3-digit, then 1-digit."""
    if not zip_code:
        return None
    zip_code = str(zip_code).strip()
    if len(zip_code) < 1:
        return None

    prefixes = [zip_code[:5], zip_code[:3], zip_code[:1]]
    with get_db() as db:
        for prefix in prefixes:
            row = db.execute(
                "SELECT locality, state, region FROM zip_locality_map WHERE zip_prefix = ?",
                (prefix,),
            ).fetchone()
            if row:
                return dict(row)
    return None


def get_preferred_zip(user_zip: str | None = None, provider_address: str | None = None) -> str | None:
    """Prefer provider ZIP when available, then user ZIP."""
    return extract_zip(provider_address) or (str(user_zip).strip() if user_zip else None)


def get_medicare_locality(user_zip: str | None = None, provider_address: str | None = None) -> str:
    """Resolve Medicare locality using ZIP mapping, then legacy state lookup."""
    preferred_zip = get_preferred_zip(user_zip, provider_address)
    mapping = _lookup_zip_mapping(preferred_zip)
    if mapping and mapping.get("locality"):
        return mapping["locality"]

    # Legacy fallback for backwards compatibility.
    if user_zip:
        with get_db() as db:
            row = db.execute(
                "SELECT DISTINCT locality FROM medicare_rates "
                "WHERE state = (SELECT state FROM users WHERE zip_code = ? LIMIT 1) LIMIT 1",
                (user_zip,),
            ).fetchone()
            if row and row["locality"]:
                return row["locality"]

    return "0000000"


def get_region(user_zip: str | None = None, provider_address: str | None = None) -> str:
    """Resolve benchmark region from ZIP mapping with digit-based fallback."""
    preferred_zip = get_preferred_zip(user_zip, provider_address)
    mapping = _lookup_zip_mapping(preferred_zip)
    if mapping and mapping.get("region"):
        return mapping["region"]

    if not preferred_zip:
        return "national"
    return ZIP_DIGIT_TO_REGION.get(preferred_zip[0], "national")
