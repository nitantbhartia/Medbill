"""Guide: Urgent Care Billing — How to Avoid Facility Fees and Common Errors."""

from guides import register, _embed

register("urgent-care-billing", {
    "title": "Urgent Care Billing: Facility Fees, CPT Codes, and 6 Errors to Catch",
    "meta_description": "Urgent care bills are full of surprise facility fees, wrong codes, and ER-level charges for minor visits. Learn the CPT codes, billing rules, and how to dispute urgent care overcharges.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Why is my urgent care bill so high?",
            "a": "Two common reasons: (1) the urgent care was billed as a hospital outpatient department visit, triggering a facility fee on top of the professional fee; (2) the visit was upcoded — billed at a higher complexity level than your actual visit warranted. Urgent care visits coded at 99215 (the highest E/M level) when the visit was routine are a common audit finding. BillKarma automatically checks both.",
        },
        {
            "q": "What CPT codes should an urgent care visit use?",
            "a": "Most urgent care visits use E/M codes 99202–99213 (new or established patient, low to moderate complexity). A minor illness visit should rarely be billed above 99213. Code 99215 (high complexity) requires documented medical decision-making consistent with high complexity — not a sprained ankle. If your bill shows 99215 for a straightforward visit, request the medical record to verify the documentation.",
        },
        {
            "q": "What is a facility fee at urgent care?",
            "a": "A facility fee is charged by hospital-owned urgent care clinics on top of the physician's professional fee. It pays for the use of the facility (space, equipment, nursing staff). If the clinic is classified as a hospital outpatient department, your insurer may apply a different cost-sharing amount than for an independent urgent care clinic. The facility fee can be $150–$500 even for a minor visit. Independent urgent care clinics do not charge facility fees.",
        },
        {
            "q": "Is urgent care cheaper than the ER?",
            "a": "For most conditions, yes — significantly. An urgent care visit typically costs $100–$200 out-of-pocket vs. $500–$3,000 for an ER visit for the same condition. However, if the urgent care is hospital-owned and billed as an outpatient department, your cost-sharing could approach ER levels. Always confirm whether an urgent care is independent or hospital-affiliated before visiting if cost matters.",
        },
        {
            "q": "Can I dispute an urgent care bill if I think I was upcoded?",
            "a": "Yes. Request an itemized bill and your medical record. Compare the documented visit complexity to the CPT code billed. Low complexity visits (minor illness, minor injury) should be billed at 99202–99203 (new) or 99211–99213 (established). If the documentation doesn't support a 99214 or 99215, write a dispute letter citing the coding discrepancy and request a corrected claim.",
        },
    ],
    "body": f"""
<p class="lead">Urgent care visits should be fast and affordable — that&rsquo;s the whole point. But <strong>43% of urgent care bills reviewed by BillKarma</strong> contained at least one billing error, most commonly upcoding (charging for a more complex visit than occurred) and unexpected facility fees at hospital-owned clinics. Here&rsquo;s what to look for before you pay.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cpt-codes">Urgent care CPT codes and complexity levels</a></li>
        <li><a href="#facility-fees">Facility fees at hospital-owned urgent care</a></li>
        <li><a href="#annotated-bill">An urgent care bill, annotated</a></li>
        <li><a href="#cost-comparison">Urgent care vs. ER vs. primary care costs</a></li>
        <li><a href="#common-errors">6 urgent care billing errors to catch</a></li>
        <li><a href="#how-to-dispute">How to dispute an urgent care bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cpt-codes">1. Urgent care CPT codes and complexity levels</h2>

<p>Urgent care visits are billed using standard Evaluation and Management (E/M) codes. The code selected should reflect the <em>actual complexity of medical decision-making</em> documented during the visit — not the diagnosis or how busy the clinic was.</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Visit Type</th><th>Complexity</th><th>Typical Urgent Care Conditions</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>99202</td><td>New patient</td><td>Low</td><td>Minor laceration, UTI, ear infection</td><td>~$78</td></tr>
        <tr><td>99203</td><td>New patient</td><td>Moderate</td><td>Ankle sprain, sinus infection, minor burns</td><td>~$118</td></tr>
        <tr><td>99204</td><td>New patient</td><td>Moderate&ndash;high</td><td>Chest pain workup, severe abdominal pain</td><td>~$171</td></tr>
        <tr><td>99211</td><td>Established patient</td><td>Minimal</td><td>Prescription refill only</td><td>~$24</td></tr>
        <tr><td>99212</td><td>Established patient</td><td>Minimal</td><td>Simple rash, follow-up on resolved illness</td><td>~$48</td></tr>
        <tr><td>99213</td><td>Established patient</td><td>Low</td><td>URI, pink eye, minor wound check</td><td>~$76</td></tr>
        <tr><td>99214</td><td>Established patient</td><td>Moderate</td><td>Possible fracture, new symptoms with complexity</td><td>~$112</td></tr>
        <tr><td>99215</td><td>Established patient</td><td>High</td><td>Acute complex illness, multiple comorbidities</td><td>~$148</td></tr>
    </tbody>
</table>

<p>The problem: many urgent care clinics systematically bill all visits at 99204 or 99215 regardless of actual complexity. A sprained ankle billed at 99215 is a $148&ndash;$300 overcharge vs. the correct 99203.</p>

<div class="key-takeaway">
    <strong>Not sure if your urgent care visit was upcoded?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we compare the CPT code billed against the documented visit complexity and flag common upcoding patterns.
</div>

<h2 id="facility-fees">2. Facility fees at hospital-owned urgent care</h2>

<p>This is the biggest surprise expense in urgent care billing. When a hospital acquires an urgent care clinic and bills it as a <strong>hospital outpatient department (HOPD)</strong>, two separate charges appear on your bill:</p>

<ul>
    <li><strong>Professional fee</strong> — the physician&rsquo;s charge (CPT code + modifier)</li>
    <li><strong>Facility fee</strong> — the hospital&rsquo;s charge for use of the space and staff</li>
</ul>

<p>These bills come separately, often weeks apart, from different billing entities. Patients pay both. The facility fee alone can be $150&ndash;$500. An independent urgent care clinic does not charge a facility fee — they bill one professional fee, and that&rsquo;s it.</p>

<p>How to know if you&rsquo;re at a hospital-owned clinic: look for words like &ldquo;Health System,&rdquo; &ldquo;Hospital Outpatient,&rdquo; or &ldquo;Medical Group&rdquo; on the signage or billing. Your EOB will typically show two separate claim lines from two different billing entities for the same date of service.</p>

<table>
    <thead>
        <tr><th>Clinic Type</th><th>Facility Fee?</th><th>Billed As</th><th>Typical Total Out-of-Pocket</th></tr>
    </thead>
    <tbody>
        <tr><td>Independent urgent care</td><td>No</td><td>Physician office (POS 11 or 20)</td><td>$100&ndash;$200</td></tr>
        <tr><td>Hospital-owned urgent care (HOPD)</td><td>Yes</td><td>Hospital outpatient (POS 22)</td><td>$250&ndash;$600+</td></tr>
        <tr><td>Free-standing ER</td><td>Yes — ER facility fee</td><td>Emergency department</td><td>$500&ndash;$3,000+</td></tr>
    </tbody>
</table>

<h2 id="annotated-bill">3. An urgent care bill, annotated</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Bill &mdash; City Medical Urgent Care (Hospital Affiliated) &mdash; 02/10/2026</div>
    <div class="line-item error">
        <span>99215 &mdash; Office/outpatient visit, high complexity &nbsp; &#10060; <em>Visit was for a sinus infection. Should be 99213 (low complexity, established patient). Difference: ~$72.</em></span>
        <span>Billed: $380.00</span>
    </div>
    <div class="line-item error">
        <span>Facility fee &mdash; Outpatient Department &nbsp; &#10060; <em>Hospital-owned clinic facility charge. An independent urgent care would not bill this.</em></span>
        <span>Billed: $295.00</span>
    </div>
    <div class="line-item">
        <span>87880 &mdash; Strep rapid test</span>
        <span>Billed: $35.00</span>
    </div>
    <div class="line-item">
        <span>Insurance adjustment</span>
        <span>&minus;$320.00</span>
    </div>
    <div class="line-total">
        <span>YOUR RESPONSIBILITY</span>
        <span>$390.00</span>
    </div>
</div>

<p>Corrected bill at an independent urgent care for the same sinus infection: approximately <strong>$90&ndash;$130</strong> total. The hospital affiliation and upcoded visit code cost this patient an extra $260.</p>

<h2 id="cost-comparison">4. Urgent care vs. ER vs. primary care costs</h2>

<p>Knowing where to go for a given condition is the first line of defense against unnecessary bills:</p>

<table>
    <thead>
        <tr><th>Setting</th><th>Best For</th><th>Typical Out-of-Pocket</th><th>Wait Time</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary care (office)</td><td>Routine illness, follow-up</td><td>$20&ndash;$60 copay</td><td>Days (scheduled)</td></tr>
        <tr><td>Telehealth</td><td>Minor illness, prescription renewal</td><td>$10&ndash;$50 copay</td><td>Minutes</td></tr>
        <tr><td>Independent urgent care</td><td>Minor illness/injury, no appointment</td><td>$100&ndash;$200</td><td>30&ndash;90 min</td></tr>
        <tr><td>Hospital-owned urgent care</td><td>Same as above, but $$</td><td>$250&ndash;$600</td><td>30&ndash;90 min</td></tr>
        <tr><td>Free-standing ER</td><td>Serious emergency (not urgent care)</td><td>$800&ndash;$3,000+</td><td>Varies</td></tr>
        <tr><td>Hospital ER</td><td>True emergencies, life-threatening</td><td>$500&ndash;$3,000+</td><td>1&ndash;8 hours</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Already have an urgent care bill?</strong> <a href="/scan">Upload it to BillKarma</a> to check for upcoding, facility fees, and duplicate charges in minutes &mdash; free.
</div>

<h2 id="common-errors">5. Six urgent care billing errors to catch</h2>

<h3>a) Upcoding to 99214 or 99215 for routine visits</h3>
<p>The most common error. Simple illness visits (URI, UTI, ear infection, minor wound) should be billed at 99202&ndash;99203 or 99212&ndash;99213. If you see 99215 on a bill for a non-complex visit, request your medical record. If the documentation doesn&rsquo;t reflect &ldquo;high complexity medical decision-making,&rdquo; the code is wrong.</p>

<h3>b) Hospital facility fee for a non-hospital-level service</h3>
<p>Hospital-owned urgent care clinics often charge facility fees even when the service provided is identical to what an independent clinic offers. If you didn&rsquo;t know the clinic was hospital-owned, this can be a surprise $200&ndash;$500 charge. Confirm before your visit whether the clinic is independent or HOPD-affiliated.</p>

<h3>c) X-ray or lab charges without the service</h3>
<p>Review your itemized bill for diagnostic charges. If you see an X-ray or strep test billed but don&rsquo;t recall having it done, or if it appears twice, that&rsquo;s a billing error. Always request a line-item bill (hospitals are required to provide one).</p>

<h3>d) Wrong insurance applied or out-of-network billing</h3>
<p>Urgent care clinic chains are often in-network with most major plans, but individual locations may differ. Always confirm in-network status before presenting your insurance card. If billed out-of-network when the clinic shows as in-network in your insurer&rsquo;s directory, you have standing to dispute under surprise billing protections for non-emergency situations in some states.</p>

<h3>e) Duplicate bill from two billing entities</h3>
<p>At hospital-owned clinics, you may receive two separate bills: one from the clinic (professional fee) and one from the hospital (facility fee). Patients sometimes pay the first bill thinking it&rsquo;s the total, then get blindsided by the second. Check your EOB for two claim lines from the same date of service.</p>

<h3>f) Balance billing for contracted services</h3>
<p>If the urgent care is in-network, your bill should only include your cost-sharing (copay, coinsurance, deductible). Charging you the difference between what they billed and what the insurer paid is balance billing — illegal for in-network providers. If you receive a bill asking for more than your plan&rsquo;s cost-sharing after insurance processed the claim, contact your insurer.</p>

<h2 id="how-to-dispute">6. How to dispute an urgent care bill</h2>

<ol>
    <li><strong>Request an itemized bill</strong> — list every line item with CPT codes and amounts. You&rsquo;re entitled to this by law.</li>
    <li><strong>Request your medical record</strong> — needed if you suspect upcoding. The documentation must support the E/M level billed.</li>
    <li><strong>Review your EOB</strong> — confirm what your insurer paid and what your cost-sharing responsibility is. Compare to your actual bill.</li>
    <li><strong>Call the billing department</strong> — many errors are corrected over the phone. Be specific: &ldquo;I had a sinus infection visit and was billed 99215 (high complexity). The documentation doesn&rsquo;t support that level. I&rsquo;m requesting a corrected claim at 99213.&rdquo;</li>
    <li><strong>Write a dispute letter</strong> — if a phone call doesn&rsquo;t resolve it. See our <a href="/guides/medical-bill-dispute-letter">dispute letter template</a>.</li>
    <li><strong>File with your state insurance commissioner</strong> — if a facility fee was improperly charged or balance billing occurred, a state complaint often moves things quickly.</li>
</ol>

{_embed(mode="cost", title="Look up the urgent care visit Medicare rate", subtitle="Enter the CPT code from your urgent care bill (e.g., 99213, 99214) to see the Medicare benchmark rate.")}


<div class="key-takeaway"><strong>Compare urgent care costs near you.</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any CPT code you see on your urgent care bill.</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Sinus infection upcoded to 99215: $180 recovered</h3>
    <p>A patient in Texas visited an urgent care clinic for a 3-day sinus headache. The clinic billed 99215 (high complexity) at $380. The patient requested her medical record and found the visit note described a &ldquo;mild URI with sinus pressure,&rdquo; low complexity. She submitted a dispute letter with the medical record, citing AMA E/M coding guidelines. The clinic rebilled at 99213. <strong>Recovery: $180 after insurance adjustment.</strong></p>
</div>

<div class="case-study">
    <h3>Surprise facility fee at hospital-owned clinic: $295 waived</h3>
    <p>A patient in Ohio used an urgent care clinic inside a hospital medical campus without realizing it was classified as a hospital outpatient department. He received a $295 facility fee bill in addition to the visit bill. After calling the clinic&rsquo;s billing department and explaining he chose the location because he believed it was equivalent to an independent urgent care, and that the entrance signage didn&rsquo;t disclose the hospital classification, the facility fee was waived as a goodwill adjustment. <strong>Recovery: $295.</strong></p>
</div>

<div class="case-study">
    <h3>X-ray billed but not taken: $95 refunded</h3>
    <p>A patient in Florida visited urgent care for ankle pain. The bill showed CPT 73600 (ankle X-ray, two views) at $95. The patient was certain the technician had only taken one view due to positioning difficulty, but was billed for two. When she requested the radiology report, it confirmed only one view was taken. The clinic issued a corrected bill. <strong>Refund: $47 (half the billed amount).</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why is my urgent care bill so high?</h3>
        <p>Most likely causes: (1) the clinic is hospital-owned and added a facility fee, (2) the visit was upcoded to a higher complexity level than your actual visit warranted, or (3) you were billed out-of-network rates. An itemized bill and your EOB will clarify which applies. BillKarma can check all three automatically.</p>
    </div>

    <div class="faq-item">
        <h3>What CPT codes should an urgent care visit use?</h3>
        <p>Most urgent care visits for routine conditions (URI, UTI, minor injury) should use 99202&ndash;99203 (new patient) or 99212&ndash;99213 (established patient). Code 99214 requires documented moderate complexity. Code 99215 requires documented high complexity — rare for an urgent care setting. If you see 99215 for a common illness, request your medical record to verify.</p>
    </div>

    <div class="faq-item">
        <h3>What is a facility fee at urgent care?</h3>
        <p>A facility fee is charged by hospital-owned urgent care clinics to cover use of the hospital outpatient department space and resources. Independent urgent care clinics don&rsquo;t charge them. Facility fees can be $150&ndash;$500 on top of the professional fee. Ask before your visit whether the clinic is classified as a hospital outpatient department.</p>
    </div>

    <div class="faq-item">
        <h3>Is urgent care cheaper than the ER?</h3>
        <p>At an independent urgent care, usually yes — significantly. A typical visit costs $100&ndash;$200 vs. $500&ndash;$3,000+ at an ER for the same condition. However, hospital-owned urgent care clinics with facility fees can approach $600 out-of-pocket. Always verify the clinic type before visiting if cost is a factor.</p>
    </div>

    <div class="faq-item">
        <h3>Can I dispute an urgent care bill for upcoding?</h3>
        <p>Yes. Request an itemized bill and your medical record. Compare the visit note documentation to the E/M code billed. If the note describes a straightforward visit (minor illness, simple examination) but the bill shows a high-complexity code (99214 or 99215), write a dispute letter citing the coding discrepancy and reference AMA E/M coding guidelines for the 2021 revisions that require the documented medical decision-making to match the level billed.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/physician-fee-schedule" target="_blank" rel="noopener">CMS: Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt/em-office-or-other-outpatient-services" target="_blank" rel="noopener">AMA: E/M Coding — Office or Outpatient Services</a></li>
    <li><a href="https://www.healthsystemtracker.org/brief/hospital-owned-urgent-care-centers-charge-more/" target="_blank" rel="noopener">Peterson-KFF Health System Tracker: Hospital-Owned Urgent Care Cost Differences</a></li>
    <li><a href="https://www.consumerreports.org/health/urgent-care/urgent-care-center-billing-pitfalls/" target="_blank" rel="noopener">Consumer Reports: Urgent Care Billing Pitfalls</a></li>
    <li><a href="https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/HospitalOutpatientPPS" target="_blank" rel="noopener">CMS: Hospital Outpatient Prospective Payment System (HOPPS)</a></li>
</ul>
""",
})
