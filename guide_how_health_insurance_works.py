"""Guide: How Health Insurance Works."""

from guides import register, _embed

register("how-health-insurance-works", {
    "title": "How Health Insurance Works: A Complete Guide to Premiums",
    "meta_description": "Understand how health insurance actually works: premiums, deductibles, copays, coinsurance, out-of-pocket maximums, how claims flow, and network types.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Insurance",
    "faqs": [
        {
            "q": "What is the difference between a deductible and an out-of-pocket maximum?",
            "a": "Your deductible is the amount you pay before insurance starts sharing costs (e.g., $1,500). After meeting your deductible, you pay coinsurance (e.g., 20%) while insurance pays the rest. Your out-of-pocket maximum is the absolute most you will pay in a year (e.g., $8,000). After reaching it, insurance covers 100% of in-network costs. The out-of-pocket max includes your deductible, copays, and coinsurance.",
        },
        {
            "q": "What is the difference between a copay and coinsurance?",
            "a": "A copay is a flat dollar amount you pay for a service (e.g., $30 for a doctor visit). Coinsurance is a percentage of the allowed amount (e.g., 20% of a $5,000 surgery = $1,000). Some plans use copays for routine visits and coinsurance for larger services like hospital stays and surgeries. Both count toward your out-of-pocket maximum.",
        },
        {
            "q": "What happens if I go to an out-of-network doctor?",
            "a": "If you have an HMO or EPO plan, out-of-network care generally is not covered at all except in emergencies. With a PPO or POS plan, out-of-network care is covered but at a lower rate (e.g., 50% instead of 80%), and the provider can balance bill you for the difference between their full charge and the insurance-allowed amount. Out-of-network costs often have a separate, higher deductible and out-of-pocket maximum.",
        },
        {
            "q": "What is an Explanation of Benefits (EOB)?",
            "a": "An EOB is a statement from your insurance company showing how a claim was processed. It lists the provider's charges, the insurance-allowed amount, what insurance paid, and what you owe. An EOB is not a bill. You will receive a separate bill from the provider for your portion. Always compare your EOB to the provider's bill to make sure they match.",
        },
        {
            "q": "When is open enrollment and can I get insurance outside of it?",
            "a": "Open enrollment for ACA marketplace plans typically runs from November 1 to January 15. Employer plans set their own enrollment periods, usually in the fall. Outside open enrollment, you can only enroll or change plans if you have a qualifying life event: job loss, marriage, divorce, having a baby, moving to a new state, or losing other coverage.",
        },
    ],
    "body": f"""
<p class="lead">Health insurance is the single biggest factor in what you actually pay for medical care&mdash;yet most Americans don&rsquo;t fully understand how it works. A 2024 survey found that <strong>56% of insured adults</strong> could not correctly define basic terms like deductible and coinsurance. That confusion costs real money: people who don&rsquo;t understand their coverage overpay on bills, skip preventive care, and choose plans that don&rsquo;t match their needs. Here&rsquo;s how health insurance actually works, in plain language.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#key-terms">The 5 key terms you must understand</a></li>
        <li><a href="#how-costs-flow">How costs flow: a visual example</a></li>
        <li><a href="#claims-process">How the claims process works</a></li>
        <li><a href="#network-types">Network types: HMO, PPO, EPO, and POS</a></li>
        <li><a href="#choosing-plan">How to choose the right plan</a></li>
        <li><a href="#open-enrollment">Open enrollment and special enrollment</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="key-terms">1. The 5 key terms you must understand</h2>

<p>Every health insurance plan has the same five cost components. Understanding how they interact is the foundation of managing your medical costs:</p>

<table>
    <thead>
        <tr><th>Term</th><th>What It Is</th><th>Typical Range</th><th>When You Pay It</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Premium</strong></td><td>Monthly payment to keep your insurance active</td><td>$200&ndash;$700/month (individual)</td><td>Every month, regardless of whether you use care</td></tr>
        <tr><td><strong>Deductible</strong></td><td>Amount you pay out of pocket before insurance starts paying</td><td>$500&ndash;$8,000/year</td><td>First, for most non-preventive services</td></tr>
        <tr><td><strong>Copay</strong></td><td>Flat fee for a specific service (e.g., $30 for a doctor visit)</td><td>$20&ndash;$75 per visit</td><td>At the time of service</td></tr>
        <tr><td><strong>Coinsurance</strong></td><td>Your percentage share after the deductible is met (e.g., you pay 20%)</td><td>10&ndash;40% of allowed amount</td><td>After meeting your deductible</td></tr>
        <tr><td><strong>Out-of-pocket maximum</strong></td><td>The most you pay in a year; after this, insurance covers 100%</td><td>$3,000&ndash;$9,200/year</td><td>Caps your annual costs</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The relationship:</strong> You pay your premium every month. When you get care, you pay the full allowed amount until you hit your deductible. Then you pay coinsurance (your percentage) until you hit your out-of-pocket maximum. After the out-of-pocket max, insurance pays 100%. Preventive care is always free, regardless of deductible status. Learn exactly which services qualify in <a href="/guides/preventive-care-billing">our guide to preventive care billing</a>.
</div>

<h2 id="how-costs-flow">2. How costs flow: a visual example</h2>

<p>Let&rsquo;s trace how a <strong>$12,000 surgery</strong> gets paid on a plan with a $1,500 deductible, 20% coinsurance, and $6,000 out-of-pocket maximum. Assume the patient has already paid $500 toward the deductible this year.</p>

<div class="bill-example">
    <div class="bill-header">Cost Breakdown &mdash; $12,000 Surgery &mdash; Plan: $1,500 Deductible / 20% Coinsurance / $6,000 OOP Max</div>
    <div class="line-item">
        <span>Hospital billed amount</span>
        <span>$12,000.00</span>
    </div>
    <div class="line-item">
        <span>Insurance-allowed (negotiated) amount</span>
        <span>$8,400.00</span>
    </div>
    <div class="line-item">
        <span>Network discount (hospital writes off)</span>
        <span>&minus;$3,600.00</span>
    </div>
    <div class="line-item">
        <span>Remaining deductible ($1,500 &minus; $500 already paid)</span>
        <span>$1,000.00</span>
    </div>
    <div class="line-item">
        <span>Coinsurance: 20% of remaining $7,400</span>
        <span>$1,480.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays: 80% of remaining $7,400</span>
        <span>$5,920.00</span>
    </div>
    <div class="line-total">
        <span>YOUR TOTAL COST</span>
        <span>$2,480.00</span>
    </div>
</div>

<p><strong>What happened:</strong> The hospital charged $12,000, but the insurance-negotiated rate was only $8,400 (the &ldquo;allowed amount&rdquo;). The patient paid the remaining $1,000 deductible, then 20% coinsurance on the rest ($1,480). Total patient cost: <strong>$2,480</strong>. If this patient has more care this year, they only need to pay $3,020 more before hitting the $6,000 out-of-pocket max (they&rsquo;ve already paid $500 + $1,000 + $1,480 = $2,980). Use our <a href="/calculator">cost calculator</a> to look up the Medicare allowable rate for any procedure&mdash;it&rsquo;s a useful benchmark for what you should expect to pay.</p>

<div class="case-study">
    <h3>Case study: Understanding your plan saves $4,200</h3>
    <p><strong>Situation:</strong> David needed knee surgery. His in-network surgeon quoted $15,000 (allowed amount: $9,800). David had a $2,000 deductible (already met) and 20% coinsurance with a $7,000 out-of-pocket max. He had already paid $3,500 toward his OOP max earlier in the year.</p>
    <p><strong>What he calculated:</strong> 20% of $9,800 = $1,960 in coinsurance. But wait&mdash;he had already paid $3,500 toward his $7,000 OOP max, meaning he only had $3,500 left before hitting it. Since $1,960 was less than $3,500, he&rsquo;d pay the full $1,960.</p>
    <p><strong>If he had waited:</strong> David realized that if he had the surgery in January of the next year, his OOP max and deductible would reset, and he&rsquo;d owe $2,000 (deductible) + $1,560 (20% of remaining $7,800) = <strong>$3,560</strong>. By having the surgery in the current year after already accumulating $3,500 in costs, he paid only <strong>$1,960</strong>. <strong>Timing saved him $1,600.</strong></p>
    <p>Additionally, David <a href="/scan">scanned his post-surgery bill</a> and found two duplicate charges totaling $2,600 that had inflated the billed amount. After correction, his coinsurance dropped further. <strong>Total savings from understanding his plan and auditing the bill: $4,200.</strong></p>
</div>

{_embed(mode="cost", cpt="27447", title="Look up surgery costs", subtitle="See what Medicare pays for common procedures.")}

<h2 id="claims-process">3. How the claims process works</h2>

<p>Understanding how a claim moves from your doctor&rsquo;s office to your mailbox explains why bills can take weeks and why errors happen:</p>

<ol>
    <li><strong>You receive care.</strong> The provider documents the visit, diagnoses, and procedures.</li>
    <li><strong>Provider submits a claim.</strong> The billing department sends a claim to your insurance company with CPT codes (procedures) and ICD-10 codes (diagnoses). This usually happens within 1&ndash;5 business days.</li>
    <li><strong>Insurance processes the claim (adjudication).</strong> The insurer checks your coverage, applies the allowed amount, calculates your deductible and coinsurance, and determines what they pay vs. what you owe. This takes 15&ndash;45 days.</li>
    <li><strong>You receive an EOB.</strong> Your insurance sends an Explanation of Benefits showing how the claim was processed. This is <strong>not a bill</strong>&mdash;it&rsquo;s a statement from your insurer.</li>
    <li><strong>Provider sends your bill.</strong> After receiving insurance payment, the provider bills you for your remaining balance (deductible, coinsurance, copay, or any denied amounts). Compare this to your EOB carefully&mdash;see <a href="/guides/understanding-your-eob">our guide to reading your EOB</a> for help.</li>
</ol>

<div class="key-takeaway">
    <strong>Always compare the EOB to the provider&rsquo;s bill.</strong> They should match. If the provider bills more than what the EOB says you owe, that&rsquo;s a billing error. Common discrepancies include the provider billing you for the full charge instead of the allowed amount, or not crediting the insurance payment. <a href="/scan">Upload your bill to BillKarma</a> to check for errors.
</div>

<h2 id="network-types">4. Network types: HMO, PPO, EPO, and POS</h2>

<p>Your plan&rsquo;s network type determines which doctors you can see and how much you pay for out-of-network care:</p>

<table>
    <thead>
        <tr><th>Plan Type</th><th>Need Referral?</th><th>Out-of-Network Coverage</th><th>Cost Level</th><th>Best For</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>HMO</strong> (Health Maintenance Organization)</td><td>Yes, from PCP</td><td>None (except emergencies)</td><td>Lowest premiums</td><td>People who want lower costs and don&rsquo;t mind referrals</td></tr>
        <tr><td><strong>PPO</strong> (Preferred Provider Organization)</td><td>No</td><td>Partial (higher cost-sharing)</td><td>Highest premiums</td><td>People who want flexibility to see specialists without referrals</td></tr>
        <tr><td><strong>EPO</strong> (Exclusive Provider Organization)</td><td>No</td><td>None (except emergencies)</td><td>Moderate premiums</td><td>People who want no referrals but don&rsquo;t need out-of-network coverage</td></tr>
        <tr><td><strong>POS</strong> (Point of Service)</td><td>Yes, from PCP</td><td>Partial (higher cost-sharing)</td><td>Moderate premiums</td><td>People who want some out-of-network flexibility with a PCP gatekeeper</td></tr>
    </tbody>
</table>

<p><strong>The cost difference is real.</strong> An in-network MRI might cost you $400 (after negotiated rates and insurance). The same MRI out-of-network on a PPO plan might cost $1,200 (higher coinsurance plus balance billing). On an HMO, the out-of-network MRI may not be covered at all, leaving you with the full $3,000+ charge. Check how hospitals in your area price common procedures in our <a href="/hospitals/">hospital pricing directory</a>.</p>

<h2 id="choosing-plan">5. How to choose the right plan</h2>

<p>The right plan depends on how much care you expect to use. Here is a simplified framework:</p>

<p><strong>If you are healthy and rarely see doctors:</strong> Choose a high-deductible plan (HDHP) with low premiums. Pair it with a Health Savings Account (HSA) to save pre-tax dollars for medical costs. You&rsquo;ll pay more if something happens, but your monthly costs are minimized.</p>

<p><strong>If you have ongoing medical needs:</strong> Choose a plan with a lower deductible and lower coinsurance, even if premiums are higher. If you know you&rsquo;ll hit your deductible every year, the lower deductible plan almost always saves money overall.</p>

<p><strong>If you see specialists frequently:</strong> Choose a PPO or EPO so you can see specialists without referrals. The premium is higher, but avoiding the referral process and having broader provider choices saves time and can prevent delays in care. Before selecting a plan, look up the hospitals and providers you use most in our <a href="/hospitals/">hospital directory</a> to see how their pricing compares.</p>

<p><strong>The math check:</strong> Add up your expected annual costs: (monthly premium &times; 12) + expected deductible + expected coinsurance. Compare this total across plans. The cheapest premium is not always the cheapest plan.</p>

<div class="key-takeaway">
    <strong>The #1 mistake:</strong> Choosing the lowest-premium plan without calculating total costs. A plan with a $150/month premium and $6,000 deductible costs $1,800/year in premiums alone. If you need a $5,000 procedure, you pay $6,800 total. A $300/month plan with a $1,500 deductible costs $3,600 in premiums plus $1,500 deductible = $5,100 total. The &ldquo;expensive&rdquo; plan saves you $1,700. For a deeper dive on deductibles and out-of-pocket costs, see <a href="/guides/out-of-pocket-maximum-explained">our guide to out-of-pocket maximums</a>.
</div>

<h2 id="open-enrollment">6. Open enrollment and special enrollment</h2>

<p><strong>Open enrollment</strong> is the annual window when you can enroll in, switch, or drop a health insurance plan. For ACA marketplace plans, open enrollment typically runs <strong>November 1 through January 15</strong>. Employer-sponsored plans set their own window, usually in the fall.</p>

<p><strong>Special enrollment periods (SEPs)</strong> allow you to enroll or change plans outside of open enrollment if you experience a qualifying life event:</p>

<ul>
    <li>Losing existing health coverage (job loss, aging off a parent&rsquo;s plan)</li>
    <li>Getting married or divorced</li>
    <li>Having or adopting a child</li>
    <li>Moving to a new state or ZIP code</li>
    <li>Changes in household income affecting marketplace subsidy eligibility</li>
</ul>

<p>SEPs typically give you <strong>60 days</strong> from the qualifying event to enroll. Missing this window means waiting until the next open enrollment. If you&rsquo;re between plans and receive a medical bill, <a href="/scan">scan it with BillKarma</a> to make sure you&rsquo;re not being overcharged while uninsured.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the difference between a deductible and an out-of-pocket maximum?</h3>
        <p>Your deductible is the amount you pay before insurance starts covering costs. Your out-of-pocket maximum is the total cap on what you pay in a year, including deductible, copays, and coinsurance. After hitting the OOP max, insurance covers 100% of in-network costs for the rest of the year.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a copay and coinsurance?</h3>
        <p>A copay is a fixed dollar amount (e.g., $30 for a doctor visit). Coinsurance is a percentage of the cost (e.g., 20% of a $5,000 surgery = $1,000). Both count toward your out-of-pocket maximum.</p>
    </div>

    <div class="faq-item">
        <h3>What happens if I go to an out-of-network doctor?</h3>
        <p>With HMO or EPO plans, out-of-network care generally is not covered except in emergencies. With PPO or POS plans, it is covered at a lower rate with higher cost-sharing, and the provider can balance bill you. Always verify a provider&rsquo;s network status before receiving care.</p>
    </div>

    <div class="faq-item">
        <h3>What is an Explanation of Benefits (EOB)?</h3>
        <p>An EOB is a statement from your insurer showing how a claim was processed&mdash;what was billed, the allowed amount, what insurance paid, and what you owe. It is not a bill. Always compare your EOB to the provider&rsquo;s bill to ensure accuracy.</p>
    </div>

    <div class="faq-item">
        <h3>When is open enrollment and can I get insurance outside of it?</h3>
        <p>ACA marketplace open enrollment runs November 1 through January 15. Outside this window, you need a qualifying life event (job loss, marriage, baby, move) to enroll during a special enrollment period, which lasts 60 days from the event.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: How Health Insurance Works</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Employer Health Benefits Survey (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Marketplace Open Enrollment Period</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Health Insurance Literacy Survey (2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">U.S. Department of Labor: Understanding Your Health Plan</a></li>
</ul>
""",
})
