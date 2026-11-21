"""ClaimCoach universal links: the apple-app-site-association file served on claimcoach.app."""

import config


def is_claimcoach_host(host: str) -> bool:
    hostname = host.split(":")[0].lower()
    return hostname in (config.CC_DOMAIN, f"www.{config.CC_DOMAIN}")


def apple_app_site_association() -> dict:
    app_id = f"{config.APPLE_TEAM_ID}.{config.CC_BUNDLE_ID}"
    components = [{"/": path} for path in config.CC_UNIVERSAL_LINK_PATHS]
    return {"applinks": {"details": [{"appIDs": [app_id], "components": components}]}}
