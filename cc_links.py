"""ClaimCoach on claimcoach.app: the apple-app-site-association file and the four static pages."""

from pathlib import Path

import config

SITE_DIR = Path(__file__).parent / "claimcoach_site"
SITE_PAGES = {"/": "index.html", "/privacy": "privacy.html", "/terms": "terms.html", "/support": "support.html"}


def is_claimcoach_host(host: str) -> bool:
    hostname = host.split(":")[0].lower()
    return hostname in (config.CC_DOMAIN, f"www.{config.CC_DOMAIN}")


def apple_app_site_association() -> dict:
    app_id = f"{config.APPLE_TEAM_ID}.{config.CC_BUNDLE_ID}"
    components = [{"/": path} for path in config.CC_UNIVERSAL_LINK_PATHS]
    return {"applinks": {"details": [{"appIDs": [app_id], "components": components}]}}


def site_page(host: str, path: str) -> str | None:
    """The HTML for a claimcoach.app page, or None when the host or path is not one of them."""
    if not is_claimcoach_host(host):
        return None
    filename = SITE_PAGES.get(path.rstrip("/") or "/")
    if filename is None:
        return None
    return (SITE_DIR / filename).read_text(encoding="utf-8")
