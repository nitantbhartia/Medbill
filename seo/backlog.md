# SEO backlog

Ordered by expected disputes per hour of work. Top item ships next.

1. **Connect Search Console** (owner). Set `GOOGLE_SITE_VERIFICATION` in Railway (or verify the domain by DNS), then connect a Search Console data source. Every item below that says "by impressions" depends on it.
2. **Check the 22 consolidated guides** (needs item 1). For each redirect added on 2026-11-11 in `GUIDE_REDIRECTS`, compare clicks between the two old URLs. If the redirected page had more, swap the direction.
3. **Page 2 to page 1 for the core guides** (needs item 1). Queries in positions 8–20 from `keyword-map.csv`: answer in the first two sentences, add the missing sections the top three have, link from the hospital pages.
4. **"Most overpriced hospitals in [state]" data pages.** Query: `most expensive hospitals [state]`. Build from billing grades in `hospital_seo.py`, one page per state, with method and as-of date. Doubles as the press asset from the strategy doc.
5. **Medical bill negotiation service cost page.** Query: `medical bill negotiation service cost`. A fair comparison of fee models (contingency vs flat fee vs free nonprofit) with sources and as-of dates, including where human negotiators are the better choice.
6. **Comparison pages: BillKarma vs Resolve, vs Goodbill.** Fair, sourced, dated. Say plainly when a $20k+ bill is better served by a human negotiator.
7. **State guide overlap.** Each state has up to three pages (`{state}-medical-billing`, `medical-debt-laws-{state}`, `/rights/{state}/`). Pick one primary query per page; merge where two chase the same query.
8. **Trim off-niche guide growth.** Insurance-shopping and elective-procedure guides (LASIK, Invisalign, tummy tuck coverage) don't lead to a hospital-bill dispute. No new pages there; refresh only if they already earn clicks.
9. **Hospital page internal links.** Link each core guide from the matching hospital page section (itemized bill, financial assistance, dispute).
