"""Guide: Medicare Part D Drug Coverage"""

from guides import register, _embed

register("medicare-part-d-drug-coverage", {
    "title": "Medicare Part D Drug Coverage: Formulary Tiers, the Donut Hole, and Extra Help",
    "meta_description": "Medicare Part D drug coverage explained: formulary tiers 1-5, coverage gap status, catastrophic threshold, formulary exceptions, Extra Help LIS program, and comparing Part D plans in 2026.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "What are Medicare Part D formulary tiers?",
            "a": "Medicare Part D drug formularies use 5 tiers to set cost-sharing levels. Tier 1 is generic drugs (lowest copay, typically $0&ndash;$5). Tier 2 is preferred brand-name drugs ($10&ndash;$40). Tier 3 is non-preferred brand-name drugs ($40&ndash;$100). Tier 4 is specialty drugs ($100&ndash;$200 or 25&ndash;33% coinsurance). Tier 5 is select care specialty drugs (higher coinsurance). Higher tiers mean higher out-of-pocket costs.",
        },
        {
            "q": "Is the Medicare donut hole still in effect in 2026?",
            "a": "The coverage gap (donut hole) was largely eliminated by the Inflation Reduction Act. In 2026, once you spend $2,000 out-of-pocket on Part D drugs (the catastrophic threshold), your cost-sharing drops to $0 for the rest of the year. The traditional donut hole structure no longer creates a period of dramatically increased drug costs the way it did before 2024.",
        },
        {
            "q": "What is the Extra Help program for Medicare Part D?",
            "a": "Extra Help (also called the Low Income Subsidy or LIS) is a federal program that pays most or all of your Part D premium, deductible, and copays if you have limited income and resources. Qualifying saves an average of $5,000 per year in drug costs. You qualify automatically if you receive full Medicaid, SSI, or Medicare Savings Program benefits. Others can apply through Social Security.",
        },
        {
            "q": "How do I request a formulary exception for a drug not on my plan's formulary?",
            "a": "Ask your doctor to submit a formulary exception request to your Part D plan, with documentation that the requested drug is medically necessary and that formulary alternatives are not appropriate for you. The plan must respond within 72 hours (24 hours for expedited requests). If denied, you can appeal through the Part D appeals process.",
        },
        {
            "q": "When can I change my Medicare Part D plan?",
            "a": "You can change Part D plans during Medicare's Annual Enrollment Period (October 15 &ndash; December 7), with changes effective January 1. If you have Extra Help (LIS), you can switch Part D plans once per quarter in the first three quarters of the year.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> Medicare Part D covers outpatient prescription drugs through private plans using a tiered formulary system. In 2026, your out-of-pocket drug costs are capped at $2,000/year after which you pay nothing. If you have low income, the Extra Help program can save you $5,000+ per year. Comparing Part D plans annually during open enrollment is essential because formularies change every year.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-part-d-works">How Part D Works</a></li>
        <li><a href="#formulary-tiers">Formulary Tiers 1&ndash;5</a></li>
        <li><a href="#donut-hole">The Coverage Gap: 2026 Status</a></li>
        <li><a href="#catastrophic">Catastrophic Coverage Threshold</a></li>
        <li><a href="#exceptions">How to Request a Formulary Exception</a></li>
        <li><a href="#extra-help">Extra Help / Low Income Subsidy</a></li>
        <li><a href="#prior-auth">Prior Authorization for Specialty Drugs</a></li>
        <li><a href="#comparing-plans">How to Compare Part D Plans</a></li>
    </ol>
</nav>

<h2 id="how-part-d-works">How Part D Works</h2>

<p>Medicare Part D is prescription drug coverage. Unlike Parts A and B, which are run directly by the federal government, Part D plans are operated by private insurance companies approved by CMS. You enroll in a Part D plan from your local options, each with its own formulary (drug list), premiums, and cost-sharing structure.</p>

<p>Part D plans come in two forms:</p>
<ul>
    <li><strong>Standalone Prescription Drug Plans (PDPs):</strong> Add drug coverage to Original Medicare. You keep your original Medicare and Medigap coverage and add a Part D plan for drugs.</li>
    <li><strong>Medicare Advantage Prescription Drug (MA-PD) plans:</strong> Combine all Medicare coverage (Parts A, B, and D) through a Medicare Advantage plan.</li>
</ul>

<p>Key 2026 Part D parameters:</p>
<table>
    <thead>
        <tr><th>Parameter</th><th>2026 Standard</th></tr>
    </thead>
    <tbody>
        <tr><td>Annual Deductible (standard maximum)</td><td>$590</td></tr>
        <tr><td>Out-of-Pocket Cap (catastrophic threshold)</td><td>$2,000</td></tr>
        <tr><td>Standard Monthly Premium (national average)</td><td>~$46/month</td></tr>
        <tr><td>Late Enrollment Penalty</td><td>1% per month without coverage</td></tr>
    </tbody>
</table>

<h2 id="formulary-tiers">Formulary Tiers 1&ndash;5</h2>

<p>Every Part D plan uses a formulary&mdash;a list of covered drugs&mdash;organized into tiers that determine your copay or coinsurance. The specific drugs in each tier and the exact cost-sharing vary by plan, but the general structure is consistent:</p>

<table>
    <thead>
        <tr><th>Tier</th><th>Drug Type</th><th>Typical Copay (30-day supply)</th></tr>
    </thead>
    <tbody>
        <tr><td>Tier 1</td><td>Preferred generic drugs</td><td>$0&ndash;$5</td></tr>
        <tr><td>Tier 2</td><td>Generic and preferred brand drugs</td><td>$10&ndash;$20</td></tr>
        <tr><td>Tier 3</td><td>Non-preferred brand-name drugs</td><td>$40&ndash;$100</td></tr>
        <tr><td>Tier 4</td><td>Non-preferred brand / specialty drugs</td><td>$100&ndash;$200 or 25&ndash;33%</td></tr>
        <tr><td>Tier 5</td><td>Select care specialty / high-cost biologics</td><td>25&ndash;33% coinsurance</td></tr>
    </tbody>
</table>

<p>A drug that costs you $10/month on one plan may cost $100/month on another if it's in a higher tier. This is why comparing plans annually using Medicare's Plan Finder tool is essential&mdash;formularies change every year and your drug may move to a more expensive tier.</p>

<h3>Formulary changes and transition fills</h3>
<p>Part D plans can change their formularies mid-year for certain drugs. If your drug is removed from the formulary or moved to a higher tier mid-year, your plan must provide a 60-day notice and give you a 30-day transition fill (one fill at the current cost-sharing) to allow time to find an alternative.</p>

<h2 id="donut-hole">The Coverage Gap: 2026 Status</h2>

<p>The "donut hole" was the original Part D coverage gap: after spending a certain amount on drugs, you entered a coverage gap where you paid significantly more out-of-pocket until you reached catastrophic coverage. This structure was phased out by the Affordable Care Act and fully transformed by the Inflation Reduction Act (IRA) of 2022.</p>

<p>The IRA fundamentally changed Part D starting in 2024:</p>
<ul>
    <li>The catastrophic out-of-pocket cap was set at <strong>$2,000 in 2026</strong>. Once you spend $2,000 out-of-pocket on covered Part D drugs, you pay <strong>$0</strong> for the rest of the year.</li>
    <li>The traditional "donut hole" gap is gone. There is no longer a period where you suddenly pay 25&ndash;100% of drug costs after reaching a certain spending threshold.</li>
    <li>Manufacturers of brand-name drugs are required to provide discounts that count toward your out-of-pocket total, reducing how quickly you hit the $2,000 cap.</li>
    <li>For beneficiaries on expensive specialty drugs (e.g., cancer medications, MS drugs, biologics), the $2,000 cap provides enormous protection compared to the previous system.</li>
</ul>

<div class="key-takeaway">
    <strong>The $2,000 out-of-pocket cap is one of the most significant Medicare improvements in decades.</strong> Before 2024, there was no catastrophic limit on Part D drug costs. A $100,000/year specialty drug could cost a beneficiary $10,000+ annually in Part D. In 2026, the maximum you pay for covered Part D drugs is $2,000.
</div>

<h2 id="catastrophic">Catastrophic Coverage Threshold</h2>

<p>In 2026, once you've paid <strong>$2,000 out-of-pocket</strong> in covered Part D drugs, you enter the "catastrophic coverage" phase where your cost-sharing drops to $0 for the rest of the plan year.</p>

<p>What counts toward the $2,000 out-of-pocket:</p>
<ul>
    <li>Your actual copays and coinsurance for covered drugs</li>
    <li>Your annual deductible payments</li>
    <li>Manufacturer discounts on brand-name drugs (counts toward your total)</li>
</ul>

<p>What does <em>not</em> count:</p>
<ul>
    <li>Your monthly premium</li>
    <li>Costs for drugs not on your plan's formulary</li>
    <li>Costs for drugs you pay for outside your plan (e.g., using GoodRx instead of your Part D)</li>
</ul>

<p>The Medicare Part D Payment Modernization program also lets you spread your out-of-pocket drug costs over monthly payments rather than paying them all at the pharmacy at once. Ask your plan about the Medicare Prescription Payment Plan (MPPP) option.</p>

{_embed("cost", title="Estimate Your Part D Drug Costs", subtitle="Compare Part D plans based on your actual medications.")}

<h2 id="exceptions">How to Request a Formulary Exception</h2>

<p>If your drug is not on your plan's formulary, or if it's on the formulary but your doctor believes a higher-tier drug is medically necessary, you can request a formulary exception.</p>

<ol>
    <li><strong>Have your doctor submit the request.</strong> The plan requires a physician statement explaining why the formulary drug alternatives are not appropriate for your specific medical condition.</li>
    <li><strong>Request an expedited review if medically urgent.</strong> Standard review: 72 hours. Expedited review: 24 hours. If your condition is serious, request expedited.</li>
    <li><strong>If denied, appeal.</strong> Part D exception denials go through the standard Part D appeals process (redetermination, IRO review, ALJ hearing).</li>
    <li><strong>Document everything.</strong> Keep copies of the exception request, supporting medical documentation, and all correspondence.</li>
</ol>

<p>Common grounds for a successful formulary exception:</p>
<ul>
    <li>You tried the formulary alternatives and experienced adverse effects or treatment failure</li>
    <li>Your condition requires a specific drug formulation not available among the formulary alternatives</li>
    <li>A drug interaction prevents you from taking formulary alternatives</li>
    <li>Your treating specialist has documented a specific clinical reason why the requested drug is superior for your case</li>
</ul>

<h2 id="extra-help">Extra Help / Low Income Subsidy</h2>

<p>Extra Help (also called the Low Income Subsidy or LIS) is a federal program that virtually eliminates Part D drug costs for qualifying low-income Medicare beneficiaries. In 2026, Extra Help is worth an average of <strong>$5,000 per year</strong>.</p>

<p>With full Extra Help, your Part D costs are:</p>
<ul>
    <li>Premium: $0 (plan premium paid by Extra Help)</li>
    <li>Annual deductible: $0</li>
    <li>Copays: $1.10&ndash;$3.40 for generics; $3.40&ndash;$10.35 for brand-name drugs (2026 amounts)</li>
    <li>Catastrophic phase: $0</li>
</ul>

<h3>Who qualifies automatically for Extra Help</h3>
<p>You are automatically enrolled in Extra Help if you receive:</p>
<ul>
    <li>Full Medicaid benefits (Medicaid-Medicare dual eligibles)</li>
    <li>Supplemental Security Income (SSI)</li>
    <li>Benefits through a Medicare Savings Program (MSP)</li>
</ul>

<h3>Who can apply for Extra Help</h3>
<p>Even if you don't get Medicaid or SSI, you may qualify for Extra Help if your annual income is below approximately $22,590 (individual) or $30,660 (married couple) in 2026, and your assets are limited. Apply through Social Security at ssa.gov/extrahelp or call 1-800-772-1213.</p>

<h2 id="prior-auth">Prior Authorization for Specialty Drugs</h2>

<p>Part D plans require prior authorization for many specialty and high-cost drugs. Prior auth requirements are most common for:</p>
<ul>
    <li>Specialty drugs in Tier 4 and Tier 5</li>
    <li>Drugs with significant risk of misuse or abuse</li>
    <li>Brand-name drugs when generic equivalents exist</li>
    <li>Drugs with narrow therapeutic windows requiring clinical monitoring</li>
</ul>

<p>Steps to navigate Part D prior authorization:</p>
<ol>
    <li>Have your prescribing physician confirm the clinical diagnosis and necessity documentation is complete</li>
    <li>Ask the pharmacy or your doctor to initiate the prior auth request directly with the plan</li>
    <li>If denied, request peer-to-peer review between your physician and the plan's medical director</li>
    <li>If still denied, file a formal Part D coverage determination appeal</li>
</ol>

<h2 id="comparing-plans">How to Compare Part D Plans During Open Enrollment</h2>

<p>Part D plan quality varies enormously. The single best tool for comparing plans is <strong>Medicare.gov's Plan Finder</strong> at medicare.gov/plan-compare. Steps:</p>

<ol>
    <li>Enter all the drugs you take with exact dosage and supply frequency</li>
    <li>Sort plans by estimated annual drug costs (includes premium + expected drug costs)</li>
    <li>Verify your preferred pharmacy is in-network for the top plans</li>
    <li>Check the plan's Star Rating&mdash;prefer plans with 4+ stars</li>
    <li>Confirm your current drugs are on the formulary and at what tier</li>
    <li>Check deductible amounts (some plans waive the deductible for Tier 1&ndash;2 drugs)</li>
</ol>

<p>Open enrollment runs <strong>October 15 &ndash; December 7</strong> annually. Changes take effect January 1. Review your plan every year even if you are satisfied&mdash;formularies and premiums change, and a plan that was optimal last year may not be this year.</p>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/drug-coverage-part-d" target="_blank" rel="noopener">Medicare.gov &mdash; Drug Coverage (Part D)</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/prescription-drug-coverage" target="_blank" rel="noopener">CMS &mdash; Prescription Drug Coverage</a></li>
    <li><a href="https://www.ssa.gov/medicare/part-d-extra-help" target="_blank" rel="noopener">SSA &mdash; Extra Help with Part D Costs</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/the-inflation-reduction-acts-medicare-drug-price-negotiation-program/" target="_blank" rel="noopener">KFF &mdash; IRA Medicare Drug Price Changes</a></li>
</ul>
</article>""",
})
