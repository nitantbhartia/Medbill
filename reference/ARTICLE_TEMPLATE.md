# Article Template for BillKarma Guides

Use this template when creating new articles in `guide_*.py` files. Every
article registers itself with the guides system and gets served at
`/guides/{slug}`.

---

## Quality Checklist (target: 8+/10)

Before publishing, verify every item:

- [ ] **Lead paragraph** has a specific stat and dollar amount (not generic)
- [ ] **Table of contents** with anchor links to every section
- [ ] **Annotated example** — a real-looking bill, EOB, or document with
      highlighted errors and dollar amounts (use `.bill-example` markup)
- [ ] **3+ case studies** — concrete examples with CPT codes, dollar amounts,
      and outcomes (use `.case-study` markup)
- [ ] **2+ data tables** — comparisons, pricing breakdowns, or cost tables
- [ ] **Calculator embed** — at least 1 `_embed()` call where the reader would
      naturally want to look something up
- [ ] **Internal links** — natural links to `/calculator`, `/scan`,
      `/hospitals/`, and other guides (minimum 4 internal links)
- [ ] **5+ FAQs** with FAQPage schema (structured in `faqs` list)
- [ ] **Sources section** — 5+ authoritative external links (CMS, KFF, CFPB,
      Health Affairs, etc.)
- [ ] **Key takeaway callouts** — 2+ `.key-takeaway` boxes for scannable
      highlights
- [ ] **8th grade reading level** — plain language, jargon defined on first use
- [ ] **Follows PRODUCT_CONTEXT.md** — approved language only, no forbidden
      terms

---

## File Structure

Create a new file: `guide_{topic_slug}.py`

```python
"""Guide: {Title of the Article}."""

from guides import register, _embed

register("{url-slug}", {
    "title": "{Full Article Title}",
    "meta_description": "{150-160 chars. Include primary keyword, a number, and a benefit.}",
    "published": "{YYYY-MM-DD}",
    "author": "BillKarma Team",
    "category": "{Category Name}",
    "faqs": [
        {
            "q": "{Question as users would search it on Google?}",
            "a": "{Concise 2-3 sentence answer. Include a specific number or fact. This appears in FAQPage schema and may show in Google featured snippets.}",
        },
        # ... 5-6 FAQs total
    ],
    "body": f"""
{ARTICLE_BODY_HTML}
""",
})
```

Then add the import to `guides.py`:
```python
import guide_{topic_slug}
```

---

## Article Body HTML Template

```html
<p class="lead">{Opening stat or hook with a specific dollar amount.
Link to source if possible. 2-3 sentences max.}</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#section-1">{Section 1 title}</a></li>
        <li><a href="#section-2">{Section 2 title}</a></li>
        <!-- ... 6-9 sections typical -->
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="section-1">1. {Section title}</h2>

<p>{Body text. Keep paragraphs short — 2-4 sentences. Define jargon inline
on first use: "CPT code (the standard 5-digit billing code for a medical
service)."}</p>

<!-- DATA TABLE — use for comparisons, pricing, anything with numbers -->
<table>
    <thead>
        <tr><th>{Column 1}</th><th>{Column 2}</th><th>{Column 3}</th></tr>
    </thead>
    <tbody>
        <tr><td>{data}</td><td>{data}</td><td>{data}</td></tr>
    </tbody>
</table>

<!-- ANNOTATED BILL/DOCUMENT EXAMPLE -->
<div class="bill-example">
    <div class="bill-header">{Document title — Date of Service}</div>
    <div class="line-item">
        <span>{CPT code} — {Description}</span>
        <span>${amount}</span>
    </div>
    <div class="line-item flagged">
        <!-- Yellow highlight for markups/warnings -->
        <span>{CPT code} — {Description} &nbsp; &#9888; <em>{Warning text}</em></span>
        <span>${amount}</span>
    </div>
    <div class="line-item error">
        <!-- Red highlight for clear errors -->
        <span>{CPT code} — {Description} &nbsp; &#10060; <em>{Error text}</em></span>
        <span>${amount}</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>${total}</span>
    </div>
</div>

<!-- KEY TAKEAWAY — use 2-3 per article for scannable highlights -->
<div class="key-takeaway">
    <strong>{Bold summary.}</strong> {1-2 sentence supporting detail.}
</div>

<!-- CASE STUDY — use for real-world examples with dollar outcomes -->
<div class="case-study">
    <h3>{Example title: brief description}</h3>
    <p>{Setup: what happened, with CPT codes and dollar amounts.}</p>
    <p>{Outcome with bold savings amount.}
    <strong>Total savings: ${amount}.</strong></p>
</div>

<!-- CALCULATOR EMBED — place where the reader would naturally want to look up -->
{_embed(mode="cost", title="{Action-oriented title}", subtitle="{Brief instruction}.")}
{_embed(mode="markup", title="{Action-oriented title}", subtitle="{Brief instruction}.", height="420")}

<!-- INTERNAL LINKS — weave naturally into body text -->
<a href="/calculator">cost calculator</a>
<a href="/scan">upload your bill to BillKarma</a>
<a href="/hospitals/">hospital pricing directory</a>
<a href="/guides/{other-slug}">{other article title}</a>

<!-- FAQ SECTION — always the second-to-last section -->
<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>{Question exactly as it appears in the faqs list?}</h3>
        <p>{Answer — can be slightly expanded from the faqs list version.
        Include internal links where relevant.}</p>
    </div>
    <!-- ... repeat for each FAQ -->
</div>

<!-- SOURCES — always the last section -->
<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="{url}" target="_blank" rel="noopener">{Source: Description (Year)}</a></li>
    <!-- 5-6 authoritative sources -->
</ul>
```

---

## Available CSS Classes

| Class | Element | Effect |
|---|---|---|
| `lead` | `<p>` | Larger text, lime-green left border. Use for opening paragraph only. |
| `toc` | `<nav>` | White card with rounded corners for table of contents. |
| `key-takeaway` | `<div>` | Lime-green background callout box. Use for critical points. |
| `case-study` | `<div>` | White card with lime-green left border. Use for examples with outcomes. |
| `bill-example` | `<div>` | Monospace document mock-up. Use for annotated bills/EOBs. |
| `line-item` | `<div>` | Row inside `bill-example`. Flex layout with dotted border. |
| `line-item flagged` | `<div>` | Yellow-highlighted row (warnings, markups). |
| `line-item error` | `<div>` | Red-highlighted row (clear errors). |
| `line-total` | `<div>` | Bold total row with solid top border. |
| `faq-section` | `<div>` | Container for FAQ items. |
| `faq-item` | `<div>` | White card for individual FAQ. |
| `sources-list` | `<ul>` | Unstyled list with bottom borders between items. |

---

## Calculator Embed Modes

```python
# Mode: "cost" — Look up what Medicare pays for a CPT code
_embed(mode="cost", title="Look up a CPT code", subtitle="See the Medicare rate.")

# Mode: "markup" — Compare a charged amount against Medicare rates
_embed(mode="markup", title="Is your charge too high?", subtitle="Enter the CPT code and amount.", height="420")

# Pre-fill a CPT code
_embed(mode="cost", cpt="99284", title="Your ER visit level", subtitle="See what Medicare pays.")
```

---

## Categories Used

| Category | Topics |
|---|---|
| Billing Basics | Reading bills, understanding charges, CPT codes |
| Taking Action | Disputing bills, writing letters, making calls |
| ER Bills | Emergency room specific costs, levels, markups |
| Patient Rights | No Surprises Act, balance billing, legal protections |
| Negotiation | Negotiating bills, payment plans, financial assistance |
| Insurance Basics | EOBs, claims, denials, appeals |

---

## SEO Meta Description Formula

```
{Primary keyword} + {specific number/stat} + {benefit to reader}
```

Examples:
- "Learn how to decode every line on a medical bill. Understand CPT codes,
  Medicare rates, and how to identify billing errors that could save you
  hundreds."
- "The average ER visit costs $2,200 before insurance. Learn why ER bills
  are so expensive, what each charge actually covers, and 6 proven ways to
  reduce your bill."

Keep to 150-160 characters. Include the primary keyword in the first 60
characters for mobile SERP display.

---

## Voice & Tone Reminders

- **Knowledgeable, calm friend** — not corporate, not medical professional,
  not lawyer
- **Empowering, not alarming** — lead with what they can do
- **Precise with numbers** — always cite CPT codes, dollar amounts, Medicare
  rates
- **Neutral toward providers** — billing mistakes, not accusations
- **8th grade reading level** — define jargon inline on first use
- **Action-oriented** — every section should end with something the reader
  can do

See `reference/PRODUCT_CONTEXT.md` for full approved/forbidden language lists.
