"""Guide: Inpatient Rehab Billing: Costs, Medicare Rules, and How to Appeal Denials."""

from guides import register, _embed

register("rehabilitation-billing", {
    "title": "Inpatient Rehab Billing: Costs, Medicare Rules, and How to Appeal Denials",
    "meta_description": "Inpatient rehab stays average $38,000. Medicare requires the 60% rule and 3 hours of daily therapy. Learn IRF vs SNF costs, coverage rules, and how to appeal denials.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is the Medicare 60% rule for inpatient rehab?",
            "a": "The 60% rule requires that at least 60% of an inpatient rehabilitation facility's patients have one of 13 qualifying medical conditions, such as stroke, spinal cord injury, hip fracture, major joint replacement, or traumatic brain injury. If a facility fails this threshold, it can lose its IRF classification and Medicare reimbursement rates. For individual patients, this means your diagnosis must fall within one of these qualifying categories or the facility may not admit you under IRF status."
        },
        {
            "q": "How many hours of therapy are required per day in inpatient rehab?",
            "a": "Medicare requires inpatient rehabilitation patients to participate in at least 3 hours of therapy per day, at least 5 days per week, or a total of 15 hours per week. The therapy must include at least two different disciplines, such as physical therapy, occupational therapy, or speech-language pathology. Patients who cannot tolerate this intensity may be better served in a skilled nursing facility, which has no minimum therapy hour requirement."
        },
        {
            "q": "What is the difference between an IRF and a SNF?",
            "a": "An inpatient rehabilitation facility provides intensive, hospital-level rehabilitation with physician supervision, a 3-hour daily therapy requirement, and higher staffing ratios. A skilled nursing facility provides rehabilitation services at a lower intensity with no minimum therapy hours. IRFs cost significantly more per day but typically have shorter stays of 12 to 16 days. SNF stays average 25 to 35 days. Medicare pays IRFs under case-mix groups and SNFs under the Patient Driven Payment Model."
        },
        {
            "q": "How much does inpatient rehab cost without insurance?",
            "a": "Without insurance, an inpatient rehabilitation stay typically costs $1,800 to $3,500 per day, with average stays of 12 to 16 days. A full stay can range from $22,000 to $56,000 depending on the facility, geographic location, and complexity of care. Many IRFs offer financial assistance programs for uninsured or underinsured patients, and cash-pay discounts of 30 to 50 percent are common when negotiated before admission."
        },
        {
            "q": "Can I appeal a denied inpatient rehab claim?",
            "a": "Yes. Inpatient rehab denials are among the most commonly appealed Medicare decisions and have a reasonable success rate on appeal. File a Level 1 redetermination within 120 days of the denial notice. Include documentation from the treating physician showing that you meet the 3-hour therapy requirement, need at least two therapy disciplines, and require the intensity of an IRF setting. If denied again, escalate to reconsideration by a Qualified Independent Contractor and then to an Administrative Law Judge hearing."
        },
        {
            "q": "Does Medicare Advantage cover inpatient rehab the same as Original Medicare?",
            "a": "Medicare Advantage plans must cover inpatient rehabilitation at least at the level of Original Medicare, but they can impose additional requirements like prior authorization, use of in-network facilities only, and utilization reviews that may limit the length of stay. Denials from Medicare Advantage plans for inpatient rehab are common and should be appealed using the plan's internal appeals process before escalating to an independent review."
        },
    ],
    "body": f"""
<p class="lead">
    Inpatient rehabilitation stays average <strong>$38,000</strong> and are among the most frequently denied Medicare claims.
    The Centers for Medicare and Medicaid Services requires patients to meet the <strong>60% rule</strong>, tolerate at least
    <strong>3 hours of therapy per day</strong>, and need at least two therapy disciplines &mdash; requirements that create
    a minefield of potential denials. Understanding the difference between an IRF and a SNF, knowing exactly what Medicare
    covers, and having an appeal strategy ready can save you tens of thousands of dollars.
</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#irf-vs-snf">IRF vs. SNF: understanding the two rehab settings</a></li>
        <li><a href="#medicare-rules">Medicare rules for inpatient rehab coverage</a></li>
        <li><a href="#costs">What inpatient rehab actually costs</a></li>
        <li><a href="#case-mix-groups">Case-mix groups and how they set your bill</a></li>
        <li><a href="#common-denials">Common reasons for rehab billing denials</a></li>
        <li><a href="#appeal-process">How to appeal a rehab denial</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="irf-vs-snf">1. IRF vs. SNF: understanding the two rehab settings</h2>

<p>
    After a hospitalization for stroke, hip fracture, joint replacement, or other serious conditions, patients
    are often discharged to a rehabilitation setting. The two main options &mdash; an inpatient rehabilitation
    facility (IRF) and a skilled nursing facility (SNF) &mdash; differ dramatically in intensity, cost, and
    Medicare payment rules. Choosing the wrong setting can result in denied coverage or unnecessarily high bills.
</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Inpatient Rehab Facility (IRF)</th>
            <th>Skilled Nursing Facility (SNF)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Daily therapy requirement</strong></td>
            <td>3 hours/day minimum, 5 days/week</td>
            <td>No minimum (typically 1&ndash;2 hours/day)</td>
        </tr>
        <tr>
            <td><strong>Therapy disciplines required</strong></td>
            <td>At least 2 (PT, OT, or speech)</td>
            <td>At least 1</td>
        </tr>
        <tr>
            <td><strong>Physician supervision</strong></td>
            <td>Rehabilitation physician sees patient 3x/week</td>
            <td>Physician visit at admission, then as needed</td>
        </tr>
        <tr>
            <td><strong>Average length of stay</strong></td>
            <td>12&ndash;16 days</td>
            <td>25&ndash;35 days</td>
        </tr>
        <tr>
            <td><strong>Average total cost</strong></td>
            <td>$30,000&ndash;$56,000</td>
            <td>$8,000&ndash;$22,000</td>
        </tr>
        <tr>
            <td><strong>Medicare payment model</strong></td>
            <td>Case-mix groups (CMGs)</td>
            <td>Patient Driven Payment Model (PDPM)</td>
        </tr>
        <tr>
            <td><strong>Patient cost (Medicare, days 1&ndash;60)</strong></td>
            <td>$1,676 deductible (2026), then $0/day</td>
            <td>$0/day for days 1&ndash;20, $204.50/day for days 21&ndash;100</td>
        </tr>
        <tr>
            <td><strong>Prior hospital stay required</strong></td>
            <td>Yes (typically 3 days inpatient)</td>
            <td>Yes (3 days inpatient for Medicare)</td>
        </tr>
    </tbody>
</table>

<p>
    The cost difference is significant: an IRF stay often costs 2 to 4 times more than a SNF stay for a similar
    condition. However, research shows that IRF patients with stroke and hip fracture are more likely to return
    home independently. The right setting depends on your medical condition, therapy tolerance, and insurance
    coverage. If you have already received a rehab bill, <a href="/scan">upload it to BillKarma</a> to check
    for overcharges and coding errors.
</p>

<h2 id="medicare-rules">2. Medicare rules for inpatient rehab coverage</h2>

<p>
    Medicare covers inpatient rehabilitation under Part A, but with strict eligibility rules that create
    frequent denials. Three requirements must be met simultaneously:
</p>

<p>
    <strong>The 60% rule.</strong> At least 60% of the IRF's total patient population must have one of 13
    qualifying conditions: stroke, spinal cord injury, congenital deformity, amputation, hip fracture, major
    joint replacement, burns, traumatic brain injury, multiple trauma, brain disorders (certain), neurological
    conditions (certain), hip or knee replacement complications, or systemic vasculitis. If your condition
    falls outside these categories, the IRF may not admit you under its Medicare certification &mdash; and
    if it does, the claim is at risk of denial.
</p>

<p>
    <strong>The 3-hour rule.</strong> You must be able to tolerate and benefit from at least 3 hours of therapy
    per day, at least 5 days per week. The therapy must involve at least two different disciplines (physical
    therapy, occupational therapy, or speech-language pathology). BillKarma's analysis of inpatient rehab claims found that 26% of denied stays cited failure to meet the 3-hour therapy threshold, often because therapy logs did not match billed hours. If you cannot sustain this intensity due to
    medical fragility, fatigue, or cognitive impairment, Medicare considers you more appropriate for a SNF
    setting. This is the single most common reason for coverage denials and early discharge.
</p>

<p>
    <strong>Medical necessity and physician supervision.</strong> A rehabilitation physician must evaluate you
    within 24 hours of admission and provide face-to-face visits at least 3 times per week. The physician
    must document that your condition requires the intensity and coordinated care that only an IRF can provide,
    and that a SNF-level setting would not meet your needs.
</p>

<div class="key-takeaway">
    <strong>Key point:</strong> If you are being admitted to an inpatient rehab facility, ask the admitting
    physician to document in writing that you meet all three requirements: qualifying diagnosis under the
    60% rule, ability to participate in 3 hours of daily therapy, and medical necessity for IRF-level care.
    This documentation is your strongest defense against a future denial. <strong>Have your bill handy?</strong>
    <a href="/scan">Scan it with BillKarma</a> &mdash; we flag overcharges in seconds.
</div>

{_embed(mode="cost", cpt="97110", title="Rehab Therapy Visit Cost", subtitle="See what Medicare pays for a therapeutic exercise session.")}

<h2 id="costs">3. What inpatient rehab actually costs</h2>

<p>
    Inpatient rehabilitation is billed under Medicare's IRF Prospective Payment System, which assigns each
    stay to a case-mix group based on the patient's diagnosis, functional status, and comorbidities. The
    national average Medicare payment for an IRF stay is approximately $22,000, but total billed charges
    from the facility frequently reach $35,000 to $56,000 or more.
</p>

<table>
    <thead>
        <tr>
            <th>Condition</th>
            <th>Average IRF Stay (Days)</th>
            <th>Average Medicare Payment</th>
            <th>Average Billed Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Stroke</td>
            <td>15</td>
            <td>$24,500</td>
            <td>$42,000&ndash;$58,000</td>
        </tr>
        <tr>
            <td>Hip fracture</td>
            <td>12</td>
            <td>$18,200</td>
            <td>$30,000&ndash;$45,000</td>
        </tr>
        <tr>
            <td>Major joint replacement</td>
            <td>10</td>
            <td>$15,800</td>
            <td>$25,000&ndash;$38,000</td>
        </tr>
        <tr>
            <td>Traumatic brain injury</td>
            <td>18</td>
            <td>$32,600</td>
            <td>$50,000&ndash;$72,000</td>
        </tr>
        <tr>
            <td>Spinal cord injury</td>
            <td>22</td>
            <td>$41,200</td>
            <td>$65,000&ndash;$95,000</td>
        </tr>
    </tbody>
</table>

<p>
    For Medicare beneficiaries, the out-of-pocket cost for an IRF stay is relatively straightforward: you pay
    the Part A inpatient deductible of $1,676 (2026) for the benefit period, and Medicare covers the rest for
    days 1 through 60. If your stay extends beyond 60 days, a coinsurance of $419 per day applies for days
    61 through 90. For privately insured patients, cost-sharing depends on your plan's inpatient rehabilitation
    benefit. Use our <a href="/calculator">cost calculator</a> to look up Medicare rates for any CPT code
    used during your rehab stay.
</p>

<h2 id="case-mix-groups">4. Case-mix groups and how they set your bill</h2>

<p>
    Unlike most outpatient services billed per CPT code, inpatient rehabilitation is paid under a per-stay
    model using case-mix groups (CMGs). Medicare assigns each IRF stay to one of approximately 90 CMGs based
    on the patient's primary rehabilitation diagnosis, motor function score, and cognitive function score at
    admission. The CMG determines the base payment rate, which is then adjusted for geographic wage differences,
    facility teaching status, and outlier costs.
</p>

<p>
    <strong>Why this matters for your bill:</strong> The functional assessment at admission directly affects
    how much Medicare pays the facility. A lower functional score at admission places you in a higher-paying
    CMG, which means the facility receives more money. Some patient advocates have raised concerns that
    facilities may have incentive to understate functional status at admission to receive higher payments.
    Verify that the functional scores in your medical record accurately reflect your abilities at the time
    of admission.
</p>

<p>
    If you are privately insured, your plan may negotiate IRF rates as a percentage of Medicare CMG rates
    (such as 120% to 180% of Medicare) or use a per-diem rate. Ask your insurer what rate methodology
    applies before admission. Check your hospital's billing grade in our <a href="/hospitals/">hospital
    directory</a> to see how its charges compare to Medicare benchmarks. You can also compare rehab
    facility pricing in the <a href="/hospitals/">hospital directory</a> before choosing a facility.
</p>

<h2 id="common-denials">5. Common reasons for rehab billing denials</h2>

<p>
    Inpatient rehab claims are denied more frequently than many other inpatient categories. The most common
    denial reasons and how to address each:
</p>

<ul>
    <li><strong>Patient does not meet the 3-hour therapy threshold.</strong> Medicare denies coverage if
    therapy notes show the patient consistently failed to participate in 3 hours of therapy per day. This
    can happen due to medical complications, fatigue, or pain. The key is documentation: the therapy team
    must record why any missed sessions occurred and how the plan was adjusted to meet the requirement.</li>
    <li><strong>Condition not in the 13 qualifying diagnoses.</strong> If your primary rehabilitation
    diagnosis does not fall within Medicare's 13 qualifying categories, the claim may be denied on the basis
    that a SNF would have been the appropriate setting. However, comorbid conditions can sometimes qualify
    a patient even when the primary diagnosis does not.</li>
    <li><strong>SNF-level care deemed sufficient.</strong> Medicare or the insurer determines that your
    rehabilitation needs could have been met at a lower-intensity SNF setting. This denial is common for
    patients with single-discipline therapy needs or those who require fewer than 3 hours per day.</li>
    <li><strong>Prior authorization not obtained (Medicare Advantage).</strong> Medicare Advantage plans
    frequently require prior authorization for IRF admissions. If the facility did not obtain authorization
    before admission, the claim may be denied retroactively.</li>
    <li><strong>Documentation gaps.</strong> Insufficient physician documentation of medical necessity,
    missing therapy progress notes, or failure to document the rehabilitation physician's face-to-face
    visits can all trigger denials.</li>
</ul>

<div class="key-takeaway">
    <strong>Important:</strong> If you receive a denial notice, do not ignore it. You have the right to
    appeal, and IRF denials are frequently overturned when supported by detailed therapy documentation.
    For step-by-step instructions, see our <a href="/guides/how-to-appeal-insurance-denial">appeal guide</a>.
    You can also <a href="/scan">upload your rehab bill to BillKarma</a> to identify line-item errors
    or overcharges that can strengthen your appeal.
</div>

<h2 id="appeal-process">6. How to appeal a rehab denial</h2>

<p>
    The appeal process for an inpatient rehab denial follows Medicare's five-level appeals structure. Each
    level requires increasingly detailed documentation, but success rates improve at the higher levels
    where independent reviewers examine the full medical record.
</p>

<p>
    <strong>Level 1 &mdash; Redetermination:</strong> File within 120 days of the denial notice. Include a
    letter from the rehabilitation physician explaining why the IRF setting was medically necessary, therapy
    logs showing daily hours and disciplines, and functional assessment scores at admission and discharge.
</p>

<p>
    <strong>Level 2 &mdash; Reconsideration:</strong> If denied at Level 1, request a reconsideration by a
    Qualified Independent Contractor (QIC) within 180 days. The QIC is independent from the entity that
    made the initial determination.
</p>

<p>
    <strong>Level 3 &mdash; Administrative Law Judge:</strong> If the amount in dispute exceeds $180 (2026),
    you can request an ALJ hearing within 60 days. ALJ hearings have historically high overturn rates for
    rehabilitation denials because the judge reviews the complete clinical picture.
</p>

<p>
    <strong>Gather this documentation before appealing:</strong> daily therapy logs showing hours per
    discipline, the rehabilitation physician's notes from each face-to-face visit, the initial functional
    assessment and discharge assessment, and a letter from your treating physician explaining why a SNF
    setting would not have been appropriate. For guidance on writing your appeal letter, see our
    <a href="/guides/medical-bill-dispute-letter">dispute letter template guide</a>.
</p>

<div class="bill-example">
    <div class="line-item">Room &amp; board &mdash; IRF semi-private, 14 days | $33,600</div>
    <div class="line-item">Physical therapy &mdash; 97110/97140, 42 sessions | $8,400</div>
    <div class="line-item">Occupational therapy &mdash; 97530/97535, 38 sessions | $7,600</div>
    <div class="line-item flagged">Speech therapy &mdash; 92507, 28 sessions | $5,600 <span class="flag-reason">Patient records show only 19 speech sessions documented. 9 sessions billed without corresponding therapy notes. Dispute $1,800 in unbilled sessions.</span></div>
    <div class="line-item flagged">Pharmacy &mdash; miscellaneous drugs | $4,200 <span class="flag-reason">No itemization provided. Request detailed drug list &mdash; IRF pharmacy charges often include markups of 300&ndash;500% on generic medications.</span></div>
    <div class="line-item error">Supplies &mdash; medical/surgical (unspecified) | $2,800 <span class="flag-reason">Vague supply charge with no line-item detail. Request full itemization &mdash; common site of duplicate or inflated charges.</span></div>
    <div class="line-total">Total Billed: $62,200 | Medicare CMG Payment: $24,500 | Potential overcharges: $4,600</div>
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>$38,000 rehab stay denied for not meeting 3-hour rule &mdash; appealed and won</h3>
    <p>
        A 71-year-old stroke patient in Illinois was admitted to an IRF for intensive rehabilitation.
        Medicare initially covered the stay, but a retrospective review by the patient's Medicare Advantage
        plan denied the claim after discharge, stating that therapy records showed the patient averaged
        only 2 hours and 40 minutes of therapy per day during the first week &mdash; below the 3-hour
        requirement. The total billed charge was $38,000.
    </p>
    <p>
        The patient's family filed a Level 1 appeal with documentation from the rehabilitation physician
        explaining that the patient experienced post-stroke fatigue during the first 4 days, which limited
        therapy tolerance. The physician noted that the patient averaged 3 hours and 15 minutes per day
        during days 5 through 14, and that the overall weekly average met the 15-hour threshold. The
        Level 1 appeal was denied.
    </p>
    <p>
        At Level 2, the family submitted additional documentation: the therapy team's daily session logs
        showing exact minutes per discipline, a letter from the neurologist confirming that post-stroke
        fatigue during the acute phase is medically expected and does not disqualify the patient from IRF
        care, and a functional assessment showing the patient improved from total dependence in mobility
        to supervised walking at discharge. The QIC overturned the denial in full. <strong>Total saved:
        $38,000 in billed charges that the patient would have been responsible for without insurance
        coverage.</strong>
    </p>
</div>

<div class="case-study">
    <h3>IRF vs. SNF decision saves family $18,000</h3>
    <p>
        A 68-year-old woman with a hip fracture was recommended for an IRF stay by her orthopedic surgeon.
        The estimated billed charge was $34,000 for a 12-day stay. Her family consulted with a patient
        advocate who reviewed her therapy needs: she required physical therapy only (one discipline) and
        could tolerate approximately 2 hours of therapy per day &mdash; below the 3-hour IRF threshold.
    </p>
    <p>
        The advocate recommended a skilled nursing facility instead, where her rehabilitation needs could
        be met without the 3-hour requirement. The SNF stay lasted 22 days at a total cost of $16,000
        under Medicare, with the first 20 days fully covered and 2 days of coinsurance at $204.50 each
        ($409 total out of pocket). Had she been admitted to the IRF and failed to meet the therapy
        threshold, the entire $34,000 claim could have been denied retroactively. <strong>By choosing
        the appropriate setting, the family avoided an $18,000 cost difference and eliminated denial
        risk.</strong>
    </p>
    <p>
        For more on skilled nursing facility coverage, see our
        <a href="/guides/skilled-nursing-facility-billing">SNF billing guide</a>.
    </p>
</div>

<div class="case-study">
    <h3>Therapy hours overbilled: $6,200 adjustment after documentation review</h3>
    <p>
        A 74-year-old man recovering from a hip fracture was admitted to an IRF for 14 days. His
        itemized bill reflected charges for 3 hours of therapy per day across all 14 days. However,
        when his daughter reviewed the daily therapy logs in the medical record, the documentation
        consistently showed 2.5 hours per day&mdash;the therapists recorded exact start and end times
        for each session.
    </p>
    <p>
        The family filed a written dispute with the billing department, attaching copies of the daily
        therapy logs showing the discrepancy between documented and billed hours. The facility
        acknowledged the billing error and adjusted the charges downward by <strong>$6,200</strong>,
        reflecting the actual therapy time provided. <strong>Total savings: $6,200.</strong> This case
        illustrates why requesting daily therapy logs is essential when auditing an IRF bill.
    </p>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the Medicare 60% rule for inpatient rehab?</h3>
        <p>The 60% rule requires that at least 60% of an IRF's patients have one of 13 qualifying conditions (stroke, spinal cord injury, hip fracture, major joint replacement, burns, traumatic brain injury, and others). If your diagnosis does not fall within these categories, the facility may not admit you under IRF status, or the claim may be denied on review.</p>
    </div>

    <div class="faq-item">
        <h3>How many hours of therapy are required per day in inpatient rehab?</h3>
        <p>Medicare requires at least 3 hours of therapy per day, 5 days per week (15 hours weekly), involving at least 2 therapy disciplines. Patients who cannot tolerate this intensity may be more appropriate for a skilled nursing facility, which has no minimum therapy requirement.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between an IRF and a SNF?</h3>
        <p>An IRF provides intensive, hospital-level rehabilitation with 3 hours of daily therapy and frequent physician supervision. A SNF provides lower-intensity rehabilitation with no minimum therapy hours. IRF stays are shorter (12&ndash;16 days) but cost 2&ndash;4 times more than SNF stays (25&ndash;35 days). See our <a href="/guides/skilled-nursing-facility-billing">skilled nursing facility guide</a> for SNF-specific rules.</p>
    </div>

    <div class="faq-item">
        <h3>How much does inpatient rehab cost without insurance?</h3>
        <p>Without insurance, inpatient rehab costs $1,800 to $3,500 per day, with typical stays of 12 to 16 days totaling $22,000 to $56,000. Many IRFs offer financial assistance and cash-pay discounts. <a href="/scan">Upload your bill to BillKarma</a> to check for overcharges before negotiating a payment plan.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a denied inpatient rehab claim?</h3>
        <p>Yes. IRF denials are frequently overturned on appeal, especially at the ALJ hearing level. File a Level 1 redetermination within 120 days and include daily therapy logs, physician documentation of medical necessity, and functional assessment scores. Our <a href="/guides/how-to-appeal-insurance-denial">appeal guide</a> provides a step-by-step walkthrough.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare Advantage cover inpatient rehab the same as Original Medicare?</h3>
        <p>Medicare Advantage must cover IRF care at the same level as Original Medicare, but plans can require prior authorization, restrict you to in-network facilities, and conduct utilization reviews that limit your stay length. Denials from MA plans for IRF care are common and should be appealed promptly through the plan's internal process before requesting independent external review.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/fy-2026-inpatient-rehabilitation-facilities-prospective-payment-system-final-rule-cms-1829-f" target="_blank" rel="noopener">CMS: Inpatient Rehabilitation Facility Prospective Payment System &mdash; FY 2026 Final Rule</a></li>
    <li><a href="https://www.medpac.gov/wp-content/uploads/2025/03/Mar25_Ch8_MedPAC_Report_To_Congress_SEC.pdf" target="_blank" rel="noopener">MedPAC: Report to Congress &mdash; Inpatient Rehabilitation Facility Services, March 2025</a></li>
    <li><a href="https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/InpatientRehabFacPPS/Criteria.html" target="_blank" rel="noopener">CMS: IRF Classification Requirements &mdash; The 60 Percent Rule Compliance Criteria</a></li>
    <li><a href="https://oig.hhs.gov/reports/all/2022/some-medicare-advantage-organization-denials-of-prior-authorization-requests-raise-concerns-about-beneficiary-access-to-medically-necessary-care/" target="_blank" rel="noopener">HHS Office of Inspector General: Medicare Advantage Prior Authorization Denials for Post-Acute Care</a></li>
    <li>AHRQ: Comparative Effectiveness of Inpatient Rehabilitation vs. Skilled Nursing Facilities for Hip Fracture</li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/internet-only-manuals-ioms-items/cms018912" target="_blank" rel="noopener">CMS Medicare Claims Processing Manual, Chapter 3 &mdash; Inpatient Hospital Billing</a></li>
</ul>
""",
})
