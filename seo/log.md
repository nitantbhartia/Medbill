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

