# SEO backlog

Ordered by expected disputes per hour of work. Top item ships next.

1. ~~Connect Search Console.~~ Done: `sc-domain:billkarma.app` is connected (checked 2026-11-16).
2. **Check the 22 consolidated guides.** Too early on 2026-11-16: the site has had 1–2 impressions a day since the Nov 8 relaunch. Re-check after mid-December. For each redirect added on 2026-11-11 in `GUIDE_REDIRECTS`, compare clicks between the two old URLs. If the redirected page had more, swap the direction.
3. **Page 2 to page 1 for the core guides** (needs item 1). Queries in positions 8–20 from `keyword-map.csv`: answer in the first two sentences, add the missing sections the top three have, link from the hospital pages.
4. ~~Comparison page: BillKarma vs Goodbill.~~ Shipped 2026-11-11.
5. **Pitch the state rankings to press.** Run `python scripts/build_press_pitches.py` against the live database (Railway shell). It writes one draft per top-median-markup state to `seo/outreach/` with that state's real numbers. Add a reporter name and send by hand; track replies in `log.md`.
6. ~~State guide overlap.~~ Closed 2026-11-16: across ~90 state pages (Nov 2025 to Nov 2026) Search Console shows 2 clicks and no page with a ranking worth protecting, so there is no data to pick a winner and nothing to gain from redirects. Leave as is; revisit when state pages earn clicks.
7. **Trim off-niche guide growth.** Insurance-shopping and elective-procedure guides (LASIK, Invisalign, tummy tuck coverage) don't lead to a hospital-bill dispute. No new pages there; refresh only if they already earn clicks.
8. ~~Hospital page internal links.~~ Shipped 2026-11-16.
