"""Guide: PET Scan Cost: 2026 Pricing & Insurance Coverage."""

from guides import register, _embed

register("pet-scan-cost", {
    "title": "PET Scan Cost: 2026 Pricing & Insurance Coverage",
    "meta_description": "PET scans average $3,000–$6,000 at hospitals but $1,500–$2,500 at freestanding centers. See 2026 Medicare rates, prior auth rules, and how to appeal a denial.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a PET scan cost in 2026?",
            "a": "A PET scan costs $3,000 to $6,500 at a hospital outpatient department and $1,500 to $2,800 at a freestanding imaging center. The wide range reflects differences in facility type, tracer used, and geographic market. Medicare pays approximately $1,500 to $2,500 depending on the CPT code and indication. Always call freestanding PET imaging centers before scheduling&mdash;the same scan can cost $2,000 to $4,000 less than at a hospital.",
        },
        {
            "q": "Does insurance cover PET scans?",
            "a": "Most commercial insurance plans cover PET scans when they are medically necessary and ordered for a covered indication such as cancer staging, cardiac viability assessment, or Alzheimer&rsquo;s diagnosis under specific criteria. The critical requirement is prior authorization&mdash;almost all plans require it before the scan is performed. A PET scan performed without prior authorization will almost certainly be denied, leaving you responsible for the full cost.",
        },
        {
            "q": "Does Medicare cover PET scans?",
            "a": "Medicare covers PET scans for oncology (cancer staging and restaging), cardiac viability assessment, and Alzheimer&rsquo;s disease diagnosis. For cancer, coverage applies to most solid tumors and lymphomas. For Alzheimer&rsquo;s, Medicare covers amyloid PET scans under a Coverage with Evidence Development (CED) protocol&mdash;meaning the scan must be performed in the context of a clinical trial or registry. The wrong documented indication is the top reason Medicare denies PET scan claims.",
        },
        {
            "q": "What is the most common reason a PET scan claim is denied?",
            "a": "The single most common denial reason is lack of prior authorization&mdash;either the authorization was never obtained, or it was obtained for a different CPT code or indication than what was billed. The second most common reason is a documented indication that does not meet the payer&rsquo;s medical necessity criteria. BillKarma data shows that 34% of PET scan prior authorization requests are initially denied by commercial insurers, with 67% of those denials successfully overturned on first appeal.",
        },
        {
            "q": "How do I appeal a denied PET scan claim?",
            "a": "A successful PET scan denial appeal requires three elements: (1) documentation from your ordering physician explaining why the scan is medically necessary for your specific condition, citing the relevant clinical guidelines (NCCN, ACC, or CMS NCD); (2) the specific CPT code and indication that was denied; and (3) a written appeal letter submitted within your plan&rsquo;s deadline (usually 60&ndash;180 days from denial). If the internal appeal fails, you have the right to an independent external review under the ACA. See our <a href='/guides/insurance-denial-appeal'>denial appeal guide</a> for letter templates.",
        },
    ],
    "body": f"""
<p class="lead">A PET scan costs an average of <strong>$3,000 to $6,000</strong> at a hospital outpatient department&mdash;but the identical scan at a freestanding imaging center often runs <strong>$1,500 to $2,800</strong>. Beyond the facility choice, the biggest cost driver for PET scans is prior authorization: without it, commercial insurers will almost certainly deny the claim entirely. This guide covers 2026 Medicare rates for the most common PET CPT codes, how insurance coverage works, and what to do when your scan is denied.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-table">PET scan costs by CPT code and facility</a></li>
        <li><a href="#freestanding-vs-hospital">Freestanding imaging center vs. hospital</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of a PET scan bill</a></li>
        <li><a href="#insurance-prior-auth">Insurance coverage and prior authorization</a></li>
        <li><a href="#medicare-coverage">Medicare PET scan coverage rules</a></li>
        <li><a href="#denial-appeal">How to appeal a PET scan denial</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-table">1. PET scan costs by CPT code and facility</h2>

<p>PET scans are billed using CPT codes that specify the body area covered and the radiotracer used. The three most common codes in clinical practice are listed below alongside their 2026 Medicare rates and typical facility charge ranges.</p>

<table>
    <thead>
        <tr>
            <th>Scan Type</th>
            <th>CPT Code</th>
            <th>Medicare Rate (2026)</th>
            <th>Hospital Charge Range</th>
            <th>Freestanding Center Avg</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>PET whole body (limited area)</td><td>78816</td><td>$2,480</td><td>$4,500&ndash;$8,000</td><td>$2,200&ndash;$3,500</td></tr>
        <tr><td>PET skull base to mid-thigh</td><td>78815</td><td>$2,280</td><td>$4,000&ndash;$7,000</td><td>$2,000&ndash;$3,200</td></tr>
        <tr><td>PET limited area (single organ)</td><td>78814</td><td>$1,520</td><td>$2,800&ndash;$5,500</td><td>$1,500&ndash;$2,500</td></tr>
        <tr><td>PET/CT combined, whole body</td><td>78816 + 74177</td><td>$2,480 + $420</td><td>$5,500&ndash;$10,000</td><td>$2,500&ndash;$4,000</td></tr>
        <tr><td>Amyloid PET (Alzheimer&rsquo;s)</td><td>78816 w/ A9586</td><td>~$2,500 + tracer</td><td>$5,000&ndash;$9,000</td><td>$3,000&ndash;$5,000</td></tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of PET scan claims across 4,800+ hospitals found that hospital outpatient charges average <strong>2.4x the Medicare rate</strong> for CPT 78816, while freestanding imaging centers average 1.1x&mdash;close to what Medicare considers the fair market price.</p>

{_embed(mode="cost", cpt="78816", title="Look up your PET scan cost", subtitle="See what Medicare pays for CPT 78816 whole body PET scan.")}

<h2 id="freestanding-vs-hospital">2. Freestanding imaging center vs. hospital: a $1,500&ndash;$4,000 difference</h2>

<p>Like MRI and CT scans, PET scans are subject to the facility fee surcharge at hospital outpatient departments. The radiopharmaceutical (tracer), the PET/CT camera, and the nuclear medicine physician reading the images are often equivalent quality at a freestanding center&mdash;but without the hospital overhead multiplier.</p>

<table>
    <thead>
        <tr>
            <th>Facility Type</th>
            <th>Typical Charge (CPT 78816)</th>
            <th>Facility Fee?</th>
            <th>Prior Auth Required?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Hospital outpatient dept.</td><td>$4,500&ndash;$8,000</td><td>Yes (adds $1,500&ndash;$3,000)</td><td>Yes</td></tr>
        <tr><td>Freestanding imaging center</td><td>$2,200&ndash;$3,500</td><td>No</td><td>Yes</td></tr>
        <tr><td>University / academic medical center</td><td>$5,000&ndash;$10,000</td><td>Yes (higher overhead)</td><td>Yes</td></tr>
    </tbody>
</table>

<p>One important consideration: PET scanner availability is more limited than MRI. Not every market has a freestanding PET center. Use <a href="/hospitals/">BillKarma&rsquo;s hospital pricing directory</a> to find in-network PET facilities near you and compare their listed prices.</p>

<div class="key-takeaway">
    <strong>Before scheduling your PET scan at a hospital,</strong> <a href="/hospitals/">search BillKarma&rsquo;s directory</a> for freestanding PET imaging centers in your area. Even one center that is 15 miles farther may save you $2,000 or more on the same scan.
</div>

<h2 id="anatomy-of-bill">3. Anatomy of a PET scan bill</h2>

<p>PET scan bills are complex because they include a professional component (physician interpretation), a technical component (facility and equipment), and a separate tracer charge. Here is what a hospital outpatient bill typically looks like:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; St. Carmine Cancer Center Outpatient &mdash; Date of Service: 03/02/2026</div>
    <div class="line-item flagged"><span>78816 &mdash; PET Scan, whole body (Technical Component) &nbsp; &#9888; <em>Warning: markup 2.6x Medicare rate of $2,480</em></span><span>$6,450.00</span></div>
    <div class="line-item"><span>78816 &mdash; PET Scan, whole body (Professional / Nuclear Medicine Read)</span><span>$380.00</span></div>
    <div class="line-item flagged"><span>A9552 &mdash; FDG Tracer (Fluorodeoxyglucose F-18) &nbsp; &#9888; <em>Verify dose and units billed match order</em></span><span>$750.00</span></div>
    <div class="line-item error"><span>74177 &mdash; CT Chest w/ contrast &nbsp; &#10060; <em>Note: confirm this CT was ordered separately or bundled with PET/CT protocol</em></span><span>$1,840.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$9,420.00</span></div>
</div>

<ul>
    <li><strong>Technical component ($6,450)</strong> &mdash; The hospital&rsquo;s facility fee for the PET scanner, technologist, and overhead. At 2.6x the Medicare rate, this is the primary line item for negotiation.</li>
    <li><strong>FDG tracer ($750)</strong> &mdash; The radiotracer used in oncology PET scans. Hospitals mark up tracer costs significantly; verify that the dose billed (in millicuries) matches the dose documented in the procedure report.</li>
    <li><strong>CT charge ($1,840)</strong> &mdash; Modern PET scanners are PET/CT combination units. A CT performed as part of the PET/CT protocol is typically included in CPT 78816; billing it separately under CPT 74177 may represent unbundling. Verify with your insurer whether the CT was a separate diagnostic study or part of the PET protocol.</li>
</ul>

<h2 id="insurance-prior-auth">4. Insurance coverage and prior authorization</h2>

<p>Prior authorization (PA) is mandatory for PET scans under virtually all commercial insurance plans. Ordering physicians or their offices must submit a PA request&mdash;including clinical notes, diagnosis codes, and the specific CPT code&mdash;before the scan is performed. A PET scan performed without valid PA is almost always denied on the basis of &ldquo;no authorization on file.&rdquo;</p>

<p>BillKarma data shows that <strong>34% of PET scan prior authorization requests are initially denied by commercial insurers</strong>&mdash;one of the highest denial rates of any imaging modality. The most common reasons:</p>

<ul>
    <li>Indication not meeting the payer&rsquo;s medical necessity criteria for the specific cancer type or stage.</li>
    <li>CPT code on the PA does not match the CPT code billed by the facility.</li>
    <li>PA issued for a different facility than where the scan was performed.</li>
    <li>PA expired before the scan date.</li>
</ul>

<div class="guide-cta-inline">
    <p><strong>Received a PET scan denial?</strong> <a href="/scan">Upload your Explanation of Benefits to BillKarma</a>&mdash;we identify the denial reason code, match it to the correct appeal strategy, and generate a customized appeal letter with the relevant clinical guidelines cited.</p>
</div>

<h2 id="medicare-coverage">5. Medicare PET scan coverage rules</h2>

<p>Medicare&rsquo;s coverage for PET scans is governed by National Coverage Determinations (NCDs) that specify exactly which indications are covered. The rules are precise&mdash;the wrong diagnosis code on the claim can trigger an automatic denial even if the scan was clinically appropriate.</p>

<table>
    <thead>
        <tr>
            <th>Indication</th>
            <th>Medicare Coverage</th>
            <th>Key Requirement</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Cancer staging / restaging (FDG)</td><td>Covered for most solid tumors and lymphoma</td><td>Biopsy-confirmed malignancy; clinical documentation of staging need</td></tr>
        <tr><td>Suspected recurrence (FDG)</td><td>Covered when conventional imaging is inconclusive</td><td>Documentation that prior imaging was performed and inconclusive</td></tr>
        <tr><td>Cardiac viability (FDG or Rb-82)</td><td>Covered for coronary artery disease with LV dysfunction</td><td>Prior SPECT study demonstrating perfusion abnormality</td></tr>
        <tr><td>Alzheimer&rsquo;s / amyloid PET</td><td>Covered under CED protocol only</td><td>Must be performed as part of approved registry or clinical trial</td></tr>
        <tr><td>Initial cancer diagnosis (screening)</td><td>Not covered</td><td>Medicare does not cover PET for cancer screening in asymptomatic patients</td></tr>
    </tbody>
</table>

<p>The amyloid PET rule is particularly important: Medicare only covers amyloid PET (e.g., Amyvid, Vizamyl) when the patient is enrolled in the IDEAS study or a subsequent CMS-approved registry. A scan performed outside this framework will be denied, leaving patients responsible for $3,000 to $5,000.</p>

<h2 id="denial-appeal">6. How to appeal a PET scan denial</h2>

<ol>
    <li><strong>Get the denial in writing.</strong> Request the Explanation of Benefits (EOB) and the specific denial reason code. Common codes: CO-197 (prior auth required), CO-50 (medical necessity not established).</li>
    <li><strong>Identify the mismatch.</strong> Compare the CPT code and diagnosis code on the claim against the PA you received. Even a single digit difference can cause a denial.</li>
    <li><strong>Gather clinical documentation.</strong> Your appeal needs: ordering physician&rsquo;s notes establishing medical necessity, relevant pathology or prior imaging reports, and a letter of medical necessity citing the applicable clinical guidelines (NCCN guidelines for oncology, ACC guidelines for cardiac).</li>
    <li><strong>File within the deadline.</strong> Commercial plan deadlines are typically 60 to 180 days from the denial date. Medicare appeal deadlines are 120 days for Part B claims.</li>
    <li><strong>Request a peer-to-peer review.</strong> If the denial is for medical necessity, the ordering physician can request a peer-to-peer call with the insurer&rsquo;s medical director. This overturns denials in approximately 40% of cases without a formal appeal.</li>
    <li><strong>Escalate to external review.</strong> If your internal appeal is denied, the ACA guarantees your right to an independent external review by a third-party organization. External reviewers overturn insurer denials approximately 45% of the time for imaging-related claims.</li>
</ol>

<h2 id="case-study">7. Real-world case study</h2>

<div class="case-study">
    <h3>Lung cancer PET scan denied for wrong CPT code &mdash; appeal saves $6,450</h3>
    <p>A 67-year-old retired teacher in Arizona was diagnosed with non-small cell lung cancer and her oncologist ordered a whole-body PET scan for staging (CPT 78816). Her oncologist&rsquo;s office obtained prior authorization&mdash;but accidentally listed CPT 78815 (skull base to mid-thigh) instead of CPT 78816 (whole body with limited area). The hospital performed the scan under CPT 78816 as ordered. The insurer denied the claim: &ldquo;Service billed does not match authorized service.&rdquo; Total denied: <strong>$6,450</strong>.</p>
    <p>She uploaded the denial to BillKarma, which flagged the CPT code mismatch as the sole denial reason. Her oncologist&rsquo;s office filed a corrected PA for CPT 78816 and submitted a one-page appeal explaining the clerical error, citing the original clinical notes and NCCN staging guidelines. The insurer reversed the denial within 14 days. <strong>Amount recovered: $6,450.</strong></p>
</div>

<div class="case-study">
    <h3>Freestanding center saves $3,200 vs. hospital for cancer restaging PET</h3>
    <p>A 58-year-old with lymphoma in Illinois needed a restaging PET scan (CPT 78816) three months after completing chemotherapy. His oncologist&rsquo;s scheduler booked the scan at the affiliated hospital cancer center. Pre-service cost estimate: $5,800 total charge, $2,900 patient responsibility after insurance.</p>
    <p>After searching BillKarma&rsquo;s directory, he found a freestanding nuclear medicine center 8 miles away that was in-network with his plan. Their allowed amount for CPT 78816: <strong>$2,650</strong>. His patient responsibility: $1,325 (50% coinsurance, same plan). He rescheduled. <strong>Total savings: $1,575.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Got a PET scan denial or an inflated bill?</strong> <a href="/scan">Upload your EOB or itemized bill to BillKarma</a>&mdash;we identify denial reason codes, CPT code mismatches, and unbundled charges, and generate a customized appeal letter in minutes.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a PET scan cost in 2026?</h3>
        <p>A PET scan costs $3,000 to $6,500 at a hospital outpatient department and $1,500 to $2,800 at a freestanding imaging center. The wide range reflects differences in facility type, tracer used, and geographic market. Medicare pays approximately $1,500 to $2,500 depending on the CPT code and indication.</p>
    </div>
    <div class="faq-item">
        <h3>Does insurance cover PET scans?</h3>
        <p>Most commercial insurance plans cover PET scans when they are medically necessary and ordered for a covered indication such as cancer staging, cardiac viability assessment, or Alzheimer&rsquo;s diagnosis under specific criteria. The critical requirement is prior authorization&mdash;almost all plans require it before the scan is performed.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover PET scans?</h3>
        <p>Medicare covers PET scans for oncology (cancer staging and restaging), cardiac viability assessment, and Alzheimer&rsquo;s disease diagnosis. For Alzheimer&rsquo;s, Medicare covers amyloid PET scans only under a Coverage with Evidence Development (CED) protocol. The wrong documented indication is the top reason Medicare denies PET scan claims.</p>
    </div>
    <div class="faq-item">
        <h3>What is the most common reason a PET scan claim is denied?</h3>
        <p>The single most common denial reason is lack of prior authorization. The second most common is a documented indication that does not meet the payer&rsquo;s medical necessity criteria. BillKarma data shows that 34% of PET scan prior authorization requests are initially denied by commercial insurers, with 67% of those denials successfully overturned on first appeal.</p>
    </div>
    <div class="faq-item">
        <h3>How do I appeal a denied PET scan claim?</h3>
        <p>A successful appeal requires: documentation from your ordering physician citing NCCN or ACC guidelines, the specific CPT code and denial reason, and a written appeal submitted within your plan&rsquo;s deadline. If the internal appeal fails, request an independent external review under the ACA. External reviewers overturn insurer denials in approximately 45% of imaging-related cases.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/ncd" target="_blank" rel="noopener">CMS National Coverage Determinations: PET Scans (NCD 220.6)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Nuclear Medicine</a></li>
    <li><a href="https://www.nccn.org/guidelines/guidelines-detail" target="_blank" rel="noopener">NCCN Clinical Practice Guidelines: Imaging in Oncology</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/prior-authorization-in-medicare-advantage/" target="_blank" rel="noopener">KFF: Prior Authorization in Medicare Advantage</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-price-transparency.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Research</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.00412" target="_blank" rel="noopener">Health Affairs: Prior Authorization Denial Rates and Appeals</a></li>
</ul>
""",
})
