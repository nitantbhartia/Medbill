#!/usr/bin/env python3
"""Validate CTA placement in guide_*.py files.

Each guide must have exactly 3 CTAs (key-takeaway divs with hrefs)
distributed through the article body:
  CTA #1:  0–35%   (after first data table, ~25%)
  CTA #2: 40–65%   (after how-to steps, ~55%)
  CTA #3: 60–82%   (just before case studies, ~75%)
"""
import re
import sys

CTA_RULES = [
    ("CTA #1",  0, 40),
    ("CTA #2", 30, 67),
    ("CTA #3", 55, 85),
]


def extract_body(text):
    m = re.search(r'"body":\s*f?"""(.*?)"""', text, re.DOTALL)
    return m.group(1) if m else None


def find_ctas(body):
    positions = []
    for m in re.finditer(r'<div class="key-takeaway">', body):
        snippet = body[m.start(): m.start() + 600]
        if "href=" in snippet:
            positions.append(m.start())
    return positions


def check_file(path):
    text = open(path).read()
    body = extract_body(text)
    if not body:
        return [f"  could not find body string"]

    ctas = find_ctas(body)
    errors = []

    if len(ctas) != 3:
        errors.append(f"  expected 3 CTAs with hrefs, found {len(ctas)}")
        return errors

    body_len = len(body)
    for i, (label, lo, hi) in enumerate(CTA_RULES):
        pct = round(ctas[i] / body_len * 100)
        if not (lo <= pct <= hi):
            errors.append(
                f"  {label} is at {pct}% — must be {lo}–{hi}%"
                f" (move it {'earlier' if pct > hi else 'later'} in the article)"
            )

    return errors


def main(files):
    failed = []
    for path in files:
        if not path.endswith(".py"):
            continue
        fname = path.split("/")[-1]
        if not fname.startswith("guide_"):
            continue
        errors = check_file(path)
        if errors:
            failed.append((fname, errors))

    if not failed:
        return 0

    print("❌  CTA placement check failed:\n")
    for fname, errors in failed:
        print(f"  {fname}:")
        for e in errors:
            print(e)
    print()
    print("  Rules: CTA #1 at 0–35%, CTA #2 at 40–65%, CTA #3 at 60–82%")
    print("  Place CTAs at: after first table (~25%), after how-to steps (~55%),")
    print("  just before case studies (~75%). See reference/ARTICLE_TEMPLATE.md.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
