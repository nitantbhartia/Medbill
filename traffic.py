"""Where visitors come from: a named source per landing, counted per day, and carried onto the scan.

The source is, in order: a ?ref= or ?utm_source= on the link, the in-app browser (Instagram, TikTok and
Facebook open links inside their own browser and often send no referrer), then the referring site.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

from fastapi import Request

import config
from db import get_db
from referrals import valid_referral

IN_APP_BROWSERS = (("instagram", "instagram"), ("musical_ly", "tiktok"), ("tiktok", "tiktok"), ("bytedancewebview", "tiktok"),
                   ("fban", "facebook"), ("fbav", "facebook"), ("snapchat", "snapchat"), ("pinterest", "pinterest"),
                   ("linkedinapp", "linkedin"), ("twitter", "x"))
REFERRER_SITES = (("instagram.", "instagram"), ("tiktok.", "tiktok"), ("facebook.", "facebook"), ("fb.", "facebook"),
                  ("youtube.", "youtube"), ("youtu.be", "youtube"), ("reddit.", "reddit"), ("t.co", "x"), ("twitter.", "x"),
                  ("x.com", "x"), ("linkedin.", "linkedin"), ("lnkd.in", "linkedin"), ("pinterest.", "pinterest"),
                  ("threads.", "threads"), ("google.", "google"), ("bing.", "bing"), ("duckduckgo.", "duckduckgo"),
                  ("chatgpt.", "chatgpt"), ("openai.", "chatgpt"), ("perplexity.", "perplexity"), ("claude.", "claude"))
BOT_RE = re.compile(r"bot|crawl|spider|externalhit|preview|scraper|curl|python|headless|monitor|facebookcatalog", re.I)


def source_of(request: Request) -> str | None:
    """The traffic source of this request, or None when it has none (a direct visit or our own pages)."""
    params = request.query_params
    tagged = valid_referral((params.get("ref") or params.get("utm_source") or "").strip().lower())
    if tagged:
        return tagged
    agent = (request.headers.get("user-agent") or "").lower()
    for marker, source in IN_APP_BROWSERS:
        if marker in agent:
            return source
    host = (urlparse(request.headers.get("referer") or "").hostname or "").lower()
    if not host or host.endswith(urlparse(config.APP_URL).hostname or ""):
        return None
    for marker, source in REFERRER_SITES:
        if host.startswith(marker) or f".{marker}" in f".{host}":
            return source
    return valid_referral(host.removeprefix("www.").replace(".", "-")[:40])


def is_page_visit(request: Request) -> bool:
    """A person loading a page: not a bot, an API call, a static file or a link-preview fetch."""
    path = request.url.path
    return (request.method == "GET" and not path.startswith(("/api/", "/static/", "/.well-known/", "/badge/", "/mcp"))
            and "." not in path.rsplit("/", 1)[-1] and not BOT_RE.search(request.headers.get("user-agent") or "bot"))


def record_landing(source: str) -> None:
    with get_db() as db:
        db.execute(
            "INSERT INTO traffic_landings (day, source, landings) VALUES (date('now'), ?, 1) "
            "ON CONFLICT(day, source) DO UPDATE SET landings = landings + 1",
            (source,),
        )


def source_report(days: int) -> list[dict]:
    """Per source over the last `days`: visitors who landed, and bills they went on to scan."""
    since = f"-{days} days"
    with get_db() as db:
        landings = db.execute(
            "SELECT source, SUM(landings) AS landings, MAX(day) AS last_day FROM traffic_landings "
            "WHERE day >= date('now', ?) GROUP BY source", (since,),
        ).fetchall()
        scans = db.execute(
            "SELECT referral_code AS source, COUNT(*) AS scans FROM bills "
            "WHERE referral_code IS NOT NULL AND created_at >= datetime('now', ?) GROUP BY referral_code", (since,),
        ).fetchall()
    report = {row["source"]: {"source": row["source"], "landings": row["landings"], "last_day": row["last_day"], "scans": 0}
              for row in landings}
    for row in scans:
        report.setdefault(row["source"], {"source": row["source"], "landings": 0, "last_day": None, "scans": 0})["scans"] = row["scans"]
    return sorted(report.values(), key=lambda r: (-r["landings"], -r["scans"], r["source"]))
