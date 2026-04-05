"""Guide: Ultrasound Cost."""

from guides import register, _embed

register("ultrasound-cost", {
    "title": "How Much Does an Ultrasound Cost in 2026?",
    "meta_description": "Ultrasound costs range from $200 to $3,000+ depending on type and location. See what you should pay with and without insurance, common CPT codes, and how to spot billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does an ultrasound cost without insurance?",
            "a": "Without insurance, an ultrasound typically costs $200&ndash;$1,000 for common types like abdominal, pelvic, or obstetric scans. More specialized studies like a Doppler vascular ultrasound run $400&ndash;$1,000, and an echocardiogram (cardiac ultrasound) can cost $1,000&ndash;$3,000 or more. Freestanding imaging centers are significantly cheaper than hospital radiology departments for the same procedure.",
        },
        {
            "q": "Is an ultrasound covered by insurance?",
            "a": "Most health insurance plans cover medically necessary ultrasounds. After applying your deductible and coinsurance, out-of-pocket costs are typically $50&ndash;$300. First-trimester pregnancy ultrasounds are often covered at $0 under the ACA as preventive care. Cosmetic 3D/4D ultrasounds are generally not covered. Medicare Part B covers medically necessary ultrasounds at 80% after the deductible.",
        },
        {
            "q": "Why did I get two separate bills for my ultrasound?",
            "a": "Ultrasound billing almost always generates two separate charges: a facility fee (for the use of the equipment, room, and technician) and a professional fee (for the radiologist who interprets the images). These are billed separately under different CPT codes and may come from different providers. Both are legitimate charges, but both should be checked for accuracy.",
        },
        {
            "q": "What are common CPT codes for ultrasounds?",
            "a": "Common ultrasound CPT codes include: 76700 (abdominal ultrasound, complete), 76705 (abdominal ultrasound, limited), 76805 (obstetric ultrasound, after first trimester, complete), 76536 (thyroid/neck ultrasound), 76856 (pelvic ultrasound, complete), 76641/76642 (breast ultrasound), 93306 (echocardiogram, complete), and 76942 (ultrasound guidance for a procedure, billed separately). Always verify that the code on your bill matches the exam you actually received.",
        },
        {
            "q": "Is a 3D or 4D ultrasound covered by insurance?",
            "a": "Generally no. 3D and 4D ultrasounds are considered cosmetic or elective when performed outside of a specific clinical indication. If your provider orders a 3D/4D scan for a medical reason (e.g., evaluating a fetal abnormality), it may be covered. If it is a &ldquo;keepsake&rdquo; or elective session at a commercial studio, it will not be covered and the full cost is your responsibility.",
        },
    ],
    "body": f"""
<p class="lead">Ultrasounds are one of the most commonly ordered diagnostic imaging tests in medicine&mdash;and one of the most frequently misbilled. Radiology billing errors affect <strong>31% of imaging claims</strong>, according to BillKarma data. Costs range from under $200 at a freestanding imaging center to over $3,000 for a cardiac echocardiogram at a hospital. Here is what you should actually pay, how to read your bill, and the specific errors to look for.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Quick answer:</strong> A standard abdominal or pelvic ultrasound costs $300&ndash;$700 without insurance at a hospital, or $150&ndash;$400 at a freestanding imaging center. With insurance, most patients pay $50&ndash;$300 after deductible and coinsurance. Always expect two separate bills: one for the facility and one for the radiologist who reads the images.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#costs-by-type">Costs by ultrasound type</a></li>
        <li><a href="#facility-vs-imaging">Hospital vs. freestanding imaging center</a></li>
        <li><a href="#two-bills">Why you get two bills</a></li>
        <li><a href="#pregnancy-ultrasound">Pregnancy ultrasounds and ACA coverage</a></li>
        <li><a href="#medicare-coverage">Medicare coverage for ultrasounds</a></li>
        <li><a href="#cpt-codes">CPT codes and how to read your bill</a></li>
        <li><a href="#billing-errors">Common billing errors to catch</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="costs-by-type">1. Costs by ultrasound type</h2>

<p>Ultrasound costs vary significantly by the type of study ordered. The following ranges reflect self-pay (no insurance) prices across the U.S. in 2026. Prices at hospital radiology departments are typically 2&ndash;3&times; higher than freestanding imaging centers for the same study.</p>

<table>
    <thead>
        <tr><th>Ultrasound Type</th><th>Self-Pay Cost (Hospital)</th><th>Self-Pay Cost (Imaging Center)</th><th>Primary CPT Code</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Abdominal (complete)</strong></td><td>$400&ndash;$700</td><td>$150&ndash;$300</td><td>76700</td></tr>
        <tr><td><strong>Abdominal (limited)</strong></td><td>$250&ndash;$450</td><td>$100&ndash;$200</td><td>76705</td></tr>
        <tr><td><strong>Pelvic</strong></td><td>$300&ndash;$550</td><td>$130&ndash;$280</td><td>76856</td></tr>
        <tr><td><strong>Obstetric (standard)</strong></td><td>$300&ndash;$500</td><td>$150&ndash;$350</td><td>76805</td></tr>
        <tr><td><strong>Thyroid / neck</strong></td><td>$250&ndash;$450</td><td>$120&ndash;$250</td><td>76536</td></tr>
        <tr><td><strong>Breast</strong></td><td>$300&ndash;$600</td><td>$150&ndash;$350</td><td>76641</td></tr>
        <tr><td><strong>Doppler / vascular</strong></td><td>$500&ndash;$1,000</td><td>$200&ndash;$500</td><td>93971</td></tr>
        <tr><td><strong>Echocardiogram (cardiac)</strong></td><td>$1,200&ndash;$3,000</td><td>$500&ndash;$1,200</td><td>93306</td></tr>
    </tbody>
</table>

<p><em>Note: These are facility fees only. Add $80&ndash;$250 for the radiologist&rsquo;s interpretation fee, billed separately.</em></p>

<p>With insurance, most patients pay their standard outpatient coinsurance (typically 10&ndash;30%) after meeting their deductible. For a $500 ultrasound on a plan with a $2,000 deductible (not yet met), you would pay the full $500. If your deductible is already met, you would pay $50&ndash;$150 in coinsurance for the same study.</p>

{_embed(mode="cost", cpt="76700", title="Look up ultrasound pricing", subtitle="See what Medicare pays for common imaging procedures in your area.")}

<h2 id="facility-vs-imaging">2. Hospital vs. freestanding imaging center</h2>

<p>Where you get your ultrasound matters as much as what kind you need. The same CPT code billed at a hospital outpatient department vs. a freestanding imaging center can result in costs that are 2&ndash;4 times higher at the hospital&mdash;for identical services.</p>

<p><strong>Why?</strong> Hospital outpatient departments add a facility fee on top of the professional fee. This is sometimes called the &ldquo;hospital outpatient department (HOPD) surcharge.&rdquo; Freestanding imaging centers operate on leaner cost structures and are not reimbursed at hospital rates by Medicare or insurers.</p>

<div class="key-takeaway">
    <strong>If your doctor refers you to a hospital-affiliated radiology department</strong>, ask whether a freestanding imaging center is an option and whether they accept your insurance. For routine ultrasounds (abdominal, pelvic, thyroid), the quality is equivalent at an independent imaging center and the savings can be $200&ndash;$600 out of pocket.
</div>

<p>One important caveat: if your ultrasound requires immediate physician follow-up (e.g., a suspicious mass that may require same-day biopsy), having it done within a hospital system has logistical advantages. For straightforward diagnostic studies, a freestanding center is almost always the lower-cost choice.</p>

<h2 id="two-bills">3. Why you get two bills</h2>

<p>Nearly every ultrasound generates two separate bills:</p>

<ol>
    <li><strong>Facility fee:</strong> Charged by the hospital or imaging center for the room, equipment, ultrasound technician (sonographer), and supplies. This is the larger of the two charges.</li>
    <li><strong>Professional fee (interpretation fee):</strong> Charged separately by the radiologist who reviews the images and writes a diagnostic report. This may come from a different billing entity than the facility&mdash;often a radiology group that contracts with the hospital&mdash;and can arrive as a separate bill weeks after the facility bill.</li>
</ol>

<p>Both charges are legitimate. The problem arises when patients pay the facility bill and assume they are done, then receive the radiologist&rsquo;s bill unexpectedly. If you received an ultrasound and have only seen one bill, check your insurance EOB&mdash;a second professional fee claim may already have been processed.</p>

<h2 id="pregnancy-ultrasound">4. Pregnancy ultrasounds and ACA coverage</h2>

<p>Pregnancy ultrasounds occupy a unique place in insurance coverage law:</p>

<p><strong>First-trimester ultrasound:</strong> Under the ACA, the first-trimester ultrasound is generally classified as a preventive service and must be covered at <strong>$0 cost-sharing</strong> (no copay, no deductible) on non-grandfathered plans. This typically covers one standard ultrasound confirming pregnancy and estimated due date.</p>

<p><strong>20-week anatomy scan (CPT 76805):</strong> This standard mid-pregnancy scan is covered as a medically necessary prenatal service on most plans, but it may be subject to your deductible and coinsurance rather than $0 preventive coverage. Check your plan documents.</p>

<p><strong>Additional ultrasounds:</strong> Ultrasounds ordered for specific clinical reasons (monitoring high-risk pregnancy, assessing fetal growth, evaluating abnormalities) are covered as medically necessary. The number covered depends on your plan and clinical indication.</p>

<p><strong>3D/4D &ldquo;keepsake&rdquo; ultrasounds:</strong> Not covered by any insurance plan. These are elective cosmetic sessions typically offered at commercial studios, not covered by medical insurance. Costs range from $100&ndash;$300 for a session. The FDA has advised against non-medical 3D/4D ultrasounds due to unnecessary fetal exposure.</p>

<h2 id="medicare-coverage">5. Medicare coverage for ultrasounds</h2>

<p>Medicare Part B covers ultrasounds that are medically necessary and ordered by your physician. Coverage rules:</p>

<ul>
    <li>You pay the Part B deductible ($257 in 2026) if not yet met, then 20% coinsurance.</li>
    <li>Medicare pays 80% of the approved amount to the provider.</li>
    <li>If you have Medicare Supplement (Medigap) insurance, your coinsurance may be covered, reducing your cost to near $0.</li>
    <li>Medicare Advantage plans cover ultrasounds under their outpatient benefit, typically with a fixed copay.</li>
    <li>Abdominal aortic aneurysm (AAA) screening ultrasound: covered once at $0 for qualifying beneficiaries (men 65&ndash;75 who ever smoked, and certain others).</li>
</ul>

<p>Medicare does not cover 3D/4D ultrasounds or ultrasounds performed without a physician order. If you are on Medicare and receive a bill for an ultrasound you believe is covered, compare the bill to your Medicare Summary Notice to verify the allowed amount and your share.</p>

<h2 id="cpt-codes">6. CPT codes and how to read your bill</h2>

<p>Every ultrasound has a specific Current Procedural Terminology (CPT) code. The code on your bill determines what your insurance pays. Verify that the code matches the exam you actually received&mdash;upcoding (billing a more expensive code than performed) is the most common radiology billing error.</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Medicare Approx. Rate (2026)</th></tr>
    </thead>
    <tbody>
        <tr><td>76700</td><td>Abdominal ultrasound, complete</td><td>$165&ndash;$220</td></tr>
        <tr><td>76705</td><td>Abdominal ultrasound, limited</td><td>$95&ndash;$130</td></tr>
        <tr><td>76805</td><td>Obstetric ultrasound, after first trimester, complete</td><td>$140&ndash;$195</td></tr>
        <tr><td>76536</td><td>Thyroid / neck soft tissue ultrasound</td><td>$120&ndash;$160</td></tr>
        <tr><td>76856</td><td>Pelvic ultrasound, complete</td><td>$130&ndash;$175</td></tr>
        <tr><td>76641</td><td>Breast ultrasound, complete</td><td>$130&ndash;$170</td></tr>
        <tr><td>76942</td><td>Ultrasound guidance for a procedure</td><td>$100&ndash;$145</td></tr>
        <tr><td>93306</td><td>Echocardiogram, complete with Doppler</td><td>$480&ndash;$650</td></tr>
    </tbody>
</table>

<p><strong>Complete vs. limited:</strong> A &ldquo;complete&rdquo; ultrasound (e.g., 76700) examines the entire organ system. A &ldquo;limited&rdquo; ultrasound (e.g., 76705) examines a specific area or answers a specific question. Complete exams are reimbursed at a higher rate. If the technician only examined one quadrant but the bill says 76700 (complete), that is upcoding.</p>

<h2 id="billing-errors">7. Common billing errors to catch</h2>

<p>BillKarma data shows that 31% of imaging claims contain at least one billable error. The most common ultrasound billing errors are:</p>

<ol>
    <li><strong>Upcoding complete vs. limited exam.</strong> A limited ultrasound (e.g., 76705) is billed as a complete study (76700) to capture higher reimbursement. Ask your sonographer or the ordering physician whether a complete or limited exam was ordered and performed.</li>
    <li><strong>Billing ultrasound guidance separately when it is bundled.</strong> CPT 76942 (ultrasound guidance) is sometimes billed as a separate charge when it is already included in another procedure code (e.g., amniocentesis, biopsy) per NCCI bundling rules. If you see 76942 on a bill alongside a biopsy or injection code, verify it is not already included.</li>
    <li><strong>Duplicate billing of facility and professional fees under one code.</strong> Some facilities accidentally bill the interpretation fee under the facility code, and then the radiologist group bills again. Review your EOB to see if two separate claims were submitted for the same service with overlapping dates of service.</li>
    <li><strong>Wrong body part or wrong laterality.</strong> A right breast ultrasound billed as bilateral (76641 vs. 76642) doubles the charge. Verify the code matches the body part actually imaged.</li>
    <li><strong>3D add-on code billed without a 2D base exam.</strong> Some billers add 3D reconstruction codes on top of standard 2D ultrasound codes without performing the additional imaging. These add-on codes should only appear when the enhanced imaging was actually performed and documented.</li>
</ol>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;padding:1.25rem 1.5rem;margin:2rem 0;border-radius:6px;">
    <strong>Got an ultrasound bill that looks wrong?</strong> <a href="/fight-debt">Upload it to BillKarma</a> and we&rsquo;ll check the CPT codes, spot upcoding, identify duplicate charges, and generate a dispute letter if we find errors.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an ultrasound cost without insurance?</h3>
        <p>Without insurance, common ultrasounds cost $200&ndash;$1,000 at a hospital radiology department and $100&ndash;$500 at a freestanding imaging center. Echocardiograms run $1,000&ndash;$3,000. Always ask for the self-pay rate before your appointment&mdash;many facilities offer 20&ndash;40% discounts for cash-pay patients.</p>
    </div>

    <div class="faq-item">
        <h3>Is an ultrasound covered by insurance?</h3>
        <p>Yes, when medically necessary. With insurance, out-of-pocket costs are typically $50&ndash;$300 after deductible and coinsurance. First-trimester pregnancy ultrasounds are often $0 under the ACA. Cosmetic 3D/4D ultrasounds are not covered.</p>
    </div>

    <div class="faq-item">
        <h3>Why did I get two separate bills for my ultrasound?</h3>
        <p>One bill is from the facility (equipment, technician, room). The other is from the radiologist who interpreted the images. Both are standard and expected. Both can contain errors, so review each against your EOB.</p>
    </div>

    <div class="faq-item">
        <h3>What CPT codes are used for ultrasounds?</h3>
        <p>Common codes: 76700 (abdominal complete), 76705 (abdominal limited), 76805 (obstetric), 76536 (thyroid), 76856 (pelvic), 93306 (echocardiogram), 76942 (ultrasound guidance). Verify the code on your bill matches the exam you received.</p>
    </div>

    <div class="faq-item">
        <h3>Is a 3D or 4D ultrasound covered by insurance?</h3>
        <p>Generally no. 3D/4D ultrasounds are classified as cosmetic or elective unless there is a specific clinical indication. Keepsake ultrasound studios are not covered by any insurance plan.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: 2026 Medicare Physician Fee Schedule</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Institute of Ultrasound in Medicine (AIUM): Practice Guidelines for Ultrasound</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: National Correct Coding Initiative (NCCI) Policy Manual</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Preventive Care Benefits for Women</a></li>
    <li><a href="#" target="_blank" rel="noopener">FDA: Ultrasound Imaging &mdash; Safety Information for Patients</a></li>
    <li><a href="#" target="_blank" rel="noopener">RAND Corporation: Prices Paid to Hospitals by Private Health Plans (2024)</a></li>
</ul>
""",
})
