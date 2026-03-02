"""Guide: Medicare Costs 2026 - Complete Guide."""

from guides import register, _embed

_calc_embed = _embed(mode="cost", title="Look up what Medicare pays for any procedure", subtitle="Enter a CPT code to see the exact Medicare reimbursement rate for 2026.", height="400")

register("medicare-costs-2026", {
    "title": "Medicare Costs 2026: Complete Guide to Premiums, Deductibles, and How to Pay Less",
    "meta_description": "Medicare Part B premium is $202.90/month in 2026, up 10%. Get the complete breakdown of all Medicare costs and 6 ways to reduce what you pay.",
    "published": "2026-03-02",
    "author": "BillKarma Team",
    "category": "Medicare",
    "faqs": [
        {
            "q": "How much is Medicare Part B in 2026?",
            "a": "The standard Medicare Part B premium for 2026 is $202.90 per month, up $17.90 (about 10%) from $185.00 in 2025. Higher-income beneficiaries pay more through the Income-Related Monthly Adjustment Amount (IRMAA), ranging from $284.10 to $689.90 per month depending on income. The annual Part B deductible is $283, up $26 from 2025.",
        },
        {
            "q": "How much is the Medicare Part A deductible in 2026?",
            "a": "The Medicare Part A inpatient hospital deductible for 2026 is $1,736, an increase of $60 from the 2025 amount of $1,676. This deductible applies per benefit period, not per year. Hospital coinsurance is $434/day for days 61-90 and $868/day for lifetime reserve days. Skilled nursing facility coinsurance is $217/day for days 21-100.",
        },
        {
            "q": "What is IRMAA and how does it affect my Medicare premium?",
            "a": "IRMAA (Income-Related Monthly Adjustment Amount) is an additional premium charged to Medicare beneficiaries with higher incomes. It affects roughly 8% of beneficiaries. IRMAA is based on your modified adjusted gross income from two years prior (2024 income for 2026 premiums). If your income exceeds $109,000 (individual) or $218,000 (joint), you pay higher Part B and Part D premiums. You can appeal IRMAA if your income has dropped due to a life-changing event.",
        },
        {
            "q": "Does the 2026 Social Security COLA cover the Medicare premium increase?",
            "a": "Yes. The 2.8% Social Security COLA for 2026 adds about $56/month to the average retiree's benefit. The Medicare Part B premium increase is $17.90/month, so the COLA more than covers it. However, the premium increase consumes about a third of the COLA, leaving less for other expenses. Beneficiaries are protected by the hold-harmless provision, which prevents Part B premiums from reducing Social Security benefits below the prior year's level.",
        },
        {
            "q": "Why did Medicare Part B go up so much in 2026?",
            "a": "The 10% increase reflects projected price increases and higher utilization consistent with historical trends. CMS noted that without action to address unprecedented spending on skin substitutes (wound care products that rose from $256 million in 2019 to over $10 billion in 2024), the increase would have been even larger, about $11 more per month. The 2026 Physician Fee Schedule Final Rule is expected to reduce skin substitute spending by 90%.",
        },
        {
            "q": "How can I lower my Medicare costs?",
            "a": "Six strategies: apply for Medicare Savings Programs (MSPs) if your income is under $1,715/month, which can pay your Part B premium. Apply for Extra Help/Low-Income Subsidy for Part D drug costs. Compare Medicare Advantage and Medigap plans annually during open enrollment. Use the Medicare Plan Finder tool. Appeal IRMAA if your income has dropped. And scan every medical bill for errors, since Medicare patients are still responsible for coinsurance on incorrect charges.",
        },
    ],
    "body": f"""
<p class="lead">The standard Medicare Part B premium for 2026 is <strong>$202.90/month</strong> &mdash; a $17.90 increase, just under 10%, from 2025. The Part A hospital deductible jumped to <strong>$1,736</strong>. The Part B deductible is now <strong>$283</strong>. Higher-income beneficiaries pay up to <strong>$689.90/month</strong> through IRMAA. Here is the complete breakdown of every Medicare cost in 2026 and six strategies to reduce what you pay.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#part-a">Part A costs (hospital insurance)</a></li>
        <li><a href="#part-b">Part B costs (medical insurance)</a></li>
        <li><a href="#irmaa">IRMAA: the high-income surcharge</a></li>
        <li><a href="#part-d">Part D costs (prescription drugs)</a></li>
        <li><a href="#advantage">Medicare Advantage costs</a></li>
        <li><a href="#medigap">Medigap costs</a></li>
        <li><a href="#why-increase">Why costs went up in 2026</a></li>
        <li><a href="#lower-costs">6 ways to lower your Medicare costs</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="part-a">1. Part A costs (hospital insurance)</h2>

<p>Medicare Part A covers inpatient hospital stays, skilled nursing facility care, hospice, and some home health care. Most people pay no monthly premium for Part A (if you or your spouse paid Medicare taxes for 40+ quarters). But Part A has significant cost-sharing:</p>

<table>
    <thead>
        <tr><th>Cost</th><th>2025 amount</th><th>2026 amount</th><th>Change</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Premium (most people)</strong></td><td>$0</td><td>$0</td><td>No change</td></tr>
        <tr><td><strong>Premium (30&ndash;39 quarters)</strong></td><td>$285/month</td><td>$295/month</td><td>+$10</td></tr>
        <tr><td><strong>Premium (&lt;30 quarters)</strong></td><td>$518/month</td><td>$535/month</td><td>+$17</td></tr>
        <tr><td><strong>Inpatient hospital deductible</strong></td><td>$1,676</td><td>$1,736</td><td>+$60</td></tr>
        <tr><td><strong>Hospital coinsurance (days 61&ndash;90)</strong></td><td>$419/day</td><td>$434/day</td><td>+$15/day</td></tr>
        <tr><td><strong>Lifetime reserve days (days 91&ndash;150)</strong></td><td>$838/day</td><td>$868/day</td><td>+$30/day</td></tr>
        <tr><td><strong>Skilled nursing facility (days 21&ndash;100)</strong></td><td>$209.50/day</td><td>$217.00/day</td><td>+$7.50/day</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Important:</strong> The Part A deductible ($1,736) applies per <em>benefit period</em>, not per calendar year. A benefit period starts when you&rsquo;re admitted to the hospital and ends when you&rsquo;ve been out of the hospital or skilled nursing facility for 60 consecutive days. If you&rsquo;re readmitted after 60 days, you pay the deductible again. Multiple hospitalizations in a year can mean paying the $1,736 deductible more than once.
</div>

<h2 id="part-b">2. Part B costs (medical insurance)</h2>

<p>Part B covers doctor visits, outpatient care, preventive services, durable medical equipment, and some home health care. Every beneficiary pays a monthly premium and an annual deductible:</p>

<table>
    <thead>
        <tr><th>Cost</th><th>2025 amount</th><th>2026 amount</th><th>Change</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Standard monthly premium</strong></td><td>$185.00</td><td>$202.90</td><td>+$17.90 (9.7%)</td></tr>
        <tr><td><strong>Annual deductible</strong></td><td>$257</td><td>$283</td><td>+$26 (10.1%)</td></tr>
        <tr><td><strong>Coinsurance after deductible</strong></td><td>20%</td><td>20%</td><td>No change</td></tr>
    </tbody>
</table>

<p>After you meet the $283 annual deductible, you typically pay 20% of the Medicare-approved amount for most Part B services. There is <strong>no out-of-pocket maximum</strong> for Original Medicare Part B &mdash; the 20% coinsurance applies with no cap unless you have Medigap or Medicare Advantage coverage.</p>

<p><strong>Annual cost for 2026:</strong> The standard Part B premium totals <strong>$2,434.80/year</strong> ($202.90 x 12), plus the $283 deductible, for a baseline of <strong>$2,717.80/year</strong> before any medical services. This is up from $2,477 in 2025.</p>

<h2 id="irmaa">3. IRMAA: the high-income surcharge</h2>

<p>If your modified adjusted gross income (MAGI) exceeds $109,000 (individual) or $218,000 (joint), you pay an Income-Related Monthly Adjustment Amount on top of the standard premium. IRMAA is based on your tax return from two years prior &mdash; so 2026 IRMAA is based on your 2024 income.</p>

<table>
    <thead>
        <tr><th>Individual income</th><th>Joint income</th><th>2026 Part B monthly premium</th><th>Monthly surcharge</th></tr>
    </thead>
    <tbody>
        <tr><td>&le; $109,000</td><td>&le; $218,000</td><td>$202.90</td><td>$0 (standard)</td></tr>
        <tr><td>$109,001&ndash;$137,000</td><td>$218,001&ndash;$274,000</td><td>$284.10</td><td>+$81.20</td></tr>
        <tr><td>$137,001&ndash;$171,000</td><td>$274,001&ndash;$342,000</td><td>$405.80</td><td>+$202.90</td></tr>
        <tr><td>$171,001&ndash;$214,000</td><td>$342,001&ndash;$428,000</td><td>$527.50</td><td>+$324.60</td></tr>
        <tr><td>$214,001&ndash;$500,000</td><td>$428,001&ndash;$750,000</td><td>$649.20</td><td>+$446.30</td></tr>
        <tr><td>&gt; $500,000</td><td>&gt; $750,000</td><td>$689.90</td><td>+$487.00</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>You can appeal IRMAA.</strong> If your income has dropped since 2024 due to retirement, job loss, divorce, death of a spouse, or other life-changing event, file Form SSA-44 with the Social Security Administration. SSA can use your current (lower) income instead of the 2024 amount, potentially saving you hundreds per month.
</div>

<h2 id="part-d">4. Part D costs (prescription drugs)</h2>

<p>Medicare Part D (prescription drug coverage) has undergone major changes thanks to the Inflation Reduction Act. Key 2026 numbers:</p>

<table>
    <thead>
        <tr><th>Cost</th><th>2025 amount</th><th>2026 amount</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Annual out-of-pocket cap</strong></td><td>$2,000</td><td>$2,000</td></tr>
        <tr><td><strong>Medicare Prescription Payment Plan</strong></td><td>Available (spread $2,000 over 12 months)</td><td>Available</td></tr>
        <tr><td><strong>Insulin cap</strong></td><td>$35/month</td><td>$35/month</td></tr>
        <tr><td><strong>Part D IRMAA (highest bracket)</strong></td><td>$85/month</td><td>$92.00/month</td></tr>
        <tr><td><strong>Vaccines</strong></td><td>$0 copay</td><td>$0 copay</td></tr>
    </tbody>
</table>

<p>The <strong>$2,000 annual out-of-pocket cap</strong> on Part D drug costs (introduced in 2025) remains in effect. This is a game-changer for beneficiaries taking expensive specialty drugs. Before 2025, there was no out-of-pocket maximum &mdash; patients on cancer drugs or biologics could face $10,000+ in annual drug costs. The Medicare Prescription Payment Plan lets you spread the $2,000 cap into equal monthly installments.</p>

<h2 id="advantage">5. Medicare Advantage costs</h2>

<p>Medicare Advantage (Part C) plans are offered by private insurers and bundle Part A, Part B, and usually Part D. In 2026, about 54% of Medicare beneficiaries are enrolled in Advantage plans. Costs vary by plan, but key trends:</p>

<ul>
    <li><strong>Average premium:</strong> $17.00/month (in addition to Part B premium), down slightly from 2025</li>
    <li><strong>Out-of-pocket maximums:</strong> Required by law, typically $3,500&ndash;$8,300 for in-network care</li>
    <li><strong>Benefits tightening:</strong> Some plans are reducing supplemental benefits (dental, vision, hearing) and narrowing provider networks in 2026 due to CMS rate adjustments</li>
    <li><strong>Prior authorization concerns:</strong> CMS finalized rules reducing unnecessary prior authorization in Medicare Advantage, effective 2026</li>
</ul>

<p>Compare plans annually during open enrollment (October 15 &mdash; December 7). A plan that was the best value last year may not be this year. Use the <a href="https://www.medicare.gov/plan-compare/" target="_blank" rel="noopener">Medicare Plan Finder</a> to compare premiums, copays, networks, and drug formularies side by side.</p>

<h2 id="medigap">6. Medigap costs</h2>

<p>Medigap (Medicare Supplement) plans fill the gaps in Original Medicare: the 20% Part B coinsurance, the Part A hospital deductible, and excess charges. Monthly premiums vary by plan, location, age, and insurer &mdash; typically $100&ndash;$400/month on top of the Part B premium.</p>

<p>The most popular plans in 2026:</p>

<table>
    <thead>
        <tr><th>Plan</th><th>What it covers</th><th>Typical monthly premium (age 65)</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Plan G</strong></td><td>All gaps except Part B deductible ($283)</td><td>$140&ndash;$280</td></tr>
        <tr><td><strong>Plan N</strong></td><td>Most gaps; $20 copay for some office visits, $50 ER copay</td><td>$100&ndash;$200</td></tr>
        <tr><td><strong>High-deductible Plan G</strong></td><td>Same as Plan G, but you pay first $2,870 (2026 deductible)</td><td>$40&ndash;$80</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Medigap vs. Medicare Advantage:</strong> You cannot have both. Medigap works with Original Medicare and gives you freedom to see any Medicare-accepting provider. Medicare Advantage uses networks but often includes drug coverage, dental, and vision. The right choice depends on your health needs, preferred doctors, and budget.
</div>

<h2 id="why-increase">7. Why costs went up in 2026</h2>

<p>Three factors drove the 2026 increases:</p>

<p><strong>Skin substitute spending explosion.</strong> Medicare spending on wound care products called "skin substitutes" surged from $256 million in 2019 to over <strong>$10 billion in 2024</strong> &mdash; a 40x increase driven largely by abusive pricing practices. CMS noted that without its intervention to address this spending, the Part B premium would have been about $11/month higher. The 2026 Physician Fee Schedule rule is projected to cut skin substitute spending by 90%.</p>

<p><strong>Rising healthcare utilization.</strong> Post-pandemic healthcare utilization has normalized at higher levels, with increased demand for specialty care, diagnostic imaging, and outpatient procedures.</p>

<p><strong>Drug and treatment cost inflation.</strong> New high-cost treatments (GLP-1 drugs, gene therapies, cancer immunotherapies) continue to push Part B spending upward, even as the IRA&rsquo;s drug pricing provisions moderate some Part D costs.</p>

<h2 id="lower-costs">8. Six ways to lower your Medicare costs</h2>

<ol>
    <li><strong>Apply for Medicare Savings Programs (MSPs).</strong> If your monthly income is below $1,715 (individual) or $2,320 (couple), you may qualify for an MSP that pays your Part B premium, deductibles, and coinsurance. Four programs exist at different income levels. Apply through your state Medicaid office.</li>
    <li><strong>Apply for Extra Help (Low-Income Subsidy).</strong> If your income is below $22,590 (individual) or $30,660 (couple) and your assets are limited, Extra Help can reduce Part D premiums, deductibles, and copays to near zero. Apply at <a href="https://www.ssa.gov/medicare/part-d-extra-help" target="_blank" rel="noopener">ssa.gov</a> or call 1-800-772-1213.</li>
    <li><strong>Appeal IRMAA if your income dropped.</strong> File SSA-44 if you&rsquo;ve retired, lost a job, divorced, or experienced another life-changing event since the tax year used for IRMAA (2024 for 2026 premiums).</li>
    <li><strong>Compare plans every year during open enrollment.</strong> Use <a href="https://www.medicare.gov/plan-compare/" target="_blank" rel="noopener">Medicare Plan Finder</a> to compare Medicare Advantage and Part D plans. Formularies, networks, and premiums change annually.</li>
    <li><strong>Use the $2,000 Part D out-of-pocket cap.</strong> If you take expensive medications, enroll in the Medicare Prescription Payment Plan to spread costs into equal monthly payments instead of paying large amounts upfront in the coverage gap.</li>
    <li><strong>Scan every bill for errors.</strong> Medicare patients are responsible for 20% coinsurance on Part B services. If the underlying charge is wrong, your 20% is calculated on the wrong amount. <a href="/scan">Upload your bills to BillKarma</a> to check for duplicate charges, upcoding, and services not rendered.</li>
</ol>

{_calc_embed}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much is Medicare Part B in 2026?</h3>
        <p>The standard Part B premium is $202.90/month ($2,434.80/year). The annual deductible is $283. After the deductible, you pay 20% coinsurance with no out-of-pocket cap under Original Medicare. Higher-income beneficiaries pay IRMAA surcharges of $81.20&ndash;$487.00/month depending on income level.</p>
    </div>
    <div class="faq-item">
        <h3>How much is the Medicare Part A deductible in 2026?</h3>
        <p>The Part A inpatient hospital deductible is $1,736 per benefit period. Hospital coinsurance is $434/day for days 61&ndash;90 and $868/day for lifetime reserve days. Skilled nursing facility coinsurance is $217/day for days 21&ndash;100. A benefit period resets after 60 consecutive days out of the hospital.</p>
    </div>
    <div class="faq-item">
        <h3>Does Social Security COLA cover the Medicare premium increase?</h3>
        <p>The 2.8% COLA adds roughly $56/month to the average benefit. The Part B increase is $17.90/month, so COLA more than covers it. But the premium increase absorbs about a third of the COLA, leaving less for other expenses. The hold-harmless provision prevents Part B premiums from reducing your Social Security check below the prior year&rsquo;s level.</p>
    </div>
    <div class="faq-item">
        <h3>How can I lower my Medicare premiums?</h3>
        <p>Apply for Medicare Savings Programs (income under $1,715/month individual), appeal IRMAA if your income dropped (Form SSA-44), compare plans annually during open enrollment, and apply for Extra Help on Part D drug costs (income under $22,590 individual). Contact your state Medicaid office or call 1-800-MEDICARE for help.</p>
    </div>
    <div class="faq-item">
        <h3>Why did Medicare Part B go up 10% in 2026?</h3>
        <p>Rising healthcare utilization, new expensive treatments, and the skin substitute spending explosion ($256M to $10B in five years) drove the increase. CMS said the premium would have been $11/month higher without action to curb skin substitute abuse. The 2026 fee schedule rule cuts skin substitute spending by 90%.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles" target="_blank" rel="noopener">CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles</a></li>
    <li><a href="https://www.federalregister.gov/documents/2025/11/19/2025-20251/medicare-program-medicare-part-b-monthly-actuarial-rates-premium-rates-and-annual-deductible" target="_blank" rel="noopener">Federal Register: Medicare Part B 2026 Actuarial Rates and Premiums</a></li>
    <li><a href="https://www.medicare.gov/publications/11579-medicare-costs.pdf" target="_blank" rel="noopener">Medicare.gov: 2026 Medicare Costs Fact Sheet</a></li>
    <li><a href="https://www.rrb.gov/Newsroom/NewsReleases/MedicarePartBPremium" target="_blank" rel="noopener">Railroad Retirement Board: Medicare Part B Premium Increase Announcement</a></li>
    <li><a href="https://www.medicarerights.org/medicare-watch/2025/11/20/2026-medicare-premiums-announced-last-weeks-of-open-enrollment" target="_blank" rel="noopener">Medicare Rights Center: 2026 Premiums and Open Enrollment</a></li>
    <li><a href="https://medicareadvocacy.org/2026-medicare-rates/" target="_blank" rel="noopener">Center for Medicare Advocacy: 2026 Medicare Parts A &amp; B Premiums and Deductibles</a></li>
    <li><a href="https://www.medicareresources.org/faqs/what-kind-of-medicare-benefit-changes-can-i-expect-this-year/" target="_blank" rel="noopener">MedicareResources.org: 2026 Medicare Benefit Changes</a></li>
</ul>
""",
})
