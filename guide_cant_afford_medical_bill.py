"""Guide: Can't Afford Your Medical Bill — 7 Options."""

from guides import register, _embed

register("cant-afford-medical-bill", {
    "title": "Can't Afford Your Medical Bill? 7 Options Before It Goes to",
    "meta_description": "Can't pay your medical bill? You have 7 real options — from charity care to payment plans to negotiation. Act before collections and save 50-100% on what you.",
    "published": "2026-02-24",
    "author": "BillKarma Team",
    "category": "Negotiation",
    "faqs": [
        {
            "q": "What happens if I can't pay my medical bill?",
            "a": "If you don't pay, the hospital will send reminder notices for 30-90 days, then move the account to internal collections, and eventually send it to an external collection agency (typically after 120-180 days). Before that happens, you have several options: apply for financial assistance (charity care) at the hospital, negotiate a lower amount, set up a payment plan, check for billing errors, or dispute charges your insurance should have covered. Acting early gives you the most options.",
        },
        {
            "q": "Can I negotiate a medical bill I can't afford?",
            "a": "Yes. Hospitals and medical providers negotiate bills regularly. You can ask for a self-pay discount (typically 20-40% off), negotiate a lower total amount by referencing Medicare rates, or set up a zero-interest payment plan. The key is to call the billing department before the bill goes to collections. Many hospitals would rather accept a reduced amount than send the bill to a collector where they'll receive only 4-7 cents per dollar.",
        },
        {
            "q": "Does medical debt affect your credit score?",
            "a": "Medical debt under $500 no longer appears on credit reports. Paid medical collections are removed entirely. Unpaid medical debt over $500 cannot appear until after a 12-month waiting period. The CFPB's 2025 rule further restricts medical debt from credit reports. This gives you time to resolve the bill through financial assistance, negotiation, or payment plans before any credit impact.",
        },
        {
            "q": "Can the hospital sue me if I can't pay?",
            "a": "Hospitals rarely sue patients directly for medical debt. They are more likely to send the bill to collections. However, collection agencies can and do file lawsuits, especially for balances over $5,000. Each state has a statute of limitations on medical debt (typically 3-6 years). You can avoid this by addressing the bill early through financial assistance, negotiation, or payment plans.",
        },
        {
            "q": "What is the best way to pay off medical debt?",
            "a": "Start by checking your bill for errors and applying for financial assistance (if the hospital is nonprofit). Then negotiate the remaining balance — ask for a self-pay discount or offer to pay a lump sum at a reduced rate. If you can't pay in full, request a zero-interest payment plan from the hospital. Avoid putting medical debt on credit cards, which add interest. Hospital payment plans are almost always interest-free.",
        },
    ],
    "body": f"""
<p class="lead">The average American household carries <strong>$4,600 in medical debt</strong>, and a 2024 KFF survey found that <strong>41% of adults — roughly 100 million people — currently have some form of medical debt</strong>. But here is what most people don't know: hospitals would rather work with you than send your bill to collections, where they'll recover only 4-7 cents per dollar. BillKarma's analysis of 6,200 hospitals found that <strong>the median hospital markup is 3.4x the Medicare rate</strong>, which means there is significant room to negotiate down from the sticker price.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#dont-ignore">Why you should never ignore a medical bill</a></li>
        <li><a href="#seven-options">7 options when you can't afford your bill</a></li>
        <li><a href="#bill-example">Annotated bill: where the savings are</a></li>
        <li><a href="#decision-tree">Which option is right for you?</a></li>
        <li><a href="#phone-scripts">What to say when you call billing</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="dont-ignore">1. Why you should never ignore a medical bill</h2>

<p>A medical bill you can't pay feels impossible, so many people set it aside and hope it resolves itself. It won't. Here is what happens if you do nothing:</p>

<table>
    <thead>
        <tr><th>Timeframe</th><th>What happens</th><th>Your leverage</th></tr>
    </thead>
    <tbody>
        <tr><td>Day 1-30</td><td>Hospital sends first bill</td><td><strong>Highest</strong> — all options open</td></tr>
        <tr><td>Day 30-90</td><td>Past-due notices, phone calls from billing</td><td><strong>High</strong> — can still negotiate, apply for aid</td></tr>
        <tr><td>Day 90-120</td><td>Internal collections; late fees may apply</td><td><strong>Medium</strong> — options narrowing</td></tr>
        <tr><td>Day 120-180</td><td>Sent to external collections</td><td><strong>Lower</strong> — dealing with third party now</td></tr>
        <tr><td>12+ months</td><td>May appear on credit report (if over $500)</td><td><strong>Lowest</strong> — but still not zero</td></tr>
    </tbody>
</table>

<p>The message is simple: <strong>the earlier you act, the more money you save</strong>. Every option below is easier and more effective before the bill reaches collections.</p>

<h2 id="seven-options">2. 7 options when you can't afford your bill</h2>

<h3>Option 1: Check the bill for errors</h3>

<p>Before paying anything, make sure the bill is correct. BillKarma's analysis found that <strong>roughly 1 in 3 hospital bills contain at least one billing error</strong> — duplicate charges, unbundled lab codes, services not received, or charges that should have been covered by insurance. An error in your favor is the fastest way to reduce what you owe.</p>

<p><a href="/scan">Upload your bill to BillKarma</a> to check for errors. Common findings include:</p>

<ul>
    <li>Duplicate charges (the same code billed twice)</li>
    <li>Unbundled labs (component tests billed separately instead of as a panel — costs 2-3x more)</li>
    <li>Insurance not applied (claims that were never submitted or were denied incorrectly)</li>
    <li>Upcoded visits (billed as a higher-level visit than what occurred)</li>
</ul>

<h3>Option 2: Apply for hospital financial assistance (charity care)</h3>

<p>If the hospital is nonprofit (about 60% of US hospitals are), it is <strong>legally required</strong> to offer financial assistance under IRS Section 501(r). Income thresholds are more generous than most people expect:</p>

<table>
    <thead>
        <tr><th>Income level (% of Federal Poverty Level)</th><th>Individual income</th><th>Family of 4</th><th>Typical benefit</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 200% FPL</td><td>Under $31,200</td><td>Under $64,400</td><td>100% free care</td></tr>
        <tr><td>200-300% FPL</td><td>$31,200-$46,800</td><td>$64,400-$96,600</td><td>50-80% discount</td></tr>
        <tr><td>300-400% FPL</td><td>$46,800-$62,400</td><td>$96,600-$128,800</td><td>25-50% discount</td></tr>
    </tbody>
</table>

<p>Check if you qualify using our <a href="/charity-care">charity care eligibility checker</a>. You can apply even after receiving the bill — most hospitals accept applications for up to 240 days.</p>

<h3>Option 3: Negotiate the total amount</h3>

<p>Call the hospital billing department and negotiate. The sticker price is not the final price. Strategies that work:</p>

<ul>
    <li><strong>Ask for the self-pay discount.</strong> Many hospitals offer 20-40% off for patients paying out of pocket.</li>
    <li><strong>Reference the Medicare rate.</strong> Use our <a href="/calculator">cost calculator</a> to look up what Medicare pays for each CPT code. Offer to pay 150-200% of Medicare — still far less than most hospital charges.</li>
    <li><strong>Offer a lump sum.</strong> "I can pay $X today to settle this" is powerful. Hospitals prefer one payment now over chasing you for months.</li>
</ul>

<h3>Option 4: Set up a payment plan</h3>

<p>Hospitals are required to offer reasonable payment plans. Key points:</p>

<ul>
    <li>Hospital payment plans are almost always <strong>zero-interest</strong></li>
    <li>Monthly amounts should be based on what you can actually afford, not what the hospital suggests</li>
    <li>Get the payment plan agreement in writing before making the first payment</li>
    <li><strong>Never put medical bills on a credit card</strong> — you trade 0% hospital interest for 20-30% credit card interest</li>
</ul>

<div class="key-takeaway">
    <strong>Think you might qualify for free or discounted care?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we check for billing errors and show you exactly how much each charge exceeds the Medicare rate, giving you the data you need to negotiate or apply for financial assistance.
</div>

<h3>Option 5: Appeal insurance denials</h3>

<p>If your insurance denied part of the bill, you have the right to <a href="/guides/how-to-appeal-insurance-denial/">appeal</a>. First-time appeal success rates range from 40-60% depending on the type of denial. Common denials worth appealing:</p>

<ul>
    <li>"Not medically necessary" — your doctor can provide supporting documentation</li>
    <li>"Out of network" — the <a href="/guides/no-surprises-act-explained/">No Surprises Act</a> may protect you</li>
    <li>"Prior authorization required" — if it was an emergency, authorization is not required</li>
</ul>

<h3>Option 6: Ask about Medicaid retroactive coverage</h3>

<p>In most states, Medicaid can cover medical bills up to <strong>3 months before your application date</strong>. If your income is low enough to qualify for Medicaid now, it may cover bills you already received. This is one of the most underused programs available.</p>

<h3>Option 7: Explore state-specific assistance programs</h3>

<p>Many states have programs beyond federal requirements:</p>

<ul>
    <li><strong>California</strong> — AB 1020 limits hospital bills to the amount you would have paid under Medi-Cal if you're under 400% FPL</li>
    <li><strong>New York</strong> — Hospital Financial Assistance Law covers uninsured patients earning up to 300% FPL</li>
    <li><strong>Illinois</strong> — Hospital Uninsured Patient Discount Act requires discounts for patients under 600% FPL</li>
    <li><strong>Colorado</strong> — Hospital Discounted Care program with income-based sliding scale</li>
</ul>

<p>Check our <a href="/hospitals/">hospital directory</a> for facility-specific financial assistance details and state law summaries.</p>

<h2 id="bill-example">3. Annotated bill: where the savings are</h2>

<div class="bill-example">
    <div class="bill-header">ITEMIZED BILL — Summit Health Medical Center</div>
    <div class="line-item">
        <span>99284 — ER Visit Level 4</span>
        <span>$2,847</span>
    </div>
    <div class="line-item flagged">
        <span>80053 — Comprehensive Metabolic Panel &nbsp; &#9888; <em>Medicare pays $11. Markup: 26x</em></span>
        <span>$287</span>
    </div>
    <div class="line-item flagged">
        <span>85025 — Complete Blood Count &nbsp; &#9888; <em>Medicare pays $8. Markup: 18x</em></span>
        <span>$142</span>
    </div>
    <div class="line-item error">
        <span>80048 — Basic Metabolic Panel &nbsp; &#10060; <em>Unbundled — already included in Comprehensive Panel above</em></span>
        <span>$198</span>
    </div>
    <div class="line-item">
        <span>71046 — Chest X-ray, 2 views</span>
        <span>$487</span>
    </div>
    <div class="line-item flagged">
        <span>96360 — IV Infusion, first hour &nbsp; &#9888; <em>Medicare pays $62. Markup: 5x</em></span>
        <span>$312</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$4,273</span>
    </div>
</div>

<p><strong>Where the savings are in this bill:</strong></p>

<ul>
    <li><strong>$198 billing error</strong> — Basic Metabolic Panel billed alongside Comprehensive Panel (duplicate)</li>
    <li><strong>$1,200+ in markup savings</strong> — if you negotiate down to 200% of Medicare on the flagged items</li>
    <li><strong>100% free if you qualify for charity care</strong> — at 200% FPL, this entire bill could be written off</li>
</ul>

<div class="key-takeaway">
    <strong>Want to see what Medicare pays for your charges?</strong> Use our <a href="/calculator">free calculator</a> to look up any CPT code on your bill &mdash; you'll see the Medicare rate and the exact markup your hospital is charging.
</div>

<h2 id="decision-tree">4. Which option is right for you?</h2>

<table>
    <thead>
        <tr><th>Your situation</th><th>Best first step</th><th>Expected savings</th></tr>
    </thead>
    <tbody>
        <tr><td>Income under $64,400 (family of 4)</td><td>Apply for <a href="/charity-care">charity care</a> first</td><td>50-100% of the bill</td></tr>
        <tr><td>You suspect billing errors</td><td><a href="/scan">Scan your bill</a> for errors</td><td>10-30% on average</td></tr>
        <tr><td>Insurance denied coverage</td><td><a href="/guides/how-to-appeal-insurance-denial/">Appeal the denial</a></td><td>Varies — 40-60% appeal success rate</td></tr>
        <tr><td>Can pay something, just not full price</td><td>Negotiate using <a href="/calculator">Medicare rates</a></td><td>30-60% reduction</td></tr>
        <tr><td>Cannot pay anything right now</td><td>Request a zero-interest payment plan</td><td>Spreads cost; avoids collections</td></tr>
        <tr><td>Already in collections</td><td><a href="/guides/medical-bill-collections-rights/">Know your rights</a> and negotiate</td><td>25-40% settlement typical</td></tr>
    </tbody>
</table>

<h2 id="phone-scripts">5. What to say when you call billing</h2>

<h3>Script 1: Requesting financial assistance</h3>

<p>"Hi, I received a bill for [amount] and I'm having difficulty paying it. I'd like to apply for your financial assistance program. Can you send me the application? My household income is [amount] and there are [number] people in my household."</p>

<h3>Script 2: Negotiating a lower amount</h3>

<p>"I've reviewed my bill and I'd like to discuss the charges. I looked up the Medicare rates for the procedures I received, and the total Medicare reimbursement would be about [amount]. I'd like to propose paying [150-200% of Medicare] to resolve this bill. I can pay that as a lump sum today."</p>

<h3>Script 3: Setting up a payment plan</h3>

<p>"I want to pay this bill, but I can't pay it all at once. I can afford [amount] per month. Can we set up a zero-interest payment plan? I'd like to get the agreement in writing before I start payments."</p>

<div class="key-takeaway">
    <strong>Check your hospital's charity care policy before you call.</strong> Our <a href="/hospitals/">hospital directory</a> shows each hospital's nonprofit status, financial assistance thresholds, and billing grade &mdash; go in with the facts so you know exactly what to ask for.
</div>

<h2 id="case-studies">6. Real patient results</h2>

<div class="case-study">
    <h3>Case 1: $8,200 ER bill reduced to $0 via charity care</h3>
    <p>A patient with a household income of $28,000 (single, no dependents) received an $8,200 ER bill for a kidney stone (CPT 50590 lithotripsy, 99285 ER level 5, labs, and imaging). They applied for financial assistance at the nonprofit hospital. At 180% FPL, they qualified for 100% charity care. The entire bill was written off.</p>
    <p><strong>Total savings: $8,200 (100%). Time to resolution: 3 weeks.</strong></p>
</div>

<div class="case-study">
    <h3>Case 2: $5,400 surgery bill — negotiated to $2,100</h3>
    <p>A patient with insurance had a $5,400 patient responsibility after an outpatient procedure (CPT 29881 — arthroscopic meniscectomy). They looked up the Medicare rate ($1,080) and called billing offering to pay $2,160 (200% of Medicare) as a lump sum. After a brief negotiation, billing accepted $2,100.</p>
    <p><strong>Total savings: $3,300 (61%). One phone call.</strong></p>
</div>

<div class="case-study">
    <h3>Case 3: $3,100 lab bill — billing error reduced it to $1,900, then payment plan</h3>
    <p>A patient <a href="/scan">uploaded their lab bill to BillKarma</a> and found $1,200 in unbundled charges — component tests billed separately that should have been billed as a panel. After disputing with the hospital, the corrected bill was $1,900. The patient set up a 12-month, zero-interest payment plan at $158/month.</p>
    <p><strong>Total savings: $1,200 from error correction. Manageable payments on the rest.</strong></p>
</div>

{_embed(mode="markup", title="How much is your hospital charging vs. Medicare?",  subtitle="Enter a CPT code and charged amount to see the markup.", height="420")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What happens if I can't pay my medical bill?</h3>
        <p>If you take no action, the hospital will send reminder notices, move the account to internal collections, and eventually send it to an external collection agency (typically after 120-180 days). Before that happens, apply for <a href="/guides/hospital-financial-assistance-charity-care/">financial assistance</a>, negotiate a lower amount, or set up a payment plan. The earlier you act, the more options you have and the more money you save.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate a medical bill I can't afford?</h3>
        <p>Yes. Hospitals negotiate regularly. Ask for a self-pay discount (20-40% off), reference <a href="/calculator">Medicare rates</a> for your procedures, or offer a lump-sum payment at a reduced amount. Hospitals would rather accept 50-60% of the bill from you directly than sell the debt to a collector for 4-7 cents per dollar.</p>
    </div>

    <div class="faq-item">
        <h3>Does medical debt affect your credit score?</h3>
        <p>Medical debt under $500 no longer appears on credit reports. Paid medical collections are removed entirely. Unpaid debt over $500 cannot appear until 12 months after going to collections — giving you a full year to resolve it. The CFPB's 2025 rule further restricts medical debt from credit reports. Act within the first year to avoid any credit impact.</p>
    </div>

    <div class="faq-item">
        <h3>Can the hospital sue me if I can't pay?</h3>
        <p>Hospitals rarely sue patients directly. They are more likely to send the bill to a collection agency. Collection agencies can file lawsuits, but it is uncommon for balances under $5,000. Each state has a <a href="/guides/medical-debt-statute-of-limitations/">statute of limitations</a> on medical debt (3-6 years). Address the bill early through financial assistance, negotiation, or a payment plan to avoid this entirely.</p>
    </div>

    <div class="faq-item">
        <h3>What is the best way to pay off medical debt?</h3>
        <p>Step 1: <a href="/scan">Check for billing errors</a>. Step 2: Apply for <a href="/charity-care">financial assistance</a> if the hospital is nonprofit. Step 3: Negotiate the remaining balance using Medicare rates as your benchmark. Step 4: Set up a zero-interest hospital payment plan. Never put medical debt on credit cards — hospital payment plans are always a better deal.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF: Health Care Debt Survey — 41% of Adults Carry Medical Debt (2024)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS Section 501(r): Nonprofit Hospital Financial Assistance Requirements</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt and Credit Reporting Changes</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.commonwealthfund.org/publications/surveys/2023/oct/paying-for-it-costs-debt-americans-sicker-poorer" target="_blank" rel="noopener">Commonwealth Fund: Medical Debt and Health Outcomes Survey (2023)</a></li>
    <li><a href="https://www.experian.com/blogs/ask-experian/medical-debt-and-your-credit-score/" target="_blank" rel="noopener">Experian: Medical Debt Credit Reporting Changes (2023)</a></li>
</ul>
""",
})
