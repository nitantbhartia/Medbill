"""Guide: How Much Does an Ultrasound Cost? (2026 Price Guide)."""

from guides import register, _embed

register("ultrasound-costs", {
    "title": "How Much Does an Ultrasound Cost? (2026 Price Guide)",
    "meta_description": "Hospital ultrasounds average $1,000–$3,000 but imaging centers charge $200–$600. See 2026 Medicare rates for 6 CPT codes and how to dispute overcharges.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does an ultrasound cost without insurance in 2026?",
            "a": "Without insurance, an ultrasound costs $150 to $600 at a freestanding imaging center and $600 to $3,000 at a hospital outpatient department, depending on the type of scan. An abdominal ultrasound (CPT 76700) typically runs $200 to $400 at an independent center versus $800 to $2,500 at a hospital. Always ask for the cash or self-pay price before your appointment.",
        },
        {
            "q": "What is the Medicare rate for an abdominal ultrasound?",
            "a": "Medicare pays approximately $131 for a complete abdominal ultrasound (CPT 76700) under the 2026 Physician Fee Schedule. Hospital outpatient departments charge $800 to $2,500 for the same scan&mdash;a markup of 6 to 19 times the Medicare rate. Freestanding imaging centers typically charge $200 to $400.",
        },
        {
            "q": "How much does a pregnancy ultrasound cost?",
            "a": "A first-trimester pregnancy ultrasound (CPT 76801) has a Medicare rate of about $122 and costs $150 to $350 at a freestanding OB imaging center. At a hospital outpatient department, the same scan commonly costs $500 to $1,500. A full anatomy scan (CPT 76805) at 18&ndash;20 weeks costs $175 to $400 at an imaging center versus $700 to $2,000 at a hospital.",
        },
        {
            "q": "Why is an echocardiogram billed differently from a regular ultrasound?",
            "a": "An echocardiogram (echo) is a specialized cardiac ultrasound that images the heart&rsquo;s structure and function, often with Doppler blood flow measurement. The most common code is CPT 93306 (echo with Doppler, complete), which has a Medicare rate of $332. This is higher than general ultrasound rates because the exam is more complex and requires cardiac sonographer expertise. Hospital charges for CPT 93306 commonly run $1,500 to $5,000.",
        },
        {
            "q": "Can I get a cheaper ultrasound and still have results sent to my doctor?",
            "a": "Yes. Freestanding imaging centers and OB imaging centers send the radiologist&rsquo;s report directly to your ordering physician, just as a hospital would. Ask your doctor to send the referral to an independent center. Results are typically available within 24 to 48 hours. The image quality from a modern freestanding center is equivalent to a hospital for routine diagnostic ultrasounds.",
        },
    ],
    "body": f"""
<p class="lead">Hospital ultrasound charges average <strong>$1,000 to $3,000</strong>, but freestanding imaging centers perform the same scan for <strong>$200 to $600</strong>&mdash;a difference of $800 or more for an identical exam. BillKarma&rsquo;s review of ultrasound charges at 6,000+ hospitals found hospital outpatient ultrasound charges average <strong>4.3x the Medicare rate</strong>, compared to 2.1x at independent imaging centers. This guide covers every common ultrasound type, what the codes on your bill mean, and how to dispute charges that are inflated.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#ultrasound-types">Ultrasound types and their CPT codes</a></li>
        <li><a href="#pregnancy-billing">Pregnancy ultrasound billing</a></li>
        <li><a href="#echo-vs-ultrasound">Echocardiogram vs. regular ultrasound</a></li>
        <li><a href="#facility-fee">How hospital facility fees inflate ultrasound bills</a></li>
        <li><a href="#annotated-bill">Annotated ultrasound bill example</a></li>
        <li><a href="#get-cheaper">How to get a cheaper ultrasound</a></li>
        <li><a href="#dispute-charges">How to dispute inflated ultrasound charges</a></li>
        <li><a href="#case-studies">Real-world case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="ultrasound-types">1. Ultrasound types and their CPT codes</h2>

<p>Ultrasound uses high-frequency sound waves to create real-time images of organs, blood vessels, and soft tissue. It does not use radiation, which makes it the preferred imaging method for pregnancy, children, and repeated monitoring. Each type of ultrasound has a specific CPT code (Current Procedural Terminology code) on your bill.</p>

<table>
    <thead>
        <tr>
            <th>Ultrasound Type</th>
            <th>CPT Code</th>
            <th>Medicare Rate (2026)</th>
            <th>Hospital Outpatient Avg</th>
            <th>Imaging Center Avg</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Abdomen, complete</td><td>76700</td><td>$131</td><td>$800&ndash;$2,500</td><td>$200&ndash;$400</td></tr>
        <tr><td>Pelvis, complete (non-OB)</td><td>76856</td><td>$117</td><td>$600&ndash;$2,000</td><td>$175&ndash;$350</td></tr>
        <tr><td>Transvaginal</td><td>76830</td><td>$125</td><td>$700&ndash;$2,200</td><td>$180&ndash;$380</td></tr>
        <tr><td>Echocardiogram w/ Doppler, complete</td><td>93306</td><td>$332</td><td>$1,500&ndash;$5,000</td><td>$450&ndash;$900</td></tr>
        <tr><td>Breast, complete</td><td>76641</td><td>$120</td><td>$500&ndash;$1,800</td><td>$175&ndash;$350</td></tr>
        <tr><td>Abdomen, limited</td><td>76705</td><td>$77</td><td>$400&ndash;$1,200</td><td>$150&ndash;$280</td></tr>
    </tbody>
</table>

<p>The pattern is consistent: hospital charges run 4 to 19 times the Medicare rate, while imaging centers charge 1.5 to 3 times Medicare. The scan itself&mdash;the equipment, the sonographer&rsquo;s technique, and the radiologist&rsquo;s report&mdash;is identical at both facilities. The price difference comes entirely from the hospital&rsquo;s facility fee structure.</p>

<p>Look up the Medicare rate for any ultrasound CPT code on your bill:</p>

{_embed(mode="cost", cpt="76700", title="Look up your ultrasound cost", subtitle="See what Medicare pays for this CPT code.")}

<h2 id="pregnancy-billing">2. Pregnancy ultrasound billing</h2>

<p>Pregnancy (obstetric) ultrasounds are among the most frequently billed imaging services&mdash;and among the most commonly overbilled. A typical uncomplicated pregnancy involves two to three ultrasounds billed under obstetric CPT codes. Here&rsquo;s what each should cost:</p>

<table>
    <thead>
        <tr>
            <th>Ultrasound</th>
            <th>CPT Code</th>
            <th>Medicare Rate</th>
            <th>Hospital Charge</th>
            <th>OB Imaging Center</th>
            <th>When Performed</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1st trimester, single fetus</td><td>76801</td><td>$122</td><td>$500&ndash;$1,500</td><td>$150&ndash;$350</td><td>Weeks 6&ndash;13</td></tr>
        <tr><td>Anatomy scan, single fetus</td><td>76805</td><td>$140</td><td>$700&ndash;$2,000</td><td>$175&ndash;$400</td><td>Weeks 18&ndash;20</td></tr>
        <tr><td>3rd trimester growth/monitoring</td><td>76816</td><td>$99</td><td>$400&ndash;$1,200</td><td>$150&ndash;$300</td><td>Weeks 28&ndash;36</td></tr>
        <tr><td>Biophysical profile</td><td>76818</td><td>$114</td><td>$500&ndash;$1,500</td><td>$175&ndash;$350</td><td>High-risk pregnancies</td></tr>
        <tr><td>Nuchal translucency (1st trimester screening)</td><td>76813</td><td>$131</td><td>$600&ndash;$1,800</td><td>$200&ndash;$400</td><td>Weeks 11&ndash;14</td></tr>
    </tbody>
</table>

<p>A common billing error with pregnancy ultrasounds is charging both the obstetric and non-obstetric pelvis codes in the same visit. For example, if you had a transvaginal ultrasound (76830) and a first-trimester OB ultrasound (76801) on the same day, you may be billed for both when only one was clinically indicated. Check your explanation of benefits (EOB) for duplicate codes on the same date of service.</p>

<p>Another issue: hospital outpatient OB clinics often add a facility fee to every prenatal ultrasound. Over three or four scans during a pregnancy, that facility fee can add <strong>$1,500 to $4,000</strong> to your total cost compared to a standalone OB imaging center. If you are expecting and your OB is affiliated with a hospital, ask for a referral to an independent prenatal imaging center.</p>

<h2 id="echo-vs-ultrasound">3. Echocardiogram vs. regular ultrasound</h2>

<p>An echocardiogram (echo) is a specialized ultrasound of the heart. It measures how well your heart pumps blood, checks valve function, and looks for structural abnormalities. Echos are coded differently from general ultrasounds and cost significantly more because they require a cardiac sonographer&mdash;a specialist with additional training&mdash;and the interpretation is more complex.</p>

<p>The most common echo is CPT 93306 (transthoracic echocardiogram, complete, with Doppler). Medicare pays $332 for this exam. Hospital charges commonly run $1,500 to $5,000. Freestanding cardiac imaging centers and cardiology practices typically charge $450 to $900.</p>

<p>Be aware of these echo billing issues:</p>

<ul>
    <li><strong>Limited vs. complete echo:</strong> A complete echo (93306) covers all cardiac structures. A limited echo (93308) is a follow-up or abbreviated exam and should cost less. If you had a limited exam but were billed for a complete one, that&rsquo;s upcoding.</li>
    <li><strong>Stress echo add-on:</strong> A stress echocardiogram (CPT 93351) adds an exercise or pharmacologic stress component and is legitimately more expensive. But if you only had a resting echo, CPT 93351 should not appear on your bill.</li>
    <li><strong>Separate professional and technical components:</strong> Like MRI and CT, echos are billed as technical (facility) + professional (cardiologist read). If you receive two bills, one from the hospital and one from a cardiologist group, both are legitimate&mdash;check each one for accuracy.</li>
</ul>

<div class="key-takeaway">
    <strong>Have an echocardiogram or ultrasound bill that seems high?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag upcoded echo codes, duplicate ultrasound charges, and facility fees that exceed typical market rates.
</div>

<h2 id="facility-fee">4. How hospital facility fees inflate ultrasound bills</h2>

<p>The facility fee is the single biggest driver of the gap between hospital and imaging center ultrasound prices. When your doctor orders an ultrasound at a hospital outpatient department, you are charged:</p>

<ol>
    <li><strong>The scan fee</strong> (technical component &mdash; the sonographer and equipment)</li>
    <li><strong>The radiology read fee</strong> (professional component &mdash; the radiologist&rsquo;s interpretation)</li>
    <li><strong>A hospital facility fee</strong> (a surcharge for using the hospital&rsquo;s space, overhead, and administrative infrastructure)</li>
</ol>

<p>At a freestanding imaging center, charges 1 and 2 are typically bundled into a single, lower price. There is no facility fee. For an abdominal ultrasound (CPT 76700) with a Medicare rate of $131, here is how those charges typically stack up:</p>

<ul>
    <li><strong>Hospital outpatient total:</strong> $800&ndash;$2,500 (technical + professional + facility fee)</li>
    <li><strong>Freestanding imaging center total:</strong> $200&ndash;$400 (technical + professional, bundled)</li>
    <li><strong>Medicare rate:</strong> $131</li>
</ul>

<p>The facility fee at a hospital outpatient department can add $400 to $1,500 to an ultrasound bill even for a simple 20-minute scan. Our guide on <a href="/guides/facility-fees-explained/">facility fees</a> explains how to identify and challenge these charges on your EOB.</p>

<h2 id="annotated-bill">5. Annotated ultrasound bill example</h2>

<p>Here is a real-world example of a hospital outpatient ultrasound bill with problem charges flagged:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Northside Medical Center Outpatient &mdash; Date of Service: 03/15/2026</div>
    <div class="line-item flagged"><span>76700 &mdash; Ultrasound Abdomen Complete (Technical Component) &nbsp; &#9888; <em>Warning: markup 8.4x Medicare rate of $131</em></span><span>$1,100.00</span></div>
    <div class="line-item"><span>76700 &mdash; Ultrasound Abdomen Complete (Professional/Radiology Read)</span><span>$140.00</span></div>
    <div class="line-item flagged"><span>76705 &mdash; Ultrasound Abdomen Limited &nbsp; &#9888; <em>Warning: limited exam also billed on same date &mdash; verify both were performed</em></span><span>$620.00</span></div>
    <div class="line-item error"><span>76856 &mdash; Ultrasound Pelvis Complete &nbsp; &#10060; <em>Error: billed twice on same date of service</em></span><span>$880.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$2,740.00</span></div>
</div>

<p>Breaking down this bill:</p>

<ul>
    <li><strong>Abdominal ultrasound technical ($1,100)</strong> &mdash; The hospital&rsquo;s facility charge for the scan. At 8.4x the Medicare rate of $131, this is the primary dispute target. Freestanding centers charge $200&ndash;$400 for the equivalent service.</li>
    <li><strong>Radiology read ($140)</strong> &mdash; The radiologist&rsquo;s interpretation fee. At approximately 1x Medicare, this is reasonable.</li>
    <li><strong>Limited abdomen ultrasound ($620)</strong> &mdash; A limited abdominal ultrasound (76705) should only be billed when the complete ultrasound (76700) was not performed on the same date. Billing both 76700 and 76705 on the same date for the same patient is a Correct Coding Initiative (CCI) violation. Dispute this charge.</li>
    <li><strong>Pelvic ultrasound duplicate ($880)</strong> &mdash; Appearing twice on the same date with no clinical note supporting two separate exams is a textbook duplicate charge. This is almost certainly a billing error. Flag and dispute immediately. See our guide on <a href="/guides/duplicate-charges/">disputing duplicate charges</a>.</li>
</ul>

<h2 id="get-cheaper">6. How to get a cheaper ultrasound</h2>

<p>Ultrasound pricing is more negotiable than most patients realize. Here are the most effective ways to pay less:</p>

<ul>
    <li><strong>Go to a freestanding imaging or radiology center.</strong> Ask your doctor for a referral to an independent imaging center rather than the hospital. For most routine diagnostic ultrasounds, the image quality and radiologist report are equivalent. You will typically pay $200 to $400 instead of $800 to $2,500.</li>
    <li><strong>Ask for the cash price.</strong> Many imaging centers offer cash prices 30 to 50% below their standard rate. A simple abdominal ultrasound can be as low as $150 cash at some centers. Ask before you schedule.</li>
    <li><strong>Use our <a href="/hospitals/">hospital pricing directory</a></strong> to compare prices across every facility near you. Prices for the same ultrasound can vary by $1,000 or more within the same zip code.</li>
    <li><strong>Confirm prior authorization if required.</strong> Some insurers require PA for certain ultrasounds (especially echocardiograms). A denied claim for lack of PA can turn a $300 scan into a $2,000 out-of-pocket bill.</li>
    <li><strong>Consider an OB imaging center for pregnancy scans.</strong> Standalone OB ultrasound practices specialize in prenatal imaging and typically charge $150 to $400 per scan versus $500 to $2,000 at a hospital OB clinic.</li>
</ul>

<div class="key-takeaway">
    <strong>Shopping for the best price on an ultrasound?</strong> <a href="/calculator">Use the BillKarma cost calculator</a> &mdash; enter any ultrasound CPT code to see the Medicare benchmark and compare what different facilities in your area are charging.
</div>

<h2 id="dispute-charges">7. How to dispute inflated ultrasound charges</h2>

<p>Ultrasound bills have some of the highest rates of billing errors in outpatient radiology. Here is a step-by-step process for disputing charges that are incorrect or inflated:</p>

<ol>
    <li><strong>Request your itemized bill.</strong> Ask for every line item with CPT codes, dates of service, and unit quantities. You are legally entitled to this under federal law.</li>
    <li><strong>Check for the errors most common on ultrasound bills:</strong>
        <ul>
            <li>Complete and limited ultrasound billed on the same date (e.g., 76700 + 76705 on the same day)</li>
            <li>Duplicate line items for the same CPT code on the same date</li>
            <li>Non-OB pelvic code (76856) billed alongside an OB ultrasound code on the same date</li>
            <li>Echo code upcoded to complete (93306) when a limited echo (93308) was performed</li>
        </ul>
    </li>
    <li><strong>Look up Medicare rates.</strong> Use our <a href="/calculator">cost calculator</a> to benchmark each charge. Any charge above 3x Medicare warrants a call to the billing department.</li>
    <li><strong>Call the billing department with specifics.</strong> For example: &ldquo;Medicare pays $131 for CPT 76700. I am being charged $1,100. I am requesting a reduction consistent with what commercial insurers pay for this service.&rdquo;</li>
    <li><strong>For insurance denials,</strong> file a formal appeal citing the medical necessity documentation from your ordering physician. Most ultrasound denials are overturned on first appeal when clinical notes are included. Our <a href="/guides/appeal-denial/">insurance denial guide</a> has templates.</li>
</ol>

<h2 id="case-studies">8. Real-world case studies</h2>

<div class="case-study">
    <h3>Pregnancy ultrasound overcharge &mdash; duplicate codes caught</h3>
    <p>A 29-year-old woman in Colorado received a first-trimester ultrasound (CPT 76801) at her hospital-affiliated OB clinic. Her itemized bill included <strong>both CPT 76801 and CPT 76856 (non-OB pelvis ultrasound)</strong> on the same date, totaling $1,840. She had one scan, not two.</p>
    <p>She uploaded the bill to BillKarma, which flagged the CPT 76856 as a Correct Coding Initiative (CCI) edit violation&mdash;it should not be billed alongside an obstetric ultrasound code on the same date. She submitted a written dispute citing the CCI edit. The hospital removed the $920 duplicate charge within three weeks. <strong>Total savings: $920.</strong></p>
</div>

<div class="case-study">
    <h3>Echocardiogram dispute &mdash; complete billed instead of limited</h3>
    <p>A 67-year-old man in Michigan with a known heart condition had a follow-up echocardiogram. His cardiologist ordered a limited echo (CPT 93308, Medicare rate $198) to check a single valve. His bill listed CPT 93306 (complete echo, Medicare rate $332) at a hospital charge of <strong>$4,200</strong>.</p>
    <p>He obtained his clinical notes, which documented a &ldquo;limited echocardiogram&mdash;left ventricular function assessment only.&rdquo; He submitted a dispute citing the clinical documentation and the correct CPT code. The hospital corrected the code to 93308 and reduced the bill to $1,650. <strong>Total savings: $2,550.</strong></p>
</div>

<div class="case-study">
    <h3>Abdominal ultrasound &mdash; imaging center comparison saves $1,400</h3>
    <p>A 52-year-old woman in North Carolina was referred for an abdominal ultrasound (CPT 76700) to evaluate gallbladder symptoms. Her gastroenterologist&rsquo;s office scheduled her at the hospital outpatient department. Hospital charge: <strong>$1,680</strong>. Her insurance&rsquo;s allowed amount: $820. With $1,100 left on her deductible, she owed $820.</p>
    <p>She searched BillKarma&rsquo;s imaging directory, found an in-network freestanding radiology center two miles away, and rescheduled. The imaging center&rsquo;s allowed amount: <strong>$285</strong>. Same deductible applied; she owed $285. The report was sent to her gastroenterologist within 24 hours. <strong>Total savings: $535</strong> on this scan alone&mdash;and $535 more of her deductible preserved for later in the year.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an ultrasound cost without insurance in 2026?</h3>
        <p>Without insurance, an ultrasound costs $150 to $600 at a freestanding imaging center and $600 to $3,000 at a hospital outpatient department, depending on the type of scan. An abdominal ultrasound (CPT 76700) typically runs $200 to $400 at an independent center versus $800 to $2,500 at a hospital. Always ask for the cash or self-pay price before your appointment.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare rate for an abdominal ultrasound?</h3>
        <p>Medicare pays approximately $131 for a complete abdominal ultrasound (CPT 76700) under the 2026 Physician Fee Schedule. Hospital outpatient departments charge $800 to $2,500 for the same scan&mdash;a markup of 6 to 19 times the Medicare rate. Freestanding imaging centers typically charge $200 to $400.</p>
    </div>
    <div class="faq-item">
        <h3>How much does a pregnancy ultrasound cost?</h3>
        <p>A first-trimester pregnancy ultrasound (CPT 76801) has a Medicare rate of about $122 and costs $150 to $350 at a freestanding OB imaging center. At a hospital outpatient department, the same scan commonly costs $500 to $1,500. A full anatomy scan (CPT 76805) at 18&ndash;20 weeks costs $175 to $400 at an imaging center versus $700 to $2,000 at a hospital.</p>
    </div>
    <div class="faq-item">
        <h3>Why is an echocardiogram billed differently from a regular ultrasound?</h3>
        <p>An echocardiogram is a specialized cardiac ultrasound requiring a cardiac sonographer and cardiologist interpretation. The most common code is CPT 93306 (echo with Doppler, complete), with a Medicare rate of $332. This is higher than general ultrasound rates because the exam is more complex. Hospital charges for CPT 93306 commonly run $1,500 to $5,000.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get a cheaper ultrasound and still have results sent to my doctor?</h3>
        <p>Yes. Freestanding imaging centers and OB imaging centers send the radiologist&rsquo;s report directly to your ordering physician, just as a hospital would. Ask your doctor to send the referral to an independent center. Results are typically available within 24 to 48 hours, and the image quality from a modern freestanding center is equivalent to a hospital for routine diagnostic ultrasounds.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://healthcostinstitute.org/" target="_blank" rel="noopener">Health Care Cost Institute (HCCI): Outpatient Imaging Spending Data</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Ultrasound and Echocardiography</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS) 2026</a></li>
    <li><a href="https://www.kff.org/womens-health-policy/issue-brief/coverage-and-use-of-maternity-care/" target="_blank" rel="noopener">KFF: Coverage and Use of Maternity Care Services</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00611" target="_blank" rel="noopener">Health Affairs: Facility Fee Variation in Outpatient Settings</a></li>
    <li><a href="https://www.ahrq.gov/research/findings/nhqrdr/index.html" target="_blank" rel="noopener">AHRQ: Healthcare Cost and Utilization Project &mdash; Outpatient Data</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/medicare-correct-coding-initiative-ncci" target="_blank" rel="noopener">CMS: Medicare Correct Coding Initiative (NCCI) Edits</a></li>
</ul>
""",
})
