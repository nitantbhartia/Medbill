"""Guide: ICD-10 and DRG Codes: How Diagnosis Codes Affect Your Hospital Bill."""

from guides import register, _embed

register("icd10-drg-codes", {
    "title": "ICD-10 and DRG Codes: How Diagnosis Codes Affect Your Hospital Bill",
    "meta_description": "A wrong DRG code can inflate your hospital bill by $14,000 or more. Learn how ICD-10 and DRG codes work, how upcoding happens, and how to verify your coding.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is an ICD-10 code on my medical bill?",
            "a": "An ICD-10 code is a standardized diagnosis code from the International Classification of Diseases, 10th Revision. Every diagnosis, symptom, and medical condition has a unique alphanumeric code. For example, I10 is essential hypertension and S72.001A is a fracture of the right femoral neck. These codes are assigned by your provider to describe why you received treatment. They determine what your insurer will pay, how your claim is processed, and in many cases, how much the hospital receives."
        },
        {
            "q": "What is a DRG and how does it affect my bill?",
            "a": "A Diagnosis-Related Group is a classification system used to determine how much Medicare and many commercial insurers pay hospitals for inpatient stays. Each DRG has a fixed payment amount based on the average cost of treating patients with that condition. The DRG is assigned based on your ICD-10 diagnosis codes, procedures performed, age, and whether you had complications or comorbidities. A higher-severity DRG results in a higher payment to the hospital."
        },
        {
            "q": "What is upcoding and how do I spot it?",
            "a": "Upcoding is the practice of assigning a more severe diagnosis code or DRG than the patient's condition warrants, resulting in a higher payment to the hospital. Signs of upcoding include diagnosis codes for conditions not documented in your medical record, a DRG with major complications when your stay was uncomplicated, and charges that seem disproportionate to the care you received. You can request your medical record and compare the documented conditions to the ICD-10 codes on your bill."
        },
        {
            "q": "How do complications and comorbidities change my hospital bill?",
            "a": "Medicare uses two tiers of severity modifiers: CC (complication or comorbidity) and MCC (major complication or comorbidity). Adding a CC to your diagnosis can increase the DRG payment by $2,000 to $5,000. Adding an MCC can increase it by $5,000 to $20,000 or more. For commercial insurance, a higher DRG also means higher billed charges and higher cost-sharing for you. This is why verifying that every diagnosis code on your bill accurately reflects your documented conditions is important."
        },
        {
            "q": "Can I request my ICD-10 and DRG codes?",
            "a": "Yes. You have the right to request an itemized bill showing all ICD-10 diagnosis codes and procedure codes assigned to your stay. For inpatient stays, ask the hospital billing department for the DRG assignment as well. Compare these codes to your medical record and discharge summary. If a code does not match a documented condition, request a correction in writing."
        },
        {
            "q": "What should I do if I think my bill has the wrong DRG?",
            "a": "Request your complete medical record and compare the documented diagnoses to the ICD-10 codes on your bill. If you identify codes for conditions that were not present or not treated, submit a written dispute to the hospital billing department requesting a coding review and DRG reassignment. If the hospital does not correct the error, escalate to your insurer's claims review department. You can also file a complaint with the Office of Inspector General if you believe intentional upcoding occurred."
        },
    ],
    "body": f"""
<p class="lead">
    A single ICD-10 diagnosis code added to your hospital record can change your bill by <strong>$5,000 to
    $20,000</strong> or more. When hospitals assign diagnosis codes that trigger a higher-severity Diagnosis-Related
    Group (DRG), the payment they receive from Medicare or your insurer increases &mdash; and so does your
    cost-sharing. The Office of Inspector General found that <strong>upcoding errors</strong> account for billions
    in overpayments annually. Understanding how ICD-10 and DRG codes work gives you the tools to verify your
    bill and challenge charges that do not match your medical record.
</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-are-icd10">What ICD-10 codes are and why they matter</a></li>
        <li><a href="#how-drgs-work">How DRGs work for inpatient billing</a></li>
        <li><a href="#cc-mcc">CC and MCC: how complications change your bill</a></li>
        <li><a href="#upcoding">Upcoding: when the wrong code inflates your bill</a></li>
        <li><a href="#verify-coding">How to verify your coding</a></li>
        <li><a href="#bill-example">Reading a DRG-based hospital bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-are-icd10">1. What ICD-10 codes are and why they matter</h2>

<p>
    The International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM) is a
    system of approximately 70,000 diagnosis codes used by every hospital, physician, and insurer in the
    United States. Every condition you are treated for &mdash; from a broken arm to diabetes to pneumonia
    &mdash; is assigned one or more ICD-10 codes.
</p>

<p>
    These codes serve three billing functions: they tell your insurer what condition was treated (which
    determines whether the service is covered), they drive the DRG assignment for inpatient stays (which
    determines how much the hospital gets paid), and they appear on your Explanation of Benefits as the
    reason for each charge. A wrong ICD-10 code can cause a claim denial, an inflated bill, or an incorrect
    cost-sharing calculation.
</p>

<p>
    <strong>How codes are structured:</strong> ICD-10 codes are 3 to 7 characters long. The first character
    is a letter, followed by digits and sometimes an additional letter. For example:
</p>

<ul>
    <li><strong>I10</strong> &mdash; Essential hypertension (simple, 3 characters)</li>
    <li><strong>S72.001A</strong> &mdash; Fracture of unspecified intracapsular section of right femur, initial encounter (7 characters, highly specific)</li>
    <li><strong>J18.9</strong> &mdash; Pneumonia, unspecified organism</li>
    <li><strong>K80.10</strong> &mdash; Calculus of gallbladder with chronic cholecystitis without obstruction</li>
</ul>

<p>
    The more specific the code, the more accurately it describes your condition &mdash; and the more
    precisely it determines payment. Hospitals employ certified medical coders who review your medical
    record after discharge and assign ICD-10 codes based on physician documentation. Errors in this
    process, whether accidental or intentional, directly affect your bill.
    <a href="/scan">Upload your bill to BillKarma</a> to check whether your diagnosis codes match the
    care you received.
</p>

<h2 id="how-drgs-work">2. How DRGs work for inpatient billing</h2>

<p>
    For inpatient hospital stays, Medicare (and many commercial insurers) does not pay per service or per
    day. Instead, it pays a single lump sum based on the Diagnosis-Related Group assigned to your stay. The
    DRG is determined by a computer algorithm (the MS-DRG Grouper) that considers your principal diagnosis,
    secondary diagnoses, procedures performed, age, and discharge status.
</p>

<p>
    There are approximately 770 MS-DRGs, each with a fixed payment weight. The weight is multiplied by the
    hospital's base rate (adjusted for geographic wages and other factors) to determine the payment. For
    example, DRG 470 (major joint replacement without complications) has a national average payment of
    approximately $12,000. DRG 469 (major joint replacement with MCC) pays approximately $26,000 &mdash;
    more than double &mdash; for the same procedure with a documented major complication.
</p>

<p>
    <strong>Why this matters for your bill:</strong> Even though Medicare pays the hospital a fixed DRG
    amount, the DRG assignment affects commercially insured patients too. Many commercial contracts set
    reimbursement as a percentage of Medicare DRG rates (such as 150% to 250% of Medicare). A higher DRG
    means a higher percentage-based payment, which means higher cost-sharing for you. Check your hospital's
    billing patterns in our <a href="/hospitals/">hospital directory</a>.
</p>

{_embed(mode="cost", cpt="99223", title="Hospital Admission Evaluation", subtitle="See what Medicare pays for a high-complexity inpatient admission visit.")}

<h2 id="cc-mcc">3. CC and MCC: how complications change your bill</h2>

<p>
    The DRG system uses two severity tiers that dramatically affect payment:
</p>

<p>
    <strong>CC (Complication or Comorbidity):</strong> A secondary diagnosis that increases the cost and
    complexity of care. Examples include diabetes (E11.9), chronic kidney disease stage 3 (N18.3), and
    atrial fibrillation (I48.91). Adding a CC to a DRG typically increases the payment by $2,000 to $5,000.
</p>

<p>
    <strong>MCC (Major Complication or Comorbidity):</strong> A secondary diagnosis that significantly
    increases cost and complexity. Examples include sepsis (A41.9), respiratory failure (J96.00), and acute
    kidney failure (N17.9). Adding an MCC increases the DRG payment by $5,000 to $20,000 or more.
</p>

<table>
    <thead>
        <tr>
            <th>DRG</th>
            <th>Description</th>
            <th>CC/MCC Level</th>
            <th>Avg. Medicare Payment</th>
            <th>Difference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>470</td>
            <td>Major joint replacement</td>
            <td>Without CC/MCC</td>
            <td>$12,000</td>
            <td>&mdash;</td>
        </tr>
        <tr>
            <td>469</td>
            <td>Major joint replacement</td>
            <td>With MCC</td>
            <td>$26,000</td>
            <td>+$14,000</td>
        </tr>
        <tr>
            <td>194</td>
            <td>Heart failure</td>
            <td>Without CC/MCC</td>
            <td>$5,200</td>
            <td>&mdash;</td>
        </tr>
        <tr>
            <td>193</td>
            <td>Heart failure</td>
            <td>With CC</td>
            <td>$7,100</td>
            <td>+$1,900</td>
        </tr>
        <tr>
            <td>192</td>
            <td>Heart failure</td>
            <td>With MCC</td>
            <td>$10,400</td>
            <td>+$5,200</td>
        </tr>
        <tr>
            <td>690</td>
            <td>Kidney/urinary tract infection</td>
            <td>Without CC/MCC</td>
            <td>$4,800</td>
            <td>&mdash;</td>
        </tr>
        <tr>
            <td>689</td>
            <td>Kidney/urinary tract infection</td>
            <td>With CC</td>
            <td>$6,500</td>
            <td>+$1,700</td>
        </tr>
        <tr>
            <td>688</td>
            <td>Kidney/urinary tract infection</td>
            <td>With MCC</td>
            <td>$9,200</td>
            <td>+$4,400</td>
        </tr>
        <tr>
            <td>378</td>
            <td>GI hemorrhage</td>
            <td>Without CC/MCC</td>
            <td>$4,600</td>
            <td>&mdash;</td>
        </tr>
        <tr>
            <td>377</td>
            <td>GI hemorrhage</td>
            <td>With CC</td>
            <td>$6,900</td>
            <td>+$2,300</td>
        </tr>
        <tr>
            <td>376</td>
            <td>GI hemorrhage</td>
            <td>With MCC</td>
            <td>$11,800</td>
            <td>+$7,200</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Key point:</strong> A single MCC diagnosis added to your record can increase the DRG payment by
    $5,000 to $14,000. If your medical record does not support that diagnosis, you are being overbilled.
    Always request your ICD-10 codes and compare them to your discharge summary. <strong>Have your bill
    handy?</strong> <a href="/scan">Scan it with BillKarma</a> &mdash; we flag coding discrepancies
    automatically.
</div>

<h2 id="upcoding">4. Upcoding: when the wrong code inflates your bill</h2>

<p>
    Upcoding is the assignment of a higher-severity diagnosis code or DRG than the patient's documented
    condition warrants. It can be accidental (coding error, ambiguous documentation) or intentional (fraud).
    Either way, it inflates payments and increases your cost-sharing.
</p>

<p>
    <strong>Common upcoding patterns:</strong>
</p>

<ul>
    <li><strong>Adding CC/MCC codes not supported by documentation.</strong> A coder assigns "acute
    respiratory failure" (MCC) when the physician documented "shortness of breath" (not an MCC). The DRG
    payment increases by $5,000 to $15,000.</li>
    <li><strong>Coding a chronic condition as acute.</strong> "Acute kidney injury" (MCC) coded instead
    of "chronic kidney disease stage 3" (CC). The acute version triggers a much higher payment.</li>
    <li><strong>Selecting a more specific code than documented.</strong> "Sepsis" (MCC) coded when the
    physician documented "suspected infection" or "SIRS" without confirmed sepsis criteria.</li>
    <li><strong>Principal diagnosis manipulation.</strong> Choosing a principal diagnosis that maps to a
    higher-paying DRG when multiple diagnoses are present. The principal diagnosis should be the condition
    most responsible for the admission, but in ambiguous cases, coding can be steered toward higher payment.</li>
</ul>

<p>
    The HHS Office of Inspector General has identified upcoding as a persistent problem, particularly in
    Medicare Advantage plans where risk adjustment payments create additional incentives to code higher
    severity. See our <a href="/guides/common-hospital-billing-errors">billing errors guide</a> for
    other common mistakes that inflate your bill. Check your hospital's upcoding risk in our
    <a href="/hospitals/">hospital directory</a>.
</p>

<table>
    <thead>
        <tr>
            <th>Upcoding Pattern</th>
            <th>What Was Documented</th>
            <th>What Was Coded</th>
            <th>Payment Increase</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Acute vs. chronic kidney disease</td>
            <td>CKD stage 3 (N18.3, CC)</td>
            <td>Acute kidney failure (N17.9, MCC)</td>
            <td>+$5,000&ndash;$12,000</td>
        </tr>
        <tr>
            <td>Respiratory failure vs. hypoxia</td>
            <td>Hypoxia / low O2 (R09.02)</td>
            <td>Acute respiratory failure (J96.00, MCC)</td>
            <td>+$5,000&ndash;$15,000</td>
        </tr>
        <tr>
            <td>Sepsis vs. infection</td>
            <td>Suspected infection / SIRS</td>
            <td>Sepsis (A41.9, MCC)</td>
            <td>+$8,000&ndash;$20,000</td>
        </tr>
        <tr>
            <td>Malnutrition severity</td>
            <td>Mild malnutrition (E44.1)</td>
            <td>Severe malnutrition (E43, MCC)</td>
            <td>+$4,000&ndash;$10,000</td>
        </tr>
    </tbody>
</table>

<h2 id="verify-coding">5. How to verify your coding</h2>

<p>
    You do not need to be a medical coder to catch major coding errors on your hospital bill. Follow these
    steps:
</p>

<p>
    <strong>Step 1 &mdash; Request your itemized bill with ICD-10 codes.</strong> Call the billing
    department and ask for a fully itemized statement showing all diagnosis codes (ICD-10-CM) and procedure
    codes (ICD-10-PCS or CPT). For inpatient stays, also request the DRG assignment.
</p>

<p>
    <strong>Step 2 &mdash; Request your medical record and discharge summary.</strong> Under HIPAA, you
    have the right to a copy of your complete medical record. The discharge summary lists your final
    diagnoses as documented by the treating physician. Compare this list to the ICD-10 codes on your bill.
</p>

<p>
    <strong>Step 3 &mdash; Look for codes that do not match.</strong> If your bill lists an ICD-10 code
    for a condition not mentioned in your discharge summary or medical record, that code may be incorrect.
    Common red flags: codes for "acute" versions of chronic conditions, codes for complications you did
    not experience, and codes for conditions that were "ruled out" but not confirmed.
</p>

<p>
    <strong>Step 4 &mdash; Submit a dispute.</strong> Write to the billing department identifying the
    specific ICD-10 codes you believe are incorrect and requesting a coding review. Include a copy of
    your discharge summary highlighting the documented diagnoses. Use our <a href="/calculator">cost
    calculator</a> to look up Medicare rates and understand the financial impact of each code.
</p>

<div class="key-takeaway">
    <strong>Important:</strong> If you believe a hospital intentionally upcoded your bill, you can report
    it to the HHS Office of Inspector General at 1-800-HHS-TIPS. Under the False Claims Act, intentional
    upcoding of Medicare claims is fraud. For your own bill, start with a written dispute to the billing
    department and escalate to your insurer if needed. <a href="/scan">Upload your bill to BillKarma</a>
    for an automated coding analysis.
</div>

<h2 id="bill-example">6. Reading a DRG-based hospital bill</h2>

<div class="bill-example">
    <div class="line-item">Principal Dx: M17.11 &mdash; Primary osteoarthritis, right knee | DRG 469</div>
    <div class="line-item flagged">Secondary Dx: N17.9 &mdash; Acute kidney failure, unspecified (MCC) | Triggers DRG 469 <span class="flag-reason">Review medical record. If patient had pre-existing CKD stage 3 (N18.3, a CC) rather than acute kidney failure, the correct DRG may be 468 or 470. Difference: $8,000&ndash;$14,000 in hospital payment.</span></div>
    <div class="line-item">Secondary Dx: I10 &mdash; Essential hypertension | No CC/MCC impact</div>
    <div class="line-item flagged">Secondary Dx: J96.00 &mdash; Acute respiratory failure (MCC) | Additional MCC <span class="flag-reason">Verify against medical record. Was the patient intubated or on mechanical ventilation? If the physician documented "hypoxia" or "oxygen desaturation" without meeting criteria for respiratory failure, this code is incorrect.</span></div>
    <div class="line-item">Procedure: 0SRC0J9 &mdash; Replacement of right knee joint, cemented | Matches CPT 27447</div>
    <div class="line-item error">DRG 469 assigned (with MCC) &mdash; Medicare payment: ~$26,000 <span class="flag-reason">If both MCC codes are unsupported, correct DRG is 470 (without CC/MCC) at ~$12,000. Potential overbilling: $14,000.</span></div>
    <div class="line-total">DRG 469 Payment: $26,000 | Correct DRG (if MCCs unsupported): $12,000 | Potential overbilling: $14,000</div>
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Wrong DRG assignment inflated bill by $14,000</h3>
    <p>
        A 67-year-old Medicare patient in Texas underwent elective total knee replacement. His
        postoperative course was uncomplicated: he was discharged on day 2 in good condition with no
        respiratory or renal issues. His bill showed DRG 469 (major joint replacement with MCC) with
        a Medicare payment of $26,200.
    </p>
    <p>
        The patient's daughter, a nurse, requested the itemized bill and noticed two MCC diagnosis codes:
        N17.9 (acute kidney failure) and J96.00 (acute respiratory failure). She obtained the medical
        record and found no documentation of either condition. The patient's creatinine was stable
        throughout the stay, and he never required supplemental oxygen. The physician's discharge summary
        listed only osteoarthritis and controlled hypertension as diagnoses.
    </p>
    <p>
        She submitted a written dispute to the hospital billing department with copies of the medical
        record pages showing stable lab values and no respiratory events. The hospital performed a
        coding review, removed both MCC codes, and reassigned the stay to DRG 470 (without CC/MCC).
        The corrected Medicare payment was $12,100 &mdash; a reduction of <strong>$14,100</strong>.
        While this savings accrued primarily to Medicare, it also corrected the patient's medical record
        and prevented the inaccurate diagnoses from affecting future insurance underwriting.
    </p>
</div>

<div class="case-study">
    <h3>Commercial insurance patient saves $4,800 by challenging CC codes</h3>
    <p>
        A 52-year-old woman with commercial insurance was hospitalized for gallbladder removal
        (cholecystectomy). Her insurer paid the hospital based on a DRG that included two CC diagnoses:
        E11.65 (type 2 diabetes with hyperglycemia) and I48.91 (atrial fibrillation). Her 20%
        coinsurance on the insurer's negotiated rate of $24,000 was $4,800.
    </p>
    <p>
        She reviewed her discharge summary and found no mention of atrial fibrillation. Her medical
        history included a single episode of palpitations three years earlier that was evaluated and found
        to be benign. She filed a dispute with her insurer, who initiated a claim review. The atrial
        fibrillation code was removed, the DRG was reassigned to a lower-severity group, and the
        negotiated payment dropped to $18,800. Her coinsurance was recalculated at $3,760 &mdash; saving
        her <strong>$1,040 out of pocket</strong>. She also requested correction of the atrial
        fibrillation diagnosis in her medical record to prevent it from appearing on future claims.
    </p>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is an ICD-10 code on my medical bill?</h3>
        <p>An ICD-10 code is a standardized diagnosis code assigned to every medical condition. These codes determine what your insurer pays, how your claim is processed, and the DRG assignment for inpatient stays. You can request a list of all ICD-10 codes on your bill from the hospital billing department.</p>
    </div>

    <div class="faq-item">
        <h3>What is a DRG and how does it affect my bill?</h3>
        <p>A DRG is a classification that groups inpatient stays by diagnosis, procedures, and severity. Each DRG has a fixed payment amount. Higher-severity DRGs pay the hospital more and can increase your cost-sharing. A DRG with major complications (MCC) can pay $10,000 to $15,000 more than the same procedure without complications.</p>
    </div>

    <div class="faq-item">
        <h3>What is upcoding and how do I spot it?</h3>
        <p>Upcoding is assigning a higher-severity code than warranted, inflating payment. Red flags include MCC diagnoses not mentioned in your discharge summary, "acute" versions of your chronic conditions, and conditions that were ruled out but still coded. Compare your ICD-10 codes to your medical record. For automated analysis, <a href="/scan">upload your bill to BillKarma</a>.</p>
    </div>

    <div class="faq-item">
        <h3>How do complications and comorbidities change my hospital bill?</h3>
        <p>A CC (complication or comorbidity) increases the DRG payment by $2,000 to $5,000. An MCC (major complication) increases it by $5,000 to $20,000. These amounts flow through to your cost-sharing. If a CC or MCC code on your bill does not match your documented conditions, you may be overpaying.</p>
    </div>

    <div class="faq-item">
        <h3>Can I request my ICD-10 and DRG codes?</h3>
        <p>Yes. You have the right to an itemized bill showing all ICD-10 codes and, for inpatient stays, the DRG assignment. Call the billing department and specifically request this information. Compare the codes to your discharge summary, which lists your final documented diagnoses.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I think my bill has the wrong DRG?</h3>
        <p>Request your medical record and compare documented diagnoses to the ICD-10 codes. Submit a written dispute identifying the specific codes you believe are incorrect. If the hospital does not correct the error, escalate to your insurer. For suspected intentional upcoding, report to the HHS OIG at 1-800-HHS-TIPS. See our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> for detailed instructions.</p>
    </div>
</div>

<div class="key-takeaway">
    <strong>Worried your bill has the wrong DRG?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; our scanner checks diagnosis codes against your charges and flags mismatches. Look up your hospital&rsquo;s pricing patterns in our <a href="/hospitals/">hospital directory</a>.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">CMS: MS-DRG Definitions Manual &mdash; Version 42.0 (FY 2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">HHS Office of Inspector General: Upcoding in Medicare Advantage and Inpatient Hospital Claims</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: ICD-10-CM Official Guidelines for Coding and Reporting (FY 2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">MedPAC: Hospital Inpatient and Outpatient Services &mdash; March 2025 Report to Congress</a></li>
    <li><a href="#" target="_blank" rel="noopener">AHIMA: Understanding the MS-DRG Classification System &mdash; CC/MCC Impact Analysis</a></li>
    <li><a href="#" target="_blank" rel="noopener">GAO: Medicare Improper Payments &mdash; Coding Accuracy and Overpayment Estimates</a></li>
</ul>
""",
})
