# SEO backlog

Ordered by expected disputes per hour of work. Top item ships next.

1. **Connect Search Console** (owner). Set `GOOGLE_SITE_VERIFICATION` in Railway (or verify the domain by DNS), then connect a Search Console data source. Every item below that says "by impressions" depends on it.
2. **Check the 22 consolidated guides** (needs item 1). For each redirect added on 2026-11-11 in `GUIDE_REDIRECTS`, compare clicks between the two old URLs. If the redirected page had more, swap the direction.
3. **Page 2 to page 1 for the core guides** (needs item 1). Queries in positions 8–20 from `keyword-map.csv`: answer in the first two sentences, add the missing sections the top three have, link from the hospital pages.
4. ~~Comparison page: BillKarma vs Goodbill.~~ Shipped 2026-11-11.
5. **Pitch the state rankings to press.** Draft five pitches in `seo/outreach/` to health reporters in the states with the highest median markup, each with that state's ranking page.
6. **State guide overlap.** Each state has up to three pages (`{state}-medical-billing`, `medical-debt-laws-{state}`, `/rights/{state}/`). Pick one primary query per page; merge where two chase the same query.
7. **Trim off-niche guide growth.** Insurance-shopping and elective-procedure guides (LASIK, Invisalign, tummy tuck coverage) don't lead to a hospital-bill dispute. No new pages there; refresh only if they already earn clicks.
8. **Hospital page internal links.** Link each core guide from the matching hospital page section (itemized bill, financial assistance, dispute).
