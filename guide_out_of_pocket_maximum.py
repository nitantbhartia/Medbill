"""Guide: Out-of-Pocket Maximum Explained."""

from guides import register, _embed

register("out-of-pocket-maximum", {
    "title": "Out-of-Pocket Maximum Explained: The Most Important Number in Your Plan",
    "meta_description": "Your out-of-pocket maximum is the most you'll pay in a year for covered in-network care. Learn the 2026 ACA limits, what counts, what doesn't, and how to use it.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is the out-of-pocket maximum for 2026?",
            "a": "Under the ACA, the 2026 out-of-pocket maximum limits are $9,450 for an individual and $18,900 for a family on marketplace and most employer plans. These are federal ceilings — your plan's actual OOP max may be lower, but it cannot be higher for covered in-network services.",
        },
        {
            "q": "What happens after I reach my out-of-pocket maximum?",
            "a": "Once you hit your OOP max, your insurance pays 100% of covered in-network services for the rest of the calendar year. You still owe your monthly premium, and out-of-network charges and non-covered services still cost you money regardless of your OOP max status.",
        },
        {
            "q": "Does my deductible count toward my out-of-pocket maximum?",
            "a": "Yes. Your deductible, copays, and coinsurance for covered in-network services all count toward your out-of-pocket maximum. Your premium does not count.",
        },
        {
            "q": "What doesn't count toward my out-of-pocket maximum?",
            "a": "Monthly premiums, out-of-network charges (on plans with separate OON OOP max or no OON coverage), balance bills from out-of-network providers, and costs for non-covered services do not count toward your in-network OOP maximum.",
        },
        {
            "q": "How does the family out-of-pocket maximum work?",
            "a": "Like deductibles, family OOP maximums can be embedded or aggregate. With an embedded OOP max, each family member has an individual OOP limit (e.g., $9,450), and once any one member hits it, insurance covers 100% for that person. The family OOP max (e.g., $18,900) caps total family spending. With an aggregate OOP max, insurance only kicks in at 100% once the combined family total hits the family OOP max.",
        },
    ],
    "body": f"""
<p class="lead">Your out-of-pocket maximum is the single most important number in your health insurance plan &mdash; yet most people only discover it after a major diagnosis or hospitalization. It is the <strong>absolute most you will pay in a year</strong> for covered in-network services. After you hit it, insurance pays 100% for the rest of the year. In 2026, the ACA caps this at <strong>$9,450 for individuals and $18,900 for families</strong>. But billing errors can push patients past their legitimate maximum &mdash; BillKarma data shows patients who reach their OOP max still face an average of <strong>$1,100 in billing errors</strong> on top of what they actually owe.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-oop-max">What the out-of-pocket maximum actually does</a></li>
        <li><a href="#2026-limits">2026 ACA out-of-pocket maximum limits</a></li>
        <li><a href="#what-counts">What counts toward your OOP max</a></li>
        <li><a href="#what-doesnt-count">What does NOT count toward your OOP max</a></li>
        <li><a href="#family-oop">Embedded vs. aggregate family OOP maximums</a></li>
        <li><a href="#prescriptions">How prescription drugs interact with your OOP max</a></li>
        <li><a href="#planning">How to plan around your OOP max</a></li>
        <li><a href="#tracking">How to track your OOP max progress</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-oop-max">1. What the out-of-pocket maximum actually does</h2>

<p>Your OOP max is a financial ceiling. Once your cumulative cost-sharing payments for the year &mdash; deductible + copays + coinsurance for covered in-network services &mdash; reach this number, your insurance pays 100% of covered in-network costs for the rest of the calendar year.</p>

<p>It protects you from catastrophic medical debt. Without an OOP max, a patient facing $250,000 in cancer treatment at 20% coinsurance would owe $50,000. With a $9,450 OOP max, their exposure is capped at $9,450 regardless of how much care they receive.</p>

<div class="bill-example">
    <div class="bill-header">How the OOP Max Works &mdash; Cancer Treatment Year &mdash; $3,000 Deductible / 20% Coinsurance / $9,450 OOP Max</div>
    <div class="line-item">
        <span>Total covered in-network treatment (allowed amounts)</span>
        <span>$180,000.00</span>
    </div>
    <div class="line-item">
        <span>You pay: deductible</span>
        <span>$3,000.00</span>
    </div>
    <div class="line-item">
        <span>You pay: coinsurance (20% of next $32,250 until OOP max hit)</span>
        <span>$6,450.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays: 80% until OOP max, then 100% of remainder</span>
        <span>$170,550.00</span>
    </div>
    <div class="line-total">
        <span>YOUR TOTAL COST (OOP max)</span>
        <span>$9,450.00</span>
    </div>
</div>

<div class="key-takeaway">
    <strong>The OOP max is your catastrophic cost ceiling.</strong> In a high-cost year &mdash; cancer, surgery, major accident &mdash; this number determines your worst-case financial exposure. Knowing it in advance lets you plan. Not knowing it means surprise bills when you&rsquo;re at your most vulnerable.
</div>

{_embed(mode="cost", cpt="27447", title="Look up procedure costs", subtitle="See what Medicare pays for major procedures &mdash; a useful benchmark for your expected costs.")}

<h2 id="2026-limits">2. 2026 ACA out-of-pocket maximum limits</h2>

<p>The ACA sets annual federal ceilings on OOP maximums for non-grandfathered plans. Your plan&rsquo;s OOP max cannot exceed these limits for covered in-network services:</p>

<table>
    <thead>
        <tr><th>Coverage Type</th><th>2026 ACA OOP Max Limit</th><th>2025 Limit</th><th>Change</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Individual</strong></td><td>$9,450</td><td>$9,200</td><td>+$250</td></tr>
        <tr><td><strong>Family</strong></td><td>$18,900</td><td>$18,400</td><td>+$500</td></tr>
    </tbody>
</table>

<p>These are <strong>ceilings, not targets.</strong> Many plans set their OOP max below the ACA limit. Check your Summary of Benefits and Coverage for your plan&rsquo;s specific number. Out-of-network costs often have a <strong>separate, higher OOP max</strong> &mdash; or no cap at all &mdash; because they fall under different cost-sharing rules.</p>

<p><strong>Medicare note:</strong> The standard Medicare Part D out-of-pocket cap for 2026 is <strong>$2,000</strong> under the Inflation Reduction Act. After $2,000 in out-of-pocket drug costs, Part D covers 100% for the rest of the year. Original Medicare Parts A and B have no unified OOP max without a Medigap supplement.</p>

<h2 id="what-counts">3. What counts toward your OOP max</h2>

<p>All three forms of cost-sharing for covered in-network services accumulate toward your OOP max:</p>

<ul>
    <li><strong>Deductible payments</strong> &mdash; every dollar you pay before insurance starts sharing costs</li>
    <li><strong>Copays</strong> &mdash; flat fees for office visits, urgent care, and most prescriptions (Tier 1&ndash;4)</li>
    <li><strong>Coinsurance</strong> &mdash; your percentage share after the deductible is met</li>
</ul>

<p>Because all three count, you can hit your OOP max faster than you might expect. A patient who pays a $3,000 deductible, $1,500 in copays throughout the year, and $4,950 in coinsurance has hit a $9,450 OOP max &mdash; even though each individual transaction seemed manageable.</p>

<h2 id="what-doesnt-count">4. What does NOT count toward your OOP max</h2>

<table>
    <thead>
        <tr><th>Does Not Count</th><th>Why</th></tr>
    </thead>
    <tbody>
        <tr><td>Monthly premiums</td><td>Premiums are a separate cost of having insurance &mdash; never applied to any cost-sharing accumulator</td></tr>
        <tr><td>Out-of-network charges (in-network OOP max)</td><td>OON costs accrue to a separate OON OOP max or have no cap on some plans</td></tr>
        <tr><td>Balance bills from out-of-network providers</td><td>Balance billing is the difference between a provider&rsquo;s full charge and the insurance-allowed amount</td></tr>
        <tr><td>Non-covered services</td><td>Cosmetic procedures, most weight-loss surgery, many alternative therapies are not covered services</td></tr>
        <tr><td>Costs above plan limits (grandfathered plans)</td><td>Some pre-ACA grandfathered plans have benefit limits that can expose you to costs above their OOP max</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The out-of-network trap:</strong> If you have a PPO and go out of network, those costs usually do NOT count toward your in-network OOP max. They accumulate separately toward a higher OON OOP max &mdash; or on some plans, have no cap at all. Always verify whether a provider is in-network before receiving non-emergency care. See <a href="/guides/hmo-ppo-epo-hdhp-plan-types">our plan type comparison guide</a> for network coverage by plan type.
</div>

<h2 id="family-oop">5. Embedded vs. aggregate family OOP maximums</h2>

<p>If you have a family plan, the OOP max structure determines when insurance kicks in at 100% for individual members:</p>

<p><strong>Embedded OOP max:</strong> Each family member has their own individual OOP limit. Once any single member hits their individual limit, insurance pays 100% for that person. The family OOP max applies to the combined total &mdash; once the family hits it, everyone is covered at 100%.</p>

<p><strong>Aggregate OOP max:</strong> There is only one family OOP max. Insurance does not pay 100% for any individual until the combined family total reaches the family OOP max. This can be costly in a high-cost year for one family member.</p>

<p><strong>ACA rule:</strong> For plan years starting on or after January 1, 2016, ACA-compliant plans cannot require any individual on a family plan to pay more than the individual OOP max in a single year &mdash; even on aggregate family structures. This effectively embeds individual OOP max protection into all ACA-compliant plans.</p>

<h2 id="prescriptions">6. How prescription drugs interact with your OOP max</h2>

<p>For most ACA-compliant plans, prescription drug copays and coinsurance (Tier 1&ndash;4 drugs) <strong>count toward your OOP max</strong>. However, there are exceptions:</p>

<ul>
    <li><strong>Grandfathered plans</strong> may still have separate drug OOP maximums that do not integrate with your medical OOP max.</li>
    <li><strong>Specialty drugs (Tier 5)</strong> sometimes have separate cost-sharing structures, particularly on older plans. Check your plan documents.</li>
    <li><strong>Accumulator adjustment programs (AAPs):</strong> Some insurers exclude manufacturer copay assistance from counting toward your OOP max accumulator. If you use a drug manufacturer coupon, verify whether your plan has this provision &mdash; it can delay when you hit your OOP max.</li>
</ul>

<h2 id="planning">7. How to plan around your OOP max</h2>

<p>Your OOP max is not just a safety net &mdash; it is a planning tool. Here is how to use it strategically:</p>

<ol>
    <li><strong>Front-load care if you know you&rsquo;ll hit your OOP max.</strong> If you have a chronic condition or scheduled surgery and expect to hit your OOP max by mid-year, schedule additional elective care during the same year. After your OOP max is met, that care costs you nothing.</li>
    <li><strong>Schedule high-cost care in January if you hit your OOP max every year.</strong> If you reliably hit your OOP max, scheduling your most expensive care at the start of the year maximizes the months insurance covers 100%.</li>
    <li><strong>Factor in the OOP max when comparing plans.</strong> A plan with a lower premium but higher OOP max may cost you more in a bad year. Calculate worst-case exposure: (monthly premium &times; 12) + OOP max = maximum annual cost.</li>
    <li><strong>Build an HSA to the OOP max amount.</strong> If you have an HDHP, consider saving enough in your HSA to cover your full OOP max. This ensures you pay all cost-sharing with pre-tax dollars.</li>
    <li><strong>Audit your bills before and after hitting OOP max.</strong> Billing errors can push you over your OOP max unnecessarily. <a href="/fight-debt">If you&rsquo;ve been overbilled, BillKarma can help you dispute the charges.</a></li>
</ol>

<div class="case-study">
    <h3>Case study: Strategic scheduling saves $4,100</h3>
    <p><strong>Situation:</strong> James has Type 1 diabetes and reliably hits his $8,700 OOP max every year by August. He needs elective physical therapy for a knee injury (5 sessions at $400 each = $2,000) and a covered dental procedure ($800).</p>
    <p><strong>His choice:</strong> He schedules both in September, after already hitting his OOP max. Both are covered at 100% &mdash; cost to James: $0 instead of $2,800. He also scanned his EOBs and found $1,300 in processing errors that had incorrectly counted OON charges toward his in-network OOP max, catching the error before it inflated future bills.</p>
    <p><strong>Total savings from planning and auditing: $4,100.</strong></p>
</div>

<h2 id="tracking">8. How to track your OOP max progress</h2>

<p>Tracking your OOP max accumulation in real time prevents two common errors: overpaying because you haven&rsquo;t hit it yet, and missing free care because you have.</p>

<ol>
    <li><strong>Member portal:</strong> Log in to your insurer&rsquo;s website or app. Look for &ldquo;Deductibles &amp; Out-of-Pocket&rdquo; or &ldquo;Benefits Summary.&rdquo; Your insurer is required to provide this in real time for ACA-compliant plans.</li>
    <li><strong>Explanation of Benefits (EOB):</strong> Every EOB shows your running year-to-date OOP accumulation. The line typically reads &ldquo;Out-of-pocket maximum applied: $X | Remaining: $Y.&rdquo; See <a href="/guides/explanation-of-benefits-eob">our full guide to reading your EOB</a> for help interpreting each column.</li>
    <li><strong>Call member services:</strong> The number on the back of your insurance card connects you to a representative who can confirm your current accumulator status.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the out-of-pocket maximum for 2026?</h3>
        <p>The ACA 2026 limits are $9,450 for an individual and $18,900 for a family. These are the maximum allowed limits &mdash; your plan may set a lower OOP max. Check your Summary of Benefits and Coverage for your specific number.</p>
    </div>

    <div class="faq-item">
        <h3>What happens after I reach my out-of-pocket maximum?</h3>
        <p>Insurance pays 100% of covered in-network services for the rest of the calendar year. You still owe your monthly premium. Out-of-network charges and non-covered services still cost you out of pocket.</p>
    </div>

    <div class="faq-item">
        <h3>Does my deductible count toward my out-of-pocket maximum?</h3>
        <p>Yes. Your deductible, copays, and coinsurance for covered in-network services all count toward your OOP max. Your premium never counts.</p>
    </div>

    <div class="faq-item">
        <h3>What doesn't count toward my out-of-pocket maximum?</h3>
        <p>Premiums, out-of-network charges, balance bills, and costs for non-covered services do not count toward your in-network OOP maximum. On most plans, OON charges go toward a separate OON OOP max.</p>
    </div>

    <div class="faq-item">
        <h3>How does the family out-of-pocket maximum work?</h3>
        <p>ACA-compliant family plans must not require any individual to pay more than the individual OOP max, even on aggregate family plans. Once the family hits the family OOP max, insurance covers 100% for everyone.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: 2026 Out-of-Pocket Limits</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Out-of-Pocket Maximum/Limit</a></li>
    <li><a href="#" target="_blank" rel="noopener">IRS Revenue Procedure 2025-19: HSA Contribution and HDHP Limits</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Employer Health Benefits Survey (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Inflation Reduction Act: Medicare Part D Out-of-Pocket Cap Summary</a></li>
</ul>
""",
})
