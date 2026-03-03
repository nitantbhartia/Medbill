"""Guide: How to Negotiate Medical Costs Before Your Procedure."""

from guides import register, _embed

_calc_embed = _embed(mode="cost", title="Look up Medicare rates for your procedure", subtitle="Enter your CPT code to see the Medicare benchmark &mdash; your strongest negotiation tool.", height="400")

register("negotiate-medical-costs-before-procedure", {
    "title": "How to Negotiate Medical Costs Before Your Procedure and Save 30\u201370%",
    "meta_description": "You have more negotiating power BEFORE a procedure than after. Learn exactly how to get a lower price from hospitals, surgeons, and imaging centers before treatment.",
    "published": "2026-03-03",
    "author": "BillKarma Team",
    "category": "Medical Bills",
    "faqs": [
        {
            "q": "Can I negotiate medical costs before a procedure?",
            "a": "Yes, and you should. You have far more leverage before a procedure than after. Before treatment, the provider wants your business and will compete on price. After treatment, you owe the money and have no leverage. Studies show patients who negotiate before a procedure save 30-70% compared to those who pay without negotiating. The key tools: Good Faith Estimates, price transparency data, Medicare rate benchmarks, and competing quotes from other facilities.",
        },
        {
            "q": "How do I get a Good Faith Estimate?",
            "a": "Under the No Surprises Act, you have the right to a written Good Faith Estimate for any scheduled service if you are uninsured or self-pay. Simply tell the provider: 'I would like a Good Faith Estimate for this procedure as required under the No Surprises Act.' The estimate must include expected charges from the primary provider and any other providers involved (anesthesiologist, lab, facility). If the final bill exceeds the estimate by $400 or more, you can dispute it through the federal process.",
        },
        {
            "q": "How do I compare prices at different facilities?",
            "a": "Three ways: check hospital price transparency files on hospital websites (required by law), use your insurer's cost estimator tool (required by the Transparency in Coverage Rule), or use the BillKarma hospital directory to compare prices across facilities in your area. For outpatient procedures, always compare hospital outpatient department prices to ambulatory surgery center prices — ASCs are typically 40-60% cheaper for the same procedure.",
        },
        {
            "q": "What is the best way to negotiate a cash price?",
            "a": "Ask for the 'self-pay' or 'cash-pay' rate, which is always lower than the chargemaster rate. Then look up the Medicare rate for your procedure and offer 150-200% of Medicare as a lump-sum payment. Mention that you've compared prices at competing facilities. If the provider won't budge, ask for a payment plan at the lower rate, or offer to pay in full upfront for an additional discount. Most providers will negotiate rather than risk losing the patient.",
        },
        {
            "q": "Should I negotiate with the hospital or the surgeon?",
            "a": "Both, separately. The hospital charges a facility fee, and the surgeon charges a professional fee. These are negotiated independently. Start with the hospital (where the larger charges are), then the surgeon. Don't forget to ask about and negotiate anesthesia, lab work, pathology, and any other providers who will be involved. Get everything in writing before the procedure.",
        },
        {
            "q": "What if I have insurance — can I still negotiate?",
            "a": "Insured patients have less room to negotiate the rate (which is set by the insurer's contract), but you can still: choose a lower-cost facility (same insurer rates vary by facility), confirm all providers are in-network before the procedure, compare your insurer's cost estimator across facilities, ask about the cash-pay rate if it's lower than your insured rate (possible if you haven't met your deductible), and verify the correct codes are being used to maximize insurance coverage.",
        },
    ],
    "body": f"""
<p class="lead">The time to negotiate a medical bill is <strong>before the procedure, not after</strong>. Before treatment, you have leverage: the provider wants your business, competing facilities want it too, and you can walk away. After treatment, you owe the money and your leverage is gone. Patients who negotiate before scheduled procedures save <strong>30&ndash;70%</strong> compared to those who accept the first price. Here is exactly how to do it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-before">Why negotiating before is critical</a></li>
        <li><a href="#get-codes">Step 1: Get the CPT codes</a></li>
        <li><a href="#benchmark">Step 2: Find your benchmark prices</a></li>
        <li><a href="#compare">Step 3: Compare facilities</a></li>
        <li><a href="#negotiate">Step 4: Negotiate the price</a></li>
        <li><a href="#get-writing">Step 5: Get it in writing</a></li>
        <li><a href="#insured">Special considerations for insured patients</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-before">1. Why negotiating before is critical</h2>

<table>
    <thead>
        <tr><th>Factor</th><th>Before procedure</th><th>After procedure</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Your leverage</strong></td><td>High &mdash; you can choose another provider</td><td>None &mdash; service already rendered</td></tr>
        <tr><td><strong>Provider&rsquo;s incentive</strong></td><td>Wants to win your business</td><td>Has no competitive pressure</td></tr>
        <tr><td><strong>Price transparency</strong></td><td>Can compare across facilities before committing</td><td>Bill is final, comparison is academic</td></tr>
        <tr><td><strong>Good Faith Estimate</strong></td><td>Legal right to written estimate</td><td>Can only dispute if bill exceeds estimate by $400+</td></tr>
        <tr><td><strong>Payment terms</strong></td><td>Can negotiate upfront payment discount</td><td>Payment plan is only option</td></tr>
        <tr><td><strong>Typical savings</strong></td><td>30&ndash;70%</td><td>10&ndash;30% (if any)</td></tr>
    </tbody>
</table>

<h2 id="get-codes">2. Step 1: Get the CPT codes</h2>

<p>Before you can compare prices, you need to know exactly what codes will be billed. Call your doctor&rsquo;s office and ask:</p>

<p><strong>Script:</strong> &ldquo;I&rsquo;m scheduling [procedure]. Can you give me the CPT codes that will be billed, including any facility, anesthesia, lab, or pathology codes? I want to compare pricing and get a Good Faith Estimate.&rdquo;</p>

<p>For a typical outpatient procedure, you may receive separate charges for:</p>
<ul>
    <li><strong>Surgeon&rsquo;s professional fee</strong> (CPT code for the procedure)</li>
    <li><strong>Facility fee</strong> (if at a hospital outpatient department)</li>
    <li><strong>Anesthesia</strong> (anesthesia code + time units)</li>
    <li><strong>Lab/pathology</strong> (if tissue is sent for analysis)</li>
    <li><strong>Imaging</strong> (if X-ray or fluoroscopy is used during the procedure)</li>
</ul>

<h2 id="benchmark">3. Step 2: Find your benchmark prices</h2>

<p>Once you have the CPT codes, look up three benchmark prices:</p>

<p><strong>Medicare rate:</strong> This is the gold standard benchmark. It represents what the federal government has determined is a fair price for the service. Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for each CPT code. Most negotiations with hospitals settle between 150&ndash;250% of the Medicare rate.</p>

{_calc_embed}

<p><strong>Hospital&rsquo;s published cash price:</strong> Under the price transparency rule, hospitals must publish their discounted cash price. Check the hospital&rsquo;s website or the <a href="/hospitals/">BillKarma hospital directory</a> to find the published self-pay rate.</p>

<p><strong>Competing facility prices:</strong> Get quotes from at least two other facilities. For outpatient procedures, include at least one ambulatory surgery center (ASC), which is typically 40&ndash;60% cheaper than a hospital outpatient department.</p>

<div class="bill-example">
    <div class="bill-header">Price comparison: Knee arthroscopy (CPT 29881) &mdash; same metro area</div>
    <div class="line-item">
        <span>Medicare rate (2026)</span>
        <span>$1,420</span>
    </div>
    <div class="line-item">
        <span>Ambulatory surgery center (ASC) cash price</span>
        <span>$2,800</span>
    </div>
    <div class="line-item">
        <span>Community hospital &mdash; published cash price</span>
        <span>$4,200</span>
    </div>
    <div class="line-item flagged">
        <span>Academic medical center &mdash; published cash price</span>
        <span>$8,500</span>
    </div>
    <div class="line-total">
        <span>Potential savings: ASC vs. academic medical center</span>
        <span>$5,700 (67%)</span>
    </div>
</div>

<h2 id="compare">4. Step 3: Compare facilities</h2>

<p>For any scheduled outpatient procedure, compare at least three facilities:</p>

<ol>
    <li><strong>Hospital outpatient department (HOPD):</strong> The most expensive option. Adds a facility fee on top of the professional fee. See our <a href="/guides/site-neutral-payment-2026">facility fee guide</a>.</li>
    <li><strong>Ambulatory surgery center (ASC):</strong> Typically 40&ndash;60% less than HOPDs for the same procedure. Same doctors, same equipment, no facility fee.</li>
    <li><strong>Independent imaging center</strong> (for scans/imaging): Often 50&ndash;70% less than hospital-based imaging.</li>
</ol>

<p><strong>Important:</strong> Ask your surgeon if they operate at multiple facilities. Many surgeons have privileges at both hospitals and ASCs. If your surgeon only operates at a hospital, ask if they can refer you to a colleague at an ASC, or find an ASC-based surgeon for the same procedure.</p>

<h2 id="negotiate">5. Step 4: Negotiate the price</h2>

<h3>If you&rsquo;re uninsured or self-pay</h3>

<p><strong>Script:</strong> &ldquo;I&rsquo;m a self-pay patient and I&rsquo;ve been comparing prices for [procedure]. I see that [competing facility] offers this for $[lower price], and the Medicare rate is $[Medicare rate]. I&rsquo;d like to schedule with you. Can you match $[target price]? I can pay in full upfront.&rdquo;</p>

<p><strong>Key leverage points:</strong></p>
<ul>
    <li>You can pay upfront (eliminates billing and collection costs for the provider)</li>
    <li>You have competing quotes from other facilities</li>
    <li>You know the Medicare rate (what the government says is fair)</li>
    <li>You know their published cash price from the transparency file</li>
    <li>You&rsquo;re a patient they want to keep (or gain)</li>
</ul>

<p><strong>Target price ranges:</strong></p>
<table>
    <thead>
        <tr><th>Your offer</th><th>When to use it</th><th>Likelihood of acceptance</th></tr>
    </thead>
    <tbody>
        <tr><td>150% of Medicare</td><td>Starting offer, especially at ASCs</td><td>Moderate &mdash; some accept, many counter</td></tr>
        <tr><td>200% of Medicare</td><td>Sweet spot for most providers</td><td>High &mdash; most providers accept</td></tr>
        <tr><td>250% of Medicare</td><td>Fair ceiling for complex procedures</td><td>Very high &mdash; almost always accepted</td></tr>
        <tr><td>Published cash price</td><td>If you can&rsquo;t negotiate lower</td><td>Guaranteed &mdash; it&rsquo;s their posted rate</td></tr>
    </tbody>
</table>

<h3>If you&rsquo;re insured but haven&rsquo;t met your deductible</h3>

<p>If your deductible is high and you haven&rsquo;t met it, you&rsquo;re effectively paying the full negotiated rate out of pocket. In some cases, the cash-pay price is actually <strong>lower</strong> than your insurer&rsquo;s negotiated rate:</p>

<p><strong>Script:</strong> &ldquo;I have insurance but haven&rsquo;t met my deductible, so I&rsquo;ll be paying the full negotiated rate out of pocket. What is your self-pay or cash-pay rate for [procedure]? If it&rsquo;s lower than my insured rate, I&rsquo;d like to pay cash.&rdquo;</p>

<p><strong>Warning:</strong> If you pay cash instead of running it through insurance, the payment will not count toward your deductible. This only makes sense if you don&rsquo;t expect to meet your deductible this year anyway.</p>

<h2 id="get-writing">6. Step 5: Get it in writing</h2>

<p>Once you&rsquo;ve negotiated a price, get a written confirmation before the procedure. This should include:</p>

<ul>
    <li>The total agreed price</li>
    <li>Which services are included (facility, surgeon, anesthesia, lab)</li>
    <li>Any services that are NOT included (and their estimated cost)</li>
    <li>Payment terms (upfront, payment plan, due date)</li>
    <li>The provider&rsquo;s agreement not to bill above this amount</li>
</ul>

<p>If you are uninsured, this written quote also serves as your <strong>Good Faith Estimate</strong> under the No Surprises Act. If the final bill exceeds it by $400 or more, you can dispute through the federal patient-provider dispute resolution process.</p>

<div class="case-study">
    <h3>Case study: Patient saves $4,100 negotiating before shoulder surgery</h3>
    <p><strong>Situation:</strong> Lisa needed arthroscopic shoulder surgery (CPT 29827). Her hospital quoted $9,200 for the facility fee alone (not including the surgeon or anesthesiologist). She had a $5,000 deductible she hadn&rsquo;t met.</p>
    <p><strong>What she did:</strong> She looked up the Medicare rate ($1,850), got a quote from a nearby ASC ($3,400 total including facility), and called the hospital: &ldquo;I have a quote from [ASC] for $3,400 total. The Medicare rate is $1,850. Can you match $5,100?&rdquo; The hospital countered at $5,800. She then asked her surgeon about operating at the ASC instead.</p>
    <p><strong>Result:</strong> She had the surgery at the ASC for $3,400, plus $1,700 for the surgeon (negotiated from $2,400 using the same approach). Total: $5,100 instead of an estimated $12,500+ at the hospital. <strong>Savings: $7,400.</strong> She also <a href="/scan">scanned the final ASC bill</a> to verify no extras were added.</p>
</div>

<h2 id="insured">7. Special considerations for insured patients</h2>

<ul>
    <li><strong>Verify ALL providers are in-network before the procedure.</strong> The surgeon may be in-network but the anesthesiologist or pathologist may not. Ask the facility: &ldquo;Will every provider involved in my care be in-network with [insurer]?&rdquo; Get it in writing.</li>
    <li><strong>Use your insurer&rsquo;s cost estimator.</strong> Under the Transparency in Coverage Rule, your insurer must offer a tool showing personalized cost estimates at different facilities.</li>
    <li><strong>Choose the lowest-cost in-network facility.</strong> Your insurer&rsquo;s negotiated rates vary by facility. The same procedure at two in-network hospitals can cost you very different amounts because of different negotiated rates and facility fees.</li>
    <li><strong>Get prior authorization.</strong> Confirm that prior authorization is approved before the procedure. A denied prior auth after the fact can leave you with the entire bill. See our <a href="/guides/prior-authorization-explained">prior authorization guide</a>.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can I negotiate medical costs before a procedure?</h3>
        <p>Yes. You have far more leverage before treatment than after. Compare prices at multiple facilities, look up Medicare rates as a benchmark, get competing quotes, and offer to pay upfront for a discount. Patients who negotiate save 30&ndash;70% on average.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find out what a procedure should cost?</h3>
        <p>Three benchmarks: the Medicare rate (use the <a href="/calculator">BillKarma calculator</a>), hospital price transparency files (published on hospital websites), and competing facility quotes. For outpatient procedures, always compare hospital prices to ambulatory surgery center prices.</p>
    </div>
    <div class="faq-item">
        <h3>Should I pay cash or use insurance if I haven&rsquo;t met my deductible?</h3>
        <p>Compare the cash-pay price to your insurer&rsquo;s negotiated rate. If the cash price is lower and you don&rsquo;t expect to meet your deductible this year, cash may save money. But cash payments don&rsquo;t count toward your deductible, so if you expect significant medical expenses later in the year, using insurance may be better long-term.</p>
    </div>
    <div class="faq-item">
        <h3>How much lower than the chargemaster price should I aim for?</h3>
        <p>The chargemaster price is irrelevant &mdash; it&rsquo;s an inflated list price no one should pay. Aim for 150&ndash;250% of the Medicare rate for self-pay, or the facility&rsquo;s published cash price. Most providers will accept 200% of Medicare for upfront payment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Good Faith Estimates for Uninsured/Self-Pay Patients</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency Requirements</a></li>
    <li><a href="https://www.cms.gov/healthplan-price-transparency" target="_blank" rel="noopener">CMS: Transparency in Coverage Rule &mdash; Insurer Cost Estimator Requirements</a></li>
    <li><a href="https://www.patientrightsadvocate.org/how-to-fight-medical-bill-overcharges" target="_blank" rel="noopener">Patient Rights Advocate: Fighting Medical Bill Overcharges</a></li>
    <li><a href="https://www.healthcare.gov/using-marketplace-coverage/" target="_blank" rel="noopener">HealthCare.gov: Understanding Your Coverage</a></li>
</ul>
""",
})
