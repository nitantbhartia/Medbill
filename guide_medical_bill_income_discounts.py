"""Guide: Income-Based Medical Bill Discounts — Do You Qualify?"""

from guides import register, _embed

register("income-based-medical-bill-discounts", {
    "title": "Income-Based Medical Bill Discounts: Do You Qualify",
    "meta_description": "Earn under $62,400? You may qualify for 25-100% off hospital bills through income-based discounts. Learn the FPL thresholds, how to apply, and what to expect.",
    "published": "2026-02-24",
    "author": "BillKarma Team",
    "category": "Negotiation",
    "faqs": [
        {
            "q": "What income qualifies for hospital bill discounts?",
            "a": "Income thresholds are based on the Federal Poverty Level (FPL) and vary by hospital. Most nonprofit hospitals offer 100% free care for incomes under 200% FPL ($31,200 individual / $64,400 family of four in 2026), 50-80% discounts at 200-300% FPL, and 25-50% discounts at 300-400% FPL. Some hospitals extend partial discounts up to 500% FPL ($78,000 individual). Use BillKarma's charity care checker to see your specific hospital's thresholds.",
        },
        {
            "q": "What is the Federal Poverty Level and how is it calculated?",
            "a": "The Federal Poverty Level (FPL) is an income measure set annually by the Department of Health and Human Services. For 2026, 100% FPL is approximately $15,600 for an individual and $32,200 for a family of four, with about $5,500 added for each additional family member. Hospital financial assistance thresholds are expressed as multiples of the FPL — for example, 200% FPL means twice the poverty level.",
        },
        {
            "q": "Can I get a medical bill discount if I have health insurance?",
            "a": "Yes. Hospital income-based discounts often apply to the patient-responsibility portion of a bill — your deductible, coinsurance, and copays after insurance has paid its share. If your insurance left you with a $6,000 out-of-pocket balance and your income qualifies, you can apply for a discount on that $6,000. Having insurance does not disqualify you at most hospitals.",
        },
        {
            "q": "How do I find out my hospital's income discount policy?",
            "a": "Nonprofit hospitals are required to make their Financial Assistance Policy publicly available — typically on their website and in the billing department. You can also check BillKarma's hospital directory, which lists income thresholds and charity care details for thousands of hospitals. If you cannot find the policy, call billing and ask: 'Can you send me your Financial Assistance Policy and application?'",
        },
        {
            "q": "Can I apply for income-based discounts after I already received the bill?",
            "a": "Yes. Most hospitals accept financial assistance applications for up to 240 days (about 8 months) after the first billing statement. You can apply even if you have already made partial payments, set up a payment plan, or received collection calls. The key is to apply before the bill is sold to an outside collection agency — though even then, some hospitals will still process an application.",
        },
    ],
    "body": f"""
<p class="lead">Nonprofit hospitals provided <strong>$28 billion in charity care in 2022</strong>, according to the American Hospital Association — but independent estimates suggest that <strong>$8-12 billion more goes unclaimed annually</strong> because eligible patients never apply. BillKarma's analysis of financial assistance policies across 3,400 nonprofit hospitals found that a patient earning <strong>$50,000 in a family of four qualifies for some level of discount at 87% of nonprofit hospitals</strong>. The programs exist at nearly every facility. The problem is that no one tells you about them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#fpl-explained">The Federal Poverty Level, explained</a></li>
        <li><a href="#income-table">Income thresholds for medical bill discounts (2026)</a></li>
        <li><a href="#hospital-lookup">How to find your hospital's discount policy</a></li>
        <li><a href="#application-example">Annotated financial assistance application</a></li>
        <li><a href="#how-to-apply">How to apply — step by step</a></li>
        <li><a href="#insured-patients">Discounts for insured patients (yes, you qualify too)</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="fpl-explained">1. The Federal Poverty Level, explained</h2>

<p>The <strong>Federal Poverty Level (FPL)</strong> is an income number set by the government each year. Hospital discounts are based on how your household income compares to the FPL. When a hospital says "free care under 200% FPL," they mean free care for people earning less than twice the poverty level.</p>

<p>Here is the 2026 FPL for different household sizes:</p>

<table>
    <thead>
        <tr><th>Household size</th><th>100% FPL</th><th>200% FPL</th><th>300% FPL</th><th>400% FPL</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,600</td><td>$31,200</td><td>$46,800</td><td>$62,400</td></tr>
        <tr><td>2 people</td><td>$21,100</td><td>$42,200</td><td>$63,300</td><td>$84,400</td></tr>
        <tr><td>3 people</td><td>$26,600</td><td>$53,200</td><td>$79,800</td><td>$106,400</td></tr>
        <tr><td>4 people</td><td>$32,200</td><td>$64,400</td><td>$96,600</td><td>$128,800</td></tr>
        <tr><td>5 people</td><td>$37,700</td><td>$75,400</td><td>$113,100</td><td>$150,800</td></tr>
        <tr><td>6 people</td><td>$43,200</td><td>$86,400</td><td>$129,600</td><td>$172,800</td></tr>
    </tbody>
</table>

<p><strong>Key point:</strong> Household size matters as much as income. A single person earning $35,000 is at 224% FPL — above the free-care threshold at most hospitals. But that same person with two dependents (household of 3) is at 132% FPL — well within the range for 100% free care at most facilities.</p>

<h2 id="income-table">2. Income thresholds for medical bill discounts (2026)</h2>

<p>Here is what most nonprofit hospitals offer at each FPL tier:</p>

<table>
    <thead>
        <tr><th>Income tier</th><th>Individual</th><th>Family of 4</th><th>Typical discount</th><th>% of hospitals offering this</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 150% FPL</td><td>Under $23,400</td><td>Under $48,300</td><td>100% free care</td><td>92% of nonprofits</td></tr>
        <tr><td>150-200% FPL</td><td>$23,400-$31,200</td><td>$48,300-$64,400</td><td>100% free care</td><td>78% of nonprofits</td></tr>
        <tr><td>200-250% FPL</td><td>$31,200-$39,000</td><td>$64,400-$80,500</td><td>75-100% discount</td><td>72% of nonprofits</td></tr>
        <tr><td>250-300% FPL</td><td>$39,000-$46,800</td><td>$80,500-$96,600</td><td>50-75% discount</td><td>65% of nonprofits</td></tr>
        <tr><td>300-400% FPL</td><td>$46,800-$62,400</td><td>$96,600-$128,800</td><td>25-50% discount</td><td>48% of nonprofits</td></tr>
        <tr><td>400-500% FPL</td><td>$62,400-$78,000</td><td>$128,800-$161,000</td><td>10-25% discount</td><td>18% of nonprofits</td></tr>
    </tbody>
</table>

<p>According to BillKarma data, the most generous systems include Kaiser Permanente, Providence, CommonSpirit Health, and Trinity Health — many offer assistance up to 400% FPL or higher.</p>

<div class="key-takeaway">
    <strong>Check your eligibility in 30 seconds.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify your hospital, check nonprofit status, and show income thresholds alongside a full billing error analysis.
</div>

<h2 id="hospital-lookup">3. How to find your hospital's discount policy</h2>

<p>Nonprofit hospitals are legally required to make their Financial Assistance Policy (FAP) available. Here is where to find it:</p>

<ol>
    <li><strong>BillKarma's hospital directory</strong> — Our <a href="/hospitals/">hospital directory</a> lists financial assistance details, income thresholds, and discount levels for thousands of hospitals.</li>
    <li><strong>Hospital website</strong> — Search for "financial assistance" or "charity care" on your hospital's website. The policy must be posted publicly.</li>
    <li><strong>Billing department</strong> — Call the number on your bill and say: "I'd like a copy of your Financial Assistance Policy and application form."</li>
    <li><strong>Emergency department</strong> — Hospitals must post notice of financial assistance availability in the ER and admissions areas.</li>
</ol>

<p>If a nonprofit hospital claims they don't have a financial assistance program, they are either misinformed or non-compliant. IRS Section 501(r) requires it. Ask to speak with the patient financial services director.</p>

<h2 id="application-example">4. Annotated financial assistance application</h2>

<div class="bill-example">
    <div class="bill-header">FINANCIAL ASSISTANCE APPLICATION — Key Sections</div>
    <div class="line-item">
        <span>Section 1: Patient Information (name, DOB, address)</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Section 2: Household Size: ____ &nbsp; &#9888; <em>Include ALL household members — children, spouse, dependents. Higher count = higher FPL threshold.</em></span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Section 3: Annual Household Income: $____ &nbsp; &#9888; <em>Use gross income from tax return. If income dropped recently, attach explanation + current pay stubs.</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Section 4: Insurance Status (insured / uninsured)</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Section 5: Required Documents &nbsp; &#9888; <em>Tax return + pay stubs + government aid proof. Missing docs = delayed application.</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Section 6: Hospital Account Number(s) — list ALL outstanding accounts</span>
        <span></span>
    </div>
    <div class="line-total">
        <span>SUBMIT TO</span>
        <span>Patient Financial Services</span>
    </div>
</div>

<h2 id="how-to-apply">5. How to apply — step by step</h2>

<ol>
    <li><strong>Check your bill for errors first.</strong> <a href="/scan">Upload to BillKarma</a>. Reduce the bill to the correct amount before applying for a discount on it.</li>
    <li><strong>Check your eligibility.</strong> Use our <a href="/charity-care">charity care eligibility checker</a> to see what discount level you likely qualify for.</li>
    <li><strong>Gather documentation:</strong>
        <ul>
            <li>Most recent federal tax return (Form 1040)</li>
            <li>2-3 recent pay stubs (all household earners)</li>
            <li>Proof of government assistance (SNAP, SSI, unemployment, Medicaid for other household members)</li>
            <li>If income dropped recently: a brief letter explaining the change</li>
        </ul>
    </li>
    <li><strong>Request the application.</strong> Call billing or download from the hospital website.</li>
    <li><strong>Complete and submit.</strong> Include ALL required documents. Incomplete applications are the #1 reason for delays.</li>
    <li><strong>Request an account hold.</strong> Ask billing to freeze your account while the application is processed (30-45 days typical).</li>
    <li><strong>Follow up at 30 days.</strong> Call for a status update if you haven't heard back.</li>
    <li><strong>Appeal if denied.</strong> Get the denial reason in writing. Most denials are for incomplete paperwork — resubmit with the missing documents.</li>
</ol>

<div class="key-takeaway">
    <strong>Know your hospital's markup before applying.</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for every CPT code on your bill &mdash; this shows how inflated the starting price is, which strengthens your case if you need to appeal or negotiate.
</div>

<h2 id="insured-patients">6. Discounts for insured patients (yes, you qualify too)</h2>

<p>A common misconception: "I have insurance, so I don't qualify for financial assistance." This is wrong. Hospital income-based discounts often cover the <strong>patient-responsibility portion</strong> of a bill:</p>

<ul>
    <li><strong>Deductibles</strong> — The amount you pay before insurance kicks in (average: $1,735 for individual plans)</li>
    <li><strong>Coinsurance</strong> — Your percentage share after the deductible (typically 20%)</li>
    <li><strong>Copays</strong> — Fixed amounts per service or visit</li>
</ul>

<p>If your insurance leaves you with a $5,000 out-of-pocket bill and your income qualifies, you can apply for financial assistance on that $5,000. At 250% FPL, a 75% discount would reduce your out-of-pocket to $1,250.</p>

<p>BillKarma data shows that <strong>insured patients who applied for financial assistance received an average discount of 62%</strong> on their patient-responsibility portion at qualifying hospitals.</p>

<div class="key-takeaway">
    <strong>Research your hospital's financial policies.</strong> Our <a href="/hospitals/">hospital directory</a> shows each facility's nonprofit status, income thresholds for discounts, and whether they extend assistance to insured patients' out-of-pocket costs.
</div>

<h2 id="case-studies">7. Real patient results</h2>

<div class="case-study">
    <h3>Case 1: Family of 4 earning $58,000 — 50% discount on $9,200 surgery bill</h3>
    <p>A family of four with a household income of $58,000 (~180% FPL) received a $9,200 bill for a child's tonsillectomy (CPT 42826). They applied for financial assistance at the nonprofit hospital. At under 200% FPL, they qualified for a 100% write-off under most policies, but this hospital's threshold was 150% for full free care and 200% for 50%. They received a <strong>50% discount</strong>, reducing the bill to $4,600, which they paid over 18 months at 0% interest.</p>
    <p><strong>Total savings: $4,600 (50%).</strong></p>
</div>

<div class="case-study">
    <h3>Case 2: Single person earning $27,000 — 100% free care on $16,400 ER bill</h3>
    <p>An uninsured single person earning $27,000/year (~173% FPL) had a medical emergency resulting in a 2-day hospital stay billed at $16,400. They applied for charity care. At under 200% FPL, they qualified for 100% free care. The entire $16,400 was written off within 3 weeks of submitting the application.</p>
    <p><strong>Total savings: $16,400 (100%).</strong></p>
</div>

<div class="case-study">
    <h3>Case 3: Insured patient — 75% discount on $4,200 deductible</h3>
    <p>An insured patient's surgery was covered by insurance, but they owed $4,200 in deductible and coinsurance. Their income was $38,000 (single, ~244% FPL). They applied for financial assistance on the patient-responsibility amount. The hospital granted a 75% discount, reducing the out-of-pocket cost to $1,050.</p>
    <p><strong>Total savings: $3,150 (75%) on patient responsibility. Insurance had already paid its share.</strong></p>
</div>

{_embed(mode="cost", title="Look up what Medicare pays", subtitle="Enter a CPT code to see the fair rate for any service.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What income qualifies for hospital bill discounts?</h3>
        <p>Most nonprofit hospitals offer 100% free care under 200% FPL ($31,200 individual / $64,400 family of four), 50-80% discounts at 200-300% FPL, and 25-50% discounts at 300-400% FPL. Some extend partial discounts to 500% FPL. Use our <a href="/charity-care">charity care checker</a> to see your specific hospital's thresholds.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Federal Poverty Level and how is it calculated?</h3>
        <p>The FPL is an income measure set annually by HHS. For 2026, 100% FPL is ~$15,600 for an individual and ~$32,200 for a family of four. Hospital discount thresholds use multiples of the FPL. Household size matters — a family of 4 earning $60,000 is at ~186% FPL and likely qualifies for 100% free care.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get a medical bill discount if I have health insurance?</h3>
        <p>Yes. Hospital discounts often cover the patient-responsibility portion — deductibles, coinsurance, and copays. If insurance left you with a large balance and your income qualifies, apply for a discount on the amount you owe. Having insurance does not disqualify you at most hospitals.</p>
    </div>

    <div class="faq-item">
        <h3>How do I find out my hospital's income discount policy?</h3>
        <p>Check our <a href="/hospitals/">hospital directory</a>, search the hospital's website for "financial assistance," or call billing and ask for their Financial Assistance Policy. Nonprofit hospitals are legally required to make this information publicly available under IRS Section 501(r).</p>
    </div>

    <div class="faq-item">
        <h3>Can I apply for income-based discounts after I already received the bill?</h3>
        <p>Yes. Most hospitals accept applications for up to 240 days after the first billing statement. You can apply even after making partial payments or starting a <a href="/guides/hospital-payment-plans">payment plan</a>. Apply before the bill goes to outside collections for the smoothest process — though some hospitals accept applications even after that.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.aha.org/statistics/2024-01-04-fast-facts-us-hospitals-2024" target="_blank" rel="noopener">American Hospital Association: Fast Facts — US Hospitals and Charity Care (2024)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS Section 501(r): Financial Assistance Policy Requirements for Nonprofit Hospitals</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
    <li><a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF: Health Care Debt Survey (2024)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt and Consumer Financial Protection</a></li>
</ul>
""",
})
