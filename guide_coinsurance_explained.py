"""Guide: What Is Coinsurance? How the 80/20 Split Works."""

from guides import register, _embed

register("what-is-coinsurance", {
    "title": "What Is Coinsurance? How the 80/20 Split Actually Works",
    "meta_description": "Coinsurance is the percentage you pay after your deductible is met. Learn how the 80/20 split works, how it differs from copays, and how to calculate your real exposure.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is coinsurance in health insurance?",
            "a": "Coinsurance is the percentage of a covered medical cost that you pay after your deductible has been met. For example, with 20% coinsurance, you pay 20% of the allowed amount for a service and your insurance pays 80%. Coinsurance continues until you reach your out-of-pocket maximum, after which insurance pays 100%.",
        },
        {
            "q": "What is the difference between coinsurance and a copay?",
            "a": "A copay is a flat dollar amount you pay for a specific service (e.g., $30 for a primary care visit). Coinsurance is a percentage of the cost (e.g., 20% of a $5,000 hospital bill = $1,000). Copays are predictable regardless of the cost of the service. Coinsurance scales with the cost — the more expensive the service, the more you pay. Both types of cost-sharing count toward your out-of-pocket maximum.",
        },
        {
            "q": "Does coinsurance apply before or after the deductible?",
            "a": "Coinsurance applies after your deductible is met. You pay 100% of covered costs until you reach your deductible. Once your deductible is met, coinsurance kicks in — you pay your percentage (e.g., 20%) and insurance pays the rest (e.g., 80%).",
        },
        {
            "q": "What does 80/20 coinsurance mean?",
            "a": "80/20 coinsurance means your insurance pays 80% of covered costs and you pay 20%, after your deductible is met. On a $10,000 hospital bill with a $3,000 deductible already paid, you would owe 20% of the remaining $10,000 = $2,000. Your insurance pays $8,000.",
        },
        {
            "q": "When does coinsurance stop?",
            "a": "Coinsurance stops when you reach your out-of-pocket maximum for the year. After that, insurance covers 100% of covered in-network services for the rest of the year.",
        },
    ],
    "body": f"""
<p class="lead">Coinsurance is the percentage of a medical bill you pay after your deductible is met. It sounds simple &mdash; but BillKarma data shows patients underestimate their total cost-sharing by an average of <strong>$1,800</strong> because they calculate only their deductible and forget that coinsurance can stack thousands of dollars of additional exposure on top of it. Here is exactly how coinsurance works and how to calculate your real out-of-pocket costs.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-coinsurance-works">How coinsurance works</a></li>
        <li><a href="#coinsurance-vs-copay">Coinsurance vs. copay: key differences</a></li>
        <li><a href="#coinsurance-vs-deductible">Coinsurance vs. deductible: the sequence</a></li>
        <li><a href="#common-splits">Common coinsurance splits: 80/20, 70/30, 60/40</a></li>
        <li><a href="#oon-coinsurance">In-network vs. out-of-network coinsurance</a></li>
        <li><a href="#prescriptions">Coinsurance for prescriptions</a></li>
        <li><a href="#medicare">Medicare coinsurance in 2026</a></li>
        <li><a href="#planning">Calculating your maximum coinsurance exposure</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-coinsurance-works">1. How coinsurance works</h2>

<p>Coinsurance is triggered once you have paid your full deductible for the year. At that point, instead of paying 100% of covered costs, you pay a fixed percentage &mdash; and your insurer pays the rest.</p>

<p>Here is a concrete example on a plan with a <strong>$3,000 deductible and 20% coinsurance</strong>:</p>

<div class="bill-example">
    <div class="bill-header">Hospital Bill &mdash; $10,000 Allowed Amount &mdash; Deductible Already Met</div>
    <div class="line-item">
        <span>Allowed amount (insurer&rsquo;s contracted rate for the service)</span>
        <span>$10,000.00</span>
    </div>
    <div class="line-item">
        <span>Deductible remaining (already met for the year)</span>
        <span>$0.00</span>
    </div>
    <div class="line-item">
        <span>Your coinsurance: 20% of $10,000</span>
        <span>$2,000.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays: 80% of $10,000</span>
        <span>$8,000.00</span>
    </div>
    <div class="line-total">
        <span>YOU OWE</span>
        <span>$2,000.00</span>
    </div>
</div>

<p>Now the same scenario, but the deductible is only <strong>partially met</strong> (you have $1,500 remaining on your $3,000 deductible):</p>

<div class="bill-example">
    <div class="bill-header">Hospital Bill &mdash; $10,000 Allowed Amount &mdash; $1,500 Deductible Remaining</div>
    <div class="line-item">
        <span>Allowed amount</span>
        <span>$10,000.00</span>
    </div>
    <div class="line-item">
        <span>You pay: remaining deductible</span>
        <span>$1,500.00</span>
    </div>
    <div class="line-item">
        <span>You pay: 20% coinsurance on remaining $8,500</span>
        <span>$1,700.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays: 80% of $8,500</span>
        <span>$6,800.00</span>
    </div>
    <div class="line-total">
        <span>YOU OWE</span>
        <span>$3,200.00</span>
    </div>
</div>

<div class="key-takeaway">
    <strong>The coinsurance percentage applies to the allowed amount, not the billed amount.</strong> If a hospital bills $25,000 but the insurance-allowed rate is $10,000, your 20% applies to $10,000 ($2,000), not $25,000 ($5,000). This is why in-network care is significantly cheaper. See <a href="/guides/explanation-of-benefits-eob">our EOB guide</a> to understand how allowed amounts appear on your statement.
</div>

{_embed(mode="markup", title="Check if your charge is reasonable", subtitle="Enter a CPT code and billed amount to compare against Medicare&rsquo;s allowed rate.", height="420")}

<h2 id="coinsurance-vs-copay">2. Coinsurance vs. copay: key differences</h2>

<table>
    <thead>
        <tr><th></th><th>Copay</th><th>Coinsurance</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Structure</strong></td>
            <td>Flat dollar amount</td>
            <td>Percentage of the allowed amount</td>
        </tr>
        <tr>
            <td><strong>Example</strong></td>
            <td>$35 per primary care visit</td>
            <td>20% of a $5,000 surgery = $1,000</td>
        </tr>
        <tr>
            <td><strong>Predictability</strong></td>
            <td>Known in advance; same every time</td>
            <td>Varies with the cost of each service</td>
        </tr>
        <tr>
            <td><strong>When it applies</strong></td>
            <td>At time of service, often before deductible</td>
            <td>After deductible is met</td>
        </tr>
        <tr>
            <td><strong>Counts toward OOP max?</strong></td>
            <td>Yes (on most ACA-compliant plans)</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td><strong>Typical use</strong></td>
            <td>Routine office visits, urgent care, prescriptions</td>
            <td>Major services: hospital, surgery, imaging</td>
        </tr>
    </tbody>
</table>

<p>Many plans use both. You might have a $35 copay for a primary care visit (no deductible applies) and 20% coinsurance for a hospital stay (applies after deductible). Both count toward your out-of-pocket maximum. For a deeper look at the deductible-coinsurance relationship, see <a href="/guides/what-is-a-deductible">our deductible guide</a>.</p>

<h2 id="coinsurance-vs-deductible">3. Coinsurance vs. deductible: the sequence</h2>

<p>Deductible and coinsurance are sequential, not simultaneous. The order matters:</p>

<ol>
    <li><strong>Phase 1 &mdash; Deductible:</strong> You pay 100% of covered costs until your annual deductible is met.</li>
    <li><strong>Phase 2 &mdash; Coinsurance:</strong> After the deductible is met, you pay your coinsurance percentage (e.g., 20%) on each covered service. Insurance pays the rest.</li>
    <li><strong>Phase 3 &mdash; Out-of-pocket max:</strong> Once your total payments (deductible + copays + coinsurance) reach your OOP max, insurance pays 100% for the rest of the year.</li>
</ol>

<p>The most common mistake: patients in Phase 1 see a large bill and assume they have insurance coverage because they have insurance. Coverage does not mean the insurer pays immediately &mdash; you must exhaust your deductible first. Understanding which phase you are in determines how to budget for upcoming care. Track your phase status through your insurer&rsquo;s member portal or on each EOB. See <a href="/guides/out-of-pocket-maximum">our out-of-pocket maximum guide</a> for detail on Phase 3.</p>

<h2 id="common-splits">4. Common coinsurance splits: 80/20, 70/30, 60/40</h2>

<table>
    <thead>
        <tr><th>Plan Coinsurance Split</th><th>You Pay</th><th>Insurance Pays</th><th>Your Cost on $10,000 Service</th><th>Plan Premium Level</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>80/20</strong></td><td>20%</td><td>80%</td><td>$2,000</td><td>Mid to high premium</td></tr>
        <tr><td><strong>70/30</strong></td><td>30%</td><td>70%</td><td>$3,000</td><td>Mid premium</td></tr>
        <tr><td><strong>60/40</strong></td><td>40%</td><td>60%</td><td>$4,000</td><td>Lower premium</td></tr>
        <tr><td><strong>100/0 (after deductible)</strong></td><td>0%</td><td>100%</td><td>$0</td><td>Highest premium (rare)</td></tr>
    </tbody>
</table>

<p>Lower-premium plans typically have higher coinsurance percentages. A 60/40 plan may cost $150/month less in premiums than an 80/20 plan &mdash; but if you need a $20,000 surgery, you pay $8,000 vs. $4,000 in coinsurance. The premium savings ($1,800/year) do not offset a $4,000 difference in a bad year. Run the math before choosing based on premium alone.</p>

<p><strong>ACA metal tier and coinsurance:</strong> The ACA&rsquo;s metal tiers are largely defined by coinsurance and cost-sharing levels (the &ldquo;actuarial value&rdquo; &mdash; how much of total costs the plan covers on average):</p>

<ul>
    <li><strong>Bronze (60% actuarial value):</strong> You pay ~40% of total costs on average &mdash; typical coinsurance 30&ndash;40%</li>
    <li><strong>Silver (70%):</strong> You pay ~30% on average &mdash; typical coinsurance 20&ndash;30%</li>
    <li><strong>Gold (80%):</strong> You pay ~20% on average &mdash; typical coinsurance 10&ndash;20%</li>
    <li><strong>Platinum (90%):</strong> You pay ~10% on average &mdash; low coinsurance, highest premium</li>
</ul>

<h2 id="oon-coinsurance">5. In-network vs. out-of-network coinsurance</h2>

<p>Most plans have different coinsurance rates for in-network and out-of-network providers. The out-of-network rate is typically much higher &mdash; or care is simply not covered:</p>

<table>
    <thead>
        <tr><th>Plan Type</th><th>In-Network Coinsurance (typical)</th><th>Out-of-Network Coinsurance (typical)</th></tr>
    </thead>
    <tbody>
        <tr><td>PPO</td><td>20%</td><td>40&ndash;50% (plus possible balance billing)</td></tr>
        <tr><td>HMO</td><td>20%</td><td>Not covered (except emergencies)</td></tr>
        <tr><td>EPO</td><td>20%</td><td>Not covered (except emergencies)</td></tr>
        <tr><td>POS</td><td>20%</td><td>30&ndash;40%</td></tr>
    </tbody>
</table>

<p>On a PPO plan, going out of network for a $10,000 procedure at 40% coinsurance costs you $4,000 vs. $2,000 in-network &mdash; a $2,000 difference on just one procedure. Additionally, out-of-network providers can balance bill you for the difference between their charge and the insurance allowed amount, a protection you don&rsquo;t have in-network. Always verify network status before receiving care. See <a href="/guides/hmo-ppo-epo-hdhp-plan-types">our plan type comparison</a> for how network types affect your coinsurance exposure.</p>

<h2 id="prescriptions">6. Coinsurance for prescriptions</h2>

<p>Most prescriptions are subject to flat copays rather than coinsurance &mdash; but specialty drugs are often an exception:</p>

<ul>
    <li><strong>Tier 1 (generic drugs):</strong> Typically $5&ndash;$15 flat copay</li>
    <li><strong>Tier 2 (preferred brand):</strong> Typically $30&ndash;$60 flat copay</li>
    <li><strong>Tier 3 (non-preferred brand):</strong> Typically $60&ndash;$100 flat copay</li>
    <li><strong>Tier 4&ndash;5 (specialty drugs):</strong> Often <strong>25&ndash;33% coinsurance</strong> instead of a flat copay. A specialty biologic drug costing $8,000/month at 25% coinsurance = $2,000/month out of pocket before hitting your OOP max.</li>
</ul>

<p>Specialty drug coinsurance is one of the fastest paths to hitting your out-of-pocket maximum. If you take specialty medications, calculate whether your annual specialty drug coinsurance alone will push you toward your OOP max &mdash; if so, plan other care accordingly.</p>

<h2 id="medicare">7. Medicare coinsurance in 2026</h2>

<p>Medicare has its own coinsurance structure, separate from private insurance:</p>

<table>
    <thead>
        <tr><th>Medicare Part</th><th>Coinsurance Details (2026)</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Part A (Hospital)</strong></td>
            <td>Days 1&ndash;60: $0 coinsurance after $1,676 deductible. Days 61&ndash;90: $419/day coinsurance. Days 91+: $838/day (lifetime reserve days).</td>
        </tr>
        <tr>
            <td><strong>Part B (Medical)</strong></td>
            <td>20% coinsurance after $257 annual deductible for most covered services &mdash; with no out-of-pocket maximum. This is why Medigap plans are important for Medicare beneficiaries.</td>
        </tr>
        <tr>
            <td><strong>Part D (Drugs)</strong></td>
            <td>Varies by drug tier and plan. 2026 OOP cap of $2,000 after which coverage is 100%.</td>
        </tr>
    </tbody>
</table>

<p><strong>No OOP max on Original Medicare:</strong> Unlike ACA marketplace plans, Original Medicare Parts A and B have no annual out-of-pocket maximum. If you have a long hospitalization or chronic disease requiring Part B services, your 20% coinsurance exposure is theoretically unlimited. This is the primary reason Medicare beneficiaries purchase Medigap (Medicare Supplement) insurance &mdash; Medigap covers the Part A and Part B coinsurance, effectively capping your exposure.</p>

<h2 id="planning">8. Calculating your maximum coinsurance exposure</h2>

<p>If you have a scheduled procedure, you can calculate your maximum out-of-pocket cost in advance. Here is the formula:</p>

<ol>
    <li><strong>Get the allowed amount.</strong> Call your insurer&rsquo;s pre-authorization line and ask for the allowed amount for the procedure&rsquo;s CPT code at the specific facility. Or use Medicare rates as a rough benchmark &mdash; Medicare typically pays 80&ndash;120% of what commercial insurers pay for common procedures.</li>
    <li><strong>Subtract your remaining deductible.</strong> Check your member portal for your year-to-date deductible accumulation. Subtract from your annual deductible to find what you still owe.</li>
    <li><strong>Apply coinsurance to the remainder.</strong> After your deductible, multiply the remaining allowed amount by your coinsurance percentage.</li>
    <li><strong>Check your remaining OOP max.</strong> Your maximum exposure is capped at your remaining out-of-pocket maximum. If you are close to your OOP max, your actual cost may be much lower than the coinsurance calculation suggests.</li>
</ol>

<p><strong>Example:</strong> $15,000 allowed amount procedure. $800 deductible remaining. 20% coinsurance. $6,000 OOP max, with $4,200 already paid toward it.</p>

<ul>
    <li>You pay $800 deductible first.</li>
    <li>20% of remaining $14,200 = $2,840 coinsurance.</li>
    <li>Total = $3,640.</li>
    <li>But your remaining OOP max is $6,000 &minus; $4,200 = $1,800.</li>
    <li><strong>Your actual cost: $1,800</strong> (capped by OOP max, not the coinsurance formula).</li>
</ul>

<div class="case-study">
    <h3>Case study: Coinsurance math prevents a $2,200 planning error</h3>
    <p><strong>Situation:</strong> Kevin needed knee surgery. His plan had a $2,500 deductible, 20% coinsurance, and $8,500 OOP max. He had already paid $1,200 toward his deductible. The surgeon quoted a $22,000 allowed amount. Kevin assumed he would owe his deductible ($1,300 remaining) plus maybe a small copay.</p>
    <p><strong>The actual math:</strong> $1,300 deductible + 20% of remaining $20,700 = $1,300 + $4,140 = <strong>$5,440</strong>. Kevin had not factored in coinsurance at all and was not financially prepared.</p>
    <p><strong>What he did:</strong> He reviewed his OOP max status ($1,200 paid of $8,500 max), confirmed $7,300 remaining exposure, and moved $5,500 from his savings to his HSA before the procedure to pay with pre-tax dollars. He also <a href="/scan">scanned his post-surgery bill</a> and found two duplicate charges totaling $1,800 that were removed. Final cost: $3,640 after corrections. <strong>Savings from catching the error: $360 (his 20% of $1,800).</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is coinsurance in health insurance?</h3>
        <p>Coinsurance is the percentage of covered medical costs you pay after your deductible is met. With 20% coinsurance, you pay 20% of the allowed amount and insurance pays 80%, until you hit your out-of-pocket maximum.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between coinsurance and a copay?</h3>
        <p>A copay is a flat dollar amount (e.g., $35 per visit). Coinsurance is a percentage of the cost (e.g., 20% of a $5,000 surgery = $1,000). Copays are predictable; coinsurance scales with the cost of the service. Both count toward your out-of-pocket maximum.</p>
    </div>

    <div class="faq-item">
        <h3>Does coinsurance apply before or after the deductible?</h3>
        <p>After. You pay 100% of covered costs until your deductible is met. Then coinsurance applies: you pay your percentage, insurance pays the rest. Both stop once you hit your out-of-pocket maximum.</p>
    </div>

    <div class="faq-item">
        <h3>What does 80/20 coinsurance mean?</h3>
        <p>Your insurance pays 80% of the allowed amount and you pay 20% after your deductible is met. On a $10,000 allowed service, you pay $2,000 and insurance pays $8,000.</p>
    </div>

    <div class="faq-item">
        <h3>When does coinsurance stop?</h3>
        <p>Coinsurance stops when you reach your annual out-of-pocket maximum. After that, insurance pays 100% of covered in-network services for the rest of the calendar year.</p>
    </div>
</div>

<div class="key-takeaway">
    <strong>Paying coinsurance on a bill that seems too high?</strong> Billing errors can inflate the allowed amount you&rsquo;re paying a percentage of &mdash; meaning you overpay coinsurance on a charge that shouldn&rsquo;t exist. <a href="/fight-debt">BillKarma can audit your bill and help you recover overpayments.</a>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Coinsurance Definition and Examples</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: 2026 Medicare Cost-Sharing</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Employer Health Benefits Survey (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">IRS: Publication 969 &mdash; Health Savings Accounts (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Consumer Financial Protection Bureau: Medical Cost-Sharing Survey (2025)</a></li>
</ul>
""",
})
