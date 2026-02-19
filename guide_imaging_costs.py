"""Guide: How Much Does an MRI or CT Scan Cost? A Complete Price Guide."""

from guides import register, _embed

register("how-much-does-mri-ct-scan-cost", {
    "title": "How Much Does an MRI or CT Scan Cost? A Complete Price Guide",
    "meta_description": "MRI scans cost $400-$3,500 and CT scans $300-$6,750 depending on where you go. Learn what drives imaging costs and 5 ways to pay less for your scan.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does an MRI cost without insurance?",
            "a": "Without insurance, an MRI costs between $400 and $3,500 depending on where you go and what body part is being scanned. The national average is about $1,325. Freestanding imaging centers typically charge $400-$900, while hospital outpatient departments charge $1,500-$4,500 for the same scan. Always ask for the cash or self-pay price, which is often 40-60% less than the listed rate.",
        },
        {
            "q": "Why is the same MRI so much cheaper at an imaging center than a hospital?",
            "a": "Hospital outpatient departments add a facility fee on top of the scan itself. This fee covers hospital overhead like 24/7 staffing, emergency readiness, and administrative costs. Freestanding imaging centers do not charge a facility fee, so their prices are typically 50-80% lower for the exact same scan on the same type of machine.",
        },
        {
            "q": "Does insurance cover MRI and CT scans?",
            "a": "Most insurance plans cover MRI and CT scans that are medically necessary, but you may still owe a significant amount. If you have not met your deductible, you could owe the full allowed amount. Even after meeting your deductible, coinsurance of 20-40% on a $2,000 scan means $400-$800 out of pocket. Always check with your insurer before scheduling and ask whether the scan requires prior authorization.",
        },
        {
            "q": "What is the difference between an MRI and a CT scan?",
            "a": "An MRI (magnetic resonance imaging) uses magnets and radio waves to create detailed images of soft tissue like muscles, ligaments, and the brain. A CT scan (computed tomography) uses X-rays to create cross-sectional images and is better for bones, bleeding, and organ injuries. Your doctor chooses based on what they need to see. MRIs generally cost more and take longer (30-60 minutes vs. 5-15 minutes for a CT).",
        },
        {
            "q": "What does 'with contrast' mean on my imaging bill?",
            "a": "Contrast is a special dye injected into your vein before or during the scan. It makes certain tissues and blood vessels show up more clearly on the images. Scans with contrast cost more because of the dye itself (typically $100-$300 extra) and the additional imaging time. The CPT code on your bill will be different for a scan with contrast vs. without.",
        },
        {
            "q": "Can I negotiate the price of an MRI or CT scan?",
            "a": "Yes. If you are paying out of pocket, call the imaging center or hospital and ask for their cash or self-pay price. Many facilities offer 30-50% discounts for upfront payment. You can also compare prices across facilities in your area, since the same MRI can vary by thousands of dollars within the same city.",
        },
    ],
    "body": f"""
<p class="lead">The average MRI costs <strong>$1,325</strong> without insurance, according to data from the Health Care Cost Institute. CT scans average around <strong>$825</strong>. But those averages hide enormous variation&mdash;the same knee MRI can cost $400 at a freestanding imaging center or $3,500 at a hospital outpatient department just a few miles away. This guide breaks down exactly what drives imaging costs, what every common scan should cost, and five concrete ways to pay less.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-drives-costs">What drives imaging costs</a></li>
        <li><a href="#mri-costs">Common MRI costs by body part</a></li>
        <li><a href="#ct-costs">Common CT scan costs</a></li>
        <li><a href="#real-bill">An actual imaging bill, annotated</a></li>
        <li><a href="#pay-less">5 ways to pay less for imaging</a></li>
        <li><a href="#case-studies">Real-world case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-drives-costs">1. What drives imaging costs</h2>

<p>Four factors determine how much you&rsquo;ll pay for an MRI or CT scan:</p>

<ul>
    <li><strong>Facility type</strong> &mdash; This is the biggest factor. Hospital outpatient departments charge a &ldquo;facility fee&rdquo; (a surcharge for using the hospital&rsquo;s space and overhead) on top of the scan itself. Freestanding imaging centers do not. The facility fee alone can add $500&ndash;$2,000 to your bill.</li>
    <li><strong>Geographic location</strong> &mdash; Medicare rates vary by region, and private prices follow the same pattern. An MRI in Manhattan can cost 2&ndash;3x more than the same scan in rural Texas.</li>
    <li><strong>With or without contrast</strong> &mdash; Contrast dye (a liquid injected into your vein to improve image clarity) adds $100&ndash;$300 to the cost. The CPT code changes when contrast is used, so you&rsquo;ll see a different code on your bill.</li>
    <li><strong>Body part</strong> &mdash; A brain MRI requires more imaging sequences and takes longer than a knee MRI, so it costs more. Scans of the abdomen and pelvis are typically the most expensive because they cover a larger area.</li>
</ul>

<p>Here&rsquo;s how the same scans compare at hospitals vs. freestanding imaging centers:</p>

<table>
    <thead>
        <tr><th>Scan</th><th>CPT Code</th><th>Hospital Outpatient</th><th>Freestanding Center</th><th>Difference</th></tr>
    </thead>
    <tbody>
        <tr><td>Brain MRI w/ contrast</td><td>70553</td><td>$2,000&ndash;$4,500</td><td>$400&ndash;$900</td><td>$1,100&ndash;$3,600</td></tr>
        <tr><td>Knee MRI w/o contrast</td><td>73721</td><td>$1,500&ndash;$3,500</td><td>$350&ndash;$800</td><td>$700&ndash;$2,700</td></tr>
        <tr><td>CT abdomen w/ contrast</td><td>74178</td><td>$1,800&ndash;$6,750</td><td>$350&ndash;$800</td><td>$1,000&ndash;$5,950</td></tr>
        <tr><td>CT chest w/ contrast</td><td>71260</td><td>$1,500&ndash;$5,000</td><td>$300&ndash;$700</td><td>$800&ndash;$4,300</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The facility matters more than the scan.</strong> The single biggest thing you can do to lower your imaging cost is to get your scan at a freestanding imaging center instead of a hospital outpatient department. The machines are the same. The radiologists reading the images often work at both locations. The only difference is the facility fee&mdash;and it can cost you thousands.
</div>

<h2 id="mri-costs">2. Common MRI costs by body part</h2>

<p>MRI (magnetic resonance imaging) uses powerful magnets and radio waves to create detailed pictures of soft tissues like muscles, ligaments, the brain, and internal organs. A typical MRI takes 30&ndash;60 minutes. Here&rsquo;s what the most common MRI scans cost:</p>

<table>
    <thead>
        <tr><th>Body Part</th><th>CPT Code</th><th>Medicare Rate</th><th>Hospital Charge</th><th>Imaging Center</th></tr>
    </thead>
    <tbody>
        <tr><td>Brain MRI w/ contrast</td><td>70553</td><td>~$285</td><td>$2,000&ndash;$4,500</td><td>$400&ndash;$900</td></tr>
        <tr><td>Knee MRI w/o contrast</td><td>73721</td><td>~$245</td><td>$1,500&ndash;$3,500</td><td>$350&ndash;$800</td></tr>
        <tr><td>Lumbar spine MRI w/o contrast</td><td>72148</td><td>~$255</td><td>$1,800&ndash;$4,000</td><td>$400&ndash;$900</td></tr>
        <tr><td>Shoulder MRI w/o contrast</td><td>73221</td><td>~$270</td><td>$1,500&ndash;$3,500</td><td>$350&ndash;$850</td></tr>
    </tbody>
</table>

<p>Notice the pattern: Medicare pays $245&ndash;$285 for these scans. Hospitals charge 6&ndash;16x that amount. Imaging centers charge 1.5&ndash;3x Medicare&mdash;still a markup, but a fraction of what hospitals charge.</p>

<p>Look up the Medicare rate for any MRI CPT code from your bill:</p>

{_embed(mode="cost", cpt="73721", title="Look up your MRI cost", subtitle="Enter the CPT code from your imaging bill to see what Medicare pays.")}

<h2 id="ct-costs">3. Common CT scan costs</h2>

<p>A CT scan (computed tomography) uses X-rays to create cross-sectional images of your body. CT scans are faster than MRIs (5&ndash;15 minutes) and are better for viewing bones, bleeding, and organ injuries. Here&rsquo;s what the most common CT scans cost:</p>

<table>
    <thead>
        <tr><th>Body Part</th><th>CPT Code</th><th>Medicare Rate</th><th>Hospital Charge</th><th>Imaging Center</th></tr>
    </thead>
    <tbody>
        <tr><td>CT abdomen/pelvis w/ contrast</td><td>74178</td><td>~$248</td><td>$1,800&ndash;$6,750</td><td>$350&ndash;$800</td></tr>
        <tr><td>CT chest w/ contrast</td><td>71260</td><td>~$200</td><td>$1,500&ndash;$5,000</td><td>$300&ndash;$700</td></tr>
        <tr><td>CT head/brain w/o contrast</td><td>70551</td><td>~$195</td><td>$1,200&ndash;$4,000</td><td>$250&ndash;$600</td></tr>
    </tbody>
</table>

<p>CT scans of the abdomen and pelvis show the widest price range. A 2023 KFF analysis found that hospital charges for a CT abdomen with contrast ranged from $300 to <strong>$6,750</strong> across facilities&mdash;a 22x difference for the identical scan. That&rsquo;s why comparing prices before you schedule matters so much.</p>

<p>You can also check how your hospital prices these scans in our <a href="/hospitals/">hospital pricing directory</a>.</p>

<h2 id="real-bill">4. An actual imaging bill, annotated</h2>

<p>Here&rsquo;s a real bill for a patient who got a knee MRI at a <strong>hospital outpatient department</strong>. We&rsquo;ve flagged the key cost drivers:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Metro General Hospital Outpatient &mdash; Date of Service: 01/08/2026</div>
    <div class="line-item flagged">
        <span>73721 &mdash; MRI Knee w/o Contrast (Technical Component) &nbsp; &#9888; <em>Hospital facility fee &mdash; biggest cost driver</em></span>
        <span>$2,450.00</span>
    </div>
    <div class="line-item">
        <span>73721 &mdash; MRI Knee w/o Contrast (Professional Component)</span>
        <span>$375.00</span>
    </div>
    <div class="line-item flagged">
        <span>A4550 &mdash; Surgical tray/supplies &nbsp; &#9888; <em>No surgery was performed</em></span>
        <span>$85.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$2,910.00</span>
    </div>
</div>

<p>Let&rsquo;s break this down:</p>

<ul>
    <li><strong>Technical component ($2,450)</strong> &mdash; This is the hospital&rsquo;s facility fee for using the MRI machine. It covers the equipment, the technologist who operates it, and the hospital&rsquo;s overhead. Medicare pays about $245 total for this scan. The hospital is charging <strong>10x the Medicare rate</strong> for the technical component alone.</li>
    <li><strong>Professional component ($375)</strong> &mdash; This is the radiologist&rsquo;s fee for reading the images and writing the report. This portion is more in line with typical rates.</li>
    <li><strong>Surgical tray ($85)</strong> &mdash; An MRI is a non-invasive scan. No needles, no incisions, no surgical trays. This charge doesn&rsquo;t belong on the bill and should be disputed.</li>
</ul>

<p><strong>What the same MRI would cost at a freestanding imaging center:</strong> $350&ndash;$800 total (technical + professional combined, no facility fee). That&rsquo;s a potential savings of <strong>$2,110&ndash;$2,560</strong> for the identical scan.</p>

<div class="key-takeaway">
    <strong>The facility fee is the hidden cost on every hospital imaging bill.</strong> When you get a scan at a hospital outpatient department, you&rsquo;re paying two charges: the radiologist&rsquo;s reading fee (professional component) and the hospital&rsquo;s facility fee (technical component). At a freestanding center, these are bundled into a single, lower price. Understanding this split is the key to understanding why hospital imaging bills are so high.
</div>

<p>Not sure how to decode the rest of your bill? Read our full guide on <a href="/guides/how-to-read-your-medical-bill">how to read your medical bill</a>.</p>

<h2 id="pay-less">5. 5 ways to pay less for imaging</h2>

<h3>a) Get a prescription and go to a freestanding imaging center</h3>

<p>Your doctor orders the scan, but you choose where to get it. Ask your doctor for a written prescription (or referral, if your insurance requires one) and schedule the scan at a freestanding imaging center instead of the hospital. The radiologist at the center reads the images and sends the results to your doctor&mdash;same as the hospital would.</p>

<p>Freestanding centers charge 50&ndash;80% less for the same scan because they don&rsquo;t add a hospital facility fee. For a knee MRI, that typically means $350&ndash;$800 instead of $1,500&ndash;$3,500.</p>

<h3>b) Ask for the cash or self-pay price</h3>

<p>Even if you have insurance, paying cash can sometimes be cheaper than going through your plan&mdash;especially if you haven&rsquo;t met your deductible. Many imaging centers offer cash prices of $300&ndash;$600 for MRIs and $200&ndash;$500 for CT scans. Call ahead and ask: &ldquo;What is your cash price for a [scan type]?&rdquo; If the cash price is lower than what you&rsquo;d owe through insurance, pay cash. Just know that cash payments won&rsquo;t count toward your deductible.</p>

<h3>c) Compare prices using hospital price transparency data</h3>

<p>Since 2021, hospitals are required by federal law to publish their prices online. Use our <a href="/hospitals/">hospital pricing directory</a> to compare what different facilities charge for the same scan in your area. Price differences of $1,000&ndash;$3,000 between nearby facilities are common.</p>

<h3>d) Use the BillKarma calculator to check Medicare rates</h3>

<p>Before you schedule (or after you get the bill), <a href="/calculator">look up what Medicare pays</a> for your scan. Medicare rates are the federal government&rsquo;s benchmark for what a service is worth. If a facility is charging more than 3x the Medicare rate, that&rsquo;s above typical market pricing and worth questioning. You can also <a href="/scan">upload your bill to BillKarma</a> for an instant line-by-line comparison against Medicare rates.</p>

<h3>e) Ask your doctor if the imaging is truly necessary</h3>

<p>This is called &ldquo;shared decision making&rdquo;&mdash;having an honest conversation with your doctor about whether the scan will change your treatment plan. Some questions to ask:</p>

<ul>
    <li>&ldquo;Will the results of this scan change what we do next?&rdquo;</li>
    <li>&ldquo;Is there a less expensive test that could give us the information we need?&rdquo;</li>
    <li>&ldquo;Can we try conservative treatment first and only do the scan if symptoms don&rsquo;t improve?&rdquo;</li>
</ul>

<p>The American College of Radiology&rsquo;s Appropriateness Criteria provide evidence-based guidelines on when imaging is warranted. A good doctor will welcome these questions.</p>

<h2 id="case-studies">6. Real-world case studies</h2>

<div class="case-study">
    <h3>Case study 1: Knee MRI &mdash; hospital vs. imaging center</h3>
    <p>A patient was referred for a knee MRI (CPT 73721) after a sports injury. Their orthopedist&rsquo;s office scheduled the scan at the hospital outpatient department by default.</p>
    <p><strong>Hospital bill:</strong> $3,200 (13x the Medicare rate of $245).</p>
    <p>The patient hadn&rsquo;t met their $3,000 deductible, so they owed the full insurer-negotiated rate of $1,850 out of pocket.</p>
    <p>A freestanding imaging center <strong>5 miles away</strong> offered the same scan for <strong>$475 cash</strong>.</p>
    <p><strong>Savings: $2,725</strong> by choosing the imaging center over the hospital. The scan quality was identical&mdash;same type of MRI machine, images read by a board-certified radiologist.</p>
</div>

<div class="case-study">
    <h3>Case study 2: CT abdomen &mdash; negotiating with Medicare rate data</h3>
    <p>A patient received a CT abdomen with contrast (CPT 74178) at a hospital. The bill: <strong>$4,800</strong>&mdash;that&rsquo;s 19x the Medicare rate of $248.</p>
    <p>The patient called the billing department with a clear request: &ldquo;Medicare pays $248 for this scan. I&rsquo;m being charged $4,800. I&rsquo;d like to discuss a reduction to something closer to what insurance companies pay.&rdquo;</p>
    <p>After two calls and a written follow-up citing the Medicare rate, the hospital reduced the bill to <strong>$1,200</strong> (about 5x Medicare).</p>
    <p><strong>Savings: $3,600.</strong> The patient used our <a href="/calculator">cost calculator</a> to get the Medicare rate and our <a href="/guides/how-to-negotiate-medical-bills">negotiation guide</a> for the script.</p>
</div>

<div class="case-study">
    <h3>Case study 3: Brain MRI &mdash; insurance deductible trap</h3>
    <p>A patient got a brain MRI with contrast (CPT 70553) at a hospital outpatient department without asking about cost. The bill: <strong>$4,500</strong>.</p>
    <p>Their insurance processed the claim. The insurer&rsquo;s allowed amount (the negotiated rate) was <strong>$650</strong>. But the patient hadn&rsquo;t met their deductible, so they owed the full $650 out of pocket.</p>
    <p>A freestanding imaging center nearby offered the same brain MRI for <strong>$500 cash</strong>. If the patient had gone there instead, they would have saved <strong>$150</strong> on the scan AND the $650 would not have counted against their insurance deductible&mdash;preserving that deductible space for future care.</p>
    <p><strong>Lesson:</strong> When you haven&rsquo;t met your deductible, compare the imaging center&rsquo;s cash price against what your insurer would make you pay at the hospital. The cash route is often cheaper.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an MRI cost without insurance?</h3>
        <p>Without insurance, an MRI costs between $400 and $3,500 depending on where you go. Freestanding imaging centers charge $400&ndash;$900 for most MRIs. Hospital outpatient departments charge $1,500&ndash;$4,500 for the same scan. The national average is about $1,325. Always call ahead and ask for the cash or self-pay price.</p>
    </div>

    <div class="faq-item">
        <h3>Why is the same MRI so much cheaper at an imaging center than a hospital?</h3>
        <p>Hospital outpatient departments add a facility fee that covers overhead like 24/7 staffing and emergency readiness. Freestanding imaging centers do not charge this fee. The MRI machine, the scan protocol, and the radiologist reading the images are the same&mdash;the only difference is the facility surcharge.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover MRI and CT scans?</h3>
        <p>Most plans cover medically necessary imaging, but you may still owe a significant amount. If you haven&rsquo;t met your deductible, you could owe the full allowed amount. Even after meeting your deductible, coinsurance (the percentage you pay, typically 20&ndash;40%) on a $2,000 scan means $400&ndash;$800 out of pocket. Always check whether prior authorization is required before scheduling.</p>
    </div>

    <div class="faq-item">
        <h3>What does &ldquo;with contrast&rdquo; mean on my imaging bill?</h3>
        <p>Contrast is a special dye injected into your vein to make certain tissues show up more clearly on the images. Scans with contrast cost $100&ndash;$300 more because of the dye and additional imaging time. The CPT code on your bill changes when contrast is used&mdash;for example, a brain MRI without contrast is CPT 70551, while with contrast it&rsquo;s CPT 70553.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate the price of an MRI or CT scan?</h3>
        <p>Yes. Call the facility and ask for their cash or self-pay price. Many offer 30&ndash;50% discounts for upfront payment. You can also compare prices across facilities using our <a href="/hospitals/">hospital pricing directory</a> and <a href="/guides/how-to-negotiate-medical-bills">negotiate your bill</a> after the fact using Medicare rates as your anchor.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if my imaging bill seems too high?</h3>
        <p>First, request an itemized bill with CPT codes if you don&rsquo;t have one. Then <a href="/calculator">look up what Medicare pays</a> for each code. If any charge exceeds 3x the Medicare rate, you have strong grounds to <a href="/guides/how-to-dispute-a-medical-bill">dispute the bill</a>. You can also <a href="/scan">upload your bill to BillKarma</a> for an instant audit that compares every line item against federal pricing data.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://healthcostinstitute.org/" target="_blank" rel="noopener">Health Care Cost Institute: Imaging Cost Data</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS)</a></li>
    <li><a href="https://www.kff.org/health-costs/" target="_blank" rel="noopener">KFF: Health Care Costs and Affordability</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios</a></li>
    <li><a href="https://www.acr.org/Clinical-Resources/ACR-Appropriateness-Criteria" target="_blank" rel="noopener">American College of Radiology: Appropriateness Criteria</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency Requirements</a></li>
</ul>
""",
})
