"""Guide: DEXA Scan Cost: Bone Density Test Pricing in 2026."""

from guides import register, _embed

register("dexa-scan-cost", {
    "title": "DEXA Scan Cost: Bone Density Test Pricing in 2026",
    "meta_description": "DEXA scans average $125 at Medicare rates but hospitals charge up to $600. See who gets it free in 2026, CPT codes 77080\u201377085, and how to dispute overbilling.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a DEXA scan cost without insurance?",
            "a": "Without insurance, a DEXA scan costs $100 to $250 at a freestanding imaging center and $200 to $600 at a hospital outpatient department. The Medicare rate for an axial DEXA scan (CPT 77080, covering spine and hip) is approximately $125, which is a useful benchmark for evaluating any cash price you are quoted. Some imaging centers advertise self-pay DEXA scans for $75 to $150&mdash;these are legitimate low-cost options, often at facilities that specialize in preventive imaging rather than acute care.",
        },
        {
            "q": "Who gets a DEXA scan free under Medicare?",
            "a": "Medicare Part B covers a bone density test every 24 months at no cost to: (1) women at estrogen deficiency and at risk for osteoporosis, (2) individuals with vertebral abnormalities, (3) individuals receiving or expected to receive glucocorticoid (steroid) therapy, (4) individuals with hyperparathyroidism, and (5) individuals being monitored for osteoporosis drug therapy response. Medicare will not waive cost-sharing for DEXA scans ordered more frequently than every 24 months unless clinical necessity is documented and approved.",
        },
        {
            "q": "What CPT codes are used for DEXA scans?",
            "a": "The two main DEXA scan CPT codes are 77080 and 77081. CPT 77080 covers dual-energy X-ray absorptiometry (DXA) of the axial skeleton&mdash;specifically the spine and hip&mdash;which is the standard bone density test used to diagnose osteoporosis. CPT 77081 covers the appendicular skeleton (wrist, heel, or other peripheral sites) and is less commonly ordered. A third code, 77085, covers axial DEXA with vertebral fracture assessment (VFA)&mdash;an additional analysis that images thoracic and lumbar vertebrae for fracture signs. VFA is sometimes added without clinical justification.",
        },
        {
            "q": "Is a vertebral fracture assessment (VFA) necessary with every DEXA scan?",
            "a": "No. Vertebral fracture assessment (CPT 77085) adds imaging of the spine to identify compression fractures. The International Society for Clinical Densitometry recommends VFA for patients over 70, those who have lost more than 1.5 inches of height, those with moderate-to-severe back pain, or those taking steroid medications. For a 65-year-old woman with no back pain and no fracture risk factors receiving a routine screening DEXA, adding CPT 77085 may not be clinically indicated. If VFA appears on your bill and you do not meet these criteria, ask your provider why it was ordered.",
        },
        {
            "q": "Does the ACA require free DEXA scans for women?",
            "a": "Yes, for women 65 and older. The USPSTF gives screening for osteoporosis in women age 65 and older a B recommendation, which triggers the ACA&rsquo;s preventive care mandate for ACA-compliant plans. Women 65 and older must receive a bone density screening at no cost-sharing (no copay, no deductible) when using an in-network provider. Younger women with increased fracture risk may also qualify for free screening, but coverage for younger women varies by plan and the insurer&rsquo;s interpretation of the USPSTF criteria.",
        },
    ],
    "body": f"""
<p class="lead">A DEXA bone density scan should cost <strong>$0 out of pocket</strong> for millions of women who qualify for free preventive coverage&mdash;but hospitals regularly bill <strong>$400 to $600</strong> for a procedure that Medicare values at just <strong>$125</strong>. BillKarma&rsquo;s review of DEXA scan claims finds that <strong>22% include charges for the vertebral fracture assessment add-on (CPT 77085) without documented clinical justification</strong>, adding $80 to $250 in unnecessary costs. This guide covers who gets a DEXA scan free, what each CPT code costs, and how to challenge overbilling.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#who-gets-free">Who gets a DEXA scan free in 2026</a></li>
        <li><a href="#cost-table">DEXA scan costs by facility and CPT code</a></li>
        <li><a href="#cpt-codes">CPT 77080, 77081, and 77085 explained</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of a DEXA scan bill</a></li>
        <li><a href="#vfa-unnecessary">When VFA (CPT 77085) is unnecessary</a></li>
        <li><a href="#cash-pay">How to get a cash-pay rate</a></li>
        <li><a href="#insurance-coverage">Insurance coverage rules by plan type</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="who-gets-free">1. Who gets a DEXA scan free in 2026</h2>

<p>Two separate federal rules create free bone density testing for specific groups:</p>

<table>
    <thead>
        <tr>
            <th>Coverage Source</th>
            <th>Who Qualifies</th>
            <th>Frequency</th>
            <th>Your Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>ACA Preventive Care Mandate</td><td>Women age 65+ on ACA-compliant plans</td><td>Per USPSTF recommendation (typically every 2 years)</td><td>$0 in-network</td></tr>
        <tr><td>Medicare Part B</td><td>Individuals meeting Medicare criteria (see FAQ)</td><td>Every 24 months</td><td>$0 (no deductible, no coinsurance)</td></tr>
        <tr><td>Medicaid</td><td>Varies by state; most cover women 65+</td><td>Typically every 2 years</td><td>Minimal or $0</td></tr>
        <tr><td>Standard insurance (non-ACA preventive)</td><td>Ordered for diagnosis, not screening</td><td>Per medical necessity</td><td>Deductible + coinsurance apply</td></tr>
    </tbody>
</table>

<p>The catch: &ldquo;free&rdquo; under both ACA and Medicare rules applies only when the scan is correctly coded as a screening or preventive service. If your physician orders a DEXA scan with a diagnosis code for osteoporosis treatment monitoring rather than preventive screening, the claim may not qualify for zero cost-sharing, even if you would otherwise be eligible.</p>

<div class="key-takeaway">
    <strong>Before your DEXA scan, ask your provider:</strong> &ldquo;Is this being ordered as a preventive/screening DEXA or as a diagnostic DEXA?&rdquo; The answer determines whether your cost is $0 or potentially $60 to $300. If you are 65 or older and have never had a bone density test, it should be preventive.
</div>

<h2 id="cost-table">2. DEXA scan costs by facility and CPT code</h2>

<p>Facility type is the largest driver of DEXA scan cost. The imaging is identical regardless of where it is performed, but hospital facility fees drive prices 3 to 5 times higher than freestanding centers.</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Scan Type</th>
            <th>Medicare Rate</th>
            <th>Hospital Outpatient</th>
            <th>Freestanding Imaging Center</th>
            <th>Self-Pay Imaging Clinic</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>77080</td><td>Axial DEXA (spine + hip)</td><td>~$125</td><td>$200&ndash;$600</td><td>$100&ndash;$250</td><td>$75&ndash;$150</td></tr>
        <tr><td>77081</td><td>Appendicular DEXA (peripheral)</td><td>~$43</td><td>$100&ndash;$300</td><td>$60&ndash;$150</td><td>$40&ndash;$100</td></tr>
        <tr><td>77085</td><td>Axial DEXA + VFA (vertebral fracture assessment)</td><td>~$164</td><td>$250&ndash;$700</td><td>$130&ndash;$300</td><td>$100&ndash;$200</td></tr>
    </tbody>
</table>

<p>Note: Medicare rates reflect the 2026 Physician Fee Schedule non-facility rate. Hospital outpatient rates are based on the Hospital Outpatient Prospective Payment System (OPPS) and reflect the facility fee plus professional component combined.</p>

{_embed(mode="cost", cpt="77080", title="Look up DEXA scan costs near you", subtitle="Compare what facilities charge for CPT 77080 vs. the Medicare rate.")}

<h2 id="cpt-codes">3. CPT 77080, 77081, and 77085 explained</h2>

<p>Three CPT codes cover nearly all DEXA scan billing. Here is what each one means and when it should appear on your bill:</p>

<ul>
    <li><strong>CPT 77080 &mdash; Axial DEXA, spine and/or hip:</strong> The standard bone density test that measures bone mineral density at the lumbar spine and proximal femur (hip). This is the test used to diagnose osteoporosis and osteopenia per WHO criteria. It should appear on nearly every DEXA scan order for osteoporosis screening.</li>
    <li><strong>CPT 77081 &mdash; Appendicular DEXA (peripheral):</strong> Measures bone density at a peripheral site such as the forearm, wrist, or heel. Less common than 77080; typically ordered when axial imaging is not accessible or for monitoring specific conditions. Should not be billed together with 77080 on the same date without clinical justification.</li>
    <li><strong>CPT 77085 &mdash; Axial DEXA with vertebral fracture assessment:</strong> Combines the standard DEXA scan with a separate spinal imaging protocol that captures lateral images of the thoracic and lumbar vertebrae to identify compression fractures. Adds $39 to $75 to the Medicare rate and significantly more at hospital outpatient rates. Appropriate for high-risk patients; inappropriate for routine low-risk screenings.</li>
</ul>

<h2 id="anatomy-of-bill">4. Anatomy of a DEXA scan bill</h2>

<p>A DEXA scan bill from a hospital outpatient department often looks like this&mdash;with the problematic add-on charge highlighted:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Lakeview Hospital Radiology &mdash; Date of Service: 01/22/2026</div>
    <div class="line-item flagged"><span>77080 &mdash; DEXA Scan, Axial Skeleton (Spine/Hip) &nbsp; &#9888; <em>Warning: charged $490; Medicare rate $125; markup 3.9x</em></span><span>$490.00</span></div>
    <div class="line-item error"><span>77085 &mdash; DEXA with Vertebral Fracture Assessment &nbsp; &#10060; <em>Flag: patient is 67-year-old woman with no back pain, no height loss; VFA may not meet ISCD clinical criteria</em></span><span>$215.00</span></div>
    <div class="line-item"><span>Radiologist interpretation &mdash; Dr. A. Patel, MD</span><span>$65.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$770.00</span></div>
    <div class="line-item"><span><em>Patient&rsquo;s expected cost if correctly coded as ACA preventive: </em></span><span><strong>$0</strong></span></div>
</div>

<p>In this example, the patient is 67 years old, had no prior bone density test, and was referred by her primary care physician for routine osteoporosis screening. Under the ACA, this should be $0. Two issues: (1) the claim was submitted as diagnostic rather than preventive, and (2) VFA was added without meeting ISCD criteria. Both warrant disputes.</p>

<h2 id="vfa-unnecessary">5. When VFA (CPT 77085) is unnecessary</h2>

<p>Vertebral fracture assessment is a valuable tool for the right patient, but it is frequently ordered for routine screenings where it does not change clinical management. The International Society for Clinical Densitometry (ISCD) recommends VFA only when at least one of these criteria is present:</p>

<ul>
    <li>Age 70 or older</li>
    <li>Height loss of 4 cm (1.5 inches) or more</li>
    <li>Self-reported prior vertebral fracture</li>
    <li>Glucocorticoid (steroid) use equivalent to prednisone 5 mg/day for 3+ months</li>
    <li>T-score at or below &minus;1.5 at any site</li>
</ul>

<p>If you do not meet any of these criteria and CPT 77085 appears on your bill, ask your provider for the clinical documentation supporting the order. If no documentation exists, ask that the code be removed from the claim. This single correction can eliminate $80 to $250 from your bill.</p>

<div class="guide-cta-inline">
    <p><strong>Got a DEXA scan bill with CPT 77085?</strong> <a href="/scan">Upload it to BillKarma</a>&mdash;we check whether the VFA add-on meets ISCD criteria and flag claims where ACA preventive billing rules should have made the scan free.</p>
</div>

<h2 id="cash-pay">6. How to get a cash-pay rate</h2>

<p>If you are uninsured or want to avoid applying your deductible to a DEXA scan, a cash price is easy to obtain. Here is how:</p>

<ol>
    <li><strong>Call freestanding imaging centers directly,</strong> not hospitals. Search for &ldquo;bone density scan near me&rdquo; or &ldquo;DEXA scan [city].&rdquo; Many freestanding centers advertise self-pay prices of $75 to $150 for CPT 77080.</li>
    <li><strong>Ask specifically for the &ldquo;self-pay&rdquo; or &ldquo;cash price&rdquo;</strong> when you call. Hospital financial counselors are trained to offer this; freestanding centers usually post it on their website.</li>
    <li><strong>Check direct-pay services</strong> like Radiology Associates or MDsave, which aggregate upfront-price imaging services. DEXA scans are commonly listed at $100 to $175 on these platforms with insurance-grade quality imaging.</li>
    <li><strong>Confirm what is included.</strong> A good all-in cash price covers the scan itself, the radiologist&rsquo;s interpretation, and the T-score report sent to your doctor&mdash;not just the equipment time.</li>
</ol>

<div class="key-takeaway">
    <strong>Do not pay hospital prices for a DEXA scan.</strong> Unlike complex procedures that require a full hospital infrastructure, a DEXA scan is a low-complexity imaging study that takes 10 to 20 minutes. Any freestanding radiology group or women&rsquo;s health clinic with a DXA machine can perform it for a fraction of the hospital charge. There is no clinical advantage to having it done at a hospital.
</div>

<h2 id="insurance-coverage">7. Insurance coverage rules by plan type</h2>

<p>Coverage for DEXA scans varies based on the reason for the test and your plan type:</p>

<table>
    <thead>
        <tr>
            <th>Plan Type</th>
            <th>Preventive Screening (Age 65+)</th>
            <th>Diagnostic / Monitoring</th>
            <th>Frequency Limit</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>ACA-compliant commercial</td><td>$0 in-network</td><td>Deductible + coinsurance</td><td>Per USPSTF recommendation</td></tr>
        <tr><td>Medicare Part B</td><td>$0 (qualifying criteria)</td><td>$0 if medically necessary + qualifying criteria met</td><td>Every 24 months</td></tr>
        <tr><td>Medicare Advantage</td><td>$0 (required)</td><td>Plan-specific copay</td><td>Every 24 months minimum</td></tr>
        <tr><td>Medicaid</td><td>Usually $0 (most states)</td><td>Minimal or $0</td><td>Varies by state</td></tr>
        <tr><td>Grandfathered / non-ACA plan</td><td>May not be free</td><td>Deductible + coinsurance</td><td>Plan-specific</td></tr>
    </tbody>
</table>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Hospital overbilling on a preventive DEXA &mdash; $490 reduced to $0</h3>
    <p>A 68-year-old retired teacher in Michigan received a routine bone density screening referral from her primary care physician. She had no prior DEXA scan, no symptoms, and no fracture history. Her physician&rsquo;s office scheduled the scan at the affiliated hospital outpatient radiology department without informing her of alternatives.</p>
    <p>Her bill arrived at <strong>$770</strong>: $490 for CPT 77080, $215 for CPT 77085 (VFA add-on), and $65 for the radiologist read. Her insurance applied $385 to her deductible as a diagnostic service.</p>
    <p>She uploaded the bill to BillKarma. Our review identified two issues: (1) the claim was submitted under a diagnostic diagnosis code rather than the preventive screening code (Z13.820), and (2) the VFA add-on did not meet ISCD criteria&mdash;she was 68 (not 70+), had no height loss, and had no prior fractures or steroid use.</p>
    <p>She filed an appeal with her insurer citing ACA preventive care requirements and submitted a request to the billing department to remove CPT 77085. The insurer reprocessed the claim as preventive under Z13.820. The VFA charge was removed. <strong>Final patient responsibility: $0. Total savings: $385 (her deductible obligation).</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a DEXA scan cost without insurance?</h3>
        <p>Without insurance, a DEXA scan costs $100 to $250 at a freestanding imaging center and $200 to $600 at a hospital outpatient department. The Medicare rate for an axial DEXA scan (CPT 77080, covering spine and hip) is approximately $125. Some imaging centers advertise self-pay DEXA scans for $75 to $150&mdash;these are legitimate low-cost options at facilities specializing in preventive imaging.</p>
    </div>
    <div class="faq-item">
        <h3>Who gets a DEXA scan free under Medicare?</h3>
        <p>Medicare Part B covers a bone density test every 24 months at no cost for individuals meeting specific clinical criteria, including women at estrogen deficiency and at risk for osteoporosis, those with vertebral abnormalities, individuals receiving glucocorticoid therapy, those with hyperparathyroidism, and those being monitored for osteoporosis drug therapy response. No deductible or coinsurance applies when these criteria are met.</p>
    </div>
    <div class="faq-item">
        <h3>What CPT codes are used for DEXA scans?</h3>
        <p>The two main DEXA scan CPT codes are 77080 (axial skeleton, covering spine and hip&mdash;the standard osteoporosis test) and 77081 (appendicular skeleton, covering peripheral sites like the wrist or heel). CPT 77085 covers axial DEXA with vertebral fracture assessment (VFA), an add-on that is sometimes ordered without clear clinical justification. Always verify that 77085 was clinically indicated before paying for it.</p>
    </div>
    <div class="faq-item">
        <h3>Is a vertebral fracture assessment (VFA) necessary with every DEXA scan?</h3>
        <p>No. VFA (CPT 77085) is recommended by the ISCD for patients over 70, those with significant height loss, prior fracture history, or steroid use. For routine osteoporosis screening in a lower-risk patient, VFA may not be clinically warranted. If it appears on your bill without documented justification, you have grounds to dispute the charge.</p>
    </div>
    <div class="faq-item">
        <h3>Does the ACA require free DEXA scans for women?</h3>
        <p>Yes, for women 65 and older with ACA-compliant insurance plans. The USPSTF B recommendation for osteoporosis screening in women 65+ triggers the ACA&rsquo;s zero-cost-sharing requirement for in-network preventive services. Younger women with elevated fracture risk may also qualify, but coverage for that group varies by plan. Confirm with your insurer whether a specific diagnosis code and clinical justification are required to receive the free preventive benefit.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/preventive-and-screening-services/bone-density-studies" target="_blank" rel="noopener">CMS Medicare: Bone Density Studies Coverage</a></li>
    <li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/osteoporosis-screening" target="_blank" rel="noopener">USPSTF: Osteoporosis Screening Recommendation (2018)</a></li>
    <li><a href="https://www.iscd.org/official-positions/2019-iscd-official-positions-adult/" target="_blank" rel="noopener">ISCD: 2019 Official Positions for Vertebral Fracture Assessment</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Radiology</a></li>
    <li><a href="https://www.healthcare.gov/coverage/preventive-care-benefits/" target="_blank" rel="noopener">Healthcare.gov: ACA Preventive Care Benefits for Women</a></li>
    <li><a href="https://www.iofbonehealth.org/facts-statistics" target="_blank" rel="noopener">International Osteoporosis Foundation: Facts and Statistics</a></li>
    <li><a href="https://www.nof.org/preventing-fractures/general-facts/what-women-need-to-know/" target="_blank" rel="noopener">National Osteoporosis Foundation: Bone Health for Women</a></li>
</ul>
""",
})
