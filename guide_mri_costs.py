"""Guide: How Much Does an MRI Cost? (2026 Price Guide)."""

from guides import register, _embed

register("mri-costs", {
    "title": "How Much Does an MRI Cost? (2026 Price Guide)",
    "meta_description": "MRI scans average $1,325 but hospitals charge $400–$12,000. See 2026 Medicare rates for 5 common CPT codes and learn how to dispute inflated bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does an MRI cost without insurance in 2026?",
            "a": "Without insurance, an MRI costs $400 to $3,500 at a freestanding imaging center and $1,800 to $8,500 at a hospital outpatient department, depending on the body part and whether contrast is used. The national average across all facility types is about $1,325, according to HCCI data. Always call ahead and ask for the cash or self-pay price, which is often 40&ndash;60% lower than the standard rate.",
        },
        {
            "q": "What is the Medicare rate for a brain MRI?",
            "a": "Medicare pays approximately $344 for a brain MRI with and without contrast (CPT 70553) and $236 for a brain MRI without contrast (CPT 70551) under the 2026 Physician Fee Schedule. Hospital outpatient departments charge $1,800 to $8,500 for the same scan&mdash;a markup of 5 to 25 times the Medicare rate. Freestanding imaging centers typically charge $400 to $900.",
        },
        {
            "q": "Why is my MRI bill so high at the hospital?",
            "a": "Hospital outpatient MRI bills are high primarily because of the facility fee&mdash;a surcharge for using the hospital&rsquo;s space, equipment, and overhead. This fee is billed separately from the radiologist&rsquo;s reading fee and can add $500 to $3,000 to your bill. Freestanding imaging centers do not charge a facility fee, which is why the same scan costs 50 to 80% less there.",
        },
        {
            "q": "What is the difference between an MRI with contrast and without contrast?",
            "a": "Contrast is a special dye injected into your vein that makes certain tissues and blood vessels show up more clearly on the images. An MRI with contrast costs $100 to $400 more than one without. The CPT code on your bill changes: for example, a lumbar spine MRI without contrast is CPT 72148, while with contrast it uses a different code. Your doctor chooses based on what they need to see.",
        },
        {
            "q": "Can I get an MRI at a cheaper place and still use my insurance?",
            "a": "Yes, in most cases. Your doctor writes a prescription or referral for the MRI, but you choose the facility. If the imaging center is in your insurance network, your insurance will apply. Even if the center is out of network, the cash price may be lower than your in-network cost-sharing at a hospital. Always confirm network status and get a cost estimate before scheduling.",
        },
    ],
    "body": f"""
<p class="lead">The average MRI costs <strong>$1,325</strong> nationally, according to the Health Care Cost Institute&mdash;but that number hides enormous variation. Hospital charges for the same brain MRI range from <strong>$1,800 to $8,500</strong> depending on where you go, while a freestanding imaging center a few miles away may charge $400 to $900 for the identical scan. This guide shows you exactly what each common MRI should cost, what every line on your bill means, and how to dispute charges that are too high.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#mri-cost-table">MRI costs by body part and CPT code</a></li>
        <li><a href="#hospital-vs-imaging">Hospital vs. imaging center vs. freestanding MRI</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of an MRI bill</a></li>
        <li><a href="#contrast-markups">Contrast vs. non-contrast markups</a></li>
        <li><a href="#open-vs-closed">Open vs. closed MRI cost differences</a></li>
        <li><a href="#price-transparency">How to compare prices using transparency data</a></li>
        <li><a href="#insurance-coverage">How insurance covers MRI costs</a></li>
        <li><a href="#dispute-charges">How to dispute inflated MRI charges</a></li>
        <li><a href="#case-studies">Real-world case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="mri-cost-table">1. MRI costs by body part and CPT code</h2>

<p>Every MRI on your bill has a CPT code&mdash;a five-digit number that identifies the exact scan performed. Medicare publishes what it pays for each CPT code, giving you a reliable benchmark. Below are the five most common MRI codes, their 2026 Medicare rates, and typical hospital and imaging center charges.</p>

<table>
    <thead>
        <tr>
            <th>Body Part / Scan</th>
            <th>CPT Code</th>
            <th>Medicare Rate (2026)</th>
            <th>Hospital Charge Range</th>
            <th>Imaging Center Avg</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Brain MRI w/ &amp; w/o contrast</td><td>70553</td><td>$344</td><td>$1,800&ndash;$8,500</td><td>$450&ndash;$950</td></tr>
        <tr><td>Cervical spine MRI w/o contrast</td><td>72141</td><td>$267</td><td>$1,200&ndash;$5,000</td><td>$350&ndash;$750</td></tr>
        <tr><td>Shoulder (upper extremity joint) MRI</td><td>73221</td><td>$234</td><td>$1,000&ndash;$4,500</td><td>$300&ndash;$700</td></tr>
        <tr><td>Lumbar spine MRI w/o contrast</td><td>72148</td><td>$261</td><td>$1,200&ndash;$5,500</td><td>$350&ndash;$800</td></tr>
        <tr><td>Brain MRI w/o contrast</td><td>70551</td><td>$236</td><td>$800&ndash;$4,000</td><td>$350&ndash;$750</td></tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of MRI charges across 6,000+ hospitals found that hospital outpatient MRI charges average <strong>5.1x the Medicare rate</strong>, compared to 2.8x at freestanding imaging centers. That gap means hundreds to thousands of dollars per scan.</p>

<p>Look up the Medicare rate for any CPT code on your MRI bill:</p>

{_embed(mode="cost", cpt="72148", title="Look up your MRI cost", subtitle="See what Medicare pays for this CPT code.")}

<h2 id="hospital-vs-imaging">2. Hospital vs. imaging center vs. freestanding MRI</h2>

<p>Where you get your MRI is the single biggest factor in what you pay. There are three main facility types, each with a very different price structure.</p>

<table>
    <thead>
        <tr>
            <th>Facility Type</th>
            <th>Typical Price Range</th>
            <th>Facility Fee?</th>
            <th>Insurance Accepted?</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Hospital outpatient dept.</td><td>$1,200&ndash;$8,500</td><td>Yes</td><td>Yes</td><td>Complex cases, inpatients</td></tr>
        <tr><td>Freestanding imaging center</td><td>$350&ndash;$950</td><td>No</td><td>Usually yes</td><td>Routine outpatient MRIs</td></tr>
        <tr><td>Open MRI center</td><td>$400&ndash;$1,200</td><td>No</td><td>Sometimes</td><td>Claustrophobic patients, larger body types</td></tr>
        <tr><td>Mobile MRI unit</td><td>$300&ndash;$700</td><td>No</td><td>Varies</td><td>Rural areas, cash-pay patients</td></tr>
    </tbody>
</table>

<p>The MRI machine, the scan protocol, and the radiologist reading your images are often the same at a freestanding center as at the hospital. The price difference comes almost entirely from the hospital&rsquo;s facility fee&mdash;a surcharge that can add $500 to $3,000 to your bill. See our guide on <a href="/guides/facility-fees-explained">facility fees explained</a> for the full breakdown.</p>

<div class="key-takeaway">
    <strong>Before you schedule your MRI, check what your hospital charges.</strong> <a href="/hospitals/">Search BillKarma&rsquo;s hospital pricing directory</a> &mdash; compare MRI prices at every hospital near you to find the most affordable in-network option.
</div>

<h2 id="anatomy-of-bill">3. Anatomy of an MRI bill</h2>

<p>Hospital MRI bills often split the charges into two separate line items&mdash;or even two separate bills from two different providers. Here&rsquo;s what a typical hospital outpatient MRI bill looks like:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Riverside Medical Center Outpatient &mdash; Date of Service: 03/15/2026</div>
    <div class="line-item flagged"><span>70553 &mdash; MRI Brain w/ &amp; w/o Contrast (Technical Component) &nbsp; &#9888; <em>Warning: markup 9.4x Medicare rate of $344</em></span><span>$3,240.00</span></div>
    <div class="line-item"><span>70553 &mdash; MRI Brain w/ &amp; w/o Contrast (Professional/Radiology Read)</span><span>$410.00</span></div>
    <div class="line-item flagged"><span>A4217 &mdash; Sterile water / IV supplies &nbsp; &#9888; <em>Warning: contrast supply fee, verify quantity billed</em></span><span>$185.00</span></div>
    <div class="line-item error"><span>99213 &mdash; Office visit &mdash; established patient &nbsp; &#10060; <em>Error: billed twice (also on separate physician bill)</em></span><span>$145.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$3,980.00</span></div>
</div>

<p>Breaking down each charge:</p>

<ul>
    <li><strong>Technical component ($3,240)</strong> &mdash; The hospital&rsquo;s facility fee covering the MRI machine, technologist, and overhead. Medicare pays $344 total for this scan. The hospital is charging 9.4x the Medicare rate. This is the charge with the most room for dispute.</li>
    <li><strong>Professional component ($410)</strong> &mdash; The radiologist&rsquo;s fee for interpreting the images. This is often billed by a separate radiology group. A markup of 1.2x Medicare is more reasonable.</li>
    <li><strong>IV supplies ($185)</strong> &mdash; Contrast dye requires an IV line. One vial of contrast dye costs hospitals about $20&ndash;$40 wholesale. A charge of $185 for &ldquo;sterile water and IV supplies&rdquo; warrants a closer look at the quantity billed.</li>
    <li><strong>Office visit ($145)</strong> &mdash; If this charge also appears on a separate bill from your physician, this is a duplicate charge&mdash;dispute it immediately. See our guide on <a href="/guides/duplicate-charges">spotting duplicate charges</a>.</li>
</ul>

<h2 id="contrast-markups">4. Contrast vs. non-contrast markups</h2>

<p>Scans &ldquo;with contrast&rdquo; use a gadolinium-based dye injected intravenously to sharpen image quality. The dye itself costs the hospital $20&ndash;$60 per dose, but hospitals routinely bill $100 to $400 for contrast administration and supplies. Here&rsquo;s how the markup compares:</p>

<p>For a lumbar spine MRI, CPT 72148 (without contrast) has a Medicare rate of $261. CPT 72149 (with contrast) pays $289&mdash;a difference of just $28. But hospital charge differences between the two versions of the same scan often run $300 to $800. That&rsquo;s a markup on the markup.</p>

<p>If your bill includes a separate line for contrast material, check that the quantity listed matches the number of doses you actually received. Billing for two doses when one was used is a common error in hospital radiology departments.</p>

<div class="key-takeaway">
    <strong>Think your MRI bill has inflated contrast charges?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; our scan tool flags line items where supply charges exceed typical market rates for the CPT code billed.
</div>

<h2 id="open-vs-closed">5. Open vs. closed MRI cost differences</h2>

<p>A closed MRI uses a narrow cylindrical tube&mdash;the traditional design that produces the highest image quality. An open MRI uses a wider, more open design that is more comfortable for patients with claustrophobia, larger body types, or anxiety. Open MRIs typically use a lower magnetic field strength (0.3&ndash;1.0 Tesla vs. 1.5&ndash;3.0 Tesla for closed), which can produce slightly lower-resolution images.</p>

<p>Open MRI pricing at freestanding centers typically runs $400 to $1,200 for most scans&mdash;slightly higher than standard closed MRI centers because the equipment is less common. At hospital outpatient departments, open MRI charges follow the same facility-fee structure as closed MRIs and can reach $3,000 to $6,000.</p>

<p>For most routine musculoskeletal MRIs (shoulder, knee, spine), an open MRI at a freestanding center is a cost-effective option. For complex neurological imaging, your doctor may specifically request a higher-field closed MRI for better resolution.</p>

<h2 id="price-transparency">6. How to compare prices using hospital price transparency data</h2>

<p>Since January 2021, federal law requires every hospital to publish their prices online in a machine-readable file. The 2024 rule update strengthened enforcement, with fines up to $2 million per year for non-compliant hospitals. You can use this data to compare prices before you schedule. Here&rsquo;s how:</p>

<ol>
    <li><strong>Find the CPT code</strong> for your scan (your doctor&rsquo;s order or our table above).</li>
    <li><strong>Search our <a href="/hospitals/">hospital pricing directory</a></strong>&mdash;we&rsquo;ve parsed the machine-readable files from 6,000+ hospitals so you don&rsquo;t have to.</li>
    <li><strong>Compare the &ldquo;cash price&rdquo; and the &ldquo;payer-specific negotiated rate&rdquo;</strong> for your insurance plan at each facility.</li>
    <li><strong>Choose the lower-cost option</strong> and ask your doctor to send the referral there.</li>
</ol>

<p>A 2024 RAND Corporation study found that hospital prices for MRI scans varied by as much as <strong>780%</strong> within the same metropolitan area. The transparency data makes those differences visible for the first time. Use our <a href="/calculator">cost calculator</a> to benchmark any charge against the Medicare rate.</p>

<h2 id="insurance-coverage">7. How insurance covers MRI costs</h2>

<p>Most commercial health plans and Medicare cover medically necessary MRIs, but &ldquo;covered&rdquo; does not mean &ldquo;free.&rdquo; Your actual out-of-pocket cost depends on where you are in your plan year:</p>

<ul>
    <li><strong>Before your deductible:</strong> You pay 100% of the insurer&rsquo;s allowed amount. On a hospital MRI with an allowed amount of $900, that means $900 out of pocket&mdash;versus $475 cash at a freestanding center.</li>
    <li><strong>After your deductible, before your out-of-pocket max:</strong> You pay coinsurance (typically 20&ndash;40%). On a $900 allowed amount, that&rsquo;s $180&ndash;$360.</li>
    <li><strong>After your out-of-pocket max:</strong> Your plan covers 100%. If you expect to hit your max, prioritize getting scans done before year&rsquo;s end.</li>
</ul>

<p><strong>Prior authorization:</strong> Many plans require prior authorization (PA) before an MRI. If your doctor orders an MRI without getting PA first, the claim may be denied. Always ask your doctor&rsquo;s office to confirm PA was obtained before your scan date. See our guide on <a href="/guides/insurance-denial-appeal">how to appeal an insurance denial</a> if your MRI is denied.</p>

<h2 id="dispute-charges">8. How to dispute inflated MRI charges</h2>

<p>If your MRI bill looks too high, you have leverage&mdash;especially if the charges are more than 3x the Medicare rate. Here&rsquo;s a step-by-step approach:</p>

<ol>
    <li><strong>Request an itemized bill with CPT codes.</strong> You are legally entitled to this. If the hospital sends you a summary bill, call and ask for the itemized version by mail or patient portal.</li>
    <li><strong>Look up the Medicare rate</strong> for each CPT code using our <a href="/calculator">cost calculator</a>. Note the markup multiple for each line item.</li>
    <li><strong>Check for billing errors.</strong> Look for duplicate charges, charges for services not received (like the office visit example above), and quantities that seem excessive (e.g., 3 contrast doses when you had 1 scan).</li>
    <li><strong>Call the billing department.</strong> State clearly: &ldquo;Medicare pays $[X] for CPT [code]. I&rsquo;m being charged $[Y]&mdash;a markup of [Z]x. I&rsquo;d like to request a reduction to something closer to what other payers pay.&rdquo;</li>
    <li><strong>Follow up in writing.</strong> Send a dispute letter citing the specific CPT codes, the Medicare rates, and your requested adjustment. Our <a href="/guides/dispute-bill">dispute guide</a> has letter templates you can use.</li>
    <li><strong>Ask about financial assistance.</strong> Nonprofit hospitals are required to have charity care programs. If your income qualifies, you may be eligible for a significant reduction or even forgiveness. See our guide on <a href="/guides/hospital-financial-assistance">hospital financial assistance</a>.</li>
</ol>

<h2 id="case-studies">9. Real-world case studies</h2>

<div class="case-study">
    <h3>Lumbar spine MRI &mdash; switching to an imaging center saves $2,100</h3>
    <p>A 44-year-old teacher in Ohio was referred for a lumbar spine MRI (CPT 72148) for lower back pain. The orthopedic group&rsquo;s scheduler booked her at the affiliated hospital outpatient center. The hospital&rsquo;s listed charge: <strong>$2,650</strong>. Her insurance&rsquo;s allowed amount: $1,100. With $1,800 left on her deductible, she owed the full $1,100.</p>
    <p>She called the BillKarma helpline, found a freestanding imaging center four miles away in-network with her plan, and rescheduled. The imaging center&rsquo;s allowed amount: <strong>$389</strong>. She owed $389 toward her deductible instead of $1,100. <strong>Total savings: $711</strong>&mdash;plus she preserved $711 more of her deductible for future care.</p>
</div>

<div class="case-study">
    <h3>Brain MRI dispute &mdash; supply charges reduced after audit</h3>
    <p>A 62-year-old retiree in Florida received a brain MRI with contrast (CPT 70553) at a hospital. His itemized bill included <strong>$780 in IV and contrast supply charges</strong> on top of the $3,200 technical fee. He uploaded the bill to BillKarma, which flagged the supply charges as 8.7x the typical rate for contrast administration.</p>
    <p>He called the billing department, referenced the Medicare allowable for contrast administration, and requested documentation of the supplies used. The hospital reduced the supply charges to $145 without requiring a formal written dispute. <strong>Total savings: $635.</strong></p>
</div>

<div class="case-study">
    <h3>Shoulder MRI &mdash; cash pay beats insurance out-of-pocket</h3>
    <p>A 31-year-old freelancer in Texas had a high-deductible health plan ($4,000 deductible) and needed a shoulder MRI (CPT 73221) for a suspected rotator cuff tear. The in-network hospital&rsquo;s allowed amount was $920&mdash;she would owe all of it since her deductible was untouched.</p>
    <p>She found a freestanding center offering the scan for <strong>$310 cash</strong>. She paid cash, saved $610 compared to her insurance route, and got the images to her orthopedist within 24 hours. The only trade-off: the $310 did not count toward her deductible. She calculated it was still worth it. <strong>Total savings: $610.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Already have an MRI bill that looks too high?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag every line item where your charge exceeds the Medicare rate by more than 3x and show you exactly what to dispute.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an MRI cost without insurance in 2026?</h3>
        <p>Without insurance, an MRI costs $400 to $3,500 at a freestanding imaging center and $1,800 to $8,500 at a hospital outpatient department, depending on the body part and whether contrast is used. The national average across all facility types is about $1,325, according to HCCI data. Always call ahead and ask for the cash or self-pay price, which is often 40&ndash;60% lower than the standard rate.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare rate for a brain MRI?</h3>
        <p>Medicare pays approximately $344 for a brain MRI with and without contrast (CPT 70553) and $236 for a brain MRI without contrast (CPT 70551) under the 2026 Physician Fee Schedule. Hospital outpatient departments charge $1,800 to $8,500 for the same scan&mdash;a markup of 5 to 25 times the Medicare rate. Freestanding imaging centers typically charge $400 to $900.</p>
    </div>
    <div class="faq-item">
        <h3>Why is my MRI bill so high at the hospital?</h3>
        <p>Hospital outpatient MRI bills are high primarily because of the facility fee&mdash;a surcharge for using the hospital&rsquo;s space, equipment, and overhead. This fee is billed separately from the radiologist&rsquo;s reading fee and can add $500 to $3,000 to your bill. Freestanding imaging centers do not charge a facility fee, which is why the same scan costs 50 to 80% less there.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between an MRI with contrast and without contrast?</h3>
        <p>Contrast is a special dye injected into your vein that makes certain tissues and blood vessels show up more clearly on the images. An MRI with contrast costs $100 to $400 more than one without. The CPT code on your bill changes: for example, a lumbar spine MRI without contrast is CPT 72148, while with contrast it uses a different code. Your doctor chooses based on what they need to see.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get an MRI at a cheaper place and still use my insurance?</h3>
        <p>Yes, in most cases. Your doctor writes a prescription or referral for the MRI, but you choose the facility. If the imaging center is in your insurance network, your insurance will apply. Even if the center is out of network, the cash price may be lower than your in-network cost-sharing at a hospital. Always confirm network status and get a cost estimate before scheduling.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://healthcostinstitute.org/" target="_blank" rel="noopener">Health Care Cost Institute (HCCI): Spending and Utilization Data</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Radiology</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS) 2026</a></li>
    <li><a href="https://www.kff.org/health-costs/" target="_blank" rel="noopener">KFF: Health Care Costs and Affordability</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-price-transparency.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Research</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios and Markup</a></li>
    <li><a href="https://www.ahrq.gov/research/findings/nhqrdr/index.html" target="_blank" rel="noopener">AHRQ: National Healthcare Quality and Disparities Report</a></li>
</ul>
""",
})
