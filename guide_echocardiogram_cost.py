"""Guide: Echocardiogram Cost in 2026."""

from guides import register, _embed

register("echocardiogram-cost", {
    "title": "Echocardiogram Cost in 2026: What You'll Pay With & Without Insurance",
    "meta_description": "Echocardiogram costs range from $500 at a freestanding center to $3,000+ at a hospital. Learn what Medicare covers, how prior auth works, and how to avoid surprise bills from out-of-network cardiologists.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does an echocardiogram cost without insurance?",
            "a": "A transthoracic echocardiogram (TTE) at a hospital typically costs $1,000–$3,000 without insurance. At a freestanding cardiology imaging center, the same test often runs $500–$1,500. A transesophageal echocardiogram (TEE) averages $2,000–$5,000. A stress echocardiogram runs $1,500–$3,500. Hospital outpatient departments add a facility fee that can add $500–$1,500 to the total.",
        },
        {
            "q": "Does Medicare cover echocardiograms?",
            "a": "Yes. Medicare Part B covers echocardiograms when medically necessary — meaning there is a diagnosed or suspected cardiac condition such as coronary artery disease, heart failure, valvular disease, or unexplained symptoms (chest pain, shortness of breath, palpitations). Medicare pays 80% of the approved amount after the Part B deductible ($257 in 2026). You pay the remaining 20%.",
        },
        {
            "q": "Do I need prior authorization for an echocardiogram?",
            "a": "Prior authorization is required for most scheduled or elective echocardiograms under commercial insurance. Emergency echos during hospitalization typically do not require advance authorization. Your cardiologist's office should submit the PA request with clinical documentation. If denied as not medically necessary, your cardiologist can request a peer-to-peer review with the insurance medical director.",
        },
        {
            "q": "Why did I get two bills for one echocardiogram?",
            "a": "Echocardiograms are frequently billed in two parts: the technical component (ultrasound equipment and technician, billed by the facility) and the professional component (the cardiologist's interpretation, billed by the physician's practice). These are separate bills. Verify that the reading cardiologist is in-network even if the facility is in-network — the interpreting physician can be out-of-network and bill you separately.",
        },
        {
            "q": "What is the difference between a complete and limited echocardiogram?",
            "a": "A complete echocardiogram (CPT 93306) includes two-dimensional imaging, Doppler flow studies, and color flow mapping. A limited echocardiogram (CPT 93308) is a focused follow-up study. Complete echos are reimbursed at a higher rate. A common billing error is submitting a complete echo code when only a limited study was performed.",
        },
    ],
    "body": f"""
<p class="lead">An echocardiogram is one of the most ordered cardiac tests in the United States&mdash;and one of the most variable in price. The same transthoracic echo can cost <strong>$500 at a freestanding cardiology center</strong> or <strong>$3,000 at a hospital outpatient department</strong>. BillKarma data shows cardiac diagnostic testing has a <strong>34% billing error rate</strong>, driven largely by split component billing and out-of-network reading cardiologists. Here is what to expect in 2026.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#types-and-costs">Echo types and what each costs</a></li>
        <li><a href="#hospital-vs-center">Hospital vs. freestanding imaging center</a></li>
        <li><a href="#insurance-coverage">Insurance coverage and Medicare</a></li>
        <li><a href="#prior-auth">Prior authorization and medical necessity</a></li>
        <li><a href="#split-billing">Technical vs. professional component billing</a></li>
        <li><a href="#cpt-codes">CPT codes and common billing errors</a></li>
        <li><a href="#oon-cardiologist">How to verify your reading cardiologist is in-network</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="types-and-costs">1. Echo types and what each costs</h2>

<p>There are four main types of echocardiogram, each used for different clinical purposes:</p>

<table>
    <thead>
        <tr><th>Echo Type</th><th>What It Does</th><th>Without Insurance</th><th>With Insurance (After Deductible)</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Transthoracic (TTE)</strong></td><td>Standard external echo; evaluates heart structure and function</td><td>$500&ndash;$3,000</td><td>20% coinsurance after deductible</td></tr>
        <tr><td><strong>Transesophageal (TEE)</strong></td><td>Probe inserted in esophagus for detailed imaging; requires sedation</td><td>$2,000&ndash;$5,000</td><td>20% coinsurance after deductible</td></tr>
        <tr><td><strong>Stress echocardiogram</strong></td><td>TTE performed before and after exercise or pharmacologic stress</td><td>$1,500&ndash;$3,500</td><td>20% coinsurance after deductible</td></tr>
        <tr><td><strong>Doppler echocardiogram</strong></td><td>Measures blood flow velocity; bundled with TTE (CPT 93306)</td><td>Included in TTE cost</td><td>Included in TTE coverage</td></tr>
    </tbody>
</table>

<p>The Doppler component&mdash;which maps blood flow through the heart&rsquo;s valves and chambers&mdash;is included in CPT 93306 and should <em>not</em> be billed separately. Separate billing of Doppler when bundled in a complete TTE is a known billing error covered in the billing errors section below.</p>

<div class="key-takeaway">
    <strong>Cost-saving tip:</strong> If you have not met your deductible, ask whether a freestanding cardiology imaging center is an option. The Medicare-allowed amount for a TTE (93306) at a freestanding facility is roughly <strong>40&ndash;60% lower</strong> than at a hospital outpatient department, because hospitals add a separate facility fee. Use our <a href="/calculator">cost calculator</a> to look up the allowed rate in your area.
</div>

<h2 id="hospital-vs-center">2. Hospital vs. freestanding imaging center</h2>

<p>Where you get your echo is often the biggest cost variable. A hospital outpatient department bills using two separate charges: the facility fee (hospital overhead, equipment, staff) and the physician fee (cardiologist interpretation). A freestanding cardiology practice or imaging center typically bundles these or bills the physician fee only, resulting in significantly lower total costs.</p>

<table>
    <thead>
        <tr><th>Setting</th><th>Facility Fee?</th><th>Typical TTE Total Cost</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Hospital outpatient department</td><td>Yes ($500&ndash;$1,500)</td><td>$1,500&ndash;$3,000</td><td>Higher cost, but may be necessary for high-risk patients</td></tr>
        <tr><td>Freestanding cardiology center</td><td>No</td><td>$500&ndash;$1,500</td><td>Same test quality; significantly lower cost</td></tr>
        <tr><td>Academic medical center</td><td>Yes (higher)</td><td>$2,000&ndash;$4,000+</td><td>Teaching hospital overhead adds cost</td></tr>
    </tbody>
</table>

<p>Your cardiologist may have privileges at a hospital but also have a separate freestanding practice. Ask whether the echo can be performed at the non-hospital location. For elective echos, this simple question can save hundreds of dollars.</p>

<h2 id="insurance-coverage">3. Insurance coverage and Medicare</h2>

<p>Commercial insurance covers echocardiograms when medically necessary. Most plans pay 80% of the allowed amount after your deductible is met, leaving you with 20% coinsurance. On a $1,000 allowed amount at a freestanding center after meeting your deductible, that is a $200 patient responsibility.</p>

<p><strong>Medicare Part B coverage:</strong> Medicare covers echocardiograms as a diagnostic test under Part B when the ordering physician documents a valid medical indication. Covered indications include:</p>

<ul>
    <li>Known or suspected coronary artery disease (CAD)</li>
    <li>Heart failure evaluation or monitoring</li>
    <li>Valvular heart disease (murmur evaluation, mitral valve prolapse, etc.)</li>
    <li>Unexplained chest pain, shortness of breath, or syncope</li>
    <li>Cardiomyopathy workup</li>
    <li>Pericardial disease or effusion</li>
    <li>Pre-operative cardiac risk assessment (when clinically indicated)</li>
</ul>

<p>Medicare pays 80% of the approved amount after the <strong>$257 Part B deductible</strong> (2026). You pay 20%. If you have a Medicare supplement (Medigap) plan, it typically covers that 20%. If you are in Medicare Advantage, your plan&rsquo;s cost-sharing rules apply instead.</p>

{_embed(mode="cost", cpt="93306", title="Look up echocardiogram costs", subtitle="See what Medicare pays for echocardiograms in your area.")}

<h2 id="prior-auth">4. Prior authorization and medical necessity</h2>

<p>Most commercial insurers require prior authorization for elective echocardiograms. The process typically takes 3&ndash;10 business days. Here is how it works:</p>

<ol>
    <li><strong>Cardiologist documents the clinical indication.</strong> The ordering physician must document the specific symptoms or diagnosis justifying the echo (e.g., &ldquo;new murmur, rule out valvular disease&rdquo; or &ldquo;newly diagnosed atrial fibrillation, evaluate LV function&rdquo;).</li>
    <li><strong>Office submits PA request.</strong> Your cardiologist&rsquo;s billing or care coordination team submits the request to your insurer with supporting clinical notes.</li>
    <li><strong>Insurer applies medical necessity criteria.</strong> Most insurers use the MCG or InterQual criteria. The echo must match approved indications.</li>
    <li><strong>Authorization granted or denied.</strong> If approved, the echo can be scheduled. If denied, your cardiologist can request a peer-to-peer review within 24&ndash;72 hours&mdash;which often reverses the denial.</li>
    <li><strong>Appeal if necessary.</strong> A formal appeal with additional documentation resolves most wrongful denials. If you receive an unexpected bill after a denial, <a href="/fight-debt">BillKarma can help you navigate the appeal</a>.</li>
</ol>

<div class="key-takeaway">
    <strong>Emergency exception:</strong> If you are in the hospital or emergency department with acute cardiac symptoms, echocardiograms are typically authorized retrospectively. Do not delay emergency care waiting for PA approval.
</div>

<h2 id="split-billing">5. Technical vs. professional component billing</h2>

<p>This is the most common source of surprise echocardiogram bills. When an echo is performed, two separate services happen:</p>

<ul>
    <li><strong>Technical component:</strong> The sonographer performs the ultrasound using the facility&rsquo;s equipment. This is billed by the hospital or imaging center using modifier &ldquo;TC.&rdquo;</li>
    <li><strong>Professional component:</strong> The cardiologist reviews the images and writes the interpretation report. This is billed by the physician&rsquo;s practice using modifier &ldquo;26.&rdquo;</li>
</ul>

<p>When both are performed in a freestanding cardiology practice that employs both the sonographer and the reading cardiologist, they are often billed as a single global fee. But at hospitals, the facility and the cardiologist bill separately&mdash;and the cardiologist may be employed by a separate physician group that is <em>not in-network</em> with your insurance, even though the hospital is.</p>

<div class="case-study">
    <h3>Case study: $1,800 surprise bill from an out-of-network cardiologist</h3>
    <p><strong>Situation:</strong> A patient had a stress echocardiogram at an in-network hospital. The hospital facility fee was covered by insurance. Three weeks later, she received a bill for $1,800 from a cardiology group she had never heard of.</p>
    <p><strong>What happened:</strong> The cardiologist who interpreted her echo was employed by a separate physician group that was out-of-network with her insurance. The group billed the professional component (CPT 93350-26) separately at the out-of-network rate.</p>
    <p><strong>The outcome:</strong> Because the service occurred at an in-network facility and she had no ability to choose the interpreting cardiologist, this situation was covered by the No Surprises Act. After filing a dispute, her insurer processed the claim at the in-network rate, reducing her responsibility to her standard 20% coinsurance. <a href="/fight-debt">BillKarma can help you file an NSA dispute</a> if you face a similar situation.</p>
</div>

<h2 id="cpt-codes">6. CPT codes and common billing errors</h2>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Common Error</th></tr>
    </thead>
    <tbody>
        <tr><td>93306</td><td>TTE with Doppler and color flow mapping (complete)</td><td>Billing Doppler separately; billing complete when limited was performed</td></tr>
        <tr><td>93308</td><td>TTE limited or follow-up</td><td>Downcoding to 93308 when complete 93306 was performed (or upcoding vice versa)</td></tr>
        <tr><td>93312</td><td>Transesophageal echocardiogram</td><td>Billing without documentation of the esophageal probe placement</td></tr>
        <tr><td>93350</td><td>Stress echocardiogram (during stress testing)</td><td>Billing separately from stress test when should be bundled</td></tr>
        <tr><td>93306-TC</td><td>Technical component only</td><td>Billing global when only TC was performed (OON physician billed 26 separately)</td></tr>
    </tbody>
</table>

<p><strong>Top three billing errors in echocardiography:</strong></p>
<ul>
    <li><strong>Billing a complete echo (93306) when a limited study (93308) was performed.</strong> If your cardiologist only evaluated one aspect of heart function (e.g., checking for a pericardial effusion after a procedure), a limited echo was performed. Billing the complete code overstates the service and results in a higher patient responsibility.</li>
    <li><strong>Billing Doppler separately from 93306.</strong> CPT 93306 includes Doppler and color flow mapping. Adding separate Doppler codes (93320, 93321, 93325) is incorrect when the complete code is already billed.</li>
    <li><strong>Out-of-network interpreting cardiologist billed without disclosure.</strong> While not a coding error per se, this is the most financially damaging surprise. Always verify that the reading cardiologist is in-network before your echo.</li>
</ul>

<h2 id="oon-cardiologist">7. How to verify your reading cardiologist is in-network</h2>

<p>This step is often overlooked and is the primary cause of surprise echocardiogram bills. Take these steps before your scheduled echo:</p>

<ol>
    <li><strong>Ask the imaging facility which physician group interprets their echos.</strong> Get the name of the cardiology group, not just the individual cardiologist.</li>
    <li><strong>Look up the group in your insurer&rsquo;s provider directory.</strong> Search by group name, not individual physician name, since group contracts determine in-network status.</li>
    <li><strong>Call your insurer to confirm.</strong> Provider directories are not always current. A quick call to member services with the cardiologist&rsquo;s NPI number confirms network status in real time.</li>
    <li><strong>Get it in writing if possible.</strong> Ask for a reference number for your call. If you later receive an out-of-network bill despite verbal confirmation of in-network status, that reference number supports your appeal.</li>
    <li><strong>If the interpreting cardiologist is out-of-network,</strong> ask whether you can request in-network interpretation or have the test performed at a different facility where the reading physician is in-network.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an echocardiogram cost without insurance?</h3>
        <p>A transthoracic echocardiogram at a hospital typically costs $1,000&ndash;$3,000. At a freestanding cardiology center, the same test often runs $500&ndash;$1,500. TEE averages $2,000&ndash;$5,000. Stress echo runs $1,500&ndash;$3,500.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover echocardiograms?</h3>
        <p>Yes, when medically necessary for a documented cardiac condition. Medicare Part B pays 80% of the approved amount after the $257 Part B deductible. Covered indications include heart failure, CAD, valvular disease, cardiomyopathy, and unexplained cardiac symptoms.</p>
    </div>

    <div class="faq-item">
        <h3>Do I need prior authorization for an echocardiogram?</h3>
        <p>Yes, for most scheduled commercial insurance echos. Your cardiologist submits a PA request with clinical documentation. Emergency echos during hospitalization are typically authorized after the fact. Denials can often be reversed through peer-to-peer review.</p>
    </div>

    <div class="faq-item">
        <h3>Why did I get two bills for one echocardiogram?</h3>
        <p>Echos are billed in two parts: the technical component (facility fee for the ultrasound) and the professional component (cardiologist&rsquo;s interpretation). These are separate bills, often from separate entities. Always verify the reading cardiologist is in-network before your test.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a complete and limited echocardiogram?</h3>
        <p>A complete TTE (CPT 93306) includes 2D imaging, Doppler, and color flow mapping. A limited echo (CPT 93308) is a focused follow-up study. Billing a complete echo code when a limited study was performed is one of the most common echocardiogram billing errors.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">American College of Cardiology: Appropriate Use Criteria for Echocardiography (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Medicare Part B Fee Schedule (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Society of Echocardiography: Guidelines for Performing a Comprehensive Adult TTE (2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: No Surprises Act Implementation (2022&ndash;2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Healthcare Bluebook: Echocardiogram Fair Price Data (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">JAMA Internal Medicine: Facility Fee Variation in Cardiac Diagnostics (2024)</a></li>
</ul>
""",
})
