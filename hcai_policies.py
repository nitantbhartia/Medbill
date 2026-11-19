"""Read hospital policy pages that California's HCAI posts: which hospitals exist, where they are, and their policy files."""

from __future__ import annotations

import re
from datetime import datetime
from html import unescape
from urllib.request import Request, urlopen

import config

USER_AGENT = "Mozilla/5.0 (compatible; BillKarma policy research)"
POLICY_LINK = re.compile(
    r'<span class="date">\s*(\d\d/\d\d/\d{4})\s*</span>.*?<a href="(https://api\.hdc\.hcai\.ca\.gov/Public/Extract/Attachment\?id=[\w-]+)">\s*(.*?)\s*</a>',
    re.S)
ADDRESS = re.compile(r"(\d[^<]{3,80}?),\s*([A-Z][A-Z .'-]+),\s*CA\s*(\d{5})")


def _get(url: str) -> str:
    with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=60) as response:
        return response.read().decode("utf-8", errors="ignore")


def hospital_page_urls() -> list[str]:
    return sorted(set(re.findall(r"<loc>([^<]+)</loc>", _get(config.HCAI_POLICIES_SITEMAP))))


def _newest(links: list[tuple[str, str, str]], label: str) -> tuple[str, str] | None:
    matching = [(datetime.strptime(date, "%m/%d/%Y"), url, date) for date, url, text in links if text == label]
    if not matching:
        return None
    _, url, date = max(matching)
    return url, date


def parse_page(html: str) -> dict:
    """Name, address, license and the newest charity care policy, discount policy and application on one hospital's page."""
    title = re.search(r"<title>(.*?)\s*-\s*HCAI", html, re.S)
    address = ADDRESS.search(unescape(re.sub(r"<[^>]+>", " ", html)))
    license_number = re.search(r"License #:\s*(\d+)", re.sub(r"<[^>]+>", " ", html))
    links = [(date, url, re.sub(r"<[^>]+>|\s+", " ", unescape(text)).strip()) for date, url, text in POLICY_LINK.findall(html)]
    charity, discount = _newest(links, "Charity Care Policy"), _newest(links, "Discount Payment Policy")
    application = _newest(links, "Application for Charity Care") or _newest(links, "Application for Discount Payment")
    return {
        "name": unescape(title.group(1)).strip() if title else None,
        "city": address.group(2).title() if address else None,
        "zip": address.group(3) if address else None,
        "license": license_number.group(1) if license_number else None,
        "charity_policy": charity, "discount_policy": discount,
        "application_form_url": application[0] if application else None,
    }


def fetch_hospital(url: str) -> dict:
    return {**parse_page(_get(url)), "page_url": url}
