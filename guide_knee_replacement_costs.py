"""Guide: Knee Replacement Cost."""

from guides import register, _embed

register("knee-replacement-surgery-cost", {
    "title": "Knee Replacement Cost in 2026: What You'll Actually Pay",
    "meta_description": "Total knee replacement averages $30,000-$50,000. With insurance you'll pay $3,000-$8,000. See the full cost breakdown, Medicare rates, and how to save.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a total knee replacement cost without insurance?",
            "a": "A total knee replacement (CPT 27447) costs $30,000-$50,000 without insurance at most hospitals. This includes the surgeon's fee ($4,000-$8,000), anesthesia ($2,000-$4,000), facility/room charges ($15,000-$25,000), and the implant itself ($5,000-$12,000). Prices vary dramatically by location\u2014the same surgery can cost $20,000 in one city and $60,000 in another.",
        },
        {
            "q": "How much does a knee replacement cost with insurance?",
            "a": "With insurance, most patients pay $3,000-$8,000 out of pocket for a knee replacement, depending on their deductible and coinsurance. If you've already met your annual deductible, you'll pay your coinsurance (typically 20%) up to your out-of-pocket maximum. Many patients hit their out-of-pocket max with this surgery, which caps your total cost at $8,050-$9,200 for most plans in 2026.",
        },
        {
            "q": "Does Medicare cover knee replacement surgery?",
            "a": "Yes. Medicare covers total knee replacement as a medically necessary procedure. Medicare pays hospitals via DRG 470 (major joint replacement without complications), which reimburses approximately $12,000-$14,000 depending on the region. Your Part A deductible is $1,676, and after that, Medicare covers days 1-60 in full. For outpatient/ASC settings, you pay 20% coinsurance after meeting the Part B deductible.",
        },
        {
            "q": "Is a partial knee replacement cheaper than a total knee replacement?",
            "a": "Yes. A partial (unicompartmental) knee replacement (CPT 27446) typically costs 20-30% less than a total, averaging $22,000-$38,000. The surgery is less invasive, requires a smaller implant, and often has a shorter hospital stay (sometimes outpatient). However, not all patients are candidates\u2014partial replacement works best when damage is limited to one compartment of the knee.",
        },
        {
            "q": "Can I get a knee replacement at an ambulatory surgery center?",
            "a": "Yes, and it can save you 30-50%. CMS approved total knee replacements for ASC settings starting in 2020, and many surgeons now perform them outpatient. A knee replacement at an ASC typically costs $18,000-$30,000 vs $30,000-$50,000 at a hospital. Recovery and complication rates are comparable for healthy patients. Check our surgery center directory at /surgery-centers/ to find ASCs near you.",
        },
    ],
    "body": f"""
<p class="lead">A total knee replacement costs <strong>$30,000&ndash;$50,000</strong> at most hospitals before insurance. With insurance, you&rsquo;ll typically pay <strong>$3,000&ndash;$8,000</strong> out of pocket. But the price for the exact same surgery can vary by $30,000+ depending on where you have it done. Here&rsquo;s the full cost breakdown, what Medicare pays, and how to avoid overpaying.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Full cost breakdown</a></li>
        <li><a href="#with-without-insurance">Cost with vs. without insurance</a></li>
        <li><a href="#medicare-coverage">Medicare coverage and rates</a></li>
        <li><a href="#partial-vs-total">Partial vs. total knee replacement</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. surgery center</a></li>
        <li><a href="#cost-factors">Factors that affect your cost</a></li>
        <li><a href="#lower-your-bill">5 ways to lower your knee replacement bill</a></li>
        <li><a href="#hidden-costs">Recovery costs people forget</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Full cost breakdown</h2>

<p>A total knee replacement bill includes charges from multiple providers and departments. Here&rsquo;s what each piece typically costs:</p>

<table>
    <thead>
        <tr><th>Component</th><th>CPT/DRG Code</th><th>Typical Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Surgeon&rsquo;s fee</td><td>CPT 27447</td><td>$4,000&ndash;$8,000</td><td>~$1,500&ndash;$1,800</td></tr>
        <tr><td>Anesthesia</td><td>CPT 01402</td><td>$2,000&ndash;$4,000</td><td>~$800&ndash;$1,200</td></tr>
        <tr><td>Facility/room (1&ndash;3 nights)</td><td>DRG 470/469</td><td>$15,000&ndash;$25,000</td><td>~$10,000&ndash;$14,000 (total DRG)</td></tr>
        <tr><td>Knee implant</td><td>Various</td><td>$5,000&ndash;$12,000</td><td>Bundled in DRG</td></tr>
        <tr><td>Pre-op imaging (MRI/X-ray)</td><td>CPT 73721/73565</td><td>$500&ndash;$2,500</td><td>~$200&ndash;$500</td></tr>
        <tr><td>Lab work</td><td>Various</td><td>$200&ndash;$800</td><td>~$50&ndash;$150</td></tr>
        <tr><td>Physical therapy (in-hospital)</td><td>CPT 97110</td><td>$300&ndash;$800</td><td>~$100&ndash;$200</td></tr>
        <tr><td>Post-op medications</td><td>Various</td><td>$200&ndash;$600</td><td>Varies</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The implant is a hidden cost driver.</strong> Knee implant prices range from $5,000 to $12,000+ depending on the brand and type (standard vs. custom, metal vs. ceramic). Hospitals mark up implants significantly. Ask your surgeon which implant they plan to use and whether a less expensive option is clinically equivalent.
</div>

<p>Look up what Medicare pays for knee replacement in your area:</p>

{_embed(mode="cost", cpt="27447", title="Look Up Knee Replacement Cost", subtitle="See what Medicare pays for CPT 27447 in your area.")}

<h2 id="with-without-insurance">2. Cost with vs. without insurance</h2>

<table>
    <thead>
        <tr><th>Scenario</th><th>Typical Total Bill</th><th>What You Pay</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer insurance (PPO)</td><td>$35,000&ndash;$50,000</td><td>$3,000&ndash;$8,000 (deductible + 20% coinsurance up to OOP max)</td></tr>
        <tr><td>Medicare (Original)</td><td>$12,000&ndash;$14,000 (DRG rate)</td><td>$1,676 deductible + $0 for days 1&ndash;60</td></tr>
        <tr><td>Medicare Advantage</td><td>Varies by plan</td><td>$1,500&ndash;$5,000 (plan-specific copay)</td></tr>
        <tr><td>Medicaid</td><td>$8,000&ndash;$12,000 (Medicaid rate)</td><td>$0&ndash;$4</td></tr>
        <tr><td>Uninsured (hospital chargemaster)</td><td>$35,000&ndash;$60,000</td><td>Full amount (negotiate down 40&ndash;60%)</td></tr>
        <tr><td>Uninsured (negotiated/cash pay)</td><td>$18,000&ndash;$28,000</td><td>Full amount (ask for self-pay rate)</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Same surgery, $32,000 price difference</h3>
    <p>A 2025 RAND Corporation analysis found that the price of a total knee replacement ranged from <strong>$18,500 to $50,800</strong> within the same metro area. The cheapest option was an ambulatory surgery center; the most expensive was a large academic medical center 12 miles away. The clinical outcomes were statistically identical.</p>
</div>

<h2 id="medicare-coverage">3. Medicare coverage and rates</h2>

<p>Medicare covers total knee replacement (CPT 27447) as medically necessary. Most knee replacements are billed under <strong>DRG 470</strong> (major joint replacement without complications) or <strong>DRG 469</strong> (with complications).</p>

<table>
    <thead>
        <tr><th>DRG</th><th>Description</th><th>Medicare Payment (2026)</th></tr>
    </thead>
    <tbody>
        <tr><td>DRG 470</td><td>Major joint replacement, no complications</td><td>~$12,000&ndash;$13,500</td></tr>
        <tr><td>DRG 469</td><td>Major joint replacement, with complications</td><td>~$16,000&ndash;$20,000</td></tr>
    </tbody>
</table>

<p><strong>Your cost on Original Medicare:</strong> You pay the Part A deductible ($1,676 in 2026) for the hospital stay. Days 1&ndash;60 are fully covered after the deductible. If you have a Medigap supplement, it may cover the deductible too.</p>

<p><strong>Important:</strong> If your surgeon is &ldquo;non-participating&rdquo; with Medicare, they can charge up to 15% above the Medicare-approved amount. Always confirm your surgeon is Medicare-participating before scheduling. See our <a href="/guides/medicare-billing/">Medicare billing guide</a> for more.</p>

<h2 id="partial-vs-total">4. Partial vs. total knee replacement</h2>

<table>
    <thead>
        <tr><th>Factor</th><th>Partial (CPT 27446)</th><th>Total (CPT 27447)</th></tr>
    </thead>
    <tbody>
        <tr><td>Average cost</td><td>$22,000&ndash;$38,000</td><td>$30,000&ndash;$50,000</td></tr>
        <tr><td>Medicare surgeon fee</td><td>~$1,200&ndash;$1,500</td><td>~$1,500&ndash;$1,800</td></tr>
        <tr><td>Hospital stay</td><td>0&ndash;1 night (often outpatient)</td><td>1&ndash;3 nights</td></tr>
        <tr><td>Recovery time</td><td>4&ndash;6 weeks</td><td>6&ndash;12 weeks</td></tr>
        <tr><td>Implant lifespan</td><td>15&ndash;20 years</td><td>20&ndash;25 years</td></tr>
        <tr><td>ASC eligible</td><td>Yes (common)</td><td>Yes (for healthy patients)</td></tr>
        <tr><td>Best for</td><td>Damage in one compartment only</td><td>Widespread arthritis in multiple compartments</td></tr>
    </tbody>
</table>

<h2 id="hospital-vs-asc">5. Hospital vs. surgery center</h2>

<p>Since CMS approved total knee replacements for ambulatory surgery centers in 2020, ASCs have become a major cost-saving option:</p>

<table>
    <thead>
        <tr><th>Setting</th><th>Typical Total Cost</th><th>Savings vs. Hospital</th></tr>
    </thead>
    <tbody>
        <tr><td>Hospital inpatient (1&ndash;3 nights)</td><td>$35,000&ndash;$50,000</td><td>&mdash;</td></tr>
        <tr><td>Hospital outpatient</td><td>$25,000&ndash;$38,000</td><td>15&ndash;25%</td></tr>
        <tr><td>Ambulatory surgery center</td><td>$18,000&ndash;$30,000</td><td>30&ndash;50%</td></tr>
    </tbody>
</table>

<p>Find surgery centers near you in our <a href="/surgery-centers/">surgery center directory</a>.</p>

<div class="key-takeaway">
    <strong>ASCs aren&rsquo;t for everyone.</strong> You may need a hospital setting if you have: BMI over 40, uncontrolled diabetes, significant heart disease, sleep apnea requiring CPAP, or if your surgeon anticipates complications. Discuss the setting with your surgeon based on your health profile.
</div>

<h2 id="cost-factors">6. Factors that affect your cost</h2>

<ul>
    <li><strong>Geography:</strong> Knee replacement costs 40&ndash;60% more in high-cost areas (NYC, SF, Boston) than in lower-cost regions (Midwest, rural South). Medicare rates also vary by region.</li>
    <li><strong>Hospital type:</strong> Academic medical centers charge the most. Community hospitals are mid-range. ASCs are cheapest. For-profit hospitals tend to charge more than nonprofits.</li>
    <li><strong>Implant brand:</strong> Standard implants cost $5,000&ndash;$8,000. Custom/robotic-assisted implants can cost $10,000&ndash;$15,000. Clinical evidence shows comparable outcomes for most patients.</li>
    <li><strong>Complications:</strong> Infection, blood clots, or revision surgery can add $10,000&ndash;$50,000+ to total costs. Choose a high-volume surgeon (100+ knee replacements/year) to minimize risk.</li>
    <li><strong>Length of stay:</strong> Each extra hospital night adds $2,500&ndash;$5,000. Same-day discharge (common at ASCs) eliminates room charges entirely.</li>
    <li><strong>Bilateral (both knees):</strong> Having both knees done in one surgery costs 40&ndash;50% less than two separate surgeries but requires longer recovery.</li>
</ul>

<p>Compare hospital pricing in your area with our <a href="/hospitals/">hospital directory</a>.</p>

<h2 id="lower-your-bill">7. 5 ways to lower your knee replacement bill</h2>

<h3>a) Get a Good Faith Estimate</h3>
<p>Under the No Surprises Act, you have the right to a written cost estimate before any scheduled procedure. Request estimates from 2&ndash;3 facilities and compare. If the final bill exceeds the estimate by $400+, you can dispute it.</p>

<h3>b) Choose an ASC over a hospital</h3>
<p>If you&rsquo;re a candidate for outpatient surgery, an ASC can save you $10,000&ndash;$20,000. Ask your surgeon if they operate at an ASC and whether you&rsquo;re a good candidate.</p>

<h3>c) Audit your itemized bill</h3>
<p>Request an itemized statement with CPT codes after surgery. Common knee replacement billing errors include: duplicate charges for implant components, upcoding to DRG 469 (with complications) when there were none, and inflated supply charges. <a href="/scan">Upload your bill to BillKarma</a> for an instant audit.</p>

<h3>d) Ask about the implant</h3>
<p>Ask your surgeon whether a standard implant will provide the same outcome as a premium/custom one. Many surgeons have implant preferences based on training rather than clinical evidence. A $6,000 implant may work just as well as a $12,000 one for your situation.</p>

<h3>e) Apply for financial assistance</h3>
<p>If you&rsquo;re uninsured or underinsured, apply for the hospital&rsquo;s financial assistance program before surgery. Nonprofit hospitals are required to have charity care policies. Many offer 50&ndash;100% discounts for patients below 300&ndash;400% of the federal poverty level. See our <a href="/guides/hospital-financial-assistance-charity-care/">financial assistance guide</a>.</p>

<div class="case-study">
    <h3>$47,000 bill reduced to $14,200</h3>
    <p>A 58-year-old uninsured patient in Texas received a $47,000 bill for a total knee replacement. After requesting an itemized bill, she found: a duplicate charge for the implant ($6,200), a DRG 469 coding (with complications) despite an uneventful recovery, and a $3,800 &ldquo;surgical tray&rdquo; charge. After disputing the errors and applying for the hospital&rsquo;s self-pay discount, the bill was reduced to <strong>$14,200</strong>&mdash;a 70% reduction.</p>
</div>

<h2 id="hidden-costs">8. Recovery costs people forget</h2>

<p>The surgery bill is only part of the total cost. Budget for these post-op expenses:</p>

<table>
    <thead>
        <tr><th>Recovery Cost</th><th>Typical Range</th><th>Insurance Coverage</th></tr>
    </thead>
    <tbody>
        <tr><td>Physical therapy (2&ndash;3x/week for 6&ndash;12 weeks)</td><td>$2,400&ndash;$7,200</td><td>Usually covered with copay ($30&ndash;75/visit)</td></tr>
        <tr><td>Walker/crutches</td><td>$50&ndash;$200</td><td>Covered as DME under most plans</td></tr>
        <tr><td>CPM machine rental (if prescribed)</td><td>$500&ndash;$1,500/month</td><td>Sometimes covered; check with insurer</td></tr>
        <tr><td>Home modifications (grab bars, raised toilet seat)</td><td>$100&ndash;$500</td><td>Not covered</td></tr>
        <tr><td>Pain medications</td><td>$50&ndash;$300</td><td>Covered under Part D / Rx benefit</td></tr>
        <tr><td>Follow-up visits (surgeon, 3&ndash;4 visits)</td><td>Usually bundled in surgical fee</td><td>Included in global surgical period</td></tr>
        <tr><td>Lost wages (4&ndash;12 weeks off work)</td><td>Varies</td><td>Short-term disability if available</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Physical therapy is the biggest hidden cost.</strong> Plan for 18&ndash;36 sessions at $130&ndash;$200 each. Your insurance likely covers it, but copays of $30&ndash;$75 per visit add up to $540&ndash;$2,700. Ask about home exercise programs to reduce the number of in-office PT sessions needed.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a total knee replacement cost without insurance?</h3>
        <p>$30,000&ndash;$50,000 at most hospitals, including surgeon, anesthesia, facility, and implant. At an ambulatory surgery center, costs drop to $18,000&ndash;$30,000. Uninsured patients should request the self-pay rate and apply for financial assistance before surgery.</p>
    </div>

    <div class="faq-item">
        <h3>How much does a knee replacement cost with insurance?</h3>
        <p>Most insured patients pay $3,000&ndash;$8,000 out of pocket (deductible + 20% coinsurance up to their out-of-pocket maximum). Many patients hit their annual OOP max with this surgery, capping costs at $8,050&ndash;$9,200 for most 2026 plans.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover knee replacement surgery?</h3>
        <p>Yes. Medicare pays approximately $12,000&ndash;$14,000 via DRG 470. You owe the Part A deductible ($1,676), then days 1&ndash;60 are fully covered. Medigap plans may cover the deductible. Medicare also covers knee replacement at ASCs.</p>
    </div>

    <div class="faq-item">
        <h3>Is a partial knee replacement cheaper than a total?</h3>
        <p>Yes, typically 20&ndash;30% cheaper ($22,000&ndash;$38,000 vs. $30,000&ndash;$50,000). Partial replacements also have shorter hospital stays and faster recovery. However, not all patients are candidates&mdash;you need damage limited to one compartment of the knee.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get a knee replacement at an ambulatory surgery center?</h3>
        <p>Yes. CMS approved total knee replacements for ASCs in 2020. ASCs save 30&ndash;50% compared to hospitals. You need to be generally healthy (no major cardiac, pulmonary, or obesity issues) to be a candidate. Ask your surgeon and find ASCs in our <a href="/surgery-centers/">surgery center directory</a>.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener noreferrer">CMS: Acute Inpatient PPS &mdash; DRG Rates (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (CPT 27447)</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-pricing.html" target="_blank" rel="noopener noreferrer">RAND Corporation: Hospital Price Transparency Analysis</a></li>
    <li><a href="https://www.aaos.org/quality/quality-programs/knee-replacement/" target="_blank" rel="noopener noreferrer">AAOS: Knee Replacement Clinical Guidelines</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Hospital Costs by Procedure</a></li>
</ul>
""",
})
