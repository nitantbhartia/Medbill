"""Billing contact extraction rules: parse a hospital page and find its billing phone, address and links.

Rules are strict on purpose: a wrong billing number is worse than none. A phone or address is
returned only when exactly one distinct candidate on the page qualifies.
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
CALL_CUE_RE = re.compile(r"\b(call|phone|telephone|dial|tel)\b", re.I)
MAIL_CUE_RE = re.compile(r"\b(mail|mailed|mailing|send|remit|payable)\b", re.I)
SENTENCE_BREAK_RE = re.compile(r"[.!?]\s+[A-Z]")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[-.\s]?)?\(?([2-9]\d{2})\)?[-.\s]?([2-9]\d{2})[-.\s]?(\d{4})(?!\d)")
STREET_SUFFIX = (
    r"Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Way|Parkway|Pkwy|Lane|Ln|"
    r"Highway|Hwy|Place|Pl|Court|Ct"
)
ADDRESS_RE = re.compile(
    rf"(?:(?i:P\.?\s?O\.?\s?Box)\s+\d+|\d{{1,6}}\s+(?:[A-Za-z0-9'\-]+\.?\s+){{0,4}}?(?:{STREET_SUFFIX})\.?)"
    r"\s*,?\s*[A-Za-z .'-]{2,40}?,?\s+[A-Z]{2}\s+\d{5}(?:-\d{4})?"
)
PO_BOX_RE = re.compile(r"P\.?\s?O\.?\s?Box", re.I)
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
        self.links: list[tuple[str, str]] = []
        self._hidden_depth = 0
        self._href: str | None = None
        self._anchor_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._hidden_depth += 1
        elif tag == "a":
            self._href = (dict(attrs).get("href") or "").strip()
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
    return Page(text=text, links=parser.links)


def _format_phone(digits: str) -> str:
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def _keyword_spans(text: str) -> list[tuple[int, int]]:
    return [m.span() for m in BILLING_KEYWORD_RE.finditer(text)]


def _nearest_keyword_before(start: int, keywords: list[tuple[int, int]]) -> tuple[int, int] | None:
    before = [span for span in keywords if span[1] <= start]
    return max(before, key=lambda span: span[1], default=None)


def _is_billing_phone(text: str, start: int, keywords: list[tuple[int, int]]) -> bool:
    nearest = _nearest_keyword_before(start, keywords)
    if nearest is None:
        return False
    keyword_start, keyword_end = nearest
    if start - keyword_end > config.BILLING_CONTACT_KEYWORD_WINDOW_CHARS:
        return False
    if SENTENCE_BREAK_RE.search(text[keyword_end:start]):
        return False
    cue_zone = text[max(0, keyword_start - config.BILLING_CONTACT_CALL_CUE_CHARS):start]
    return CALL_CUE_RE.search(cue_zone) is not None


def find_billing_phone(page: Page) -> str | None:
    keywords = _keyword_spans(page.text)
    numbers = {
        "".join(match.groups())
        for match in PHONE_RE.finditer(page.text)
        if _is_billing_phone(page.text, match.start(), keywords)
    }
    return _format_phone(numbers.pop()) if len(numbers) == 1 else None


def _is_mailing_address(text: str, match: re.Match, keywords: list[tuple[int, int]]) -> bool:
    start, end = match.span()
    window = config.BILLING_CONTACT_KEYWORD_WINDOW_CHARS
    if not any(max(0, k_start - end, start - k_end) <= window for k_start, k_end in keywords):
        return False
    if PO_BOX_RE.match(match.group(0)):
        return True
    cue_zone = text[max(0, start - config.BILLING_CONTACT_MAIL_CUE_CHARS):start]
    return MAIL_CUE_RE.search(cue_zone) is not None


def find_billing_address(page: Page) -> str | None:
    keywords = _keyword_spans(page.text)
    addresses = {
        match.group(0)
        for match in ADDRESS_RE.finditer(page.text)
        if _is_mailing_address(page.text, match, keywords)
    }
    return addresses.pop() if len(addresses) == 1 else None


def find_link(page: Page, pattern: re.Pattern, page_url: str) -> str | None:
    """First link to a different page whose wording matches. A link back to this page says nothing useful."""
    for href, anchor_text in page.links:
        if not pattern.search(f"{anchor_text} {href}"):
            continue
        absolute = urljoin(page_url, href).split("#")[0]
        if urlparse(absolute).scheme in ("http", "https") and absolute != page_url.split("#")[0]:
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


def site_root(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}/"


def root_from_stored_urls(urls: list[str | None]) -> str | None:
    for url in urls:
        parsed = urlparse(url or "")
        host = parsed.hostname or ""
        if parsed.scheme not in ("http", "https") or not host or _is_shared_host(host):
            continue
        return site_root(url)
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
    # Shallowest first: a general billing page beats a single clinic's payment page reached from the same nav.
    nav_urls.sort(key=lambda url: urlparse(url).path.count("/"))
    fixed_urls = [urljoin(root, path) for path in BILLING_PATHS]
    urls = list(dict.fromkeys(nav_urls[: config.BILLING_CONTACT_MAX_NAV_LINKS] + fixed_urls))
    return [url for url in urls if url != root]
