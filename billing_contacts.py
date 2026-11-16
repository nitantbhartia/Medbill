"""Billing contact extraction rules: parse a hospital page and find its billing phone, address and links.

A phone or address counts only when it sits within a few hundred characters of a billing keyword.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import config

BILLING_PATHS = (
    "/billing",
    "/pay-your-bill",
    "/pay-bill",
    "/patients/billing",
    "/patients-visitors/billing",
    "/patient-financial-services",
    "/financial-assistance",
)
NAV_LINK_RE = re.compile(r"bill|pay|financial assistance", re.I)
FINANCIAL_LINK_RE = re.compile(r"financial assistance|charity care", re.I)
PAYMENT_LINK_RE = re.compile(r"pay[- ](your[- ])?bill|pay[- ]online|make a payment|pay[- ]now|bill[- ]pay", re.I)
BILLING_KEYWORD_RE = re.compile(
    r"billing|patient financial services|business office|pay your bill|account questions", re.I
)
PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[-.\s]?)?\(?([2-9]\d{2})\)?[-.\s]?([2-9]\d{2})[-.\s]?(\d{4})(?!\d)")
ADDRESS_RE = re.compile(
    r"(?:P\.?\s?O\.?\s?Box\s+\d+|\d{1,6}\s+[A-Za-z0-9.'\- ]{2,50}?)"
    r"\s*,?\s*[A-Za-z .'-]{2,40}?,?\s+[A-Z]{2}\s+\d{5}(?:-\d{4})?"
)
# Hosts that serve files for many organizations; a domain from them says nothing about one hospital.
SHARED_HOST_SUFFIXES = (
    "cms.gov", "medicare.gov", "irs.gov", "amazonaws.com", "cloudfront.net", "googleapis.com",
    "github.com", "githubusercontent.com", "dropbox.com", "box.com", "sharepoint.com",
    "windows.net", "dolthub.com",
)
GENERIC_NAME_WORDS = frozenset({
    "hospital", "hospitals", "medical", "center", "centre", "health", "healthcare", "regional",
    "general", "system", "community", "university", "clinic", "campus", "services",
})


@dataclass
class Page:
    text: str
    tel_numbers: set[str]
    links: list[tuple[str, str]]


@dataclass
class BillingContact:
    source_url: str
    billing_phone: str | None = None
    billing_address: str | None = None
    financial_assistance_url: str | None = None
    payment_url: str | None = None

    def has_data(self) -> bool:
        return any((self.billing_phone, self.billing_address, self.financial_assistance_url, self.payment_url))


class _PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text_parts: list[str] = []
        self.tel_numbers: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self._hidden_depth = 0
        self._href: str | None = None
        self._anchor_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._hidden_depth += 1
        elif tag == "a":
            href = (dict(attrs).get("href") or "").strip()
            if href.lower().startswith("tel:"):
                number = _ten_digits(href[4:])
                if number:
                    self.tel_numbers.add(number)
            self._href = href
            self._anchor_parts = []

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._hidden_depth = max(0, self._hidden_depth - 1)
        elif tag == "a" and self._href is not None:
            self.links.append((self._href, " ".join(self._anchor_parts)))
            self._href = None

    def handle_data(self, data):
        if self._hidden_depth:
            return
        self.text_parts.append(data)
        if self._href is not None:
            self._anchor_parts.append(data)


def parse_page(html_text: str) -> Page:
    parser = _PageParser()
    parser.feed(html_text)
    parser.close()
    text = re.sub(r"\s+", " ", " ".join(parser.text_parts)).strip()
    return Page(text=text, tel_numbers=parser.tel_numbers, links=parser.links)


def _ten_digits(raw: str) -> str | None:
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if len(digits) == 10 else None


def _format_phone(digits: str) -> str:
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def _gap_to_keyword(span: tuple[int, int], keyword_spans: list[tuple[int, int]]) -> int | None:
    start, end = span
    gaps = [max(0, k_start - end, start - k_end) for k_start, k_end in keyword_spans]
    return min(gaps, default=None)


def _chars_after_keyword(span: tuple[int, int], keyword_spans: list[tuple[int, int]]) -> int | None:
    start = span[0]
    gaps = [start - k_end for _, k_end in keyword_spans if k_end <= start]
    return min(gaps, default=None)


def _keyword_spans(text: str) -> list[tuple[int, int]]:
    return [m.span() for m in BILLING_KEYWORD_RE.finditer(text)]


def _near_billing_keyword(span: tuple[int, int], keywords: list[tuple[int, int]]) -> bool:
    gap = _gap_to_keyword(span, keywords)
    return gap is not None and gap <= config.BILLING_CONTACT_KEYWORD_WINDOW_CHARS


def find_billing_phone(page: Page) -> str | None:
    keywords = _keyword_spans(page.text)
    candidates = []
    for match in PHONE_RE.finditer(page.text):
        # Billing numbers follow their label ("call billing at ..."); a number just before the label belongs to another line.
        gap = _chars_after_keyword(match.span(), keywords)
        if gap is None or gap > config.BILLING_CONTACT_KEYWORD_WINDOW_CHARS:
            continue
        number = "".join(match.groups())
        # Closest after a keyword wins; a tel: link only breaks an exact tie.
        candidates.append((gap, number not in page.tel_numbers, number))
    if not candidates:
        return None
    return _format_phone(min(candidates)[2])


def find_billing_address(page: Page) -> str | None:
    keywords = _keyword_spans(page.text)
    candidates = []
    for match in ADDRESS_RE.finditer(page.text):
        if _near_billing_keyword(match.span(), keywords):
            candidates.append((_gap_to_keyword(match.span(), keywords), match.group(0)))
    return min(candidates)[1] if candidates else None


def find_link(page: Page, pattern: re.Pattern, page_url: str) -> str | None:
    for href, anchor_text in page.links:
        if not pattern.search(f"{anchor_text} {href}"):
            continue
        absolute = urljoin(page_url, href)
        if urlparse(absolute).scheme in ("http", "https"):
            return absolute
    return None


def extract_contact(page: Page, page_url: str) -> BillingContact:
    return BillingContact(
        source_url=page_url,
        billing_phone=find_billing_phone(page),
        billing_address=find_billing_address(page),
        financial_assistance_url=find_link(page, FINANCIAL_LINK_RE, page_url),
        payment_url=find_link(page, PAYMENT_LINK_RE, page_url),
    )


def _is_shared_host(host: str) -> bool:
    return any(host == suffix or host.endswith("." + suffix) for suffix in SHARED_HOST_SUFFIXES)


def root_from_stored_urls(urls: list[str | None]) -> str | None:
    for url in urls:
        parsed = urlparse(url or "")
        host = parsed.hostname or ""
        if parsed.scheme not in ("http", "https") or not host or _is_shared_host(host):
            continue
        return f"{parsed.scheme}://{parsed.netloc}/"
    return None


def name_tokens(name: str) -> list[str]:
    min_chars = config.BILLING_CONTACT_NAME_MIN_TOKEN_CHARS
    words = re.findall(r"[a-z]+", name.lower())
    return [w for w in words if len(w) >= min_chars and w not in GENERIC_NAME_WORDS]


def homepage_names_hospital(page: Page, name: str) -> bool:
    text = page.text.lower()
    return any(re.search(rf"\b{re.escape(token)}\b", text) for token in name_tokens(name))


def candidate_urls(root: str, home: Page) -> list[str]:
    host = urlparse(root).netloc
    nav_urls = []
    for href, anchor_text in home.links:
        absolute = urljoin(root, href)
        parsed = urlparse(absolute)
        if NAV_LINK_RE.search(anchor_text) and parsed.netloc == host and parsed.scheme in ("http", "https"):
            nav_urls.append(absolute)
    fixed_urls = [urljoin(root, path) for path in BILLING_PATHS]
    urls = list(dict.fromkeys(nav_urls[: config.BILLING_CONTACT_MAX_NAV_LINKS] + fixed_urls))
    return [url for url in urls if url != root]
