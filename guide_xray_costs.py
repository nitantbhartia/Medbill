"""Guide: X-Ray Cost."""

from guides import register, _embed

register("how-much-does-xray-cost", {
    "title": "How Much Does an X-Ray Cost in 2026? (By Body Part)",
    "meta_description": "X-rays cost $100-$1,000 without insurance depending on body part and location. See costs for chest, hand, foot, spine, and knee X-rays plus how to save.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does an X-ray cost without insurance?",
            "a": "An X-ray costs $100-$1,000 without insurance, depending on the body part and where you go. A simple chest X-ray (2-view) costs $100-$300 at an imaging center but $300-$750 at a hospital. Spinal and abdominal X-rays cost more ($200-$600 at imaging centers, $500-$1,000+ at hospitals). The technology is the same regardless of location.",
        },
        {
            "q": "Why do X-ray prices vary so much between locations?",
            "a": "The main driver is the facility fee. Hospitals add a facility fee ($200-$600) on top of the X-ray itself, covering ER overhead, 24/7 staffing, and administrative costs. Freestanding imaging centers and urgent care clinics don't have this markup. The actual X-ray technology and image quality are essentially identical across settings.",
        },
        {
            "q": "Does insurance cover X-rays?",
            "a": "Yes. Most insurance plans cover X-rays when ordered by a doctor. You'll pay a copay ($20-$75) or coinsurance (10-30%) after your deductible. Some preventive X-rays (like screening mammograms) are covered at 100% under the ACA. If your deductible hasn't been met, you'll pay the full negotiated rate, which is still lower than the cash price.",
        },
        {
            "q": "Where is the cheapest place to get an X-ray?",
            "a": "Freestanding imaging centers are almost always the cheapest option ($100-$400 for most X-rays). Urgent care clinics are next ($150-$400). Hospital outpatient departments are the most expensive ($300-$1,000+). ER X-rays cost the most because of the ER visit fee on top of the imaging charge. For a non-emergency X-ray, always ask your doctor to order it at a freestanding center.",
        },
        {
            "q": "How much does Medicare pay for X-rays?",
            "a": "Medicare pays $15-$50 for most X-rays (technical + professional components combined) at freestanding facilities, and $30-$100 at hospital outpatient departments. You pay 20% coinsurance after the Part B deductible ($257). A chest X-ray under Medicare costs you about $5-$8 out of pocket at a freestanding center.",
        },
    ],
    "body": f"""
<p class="lead">An X-ray is one of the most common medical tests&mdash;and one where prices vary the most by location. A simple chest X-ray costs <strong>$100&ndash;$300 at an imaging center</strong> but <strong>$300&ndash;$750 at a hospital</strong>. Same technology, same image, vastly different bills. Here&rsquo;s what every type of X-ray costs and where to get the best price.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-by-body-part">X-ray cost by body part</a></li>
        <li><a href="#where-to-go">Where to get an X-ray: cost by location</a></li>
        <li><a href="#why-prices-vary">Why X-ray prices vary so much</a></li>
        <li><a href="#insurance">Insurance and Medicare coverage</a></li>
        <li><a href="#xray-vs-ct-mri">When you need an X-ray vs. CT or MRI</a></li>
        <li><a href="#save-money">5 ways to save on X-rays</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-by-body-part">1. X-ray cost by body part</h2>

<table>
    <thead>
        <tr><th>Body Part</th><th>CPT Code</th><th>Imaging Center</th><th>Hospital</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Chest (2-view)</td><td>71046</td><td>$100&ndash;$250</td><td>$300&ndash;$750</td><td>~$25&ndash;$45</td></tr>
        <tr><td>Hand/finger (2-view)</td><td>73120</td><td>$80&ndash;$200</td><td>$250&ndash;$500</td><td>~$20&ndash;$35</td></tr>
        <tr><td>Foot (2-view)</td><td>73620</td><td>$80&ndash;$200</td><td>$250&ndash;$500</td><td>~$20&ndash;$35</td></tr>
        <tr><td>Ankle (3-view)</td><td>73610</td><td>$100&ndash;$250</td><td>$300&ndash;$600</td><td>~$25&ndash;$40</td></tr>
        <tr><td>Knee (2-view)</td><td>73560</td><td>$100&ndash;$250</td><td>$300&ndash;$600</td><td>~$25&ndash;$40</td></tr>
        <tr><td>Shoulder (2-view)</td><td>73030</td><td>$100&ndash;$250</td><td>$300&ndash;$650</td><td>~$25&ndash;$40</td></tr>
        <tr><td>Hip (2-view)</td><td>73502</td><td>$120&ndash;$300</td><td>$350&ndash;$700</td><td>~$30&ndash;$50</td></tr>
        <tr><td>Lumbar spine (2-view)</td><td>72100</td><td>$150&ndash;$350</td><td>$400&ndash;$800</td><td>~$35&ndash;$55</td></tr>
        <tr><td>Cervical spine (3-view)</td><td>72052</td><td>$150&ndash;$350</td><td>$400&ndash;$800</td><td>~$35&ndash;$55</td></tr>
        <tr><td>Abdomen (1-view)</td><td>74018</td><td>$120&ndash;$300</td><td>$350&ndash;$700</td><td>~$25&ndash;$45</td></tr>
        <tr><td>Pelvis (1-view)</td><td>72170</td><td>$120&ndash;$280</td><td>$300&ndash;$650</td><td>~$25&ndash;$40</td></tr>
        <tr><td>Wrist (2-view)</td><td>73100</td><td>$80&ndash;$200</td><td>$250&ndash;$500</td><td>~$20&ndash;$35</td></tr>
    </tbody>
</table>

{_embed(mode="cost", cpt="71046", title="Look Up X-Ray Cost", subtitle="Enter your X-ray CPT code to see Medicare rates in your area.")}

<div class="key-takeaway">
    <strong>The imaging center price is almost always 50&ndash;70% less than the hospital price for the exact same X-ray.</strong> Unless you&rsquo;re in the ER, there&rsquo;s rarely a medical reason to get an X-ray at a hospital outpatient department. Ask your doctor to send the order to a freestanding center.
</div>

<h2 id="where-to-go">2. Where to get an X-ray: cost by location</h2>

<table>
    <thead>
        <tr><th>Location</th><th>Typical Cost (chest X-ray)</th><th>Pros</th><th>Cons</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Freestanding imaging center</strong></td><td>$100&ndash;$250</td><td>Cheapest, quick, focused</td><td>Need doctor&rsquo;s order, may need appointment</td></tr>
        <tr><td><strong>Urgent care</strong></td><td>$150&ndash;$350</td><td>Walk-in, on-site reading</td><td>Visit fee on top of X-ray</td></tr>
        <tr><td><strong>Doctor&rsquo;s office (if equipped)</strong></td><td>$100&ndash;$300</td><td>Convenient, immediate</td><td>Not all offices have X-ray</td></tr>
        <tr><td><strong>Hospital outpatient</strong></td><td>$300&ndash;$750</td><td>Available 24/7</td><td>Facility fee markup, long waits</td></tr>
        <tr><td><strong>Emergency room</strong></td><td>$500&ndash;$1,500+</td><td>Immediate, any time</td><td>ER visit fee ($500&ndash;$3,000) on top</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Same ankle X-ray: $180 vs. $890</h3>
    <p>A runner in Colorado twisted her ankle and her doctor ordered an X-ray. The hospital outpatient department quoted $890 (imaging $340 + facility fee $550). A freestanding imaging center 2 miles away charged <strong>$180</strong> total. Same 3-view ankle X-ray (CPT 73610), same radiologist group reading the images. <strong>Savings: $710.</strong></p>
</div>

<h2 id="why-prices-vary">3. Why X-ray prices vary so much</h2>

<ul>
    <li><strong>Facility fees:</strong> Hospitals add $200&ndash;$600 in facility fees on top of the X-ray charge. This covers ER, ICU, and administrative overhead that has nothing to do with your X-ray. See our <a href="/guides/hospital-facility-fees-explained">facility fees guide</a>.</li>
    <li><strong>Hospital vs. freestanding:</strong> When a hospital buys an independent imaging center, prices often double overnight&mdash;even though nothing changes about the equipment or staff.</li>
    <li><strong>Insurance negotiated rates:</strong> The same X-ray may be billed at $600 but the insurer&rsquo;s negotiated rate is $150. Cash pay patients can often get the negotiated rate by asking.</li>
    <li><strong>Number of views:</strong> More views = higher cost. A 2-view chest X-ray costs more than a 1-view. Make sure you aren&rsquo;t billed for more views than were taken.</li>
    <li><strong>Reading fee:</strong> A radiologist charges separately to interpret the X-ray ($30&ndash;$100). This may come as a separate bill.</li>
</ul>

<h2 id="insurance">4. Insurance and Medicare coverage</h2>

<h3>Private insurance</h3>
<ul>
    <li><strong>With referral:</strong> Covered after deductible + copay ($20&ndash;$75) or coinsurance (10&ndash;30%)</li>
    <li><strong>Preventive:</strong> Some screening X-rays are covered at 100% under ACA</li>
    <li><strong>ER X-rays:</strong> Covered but subject to ER copay + facility charges</li>
</ul>

<h3>Medicare</h3>
<p>Medicare Part B covers diagnostic X-rays at 80% after the $257 annual deductible. Your 20% coinsurance on most X-rays is <strong>$5&ndash;$15</strong> at freestanding centers. At hospital outpatient departments, it&rsquo;s $10&ndash;$30.</p>

<h2 id="xray-vs-ct-mri">5. When you need an X-ray vs. CT or MRI</h2>

<table>
    <thead>
        <tr><th>Imaging Type</th><th>Best For</th><th>Cost Range</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>X-ray</strong></td><td>Fractures, lung issues, joint alignment</td><td>$100&ndash;$750</td></tr>
        <tr><td><strong>CT scan</strong></td><td>Internal injuries, kidney stones, cancer screening</td><td>$500&ndash;$3,000</td></tr>
        <tr><td><strong>MRI</strong></td><td>Soft tissue (ligaments, brain, spinal cord)</td><td>$1,000&ndash;$5,000</td></tr>
        <tr><td><strong>Ultrasound</strong></td><td>Pregnancy, gallstones, blood flow</td><td>$200&ndash;$1,000</td></tr>
    </tbody>
</table>

<p>For detailed imaging costs, see our <a href="/guides/how-much-does-mri-ct-scan-cost">MRI and CT scan cost guide</a>. Find imaging centers at <a href="/imaging/">BillKarma&rsquo;s imaging directory</a>.</p>

<h2 id="save-money">6. 5 ways to save on X-rays</h2>

<h3>a) Go to a freestanding imaging center</h3>
<p>50&ndash;70% cheaper than hospital outpatient. Ask your doctor to send the order there instead.</p>

<h3>b) Ask for the cash pay price</h3>
<p>Many imaging centers offer cash/self-pay rates of $50&ndash;$150 for basic X-rays&mdash;sometimes cheaper than your insurance copay.</p>

<h3>c) Check if your X-ray is preventive</h3>
<p>Some screening X-rays are covered at 100% under ACA preventive care rules. Ask if your X-ray qualifies.</p>

<h3>d) Avoid the ER for non-emergency X-rays</h3>
<p>An ER X-ray costs $500&ndash;$1,500+ (X-ray + ER visit fee). If it&rsquo;s not an emergency, go to urgent care or an imaging center instead.</p>

<h3>e) Verify the number of views billed</h3>
<p>Check your bill for the correct number of views. A 2-view knee X-ray (CPT 73560) costs less than a 3-view (CPT 73562). Make sure you weren&rsquo;t billed for views that weren&rsquo;t taken. <a href="/scan">Upload your bill to BillKarma</a> for a quick check.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an X-ray cost without insurance?</h3>
        <p>$100&ndash;$1,000 depending on body part and location. Imaging centers charge $100&ndash;$350, hospitals charge $300&ndash;$1,000+. The technology is identical.</p>
    </div>

    <div class="faq-item">
        <h3>Why do X-ray prices vary so much?</h3>
        <p>Hospital facility fees ($200&ndash;$600) are the main driver. Freestanding centers don&rsquo;t charge facility fees. The X-ray itself costs roughly the same everywhere.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover X-rays?</h3>
        <p>Yes, with a copay ($20&ndash;$75) or coinsurance after your deductible. Some preventive X-rays are covered at 100%. ER X-rays are covered but cost more.</p>
    </div>

    <div class="faq-item">
        <h3>Where is the cheapest place to get an X-ray?</h3>
        <p>Freestanding imaging centers ($100&ndash;$350 for most X-rays). Ask your doctor to send the order there. Urgent care is second cheapest ($150&ndash;$400).</p>
    </div>

    <div class="faq-item">
        <h3>How much does Medicare pay for X-rays?</h3>
        <p>$15&ndash;$50 for most X-rays at freestanding facilities. You pay 20% coinsurance ($5&ndash;$15) after the $257 Part B deductible.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule &mdash; Radiology CPT Codes (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener noreferrer">CMS: Hospital Outpatient PPS &mdash; Imaging Rates (2026)</a></li>
    <li><a href="https://www.acr.org/Practice-Management-Quality-Informatics/Imaging-3" target="_blank" rel="noopener noreferrer">American College of Radiology: Imaging Appropriateness Criteria</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Diagnostic Imaging Utilization Data</a></li>
</ul>
""",
})
