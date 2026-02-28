"""Guide: Surprise Medical Bills After Surgery: Why They Happen and How to Fight Them."""

from guides import register, _embed

register("surprise-medical-bills-after-surgery", {
    "title": "Surprise Medical Bills After Surgery: Why They Happen and How to Fight Them",
    "meta_description": "Got an unexpected bill after surgery from the anesthesiologist, assistant surgeon, or lab? Learn why post-surgery surprise bills happen and exactly how to fight each type.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Why did I get a surprise bill after surgery if my surgeon was in-network?",
            "a": "Your surgeon may be in-network, but other providers involved in your surgery often are not. Anesthesiologists, assistant surgeons, pathology labs, and even the facility itself may bill separately and may not participate in your insurance network. Each of these providers sends their own bill, and any one of them can be out-of-network even when your primary surgeon is not."
        },
        {
            "q": "Does the No Surprises Act protect me from all post-surgery surprise bills?",
            "a": "The No Surprises Act protects you from most surprise bills when you receive care at an in-network facility. Out-of-network ancillary providers like anesthesiologists and assistant surgeons cannot balance bill you if you did not consent to out-of-network care. However, the law does not cover ground ambulance services, post-stabilization care where you gave written consent, or situations where you voluntarily chose an out-of-network facility."
        },
        {
            "q": "How do I fight a surprise anesthesia bill after surgery?",
            "a": "First, check whether your surgery was at an in-network facility. If so, the No Surprises Act prohibits the anesthesiologist from balance billing you. Contact your insurer and request the claim be reprocessed at in-network rates. If the NSA does not apply, request the itemized anesthesia record, verify the base units and time units are correct, and compare the conversion factor to Medicare rates as a negotiation benchmark."
        },
        {
            "q": "What is a global surgical package and how does it affect my bill?",
            "a": "A global surgical package bundles the surgery itself, the pre-operative consultation on the day of surgery, and all routine post-operative follow-up visits for a defined period (typically 10 or 90 days depending on the procedure) into a single fee. If your surgeon bills the consultation, surgery, and follow-up visits as separate charges, they may be unbundling services that should be included in one payment."
        },
        {
            "q": "Can I be billed separately for surgical implants or devices?",
            "a": "Yes, surgical implants and devices like joint replacements, spinal hardware, or pacemakers are often billed separately from the surgeon and facility fees. Hospital markups on implants can be 200% to 500% above manufacturer cost. You can request an itemized bill showing the specific device, compare its price to the manufacturer list price, and negotiate based on the actual cost of the device."
        },
        {
            "q": "What should I do before surgery to prevent surprise bills?",
            "a": "Ask your surgeon to confirm all providers who will be involved, including the anesthesiologist, any assistant surgeon, and the pathology lab. Verify that each provider is in-network with your insurance. Request a good faith estimate in writing. Ask the facility to confirm there will be no separate facility fee. Get pre-authorization documentation and keep copies of everything."
        },
    ],
    "body": f"""
<p class="lead">You did everything right &mdash; chose an in-network surgeon, got pre-authorization, confirmed costs. Then weeks later, surprise bills arrive from the anesthesiologist, assistant surgeon, pathology lab, or the facility. A 2023 KFF survey found that <strong>1 in 4 surgical patients</strong> received at least one unexpected bill after a scheduled procedure. The average surprise post-surgery bill ranged from <strong>$1,000 to $5,000</strong>, with some exceeding $10,000. Here&rsquo;s why post-surgery surprise bills happen and exactly how to fight each type.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#common-surprise-bills">The 6 most common surprise bills after surgery</a></li>
        <li><a href="#no-surprises-act">No Surprises Act: what&rsquo;s protected now</a></li>
        <li><a href="#anesthesia-surprises">Anesthesia surprise bills</a></li>
        <li><a href="#assistant-surgeon">Assistant surgeon surprise bills</a></li>
        <li><a href="#lab-pathology">Lab and pathology surprise bills</a></li>
        <li><a href="#unbundling-upcoding">Unbundling and upcoding after surgery</a></li>
        <li><a href="#step-by-step">Step-by-step: fighting a post-surgery surprise bill</a></li>
        <li><a href="#prevention-checklist">Pre-surgery checklist to prevent surprise bills</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="common-surprise-bills">1. The 6 most common surprise bills after surgery</h2>

<p>Surgery involves far more providers than most patients realize. Your primary surgeon is just one of many people and entities that bill for their role. Each bills separately, each may have a different network status, and each sends its own invoice &mdash; often weeks apart. These are the six most common sources of surprise bills after a surgical procedure:</p>

<table>
    <thead>
        <tr>
            <th>Surprise Bill Type</th>
            <th>Why It Happens</th>
            <th>Typical Cost</th>
            <th>NSA Protected?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Out-of-network anesthesiologist</td>
            <td>Anesthesia groups are often independent contractors, not hospital employees; patient has no choice in provider</td>
            <td>$1,000&ndash;$5,000</td>
            <td>Yes, at in-network facility</td>
        </tr>
        <tr>
            <td>Assistant surgeon you didn&rsquo;t choose</td>
            <td>A second surgeon is added by the primary surgeon or hospital without the patient&rsquo;s knowledge; bills separately</td>
            <td>$2,000&ndash;$8,000</td>
            <td>Yes, at in-network facility</td>
        </tr>
        <tr>
            <td>Pathology/lab sent to OON lab</td>
            <td>Tissue samples or biopsies are sent to an out-of-network laboratory for analysis; patient is not told which lab will process them</td>
            <td>$500&ndash;$3,000</td>
            <td>Yes, at in-network facility</td>
        </tr>
        <tr>
            <td>Post-op follow-up billed separately</td>
            <td>Routine follow-up visits that should be included in the global surgical package are billed as separate office visits</td>
            <td>$200&ndash;$800 per visit</td>
            <td>Not a network issue &mdash; billing error</td>
        </tr>
        <tr>
            <td>Surgical implant/device markup</td>
            <td>Hospital marks up the cost of implants (joint replacements, screws, plates) by 200%&ndash;500% over manufacturer cost</td>
            <td>$3,000&ndash;$20,000+</td>
            <td>No &mdash; pricing dispute, not network issue</td>
        </tr>
        <tr>
            <td>Facility fee for outpatient surgery center</td>
            <td>The ambulatory surgery center or hospital charges a separate facility fee in addition to the surgeon&rsquo;s professional fee</td>
            <td>$1,500&ndash;$10,000</td>
            <td>Depends on network status of facility</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The pattern is always the same:</strong> you chose an in-network surgeon, but other providers involved in the surgery were out-of-network or billed incorrectly &mdash; and nobody told you in advance. The No Surprises Act now covers many of these situations, but not all. <a href="/scan">Upload your surgical bill to BillKarma</a> and we&rsquo;ll identify every provider on your bill and flag potential surprise charges.
</div>

<h2 id="no-surprises-act">2. No Surprises Act: what&rsquo;s protected now</h2>

<p>The <strong>No Surprises Act (NSA)</strong>, effective January 1, 2022, is the most important federal protection against surprise surgical bills. Here is what it covers and what it does not:</p>

<table>
    <thead>
        <tr>
            <th>Scenario</th>
            <th>Protected Under NSA?</th>
            <th>What You Owe</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Emergency surgery at any facility &mdash; any provider</td>
            <td>Yes &mdash; always</td>
            <td>In-network cost-sharing only</td>
        </tr>
        <tr>
            <td>Scheduled surgery at in-network facility &mdash; OON anesthesiologist</td>
            <td>Yes</td>
            <td>In-network cost-sharing only</td>
        </tr>
        <tr>
            <td>Scheduled surgery at in-network facility &mdash; OON assistant surgeon</td>
            <td>Yes</td>
            <td>In-network cost-sharing only</td>
        </tr>
        <tr>
            <td>Scheduled surgery at in-network facility &mdash; OON pathology lab</td>
            <td>Yes</td>
            <td>In-network cost-sharing only</td>
        </tr>
        <tr>
            <td>Post-stabilization care where you signed written OON consent</td>
            <td>No &mdash; consent waives protection</td>
            <td>Full OON charges possible</td>
        </tr>
        <tr>
            <td>Ground ambulance transport</td>
            <td>No &mdash; exempt from NSA</td>
            <td>Full OON charges possible</td>
        </tr>
        <tr>
            <td>Surgery at an out-of-network facility you chose</td>
            <td>No</td>
            <td>Full OON charges possible</td>
        </tr>
    </tbody>
</table>

<p><strong>The consent exception is critical.</strong> If a provider asked you to sign a form consenting to out-of-network care at least 72 hours before a scheduled procedure, NSA protections may not apply for that specific provider. However, the consent form must identify the specific provider by name, include a good-faith estimate of charges, and inform you that you have the right to refuse and request an in-network alternative. Generic surgical consent forms that mention &ldquo;additional physicians as needed&rdquo; do <em>not</em> meet this standard.</p>

<p>For a complete breakdown of the No Surprises Act, including the independent dispute resolution process, see our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a>. If you are uninsured, you have separate protections under the <a href="/guides/good-faith-estimate-rights">Good Faith Estimate</a> provisions of the law.</p>

{_embed(mode="cost", title="Check your surgical bill against Medicare rates", subtitle="Enter any CPT code from your bill to see what Medicare pays.", height="420")}

<h2 id="anesthesia-surprises">3. Anesthesia surprise bills</h2>

<p>Anesthesia is the single most common source of surprise bills after surgery. A 2020 <em>Health Affairs</em> study found that <strong>1 in 5 patients</strong> at in-network hospitals received an out-of-network anesthesia bill. The reason: most hospitals do not employ anesthesiologists directly. Instead, they contract with independent anesthesiology staffing companies that may not participate in your insurance network.</p>

<p><strong>Why it happens:</strong></p>
<ul>
    <li>Hospitals contract with third-party anesthesia staffing companies (like NorthStar Anesthesia, US Anesthesia Partners, or TeamHealth)</li>
    <li>These companies may not participate in your insurer&rsquo;s network</li>
    <li>Patients cannot choose their anesthesiologist &mdash; the hospital assigns whoever is on duty</li>
    <li>The bill arrives separately, often 3&ndash;6 weeks after surgery</li>
</ul>

<p><strong>Typical costs:</strong> Anesthesia bills range from <strong>$1,000 to $5,000+</strong> depending on the procedure, duration, and the anesthesiology group&rsquo;s billing rates. Medicare pays approximately $26 per anesthesia unit; commercial insurers negotiate $60&ndash;$150 per unit. Out-of-network groups may charge $150&ndash;$400+ per unit.</p>

<p><strong>How to fight it:</strong></p>
<ol>
    <li>Check whether the No Surprises Act applies &mdash; if your facility was in-network, the OON anesthesiologist cannot balance bill you</li>
    <li>Contact your insurer and request the claim be reprocessed at in-network rates</li>
    <li>Request the anesthesia record and verify the base units, time units, and any qualifying circumstance codes (see our <a href="/guides/anesthesia-billing">complete anesthesia billing guide</a> for details)</li>
    <li>If the NSA does not apply, negotiate using the Medicare rate as a benchmark</li>
</ol>

<div class="case-study">
    <h3>$3,200 anesthesia surprise bill eliminated after knee replacement</h3>
    <p>A 62-year-old patient in Ohio had a scheduled total knee replacement at an in-network hospital. Her surgeon was in-network. Four weeks after surgery, she received a $3,200 bill from &ldquo;Midwest Anesthesia Partners&rdquo; &mdash; a group she had never heard of. The anesthesiologist who administered her spinal block and sedation was out-of-network with her insurer.</p>
    <p>She contacted her insurer and cited the No Surprises Act: the surgery was scheduled, the facility was in-network, and she never signed a consent form specifically agreeing to out-of-network anesthesia services. The insurer reprocessed the claim at in-network rates. The allowed amount was recalculated at $780 (12 units at an in-network conversion factor of $65/unit). Her 20% coinsurance on the in-network amount: <strong>$156</strong>. The $3,200 bill was reduced to $156 &mdash; a savings of <strong>$3,044</strong>.</p>
    <p><a href="/scan">Upload your anesthesia bill to BillKarma</a> to check whether the No Surprises Act applies and compare your charges to Medicare benchmarks.</p>
</div>

<h2 id="assistant-surgeon">4. Assistant surgeon surprise bills</h2>

<p>An assistant surgeon is a second physician who helps the primary surgeon during the procedure. Patients rarely choose or even meet the assistant surgeon beforehand. The assistant bills separately using the same CPT code as the primary surgeon with a billing modifier (80, 82, or AS). Medicare reimburses assistant surgeons at <strong>16% of the primary surgeon&rsquo;s fee</strong> &mdash; but out-of-network assistants may bill thousands more.</p>

<p><strong>Typical costs:</strong> Assistant surgeon charges range from <strong>$2,000 to $8,000</strong>, with some exceeding $10,000 for complex spinal or cardiac procedures. When the assistant is out-of-network, you may be balance-billed for the difference between the billed charge and what your insurer pays.</p>

<p><strong>Key questions to ask:</strong></p>
<ul>
    <li>Did I consent to a specific out-of-network assistant surgeon? If not, the NSA applies at in-network facilities.</li>
    <li>Does my procedure code even require an assistant surgeon? Medicare classifies each CPT code with an assistant surgeon indicator. If the indicator is 0, an assistant is not typically medically necessary.</li>
    <li>What modifier was used? Modifier 80 (physician assistant surgeon), modifier 82 (no resident available), or modifier AS (PA/NP/CNS assistant).</li>
</ul>

<p>For a detailed breakdown of assistant surgeon billing modifiers, medical necessity indicators, and dispute strategies, see our <a href="/guides/surprise-assistant-surgeon-bills">complete guide to assistant surgeon bills</a>.</p>

<div class="key-takeaway">
    <strong>Check medical necessity first:</strong> If Medicare does not pay for an assistant surgeon for your procedure code (indicator = 0), you have strong grounds to dispute the entire charge &mdash; not just the out-of-network portion. Common procedures that typically do <em>not</em> require an assistant include laparoscopic gallbladder removal, arthroscopic knee surgery, and many hernia repairs.
</div>

<h2 id="lab-pathology">5. Lab and pathology surprise bills</h2>

<p>During surgery, tissue samples, biopsies, and fluid specimens are often sent to a pathology lab for analysis. The problem: you do not choose which lab processes your samples. The hospital or surgeon sends them to whichever lab they have a contract with &mdash; and that lab may be out-of-network with your insurer.</p>

<p><strong>How it works:</strong></p>
<ul>
    <li>During surgery, the surgeon removes tissue (a biopsy, a tumor, lymph nodes, etc.)</li>
    <li>The specimen is sent to a pathology lab for analysis</li>
    <li>The pathologist examines the specimen and sends a separate bill</li>
    <li>If the pathology lab is out-of-network, you may be balance-billed</li>
</ul>

<p><strong>Typical costs:</strong> Pathology bills range from <strong>$500 to $3,000</strong> depending on the complexity of the analysis. Simple tissue examination (CPT 88305) typically costs $200&ndash;$500. Advanced molecular testing or genetic analysis can exceed $5,000.</p>

<p><strong>How to fight a pathology surprise bill:</strong></p>
<ol>
    <li><strong>Check the No Surprises Act.</strong> If your surgery was at an in-network facility, the out-of-network pathologist cannot balance bill you. Contact your insurer and request reprocessing at in-network rates.</li>
    <li><strong>Verify what was actually tested.</strong> Request the pathology report and compare it to the line items on the bill. Sometimes labs bill for tests that were ordered but not performed, or bill multiple codes for what should be a single analysis.</li>
    <li><strong>Compare to Medicare rates.</strong> Pathology CPT codes have published Medicare rates. Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for each pathology code on your bill.</li>
    <li><strong>Ask why an out-of-network lab was used.</strong> If an in-network lab could have processed the specimen, ask the hospital why they chose the OON option. Some hospitals receive referral payments from specific labs.</li>
</ol>

<h2 id="unbundling-upcoding">6. Unbundling and upcoding after surgery</h2>

<p>Unbundling and upcoding are two of the most common billing errors &mdash; and sometimes fraudulent practices &mdash; in surgical billing. They inflate your bill by charging separately for services that should be included in one payment.</p>

<p><strong>Global surgical package:</strong> Medicare and most commercial insurers define a &ldquo;global surgical package&rdquo; that bundles these services into the surgeon&rsquo;s single fee:</p>
<ul>
    <li>The surgical procedure itself</li>
    <li>The pre-operative evaluation on the day of surgery (or the day before for major procedures)</li>
    <li>Local anesthesia or digital blocks administered by the surgeon</li>
    <li>All routine post-operative care for a defined period &mdash; 0 days for minor procedures, 10 days for minor procedures with a global period, or <strong>90 days for major procedures</strong></li>
</ul>

<p><strong>Common unbundling violations after surgery:</strong></p>
<ul>
    <li><strong>Billing a pre-op consultation separately.</strong> If your surgeon billed an E/M visit (99213&ndash;99215) on the day of surgery in addition to the surgical CPT code, the consultation may already be included in the global package.</li>
    <li><strong>Billing post-op visits as separate office visits.</strong> A follow-up visit 2 weeks after a major surgery to check the incision and remove sutures is included in the 90-day global period. Your surgeon should not bill this as a separate office visit.</li>
    <li><strong>Unbundling multi-component procedures.</strong> Some procedures that should be billed as a single CPT code are broken into component parts. For example, billing a complete shoulder arthroscopy as three separate procedures (debridement + rotator cuff repair + acromioplasty) when a single bundled code exists.</li>
</ul>

<div class="bill-example">
    <div class="bill-header">Surgical Bill &mdash; Example of Unbundling &mdash; Dr. Smith Orthopedics &mdash; DOS: 01/15/2026</div>
    <div class="line-item">
        <span>99214 &mdash; Office visit, established patient (pre-op eval) &nbsp; &#9888; <em>Should be included in global surgical package</em></span>
        <span>$285.00</span>
    </div>
    <div class="line-item">
        <span>29827 &mdash; Arthroscopy, shoulder, rotator cuff repair</span>
        <span>$4,800.00</span>
    </div>
    <div class="line-item flagged">
        <span>29826 &mdash; Arthroscopy, shoulder, acromioplasty &nbsp; &#9888; <em>NCCI edit: 29826 is bundled with 29827 &mdash; should not be billed separately</em></span>
        <span>$2,100.00</span>
    </div>
    <div class="line-item flagged">
        <span>99213 &mdash; Post-op follow-up visit (2 weeks) &nbsp; &#9888; <em>Within 90-day global period &mdash; included in surgical fee</em></span>
        <span>$175.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$7,360.00</span>
    </div>
    <div class="line-total">
        <span>CORRECT TOTAL (after removing unbundled charges)</span>
        <span>$4,800.00</span>
    </div>
</div>

<p>In this example, three charges are questionable: the pre-op evaluation should be included in the global package, the acromioplasty (29826) is bundled with the rotator cuff repair (29827) under CMS NCCI edits, and the post-op visit falls within the 90-day global period. The patient would overpay by <strong>$2,560</strong> if these charges are not challenged.</p>

<p><a href="/scan">Upload your surgical bill to BillKarma</a> &mdash; our system automatically checks every CPT code pair against NCCI bundling edits and flags post-op visits billed within the global surgical period.</p>

<h2 id="step-by-step">7. Step-by-step: fighting a post-surgery surprise bill</h2>

<p>Whether your surprise bill is from an out-of-network anesthesiologist, an assistant surgeon, or a pathology lab, the dispute process follows the same core steps:</p>

<ol>
    <li>
        <strong>Get the itemized bill.</strong> Request an itemized bill from every provider who billed you. The itemized bill must show each CPT code, the description of the service, the date of service, the billed amount, and the provider&rsquo;s name and NPI number. Do not settle for a summary statement.
    </li>
    <li>
        <strong>Check No Surprises Act applicability.</strong> Answer three questions: Was the surgery at an in-network facility? Was the provider who sent the surprise bill out-of-network? Did you sign a written consent specifically naming this out-of-network provider at least 72 hours before the procedure? If the facility was in-network and you did not sign specific consent, the NSA protects you.
    </li>
    <li>
        <strong>Verify all providers were in-network.</strong> Pull your insurance company&rsquo;s provider directory and check the network status of every provider on your bills &mdash; surgeon, anesthesiologist, assistant surgeon, pathologist, and facility. Document which are in-network and which are out-of-network.
    </li>
    <li>
        <strong>Compare charges to Medicare rates.</strong> Use the <a href="/calculator">BillKarma calculator</a> or the CMS Medicare Physician Fee Schedule to look up the Medicare rate for each CPT code. This gives you a benchmark for negotiation. If a provider is charging 10x the Medicare rate, you have strong leverage.
    </li>
    <li>
        <strong>File an NSA dispute or IDR request.</strong> If the No Surprises Act applies, contact your insurer and request the claim be reprocessed at in-network rates. If the provider or insurer refuses, you can initiate the independent dispute resolution (IDR) process through the federal portal at cms.gov/nosurprises. The IDR process allows a neutral arbitrator to determine the fair payment amount.
    </li>
    <li>
        <strong>Appeal to your insurance company.</strong> If your insurer denied coverage or applied the wrong benefit level, file a formal appeal. Include your itemized bill, the EOB, evidence of the provider&rsquo;s network status, and a letter explaining why the denial is incorrect. You have the right to an external review if your internal appeal is denied.
    </li>
    <li>
        <strong>File regulatory complaints.</strong> If the provider continues to balance bill you in violation of the NSA, file complaints with CMS at cms.gov/nosurprises (call 1-800-985-3059), your state insurance commissioner, and your state attorney general&rsquo;s consumer protection office.
    </li>
</ol>

<div class="case-study">
    <h3>Patient fights $11,400 in surprise bills after spinal fusion &mdash; saves $9,700</h3>
    <p>A 55-year-old patient in Florida had a scheduled two-level lumbar spinal fusion at an in-network hospital. The primary surgeon was in-network. After surgery, the patient received four separate bills totaling $11,400 beyond what insurance covered:</p>
    <ul>
        <li>$4,200 from an out-of-network assistant surgeon (modifier 80)</li>
        <li>$3,800 from an out-of-network anesthesiology group</li>
        <li>$1,900 from an out-of-network pathology lab</li>
        <li>$1,500 from the surgeon&rsquo;s office for two post-op visits billed outside the global surgical period</li>
    </ul>
    <p>The patient disputed each bill systematically. The assistant surgeon, anesthesiologist, and pathology lab bills were all covered by the No Surprises Act because the facility was in-network and the patient never signed specific OON consent forms. The insurer reprocessed all three claims at in-network rates, reducing the patient&rsquo;s combined responsibility from $9,900 to $1,200 in cost-sharing. The two post-op visits (at 2 weeks and 6 weeks) fell within the 90-day global surgical period for the spinal fusion CPT code &mdash; the surgeon&rsquo;s office removed both charges after the patient cited the global package rule. <strong>Total saved: $9,700.</strong></p>
</div>

{_embed(mode="markup", title="Check your surgical bill for overcharges", subtitle="Upload your bill to compare every line item against Medicare rates.", height="420")}

<h2 id="prevention-checklist">8. Pre-surgery checklist to prevent surprise bills</h2>

<p>The best way to fight a surprise bill is to prevent it. Use this checklist before any scheduled surgical procedure:</p>

<ol>
    <li><strong>Confirm your surgeon is in-network.</strong> Verify directly with your insurance company &mdash; not just the surgeon&rsquo;s office. Get the confirmation in writing or note the date, time, and representative&rsquo;s name.</li>
    <li><strong>Confirm the facility is in-network.</strong> The hospital or ambulatory surgery center must also be in your network. If the surgeon is in-network but operates at an out-of-network facility, you may lose NSA protections.</li>
    <li><strong>Ask who the anesthesiologist will be.</strong> Ask the surgeon&rsquo;s office or the facility which anesthesiology group staffs their operating rooms. Call the group and verify they are in-network with your insurer. See our <a href="/guides/anesthesia-billing">anesthesia billing guide</a> for what to ask.</li>
    <li><strong>Ask whether an assistant surgeon will be used.</strong> If yes, ask for their name and verify their network status. If the assistant will be out-of-network, ask the surgeon to use an in-network assistant or put in writing that you do not consent to OON assistant surgeon services.</li>
    <li><strong>Ask where lab and pathology specimens will be sent.</strong> If tissue samples will be taken, ask which lab will process them and verify the lab is in-network.</li>
    <li><strong>Request a <a href="/guides/good-faith-estimate-rights">good faith estimate</a>.</strong> Under the No Surprises Act, you have the right to a written estimate of expected charges. If the final bill exceeds the estimate by $400 or more, you can dispute the difference.</li>
    <li><strong>Get pre-authorization documentation.</strong> Keep copies of all pre-authorization approvals from your insurer. If your insurer later denies coverage, the pre-authorization documentation is evidence that they approved the procedure in advance.</li>
    <li><strong>Read consent forms carefully.</strong> Do not sign any form that waives your No Surprises Act protections unless you fully understand and accept the out-of-network charges. If you see language consenting to out-of-network care from a specific provider, ask for an in-network alternative before signing.</li>
</ol>

<p><a href="/scan">After your surgery, upload every bill you receive to BillKarma</a> &mdash; we&rsquo;ll cross-reference all providers, check network status, flag unbundling and upcoding, and compare charges to Medicare rates.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get a surprise bill after surgery if my surgeon was in-network?</h3>
        <p>Your surgeon may be in-network, but other providers involved in your surgery often are not. Anesthesiologists, assistant surgeons, pathology labs, and even the facility itself may bill separately and may not participate in your insurance network. Each sends their own bill, and any one can be out-of-network even when your primary surgeon is not. The No Surprises Act now protects you from most of these bills at in-network facilities.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act protect me from all post-surgery surprise bills?</h3>
        <p>The NSA protects you from most surprise bills when you receive care at an in-network facility. Out-of-network ancillary providers cannot balance bill you if you did not consent to out-of-network care. However, the law does not cover ground ambulance services, post-stabilization care where you gave written consent to OON providers, or situations where you voluntarily chose an out-of-network facility. Billing errors like unbundling and upcoding are separate issues not addressed by the NSA.</p>
    </div>

    <div class="faq-item">
        <h3>How do I fight a surprise anesthesia bill after surgery?</h3>
        <p>Check whether your surgery was at an in-network facility. If so, the No Surprises Act prohibits the anesthesiologist from balance billing you &mdash; contact your insurer and request reprocessing at in-network rates. If the NSA does not apply, request the itemized anesthesia record, verify the base units and time units are correct, and compare the conversion factor to Medicare&rsquo;s rate of approximately $26 per unit. See our <a href="/guides/anesthesia-billing">anesthesia billing guide</a> for detailed steps.</p>
    </div>

    <div class="faq-item">
        <h3>What is a global surgical package and how does it affect my bill?</h3>
        <p>A global surgical package bundles the surgery, the pre-operative evaluation on the day of surgery, and all routine post-operative follow-up visits for a defined period (10 or 90 days depending on the procedure) into a single fee. If your surgeon bills the consultation, surgery, and follow-ups as separate charges, they may be unbundling services that should be included in one payment. Check whether any post-op visit charges fall within the global period for your procedure&rsquo;s CPT code.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be billed separately for surgical implants or devices?</h3>
        <p>Yes, surgical implants and devices are often billed separately from surgeon and facility fees. Hospital markups on implants can be 200% to 500% above manufacturer cost. Request an itemized bill showing the specific device name, manufacturer, and model number. Compare the billed price to the manufacturer&rsquo;s list price. If the markup is extreme, negotiate based on the actual cost of the device.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do before surgery to prevent surprise bills?</h3>
        <p>Confirm that your surgeon, facility, anesthesiologist, assistant surgeon, and pathology lab are all in-network. Request a good faith estimate in writing. Get pre-authorization documentation and keep copies. Read all consent forms carefully and do not sign anything waiving your No Surprises Act protections unless you understand the out-of-network charges involved. Use the checklist in <a href="#prevention-checklist">Section 8</a> of this guide.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections and Complaint Process</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01453" target="_blank" rel="noopener">Health Affairs: Surprise Out-of-Network Billing at In-Network Hospitals (2020)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills/" target="_blank" rel="noopener">KFF: Surprise Medical Bills &mdash; Prevalence and Patient Impact Analysis</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS: Medicare Physician Fee Schedule &mdash; Global Surgery Indicators and Rates</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/medicare-correct-coding-initiative-ncci" target="_blank" rel="noopener">CMS: National Correct Coding Initiative (NCCI) &mdash; Procedure-to-Procedure Edits</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt/global-surgery-package" target="_blank" rel="noopener">American Medical Association: Global Surgical Package and Post-Operative Period Guidelines</a></li>
    <li><a href="https://www.commonwealthfund.org/publications/issue-briefs/2024/no-surprises-act-impact" target="_blank" rel="noopener">Commonwealth Fund: No Surprises Act Impact on Out-of-Network Billing Rates (2024)</a></li>
</ul>
""",
})
