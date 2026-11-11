# SEO context: BillKarma

Built from the code on 2026-11-11. Each fact names its source. If the code changes, the code wins.

## Product

BillKarma checks a hospital bill against what Medicare pays for each code, flags errors, and for a flat fee sends a written dispute to the hospital billing office, with follow-ups. Source: `reference/POSITIONING.md`, `dispute_service.py`.

## Buyer

Someone holding a hospital or facility bill that looks wrong or too high: uninsured or self-pay patients, insured patients with a big balance after insurance, and bills heading to collections. Source: `reference/POSITIONING.md`.

## Conversion

1. Free bill check started at `/scan` (primary).
2. Paid dispute activated at `/dispute/activate/{bill_id}`.

## Prices

Source: `config.py`.

| Offer | Price |
| --- | --- |
| Bill check, itemized-bill letter, financial assistance check | Free |
| Written dispute, bill under $1,000 | $29 |
| Written dispute, $1,000 to $5,000 | $49 |
| Written dispute, $5,000 to $20,000 | $99 |
| Written dispute, over $20,000 | $149 |
| Debt validation letter, sent certified | $19 |
| Charity-care application, sent certified | $9 |

Dispute follow-ups go out on days 7, 14, 30 and 45 (`DISPUTE_FOLLOWUP_DAYS`).

## Limits and claims we must not make

From `reference/POSITIONING.md` and `reference/PRODUCT_CONTEXT.md`:

- No phone negotiation, no guaranteed reduction, no legal advice.
- Insurance denials are not a core offer (the `/appeal` route exists but isn't promoted).
- Don't use the words in the "Forbidden language" table of `PRODUCT_CONTEXT.md`.

## Site assets

- 6,000+ hospital pages with a Medicare-markup billing grade (`hospital_seo.py`, `/hospitals/...`).
- ~390 live guides (`guides.py`, `guide_*.py`); duplicates redirect through `GUIDE_REDIRECTS`.
- State rights pages (`/rights/`), procedure cost pages, a glossary, `llms.txt`.
- Titles and metas: guides in `guide_seo.py`, hospitals in `hospital_seo.py`.

## Competitors

Fees as published by each company, checked 2026-11-11.

| Name | Model | Source |
| --- | --- | --- |
| Resolve | Human advocates; $250/$499 refundable deposit; 25% of savings (min fee $1,000, at most 50% of savings) under $15k, 10% (min $2,500) at $15k+ | [Resolve pricing FAQ](https://resolvemedicalbills.com/faqs/how-much-does-it-cost-to-work-with-resolve) |
| Goodbill | Software + experts, 20% of savings | [Goodbill help](https://help.goodbill.com/en/articles/254209) |
| CareRoute | 18–25% of savings, $1,000 cap | [CareRoute](https://www.careroute.ai/bill-defense) |
| MyCareCost | Self-serve data and scripts, $0–18 per search | [MyCareCost](https://mycarecost.net/compare/fairmedbill) |
| Dollar For | Nonprofit, free charity-care applications | [CareRoute comparison](https://www.careroute.ai/bill-defense/compare-medical-bill-negotiation-services) |

## Data sources

- Search Console: **not connected.** Unlocks real positions, clicks and the page-2 list. Verification tag reads `GOOGLE_SITE_VERIFICATION` from the environment.
- Rank/volume tool (Ahrefs or similar): **not connected.** Unlocks keyword volume and difficulty in `keyword-map.csv`.
- Analytics: not found in the repo.
