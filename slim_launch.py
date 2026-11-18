"""Pages and API routes hidden while the site sells only the Bill Check Report (config.SLIM_LAUNCH).

Hidden pages redirect to the free scan; hidden API routes answer 404. Nothing is deleted:
set SLIM_LAUNCH=0 to bring every product back.
"""

HIDDEN_PAGE_PREFIXES = (
    "/advocacy",
    "/dispute",
    "/autopilot",
    "/advisor",
    "/appeal",
    "/household",
    "/fight-debt",
    "/collection-notice",
    "/charity-care",
    "/settle-debt",
    "/score",
)

HIDDEN_API_PREFIXES = (
    "/api/advocacy",
    "/api/dispute",
    "/api/appeal",
    "/api/appeals",
    "/api/household",
    "/api/negotiate",
    "/api/debt",
    "/api/claims",
    "/api/advisor",
    "/api/autopilot",
    "/api/collection-notice",
    "/api/charity-care/checkout",
    "/api/charity-care/application",
    "/api/settlement",
    "/api/concierge-interest",
    "/api/dispute-outcome",
    "/api/phone-script",
    "/api/message-script",
    "/api/appeal-playbook",
    "/api/appeal-template",
)

# Free API routes whose names start like a hidden prefix.
ALLOWED_API_PATHS = (
    "/api/dispute-letter/",
    "/api/dispute-phone-script/",
    "/api/dispute-packet/",
    "/api/dispute-stats",
)


def _matches(path: str, prefix: str) -> bool:
    return path == prefix or path.startswith(prefix + "/")


def hidden_kind(path: str) -> str | None:
    """'api' or 'page' when the path belongs to a hidden product, else None."""
    if any(path.startswith(allowed) for allowed in ALLOWED_API_PATHS):
        return None
    if any(_matches(path, prefix) for prefix in HIDDEN_API_PREFIXES):
        return "api"
    if any(_matches(path, prefix) for prefix in HIDDEN_PAGE_PREFIXES):
        return "page"
    return None
