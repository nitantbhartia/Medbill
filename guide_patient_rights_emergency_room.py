"""Guide: Your Rights in the Emergency Room: What Hospitals Can and Can&rsquo;t Do."""

from guides import register, _embed

register("patient-rights-emergency-room", {
    "title": "Your Rights in the Emergency Room: What Hospitals Can",
    "meta_description": "Federal law guarantees your right to ER care regardless of insurance. Learn what EMTALA protects, what hospitals can't do, and how to fight an ER bill.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Can an emergency room refuse to treat me if I can't pay?",
            "a": "No. Under EMTALA, any hospital with an emergency department that accepts Medicare (virtually all hospitals) must provide a medical screening exam and stabilizing treatment to anyone who arrives, regardless of ability to pay, insurance status, or immigration status. A hospital that refuses to screen or stabilize you is breaking federal law and can be reported to the CMS regional office.",
        },
        {
            "q": "Can I be balance billed for an emergency room visit?",
            "a": "If you have private insurance, no. The No Surprises Act prohibits balance billing for all emergency services, even at out-of-network hospitals. Your cost-sharing (copay, coinsurance, deductible) must be calculated at in-network rates. This applies to the ER physician, facility fees, labs, imaging, and any specialist called in during your emergency visit.",
        },
        {
            "q": "Does leaving the ER against medical advice void my insurance coverage?",
            "a": "In most cases, no. This is one of the most persistent myths in healthcare. Multiple studies, including a 2012 analysis in the Journal of General Internal Medicine, found no evidence that insurance companies routinely deny claims for patients who leave against medical advice (AMA). Your insurer may still cover the services you received before you left.",
        },
        {
            "q": "What is EMTALA and who does it protect?",
            "a": "EMTALA is the Emergency Medical Treatment and Labor Act, a federal law enacted in 1986. It requires Medicare-participating hospitals to provide a medical screening exam and stabilizing treatment to anyone who comes to the emergency department, regardless of insurance, ability to pay, race, religion, or immigration status. It protects all patients at virtually every hospital in the United States.",
        },
        {
            "q": "How do I file a complaint if the ER violated my rights?",
            "a": "For EMTALA violations, file a complaint with your CMS regional office or call 1-800-633-4227. For No Surprises Act violations, file at cms.gov/nosurprises or call 1-800-985-3059. For billing violations, contact your state attorney general and state insurance commissioner. You can also file with The Joint Commission if the hospital is accredited.",
        },
        {
            "q": "Can a hospital force me to sign financial forms before treating me in the ER?",
            "a": "A hospital cannot condition your medical screening exam or stabilizing treatment on signing financial responsibility forms. They may ask you to sign forms, but they cannot refuse or delay care if you decline. If a hospital tells you that you must sign before being seen, that is an EMTALA violation. You can report it to CMS.",
        },
    ],
    "body": f"""
<p class="lead">When you walk into an emergency room, you have more legal protections than almost anywhere else in healthcare. Federal law (EMTALA) requires hospitals to screen and stabilize you regardless of ability to pay. The No Surprises Act protects you from surprise out-of-network ER bills. And yet hospitals routinely push the boundaries of these rights&mdash;demanding payment upfront, balance billing for emergency care, or failing to inform patients about financial assistance. Here&rsquo;s what you&rsquo;re entitled to&mdash;and what to do when a hospital crosses the line.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#emtala">EMTALA: your right to emergency care</a></li>
        <li><a href="#no-surprises-act">The No Surprises Act in the ER</a></li>
        <li><a href="#informed-consent">Your right to informed consent</a></li>
        <li><a href="#itemized-bill">Your right to an itemized bill</a></li>
        <li><a href="#hospitals-cant-do">Things hospitals CAN&rsquo;T do</a></li>
        <li><a href="#hospitals-can-do">What hospitals CAN do that surprises patients</a></li>
        <li><a href="#file-complaint">How to file a complaint</a></li>
        <li><a href="#protect-your-wallet">ER billing: how to protect your wallet</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="emtala">1. EMTALA: your right to emergency care</h2>

<p>The Emergency Medical Treatment and Labor Act (EMTALA) is the most important law protecting emergency room patients in the United States. Enacted in 1986, it applies to <strong>every hospital</strong> that participates in Medicare&mdash;which is virtually every hospital in the country. Here&rsquo;s exactly what it requires:</p>

<h3>Medical screening exam</h3>

<p>When you arrive at an emergency department and request care (or when a reasonable person would conclude you need care), the hospital must provide a <strong>medical screening exam (MSE)</strong>. This exam must be adequate to determine whether an emergency medical condition exists. It cannot be a cursory glance by a triage nurse&mdash;it must be performed by a qualified medical professional using the hospital&rsquo;s standard screening procedures.</p>

<h3>Stabilization</h3>

<p>If the screening exam reveals an emergency medical condition, the hospital must provide <strong>stabilizing treatment</strong> within its capacity. &ldquo;Stabilized&rdquo; has a specific legal definition under EMTALA: the patient&rsquo;s condition must be resolved to the point where no material deterioration is reasonably likely to result from or occur during a transfer to another facility. For a pregnant patient in active labor, stabilization means delivery of the baby and placenta.</p>

<h3>Who is protected</h3>

<p>EMTALA applies to <strong>all patients</strong> regardless of:</p>

<ul>
    <li>Insurance status (insured, uninsured, underinsured)</li>
    <li>Ability to pay</li>
    <li>Immigration or citizenship status</li>
    <li>Race, religion, gender, or national origin</li>
    <li>Whether the patient has outstanding medical debt at that hospital</li>
</ul>

<h3>What hospitals cannot do under EMTALA</h3>

<ul>
    <li><strong>Demand payment before screening or treatment.</strong> A hospital cannot require proof of insurance, a deposit, or any form of payment before providing the medical screening exam and stabilizing treatment.</li>
    <li><strong>Transfer you to avoid treating you.</strong> If a hospital has the capacity and capability to treat your emergency condition, it cannot transfer you to another facility simply because you are uninsured or underinsured. Transfers are only permitted if the patient requests one, or if a physician certifies that the medical benefits of transfer outweigh the risks.</li>
    <li><strong>Delay screening to check insurance.</strong> The hospital may collect insurance information, but it cannot delay the screening exam to do so.</li>
</ul>

<div class="key-takeaway">
    <strong>EMTALA bottom line:</strong> If you show up at an emergency room, the hospital must screen you and stabilize any emergency condition&mdash;period. No payment questions, no insurance checks, no exceptions. If a hospital refused to treat you, delayed your screening to verify insurance, or transferred you inappropriately, that is a federal violation you can report to CMS at 1-800-633-4227.
</div>

<h2 id="no-surprises-act">2. The No Surprises Act in the ER</h2>

<p>The No Surprises Act (NSA), effective January 1, 2022, added a critical layer of financial protection for ER patients. Under this law, <strong>all emergency services are treated as in-network</strong> for cost-sharing purposes&mdash;even if you go to an out-of-network hospital or are seen by an out-of-network physician.</p>

<h3>What the No Surprises Act covers in the ER</h3>

<ul>
    <li><strong>ER physician fees:</strong> The emergency doctor who treats you cannot balance bill you, even if they are out of network.</li>
    <li><strong>Facility fees:</strong> The hospital&rsquo;s emergency department facility fee is treated as in-network for cost-sharing calculations.</li>
    <li><strong>Ancillary services:</strong> Labs, imaging, medications, and supplies provided during your ER visit are covered.</li>
    <li><strong>Specialists called in during the emergency:</strong> If a surgeon, radiologist, or other specialist is called in while you are in the ER, their services are also protected.</li>
</ul>

<h3>How cost-sharing works under the NSA</h3>

<p>Your insurer must calculate your copay, coinsurance, and deductible as if all ER services were provided by an in-network provider. The out-of-network provider and your insurer work out payment between themselves&mdash;you are not responsible for any balance beyond your in-network cost-sharing amount.</p>

<h3>The post-stabilization exception</h3>

<p>Once you are stabilized, the No Surprises Act protections can end&mdash;but <strong>only if</strong> you give informed consent. The out-of-network provider must give you written notice that they are out of network, provide an estimate of charges, and explain that you have the right to be transferred to an in-network provider. You must sign this consent at least 72 hours before the service (or at the time of scheduling for services scheduled less than 72 hours in advance). If you did not sign a consent form, you are still protected.</p>

<p>For a deeper dive into how the No Surprises Act works across all healthcare settings, see our <a href="/guides/no-surprises-act-explained/">full No Surprises Act guide</a>.</p>

<div class="key-takeaway">
    <strong>If you see a balance bill from your ER visit:</strong> Check whether the provider is billing you for the difference between their charge and what your insurance paid. Under the No Surprises Act, this is illegal for emergency services. <a href="/scan">Upload your ER bill to BillKarma</a> &mdash; we&rsquo;ll flag potential No Surprises Act violations, upcoding, duplicate charges, and excessive markups automatically.
</div>

<h2 id="informed-consent">3. Your right to informed consent</h2>

<p>Even in an emergency setting, you retain fundamental rights over your own medical decisions:</p>

<h3>The hospital must explain treatments</h3>

<p>Before performing a procedure, the hospital must explain what it involves, why it is recommended, the risks and benefits, and any alternatives. You have the right to ask questions and to understand what is being done to you. Exceptions exist for life-threatening emergencies where the patient is incapacitated and no surrogate decision-maker is available.</p>

<h3>You can refuse treatment</h3>

<p>You have the right to refuse any treatment, test, or procedure&mdash;including in the emergency room. If you are a competent adult, the hospital cannot force treatment on you against your will (with narrow exceptions involving court orders or public health emergencies). The hospital should document your refusal and explain the risks of refusing.</p>

<h3>You can leave against medical advice (AMA)</h3>

<p>You have the legal right to leave the emergency room at any time, even if your doctor recommends you stay. The hospital will ask you to sign an &ldquo;AMA form&rdquo; acknowledging the risks, but you are not required to sign it.</p>

<p><strong>The myth about insurance coverage:</strong> One of the most persistent myths in healthcare is that leaving AMA means your insurance won&rsquo;t cover the visit. This is largely false. A 2012 analysis published in the <em>Journal of General Internal Medicine</em> found no consistent evidence that insurers deny claims based on AMA status. Your insurance should still cover the services you received before leaving. If an insurer denies a claim solely because you left AMA, you have grounds to appeal.</p>

<h2 id="itemized-bill">4. Your right to an itemized bill</h2>

<p>You are legally entitled to a detailed, itemized bill from any hospital or healthcare provider. This is not the same as the summary statement most hospitals send automatically.</p>

<h3>What federal law requires</h3>

<p>Under the No Surprises Act and existing federal regulations, providers must give patients access to billing information. For uninsured and self-pay patients, the NSA specifically requires good faith estimates before scheduled services. CMS has also affirmed that patients have the right to request itemized statements.</p>

<h3>What state laws add</h3>

<p>Many states go further. California, New York, Texas, and others require hospitals to provide itemized bills either automatically or upon request, often within a specific timeline (typically 30 days). Some states mandate that the itemized bill include CPT codes, quantities, and unit prices for every charge.</p>

<h3>What your itemized bill should include</h3>

<ul>
    <li><strong>CPT/HCPCS codes</strong> for every service and procedure</li>
    <li><strong>Revenue codes</strong> for facility charges</li>
    <li><strong>Quantities</strong> for each item (how many units billed)</li>
    <li><strong>Unit prices</strong> for each line item</li>
    <li><strong>Date of service</strong> for each charge</li>
    <li><strong>Provider name</strong> associated with each charge</li>
</ul>

<p>If the hospital sends you a one-page summary with a single total, call billing and specifically request an itemized statement with CPT codes. For a step-by-step walkthrough, see our <a href="/guides/how-to-get-itemized-hospital-bill/">guide to getting your itemized hospital bill</a>.</p>

<h2 id="hospitals-cant-do">5. Things hospitals CAN&rsquo;T do</h2>

<p>Here are ten things that hospitals are legally prohibited from doing in the emergency room. If any of these happened to you, you have the right to file a complaint:</p>

<table>
    <thead>
        <tr><th>#</th><th>Prohibited Action</th><th>Legal Basis</th><th>What to Do</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td><strong>Refuse to screen you</strong></td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>Ask for insurance before screening</strong> (as a condition of being seen)</td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>Demand upfront payment before treatment</strong></td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>Transfer you when they have capacity to treat you</strong> (to avoid treating an uninsured patient)</td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>Balance bill you for emergency services</strong></td>
            <td>No Surprises Act</td>
            <td>File at cms.gov/nosurprises or call 1-800-985-3059</td>
        </tr>
        <tr>
            <td>6</td>
            <td><strong>Force you to sign financial responsibility forms as a condition of treatment</strong></td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>7</td>
            <td><strong>Retaliate if you file a complaint</strong></td>
            <td>EMTALA &amp; whistleblower protections</td>
            <td>Report retaliation to CMS and your state AG</td>
        </tr>
        <tr>
            <td>8</td>
            <td><strong>Deny treatment based on immigration status</strong></td>
            <td>EMTALA</td>
            <td>Report to CMS regional office</td>
        </tr>
        <tr>
            <td>9</td>
            <td><strong>Charge for services you explicitly refused</strong></td>
            <td>Informed consent laws; state consumer protection</td>
            <td>Dispute the charge; contact state AG</td>
        </tr>
        <tr>
            <td>10</td>
            <td><strong>Send you to collections without first offering financial assistance</strong> (nonprofit hospitals)</td>
            <td>IRS Section 501(r)</td>
            <td>File IRS Form 13909; contact state AG</td>
        </tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Case study: ER demanded insurance card before treating chest pain</h3>
    <p>A 54-year-old patient arrived at a hospital ER with chest pain and shortness of breath. The registration desk told him he needed to provide his insurance card before being seen. He waited 25 minutes at the desk while staff processed his insurance information before a nurse began his screening exam. Under EMTALA, the hospital was required to begin the medical screening exam promptly regardless of insurance status. The patient filed a complaint with his CMS regional office, and the hospital was investigated and required to implement corrective measures. <strong>If this happens to you, insist on being seen immediately and document the delay&mdash;it is an EMTALA violation.</strong></p>
</div>

<h2 id="hospitals-can-do">6. What hospitals CAN do that surprises patients</h2>

<p>While hospitals have many obligations, patients are often surprised by what hospitals <em>are</em> legally permitted to do:</p>

<h3>They CAN bill you</h3>

<p>EMTALA requires hospitals to treat you&mdash;it does not require them to treat you for free. After screening and stabilizing you, the hospital will bill you (or your insurance) for the services provided. The law prevents them from refusing treatment, not from charging for it.</p>

<h3>They CAN downcode your visit retroactively</h3>

<p>Hospitals can also <em>upcode</em>, but more surprisingly, they can lower the visit level after the fact if an internal audit determines the original coding was too high. While downcoding benefits you when it reduces your bill, it can also affect insurance payments in ways that increase your share. Always check your Explanation of Benefits.</p>

<h3>They CAN charge facility fees</h3>

<p>On top of the physician&rsquo;s fee, the hospital charges a separate facility fee for using the emergency department. This fee covers 24/7 staffing, equipment, and overhead. Facility fees range from $500 to $3,500+ depending on the ER visit level. This is legal&mdash;but the amount can be disputed if it is out of proportion to the services you received. Learn more in our <a href="/guides/hospital-facility-fees-explained/">hospital facility fees guide</a>.</p>

<h3>They CAN have you wait</h3>

<p>There is no federal guarantee of ER wait times. EMTALA requires hospitals to screen you&mdash;not to screen you within a specific timeframe. Patients are triaged by severity, and a lower-acuity patient may wait hours while higher-acuity patients are seen first. However, a hospital cannot use the waiting room as a tool to discourage uninsured patients from seeking care.</p>

<h3>They CAN ask you to leave after stabilization</h3>

<p>Once your emergency medical condition is stabilized, EMTALA&rsquo;s obligations are met. The hospital can discharge you, transfer you to another facility, or admit you for further care. They are not required to provide ongoing treatment beyond stabilization unless you are admitted as an inpatient.</p>

<h2 id="file-complaint">7. How to file a complaint</h2>

<p>If a hospital violates your ER rights, you have several avenues to file a complaint. Here is where to go depending on the type of violation:</p>

<h3>EMTALA violations (refused treatment, delayed screening, improper transfer)</h3>

<ol>
    <li><strong>CMS regional office:</strong> Contact your regional CMS office. You can find the correct office at <a href="https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/SurveyCertificationGenInfo/ContactInformation" target="_blank" rel="noopener">cms.gov</a> or call the CMS hotline at <strong>1-800-633-4227</strong>.</li>
    <li><strong>State health department:</strong> Your state&rsquo;s department of health may also investigate EMTALA complaints, especially if the hospital is state-licensed.</li>
    <li><strong>The Joint Commission:</strong> If the hospital is Joint Commission-accredited, file a complaint at <a href="https://www.jointcommission.org/resources/patient-safety-topics/report-a-patient-safety-concern-or-complaint/" target="_blank" rel="noopener">jointcommission.org</a>.</li>
</ol>

<h3>No Surprises Act violations (balance billing for ER services)</h3>

<ol>
    <li><strong>CMS No Surprises Help Desk:</strong> File at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call <strong>1-800-985-3059</strong>.</li>
    <li><strong>State insurance department:</strong> Your state&rsquo;s department of insurance regulates state-regulated health plans and can investigate balance billing complaints.</li>
</ol>

<h3>Billing violations (overcharges, coding errors, financial assistance violations)</h3>

<ol>
    <li><strong>State attorney general:</strong> The consumer protection division of your state AG&rsquo;s office handles healthcare billing complaints.</li>
    <li><strong>State insurance commissioner:</strong> If the billing issue involves your insurance company&rsquo;s processing of the claim.</li>
    <li><strong>IRS (for nonprofit hospital violations):</strong> If a nonprofit hospital sent you to collections without screening you for financial assistance, file <a href="https://www.irs.gov/charities-non-profits/irs-complaint-process-tax-exempt-organizations" target="_blank" rel="noopener">IRS Form 13909</a>.</li>
</ol>

<p>For all complaints, document everything: the date and time of your ER visit, the names of staff you interacted with, what happened, and any paperwork you received (or were denied). Written complaints carry more weight than phone calls.</p>

<h2 id="protect-your-wallet">8. ER billing: how to protect your wallet</h2>

<p>Knowing your rights is the first step. Here&rsquo;s how to use them to protect yourself financially:</p>

<h3>a) Request an itemized bill before you leave</h3>

<p>Ask the billing or registration desk for an itemized statement before you are discharged. Many hospitals won&rsquo;t provide one on the spot, but making the request creates a record. Follow up in writing within 48 hours. You need the itemized bill with CPT codes to identify overcharges, duplicate charges, and upcoding. See our <a href="/guides/how-to-get-itemized-hospital-bill/">step-by-step guide to getting your itemized bill</a>.</p>

<h3>b) Photograph all paperwork</h3>

<p>Use your phone to photograph every document the hospital gives you&mdash;registration forms, consent forms, discharge papers, prescriptions, and any financial forms. If a dispute arises later, you&rsquo;ll have evidence of exactly what you signed and what information you were given (or not given).</p>

<h3>c) Note all provider names</h3>

<p>Write down the names of every doctor, nurse practitioner, or specialist who treats you. In the ER, it&rsquo;s common for multiple providers to bill separately&mdash;the ER physician, a consulting surgeon, the radiologist who reads your imaging, and the hospital itself. Knowing who treated you helps you identify out-of-network charges and file No Surprises Act disputes if needed.</p>

<h3>d) Ask for financial assistance information</h3>

<p>Before you leave the ER, ask for the hospital&rsquo;s financial assistance application. All nonprofit hospitals (about 60% of U.S. hospitals) are required to have a financial assistance policy under IRS Section 501(r). Many patients qualify even with moderate incomes&mdash;thresholds often extend to 300&ndash;400% of the federal poverty level. Don&rsquo;t assume you won&rsquo;t qualify; apply and find out. See our <a href="/guides/hospital-financial-assistance-guide/">hospital financial assistance guide</a> for more details.</p>

<h3>e) Don&rsquo;t sign anything you don&rsquo;t understand</h3>

<p>Hospitals often present financial responsibility forms alongside medical consent forms during registration. You are <strong>not required</strong> to sign financial forms as a condition of emergency treatment. If you are handed a stack of papers, ask which ones are for medical consent and which are for financial responsibility. You can cross out or decline the financial forms without affecting your right to care.</p>

<h3>f) Upload your bill for a free audit</h3>

<p>Once you receive your ER bill, <a href="/scan">upload it to BillKarma</a> to check for upcoding, duplicate charges, and excessive markups. ER bills are among the most error-prone bills in healthcare&mdash;studies suggest that up to 80% contain at least one billing error.</p>

<div class="key-takeaway">
    <strong>Got your ER bill?</strong> <a href="/scan">Upload it to BillKarma</a> to check for upcoding, duplicate charges, and excessive markups. We compare every line item against Medicare rates and flag the charges most likely to be reduced on appeal.
</div>

{_embed(mode="markup", title="Check your ER bill charges", subtitle="Enter a CPT code and billed amount to compare against Medicare benchmarks.", height="420")}

<p>Want to understand why your ER bill is so high in the first place? Our <a href="/guides/why-emergency-room-bills-are-so-high/">guide to ER bill costs</a> breaks down the anatomy of an ER bill, explains how visit levels drive charges, and shows you exactly where to focus your dispute.</p>

<p>If you&rsquo;re dealing with medical debt from an ER visit you couldn&rsquo;t afford, our <a href="/fight-debt">debt relief resources</a> can help you understand your options for negotiation, settlement, and financial assistance.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can an emergency room refuse to treat me if I can&rsquo;t pay?</h3>
        <p>No. Under EMTALA, any hospital with an emergency department that accepts Medicare must provide a medical screening exam and stabilizing treatment to anyone who arrives, regardless of ability to pay, insurance status, or immigration status. A hospital that refuses to screen or stabilize you is violating federal law. Report violations to your CMS regional office at 1-800-633-4227.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be balance billed for an emergency room visit?</h3>
        <p>If you have private insurance, no. The No Surprises Act prohibits balance billing for all emergency services, even at out-of-network hospitals. Your cost-sharing must be calculated at in-network rates. This covers the ER physician, facility fees, labs, imaging, and specialists called in during your emergency visit. If you receive a balance bill, file a complaint at cms.gov/nosurprises.</p>
    </div>

    <div class="faq-item">
        <h3>Does leaving the ER against medical advice void my insurance coverage?</h3>
        <p>In most cases, no. A 2012 analysis in the <em>Journal of General Internal Medicine</em> found no consistent evidence that insurers deny claims based on AMA status. Your insurance should still cover the services you received before leaving. If your insurer denies a claim solely because you left AMA, you have grounds for an appeal.</p>
    </div>

    <div class="faq-item">
        <h3>What is EMTALA and who does it protect?</h3>
        <p>EMTALA is the Emergency Medical Treatment and Labor Act, a federal law enacted in 1986. It requires Medicare-participating hospitals to provide a medical screening exam and stabilizing treatment to anyone who comes to the ER, regardless of insurance, ability to pay, or immigration status. It covers virtually every hospital in the United States.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint if the ER violated my rights?</h3>
        <p>For EMTALA violations, file with your CMS regional office or call 1-800-633-4227. For No Surprises Act violations, file at cms.gov/nosurprises or call 1-800-985-3059. For billing violations, contact your state attorney general and state insurance commissioner. Document everything: dates, times, staff names, and all paperwork.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital force me to sign financial forms before treating me in the ER?</h3>
        <p>No. A hospital cannot condition your medical screening exam or stabilizing treatment on signing financial responsibility forms. They may present forms during registration, but they cannot refuse or delay care if you decline to sign. If a hospital tells you that you must sign financial documents before being seen, that is an EMTALA violation you can report to CMS.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.law.cornell.edu/uscode/text/42/1395dd" target="_blank" rel="noopener">42 U.S.C. &sect; 1395dd &mdash; Emergency Medical Treatment and Labor Act (EMTALA) Full Text</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/legislation/emtala" target="_blank" rel="noopener">CMS: EMTALA Overview, Enforcement, and Guidance</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Information for Consumers and Providers</a></li>
    <li><a href="https://www.congress.gov/bill/116th-congress/house-bill/133" target="_blank" rel="noopener">Consolidated Appropriations Act, 2021 (No Surprises Act &mdash; Division BB, Title I)</a></li>
    <li><a href="https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/SurveyCertificationGenInfo/Downloads/Survey-and-Cert-Letter-07-17.pdf" target="_blank" rel="noopener">CMS Survey &amp; Certification Letter: EMTALA Compliance and Enforcement</a></li>
    <li><a href="https://www.patientadvocate.org/" target="_blank" rel="noopener">Patient Advocate Foundation: Patient Rights and Financial Assistance Resources</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/charitable-organizations/requirements-for-501c3-hospitals-under-the-affordable-care-act-section-501r" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Nonprofit Hospitals</a></li>
</ul>
""",
})
