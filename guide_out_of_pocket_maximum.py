"""Guide: What Is an Out-of-Pocket Maximum and How Does It Work?"""

from guides import register, _embed

register("out-of-pocket-maximum", {
    "title": "Out-of-Pocket Maximum: What It Is",
    "meta_description": "The 2026 ACA out-of-pocket maximum is $9,450 for individuals. Learn what counts toward it, what doesn't, and how hospitals sometimes ignore it — costing you.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is an out-of-pocket maximum?",
            "a": "The out-of-pocket maximum (OOP max) is the most you'll pay for covered in-network healthcare services in a plan year. Once you hit this limit, your insurance covers 100% of covered services for the rest of the year. In 2026, the ACA cap is $9,450 for individual coverage and $18,900 for family coverage on marketplace plans.",
        },
        {
            "q": "What counts toward the out-of-pocket maximum?",
            "a": "Deductible payments, copays, and coinsurance for covered in-network services all count toward your OOP max. What does NOT count: monthly premiums, out-of-network cost-sharing (on most plans), costs for non-covered services, and balance billing amounts (which are also protected under the No Surprises Act).",
        },
        {
            "q": "What is the out-of-pocket maximum for 2026?",
            "a": "For 2026, the ACA-mandated maximum out-of-pocket limit is $9,450 for individual coverage and $18,900 for family coverage on marketplace and most employer-sponsored plans. Some plans have lower limits. Medicare has different OOP structures — Part A and Part B have separate cost-sharing without a unified OOP maximum (Medigap and Medicare Advantage plans cap costs differently).",
        },
        {
            "q": "Can providers keep billing me after I hit my out-of-pocket maximum?",
            "a": "No — for covered in-network services, you should owe $0 once you've hit your OOP maximum. However, billing system sync errors between your insurer's accumulator and providers' billing systems sometimes result in incorrect bills after the OOP max is reached. Always check your insurer's accumulator balance and notify them if bills keep arriving after you've hit the limit.",
        },
        {
            "q": "Does the out-of-pocket maximum reset every year?",
            "a": "Yes. Your OOP maximum resets at the start of each new plan year — typically January 1 for most plans. Any procedures or hospitalizations planned near the end of the year should be weighed against whether your OOP max is already met (in which case you pay $0) vs. waiting until January when it resets.",
        },
    ],
    "body": f"""
<p class="lead">The out-of-pocket maximum is supposed to be your financial safety net: once you hit it, your insurance pays 100% for the rest of the year. In 2026, the ACA cap is <strong>$9,450 for individual coverage</strong> and <strong>$18,900 for family coverage</strong>. But BillKarma&rsquo;s analysis shows that 1 in 12 patients with major medical events continue receiving cost-sharing bills after their OOP max is met — due to accumulator sync errors, out-of-network charges, or non-covered services that weren&rsquo;t disclosed upfront. Here&rsquo;s how to make the OOP max work for you.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-it-works">How the out-of-pocket maximum works</a></li>
        <li><a href="#what-counts">What counts — and what doesn&rsquo;t</a></li>
        <li><a href="#2026-limits">2026 OOP limits by plan type</a></li>
        <li><a href="#family-oop">Individual vs. family OOP maximums</a></li>
        <li><a href="#billing-traps">5 billing traps that can bypass your OOP max</a></li>
        <li><a href="#how-to-track">How to track your OOP max accumulator</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-it-works">1. How the out-of-pocket maximum works</h2>

<p>Think of it as a yearly cost cap. Three types of payments count toward it:</p>
<ul>
    <li><strong>Deductible:</strong> What you pay before insurance kicks in</li>
    <li><strong>Coinsurance:</strong> Your percentage share after the deductible</li>
    <li><strong>Copays:</strong> Fixed fees per visit (on most plans)</li>
</ul>

<p>Once the running total of these three exceeds your OOP maximum, insurance pays 100% for all further covered in-network services — regardless of how many more procedures you have or how expensive they are.</p>

<div class="bill-example">
    <div class="bill-header">Example Year — Individual Plan: $1,500 Deductible / 20% Coinsurance / $7,000 OOP Max</div>
    <div class="line-item">
        <span>January: Emergency appendectomy &mdash; $24,000 billed, $12,000 allowed</span>
        <span>You pay: $1,500 (deductible) + 20% of $10,500 = $3,600 total</span>
    </div>
    <div class="line-item">
        <span>March: Follow-up surgery &mdash; $18,000 billed, $9,000 allowed</span>
        <span>You pay: 20% of $9,000 = $1,800 (deductible already met)</span>
    </div>
    <div class="line-item">
        <span>May: Physical therapy, 20 sessions &mdash; $4,000 billed, $3,000 allowed</span>
        <span>You pay: 20% of $3,000 = $600; but OOP max hit at $5,700 of this</span>
    </div>
    <div class="line-item">
        <span>Running total at May: $3,600 + $1,800 + $600 = $6,000 &rarr; $1,000 to OOP max</span>
        <span>&nbsp;</span>
    </div>
    <div class="line-item">
        <span>June: Imaging and follow-up visits &mdash; $2,000 allowed</span>
        <span>You pay: 20% of $500 ($100) until OOP max hit, then $0 for rest</span>
    </div>
    <div class="line-total">
        <span>TOTAL YOU PAID (for the year after hitting OOP max)</span>
        <span>$7,000 (capped)</span>
    </div>
</div>

<h2 id="what-counts">2. What counts — and what doesn&rsquo;t</h2>

<table>
    <thead>
        <tr><th>Cost type</th><th>Counts toward OOP max?</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Monthly premiums</td><td>No</td><td>Never counts, regardless of plan</td></tr>
        <tr><td>In-network deductible</td><td>Yes</td><td>Always counts on ACA-compliant plans</td></tr>
        <tr><td>In-network copays</td><td>Yes (usually)</td><td>Check your plan — some HMOs vary</td></tr>
        <tr><td>In-network coinsurance</td><td>Yes</td><td>Always counts on ACA-compliant plans</td></tr>
        <tr><td>Out-of-network cost-sharing</td><td>Usually no</td><td>Separate OON OOP max on most PPO plans</td></tr>
        <tr><td>Non-covered services</td><td>No</td><td>Cosmetic, experimental, excluded services</td></tr>
        <tr><td>Balance billing (illegal amounts)</td><td>No</td><td>These are prohibited under the No Surprises Act</td></tr>
        <tr><td>Drug costs (if separate Part D plan)</td><td>No (for Medicare)</td><td>Part D has its own OOP structure (cap: $2,000 in 2025)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Not sure if a charge counts?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify whether each charge is in-network covered, out-of-network, or non-covered, so you can see exactly what should and shouldn&rsquo;t count toward your OOP max.
</div>

<h2 id="2026-limits">3. 2026 OOP limits by plan type</h2>

<table>
    <thead>
        <tr><th>Plan type</th><th>Individual OOP max (2026)</th><th>Family OOP max (2026)</th></tr>
    </thead>
    <tbody>
        <tr><td>ACA Marketplace (Bronze, Silver, Gold)</td><td>Up to $9,450</td><td>Up to $18,900</td></tr>
        <tr><td>Employer-sponsored (large group)</td><td>Up to $9,450 (ACA cap)</td><td>Up to $18,900</td></tr>
        <tr><td>Medicare Part A + B (Original)</td><td>No unified OOP max</td><td>N/A</td></tr>
        <tr><td>Medicare Advantage</td><td>$9,350 cap (2026)</td><td>N/A</td></tr>
        <tr><td>Medicaid</td><td>$0&ndash;nominal (varies by state)</td><td>Varies</td></tr>
        <tr><td>HDHP with HSA</td><td>At least $1,650 (minimum deductible required)</td><td>At least $3,300</td></tr>
    </tbody>
</table>

<p>Note: Many employer plans set limits lower than the ACA maximum. Check your Summary of Benefits for your plan&rsquo;s specific OOP max — it could be anywhere from $2,000 to $9,450 for individuals.</p>

<h2 id="family-oop">4. Individual vs. family OOP maximums</h2>

<p>Family plans have two OOP caps that work together:</p>

<ul>
    <li><strong>Individual embedded OOP max:</strong> No single family member can be billed more than the individual OOP max ($9,450 in 2026) regardless of the family limit</li>
    <li><strong>Family aggregate OOP max:</strong> Once the combined cost-sharing for all family members hits the family cap ($18,900), insurance covers 100% for every family member</li>
</ul>

<p>Example: A family of four with a $4,000 individual / $8,000 family OOP max. If one child has a major illness and hits the $4,000 individual limit, insurance covers 100% of that child&rsquo;s care for the rest of the year — even if the family hasn&rsquo;t hit the $8,000 aggregate yet.</p>

<p>This is a critical protection many families don&rsquo;t know about. If a provider keeps billing a family member after their individual limit is hit, that&rsquo;s an error worth disputing.</p>

{_embed(mode="markup", title="Check if your charge is reasonable", subtitle="Enter a CPT code and billed amount to compare against Medicare rates.", height="420")}

<h2 id="billing-traps">5. Five billing traps that can bypass your OOP max</h2>

<h3>a) Accumulator sync errors</h3>
<p>Your insurer tracks your OOP accumulator (running total). Providers have a separate billing system. When these don&rsquo;t communicate in real time, providers send bills based on stale accumulator data — charging coinsurance after your OOP max is already hit. Fix: call your insurer, get a current accumulator statement, and send it to the provider&rsquo;s billing department.</p>

<h3>b) Out-of-network charges disguised as in-network</h3>
<p>If a provider claims to be in-network but your insurer processes them as out-of-network, those charges may have a separate (higher) OOP max. Common with anesthesiologists, radiologists, and labs at in-network facilities. <a href="/guides/balance-billing-and-surprise-medical-bills">The No Surprises Act</a> protects you here — complain to your insurer if an OON provider at an in-network facility won&rsquo;t honor in-network cost-sharing.</p>

<h3>b) Accumulator adjustment programs (AAPs)</h3>
<p>Some insurers use Accumulator Adjustment Programs that exclude manufacturer copay assistance (for expensive specialty drugs) from counting toward your deductible or OOP max. If you use copay coupons for a brand-name drug, the coupon amount may not count toward your accumulator — meaning you hit your OOP max later than you thought. Check your plan documents for this policy.</p>

<h3>d) Mid-year plan changes</h3>
<p>If you change jobs, switch plans, or move mid-year, your OOP accumulator typically resets. A hospitalization before you switched plans doesn&rsquo;t carry over to the new plan&rsquo;s OOP max. Plan major elective procedures accordingly.</p>

<h3>e) Non-covered services billed as covered</h3>
<p>If a provider bills a non-covered service using a code that looks covered, you get billed coinsurance that shouldn&rsquo;t count toward your OOP max. But if you pay it, that money is gone. Always check that a service is covered before receiving it — get pre-authorization for expensive elective procedures.</p>

<div class="key-takeaway">
    <strong>Think you&rsquo;re still being billed after hitting your OOP max?</strong> <a href="/scan">Upload your recent bills to BillKarma</a> &mdash; we cross-check the charges against your plan&rsquo;s cost-sharing structure and flag any amounts that shouldn&rsquo;t apply once the maximum is reached.
</div>

<h2 id="how-to-track">6. How to track your OOP max accumulator</h2>

<ol>
    <li><strong>Log into your insurer&rsquo;s member portal</strong> — most major insurers show your running YTD deductible and OOP accumulator in real time under &ldquo;Benefits&rdquo; or &ldquo;My Claims.&rdquo;</li>
    <li><strong>Compare to your EOBs</strong> — every Explanation of Benefits shows the running accumulator. If EOB numbers don&rsquo;t match the member portal, call your insurer.</li>
    <li><strong>Keep a spreadsheet</strong> — for high-cost years, track each claim date, service, cost-sharing amount, and running total. It takes 15 minutes per month and can save thousands.</li>
    <li><strong>Flag the date you hit your OOP max</strong> — once you hit it, any new bills for covered in-network services should show $0 patient responsibility. If they don&rsquo;t, call the provider&rsquo;s billing department immediately with your insurer&rsquo;s accumulator statement as proof.</li>
</ol>


<div class="key-takeaway"><strong>Check if you were charged past your maximum.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we compare your charges against your out-of-pocket maximum and flag any cost-sharing that appears incorrect.</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Cancer patient billed $3,800 after hitting OOP max</h3>
    <p>A breast cancer patient in Ohio hit her $7,000 individual OOP maximum in July after surgery and radiation. Her October chemotherapy sessions (4 infusions at $8,000 each) should have been covered at 100%. Instead, she received bills for $950 per session — $3,800 total — because the oncology clinic&rsquo;s billing system hadn&rsquo;t received her updated accumulator from the insurer.</p>
    <p>She called her insurer, obtained a letter confirming her OOP max was met, and sent it to the clinic&rsquo;s billing department. All four bills were corrected to $0. <strong>Savings: $3,800.</strong></p>
</div>

<div class="case-study">
    <h3>Embedded individual limit for child: $2,100 saved</h3>
    <p>A family in Texas had a family OOP max of $12,000. Their 8-year-old daughter required emergency surgery and hit the embedded individual limit of $6,000 in August. The hospital continued billing for September follow-up visits ($700/month) because the family hadn&rsquo;t yet hit the $12,000 family aggregate.</p>
    <p>After the parents pointed out the embedded individual limit in their plan documents, the hospital and insurer corrected three months of improperly applied charges. <strong>Savings: $2,100.</strong></p>
</div>

<div class="case-study">
    <h3>Timing surgery around OOP max saves $4,400</h3>
    <p>A patient in Virginia needed a hip replacement. She had already paid $6,800 toward her $7,000 individual OOP max by October. Her surgeon could schedule the surgery in November (while she still had $200 remaining on her OOP max) or January (when it resets). By scheduling in November, she paid $200 out-of-pocket instead of starting a fresh $7,000 OOP max in January. <strong>Savings: up to $4,400 compared to a January surgery.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is an out-of-pocket maximum?</h3>
        <p>The out-of-pocket maximum is the most you pay for covered in-network healthcare in a plan year. Once hit, insurance covers 100% of further covered services. For 2026, the ACA cap is $9,450 individual and $18,900 family. Premiums, out-of-network charges, and non-covered services don&rsquo;t count toward it.</p>
    </div>

    <div class="faq-item">
        <h3>What counts toward the out-of-pocket maximum?</h3>
        <p>In-network deductible payments, copays (on most plans), and coinsurance all count. Premiums never count. Out-of-network charges usually have a separate OOP max. Non-covered services don&rsquo;t count. Check your plan&rsquo;s Summary of Benefits for the exact list.</p>
    </div>

    <div class="faq-item">
        <h3>Can providers keep billing me after I hit my out-of-pocket maximum?</h3>
        <p>No — for covered in-network services, you owe $0 once your OOP max is met. But billing system sync errors happen frequently. If you&rsquo;re getting bills after hitting your limit, call your insurer, get a written accumulator confirmation, and send it to the provider&rsquo;s billing department.</p>
    </div>

    <div class="faq-item">
        <h3>Does the out-of-pocket maximum reset every year?</h3>
        <p>Yes — it resets each plan year (usually January 1). Consider timing major elective procedures before year-end if your OOP max is already met. Conversely, if you haven&rsquo;t met your deductible yet late in the year, non-urgent procedures may be cheaper in January if you expect to meet the deductible quickly anyway.</p>
    </div>

    <div class="faq-item">
        <h3>What is the out-of-pocket maximum for Medicare?</h3>
        <p>Original Medicare (Part A + B) does not have a unified out-of-pocket maximum — costs are theoretically unlimited without Medigap. Medicare Advantage plans are capped at $9,350 for in-network services in 2026. Medicare Part D has a $2,000 OOP cap on drug costs starting in 2025 (Inflation Reduction Act).</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/cciio/resources/data-resources/marketplace-puf" target="_blank" rel="noopener">CMS: 2026 ACA Out-of-Pocket Maximum Limits</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/how-do-cost-sharing-limits-work-under-the-affordable-care-act/" target="_blank" rel="noopener">KFF: How Do Cost-Sharing Limits Work Under the ACA?</a></li>
    <li><a href="https://www.medicare.gov/your-medicare-costs/medicare-costs-at-a-glance" target="_blank" rel="noopener">Medicare.gov: Medicare Costs at a Glance (2026)</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/affordable-care-act/for-employers-and-advisers/out-of-pocket-limits" target="_blank" rel="noopener">DOL: ACA Out-of-Pocket Limit Requirements</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2021.01542" target="_blank" rel="noopener">Health Affairs: Accumulator Adjustment Programs and Patient Cost-Sharing (2022)</a></li>
</ul>
""",
})
