"""Guide: Medical Billing and Coding Mistakes."""

from guides import register, _embed

register("medical-billing-coding-mistakes", {
    "title": "10 Medical Billing and Coding Mistakes That Cost You Money",
    "meta_description": "Medical billing errors inflate 30-80% of hospital bills. Learn the 10 most common coding mistakes, how to spot them, and how to get overcharges reversed.",
    "published": "2026-03-01",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How common are medical billing errors?",
            "a": "Studies consistently find that 30&ndash;80% of medical bills contain at least one error. The American Medical Association estimates that 7.1% of paid claims contain coding mistakes, and an analysis by Equifax found errors on 49% of Medicare claims. For patients, this translates to an average overcharge of $935 per billing error that goes undetected.",
        },
        {
            "q": "What is upcoding on a medical bill?",
            "a": "Upcoding occurs when a provider bills a higher-level service code than the care actually delivered. For example, billing a Level 5 office visit (CPT 99215) when the documentation only supports a Level 3 visit (CPT 99213). Upcoding inflates the charge by $100&ndash;$400 per visit and is one of the most common billing errors found on outpatient bills.",
        },
        {
            "q": "What is unbundling in medical billing?",
            "a": "Unbundling is billing individual components of a procedure as separate line items when they should be billed under a single bundled code. For example, billing each step of a blood panel as a separate test instead of using the comprehensive panel code. Unbundling typically inflates bills by 25&ndash;75% above what the bundled rate would be. The CMS National Correct Coding Initiative (NCCI) maintains official edit pairs that define which codes should not be billed together.",
        },
        {
            "q": "How do I check my medical bill for coding errors?",
            "a": "Start by requesting an itemized bill with CPT codes, ICD-10 diagnosis codes, and dates of service. Compare each CPT code against the Medicare rate using a cost lookup tool. Look for duplicate charges on the same date, codes that don&rsquo;t match the service you received, and charges for services you don&rsquo;t remember getting. Upload your bill to BillKarma for an automated audit that flags upcoding, unbundling, duplicates, and pricing outliers.",
        },
        {
            "q": "Can I get a refund for medical billing errors?",
            "a": "Yes. If you identify a coding error on your bill, contact the provider&rsquo;s billing department with the specific CPT code, date of service, and explanation of the error. Most providers will correct legitimate coding mistakes and issue a refund or credit within 30&ndash;60 days. If the provider refuses, you can escalate by filing a complaint with your state insurance commissioner or, for Medicare claims, contacting CMS directly.",
        },
        {
            "q": "What is the difference between a billing error and fraud?",
            "a": "A billing error is an unintentional mistake in coding or data entry, such as transposing digits in a CPT code or accidentally billing a service twice. Fraud is the intentional submission of false claims for payment, such as systematically upcoding every patient visit or billing for services never rendered. Both cost patients money, but fraud carries criminal penalties under the False Claims Act. If you suspect fraud, report it to the HHS Office of Inspector General.",
        },
    ],
    "body": f"""
<p class="lead">Up to <strong>80% of medical bills</strong> contain at least one error, and the average overcharge is <strong>$935</strong>. Coding mistakes &mdash; wrong CPT codes, unbundled procedures, duplicate charges &mdash; are the single biggest driver of inflated hospital bills. Most patients pay without checking because medical bills are designed to be unreadable. This guide breaks down the 10 most common medical billing and coding mistakes, shows you exactly what each one looks like on a real bill, and gives you a step-by-step process to catch and reverse them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-common">How common are medical billing and coding errors?</a></li>
        <li><a href="#upcoding">Mistake #1: Upcoding</a></li>
        <li><a href="#unbundling">Mistake #2: Unbundling</a></li>
        <li><a href="#duplicate-charges">Mistake #3: Duplicate charges</a></li>
        <li><a href="#wrong-diagnosis">Mistake #4: Wrong diagnosis code</a></li>
        <li><a href="#modifier-phantom-info">Mistakes #5&ndash;7: Modifier errors, phantom charges, wrong patient info</a></li>
        <li><a href="#or-time-units-balance">Mistakes #8&ndash;10: OR time inflation, incorrect units, balance billing errors</a></li>
        <li><a href="#how-to-audit">How to audit your own bill for coding mistakes</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-common">1. How common are medical billing and coding errors?</h2>

<p>Medical billing errors are not rare exceptions &mdash; they are the norm. Multiple independent studies have measured error rates ranging from 30% to 80% of all medical bills:</p>

<ul>
    <li><strong>Equifax</strong> found errors on 49% of Medicare claims reviewed.</li>
    <li>The <strong>American Medical Association</strong> reports a 7.1% error rate on paid claims, translating to billions in annual overcharges.</li>
    <li><strong>NerdWallet</strong> estimated that billing errors contribute to $210 billion in unnecessary healthcare costs per year in the United States.</li>
    <li>A <strong>JAMA study</strong> found that 30&ndash;40% of bills for surgical procedures contained at least one coding error.</li>
    <li>Professional medical bill auditors report finding errors on <strong>70&ndash;80%</strong> of the bills they review.</li>
</ul>

<p>The average overcharge per billing error is <strong>$935</strong>, according to data compiled from consumer advocacy organizations and billing audit firms. For hospital stays and surgical procedures, the average overcharge climbs to <strong>$1,300&ndash;$2,500</strong>.</p>

<div class="key-takeaway">
    <strong>Why errors persist:</strong> Medical billing uses over 80,000 <a href="/guides/what-are-cpt-codes">CPT codes</a> and 72,000 <a href="/guides/icd10-drg-codes">ICD-10 diagnosis codes</a>. Human coders process dozens of charts per day under productivity pressure. Errors are inevitable &mdash; and they almost always favor the provider, not the patient. <a href="/scan">Upload your bill to BillKarma</a> to check for errors in seconds.
</div>

<h2 id="upcoding">2. Mistake #1: Upcoding</h2>

<p>Upcoding is billing a higher-level service code than the documentation supports. It is the single most expensive coding mistake for patients.</p>

<p>Evaluation and management (E/M) codes &mdash; the codes used for office visits &mdash; are ranked by complexity from Level 1 (CPT 99211, minimal visit) to Level 5 (CPT 99215, high-complexity visit). Each level has a higher reimbursement rate. When a provider bills a Level 4 or 5 visit for what was actually a straightforward Level 3 encounter, the patient pays significantly more:</p>

<table>
    <thead>
        <tr><th>E/M Code</th><th>Description</th><th>Medicare Rate (2026)</th><th>Typical Hospital Charge</th></tr>
    </thead>
    <tbody>
        <tr><td>99213</td><td>Level 3 &mdash; Established patient, low complexity</td><td>~$112</td><td>$180&ndash;$350</td></tr>
        <tr><td>99214</td><td>Level 4 &mdash; Established patient, moderate complexity</td><td>~$165</td><td>$250&ndash;$550</td></tr>
        <tr><td>99215</td><td>Level 5 &mdash; Established patient, high complexity</td><td>~$224</td><td>$350&ndash;$800</td></tr>
    </tbody>
</table>

<p>If your 15-minute follow-up visit for a stable condition is billed as a 99215 instead of a 99213, the difference can be <strong>$150&ndash;$450</strong>. Over multiple visits, upcoding adds up to thousands in excess charges.</p>

<h3>How to spot upcoding</h3>
<ul>
    <li>Request your medical records for the visit and compare the documentation against the <a href="/guides/what-are-cpt-codes">CPT code</a> billed.</li>
    <li>A Level 4 or 5 visit requires documented medical decision-making of moderate or high complexity. If your visit was routine, a high-level code is suspect.</li>
    <li>Compare the time spent with you (ask front-desk staff or check your patient portal) against the code billed. Level 5 visits typically require 40+ minutes of physician time.</li>
</ul>

<div class="case-study">
    <h3>Case study: Upcoding caught and reversed &mdash; $1,240 refund</h3>
    <p>A 38-year-old woman in Virginia visited her primary care physician for a routine follow-up on controlled hypertension. The visit lasted 12 minutes. Her bill showed CPT 99215 (Level 5, high-complexity visit) at $410 per visit &mdash; for three consecutive visits over six months, totaling $1,230 in professional fees. She requested her visit notes, which documented stable blood pressure, no medication changes, and a simple &ldquo;continue current plan&rdquo; assessment. She filed a dispute citing that the documentation supported a 99213 (Level 3) code. The practice recoded all three visits, applied the 99213 rate of $185, and issued a refund of <strong>$1,240</strong> (including a duplicate charge on one visit).</p>
</div>

<h2 id="unbundling">3. Mistake #2: Unbundling</h2>

<p>Unbundling occurs when a provider bills individual components of a procedure separately instead of using a single bundled <a href="/guides/what-are-cpt-codes">CPT code</a> that covers the entire procedure. This inflates the total bill because the sum of individual component codes is always higher than the bundled rate.</p>

<p>The CMS National Correct Coding Initiative (NCCI) maintains a database of code pairs that should never be billed together because one code already includes the other. Common unbundling examples:</p>

<ul>
    <li><strong>Lab panels:</strong> Billing glucose, sodium, potassium, CO2, BUN, and creatinine individually instead of as a comprehensive metabolic panel (CPT 80053). Individual tests: $180&ndash;$360. Panel code: $45&ndash;$120.</li>
    <li><strong>Surgical procedures:</strong> Billing the incision, tissue removal, and wound closure as three separate procedures when one surgical CPT code covers all three steps.</li>
    <li><strong>Imaging:</strong> Billing the technical component and professional component of an X-ray separately without proper modifiers, resulting in a higher total than the global code.</li>
</ul>

<div class="key-takeaway">
    <strong>Unbundling red flag:</strong> If your bill shows 5 or more individual lab test codes on the same date of service, check whether a panel code (CPT 80048, 80050, 80053, or 80076) would cover them. Panel codes are almost always 50&ndash;70% cheaper than the sum of individual tests. Use our <a href="/calculator">calculator</a> to look up the Medicare rate for each code.
</div>

<div class="case-study">
    <h3>Case study: Unbundling dispute won &mdash; $780 reduced to $95</h3>
    <p>A 55-year-old man in Ohio received a lab bill for $780 after a routine annual physical. The bill listed 14 individual lab test codes. His doctor had ordered a comprehensive metabolic panel and a lipid panel &mdash; two tests that should have been billed under CPT 80053 and CPT 80061. He contacted the lab billing department with a printout of the NCCI edit pairs showing that the individual codes were components of the panel codes. The lab recoded the claim and the corrected bill was <strong>$95</strong>. Savings: <strong>$685</strong>.</p>
</div>

<h2 id="duplicate-charges">4. Mistake #3: Duplicate charges</h2>

<p>Duplicate charges are the simplest billing error to identify: the same service, on the same date, billed twice. They are also among the most common, particularly on hospital inpatient bills where multiple departments enter charges independently.</p>

<p>Duplicates happen for several reasons:</p>
<ul>
    <li>A nurse records a medication administration and a pharmacist separately enters the same charge.</li>
    <li>A procedure is scheduled, canceled, and rescheduled &mdash; but the original charge is never removed.</li>
    <li>A service is billed under both a facility and professional claim when only one is appropriate.</li>
    <li>Electronic health record (EHR) system glitches create duplicate entries during data transfers.</li>
</ul>

<p>On a typical 5-day hospital stay, professional auditors find an average of <strong>2&ndash;4 duplicate charges</strong> worth $200&ndash;$1,500 in total.</p>

<h3>How to spot duplicates</h3>
<p>Request an itemized bill sorted by date of service. Look for identical CPT codes on the same date. Pay special attention to high-frequency items like medications, IV supplies, lab draws, and vital sign monitoring charges.</p>

<h2 id="wrong-diagnosis">5. Mistake #4: Wrong diagnosis code</h2>

<p>Every medical service is linked to an <a href="/guides/icd10-drg-codes">ICD-10 diagnosis code</a> that explains <em>why</em> the service was provided. A wrong diagnosis code creates two problems: it can cause your insurance to deny the claim (leaving you with the full bill), or it can justify a more expensive treatment pathway than what you actually needed.</p>

<p>Common diagnosis code errors include:</p>
<ul>
    <li><strong>Transposed digits:</strong> ICD-10 codes are alphanumeric (e.g., E11.65 for Type 2 diabetes with hyperglycemia). Swapping two characters can change the diagnosis entirely.</li>
    <li><strong>Laterality errors:</strong> Coding a right knee procedure with a left knee diagnosis code, which can trigger a denial.</li>
    <li><strong>Unspecified vs. specified codes:</strong> Using a vague code (like &ldquo;abdominal pain, unspecified&rdquo;) instead of the correct specific diagnosis, which may not support the services billed.</li>
    <li><strong>Rule-out diagnoses billed as confirmed:</strong> Billing for a confirmed diagnosis when the physician was only ruling it out, potentially triggering more expensive treatment protocols.</li>
</ul>

<div class="key-takeaway">
    <strong>Diagnosis code errors and insurance denials:</strong> If your insurance denied a claim as &ldquo;not medically necessary,&rdquo; the first thing to check is whether the diagnosis code matches the service. A wrong ICD-10 code is the most common reason for medical necessity denials. Ask the provider to review and correct the diagnosis code, then resubmit the claim. See our <a href="/guides/common-hospital-billing-errors">guide to common billing errors</a> for more denial triggers.
</div>

<h2 id="modifier-phantom-info">6. Mistakes #5&ndash;7: Modifier errors, phantom charges, wrong patient info</h2>

<h3>Mistake #5: Modifier errors</h3>

<p>CPT modifiers are two-digit codes appended to a procedure code to indicate special circumstances &mdash; for example, modifier -25 indicates a significant, separately identifiable E/M service on the same day as a procedure. Missing or incorrect modifiers cause denials, delayed payments, and incorrect patient responsibility calculations. The most common modifier errors:</p>
<ul>
    <li>Missing modifier -59 (distinct procedural service), causing a bundling denial when two procedures were legitimately performed separately.</li>
    <li>Incorrect use of modifier -25, which adds the full E/M fee to a procedure visit when the office visit was not separately documentable.</li>
    <li>Applying modifier -50 (bilateral procedure) instead of billing both sides separately, or vice versa, resulting in under- or over-payment.</li>
</ul>

<h3>Mistake #6: Phantom charges</h3>

<p>Phantom charges are line items on your bill for services, supplies, or procedures you never received. They are disturbingly common on hospital inpatient bills. Examples include:</p>
<ul>
    <li>Charges for a physical therapy session that was ordered but never completed because you were discharged.</li>
    <li>Supply charges for a surgical tray that was opened but not used during your procedure.</li>
    <li>Medications listed on your bill that were prescribed but never administered.</li>
</ul>
<p>The only way to catch phantom charges is to keep a personal log of treatments and medications during a hospital stay and compare it against the itemized bill.</p>

<h3>Mistake #7: Wrong patient information</h3>

<p>Data entry errors in patient demographics &mdash; wrong date of birth, misspelled name, incorrect insurance ID &mdash; cause claims to be denied or applied to the wrong account. While these errors don&rsquo;t inflate your bill directly, they create cascading problems: denied claims generate patient bills for amounts the insurance should have covered, and charges applied to the wrong account can lead to collections on debts you don&rsquo;t owe.</p>

<h2 id="or-time-units-balance">7. Mistakes #8&ndash;10: OR time inflation, incorrect units, balance billing errors</h2>

<h3>Mistake #8: Operating room time inflation</h3>

<p>Hospitals bill operating room time in 15-minute increments, and the charges range from <strong>$150 to $300+ per increment</strong> depending on the facility. Inflated OR time is one of the hardest errors to detect because most patients don&rsquo;t know how long their surgery actually took. Common issues:</p>
<ul>
    <li>Billing OR time from the moment the room is reserved, not when the surgery begins.</li>
    <li>Including setup and cleanup time in the surgical time charged to the patient.</li>
    <li>Rounding up aggressively &mdash; a 47-minute procedure billed as 75 minutes (5 increments instead of 4).</li>
</ul>
<p>Request the anesthesia record, which independently documents the exact start and end time of the surgical procedure. Compare this against the OR time on your hospital bill.</p>

<h3>Mistake #9: Incorrect units</h3>

<p>Some services are billed per unit &mdash; each unit representing a specific quantity or time interval. Incorrect unit counts are especially common in:</p>
<ul>
    <li><strong>Anesthesia billing:</strong> Anesthesia is billed in 15-minute units. A 90-minute surgery should be 6 units, not 8.</li>
    <li><strong>IV medications:</strong> A 500mg dose billed as 5 units of 100mg vials when only 3 vials were used.</li>
    <li><strong>Physical therapy:</strong> Therapy is billed in 8-minute units. A 45-minute session should be 5 units (based on the 8-minute rule), not 6.</li>
</ul>

<h3>Mistake #10: Balance billing errors</h3>

<p>Balance billing occurs when an out-of-network provider bills you for the difference between their charge and what your insurance paid. Under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a>, balance billing is prohibited for emergency services and for out-of-network providers at in-network facilities. Yet balance billing errors persist because:</p>
<ul>
    <li>Providers may not update their billing systems to reflect No Surprises Act protections.</li>
    <li>Ancillary providers (anesthesiologists, pathologists, radiologists) at in-network hospitals may incorrectly bill out-of-network rates.</li>
    <li>Some providers continue to send balance bills hoping patients will pay without questioning them.</li>
</ul>

<h2 id="the-10-mistakes">Summary: The 10 mistakes at a glance</h2>

<table>
    <thead>
        <tr><th>#</th><th>Mistake</th><th>How Often It Occurs</th><th>Average Overcharge</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>Upcoding (higher E/M code than warranted)</td><td>25&ndash;30% of outpatient bills</td><td>$150&ndash;$450 per visit</td></tr>
        <tr><td>2</td><td>Unbundling (billing components separately)</td><td>15&ndash;20% of lab and surgical bills</td><td>$200&ndash;$800 per occurrence</td></tr>
        <tr><td>3</td><td>Duplicate charges</td><td>10&ndash;15% of hospital bills</td><td>$200&ndash;$1,500 per stay</td></tr>
        <tr><td>4</td><td>Wrong diagnosis code (ICD-10 errors)</td><td>10&ndash;20% of claims</td><td>Varies widely; causes denials</td></tr>
        <tr><td>5</td><td>Modifier errors</td><td>5&ndash;10% of procedural claims</td><td>$100&ndash;$600 per claim</td></tr>
        <tr><td>6</td><td>Phantom charges (services not rendered)</td><td>5&ndash;12% of inpatient bills</td><td>$150&ndash;$1,000 per occurrence</td></tr>
        <tr><td>7</td><td>Wrong patient information</td><td>5&ndash;8% of claims</td><td>Causes denials, not direct overcharge</td></tr>
        <tr><td>8</td><td>Operating room time inflation</td><td>10&ndash;15% of surgical bills</td><td>$300&ndash;$1,200 per surgery</td></tr>
        <tr><td>9</td><td>Incorrect units (time, dosage, quantity)</td><td>5&ndash;10% of procedural bills</td><td>$100&ndash;$800 per occurrence</td></tr>
        <tr><td>10</td><td>Balance billing errors</td><td>5&ndash;15% of out-of-network claims</td><td>$500&ndash;$5,000+ per episode</td></tr>
    </tbody>
</table>

<h2 id="bill-example">Real bill example: three coding errors on one statement</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Regional Medical Center &mdash; Date of Service: 02/10/2026</div>
    <div class="line-item flagged">
        <span>99215 &mdash; Office visit, established patient, Level 5 &nbsp; &#9888; <em>Upcoding: visit notes document a 15-min follow-up (supports 99213, not 99215)</em></span>
        <span>$420.00</span>
    </div>
    <div class="line-item">
        <span>36415 &mdash; Venipuncture (blood draw)</span>
        <span>$35.00</span>
    </div>
    <div class="line-item flagged">
        <span>82947 &mdash; Glucose, quantitative &nbsp; &#9888; <em>Unbundling: part of comprehensive metabolic panel (80053)</em></span>
        <span>$78.00</span>
    </div>
    <div class="line-item flagged">
        <span>82310 &mdash; Calcium, total &nbsp; &#9888; <em>Unbundling: part of comprehensive metabolic panel (80053)</em></span>
        <span>$65.00</span>
    </div>
    <div class="line-item flagged">
        <span>84443 &mdash; TSH (thyroid stimulating hormone) &nbsp; &#9888; <em>Unbundling: part of comprehensive metabolic panel (80053)</em></span>
        <span>$92.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive metabolic panel</span>
        <span>$112.00</span>
    </div>
    <div class="line-item flagged">
        <span>99215 &mdash; Office visit, established patient, Level 5 &nbsp; &#9888; <em>Duplicate: same CPT code billed twice on the same date</em></span>
        <span>$420.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$1,222.00</span>
    </div>
</div>

<p><strong>After corrections:</strong></p>
<ul>
    <li>99215 recoded to 99213: $420 &rarr; $185 (and duplicate removed: &ndash;$420)</li>
    <li>Individual lab tests removed (already included in 80053 panel): &ndash;$235</li>
    <li><strong>Corrected total: $344.00</strong> &mdash; a savings of <strong>$878</strong></li>
</ul>

{_embed(mode="cost", cpt="99215", title="Look up Medicare rates for your bill codes", subtitle="Enter any CPT code from your bill to see what Medicare actually pays.")}

<div class="key-takeaway">
    <strong>Three errors, one bill, $878 in overcharges.</strong> This is typical. Most patients would have paid the full $1,222 without questioning it. <a href="/scan">Upload your bill to BillKarma</a> &mdash; we&rsquo;ll flag upcoding, unbundling, duplicates, and pricing outliers automatically, then show you exactly what to dispute.
</div>

<h2 id="how-to-audit">8. How to audit your own bill for coding mistakes</h2>

<p>You do not need medical billing expertise to catch the most common errors. Follow these five steps using the tools linked below. For a comprehensive checklist, see our <a href="/guides/medical-bill-audit-checklist">medical bill audit checklist</a>.</p>

<p><strong>Step 1 &mdash; Request an itemized bill.</strong> Call the provider&rsquo;s billing department and ask for a complete itemized statement that includes CPT codes, ICD-10 diagnosis codes, dates of service, and quantities. Do not accept a summary statement that only shows department totals. You have the legal right to an itemized bill under HIPAA.</p>

<p><strong>Step 2 &mdash; Check for duplicates.</strong> Sort or scan the bill by date of service. Look for the same CPT code appearing twice on the same date. Flag any duplicates immediately &mdash; these are the easiest errors to get reversed.</p>

<p><strong>Step 3 &mdash; Verify the E/M code level.</strong> If you had an office visit, check whether the E/M code (99211&ndash;99215 for established patients, 99201&ndash;99205 for new patients) matches the complexity of your visit. A routine follow-up for a stable condition should not be billed at Level 4 or 5. Request your visit notes through your patient portal and compare.</p>

<p><strong>Step 4 &mdash; Look for unbundled lab tests.</strong> If your bill shows multiple individual lab test codes, check whether they are components of a standard panel (comprehensive metabolic panel CPT 80053, basic metabolic panel CPT 80048, or lipid panel CPT 80061). If so, the panel code should have been used instead.</p>

<p><strong>Step 5 &mdash; Compare against Medicare rates.</strong> Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for each CPT code on your bill. Any charge exceeding 3x the Medicare rate is worth questioning. For a full walkthrough on <a href="/guides/common-hospital-billing-errors">common hospital billing errors</a> and how to dispute them, see our dedicated guide.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t want to audit manually?</strong> <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll run all five checks automatically. Our system flags upcoding, unbundling, duplicates, diagnosis code mismatches, and pricing outliers &mdash; then generates a dispute letter you can send to the billing department. See also our guides on <a href="/guides/medical-billing-errors-statistics-2026">medical billing error statistics</a> and <a href="/guides/icd10-drg-codes">ICD-10 and DRG codes</a> for additional context.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How common are medical billing errors?</h3>
        <p>Studies consistently find that 30&ndash;80% of medical bills contain at least one error. The American Medical Association estimates that 7.1% of paid claims contain coding mistakes, and an analysis by Equifax found errors on 49% of Medicare claims. For patients, this translates to an average overcharge of $935 per billing error that goes undetected.</p>
    </div>

    <div class="faq-item">
        <h3>What is upcoding on a medical bill?</h3>
        <p>Upcoding occurs when a provider bills a higher-level service code than the care actually delivered. For example, billing a Level 5 office visit (CPT 99215) when the documentation only supports a Level 3 visit (CPT 99213). Upcoding inflates the charge by $100&ndash;$400 per visit and is one of the most common billing errors found on outpatient bills.</p>
    </div>

    <div class="faq-item">
        <h3>What is unbundling in medical billing?</h3>
        <p>Unbundling is billing individual components of a procedure as separate line items when they should be billed under a single bundled code. For example, billing each step of a blood panel as a separate test instead of using the comprehensive panel code. Unbundling typically inflates bills by 25&ndash;75% above what the bundled rate would be.</p>
    </div>

    <div class="faq-item">
        <h3>How do I check my medical bill for coding errors?</h3>
        <p>Start by requesting an itemized bill with CPT codes, ICD-10 diagnosis codes, and dates of service. Compare each CPT code against the Medicare rate using a cost lookup tool. Look for duplicate charges on the same date, codes that don&rsquo;t match the service you received, and charges for services you don&rsquo;t remember getting. <a href="/scan">Upload your bill to BillKarma</a> for an automated audit that flags upcoding, unbundling, duplicates, and pricing outliers.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get a refund for medical billing errors?</h3>
        <p>Yes. If you identify a coding error on your bill, contact the provider&rsquo;s billing department with the specific CPT code, date of service, and explanation of the error. Most providers will correct legitimate coding mistakes and issue a refund or credit within 30&ndash;60 days. If the provider refuses, you can escalate by filing a complaint with your state insurance commissioner or, for Medicare claims, contacting CMS directly.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a billing error and fraud?</h3>
        <p>A billing error is an unintentional mistake in coding or data entry, such as transposing digits in a CPT code or accidentally billing a service twice. Fraud is the intentional submission of false claims for payment, such as systematically upcoding every patient visit or billing for services never rendered. Both cost patients money, but fraud carries criminal penalties under the False Claims Act. If you suspect fraud, report it to the HHS Office of Inspector General.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ama-assn.org/practice-management/cpt/national-health-insurer-report-card" target="_blank" rel="noopener">American Medical Association &mdash; National Health Insurer Report Card: Claims Processing Accuracy</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" target="_blank" rel="noopener">CMS &mdash; National Correct Coding Initiative (NCCI) Edits: Bundling Rules and Code Pair Tables</a></li>
    <li><a href="https://jamanetwork.com/journals/jama-surgery/fullarticle/2771370" target="_blank" rel="noopener">JAMA Surgery &mdash; Prevalence and Cost of Billing Errors in Surgical Claims</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS &mdash; Medicare Physician Fee Schedule: 2026 Rate Tables and E/M Code Valuations</a></li>
    <li><a href="https://oig.hhs.gov/reports-and-publications/featured-topics/upcoding/" target="_blank" rel="noopener">HHS Office of Inspector General &mdash; Reports on Upcoding in Medicare Claims</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Balance Billing Protections and Patient Rights</a></li>
    <li><a href="https://www.nerdwallet.com/article/health/medical-billing-errors" target="_blank" rel="noopener">NerdWallet &mdash; Medical Billing Errors: How They Happen and What They Cost</a></li>
</ul>
""",
})
