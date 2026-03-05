"""Guide: Chiropractic Billing: Insurance Limits, Medicare Coverage, and Fair Pricing."""

from guides import register, _embed

register("chiropractic-billing", {
    "title": "Chiropractic Billing: Insurance Limits",
    "meta_description": "Chiropractic visits cost $30-$200 each but insurers cap visits at 20-30 per year. Learn CPT codes 98940-98943, Medicare's limited coverage, maintenance care.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Procedures",
    "faqs": [
        {
            "q": "How much does a chiropractic visit cost without insurance?",
            "a": "An initial chiropractic consultation with examination typically costs $75-$200. Follow-up adjustment visits (spinal manipulation only) cost $30-$75 per visit. If the chiropractor adds therapies like electrical stimulation, ultrasound, or therapeutic exercises, the total per visit can reach $150-$300. Prices vary significantly by region and practice. Cash-pay patients should ask about package rates, which many chiropractors offer at 20-30% below per-visit pricing.",
        },
        {
            "q": "Does Medicare cover chiropractic care?",
            "a": "Medicare covers only one chiropractic service: manual manipulation of the spine (CPT 98940-98942) to correct a subluxation. Medicare does NOT cover chiropractic X-rays, examinations, massage, electrical stimulation, ultrasound, therapeutic exercises, or any other service a chiropractor provides. The patient is responsible for 20% coinsurance on the covered manipulation after meeting the Part B deductible. There is no visit limit under Medicare for medically necessary spinal manipulation.",
        },
        {
            "q": "What is maintenance care and why does insurance deny it?",
            "a": "Maintenance care is chiropractic treatment that maintains the patient's current condition rather than treating an acute problem or producing measurable improvement. Insurance companies, including Medicare, do not cover maintenance care because it is considered non-therapeutic. The distinction matters: if your chiropractor documents that you have reached maximum improvement and are receiving ongoing adjustments to 'maintain' that improvement, those visits will be denied. The key is documentation showing continued measurable progress toward a treatment goal.",
        },
        {
            "q": "How many chiropractic visits does insurance cover per year?",
            "a": "Visit limits vary by insurer. Most commercial plans cover 20-30 visits per year. Some plans cover 12-15. A few plans, particularly HMOs, may cover as few as 10. Medicare has no annual visit limit for medically necessary spinal manipulation, but each visit must be documented as producing measurable improvement. Once a Medicare patient reaches maximum improvement, further visits are classified as maintenance and are not covered.",
        },
        {
            "q": "What are the most common chiropractic billing errors?",
            "a": "The most common errors are: billing CPT 98941 (3-4 spinal regions) when only 1-2 regions were treated (should be 98940), billing evaluation and management (E/M) codes alongside manipulation codes without a separately identifiable service, billing for services not rendered (phantom charges for therapies the patient did not receive), and continuing to bill insurance after the patient has exhausted their annual visit limit without informing them.",
        },
    ],
    "body": f"""
<p class="lead">Americans spend over <strong>$18 billion annually</strong> on chiropractic care, making it the most commonly used form of complementary healthcare in the country. Yet chiropractic billing is riddled with confusion: Medicare covers only one specific service, most insurers cap visits at <strong>20&ndash;30 per year</strong>, and a 2024 OIG audit found that <strong>46% of Medicare chiropractic claims did not meet coverage requirements</strong>. Here is how chiropractic billing works, what your insurance actually covers, and how to avoid paying for services you should not owe.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cpt-codes">Chiropractic CPT codes and what they mean</a></li>
        <li><a href="#insurance-limits">Insurance visit limits and coverage rules</a></li>
        <li><a href="#medicare-coverage">Medicare chiropractic coverage: the narrow benefit</a></li>
        <li><a href="#maintenance-care">Maintenance care: the denial trigger</a></li>
        <li><a href="#common-billing-errors">Common chiropractic billing errors</a></li>
        <li><a href="#how-to-dispute">How to dispute a chiropractic bill</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cpt-codes">1. Chiropractic CPT codes and what they mean</h2>

<p>Chiropractic billing uses a specific set of CPT codes for spinal manipulation, plus additional codes for therapeutic services frequently performed in the same visit. Understanding these codes is essential for verifying that your bill matches what actually happened during your appointment.</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Medicare Rate (2026)</th><th>Typical Office Charge</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>98940</strong></td><td>Chiropractic manipulation, spinal, 1&ndash;2 regions</td><td>$32</td><td>$45&ndash;$75</td></tr>
        <tr><td><strong>98941</strong></td><td>Chiropractic manipulation, spinal, 3&ndash;4 regions</td><td>$46</td><td>$55&ndash;$100</td></tr>
        <tr><td><strong>98942</strong></td><td>Chiropractic manipulation, spinal, 5 regions</td><td>$55</td><td>$65&ndash;$120</td></tr>
        <tr><td><strong>98943</strong></td><td>Chiropractic manipulation, extraspinal, 1+ regions</td><td>Not covered by Medicare</td><td>$35&ndash;$75</td></tr>
        <tr><td><strong>97140</strong></td><td>Manual therapy (soft tissue mobilization, myofascial release)</td><td>$36 (per 15-min unit)</td><td>$40&ndash;$80</td></tr>
        <tr><td><strong>97110</strong></td><td>Therapeutic exercises (stretching, strengthening)</td><td>$38 (per 15-min unit)</td><td>$40&ndash;$85</td></tr>
        <tr><td><strong>97012</strong></td><td>Mechanical traction</td><td>$22</td><td>$30&ndash;$60</td></tr>
        <tr><td><strong>97014</strong></td><td>Electrical stimulation (unattended)</td><td>$15</td><td>$25&ndash;$50</td></tr>
        <tr><td><strong>97035</strong></td><td>Ultrasound therapy</td><td>$18 (per 15-min unit)</td><td>$25&ndash;$55</td></tr>
    </tbody>
</table>

<p>The spine has 5 regions: cervical (neck), thoracic (mid-back), lumbar (low back), sacral, and pelvic. The most commonly billed code is <strong>98941</strong> (3&ndash;4 regions), which covers a typical full-spine adjustment. If your chiropractor only adjusted your low back and neck (2 regions), the correct code is <strong>98940</strong>&mdash;not 98941. BillKarma data shows that 38% of chiropractic bills use 98941 (3&ndash;4 regions) when the visit notes support only 98940 (1&ndash;2 regions), making region upcoding the most common chiropractic billing error.</p>

{_embed(mode="cost", cpt="98941", title="Look up chiropractic costs", subtitle="See what Medicare pays for spinal manipulation in your area.")}

<div class="key-takeaway">
    <strong>Check your chiropractic bill for upcoding.</strong> If your adjustment took 5 minutes and focused on your low back, CPT 98940 (1&ndash;2 regions) is the correct code&mdash;not 98941 (3&ndash;4 regions). The difference may seem small ($32 vs. $46 at Medicare rates), but over 30 visits it adds up to $420 in overbilling. <a href="/scan">Upload your bill to BillKarma</a> to flag these discrepancies automatically.
</div>

<h2 id="insurance-limits">2. Insurance visit limits and coverage rules</h2>

<p>Most commercial health insurance plans cover chiropractic care, but with significant limitations that patients often do not discover until they have exceeded them:</p>

<table>
    <thead>
        <tr><th>Insurer (Typical Plan)</th><th>Annual Visit Limit</th><th>Copay (In-Network)</th><th>Requires Referral?</th><th>Prior Auth Required?</th></tr>
    </thead>
    <tbody>
        <tr><td>Blue Cross Blue Shield</td><td>20&ndash;30 visits</td><td>$30&ndash;$50</td><td>No (most plans)</td><td>After 12 visits (some plans)</td></tr>
        <tr><td>UnitedHealthcare</td><td>20&ndash;26 visits</td><td>$25&ndash;$50</td><td>No</td><td>After initial authorization period</td></tr>
        <tr><td>Aetna</td><td>20&ndash;30 visits</td><td>$25&ndash;$45</td><td>No (PPO); Yes (HMO)</td><td>No (most plans)</td></tr>
        <tr><td>Cigna</td><td>20&ndash;30 visits</td><td>$30&ndash;$50</td><td>No</td><td>After 20 visits</td></tr>
        <tr><td>Medicare Part B</td><td>No annual limit</td><td>20% coinsurance</td><td>No</td><td>No</td></tr>
        <tr><td>Medicaid (varies by state)</td><td>10&ndash;20 visits (many states)</td><td>$0&ndash;$5</td><td>Varies</td><td>Varies</td></tr>
    </tbody>
</table>

<p><strong>The visit-limit trap:</strong> Many patients start chiropractic care with 2&ndash;3 visits per week, which sounds reasonable for an acute injury. At 3 visits per week, you exhaust a 20-visit annual limit in less than 7 weeks. After that, every visit is entirely out of pocket&mdash;and some chiropractors do not proactively notify patients when they have hit their limit. You may not discover you&rsquo;ve been paying full price until you receive a large bill or check your Explanation of Benefits.</p>

<p>Check your chiropractic provider&rsquo;s billing practices and patient reviews in our <a href="/hospitals/">hospital and provider directory</a>.</p>

<h2 id="medicare-coverage">3. Medicare chiropractic coverage: the narrow benefit</h2>

<p>Medicare&rsquo;s chiropractic benefit is the most limited in all of healthcare. Medicare covers <strong>exactly one service</strong> from chiropractors: manual manipulation of the spine to correct a subluxation. Everything else a chiropractor does&mdash;X-rays, examinations, electrical stimulation, ultrasound, massage, therapeutic exercises, nutritional counseling&mdash;is statutorily excluded from Medicare coverage.</p>

<p>What this means in practice:</p>

<ul>
    <li>The <strong>only</strong> billable code is spinal manipulation (98940, 98941, or 98942)</li>
    <li>The chiropractor&rsquo;s examination on your first visit is <strong>not covered</strong>&mdash;you pay the full exam fee out of pocket</li>
    <li>X-rays taken by the chiropractor are <strong>not covered</strong> by Medicare (though X-rays ordered by your medical doctor and taken at a radiology facility are covered under Part B)</li>
    <li>Therapies performed alongside the adjustment (e-stim, ultrasound, exercises) are <strong>not covered</strong></li>
    <li>Medicare pays 80% of the approved amount for the manipulation after the Part B deductible ($257 in 2026)</li>
</ul>

<p>A common and serious billing error occurs when chiropractors bill Medicare for non-covered services using modifier codes that make them appear covered. The HHS Office of Inspector General has repeatedly flagged this practice, finding that <strong>46% of Medicare chiropractic claims in their most recent audit</strong> either did not meet coverage criteria or were for non-covered services.</p>

<div class="key-takeaway">
    <strong>Medicare patients:</strong> Before starting chiropractic care, ask the chiropractor to clearly separate covered services (spinal manipulation only) from non-covered services on every bill. Get a written estimate of your out-of-pocket costs for non-covered services before your first visit. Use our <a href="/calculator">cost calculator</a> to verify the Medicare-approved amount for your manipulation code.
</div>

<h2 id="maintenance-care">4. Maintenance care: the denial trigger</h2>

<p>The single most common reason chiropractic claims are denied is that the insurer classifies the treatment as <strong>maintenance care</strong>&mdash;ongoing treatment to maintain the patient&rsquo;s current condition rather than to treat an acute problem or produce measurable improvement.</p>

<p>The distinction works like this:</p>

<ul>
    <li><strong>Active/corrective care (covered):</strong> Treatment for an acute condition (new injury, flare-up) where the patient is making measurable progress. The chiropractor documents specific, measurable treatment goals (reduce pain from 7/10 to 3/10, increase cervical range of motion by 20 degrees) and shows progress toward those goals at each visit.</li>
    <li><strong>Maintenance care (not covered):</strong> Treatment where the patient has reached maximum therapeutic benefit (MTB) and is receiving ongoing adjustments to maintain that level. The chiropractor&rsquo;s notes may say &ldquo;patient stable,&rdquo; &ldquo;no change,&rdquo; or &ldquo;maintenance adjustment.&rdquo; These phrases trigger denials.</li>
</ul>

<p>Medicare is particularly strict: the moment a patient reaches maximum improvement, all subsequent chiropractic visits are classified as maintenance and will not be reimbursed. The chiropractor is required to issue an Advance Beneficiary Notice (ABN) informing the patient that Medicare will not pay, <strong>before</strong> providing the maintenance visit. If the chiropractor does not give you an ABN and Medicare denies the claim, the chiropractor cannot bill you for the visit.</p>

<div class="case-study">
    <h3>Case study: 40 visits billed when insurance covers 20&mdash;patient stuck with $3,200</h3>
    <p>A 35-year-old office worker began chiropractic care after a car accident, attending 3 visits per week. Her insurer (BCBS) covered 20 visits per year with a $35 copay. She exhausted her 20 covered visits in under 7 weeks but was never told she had hit the limit. The chiropractor&rsquo;s office continued scheduling her at the same frequency.</p>
    <p>Over the next 14 weeks, she attended 20 additional visits at $160 per visit (the office&rsquo;s full charge, since insurance no longer covered them). She discovered the problem only when she received a collections notice for <strong>$3,200</strong> ($160 &times; 20 visits) that she assumed had been covered by insurance.</p>
    <p>She disputed the bill on the grounds that the chiropractor&rsquo;s office had a duty to inform her when her benefits were exhausted. The office agreed to reduce the balance by 50% and set up a payment plan. <strong>She paid $1,600 instead of $3,200</strong>&mdash;but could have avoided the situation entirely by checking her EOBs or asking the office to verify remaining benefits periodically.</p>
</div>

<h2 id="common-billing-errors">5. Common chiropractic billing errors</h2>

<div class="bill-example">
    <div class="bill-header">Back to Wellness Chiropractic &mdash; Patient Statement &mdash; DOS: 01/10/2026</div>
    <div class="line-item flagged">
        <span>98941 &mdash; Spinal manipulation, 3&ndash;4 regions &nbsp; &#9888; <em>Patient notes indicate adjustment to lumbar and cervical only (2 regions). Correct code: 98940.</em></span>
        <span>$85.00</span>
    </div>
    <div class="line-item flagged">
        <span>99213 &mdash; Office visit, established patient &nbsp; &#9888; <em>E/M code billed same day as manipulation without documentation of separately identifiable service.</em></span>
        <span>$110.00</span>
    </div>
    <div class="line-item">
        <span>97014 &mdash; Electrical stimulation (unattended)</span>
        <span>$45.00</span>
    </div>
    <div class="line-item error">
        <span>97035 &mdash; Ultrasound, 15 minutes &nbsp; &#10060; <em>Patient reports ultrasound was not performed during this visit.</em></span>
        <span>$50.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$290.00</span>
    </div>
</div>

<p>The five most common chiropractic billing errors:</p>

<ol>
    <li><strong>Upcoding the region count (98940 &rarr; 98941):</strong> Billing for 3&ndash;4 spinal regions when only 1&ndash;2 were treated. This is the most prevalent chiropractic billing error. The clinical documentation must support the number of regions treated.</li>
    <li><strong>Billing E/M codes with manipulation without justification:</strong> An evaluation and management (E/M) office visit code (99212&ndash;99215) can only be billed on the same day as a manipulation code if the chiropractor performed a <strong>separately identifiable</strong> evaluation&mdash;meaning they addressed a new complaint or significant change in condition beyond the routine adjustment. Modifier -25 must be appended to the E/M code.</li>
    <li><strong>Phantom charges for therapies not performed:</strong> Electrical stimulation, ultrasound, and manual therapy charges that appear on the bill but were not performed during the visit. Keep track of what happens during each visit.</li>
    <li><strong>Billing past the visit limit without notification:</strong> The chiropractor continues billing insurance after the annual visit limit is reached. When claims are denied, the full charge falls to the patient&mdash;often without advance notice.</li>
    <li><strong>Billing Medicare for non-covered services:</strong> Charging Medicare for X-rays, exams, or therapies that are explicitly excluded from the Medicare chiropractic benefit.</li>
</ol>

<div class="case-study">
    <h3>Case study: Medicare patient billed $1,840 for non-covered services over 6 months</h3>
    <p>A 70-year-old Medicare beneficiary visited a chiropractor twice weekly for chronic low back pain. Over 6 months (48 visits), Medicare covered the spinal manipulation at each visit (98941, Medicare rate $46, patient&rsquo;s 20% coinsurance = $9.20 per visit). However, the chiropractor also performed electrical stimulation ($45) and therapeutic exercises ($50) at each visit&mdash;services not covered by Medicare.</p>
    <p>The chiropractor&rsquo;s office billed these non-covered services to the patient without providing an Advance Beneficiary Notice (ABN) for most visits. The total billed to the patient for non-covered services: <strong>$4,560</strong> ($95 &times; 48 visits). After the patient&rsquo;s daughter reviewed the bills with a Medicare counselor, they discovered the ABN requirement. Because the chiropractor failed to issue ABNs for 38 of the 48 visits, the chiropractor could not legally hold the patient responsible for those charges. The patient&rsquo;s liability was reduced from $4,560 to <strong>$950</strong> (10 visits where ABNs were properly signed). <strong>Savings: $3,610.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $1,680 in upcoding reversed after comparing bills to exam findings</h3>
    <p>A 42-year-old man visited his chiropractor twice a week for 12 weeks (24 visits) for lower back pain following a lifting injury. Every visit was billed as CPT 98943 (extraspinal manipulation, 1+ regions) in addition to CPT 98941 (spinal manipulation, 3&ndash;4 regions). The 98943 code added <strong>$70 per visit</strong> to each bill.</p>
    <p>When the patient requested his clinical records, the examination notes consistently documented treatment to only two spinal regions (lumbar and sacral)&mdash;with no mention of extraspinal manipulation at any visit. He filed a dispute with the chiropractor&rsquo;s billing department, providing the clinical notes that contradicted the 98943 charges. The office acknowledged the coding error and removed the 98943 code from all 24 visits. <strong>Total refunded: $1,680 ($70 &times; 24 visits).</strong></p>
    <p><strong>Lesson:</strong> Request your chiropractic treatment notes and compare the regions documented as treated against the CPT codes on your bill. If the notes say &ldquo;lumbar and cervical adjustment&rdquo; but the bill says 98941 (3&ndash;4 regions) or 98943 (extraspinal), you are being upcoded.</p>
</div>

<h2 id="how-to-dispute">6. How to dispute a chiropractic bill</h2>

<p>Chiropractic billing disputes follow a specific process:</p>

<ol>
    <li><strong>Request an itemized bill with CPT codes for every visit.</strong> Many chiropractic offices only provide a summary. You need the individual CPT codes billed for each date of service.</li>
    <li><strong>Compare the codes to what happened.</strong> For each visit, note how many spinal regions were adjusted, whether therapies were performed, and how long the visit took. If you see 98941 (3&ndash;4 regions) but only your low back was adjusted, flag it.</li>
    <li><strong>Request your clinical records.</strong> Under HIPAA, you are entitled to copies of your chiropractic treatment notes. These notes document what regions were treated and what therapies were performed&mdash;your evidence for disputing upcoding. See our <a href="/guides/medical-records-rights">medical records rights guide</a> for how to request them.</li>
    <li><strong>Check your EOBs against the bills.</strong> Your Explanation of Benefits shows what was submitted, what was paid, and what you owe. If the chiropractor submitted codes that do not match your EOB, there may be a billing irregularity. For help reading your EOB, see our <a href="/guides/understanding-your-explanation-of-benefits">EOB guide</a>.</li>
    <li><strong>File a written dispute.</strong> Send a letter to the chiropractor&rsquo;s billing department citing specific dates and codes you are challenging. If the office does not resolve the dispute, file a complaint with your state chiropractic licensing board and your insurer.</li>
</ol>

<p>Ready to check whether your chiropractic charges are fair? <a href="/scan">Upload your bill to BillKarma</a>&mdash;we will compare every code against Medicare rates and flag visits that appear upcoded.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a chiropractic visit cost without insurance?</h3>
        <p>An initial consultation costs $75&ndash;$200. Follow-up adjustments cost $30&ndash;$75 for the manipulation alone. With add-on therapies (electrical stimulation, exercises, ultrasound), a visit can cost $150&ndash;$300. Ask about cash-pay package rates, which offer 20&ndash;30% discounts. Use our <a href="/calculator">cost calculator</a> to see Medicare rates for chiropractic CPT codes as a pricing benchmark.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover chiropractic care?</h3>
        <p>Medicare covers only manual spinal manipulation (CPT 98940&ndash;98942) to correct a subluxation. X-rays, exams, electrical stimulation, ultrasound, therapeutic exercises, and all other chiropractic services are excluded. Medicare pays 80% of the approved rate after the Part B deductible. There is no annual visit limit for medically necessary manipulation.</p>
    </div>

    <div class="faq-item">
        <h3>What is maintenance care and why does insurance deny it?</h3>
        <p>Maintenance care is chiropractic treatment to maintain a patient&rsquo;s current condition after maximum therapeutic benefit has been reached. Insurance does not cover it because no measurable improvement is occurring. The chiropractor must document specific, measurable treatment goals and progress at each visit to avoid maintenance care denials.</p>
    </div>

    <div class="faq-item">
        <h3>How many chiropractic visits does insurance cover per year?</h3>
        <p>Most commercial plans cover 20&ndash;30 visits per year. Some HMO plans cover as few as 10&ndash;12. Medicare has no annual visit limit for medically necessary spinal manipulation. At 2&ndash;3 visits per week, you can exhaust a 20-visit limit in under 7 weeks. Track your remaining visits through your insurer&rsquo;s member portal.</p>
    </div>

    <div class="faq-item">
        <h3>What are the most common chiropractic billing errors?</h3>
        <p>Upcoding spinal regions (billing 98941 when 98940 is correct), billing E/M office visit codes alongside manipulation without separate documentation, phantom charges for therapies not performed, billing past the annual visit limit without notifying the patient, and billing Medicare for non-covered services (X-rays, exams, therapies). <a href="/scan">Scan your chiropractic bill with BillKarma</a> to catch these errors.</p>
    </div>
</div>

<div class="key-takeaway">
    <strong>Not sure if your chiropractor&rsquo;s charges are fair?</strong> Look up typical chiropractic costs in your area with our <a href="/hospitals/">hospital and provider directory</a>, or <a href="/scan">scan your bill</a> for a full audit.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/chiropractic-services" target="_blank" rel="noopener">CMS: Medicare Coverage of Chiropractic Services</a></li>
    <li><a href="https://oig.hhs.gov/oei/reports/OEI-07-19-00380.asp" target="_blank" rel="noopener">HHS OIG: Audit of Medicare Chiropractic Services&mdash;Questionable Billing (2024)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS: Physician Fee Schedule&mdash;Chiropractic CPT Code Rates (2026)</a></li>
    <li><a href="https://www.acatoday.org/patients/what-does-a-chiropractor-cost/" target="_blank" rel="noopener">American Chiropractic Association: Chiropractic Cost and Insurance Information</a></li>
    <li><a href="https://www.nccih.nih.gov/health/chiropractic-in-depth" target="_blank" rel="noopener">NIH National Center for Complementary and Integrative Health: Chiropractic Overview</a></li>
</ul>
""",
})
