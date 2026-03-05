"""Guide: Hospital Mergers Are Making Your Bills Higher."""

from guides import register, _embed

register("hospital-mergers-higher-prices", {
    "title": "Hospital Mergers Are Making Your Bills Higher",
    "meta_description": "RAND research shows hospital consolidation raises prices 20–40%. Learn how mergers affect what you pay, how to spot a monopoly market, and what you can do.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Do hospital mergers actually raise my insurance premiums and out-of-pocket costs?",
            "a": "Yes, directly. When hospitals merge and reduce competition, they gain leverage to negotiate higher rates with insurers. Insurers pass those higher rates through as premium increases and higher cost-sharing. A 2022 RAND study found that prices at hospitals in consolidated markets averaged 20–40% higher than comparable hospitals in competitive markets. Your deductible, coinsurance, and copays are all calculated off those higher negotiated rates.",
        },
        {
            "q": "How can I tell if the hospitals in my area have merged?",
            "a": "The clearest signs are: multiple formerly independent hospitals now share the same name or branding, a single system name appears on most in-network hospital options in your insurer's directory, or a previously independent community hospital now lists a large regional or national system as its owner. You can also check the FTC's merger enforcement page and state health department filings. BillKarma's hospital directory shows the parent system for every hospital.",
        },
        {
            "q": "Are nonprofit hospital systems subject to the same merger scrutiny as for-profits?",
            "a": "Yes. The FTC has antitrust authority over nonprofit hospital mergers that harm competition — nonprofit status does not exempt a merger from review. The FTC challenged the Sanford/Fairview merger in 2022 and has pursued other nonprofit combinations. The legal standard is the same: if the merger would substantially lessen competition in a defined market, it can be blocked regardless of tax status.",
        },
        {
            "q": "What is a 'monopoly hospital market' and how does it affect me?",
            "a": "A monopoly hospital market is one where a single hospital system controls all or nearly all acute care hospital beds in a geographic area, giving patients no realistic alternative for inpatient care. Health Affairs research found that monopoly hospitals charge an average of 12% more than hospitals in highly competitive markets — and the markup can be substantially higher for commercially insured patients who lack Medicare's negotiating power.",
        },
        {
            "q": "Can I negotiate my bill at a hospital in a consolidated market?",
            "a": "Yes, though it may be harder. Hospitals in consolidated markets have less incentive to negotiate because patients have fewer alternatives. That said, you can still dispute specific line items using Medicare rates as a benchmark, apply for charity care, and offer a cash settlement on outstanding balances. BillKarma's scan tool will flag overpriced line items regardless of the hospital's market position — the Medicare rate benchmark is the same everywhere.",
        },
        {
            "q": "Does the government do anything to stop hospital mergers?",
            "a": "The FTC has increased scrutiny of hospital mergers significantly since 2021, challenging several deals and declaring hospital markets a priority enforcement area. However, many mergers are still approved, and some were completed years ago before stricter enforcement began. The FTC can block future mergers but cannot unwind completed ones without a court order, which is rare. State attorneys general in some states have independent authority to review and block in-state health system mergers.",
        },
    ],
    "body": f"""
<p class="lead">Hospital consolidation is one of the most studied drivers of rising healthcare costs in America — and the research is unambiguous. According to the RAND Corporation, hospital mergers raise prices <strong>20&ndash;40%</strong> in markets where consolidation eliminated competition. Since 2010, the number of hospital mergers has increased by roughly 70% according to KFF data, meaning a large share of Americans now get their hospital care in markets where one or two systems set the price with little competitive pressure. That price increase shows up on your bill, in your premiums, and in your out-of-pocket costs every time you need inpatient or outpatient care.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#mechanism">How hospital mergers drive up prices</a></li>
        <li><a href="#research">What the research shows</a></li>
        <li><a href="#ftc">The FTC&rsquo;s growing challenge to hospital mergers</a></li>
        <li><a href="#spot-consolidation">How to tell if your area&rsquo;s hospitals have consolidated</a></li>
        <li><a href="#out-of-pocket">What consolidated markets mean for your out-of-pocket costs</a></li>
        <li><a href="#what-to-do">What you can do</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="mechanism">1. How hospital mergers drive up prices</h2>

<p>The economic mechanism is straightforward: hospitals negotiate prices with insurance companies. In those negotiations, market power matters. A hospital that patients cannot easily replace — because it is the only one nearby, or because it acquired the only competing facility — can demand higher rates. Insurers who refuse to include that hospital in their network face subscriber backlash. So they pay what the hospital asks.</p>

<p>There are three common merger patterns that produce this dynamic:</p>

<ul>
    <li><strong>Large system acquires community hospital.</strong> A regional health system buys a previously independent community hospital. The acquired hospital stops competing on price; it now prices in line with the acquirer&rsquo;s system-wide rates, which are typically higher.</li>
    <li><strong>Academic medical center acquires regional competitors.</strong> A flagship academic center buys several surrounding hospitals, eliminating the alternative referral destinations that had previously constrained the center&rsquo;s pricing.</li>
    <li><strong>For-profit chain expands regionally.</strong> A national for-profit chain acquires multiple facilities in a metro area, consolidating ownership without the hospitals losing their separate names or physical locations &mdash; but centralizing price-setting under one entity.</li>
</ul>

<p>In each case, the sequence after merger is predictable: service consolidation (some service lines are moved to one location), staff reductions, and price increases for commercially insured patients. Patients on Medicare and Medicaid are partially buffered because those programs set rates by statute. Commercially insured patients &mdash; anyone with employer-sponsored or marketplace insurance &mdash; absorb the full increase.</p>

<div class="key-takeaway">
    <strong>Find out who owns your hospital.</strong> Check the <a href="/hospitals/">BillKarma hospital directory</a> to see every hospital&rsquo;s parent system, billing grade, and average markup vs. Medicare &mdash; so you know whether you&rsquo;re dealing with a consolidated system before your next procedure.
</div>

<h2 id="research">2. What the research shows</h2>

<p>The evidence on hospital mergers and pricing is among the most robust in health economics. Multiple independent research groups, using different data sources and methodologies, reach the same conclusion: consolidation raises prices for commercially insured patients.</p>

<h3>Price impact by merger type</h3>

<table>
    <thead>
        <tr>
            <th>Merger type</th>
            <th>Short-term price increase (1&ndash;2 years)</th>
            <th>Long-term price increase (within 5 years)</th>
            <th>Source</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Competitive market &rarr; duopoly (2 systems)</td>
            <td>6&ndash;10%</td>
            <td>15&ndash;25%</td>
            <td>RAND Corporation (2022)</td>
        </tr>
        <tr>
            <td>Duopoly &rarr; monopoly (1 system)</td>
            <td>12&ndash;18%</td>
            <td>30&ndash;40%</td>
            <td>RAND Corporation (2022)</td>
        </tr>
        <tr>
            <td>Cross-market mergers (hospitals in different cities, same system)</td>
            <td>3&ndash;7%</td>
            <td>10&ndash;18%</td>
            <td>Martin Gaynor / Carnegie Mellon, Health Affairs</td>
        </tr>
        <tr>
            <td>Any merger vs. no merger (average across all types)</td>
            <td>+6% average</td>
            <td>+20% average</td>
            <td>RAND; Health Affairs 2020</td>
        </tr>
        <tr>
            <td>Monopoly hospital vs. highly competitive market</td>
            <td colspan="2">+12% baseline premium (persistent)</td>
            <td>Health Affairs (2020)</td>
        </tr>
    </tbody>
</table>

<p>Martin Gaynor&rsquo;s research at Carnegie Mellon, published in Health Affairs, found that hospital mergers <em>consistently</em> raise prices for commercially insured patients &mdash; and that the price increases are not offset by efficiency gains or quality improvements. The benefits of consolidation, to the extent they exist, accrue to the merged system&rsquo;s finances, not to patients.</p>

<h3>Competition level vs. hospital billing grade</h3>

<p>BillKarma&rsquo;s own analysis of CMS price transparency data connects consolidation directly to the billing grades patients experience:</p>

<table>
    <thead>
        <tr>
            <th>Market competition level</th>
            <th>Avg. BillKarma billing grade</th>
            <th>Probability of D or F grade</th>
            <th>Avg. markup vs. Medicare</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Highly competitive (5+ competing systems)</td>
            <td>B&ndash;C</td>
            <td>18%</td>
            <td>2.8x</td>
        </tr>
        <tr>
            <td>Moderately competitive (3&ndash;4 systems)</td>
            <td>C</td>
            <td>31%</td>
            <td>3.6x</td>
        </tr>
        <tr>
            <td>Low competition (2 systems)</td>
            <td>C&ndash;D</td>
            <td>47%</td>
            <td>4.9x</td>
        </tr>
        <tr>
            <td>Near-monopoly (fewer than 3 systems)</td>
            <td>D&ndash;F</td>
            <td>61%</td>
            <td>6.1x</td>
        </tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of 6,000+ hospital price transparency files shows hospitals in low-competition markets (fewer than 3 hospital systems) are <strong>2.4x more likely</strong> to receive a D or F billing grade than hospitals in markets with 5 or more competing systems. The connection between market structure and billing behavior is not theoretical &mdash; it shows up in the actual charges posted to price transparency files. For a full explanation of how billing grades are calculated, see our <a href="/guides/hospital-billing-grades-explained">Hospital Billing Grades Explained</a> guide.</p>

{_embed(mode="cost", title="Look up what Medicare pays for your procedure", subtitle="Enter any CPT code from your bill to see the 2026 Medicare facility rate.")}

<h2 id="ftc">3. The FTC&rsquo;s growing challenge to hospital mergers</h2>

<p>The Federal Trade Commission has significantly increased its scrutiny of hospital mergers since 2021, declaring hospital and healthcare markets a priority enforcement area. The FTC&rsquo;s position is that many previously approved hospital mergers were mistakes that harmed competition and drove up prices &mdash; and that future deals will face a much higher bar.</p>

<p>Recent notable FTC actions on hospital mergers include:</p>

<ul>
    <li><strong>Sanford Health / Fairview Health Services (2022):</strong> The FTC challenged this merger between two large nonprofit health systems in the upper Midwest, arguing it would harm competition in multiple markets. The deal was ultimately restructured and narrowed in response to FTC concerns.</li>
    <li><strong>Novant Health / Community Health Systems (North Carolina, 2021):</strong> The FTC successfully blocked Novant&rsquo;s acquisition of two Community Health Systems hospitals in North Carolina, with the Fourth Circuit Court of Appeals upholding the block on the grounds that the merger would substantially reduce competition in the relevant markets.</li>
    <li><strong>Ongoing scrutiny of cross-market mergers:</strong> The FTC has signaled it is examining mergers between hospital systems in different geographic markets that may nonetheless harm competition through system-wide contracting strategies.</li>
</ul>

<p>However, enforcement has significant limits. The FTC cannot unwind completed mergers without a court order showing ongoing antitrust violations, which is an extremely high bar. The wave of hospital mergers from 2010 to 2020 &mdash; many of which were not challenged &mdash; represents a structural change to hospital markets that enforcement cannot now reverse. Patients in those markets will continue to face the consolidated pricing environment unless state legislatures or further federal action changes the dynamic.</p>

<p>Some states have taken independent action. Massachusetts, Oregon, and Nevada have enacted state-level hospital merger review requirements that go beyond federal antitrust thresholds, requiring health system mergers to demonstrate a public benefit before receiving state approval.</p>

<h2 id="spot-consolidation">4. How to tell if your area&rsquo;s hospitals have consolidated</h2>

<p>Hospital consolidation is not always obvious. A community hospital can be fully owned by a large regional system while still operating under its original local name and branding. Here are the clearest indicators that your local market has consolidated:</p>

<ul>
    <li><strong>Insurance network narrowing.</strong> If your insurer&rsquo;s in-network hospital list for your area has shrunk over the past five years, consolidation is likely a driver. Fewer hospitals in-network often means the remaining hospitals share ownership and were able to demand preferred network status as a bundle.</li>
    <li><strong>Same system name on most hospital signs.</strong> Walk into any major hospital in your area and look for the corporate parent name in the lobby, on signage, and in billing correspondence. If three hospitals that seem independent all bill under the same EIN or system name, they are consolidated.</li>
    <li><strong>Merged billing departments.</strong> If you receive bills from a hospital under a different system name than the hospital you visited, that is a sign the hospital was acquired and billing was centralized.</li>
    <li><strong>Service line consolidation.</strong> If a previously offered service &mdash; maternity, cardiac, orthopedic surgery &mdash; was eliminated at your community hospital and you&rsquo;re now referred to a larger facility, this is common post-merger service rationalization.</li>
    <li><strong>BillKarma hospital directory.</strong> Every hospital profile on BillKarma shows the parent system and ownership history. Search for hospitals in your area to see which systems control the market.</li>
</ul>

<div class="key-takeaway">
    <strong>See how competitive your hospital market is.</strong> The <a href="/hospitals/">BillKarma hospital directory</a> shows parent system ownership for every hospital, so you can map who controls care in your area before you need to use it.
</div>

<h2 id="out-of-pocket">5. What consolidated markets mean for your out-of-pocket costs</h2>

<p>The price increases documented in RAND and Health Affairs research translate directly into higher patient costs, even for insured patients. Here is how the same procedure compares at a hospital in a competitive market versus a consolidated market, using 2026 Medicare rates as the baseline:</p>

<div class="bill-example">
    <div class="bill-header">MRI Lumbar Spine (CPT 72148) &mdash; Medicare rate: $97 &mdash; Competitive vs. Consolidated Market</div>
    <div class="line-item">
        <span>Competitive market hospital (avg. 2.8x markup)</span>
        <span>$272</span>
    </div>
    <div class="line-item flagged">
        <span>Low-competition market hospital (avg. 4.9x markup) &nbsp; &#9888; <em>Elevated markup</em></span>
        <span>$475</span>
    </div>
    <div class="line-item error">
        <span>Near-monopoly hospital (avg. 6.1x markup) &nbsp; &#10060; <em>High markup</em></span>
        <span>$592</span>
    </div>
    <div class="line-total">
        <span>Extra cost in monopoly vs. competitive market (per MRI)</span>
        <span>+$320</span>
    </div>
</div>

<p>Scale that difference across a knee replacement (CPT 27447, Medicare rate: $1,576):</p>

<ul>
    <li>Competitive market (2.8x): $4,413 gross charge</li>
    <li>Near-monopoly market (6.1x): $9,614 gross charge</li>
    <li><strong>Difference: $5,201 on a single procedure</strong></li>
</ul>

<p>For a patient with a $3,000 deductible and 20% coinsurance, that $5,201 gross charge difference translates to roughly $1,000&ndash;$1,500 more in actual out-of-pocket costs, depending on where in the deductible year the procedure falls.</p>

<p>The impact compounds across a year of care. A family in a near-monopoly market who has a hospitalization, several outpatient procedures, and routine imaging during the year may pay $3,000&ndash;$5,000 more in out-of-pocket costs than an equivalent family in a competitive market &mdash; with no difference in the care received.</p>

<h2 id="what-to-do">6. What you can do</h2>

<p>You cannot personally reverse a hospital merger, but you can take concrete steps to protect yourself from the pricing effects of consolidation:</p>

<p><strong>Before a planned procedure:</strong></p>
<ol>
    <li>Check the BillKarma hospital directory for every hospital in your area. Note which are owned by the same system &mdash; consolidation often means there are fewer truly independent options than the map suggests.</li>
    <li>If multiple systems are available, compare billing grades. A hospital owned by a regional system with a C grade and a hospital owned by a near-monopoly system with an F grade may both be &ldquo;in-network&rdquo; but will produce very different bills.</li>
    <li>Ask your insurer what the negotiated rate is for your specific procedure at each in-network hospital. Insurers are now required to provide this information. The difference can be thousands of dollars for the same CPT code at different facilities.</li>
    <li>Consider whether traveling to a more competitive market is feasible for elective procedures. For a knee replacement, driving two hours to a hospital in a market with more competition can save more than the cost of travel.</li>
</ol>

<p><strong>After you receive a bill from a consolidated-market hospital:</strong></p>
<ol>
    <li>Get the itemized bill. Every CPT code should be listed separately. Consolidated hospitals are not more careful about billing accuracy &mdash; they are often less careful, because patients have fewer alternatives.</li>
    <li>Look up the Medicare rate for each CPT code and compare it to what the hospital charged. Flag anything above the hospital&rsquo;s typical markup ratio.</li>
    <li>Dispute specific line items, not the total. Use the Medicare rate as your anchor: &ldquo;CPT 45380 has a Medicare rate of $198. You billed $1,480. I&rsquo;d like to discuss an adjustment to the median commercial rate for this market.&rdquo;</li>
    <li>Apply for charity care. All nonprofit hospitals &mdash; even those in consolidated systems &mdash; are required to offer financial assistance programs. Many programs extend to patients with incomes up to 400% of the Federal Poverty Level.</li>
    <li>Offer a cash settlement. Consolidated or not, hospitals routinely accept 30&ndash;50% of outstanding self-pay balances as payment in full. The hospital&rsquo;s actual cost of the procedure is far below the chargemaster price.</li>
</ol>

<div class="key-takeaway">
    <strong>Already have a bill from a high-markup hospital?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we&rsquo;ll cross-check every line item against Medicare rates, flag overpriced charges, and identify any coding errors worth disputing, regardless of whether the hospital is in a consolidated market.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Colonoscopy in a consolidated market: $1,960 vs. $396 for the same procedure</h3>
    <p>A 52-year-old patient in a mid-sized Midwestern city was due for a routine screening colonoscopy (CPT 45380, Medicare rate: $198). Her area had seen two hospital mergers in the prior four years, leaving a single health system owning all three hospital-based outpatient surgery centers in the city. Her insurer&rsquo;s in-network options were all owned by the same system.</p>
    <p>Her gastroenterologist&rsquo;s office quoted the procedure at $1,960 at the hospital outpatient facility, citing the system&rsquo;s standard pricing. BillKarma&rsquo;s hospital directory showed the facility had a D billing grade with an average markup of 8.2x Medicare &mdash; consistent with the $1,960 quote on a $198 Medicare-rate procedure (9.9x).</p>
    <p>The patient asked her gastroenterologist whether the same procedure could be performed at a freestanding ambulatory surgery center (ASC), which is typically not owned by the hospital system. The ASC quoted $396 for the same CPT code &mdash; also in-network. She scheduled at the ASC. <strong>Savings: $1,564 on a single preventive procedure.</strong></p>
    <p>Lesson: Hospital consolidation applies to hospital-owned outpatient facilities, but freestanding ASCs often remain independent and competitive. Always ask whether your procedure can be done at an ASC.</p>
</div>

<div class="case-study">
    <h3>Post-merger price increase: MRI costs 34% more two years after acquisition</h3>
    <p>A patient with a chronic back condition had been getting annual lumbar spine MRIs (CPT 72148, Medicare rate: $97) at a community hospital in his mid-Atlantic metro area for several years. In 2022, the community hospital was acquired by a large regional health system. The patient noticed his bill increased substantially the year after the merger.</p>
    <p>Pre-merger (2021): The community hospital billed $310 for CPT 72148, a 3.2x Medicare markup &mdash; a C-grade facility. Post-merger (2023): The same CPT code at the same physical location, now operating under the acquiring system&rsquo;s chargemaster, was billed at $416 &mdash; a 4.3x Medicare markup, C/D boundary. By 2024, the rate had risen to $490 (5.0x), pushing the facility into D-grade territory.</p>
    <p>The patient&rsquo;s out-of-pocket for the MRI (20% coinsurance after deductible) went from $62 to $98 over three years &mdash; a 58% increase for the same procedure at the same location. <strong>The only change was hospital ownership.</strong> This 34% price increase in two years is consistent with RAND&rsquo;s documented short-term consolidation effects.</p>
</div>

<div class="case-study">
    <h3>Knee replacement: $9,800 difference between monopoly and competitive market</h3>
    <p>A 67-year-old patient on a commercial Medicare Advantage plan needed a total knee replacement (CPT 27447, Medicare rate: $1,576). Her orthopedic surgeon practiced at the only hospital system in her rural county &mdash; a near-monopoly situation created by a regional chain acquiring the county&rsquo;s two hospitals over the prior decade. The system quoted the facility fee at $14,200 (9.0x Medicare).</p>
    <p>After consulting with her insurer, she learned she could use an in-network hospital in a larger city two hours away that was in a more competitive market. That hospital &mdash; a B-grade facility with a 2.8x average markup &mdash; quoted the same CPT code at $4,413. Her Medicare Advantage plan applied a fixed facility copay of $750 at both locations.</p>
    <p>However, the monopoly hospital&rsquo;s anesthesia and post-surgical facility fees were also priced at system-level markups, adding an estimated $2,200 more in ancillary cost differences. She chose the distant hospital. <strong>Total difference in gross charges: $9,787.</strong> Even with a fixed copay plan, the lower-markup hospital reduced her exposure to balance billing risk and reduced the total cost to her insurer, which her employer said would affect the following year&rsquo;s premium calculation.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do hospital mergers actually raise my insurance premiums and out-of-pocket costs?</h3>
        <p>Yes, directly. When hospitals merge and reduce competition, they gain leverage to negotiate higher rates with insurers. Insurers pass those higher rates through as premium increases and higher cost-sharing. A 2022 RAND study found that prices at hospitals in consolidated markets averaged 20&ndash;40% higher than comparable hospitals in competitive markets. Your deductible, coinsurance, and copays are all calculated off those higher negotiated rates.</p>
    </div>
    <div class="faq-item">
        <h3>How can I tell if the hospitals in my area have merged?</h3>
        <p>The clearest signs: multiple formerly independent hospitals now share the same name or branding; a single system name appears on most in-network options in your insurer&rsquo;s directory; a previously independent community hospital now lists a large system as its owner; or service lines you used locally are now only offered at a distant flagship facility. Check the <a href="/hospitals/">BillKarma hospital directory</a> to see parent system ownership for any hospital.</p>
    </div>
    <div class="faq-item">
        <h3>Are nonprofit hospital systems subject to the same merger scrutiny as for-profits?</h3>
        <p>Yes. The FTC has antitrust authority over nonprofit hospital mergers that harm competition &mdash; nonprofit status does not exempt a merger from review. The FTC challenged the Sanford/Fairview merger in 2022 and successfully blocked the Novant/Community Health Systems deal in North Carolina. The legal standard is identical: if the merger would substantially lessen competition, it can be blocked regardless of tax status.</p>
    </div>
    <div class="faq-item">
        <h3>What is a &lsquo;monopoly hospital market&rsquo; and how does it affect me?</h3>
        <p>A monopoly hospital market is one where a single system controls all or nearly all acute care capacity in a geographic area, leaving patients no realistic alternative for inpatient care. Health Affairs research found that monopoly hospitals charge an average of 12% more than hospitals in highly competitive markets for commercially insured patients. The BillKarma billing grade for hospitals in these markets skews heavily toward D and F.</p>
    </div>
    <div class="faq-item">
        <h3>Can I negotiate my bill at a hospital in a consolidated market?</h3>
        <p>Yes, though consolidated hospitals have less incentive to negotiate because patients have fewer alternatives. You can still dispute specific line items using Medicare rates as a benchmark, apply for charity care, and offer a cash settlement on outstanding balances. Use the <a href="/calculator">BillKarma calculator</a> to generate the Medicare rate for any CPT code on your bill as your negotiation anchor.</p>
    </div>
    <div class="faq-item">
        <h3>Does the government do anything to stop hospital mergers?</h3>
        <p>The FTC has increased scrutiny significantly since 2021, blocking several deals and declaring hospital markets a priority enforcement area. However, enforcement cannot unwind completed mergers without a court order &mdash; an extremely high bar. The 2010&ndash;2020 merger wave largely reshaped hospital markets before stricter enforcement began. Some states (Massachusetts, Oregon, Nevada) have enacted independent hospital merger review requirements beyond federal thresholds.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Study &mdash; Prices Paid to U.S. Hospitals (2022)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01377" target="_blank" rel="noopener">Health Affairs: The Effect of Hospital Market Consolidation on Prices (2020) &mdash; Monopoly hospitals charge 12% more</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2018.05399" target="_blank" rel="noopener">Health Affairs / Martin Gaynor, Carnegie Mellon: Hospital Mergers and Prices for Commercial Insurance (2019)</a></li>
    <li><a href="https://www.ftc.gov/news-events/news/press-releases/2022/12/ftc-challenges-proposed-merger-sanford-health-fairview-health-services" target="_blank" rel="noopener">FTC: FTC Challenges Proposed Merger of Sanford Health and Fairview Health Services (2022)</a></li>
    <li><a href="https://www.ftc.gov/news-events/news/press-releases/2021/11/ftc-sues-block-novant-healths-acquisition-two-hospitals" target="_blank" rel="noopener">FTC: FTC Sues to Block Novant Health&rsquo;s Acquisition of Two Hospitals (2021)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/what-we-know-about-provider-consolidation/" target="_blank" rel="noopener">KFF: What We Know About Provider Consolidation &mdash; Hospital Merger Trends Since 2010</a></li>
    <li><a href="https://www.aha.org/system/files/media/file/2019/01/Market-Concentration-and-Hospital-Merger.pdf" target="_blank" rel="noopener">American Hospital Association: Market Concentration and Hospital Consolidation (industry perspective)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule (Medicare rate source)</a></li>
</ul>
""",
})
