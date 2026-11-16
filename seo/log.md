# SEO log

- 2026-11-11: Consolidated 22 duplicate-intent guides with one-hop 301s; removed 5 silently overwritten guide files; in-body links point at final URLs. (PR #130)
- 2026-11-11: New hospital page titles and metas lead with billing phone and Medicare markup; hand-written titles and metas for 23 core guides. (PR #130)
- 2026-11-11: Homepage refocused on the hospital-bill dispute with flat-fee tiers and "What we don't do". (PR #130)
- 2026-11-11: Fixed route shadowing that made `/guides/most-expensive-states-healthcare-2026/` and every `/guides/cheapest-cities-*-2026/` page return 404 despite being in the sitemap.
- 2026-11-11: Set up `seo/` (context, keyword map, backlog, AI prompts) and project SEO skills.
- 2026-11-11: Fixed a garbled homepage sentence; the pricing note now states the 45-day refund shown at checkout. (PR #133)
- 2026-11-11: New guides: /guides/medical-bill-negotiation-service-cost/ and /guides/billkarma-vs-resolve-medical-bills/, linked from the homepage and two guides.
- 2026-11-11: New /hospitals/{state}/most-expensive/ ranking pages (states with 5+ ranked hospitals), in the hospital sitemap and linked from each state page.

## 2026-11-11 (later)
- UI overhaul merged (PR #135): one header, page-header band, blue palette; /guides/ no longer lists all guides as cards.
- New guides: billkarma-vs-goodbill-medical-bills, upcoding-unbundling-hospital-bills, hospital-revenue-codes-explained. Auto-link table now points upcoding/unbundling/revenue code/UB-04 at them.
- Removed 'Medically reviewed' claims from guide pages. `_DEFAULT_REVIEWED` in guides.py still stamps a review date used in schema dateModified; replace with real dates when guides are actually reviewed.

## 2026-11-11 (MCP)
- /mcp live: stateless Streamable HTTP MCP server, 4 read-only tools, no auth. Setup page /ai; listed in llms.txt and footer. Links carry utm_source=ai_assistant so visits from assistants show up in analytics.
- Next: submit to the ChatGPT apps directory and Claude's Connectors Directory once it has been used in production for a while.


## 2026-11-15 (relaunch recrawl)
- Search Console: site was offline roughly Apr–Nov 8; impressions fell from ~3,000/day (Mar) to ~1/day. Pre-outage peak: 116k impressions, 407 clicks.
- All sitemap `<lastmod>` values now come from `config.SITE_UPDATED` (2026-11-11). They were hardcoded Jan–Apr dates, telling Google nothing had changed since the relaunch.
- Guide schema: removed the duplicate QAPage block (Search Console errors: missing answerCount); all JSON-LD fields now use `tojson`. 80 guides had invalid Article JSON (bad escapes), and 3 guides emitted blank FAQ questions because they use `question`/`answer` keys.
- Next (owner): resubmit sitemap.xml in Search Console; Request indexing for pre-outage top pages.

## 2026-11-16
- Hospital pages link the matching core guide from each step: call script (call billing), how financial assistance works, itemized-bill and dispute guides (send it in writing).
- Search Console review (Nov 2025 to Nov 13 2026): site total is small. Top page is the homepage (15 clicks). The guides with the most impressions (anesthesia-billing 1,344; stent-surgery-cost 1,136; hospital-drug-charges 918; stroke-treatment-cost 472) get 2 to 7 clicks each. Their average position looks like page 1, but anesthesia-billing's individual queries rank 60 to 98, so a title rewrite would not help; it needs a better page, not a better title. State guide pages: 2 clicks in total. No changes made from this review.
- hospital-drug-charges: meta description now leads with the numbers ($15–$50 per tablet, $180+ IV, up to 2,500x); new FAQ "How much does IV Tylenol cost in a hospital?" to answer the queries it already ranks 8–12 for. Only ~115 query-level impressions so far, so judge it after mid-December.

## 2026-11-16 (brand and indexing review)
- "billkarma" search shows Credit Karma and unrelated "karma" results; BillKarma absent. Zero brand queries in Search Console for the past year.
- Homepage title now leads with brand plus category ("BillKarma: Free Medical Bill Checker and Dispute Service"); schema gets `alternateName` and loses the self-referencing `sameAs` and the retired SiteLinksSearchBox node; About page states it isn't affiliated with Credit Karma or any finance app.
- Search Console: homepage last crawled Oct 27 as 404, `sitemap-guides.xml` has 1 error. Owner steps in backlog 1b.
- Sitemap audit: sitemap-guides, tools, rights, procedures all return 200 for every URL (429, 16, 50, 17 URLs, no duplicates). Core and cost sitemaps could not be audited locally without the production database.

## 2026-11-16 (full audit, `/seo audit`)
Scores from eight read-only agents on the live site (estimates, not Lighthouse): technical 68, content 34, schema 55, AI-search readiness 49, performance 82 (lab proxies), sitemap 69. Real measurements: mobile LCP about 1.0 to 1.1 s, CLS under 0.02, 33 to 40 KB per page. Not measured: Lighthouse score, INP, CrUX (no API key).
Fixed in code after checking each claim against the repo or primary sources:
- Hospital schema: removed the CMS star rating published as a review rating with count 1, and the placeholder medicalSpecialty; the hospital FAQ no longer says "grade N/A across 0 procedures" for ungraded hospitals.
- /scan was 424px wide on a 390px phone (tooltip bubbles took layout space while hidden).
- Sitemaps: cost pages that would 404 are no longer listed; the five duplicate cost URLs in sitemap-core are gone; sitemap-core.xml is now in robots.txt.
- Trailing-slash redirects are 301, not 307, for GET and HEAD.
- Compare page titles keep full hospital names where they fit instead of cutting each to 18 characters.
- Accuracy: Texas guide said wages can be garnished for medical debt (they cannot: Tex. Const. art. XVI, sec. 28); No Surprises Act guide had the Good Faith Estimate timing wrong, called grandfathered plans exempt (they are covered; short-term plans are not), and omitted that consent waivers do not apply to anesthesiologists, radiologists and similar providers at in-network facilities.
Not fixed, needs a person (details in the audit report): unsourced statistics and "real" case studies that look invented (Valley Health System, Regional Anesthesia Partners) with arithmetic that does not add up; anesthesia unit price, revenue code 0360 for ER and A6216 as gloves in sample bills; the state medical-debt law table; Alabama "most expensive" ranking benchmark; no named author or reviewer on any guide; no privacy statement on /scan. llms.txt claims inline citations and quarterly review that the guides do not have.
