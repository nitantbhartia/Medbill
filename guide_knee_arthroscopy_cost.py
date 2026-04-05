"""Guide: Knee Arthroscopy Cost."""

from guides import register, _embed

register("knee-arthroscopy-cost", {
    "title": "Knee Arthroscopy Cost in 2026: What to Expect",
    "meta_description": "Knee arthroscopy costs $5,000–$25,000+. At a surgery center it's 40–60% less. See costs by procedure type, Medicare coverage, CPT codes, and how to spot billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does knee arthroscopy cost without insurance?",
            "a": "Knee arthroscopy costs $5,000–$25,000+ without insurance depending on the procedure performed. A diagnostic-only arthroscopy runs $5,000–$10,000. A meniscus repair or partial meniscectomy costs $8,000–$18,000. ACL reconstruction is the most expensive at $15,000–$25,000+. Choosing an ambulatory surgery center over a hospital can reduce costs by 40–60% for the same procedure.",
        },
        {
            "q": "How much does knee arthroscopy cost with insurance?",
            "a": "With insurance, most patients pay $1,500–$6,000 out of pocket for knee arthroscopy, depending on their deductible and coinsurance. If you've met your deductible, you pay your coinsurance (typically 20%) until you hit your out-of-pocket maximum. Prior authorization is almost always required—confirm approval before your surgery date.",
        },
        {
            "q": "Does Medicare cover knee arthroscopy?",
            "a": "Medicare covers knee arthroscopy when it's medically necessary—for conditions like meniscus tears, loose bodies, or plica syndrome. However, Medicare does not cover knee arthroscopy for osteoarthritis alone. A 2008 clinical trial (and subsequent CMS guidance) found that arthroscopy for knee osteoarthritis (lavage/debridement) is no more effective than sham surgery, and CMS will not pay for it as a primary indication. If osteoarthritis is the primary diagnosis, your claim is likely to be denied.",
        },
        {
            "q": "Is it cheaper to have knee arthroscopy at a surgery center vs. a hospital?",
            "a": "Yes, significantly. Knee arthroscopy at an ambulatory surgery center (ASC) typically costs 40–60% less than at a hospital. A meniscectomy that costs $15,000 at a hospital may cost $6,000–$9,000 at an ASC. The procedure itself is identical; you're paying for the lower overhead of a dedicated surgical facility vs. a full hospital. Check our surgery center directory at /surgery-centers/ to find ASCs near you.",
        },
        {
            "q": "What are the most common knee arthroscopy billing errors?",
            "a": "Orthopedic billing has a 36% error rate—one of the highest in medicine. Common knee arthroscopy errors include: billing CPT 29881 (meniscectomy) when a less extensive 29870 (diagnostic only) was performed; unbundling separate charges for the arthroscope, irrigation, and closure that should be bundled into the procedure code; duplicate facility and professional fees; and upcoding a partial meniscectomy (29881) to a meniscus repair (29882/29883), which pays more.",
        },
    ],
    "body": f"""
<p class="lead">Knee arthroscopy costs <strong>$5,000&ndash;$25,000+</strong> without insurance. At an ambulatory surgery center, the same procedure costs <strong>40&ndash;60% less</strong> than at a hospital. With insurance, most patients pay <strong>$1,500&ndash;$6,000</strong> out of pocket. Orthopedic billing has a 36% error rate&mdash;the highest of any specialty. Here&rsquo;s the full breakdown.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> Knee arthroscopy costs $5,000&ndash;$25,000+ without insurance depending on what&rsquo;s done. Surgery centers charge 40&ndash;60% less than hospitals for identical procedures. Medicare covers it when medically necessary, but not for osteoarthritis alone. Request an itemized bill with CPT codes&mdash;36% of orthopedic bills contain errors.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-by-procedure">Cost by procedure type</a></li>
        <li><a href="#with-without-insurance">Cost with vs. without insurance</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. ambulatory surgery center</a></li>
        <li><a href="#medicare-coverage">Medicare coverage</a></li>
        <li><a href="#insurance-prior-auth">Insurance and prior authorization</a></li>
        <li><a href="#cpt-codes">CPT codes for knee arthroscopy</a></li>
        <li><a href="#billing-errors">Common billing errors</a></li>
        <li><a href="#recovery-costs">Recovery and PT costs after surgery</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-by-procedure">1. Cost by procedure type</h2>

<p>&ldquo;Knee arthroscopy&rdquo; is an umbrella term for several procedures of varying complexity and cost. What you pay depends primarily on what your surgeon does inside the joint:</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>CPT Code</th><th>Without Insurance</th><th>At ASC</th><th>Medicare Rate (surgeon)</th></tr>
    </thead>
    <tbody>
        <tr><td>Diagnostic arthroscopy only</td><td>29870</td><td>$5,000&ndash;$10,000</td><td>$3,000&ndash;$6,000</td><td>~$500</td></tr>
        <tr><td>Synovectomy (partial)</td><td>29875</td><td>$6,000&ndash;$12,000</td><td>$3,500&ndash;$7,000</td><td>~$580</td></tr>
        <tr><td>Partial meniscectomy</td><td>29881</td><td>$8,000&ndash;$16,000</td><td>$5,000&ndash;$9,500</td><td>~$680</td></tr>
        <tr><td>Meniscus repair</td><td>29882&ndash;29883</td><td>$10,000&ndash;$20,000</td><td>$6,000&ndash;$12,000</td><td>~$820&ndash;$950</td></tr>
        <tr><td>Chondroplasty (cartilage smoothing)</td><td>29877</td><td>$7,000&ndash;$15,000</td><td>$4,000&ndash;$9,000</td><td>~$600</td></tr>
        <tr><td>ACL reconstruction (arthroscopic)</td><td>29888</td><td>$15,000&ndash;$25,000+</td><td>$9,000&ndash;$16,000</td><td>~$1,400</td></tr>
        <tr><td>Loose body removal</td><td>29874</td><td>$6,000&ndash;$12,000</td><td>$3,500&ndash;$7,000</td><td>~$560</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Multiple procedures in one session.</strong> It&rsquo;s common for a surgeon to perform more than one procedure during one arthroscopy (e.g., a partial meniscectomy and chondroplasty). Additional procedures add to the surgeon&rsquo;s fee, but the facility fee for the operating room is typically charged once. The second procedure is usually billed at a reduced rate (50% of the full value for add-on codes).
</div>

{_embed(mode="cost", cpt="29881", title="Look Up Knee Arthroscopy Rates", subtitle="See what Medicare pays for meniscectomy (CPT 29881) and other arthroscopy codes in your area.")}

<h2 id="with-without-insurance">2. Cost with vs. without insurance</h2>

<table>
    <thead>
        <tr><th>Scenario</th><th>Total Bill</th><th>What You Pay</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer PPO (meniscectomy, deductible not met)</td><td>$12,000&ndash;$18,000</td><td>Deductible ($1,500&ndash;$3,000) + 20% until OOP max</td></tr>
        <tr><td>Employer PPO (deductible met)</td><td>$12,000&ndash;$18,000</td><td>20% coinsurance (~$1,200&ndash;$1,800) up to OOP max</td></tr>
        <tr><td>Medicare (outpatient, Part B)</td><td>APC payment</td><td>20% after Part B deductible ($257)</td></tr>
        <tr><td>Medicaid</td><td>Medicaid rate</td><td>$0&ndash;$4</td></tr>
        <tr><td>Uninsured (hospital cash price)</td><td>$12,000&ndash;$25,000</td><td>Full amount (negotiate 40&ndash;60% reduction)</td></tr>
        <tr><td>Uninsured (ASC cash price)</td><td>$5,000&ndash;$12,000</td><td>Full amount (often posted online by ASCs)</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Same surgery: $18,000 at hospital vs. $7,200 at ASC</h3>
    <p>A 34-year-old with a medial meniscus tear received a hospital quote of $18,400 for a partial meniscectomy. Her orthopedic surgeon also operated at an ASC two miles away, which quoted $7,200 for the same procedure. Both were in-network with her insurer. She chose the ASC and paid $1,440 (20% coinsurance) instead of an estimated $3,680 at the hospital&mdash;saving $2,240 in cost-sharing on a lower total bill.</p>
</div>

<h2 id="hospital-vs-asc">3. Hospital vs. ambulatory surgery center</h2>

<table>
    <thead>
        <tr><th>Setting</th><th>Typical Total Cost</th><th>Your Insurance Copay</th><th>Recovery</th></tr>
    </thead>
    <tbody>
        <tr><td>Hospital inpatient (rare for arthroscopy)</td><td>$15,000&ndash;$30,000+</td><td>Highest (inpatient deductible applies)</td><td>Overnight stay</td></tr>
        <tr><td>Hospital outpatient department</td><td>$10,000&ndash;$25,000</td><td>Moderate (facility + professional fee)</td><td>Same-day discharge</td></tr>
        <tr><td>Ambulatory surgery center (ASC)</td><td>$4,000&ndash;$12,000</td><td>Lowest (ASC facility rate)</td><td>Same-day discharge</td></tr>
    </tbody>
</table>

<p>Knee arthroscopy is almost always performed on an outpatient basis. If your surgeon recommends an overnight hospital stay for a straightforward meniscectomy, ask why&mdash;it may not be medically necessary and will significantly increase your bill.</p>

<p>Find ASCs near you in our <a href="/surgery-centers/">surgery center directory</a>.</p>

<h2 id="medicare-coverage">4. Medicare coverage</h2>

<p>Medicare covers knee arthroscopy when medically necessary. Covered indications include:</p>

<ul>
    <li>Meniscus tears (repair or meniscectomy)</li>
    <li>Loose bodies in the joint</li>
    <li>Plica syndrome</li>
    <li>ACL or PCL reconstruction</li>
    <li>Synovitis requiring synovectomy</li>
</ul>

<p><strong>Not covered: Knee arthroscopy for osteoarthritis.</strong> CMS does not cover arthroscopic lavage or debridement when the primary diagnosis is knee osteoarthritis (ICD-10: M17.x). A landmark 2002 New England Journal of Medicine trial (and subsequent evidence) found that arthroscopy for OA provides no benefit over sham surgery. If your diagnosis is primarily knee OA, Medicare will deny the claim and you will bear the full cost.</p>

<p>Arthroscopy is billed as a hospital outpatient procedure under the APC system. You pay 20% of the Medicare-approved amount after your Part B deductible. There is no separate global surgical period payment for arthroscopy under the outpatient system&mdash;follow-up visits are billed separately as office visits.</p>

<h2 id="insurance-prior-auth">5. Insurance and prior authorization</h2>

<p>Prior authorization is required by most commercial insurers for knee arthroscopy. Without it, your claim may be denied entirely. Here&rsquo;s what to expect:</p>

<ul>
    <li><strong>What insurers require for prior auth:</strong> Documentation of conservative treatment failure (typically 4&ndash;6 weeks of physical therapy), MRI or imaging confirming the diagnosis, and a letter of medical necessity from your orthopedic surgeon.</li>
    <li><strong>Timeline:</strong> Allow 5&ndash;10 business days for initial approval. Schedule surgery only after written confirmation.</li>
    <li><strong>Scope matters:</strong> Your prior auth is for the procedure as planned. If the surgeon discovers additional pathology during arthroscopy (e.g., a second meniscus tear) and performs additional procedures, those may not be covered under the original authorization. Some insurers require retroactive authorization; others don&rsquo;t cover unanticipated procedures at all.</li>
    <li><strong>Hospital vs. ASC authorization:</strong> If you switch from a hospital to an ASC (or vice versa) after receiving auth, notify your insurer. The authorization may be facility-specific.</li>
</ul>

<h2 id="cpt-codes">6. CPT codes for knee arthroscopy</h2>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Medicare Surgeon Fee (2026)</th></tr>
    </thead>
    <tbody>
        <tr><td>29870</td><td>Arthroscopy, knee, diagnostic, with or without synovial biopsy</td><td>~$500</td></tr>
        <tr><td>29871</td><td>Arthroscopy, knee, surgical; for infection, lavage, and drainage</td><td>~$550</td></tr>
        <tr><td>29873</td><td>Arthroscopy, knee, surgical; with lateral release</td><td>~$560</td></tr>
        <tr><td>29874</td><td>Arthroscopy, knee, surgical; for removal of loose body or bodies</td><td>~$560</td></tr>
        <tr><td>29875</td><td>Arthroscopy, knee, surgical; synovectomy, limited</td><td>~$580</td></tr>
        <tr><td>29877</td><td>Arthroscopy, knee, surgical; debridement/shaving of articular cartilage (chondroplasty)</td><td>~$600</td></tr>
        <tr><td>29880</td><td>Arthroscopy, knee, surgical; with meniscectomy (medial AND lateral)</td><td>~$730</td></tr>
        <tr><td>29881</td><td>Arthroscopy, knee, surgical; with meniscectomy (medial OR lateral)</td><td>~$680</td></tr>
        <tr><td>29882</td><td>Arthroscopy, knee, surgical; with meniscus repair (medial OR lateral)</td><td>~$820</td></tr>
        <tr><td>29883</td><td>Arthroscopy, knee, surgical; with meniscus repair (medial AND lateral)</td><td>~$950</td></tr>
        <tr><td>29888</td><td>Arthroscopically aided ACL repair/augmentation or reconstruction</td><td>~$1,400</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">7. Common billing errors</h2>

<p>Orthopedic billing has a <strong>36% error rate</strong>&mdash;among the highest of any medical specialty. For knee arthroscopy specifically:</p>

<ul>
    <li><strong>Upcoding the procedure:</strong> Billing a meniscus repair (29882, higher RVU) when a meniscectomy (29881) was actually performed. Repair pays more, but requires different surgical technique documented in the operative report.</li>
    <li><strong>Unbundling arthroscopy components:</strong> Billing separately for the arthroscope insertion, irrigation, and wound closure when these are included in the base arthroscopy code.</li>
    <li><strong>Billing diagnostic arthroscopy and surgical arthroscopy as separate procedures:</strong> When a diagnostic arthroscopy transitions to a surgical arthroscopy in the same session, only the surgical code is billable.</li>
    <li><strong>Modifier 50 (bilateral) errors:</strong> Bilateral knee arthroscopy is extremely rare. If modifier 50 appears on your bill, verify that both knees were actually operated on.</li>
    <li><strong>Facility fee on post-op visits:</strong> Follow-up visits within the 90-day global surgical period should not carry a facility fee if the global period is already paid.</li>
    <li><strong>Anesthesia overbilling:</strong> Anesthesia for knee arthroscopy is short (typically 45&ndash;90 minutes). Anesthesia billing is in base units + time units (15-minute increments). Verify the total time matches operative records.</li>
</ul>

<div class="cta-box">
    <h3>Think your knee arthroscopy bill has errors?</h3>
    <p>Upload your itemized bill to BillKarma. We check for upcoded procedure codes, unbundled arthroscopy components, duplicate charges, and global period violations automatically.</p>
    <a href="/fight-debt" class="cta-button">Audit My Arthroscopy Bill &rarr;</a>
</div>

<h2 id="recovery-costs">8. Recovery and PT costs after surgery</h2>

<table>
    <thead>
        <tr><th>Recovery Cost</th><th>Typical Range</th><th>Insurance Coverage</th></tr>
    </thead>
    <tbody>
        <tr><td>Physical therapy (meniscectomy, 8&ndash;16 sessions)</td><td>$800&ndash;$3,200</td><td>Usually covered with $20&ndash;$75 copay</td></tr>
        <tr><td>Physical therapy (ACL reconstruction, 30&ndash;40 sessions)</td><td>$3,000&ndash;$8,000</td><td>Usually covered; watch annual visit cap</td></tr>
        <tr><td>Crutches</td><td>$30&ndash;$150</td><td>Covered as DME under most plans</td></tr>
        <tr><td>Knee brace (functional, post-ACL)</td><td>$400&ndash;$1,200</td><td>Often covered as DME; prior auth may be required</td></tr>
        <tr><td>Ice/compression device (Game Ready, etc.)</td><td>$50&ndash;$400/week rental</td><td>Rarely covered; cash pay common</td></tr>
        <tr><td>Follow-up surgeon visits (included in global)</td><td>Typically $0</td><td>Included in surgical fee global period</td></tr>
        <tr><td>MRI if complications arise</td><td>$500&ndash;$2,500</td><td>Usually covered after deductible</td></tr>
    </tbody>
</table>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does knee arthroscopy cost without insurance?</h3>
        <p>$5,000&ndash;$25,000+ depending on the procedure. Diagnostic arthroscopy costs $5,000&ndash;$10,000. Partial meniscectomy runs $8,000&ndash;$16,000. ACL reconstruction is $15,000&ndash;$25,000+. Choosing an ASC over a hospital saves 40&ndash;60%.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover knee arthroscopy?</h3>
        <p>Yes, when medically necessary&mdash;for meniscus tears, loose bodies, ACL reconstruction, or plica syndrome. Medicare does not cover arthroscopy when the primary diagnosis is osteoarthritis. Arthroscopic debridement for OA is not covered under current CMS policy.</p>
    </div>

    <div class="faq-item">
        <h3>How much cheaper is an ASC than a hospital for knee arthroscopy?</h3>
        <p>40&ndash;60% cheaper. A meniscectomy costing $15,000 at a hospital typically runs $6,000&ndash;$9,000 at an ASC for the same procedure with the same surgeon. The lower overhead of an ASC is passed through as lower facility fees.</p>
    </div>

    <div class="faq-item">
        <h3>What is the most common billing error in knee arthroscopy?</h3>
        <p>Upcoding&mdash;billing for a meniscus repair (29882) when a meniscectomy (29881) was performed. Repairs pay more and require different documentation. Always request your operative report and compare it to the CPT codes on your bill.</p>
    </div>

    <div class="faq-item">
        <h3>Is prior authorization required for knee arthroscopy?</h3>
        <p>Almost always with commercial insurers. You typically need documentation of 4&ndash;6 weeks of failed conservative treatment and imaging confirming the diagnosis. Do not schedule surgery until you have written authorization. Medicare does not require prior auth for arthroscopy, but Medicare Advantage plans may.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (CPT 29870&ndash;29888)</a></li>
    <li><a href="https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?lcdId=34426" target="_blank" rel="noopener noreferrer">CMS: LCD for Arthroscopy of the Knee</a></li>
    <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa013259" target="_blank" rel="noopener noreferrer">Moseley et al., NEJM 2002: Controlled Trial of Arthroscopic Surgery for Osteoarthritis of the Knee</a></li>
    <li><a href="https://www.aaos.org/quality/quality-programs/knee/" target="_blank" rel="noopener noreferrer">AAOS: Knee Clinical Practice Guidelines</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Hospital Costs by Procedure</a></li>
</ul>
""",
})
