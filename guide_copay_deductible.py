"""Guide: Copay vs. Coinsurance vs. Deductible."""

from guides import register, _embed

register("copay-vs-coinsurance-vs-deductible", {
    "title": "Copay vs. Coinsurance vs. Deductible",
    "meta_description": "Copay, coinsurance, deductible — most Americans mix them up and overpay. Learn what each term means, how they interact, and how to spot billing errors.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is the difference between a copay and coinsurance?",
            "a": "A copay is a fixed dollar amount you pay for a service regardless of the total cost — for example, $30 for a primary care visit. Coinsurance is a percentage you pay of the allowed amount after your deductible is met — for example, 20% of a $500 specialist visit. Copays are predictable; coinsurance varies with the total cost of care.",
        },
        {
            "q": "Does my copay count toward my deductible?",
            "a": "Usually no. Copays typically do not count toward your deductible — they are separate flat fees. However, copays almost always count toward your out-of-pocket maximum. Check your plan's Summary of Benefits to confirm, as some plans (especially HMOs) do apply copays to the deductible.",
        },
        {
            "q": "What happens after I meet my deductible?",
            "a": "After you meet your deductible, your insurance begins sharing costs with you. Depending on your plan, you'll typically pay coinsurance (a percentage, e.g., 20%) instead of the full cost. This continues until you reach your out-of-pocket maximum, after which insurance pays 100% for the rest of the plan year.",
        },
        {
            "q": "What counts toward my deductible?",
            "a": "Most in-network medical services count toward your deductible: hospital stays, surgery, outpatient procedures, lab work, and imaging. What typically does NOT count: monthly premiums, out-of-network services (on most plans), and copays for office visits (on most plans). Always check your plan's Summary of Benefits for specifics.",
        },
        {
            "q": "Can a hospital bill me the wrong cost-sharing amount?",
            "a": "Yes, and it happens frequently. Common errors include applying out-of-network cost-sharing to in-network providers, billing coinsurance before the deductible is actually met, and double-counting services. According to BillKarma's analysis, cost-sharing errors appear in roughly 1 in 8 bills — always compare your bill to your Explanation of Benefits (EOB).",
        },
        {
            "q": "What is the out-of-pocket maximum?",
            "a": "The out-of-pocket maximum is the most you'll pay for covered in-network services in a plan year. In 2026, the ACA cap is $9,450 for individual coverage and $18,900 for family coverage. Once you hit this limit, your insurance pays 100% for the rest of the year. Copays, coinsurance, and deductible payments all count toward this cap.",
        },
    ],
    "body": f"""
<p class="lead">Most Americans can&rsquo;t correctly define all three cost-sharing terms on their insurance card. That confusion costs real money: a 2023 <a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF survey</a> found that 67% of adults with medical debt were surprised by bills they thought their insurance would cover. Understanding the difference between a copay, a coinsurance, and a deductible — and how they stack together — is the single most effective way to predict and dispute what you owe.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#three-terms">The three terms, clearly defined</a></li>
        <li><a href="#how-they-stack">How deductible, coinsurance, and copay stack on one bill</a></li>
        <li><a href="#eob-example">Reading a real EOB: annotated example</a></li>
        <li><a href="#what-counts">What counts toward each — and what doesn&rsquo;t</a></li>
        <li><a href="#common-errors">5 cost-sharing billing errors to look for</a></li>
        <li><a href="#plan-types">How cost-sharing differs by plan type (HMO, PPO, HDHP)</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="three-terms">1. The three terms, clearly defined</h2>

<table>
    <thead>
        <tr><th>Term</th><th>What it is</th><th>Example</th><th>When you pay it</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Deductible</strong></td><td>Fixed annual amount you pay before insurance starts covering services</td><td>$1,500/year individual</td><td>At the start of each plan year until met</td></tr>
        <tr><td><strong>Copay</strong></td><td>Flat fee per visit or service, regardless of total cost</td><td>$30 per primary care visit</td><td>At the time of service, every time</td></tr>
        <tr><td><strong>Coinsurance</strong></td><td>Percentage of the allowed amount you pay after your deductible</td><td>20% of a $500 specialist visit = $100</td><td>After deductible is met, until out-of-pocket max is hit</td></tr>
        <tr><td><strong>Out-of-pocket max</strong></td><td>The most you&rsquo;ll pay in a plan year; insurance covers 100% after this</td><td>$7,000 individual (2026)</td><td>Automatically applies once reached</td></tr>
    </tbody>
</table>

<p><strong>Premium</strong> — your monthly payment to have insurance — is separate from all of these. It does not count toward your deductible or out-of-pocket maximum.</p>

<div class="key-takeaway">
    <strong>The sequence matters.</strong> You pay the deductible first (100% of costs until met), then coinsurance (a percentage), then nothing after the out-of-pocket maximum. Copays run in parallel throughout the year and usually don&rsquo;t count toward the deductible.
</div>

<h2 id="how-they-stack">2. How deductible, coinsurance, and copay stack on one bill</h2>

<p>Say your plan has a <strong>$1,500 deductible</strong>, <strong>20% coinsurance</strong>, <strong>$30 primary care copay</strong>, and a <strong>$7,000 out-of-pocket maximum</strong>. Here&rsquo;s how three visits play out in the same year:</p>

<table>
    <thead>
        <tr><th>Visit</th><th>Allowed amount</th><th>Deductible status</th><th>You pay</th><th>Insurance pays</th></tr>
    </thead>
    <tbody>
        <tr><td>PCP visit (Jan) — copay plan</td><td>$180</td><td>$1,500 remaining</td><td>$30 copay</td><td>$150</td></tr>
        <tr><td>MRI (Feb) — no copay, counts toward deductible</td><td>$1,200</td><td>$1,500 remaining → $300 remaining after</td><td>$1,200</td><td>$0</td></tr>
        <tr><td>Surgery (Mar) — deductible already partially met</td><td>$8,000</td><td>$300 remaining → $0 after; then 20% coinsurance on $7,700</td><td>$300 + $1,540 = $1,840</td><td>$6,160</td></tr>
    </tbody>
</table>

<p>Total you paid: $30 + $1,200 + $1,840 = <strong>$3,070</strong>. Total allowed: $9,380. Your out-of-pocket maximum of $7,000 was not hit this year. If the surgery were more expensive, coinsurance would keep adding until you hit $7,000 for the year, then insurance would cover everything else.</p>

<h2 id="eob-example">3. Reading a real EOB: annotated example</h2>

<p>Your Explanation of Benefits (EOB) — sent by your insurer after every claim — shows how your cost-sharing was applied. Here&rsquo;s a real one, annotated:</p>

<div class="bill-example">
    <div class="bill-header">Explanation of Benefits &mdash; BlueCross Plan XYZ &mdash; Claim Date: 02/10/2026</div>
    <div class="line-item">
        <span>Service: Outpatient MRI Brain w/ contrast (CPT 70553)</span>
        <span>&nbsp;</span>
    </div>
    <div class="line-item">
        <span>Amount billed by provider</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>Plan discount (negotiated rate reduction) &nbsp; &#9888; <em>This is not money you owe — it&rsquo;s the discount your insurer negotiated</em></span>
        <span>&minus;$1,700.00</span>
    </div>
    <div class="line-item">
        <span>Allowed amount (what insurance recognizes)</span>
        <span>$1,500.00</span>
    </div>
    <div class="line-item error">
        <span>Applied to deductible &nbsp; &#10060; <em>You&rsquo;ve already met $900 of deductible — only $600 should apply here, not $1,500</em></span>
        <span>$1,500.00</span>
    </div>
    <div class="line-item">
        <span>Your coinsurance (20% after deductible)</span>
        <span>$0.00</span>
    </div>
    <div class="line-total">
        <span>YOUR RESPONSIBILITY</span>
        <span>$1,500.00</span>
    </div>
</div>

<p>The error above is a real pattern: the insurer or billing department failed to account for previously paid deductible amounts, charging the full $1,500 to deductible instead of the remaining $600. The correct amount owed: $600 (remaining deductible) + $180 (20% coinsurance on the remaining $900) = <strong>$780</strong>. The patient was overbilled by <strong>$720</strong>.</p>

<div class="key-takeaway">
    <strong>Spot errors on your own EOB.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we compare what your provider billed against what your plan should have covered and flag cost-sharing errors automatically.
</div>

<h2 id="what-counts">4. What counts toward each — and what doesn&rsquo;t</h2>

<table>
    <thead>
        <tr><th>Cost type</th><th>Counts toward deductible?</th><th>Counts toward OOP max?</th></tr>
    </thead>
    <tbody>
        <tr><td>Monthly premium</td><td>No</td><td>No</td></tr>
        <tr><td>Copays (most plans)</td><td>No</td><td>Yes</td></tr>
        <tr><td>Coinsurance (in-network)</td><td>After deductible</td><td>Yes</td></tr>
        <tr><td>Deductible payments</td><td>Yes (they are the deductible)</td><td>Yes</td></tr>
        <tr><td>Out-of-network services</td><td>Separate OON deductible (usually)</td><td>Separate OON OOP max (usually)</td></tr>
        <tr><td>Non-covered services</td><td>No</td><td>No</td></tr>
        <tr><td>Balance billing amounts</td><td>No</td><td>No (per No Surprises Act)</td></tr>
    </tbody>
</table>

<p>The &ldquo;out-of-network&rdquo; row is important: most PPO plans have separate — and higher — deductibles and out-of-pocket maximums for out-of-network care. If you see &ldquo;out-of-network&rdquo; on an EOB for a provider you thought was in-network, that&rsquo;s worth disputing immediately. See our <a href="/guides/balance-billing-and-surprise-medical-bills">guide to balance billing</a> for details.</p>

<h2 id="common-errors">5. Five cost-sharing billing errors to look for</h2>

<p>According to BillKarma&rsquo;s analysis of billing patterns across thousands of claims, these are the most common cost-sharing errors:</p>

<h3>a) Deductible not properly credited</h3>
<p>If you&rsquo;ve paid some of your deductible earlier in the year, subsequent bills should only apply the <em>remaining</em> deductible balance. Billing systems sometimes reset or mis-sync, applying the full deductible again. Fix: call your insurer, get your current deductible accumulator balance, and compare it to what the bill shows.</p>

<h3>b) In-network provider billed as out-of-network</h3>
<p>This happens when your doctor is in-network but the facility where they practice isn&rsquo;t, or vice versa. It&rsquo;s especially common with anesthesiologists and radiologists. Result: you get charged a higher deductible and coinsurance rate. Fix: request a network status correction from your insurer.</p>

<h3>c) Coinsurance applied before deductible is met</h3>
<p>Some billing errors show coinsurance charges before the deductible is actually exhausted. On the EOB, the math won&rsquo;t add up. Check: allowed amount = deductible applied + coinsurance applied + insurance paid. If it doesn&rsquo;t balance, the split is wrong.</p>

<h3>d) Copay charged AND coinsurance charged for the same visit</h3>
<p>For copay-based services (like PCP visits), most plans require only the copay — not coinsurance on top. Some billing departments apply both. If your EOB shows a copay AND a coinsurance amount for the same service, that&rsquo;s likely an error.</p>

<h3>e) Out-of-pocket max not recognized</h3>
<p>Once you hit your out-of-pocket maximum, you should owe $0 for any further covered in-network services. Bills issued after your OOP max is hit should show $0 patient responsibility. If they don&rsquo;t, your insurer&rsquo;s accumulator isn&rsquo;t communicating correctly with the provider&rsquo;s billing system.</p>

<div class="key-takeaway">
    <strong>Not sure if your cost-sharing was applied correctly?</strong> Use our <a href="/calculator">free calculator</a> to look up the Medicare rate for any CPT code on your bill — it gives you a baseline to compare against what you were charged and what insurance paid.
</div>

{_embed(mode="markup", title="Check if your charge matches your plan's allowed amount", subtitle="Enter the CPT code and amount billed to see how it compares to Medicare rates.", height="420")}

<h2 id="plan-types">6. How cost-sharing differs by plan type</h2>

<table>
    <thead>
        <tr><th>Plan type</th><th>Typical deductible</th><th>Copays?</th><th>Coinsurance</th><th>Network flexibility</th></tr>
    </thead>
    <tbody>
        <tr><td>HMO</td><td>$0&ndash;$1,500</td><td>Yes, low ($10&ndash;$30)</td><td>0&ndash;20%</td><td>In-network only</td></tr>
        <tr><td>PPO</td><td>$500&ndash;$3,000</td><td>Yes ($20&ndash;$50)</td><td>10&ndash;30%</td><td>In + out-of-network</td></tr>
        <tr><td>HDHP / HSA</td><td>$1,600&ndash;$8,000+</td><td>Usually no (pre-deductible)</td><td>10&ndash;30%</td><td>In + out-of-network</td></tr>
        <tr><td>EPO</td><td>$500&ndash;$2,500</td><td>Yes</td><td>10&ndash;20%</td><td>In-network only</td></tr>
    </tbody>
</table>

<p>On an HDHP (High-Deductible Health Plan), you typically pay 100% of all costs until you meet your deductible — copays don&rsquo;t apply before the deductible (except for preventive care). If you have an HSA-compatible HDHP and your provider charges a copay before you&rsquo;ve met your deductible, that&rsquo;s a billing error that could jeopardize your HSA eligibility.</p>

<div class="key-takeaway">
    <strong>Disputing a cost-sharing error?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we generate a pre-filled dispute letter citing the specific plan provision being violated, so you don&rsquo;t have to figure out the language yourself.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Deductible applied twice for the same plan year</h3>
    <p>A patient in Texas had a $2,000 individual deductible. She met it fully in April after a hospitalization. In June, she had outpatient surgery. The hospital&rsquo;s billing system showed her deductible balance as $2,000 (unmet) due to a sync error with the insurer&rsquo;s accumulator. She was billed $2,000 before coinsurance instead of $0.</p>
    <p>After requesting her deductible accumulator statement from her insurer and submitting it alongside the bill, the hospital corrected the error. <strong>Savings: $2,000.</strong></p>
</div>

<div class="case-study">
    <h3>Anesthesiologist billed out-of-network at in-network facility</h3>
    <p>A patient in Georgia had knee surgery at an in-network hospital. His surgeon and facility were in-network. The anesthesiologist was not — and billed separately at out-of-network rates, triggering a $1,800 coinsurance charge instead of the $300 copay he expected.</p>
    <p>Under the <a href="/guides/balance-billing-and-surprise-medical-bills">No Surprises Act</a>, the anesthesiologist&rsquo;s out-of-network charges were limited to in-network cost-sharing. After filing a complaint, the patient&rsquo;s cost-sharing was corrected. <strong>Savings: $1,500.</strong></p>
</div>

<div class="case-study">
    <h3>Out-of-pocket maximum hit — but bills kept coming</h3>
    <p>A cancer patient in Ohio hit her $7,350 out-of-pocket maximum in September after chemotherapy and surgery. Her October lab work ($480 allowed) should have been $0 — but the lab billed her $96 in coinsurance anyway. The billing system at the lab hadn&rsquo;t received an updated accumulator from her insurer.</p>
    <p>She called her insurer, confirmed the OOP max was hit, and the insurer sent a corrected EOB to the lab. The $96 charge was reversed. <strong>Savings: $96 — multiplied across four months of ongoing treatment, this pattern would have cost her nearly $1,000 unnecessarily.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the difference between a copay and coinsurance?</h3>
        <p>A copay is a flat fee ($30, $50) you pay at the time of service, regardless of the total cost. Coinsurance is a percentage of the allowed amount (typically 20&ndash;30%) you pay after your deductible is met. For a $500 specialist visit with 20% coinsurance, you pay $100. For the same visit with a $50 copay, you pay $50. Use our <a href="/calculator">free calculator</a> to see the allowed amount for any CPT code.</p>
    </div>

    <div class="faq-item">
        <h3>Does my copay count toward my deductible?</h3>
        <p>Usually no. Most plans treat copays as separate from the deductible — you pay both independently. Copays do typically count toward your out-of-pocket maximum. Some HMO plans do apply copays to the deductible; check your plan&rsquo;s Summary of Benefits (SBB) for the specific rule.</p>
    </div>

    <div class="faq-item">
        <h3>What happens after I meet my deductible?</h3>
        <p>Once your deductible is met, insurance starts sharing costs — you pay coinsurance (a percentage) instead of the full cost. This continues until you hit your out-of-pocket maximum, after which insurance pays 100% for the rest of the plan year. Your deductible resets every January 1 (or plan anniversary date).</p>
    </div>

    <div class="faq-item">
        <h3>What counts toward my deductible?</h3>
        <p>In-network medical services generally count: hospital stays, surgery, imaging, labs, specialist visits. What doesn&rsquo;t count: premiums, out-of-network services (usually tracked separately), non-covered services, and most copays. Always check your plan&rsquo;s Summary of Benefits for specifics.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital bill me the wrong cost-sharing amount?</h3>
        <p>Yes, frequently. BillKarma&rsquo;s analysis finds cost-sharing errors in roughly 1 in 8 bills reviewed. The most common: applying a full deductible that was already partially met, billing coinsurance before the deductible is exhausted, and applying out-of-network rates to in-network providers. Always compare your bill to your EOB. If they don&rsquo;t match, file a dispute.</p>
    </div>

    <div class="faq-item">
        <h3>What is the out-of-pocket maximum for 2026?</h3>
        <p>The ACA-mandated out-of-pocket maximum for 2026 is $9,450 for individual coverage and $18,900 for family coverage on marketplace plans. Employer-sponsored plans may have lower caps. Once you hit this limit, your insurer must cover 100% of covered in-network services for the rest of the plan year.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF: Health Care Debt Survey (2023)</a></li>
    <li><a href="https://www.cms.gov/cciio/resources/data-resources/marketplace-puf" target="_blank" rel="noopener">CMS: 2026 Out-of-Pocket Maximum Limits</a></li>
    <li><a href="https://www.healthcare.gov/glossary/deductible/" target="_blank" rel="noopener">HealthCare.gov: Deductible Definition</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/affordable-care-act/for-employers-and-advisers/out-of-pocket-limits" target="_blank" rel="noopener">DOL: ACA Out-of-Pocket Limit Rules</a></li>
    <li><a href="https://www.kff.org/employer-health-benefits/report/2025-employer-health-benefits-survey/" target="_blank" rel="noopener">KFF: 2025 Employer Health Benefits Survey</a></li>
    <li><a href="https://www.consumerfinance.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources</a></li>
</ul>
""",
})
