"""Guide: Open Enrollment 2026: How to Choose the Right Health Plan."""

from guides import register, _embed

register("open-enrollment-health-insurance", {
    "title": "Open Enrollment 2026: Choose the Right Health Plan",
    "meta_description": "Open enrollment for employers runs Nov 1–Dec 15, 2026. Learn how to compare HMO, PPO, HDHP, and EPO plans and avoid the 5 most costly mistakes.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "When is open enrollment for 2026 health insurance?",
            "a": "For employer-sponsored plans, open enrollment typically runs from November 1 through December 15, 2026, with coverage starting January 1, 2027. Your employer sets the exact dates&mdash;check your HR system or benefits email in late October. For ACA marketplace plans, open enrollment runs November 1, 2026 through January 15, 2027 on HealthCare.gov (and state-run exchanges). Coverage purchased by December 15 starts January 1; coverage purchased January 1&ndash;15 starts February 1.",
        },
        {
            "q": "When does an HDHP with HSA make more financial sense than a PPO?",
            "a": "An HDHP with HSA wins financially when: (1) your total expected healthcare use is low (annual out-of-pocket under $2,000), (2) the premium savings vs. the PPO are large enough to offset higher cost-sharing, and (3) you max the HSA and invest the funds. Run the math: (PPO premium &times; 12) vs. (HDHP premium &times; 12 + expected out-of-pocket + HSA contribution). If the HDHP total is lower even assuming you hit your deductible, choose the HDHP. If you have chronic conditions requiring frequent specialist visits or expensive medications, a PPO&rsquo;s lower out-of-pocket sharing usually wins.",
        },
        {
            "q": "What is a special enrollment period and what triggers it?",
            "a": "A special enrollment period (SEP) lets you enroll in or change health insurance outside of open enrollment. For employer plans, qualifying life events include: losing other coverage, getting married, having a baby or adopting, moving to a new area, and becoming a dependent. For ACA marketplace plans, additional SEP triggers include: loss of Medicaid/CHIP eligibility, income change that affects subsidy eligibility, and gaining citizenship. You generally have 60 days from the qualifying event to enroll. Losing job-based coverage is the most common trigger.",
        },
        {
            "q": "If I lose my job, should I choose COBRA or a marketplace plan?",
            "a": "Compare three numbers: (1) your COBRA monthly premium (employer + employee share, plus 2% admin fee); (2) the marketplace silver plan premium after your subsidy (use HealthCare.gov&rsquo;s estimator with your projected income); and (3) how much care you actually expect to use in the coming months. COBRA is often faster to activate and preserves your in-network relationships. Marketplace plans often cost less after subsidies if your income dropped significantly. If your income is under 150% of the federal poverty level, you qualify for a zero-premium silver plan through enhanced subsidies.",
        },
        {
            "q": "What is the most common open enrollment mistake?",
            "a": "Auto-renewal without reviewing. Most employers and marketplace plans automatically re-enroll you in your current plan if you take no action during open enrollment. In 2026, plan designs, premiums, formularies, and provider networks can all change. A plan that included your specialist and your $50/month medication last year may have changed dramatically. Take 30 minutes every open enrollment period to review the Summary of Benefits and Coverage (SBC) for your current plan and at least one alternative.",
        },
    ],
    "body": f"""
<p class="lead">Employer open enrollment typically runs <strong>November 1&ndash;December 15</strong> each year, with ACA marketplace enrollment open through <strong>January 15, 2027</strong>. Choosing the wrong plan can cost you <strong>$2,000 to $8,000 more per year</strong> than the right one&mdash;even within the same employer benefits menu. This guide walks you through every plan type, shows you how to calculate your true annual cost, and explains the five mistakes that cause people to overpay year after year.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#enrollment-dates">2026 enrollment dates: employer and ACA marketplace</a></li>
        <li><a href="#plan-types">HMO vs. PPO vs. HDHP vs. EPO: comparison table</a></li>
        <li><a href="#true-cost">How to calculate your true annual cost</a></li>
        <li><a href="#hdhp-vs-ppo">When HDHP + HSA beats PPO (and when it doesn&rsquo;t)</a></li>
        <li><a href="#check-network">How to check if your doctors are in-network</a></li>
        <li><a href="#common-mistakes">5 common open enrollment mistakes</a></li>
        <li><a href="#aca-subsidies">ACA subsidies and who qualifies</a></li>
        <li><a href="#losing-job">Losing your job: COBRA vs. marketplace</a></li>
        <li><a href="#case-study">Case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="enrollment-dates">1. 2026 enrollment dates: employer and ACA marketplace</h2>

<table>
    <thead>
        <tr>
            <th>Coverage Type</th>
            <th>Open Enrollment Window</th>
            <th>Coverage Start Date</th>
            <th>Where to Enroll</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Employer-sponsored plan</td><td>Typically Nov 1&ndash;Dec 15 (employer sets exact dates)</td><td>January 1, 2027</td><td>Your employer&rsquo;s HR portal or benefits platform</td></tr>
        <tr><td>ACA marketplace (federal)</td><td>Nov 1, 2026 &ndash; Jan 15, 2027</td><td>Jan 1 (if enrolled by Dec 15) or Feb 1 (Jan 1&ndash;15)</td><td>HealthCare.gov</td></tr>
        <tr><td>ACA marketplace (state-run)</td><td>Nov 1, 2026 &ndash; Jan 15, 2027 (varies by state)</td><td>Same as above</td><td>Your state&rsquo;s exchange website</td></tr>
        <tr><td>Medicare Advantage / Part D</td><td>Oct 15 &ndash; Dec 7, 2026</td><td>January 1, 2027</td><td>Medicare.gov or plan directly</td></tr>
        <tr><td>Medicaid / CHIP</td><td>Year-round</td><td>Often same month</td><td>Your state Medicaid agency</td></tr>
    </tbody>
</table>

<p><strong>2026-specific changes to watch for:</strong> The enhanced ACA subsidies that began under the Inflation Reduction Act continue through 2026, holding premium tax credits at elevated levels for households up to 400% of the federal poverty level (and adding subsidies above 400% for the first time). If your income changed significantly this year, recalculate your subsidy eligibility before auto-renewing.</p>

<div class="key-takeaway">
    <strong>Mark your calendar now.</strong> Employer open enrollment windows are typically only 2&ndash;4 weeks long, and missing them locks you into your current plan for another year (or forces you to wait for a qualifying life event). Set a reminder for October 25 to check your HR portal.
</div>

<h2 id="plan-types">2. HMO vs. PPO vs. HDHP vs. EPO: comparison table</h2>

<p>There are four main commercial health plan structures. Each involves a different tradeoff between premium cost, flexibility, and out-of-pocket risk:</p>

<table>
    <thead>
        <tr>
            <th>Plan Type</th>
            <th>Requires PCP?</th>
            <th>Out-of-Network Coverage?</th>
            <th>Referrals to Specialists?</th>
            <th>Typical Premium</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>HMO (Health Maintenance Organization)</td><td>Yes</td><td>No (emergencies only)</td><td>Yes (from PCP)</td><td>Lowest</td><td>Predictable, low-cost users in urban areas with large HMO networks</td></tr>
        <tr><td>PPO (Preferred Provider Organization)</td><td>No</td><td>Yes (higher cost-share)</td><td>No</td><td>Highest</td><td>People with existing specialist relationships, frequent out-of-network needs</td></tr>
        <tr><td>HDHP (High-Deductible Health Plan)</td><td>Sometimes</td><td>Varies (HMO or PPO structure)</td><td>Varies</td><td>Low</td><td>Healthy, low-utilization individuals; HSA-eligible earners</td></tr>
        <tr><td>EPO (Exclusive Provider Organization)</td><td>No</td><td>No (emergencies only)</td><td>No</td><td>Lower than PPO</td><td>People who want PPO flexibility within-network but won&rsquo;t go out-of-network</td></tr>
    </tbody>
</table>

<p>An HDHP is a plan design (high deductible), not a separate plan type&mdash;an HDHP can be structured as an HMO or PPO. The key HDHP threshold for HSA eligibility in 2026 is a minimum deductible of <strong>$1,650 (individual)</strong> or <strong>$3,300 (family)</strong>, with out-of-pocket maximums of <strong>$8,300 (individual)</strong> or <strong>$16,600 (family)</strong>.</p>

<h2 id="true-cost">3. How to calculate your true annual cost</h2>

<p>The most important number in health plan comparison is your <strong>total estimated annual cost</strong>&mdash;not just the premium. Here is the correct formula:</p>

<p><strong>True annual cost = (Monthly premium &times; 12) + Expected out-of-pocket costs</strong></p>

<p>To estimate expected out-of-pocket costs, think through last year&rsquo;s healthcare use:</p>

<table>
    <thead>
        <tr>
            <th>Usage Level</th>
            <th>Description</th>
            <th>Expected Annual OOP (PPO)</th>
            <th>Expected Annual OOP (HDHP)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Low</td><td>1&ndash;2 primary care visits, no specialists, no prescriptions</td><td>$300&ndash;$600</td><td>$400&ndash;$800</td></tr>
        <tr><td>Moderate</td><td>4&ndash;6 visits, 1&ndash;2 specialist visits, 1&ndash;2 generic Rx</td><td>$800&ndash;$2,000</td><td>$1,200&ndash;$3,000</td></tr>
        <tr><td>High</td><td>Chronic condition management, surgery, expensive Rx</td><td>$3,000&ndash;OOP max</td><td>Likely hits OOP max</td></tr>
    </tbody>
</table>

<p>Run this calculation for each plan option your employer offers. The plan with the lowest headline premium is not always the cheapest when total annual cost is factored in.</p>

{_embed(mode="insurance", title="Estimate your true annual health plan cost", subtitle="Compare premium + expected out-of-pocket across your plan options.")}

<div class="guide-cta-inline">
    <strong>Not sure which plan to choose?</strong> <a href="/scan">Upload your plan comparison documents to BillKarma</a>&mdash;our tool calculates total annual cost for each option based on your expected healthcare use and recommends the lowest-cost plan for your situation.
</div>

<h2 id="hdhp-vs-ppo">4. When HDHP + HSA beats PPO (and when it doesn&rsquo;t)</h2>

<p>The HDHP + HSA combination is one of the best financial tools in the U.S. tax code for healthy, higher-earning individuals. But it is not right for everyone. Here is a decision framework:</p>

<p><strong>HDHP + HSA wins when all of these are true:</strong></p>
<ul>
    <li>The HDHP premium is at least $100/month less than the PPO (otherwise the math rarely works)</li>
    <li>You are generally healthy and expect low to moderate healthcare use</li>
    <li>You can afford to pay the deductible out of pocket if a major expense hits (or you have HSA savings to cover it)</li>
    <li>You will actually contribute to and invest the HSA&mdash;an unfunded HSA loses most of its advantage</li>
</ul>

<p><strong>PPO or HMO wins when:</strong></p>
<ul>
    <li>You have a chronic condition (diabetes, heart disease, autoimmune disorders) requiring regular specialist care and expensive medications</li>
    <li>You are pregnant or planning a pregnancy in the coming year</li>
    <li>Your employer contributes a large amount to the PPO premium, making the net premium difference small</li>
    <li>You cannot absorb the HDHP deductible financially if a major medical event occurs</li>
</ul>

<div class="key-takeaway">
    <strong>The 2026 HSA contribution limits</strong> are $4,300 for individuals and $8,550 for families (age 55+ can add $1,000 catch-up). Maxing the HSA and investing the funds in low-cost index funds creates a triple tax-advantaged account&mdash;contributions are pre-tax, growth is tax-free, and withdrawals for medical expenses are tax-free. Over 20 years, this compounds into a powerful healthcare reserve.
</div>

<h2 id="check-network">5. How to check if your doctors are in-network</h2>

<p>Checking network status before you enroll takes 15 minutes and can save thousands of dollars. Here is the right process:</p>

<ol>
    <li><strong>Do not rely on your doctor&rsquo;s office.</strong> Front desk staff often say &ldquo;yes we take [insurer]&rdquo; without checking the specific plan product. A physician may be in-network for BlueCross PPO but not BlueCross HMO or BlueCross HDHP. Specify the exact plan name.</li>
    <li><strong>Use the insurer&rsquo;s online provider directory.</strong> Search by the exact plan name that appears on the benefits comparison sheet. Enter your doctor&rsquo;s NPI number (findable on the NPI Registry at nppes.cms.hhs.gov) rather than their name to get exact results.</li>
    <li><strong>Check all providers you use regularly:</strong> primary care physician, any specialists you see, your preferred hospital, your preferred urgent care chain, and any physical therapists or mental health providers.</li>
    <li><strong>Verify the pharmacy network separately.</strong> Your physician may be in-network but your preferred pharmacy may not be. Check the formulary (drug coverage list) for every prescription you take&mdash;tier placement determines cost and can vary dramatically between plans.</li>
    <li><strong>Call to confirm.</strong> For high-value providers (specialists you see frequently), call both the provider&rsquo;s billing office and the insurer to confirm network status with the exact plan ID. Get the insurer representative&rsquo;s name and note the date.</li>
</ol>

<h2 id="common-mistakes">6. Five common open enrollment mistakes</h2>

<table>
    <thead>
        <tr>
            <th>Mistake</th>
            <th>Average Annual Cost</th>
            <th>How to Avoid It</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Auto-renewing without reviewing plan changes</td><td>$800&ndash;$2,400</td><td>Spend 30 minutes comparing plans every enrollment period; network and formulary changes are common</td></tr>
        <tr><td>Choosing lowest premium without checking OOP max</td><td>$2,000&ndash;$6,000 in a bad year</td><td>Compare total annual cost = premium &times; 12 + expected OOP</td></tr>
        <tr><td>Not checking prescription drug formulary</td><td>$500&ndash;$3,000</td><td>Look up every prescription you take in each plan&rsquo;s formulary; tier 3&ndash;4 drugs cost far more</td></tr>
        <tr><td>Underestimating healthcare use</td><td>$1,000&ndash;$4,000</td><td>Review last year&rsquo;s EOBs to count actual visits and costs; be honest about upcoming planned care</td></tr>
        <tr><td>Enrolling in FSA with HDHP (instead of HSA)</td><td>$500&ndash;$1,500 in lost tax benefit</td><td>HDHP holders must use HSA, not standard FSA; a Limited Purpose FSA is the only FSA compatible with an HSA</td></tr>
    </tbody>
</table>

<h2 id="aca-subsidies">7. ACA subsidies and who qualifies in 2026</h2>

<p>The ACA marketplace offers two types of financial assistance:</p>

<ul>
    <li><strong>Premium tax credits (PTCs):</strong> Available to households with income 100&ndash;400% of the federal poverty level (FPL)&mdash;and extended above 400% FPL under enhanced subsidies still in effect for 2026. In 2026, a single person with $30,000 income may qualify for a $200&ndash;$500/month subsidy reducing a silver plan to near zero.</li>
    <li><strong>Cost-sharing reductions (CSRs):</strong> Available to households with income 100&ndash;250% FPL who enroll in a silver plan. CSRs reduce deductibles, copays, and out-of-pocket maximums significantly&mdash;a silver plan at 150% FPL can have a $300 deductible instead of $1,500.</li>
</ul>

<p>Use the <a href="https://www.healthcare.gov/lower-costs/" target="_blank" rel="noopener">HealthCare.gov estimator</a> to see your specific subsidy before enrollment. If you expect your income to change during the year (job change, freelance income), report it promptly&mdash;reconciliation at tax time can result in a large bill if your income was higher than estimated.</p>

<h2 id="losing-job">8. Losing your job: COBRA vs. marketplace</h2>

<div class="bill-example">
    <div class="bill-header">Sample Annual Cost Comparison &mdash; Employer Plan Options &mdash; 2026 Open Enrollment</div>
    <div class="line-item"><span>Option A: PPO Gold &mdash; Monthly premium $420 &times; 12</span><span>$5,040/yr</span></div>
    <div class="line-item"><span>Option A: Estimated out-of-pocket (moderate use)</span><span>$1,200/yr</span></div>
    <div class="line-item"><span><strong>Option A total estimated annual cost</strong></span><span><strong>$6,240</strong></span></div>
    <div class="line-item flagged"><span>Option B: HDHP &mdash; Monthly premium $185 &times; 12 &nbsp; &#9888; <em>Note: employer contributes $750 to HSA; factor that into your comparison</em></span><span>$2,220/yr</span></div>
    <div class="line-item"><span>Option B: Estimated out-of-pocket (same moderate use)</span><span>$1,200/yr</span></div>
    <div class="line-item"><span>Option B: Employer HSA contribution (credit)</span><span>&minus;$750/yr</span></div>
    <div class="line-item"><span><strong>Option B total estimated annual cost</strong></span><span><strong>$2,670</strong></span></div>
    <div class="line-total"><span>ESTIMATED ANNUAL SAVINGS (HDHP vs. PPO)</span><span>$3,570</span></div>
</div>

<p>Losing job-based coverage triggers a 60-day special enrollment period for both COBRA and the ACA marketplace. Here is how to decide:</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>COBRA</th>
            <th>ACA Marketplace</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Cost</td><td>Full premium (employee + employer share) + 2% admin = often $500&ndash;$1,800/month</td><td>Premium after subsidy; can be $0&ndash;$300/month at lower incomes</td></tr>
        <tr><td>Coverage start</td><td>Retroactive to day coverage was lost</td><td>First of following month (or same month in some states)</td></tr>
        <tr><td>Provider network</td><td>Same as your former employer plan</td><td>New network; may not include all your doctors</td></tr>
        <tr><td>Duration</td><td>Up to 18 months</td><td>Year-round if you qualify for SEP</td></tr>
        <tr><td>Best for</td><td>High earners with planned upcoming medical care (surgery, pregnancy)</td><td>Lower earners who qualify for substantial subsidies</td></tr>
    </tbody>
</table>

<p><strong>Key COBRA tip:</strong> You have 60 days to elect COBRA, and if you elect it, coverage is retroactive to the day it lapsed. You can strategically wait to elect COBRA until you actually incur a medical expense, then elect and pay back premiums retroactively. Only do this if you are confident you can afford the retroactive premiums and are comfortable with the gap risk.</p>

<h2 id="case-study">9. Case study</h2>

<div class="case-study">
    <h3>Switching from PPO to HDHP + HSA&mdash;$3,200 saved in year one</h3>
    <p>A 41-year-old marketing director in Illinois had been on her employer&rsquo;s PPO plan for four years at <strong>$420/month</strong> in premiums ($5,040/year). During 2025 open enrollment, her employer added an HDHP option at <strong>$185/month</strong> ($2,220/year), with a $1,500 individual deductible and a $5,500 out-of-pocket maximum. The employer also contributed $750 to the HSA for anyone who enrolled in the HDHP.</p>
    <p>She reviewed her prior year&rsquo;s EOBs and found she had used $980 in healthcare that year (four primary care visits, one dermatology visit, two generic prescriptions). She ran the total cost calculation: PPO total = $5,040 premium + $980 expected OOP = <strong>$6,020</strong>. HDHP total = $2,220 premium + $980 expected OOP &minus; $750 employer HSA contribution = <strong>$2,450</strong>.</p>
    <p>She enrolled in the HDHP, opened an HSA, and contributed an additional $3,550 of her own money (reaching the $4,300 individual max). She invested the full HSA balance in a low-cost index fund. First-year savings vs. PPO: <strong>$3,570</strong>. She also confirmed all three of her regular providers were in-network for the HDHP product before enrolling. <strong>Projected 5-year benefit including HSA investment growth: over $20,000</strong>.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>When is open enrollment for 2026 health insurance?</h3>
        <p>For employer-sponsored plans, open enrollment typically runs November 1 through December 15, 2026, with coverage starting January 1, 2027. For ACA marketplace plans, open enrollment runs November 1, 2026 through January 15, 2027. Coverage purchased by December 15 starts January 1; coverage purchased January 1&ndash;15 starts February 1.</p>
    </div>
    <div class="faq-item">
        <h3>When does an HDHP with HSA make more financial sense than a PPO?</h3>
        <p>An HDHP with HSA wins financially when your total expected healthcare use is low, the premium savings vs. the PPO are large, and you max the HSA and invest the funds. If you have chronic conditions requiring frequent specialist visits or expensive medications, a PPO&rsquo;s lower cost-sharing usually wins. Always run the total annual cost formula: premium &times; 12 + expected out-of-pocket.</p>
    </div>
    <div class="faq-item">
        <h3>What is a special enrollment period and what triggers it?</h3>
        <p>A special enrollment period lets you enroll in or change health insurance outside of open enrollment. Qualifying life events include: losing other coverage, getting married, having a baby, moving to a new area, and becoming a dependent. For ACA plans, losing Medicaid eligibility or an income change also qualify. You generally have 60 days from the qualifying event to enroll.</p>
    </div>
    <div class="faq-item">
        <h3>If I lose my job, should I choose COBRA or a marketplace plan?</h3>
        <p>Compare COBRA&rsquo;s full premium (often $500&ndash;$1,800/month) against the marketplace silver plan premium after your subsidy. COBRA preserves your existing provider network; marketplace plans often cost less after subsidies if your income dropped. If your income is under 150% of the federal poverty level, you may qualify for a near-zero premium silver plan.</p>
    </div>
    <div class="faq-item">
        <h3>What is the most common open enrollment mistake?</h3>
        <p>Auto-renewal without reviewing. Most employers and marketplace plans automatically re-enroll you in your current plan if you take no action. Plan designs, premiums, formularies, and provider networks can all change year to year. Take 30 minutes every open enrollment period to review the Summary of Benefits and Coverage for your current plan and at least one alternative.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/choose-a-plan/plans-categories/" target="_blank" rel="noopener">HealthCare.gov: Plan Types Explained (HMO, PPO, HDHP, EPO)</a></li>
    <li><a href="https://www.irs.gov/publications/p969" target="_blank" rel="noopener">IRS Publication 969: Health Savings Accounts and Other Tax-Favored Health Plans</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/2025-employer-health-benefits-survey/" target="_blank" rel="noopener">KFF: 2025 Employer Health Benefits Survey</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/faqs/cobra-continuation-coverage" target="_blank" rel="noopener">U.S. Department of Labor: COBRA Continuation Coverage FAQs</a></li>
    <li><a href="https://www.cms.gov/CCIIO/Resources/Files/Downloads/market-rating-reforms-value-based-insurance-design.pdf" target="_blank" rel="noopener">CMS: ACA Marketplace Plan Design and Value-Based Insurance</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.01294" target="_blank" rel="noopener">Health Affairs: Enhanced ACA Subsidies and Enrollment Outcomes, 2023&ndash;2025</a></li>
</ul>
""",
})
