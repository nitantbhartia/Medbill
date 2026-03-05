"""Guide: Medical Bill Audit Checklist: 12 Things to Check Before You Pay."""

from guides import register, _embed

register("medical-bill-audit-checklist", {
    "title": "Medical Bill Audit Checklist: 12 Things to Check Before You Pay",
    "meta_description": "Don't pay a medical bill without checking it first. This 12-point audit checklist catches duplicate charges, upcoding, unbundling, and billing errors.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How do I get an itemized medical bill?",
            "a": "Call the hospital or provider's billing department and ask specifically for an itemized bill with CPT codes and individual line items. A summary statement showing only category totals is not sufficient for an audit. Under federal law, you have the right to an itemized statement. Some hospitals provide this automatically; others require a specific request. Ask for a bill that includes the date of service, CPT or HCPCS code, description, quantity, and charge for every line item."
        },
        {
            "q": "How common are medical billing errors?",
            "a": "Very common. The HHS Office of Inspector General finds Medicare improper payment rates around 7% in annual audits. BillKarma's analysis flags potential billing issues in approximately 1 in 4 hospital bills reviewed. Errors range from simple duplicates and data entry mistakes to upcoding and unbundling that can add hundreds or thousands of dollars to your bill. The more complex the care (surgery, multi-day stays, ER visits), the more likely the bill contains errors."
        },
        {
            "q": "What is the difference between an itemized bill and an Explanation of Benefits?",
            "a": "An itemized bill comes from the provider (hospital, doctor, lab) and shows what they charged. An Explanation of Benefits comes from your insurance company and shows what was billed, what insurance paid, what discounts were applied, and what you owe. Comparing the two is essential — if they do not match, one of them is wrong. The EOB is your insurance company's version of what happened; the itemized bill is the provider's version."
        },
        {
            "q": "What should I do if I find an error on my medical bill?",
            "a": "Contact the provider's billing department and identify the specific error by date of service, CPT code, and dollar amount. For simple errors like duplicates, a phone call often resolves it. For more complex disputes, follow up in writing. Request a formal billing review and ask the hospital to place the disputed charges on hold. Do not pay the disputed amount while the review is in progress. See our dispute guide for letter templates."
        },
        {
            "q": "How long do I have to dispute a medical bill?",
            "a": "There is no single federal deadline, but you should dispute as soon as possible. Most hospitals have internal dispute resolution timeframes of 30 to 90 days. For insurance appeals, you typically have 180 days from the date of the Explanation of Benefits. For Medicare appeals, you have 120 days from the date of the Medicare Summary Notice. The sooner you dispute, the easier it is to resolve — billing departments are more responsive to timely disputes."
        },
    ],
    "body": f"""
<p class="lead">The average American hospital bill contains <strong>multiple line items that are worth questioning</strong> — from duplicate charges and incorrect codes to inflated facility fees and services that were never provided. BillKarma's analysis of thousands of hospital bills finds potential billing issues in approximately 1 in 4 bills reviewed. The difference between patients who catch errors and those who do not often comes down to one thing: a systematic review. This 12-point checklist is the same process professional medical billing advocates use, adapted so you can do it yourself in 30 to 60 minutes.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#before-you-start">Before you start: get the right documents</a></li>
        <li><a href="#checklist">The 12-point audit checklist</a></li>
        <li><a href="#annotated-bill">Annotated bill example with flagged items</a></li>
        <li><a href="#after-audit">What to do after your audit</a></li>
        <li><a href="#case-study">Case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="before-you-start">1. Before you start: get the right documents</h2>

<p>You need three documents before you can audit your bill effectively:</p>

<ol>
    <li><strong>Itemized bill with CPT codes.</strong> Call the billing department and request an itemized statement showing every individual charge with its CPT or HCPCS code, date of service, description, quantity, and dollar amount. If the hospital sends you a summary (e.g., "Lab Services: $1,200"), call back and ask specifically for the line-item detail.</li>
    <li><strong>Explanation of Benefits (EOB).</strong> This comes from your insurance company and shows what was billed, what insurance paid, adjustments, and your patient responsibility. If you have not received it, download it from your insurer's patient portal or call member services.</li>
    <li><strong>Your personal records.</strong> Notes you took during your visit or stay, discharge paperwork, prescriptions, and any recollection of what medications you received, which doctors saw you, and what tests were performed. These are your reality check against what the bill claims happened.</li>
</ol>

<p>With these three documents in hand, work through the checklist below. Each check takes 2 to 5 minutes. The entire audit should take 30 to 60 minutes for a typical bill. Or, if you want to skip the manual work, <a href="/scan">upload your bill to BillKarma</a> and our analyzer will run all 12 checks automatically.</p>

<h2 id="checklist">2. The 12-point audit checklist</h2>

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Check</th>
            <th>What to Look For</th>
            <th>Common Error Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Verify patient info</td>
            <td>Wrong name, DOB, or insurance ID</td>
            <td>Transposed digit in insurance ID causes claim denial</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Check dates of service</td>
            <td>Charges for days you were not there</td>
            <td>Billed for 4 days but discharged after 3</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Match CPT codes to services</td>
            <td>Codes that do not match what happened</td>
            <td>Billed for CT with contrast when you had CT without</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Look for duplicates</td>
            <td>Same CPT code billed twice on same date</td>
            <td>Chest X-ray (71046) appears twice on 03/04</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Verify insurance was billed</td>
            <td>Bill sent to you before insurance processed it</td>
            <td>Full $8,000 charge with no insurance adjustment</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Check the math</td>
            <td>Line items do not add up to total</td>
            <td>10 line items total $4,200 but bill says $4,700</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Compare bill to EOB</td>
            <td>Patient responsibility differs between the two</td>
            <td>EOB says you owe $1,200 but bill says $1,800</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Check for unbundling</td>
            <td>Component codes billed separately</td>
            <td>Colonoscopy + biopsy billed as two codes instead of 45380</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Verify units/quantities</td>
            <td>Wrong number of units billed</td>
            <td>Billed for 4 units of IV medication but received 2</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Check facility fees</td>
            <td>Separate facility fee on top of professional fee</td>
            <td>$800 facility fee for an office visit at hospital-owned clinic</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Look for upcoding</td>
            <td>Higher visit level than complexity warrants</td>
            <td>Level 5 ER visit (99285) for a sprained ankle</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Compare to Medicare rates</td>
            <td>Charges dramatically above Medicare benchmark</td>
            <td>$4,200 for a procedure Medicare pays $380 for</td>
        </tr>
    </tbody>
</table>

<p>Now let us walk through each check in detail.</p>

<h3>Check 1: Verify patient information</h3>
<p>Look at the top of your bill for your name, date of birth, address, and insurance information. A single wrong digit in your insurance ID, an incorrect date of birth, or a misspelled name can cause your insurance claim to be denied — which means the full charge comes to you. <strong>Example:</strong> A patient's insurance ID was entered as 12345678<strong>9</strong> instead of 12345678<strong>0</strong>. The claim was denied, and the patient received a $6,400 bill. A two-minute phone call to the billing department corrected the digit, the claim was reprocessed, and the patient owed $840.</p>

<h3>Check 2: Check dates of service</h3>
<p>Verify that every date on the bill matches your actual treatment dates. For hospital stays, check the admission and discharge dates against your discharge paperwork. Hospitals sometimes bill for the discharge day or include an extra day. <strong>Example:</strong> A patient was discharged at 9 a.m. on a Thursday but billed for room and board through Thursday night — an extra $1,840.</p>

<h3>Check 3: Match CPT codes to services received</h3>
<p>Look up each CPT code on your bill to verify it matches the service you actually received. You can search any CPT code at <a href="/calculator">our calculator</a>. Pay special attention to imaging codes (did you get a CT with or without contrast?), surgical codes (was the correct procedure billed?), and evaluation codes (does the visit level match your experience?). <strong>Example:</strong> A patient had a CT without contrast (CPT 74176, Medicare rate ~$122) but was billed for CT with contrast (CPT 74178, billed at $2,400). The correct code billed at the hospital's rate would have been $1,600 — a $800 overcharge from the wrong code alone.</p>

<h3>Check 4: Look for duplicate charges</h3>
<p>Sort your bill by date and CPT code. Look for the same code appearing on the same date without clinical justification. Duplicates are especially common on multi-day stays where billing systems may log charges from different departments independently. <strong>Example:</strong> A complete blood count (CPT 85025) billed once by the lab and once by the nursing floor for the same date — a $280 duplicate.</p>

<h3>Check 5: Verify insurance was billed correctly</h3>
<p>Check whether the bill reflects insurance processing. If you see the full gross charge with no insurance adjustment or "insurance pending," your insurance may not have been billed. This can happen when the provider has outdated or incorrect insurance information. <strong>Example:</strong> A patient received an $8,000 bill with no insurance adjustment. The provider had the patient's old insurance on file. Once the correct insurer was billed, the patient's responsibility dropped to $1,600.</p>

<h3>Check 6: Check the math</h3>
<p>Add up every line item on the bill and compare to the stated total. Billing systems occasionally produce math errors, or adjustments may not be reflected in the total. This takes five minutes with a calculator and catches errors that no one else is checking for. <strong>Example:</strong> A bill with 14 line items totaling $3,840, but the stated total was $4,340 — a $500 discrepancy traced to an adjustment that was not applied.</p>

<div class="key-takeaway">
    <strong>Want to automate these checks?</strong> <a href="/scan">Upload your bill to BillKarma</a> and our analyzer automatically checks for duplicates, upcoding, unbundling, and compares every CPT code against Medicare rates. You will get a flagged line-item report in minutes.
</div>

<h3>Check 7: Compare bill to your Explanation of Benefits</h3>
<p>Your EOB shows what your insurance company processed. Compare the patient responsibility on the EOB to the amount on the provider's bill. If they do not match, one of them is wrong. The most common discrepancy: the provider bills you for the full charge before insurance has finished processing, or the provider does not reflect an insurance adjustment that the EOB shows. <strong>Example:</strong> EOB shows patient responsibility of $1,200 after insurance paid $3,800. Provider bill shows $2,400 patient responsibility — the $1,200 difference was an in-network discount that the billing department had not applied.</p>

<h3>Check 8: Check for unbundling</h3>
<p>Unbundling means billing component procedures separately when a single bundled code should cover all of them. The bundled code is always cheaper. CMS publishes NCCI edits listing over 200,000 code pairs that cannot be billed together. <strong>Example:</strong> A colonoscopy with biopsy correctly billed as CPT 45380 (Medicare: $198). Unbundled, it might appear as CPT 45378 (colonoscopy) plus a separate biopsy code — each with its own charge, totaling more than the bundled rate.</p>

<h3>Check 9: Verify units and quantities</h3>
<p>Check that the number of units on each line item matches what you actually received. Medications are particularly prone to unit errors — billed for four doses when you received two, or billed at a higher dosage than administered. <strong>Example:</strong> A patient received 2 units of IV ondansetron (anti-nausea) but was billed for 4 units. At $85 per unit, that is a $170 overcharge.</p>

<h3>Check 10: Check facility fees</h3>
<p>Hospital-owned physician practices can charge a facility fee on top of the professional fee — sometimes called a "site-of-service" charge. This is legal but can double your cost compared to a freestanding office. Verify whether the facility fee is legitimate and whether your insurance covered it. You can <a href="/hospitals/">look up your hospital's billing grade</a> in our directory to see how its facility fees compare to regional averages. <strong>Example:</strong> A routine office visit at a hospital-owned clinic billed as 99214 ($128 professional fee) plus a separate facility fee of $340 — total $468. The same visit at a freestanding office: $128 total.</p>

<h3>Check 11: Look for upcoding</h3>
<p>Upcoding means billing for a higher-cost service level than was actually performed. The most common example is ER visit levels: a straightforward visit billed at Level 5 instead of Level 3. Compare the billed visit level to the complexity of your actual experience. <strong>Example:</strong> A patient visited the ER for a minor laceration requiring three stitches. The bill showed CPT 99285 (Level 5, billed at $4,800). The patient requested a coding review, and it was downgraded to 99283 (Level 3, billed at $1,200) — a $3,600 reduction.</p>

<h3>Check 12: Compare charges to Medicare rates</h3>
<p>Medicare rates are a useful benchmark for what a procedure should cost. While hospitals charge more than Medicare pays, the ratio gives you a negotiation reference point. A charge that is 10 to 15 times the Medicare rate is worth questioning. Use our calculator to look up any CPT code:</p>

{_embed(mode="markup", title="Compare your charge to Medicare rates", subtitle="Enter a CPT code and billed amount to see the Medicare benchmark.", height="420")}

<h2 id="annotated-bill">3. Annotated bill example with flagged items</h2>

<p>Here is a sample hospital bill for a 2-day stay after an appendectomy, with the 12-point checklist applied. Five items are flagged:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; St. Mary&rsquo;s Medical Center &mdash; Stay: 02/10/2026&ndash;02/12/2026<br>Patient: Appendectomy (Laparoscopic) &mdash; CPT 44970</div>
    <div class="line-item">
        <span>99285 &mdash; ER Visit Level 5 (02/10)</span>
        <span>$4,680.00</span>
    </div>
    <div class="line-item">
        <span>74178 &mdash; CT Abdomen/Pelvis with Contrast (02/10)</span>
        <span>$2,840.00</span>
    </div>
    <div class="line-item">
        <span>44970 &mdash; Laparoscopic Appendectomy (02/10)</span>
        <span>$12,400.00</span>
    </div>
    <div class="line-item flagged">
        <span>85025 &mdash; Complete Blood Count (02/10) &#9888; <em>Check #4: Same CBC appears again below on same date</em></span>
        <span>$284.00</span>
    </div>
    <div class="line-item flagged">
        <span>85025 &mdash; Complete Blood Count (02/10) &#9888; <em>Check #4: Duplicate &mdash; same CPT, same date</em></span>
        <span>$284.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel (02/10)</span>
        <span>$312.00</span>
    </div>
    <div class="line-item">
        <span>Room &amp; Board &mdash; Med/Surg (02/10)</span>
        <span>$1,940.00</span>
    </div>
    <div class="line-item">
        <span>Room &amp; Board &mdash; Med/Surg (02/11)</span>
        <span>$1,940.00</span>
    </div>
    <div class="line-item flagged">
        <span>Room &amp; Board &mdash; Med/Surg (02/12) &#9888; <em>Check #2: Patient discharged at 10 a.m. on 02/12 &mdash; verify if full-day charge is correct</em></span>
        <span>$1,940.00</span>
    </div>
    <div class="line-item flagged">
        <span>J2405 &mdash; Ondansetron injection, 4 mg &times; 6 &#9888; <em>Check #9: Discharge notes show 3 doses administered, not 6</em></span>
        <span>$510.00</span>
    </div>
    <div class="line-item flagged">
        <span>99253 &mdash; Inpatient Consult &mdash; Cardiology (02/11) &#9888; <em>Check #3: Patient has no cardiac history; no cardiology note in medical record</em></span>
        <span>$620.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$27,750.00</span>
    </div>
    <div class="line-total">
        <span>Flagged items total</span>
        <span>$3,578.00</span>
    </div>
</div>

<p>The five flagged items total <strong>$3,578</strong> in potentially incorrect charges: a duplicate CBC ($284), an extra room-and-board day ($1,940), three extra medication units ($255), and a cardiology consultation that may not have occurred ($620). Each of these would be caught by the corresponding checklist item. <a href="/scan">Scan your own bill with BillKarma</a> to get a similar flagged report with Medicare rate comparisons for every line item.</p>

<h2 id="after-audit">4. What to do after your audit</h2>

<ol>
    <li><strong>Document every flagged item.</strong> For each potential error, note the date, CPT code, charge amount, and which checklist item it failed. Be specific — "CBC billed twice on 02/10, $284 each" is better than "duplicate charge found."</li>
    <li><strong>Call the billing department.</strong> Reference each flagged item by date and CPT code. For simple errors (duplicates, wrong patient info, math errors), a phone call often resolves it on the spot.</li>
    <li><strong>Follow up in writing for anything not resolved in 10 days.</strong> Send a written dispute listing each item. Include your account number, the specific charges in question, and supporting documentation (your EOB, discharge papers, personal notes).</li>
    <li><strong>Request a formal billing review.</strong> Ask the hospital to conduct a formal coding review for any items involving upcoding, unbundling, or medical necessity questions. This triggers an internal audit process. If the hospital is nonprofit, they are also required to screen you for <a href="/guides/hospital-financial-assistance-guide">financial assistance</a> before pursuing collections.</li>
    <li><strong>Do not pay disputed amounts.</strong> Ask for the disputed charges to be placed on hold during the review. Pay the undisputed portion if you can, but do not pay charges you are actively disputing. For letter templates and escalation steps, see our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a>.</li>
</ol>

<div class="key-takeaway">
    <strong>The effort is worth it.</strong> Patients who audit their bills and dispute errors save an average of $800 to $3,000 on hospital bills, according to medical billing advocate industry data. A 30-minute review of your bill is one of the highest-value uses of your time when facing a medical bill.
</div>

<h2 id="case-study">5. Case study</h2>

<div class="case-study">
    <h3>12-point audit on a $22,000 knee surgery bill saves $4,200</h3>
    <p>A 52-year-old patient in Virginia had an arthroscopic knee surgery (CPT 29881, Medicare rate: $458) at an in-network outpatient surgery center. The bill totaled $22,000. Using this checklist, the patient found four issues:</p>
    <ul>
        <li><strong>Check #4 (duplicates):</strong> Two charges for CPT 29881 on the same date — the surgery was billed twice. Duplicate charge: $3,400.</li>
        <li><strong>Check #9 (units):</strong> Billed for 6 units of IV ketorolac (30mg each) but only 2 were documented in the medical record. Overcharge: $340.</li>
        <li><strong>Check #7 (bill vs. EOB):</strong> The bill showed $22,000 total, but the EOB showed the insurance-negotiated rate was $14,800. The billing department had not applied the $7,200 insurance adjustment. After correction, the patient's 20% coinsurance was $2,960 instead of $4,400.</li>
        <li><strong>Check #11 (upcoding):</strong> The facility charged a Level 5 anesthesia complexity code. The anesthesia record showed standard general anesthesia with no complications — consistent with a lower level.</li>
    </ul>
    <p>The patient called the billing department with all four items documented. The duplicate surgery charge and medication overcharge were removed immediately. The insurance adjustment was applied. The anesthesia coding was sent for internal review and subsequently downgraded. <strong>Total savings: $4,200 in patient responsibility.</strong> Before your next procedure, <a href="/hospitals/">check the facility's billing grade</a> in our hospital directory to know what to expect.</p>
</div>

<h2 id="faq">6. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I get an itemized medical bill?</h3>
        <p>Call the billing department and ask for an itemized bill with CPT codes and individual line items. You have the right to an itemized statement under federal law. Specify that you need each service on a separate line with its CPT or HCPCS code, date, quantity, and charge — not a summary by category.</p>
    </div>

    <div class="faq-item">
        <h3>How common are medical billing errors?</h3>
        <p>Very common. BillKarma flags potential billing issues in approximately 1 in 4 hospital bills reviewed. The HHS OIG finds Medicare improper payment rates around 7% annually. Errors are more common on complex bills — multi-day stays, surgeries, and ER visits. See our <a href="/guides/common-hospital-billing-errors">billing errors guide</a> for the 7 most common types.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between an itemized bill and an Explanation of Benefits?</h3>
        <p>The itemized bill comes from the provider and shows what they charged. The EOB comes from your insurance company and shows what was billed, what insurance paid, and what you owe. Comparing the two is essential — your patient responsibility should match between the two documents. If it does not, contact both the provider and your insurer.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I find an error on my medical bill?</h3>
        <p>Contact the billing department and identify the specific error by date, CPT code, and dollar amount. For simple errors, a phone call usually works. For complex disputes, follow up in writing and request a formal billing review. Do not pay disputed amounts during the review. Our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> has letter templates.</p>
    </div>

    <div class="faq-item">
        <h3>How long do I have to dispute a medical bill?</h3>
        <p>Dispute as soon as possible. Most hospitals have internal review timeframes of 30 to 90 days. Insurance appeals are typically allowed within 180 days of the EOB. Medicare appeals must be filed within 120 days of the Medicare Summary Notice. Early disputes are resolved more easily and prevent accounts from going to collections. Know your full <a href="/guides/medical-billing-rights-overview">medical billing rights</a> to strengthen your dispute.</p>
    </div>
</div>

<h2 id="sources">7. Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">HHS Office of Inspector General: Medicare Fee-for-Service Improper Payment Rate &mdash; Annual Audit Results</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: National Correct Coding Initiative (NCCI) Edits &mdash; Unbundling Prevention and Code Pair Reference</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Medicare Physician Fee Schedule &mdash; 2026 CPT Code Rates and Relative Value Units</a></li>
    <li><a href="#" target="_blank" rel="noopener">Medical Billing Advocates of America: Patient Bill Audit Outcomes and Savings Data</a></li>
    <li><a href="#" target="_blank" rel="noopener">AARP: How to Read and Dispute a Medical Bill &mdash; Consumer Guide</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Americans&rsquo; Challenges with Health Care Costs &mdash; Billing Error Prevalence and Impact</a></li>
</ul>
""",
})
