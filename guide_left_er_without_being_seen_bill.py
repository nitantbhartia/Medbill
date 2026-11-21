"""Guide: Left the ER Without Being Seen? Can They Still Bill You?"""

from guides import register

register("left-er-without-being-seen-bill", {
    "title": "Left the ER Without Being Seen? Can They Still Bill You?",
    "meta_description": "Left the ER before seeing a doctor? A hospital may still bill for triage or screening, depending on what was done. Here is how to check and dispute it.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Can a hospital bill me if I left the ER without seeing a doctor?",
            "a": "Sometimes. No federal rule we found says a hospital can never bill in this situation, and none says it always can. It depends on what the hospital actually did (registration only, nurse triage, vital signs, tests) and on the hospital's own billing policy. A charge is easier to question when your records show no service was performed, or when the bill lists tests or a visit level that do not match what happened.",
        },
        {
            "q": "Does EMTALA mean my ER screening is free?",
            "a": "No. EMTALA, the federal emergency care law, requires hospitals with emergency departments to give a medical screening exam to anyone who asks, regardless of ability to pay, and it limits asking about insurance in ways that delay care. It does not say the screening is free. Billing questions are handled by the hospital's policies, your insurance plan, and the hospital's financial assistance program.",
        },
        {
            "q": "What is CPT code 99281?",
            "a": "99281 is the lowest of the five emergency department visit codes (99281 to 99285). Since 2023 the American Medical Association describes it as an ER visit for a patient that may not require the presence of a physician or other qualified health care professional. The AMA says the tasks can be done by clinical staff, but the code still requires physician supervision.",
        },
        {
            "q": "What does revenue code 0450 mean on my hospital bill?",
            "a": "Revenue codes are four-digit codes hospitals use to group charges by department. Medicare's claims manual says emergency room services are reported under the 045x revenue code family, and 0450 is the general emergency room line. A 0450 line is the hospital's facility charge for the ER visit. It is separate from any bill from the ER doctor's group.",
        },
        {
            "q": "How do I get my ER records to check what was done?",
            "a": "Ask the hospital's medical records (health information) department in writing. Under the HIPAA Privacy Rule you have a right to a copy of your medical and billing records. The hospital must act on your request within 30 days, with one possible 30-day extension if it tells you in writing.",
        },
        {
            "q": "Can I get help paying an ER bill if I left early?",
            "a": "Possibly. Nonprofit hospitals must have a written financial assistance policy that covers emergency care, and they cannot charge eligible patients more than the amounts generally billed to insured patients. Ask the billing office for the policy and an application, even if you think your income is too high.",
        },
    ],
    "body": f"""
<p class="lead">Yes, a hospital can sometimes bill you after you leave the ER without seeing a doctor, but only for what was actually done, and the rules depend on the hospital&rsquo;s own policy. If you only checked in, you have a strong reason to question a charge; if a nurse triaged you, took vital signs or ran tests, the hospital may bill for that, and you can still check that the bill matches your records.</p>

<p>The good news: you can see exactly what was billed, compare it to what happened, and ask the hospital in writing to fix anything that does not match.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#emtala">What federal law requires when you walk into the ER</a></li>
        <li><a href="#what-can-be-billed">What a hospital may bill when you leave early</a></li>
        <li><a href="#codes">The codes to look for: 0450 and 99281</a></li>
        <li><a href="#insurance">If you have insurance</a></li>
        <li><a href="#check">How to check what was actually done</a></li>
        <li><a href="#dispute">How to dispute charges for services you did not get</a></li>
        <li><a href="#financial-assistance">Financial assistance</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="emtala">1. What federal law requires when you walk into the ER</h2>

<p>The Emergency Medical Treatment and Labor Act (EMTALA) is a federal law for hospitals that take Medicare and have an emergency department. Its rules are in the federal regulation 42 CFR 489.24. In plain terms, when you come to the ER and ask for care, the hospital must give you an <strong>appropriate medical screening examination</strong> (MSE) within its capability. The exam must be done by staff the hospital&rsquo;s own rules say are qualified to do it.</p>

<p>Here is what the MSE means in practice, based on CMS&rsquo;s official guidance to hospital inspectors (State Operations Manual, Appendix V):</p>

<ul>
    <li><strong>It is a process, not a single moment.</strong> CMS describes the MSE as the process needed to decide, with reasonable clinical confidence, whether you have an emergency medical condition.</li>
    <li><strong>Triage is the start, not the whole exam.</strong> Triage is the nurse&rsquo;s first check of your symptoms to decide how soon you will be seen. CMS says the MSE &ldquo;begins, but typically does not end, with triage.&rdquo;</li>
    <li><strong>Insurance questions cannot delay care.</strong> The hospital may ask about your insurance at registration, as long as that does not delay screening or discourage you from staying.</li>
    <li><strong>Leaving on your own is allowed.</strong> CMS says that if you leave without being seen of your own free will, with no pressure or suggestion from the hospital, the hospital has not broken EMTALA.</li>
</ul>

<p>One important limit: EMTALA is about whether you get screened and treated. It does not say whether the hospital may charge for that care. We did not find any CMS rule that sets one national billing policy for patients who leave before seeing a doctor, so billing comes down to what was done and the hospital&rsquo;s own policy.</p>

<h2 id="what-can-be-billed">2. What a hospital may bill when you leave early</h2>

<p>A hospital ER bill usually comes in two parts. The <strong>facility bill</strong> is from the hospital for the room, nurses, supplies and tests. A <strong>professional bill</strong> comes from the doctor or doctor group that treated you. When you leave early, what shows up depends on how far your visit got.</p>

<table>
    <thead>
        <tr>
            <th>How far your visit got</th>
            <th>What may show up</th>
            <th>What to check</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Checked in at the desk only</td>
            <td>Often nothing. Some hospitals may still post a facility line.</td>
            <td>Ask what service the charge is for. Registration is paperwork, not care.</td>
        </tr>
        <tr>
            <td>Nurse triage (symptoms, vital signs)</td>
            <td>Possibly a low-level ER facility charge, depending on hospital policy</td>
            <td>Ask for the hospital&rsquo;s written policy for patients who leave after triage, and the visit level billed.</td>
        </tr>
        <tr>
            <td>Tests started (blood draw, X-ray, EKG)</td>
            <td>Separate lines for each test, plus possibly an ER facility charge</td>
            <td>Match each test to your records. Tests ordered but never done should not be billed.</td>
        </tr>
        <tr>
            <td>Seen by a doctor, physician assistant or nurse practitioner</td>
            <td>Facility charge plus a professional bill from the provider&rsquo;s group</td>
            <td>Check that the visit level fits what was actually done.</td>
        </tr>
    </tbody>
</table>

<p>A professional bill from an ER doctor group generally reflects work by a physician or other qualified provider. If no doctor, physician assistant or nurse practitioner saw you, a separate professional bill is worth asking about. Ask the group who provided or supervised the service.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Leaving early does not erase every charge, but you should only pay for what was actually done. Start by asking for an itemized bill that shows each code and charge. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> shows what to ask for.</p>
</div>

<h2 id="codes">3. The codes to look for: 0450 and 99281</h2>

<p><strong>Revenue code 0450.</strong> A revenue code is a four-digit code hospitals use to group charges by department. Medicare&rsquo;s Claims Processing Manual says emergency room services are reported under the 045x family, and 0450 is the general ER line. If you see 0450 on your itemized bill, that is the hospital&rsquo;s facility charge for the ER visit. Learn more in our guide to <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes</a>.</p>

<p><strong>CPT codes 99281 to 99285.</strong> CPT codes are the standard billing codes for medical services. The five ER visit levels run from 99281 (lowest) to 99285 (highest). Here is how the American Medical Association (AMA) describes them as of the 2023 update:</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>AMA description (summarized)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>99281</td>
            <td>ER visit for a patient that may not require the presence of a physician or other qualified health care professional</td>
        </tr>
        <tr>
            <td>99282</td>
            <td>Needs a medically appropriate history and/or exam and straightforward medical decision making</td>
        </tr>
        <tr>
            <td>99283</td>
            <td>History and/or exam and low-level medical decision making</td>
        </tr>
        <tr>
            <td>99284</td>
            <td>History and/or exam and moderate-level medical decision making</td>
        </tr>
        <tr>
            <td>99285</td>
            <td>History and/or exam and high-level medical decision making</td>
        </tr>
    </tbody>
</table>

<p>The AMA says the tasks under 99281 (its example is suture removal) can be done by clinical staff, but the code still requires physician supervision, and only physicians or other qualified providers can report it on a professional bill.</p>

<p>Hospitals pick the level on the <em>facility</em> bill a different way. CMS tells hospitals to use their own internal guidelines that tie each level to the hospital resources used. So if you left after a short triage and the facility bill shows a high level, ask the hospital to explain how its guidelines support that level. For more on high levels, see our guide to <a href="/guides/er-level-5-charge-99285/">the ER level 5 charge (99285)</a>.</p>

<h2 id="insurance">4. If you have insurance</h2>

<p>If the hospital bills your insurance for the visit, your plan&rsquo;s normal rules for ER care apply. That can mean an ER copay, your deductible (the amount you pay before your plan starts paying), or coinsurance (your share as a percentage).</p>

<p>Compare the hospital bill to your Explanation of Benefits (EOB), the statement your insurer sends showing the codes billed, what the plan paid and what you owe. Our guide on <a href="/guides/understanding-explanation-of-benefits/">reading your EOB</a> explains each column.</p>

<h2 id="check">5. How to check what was actually done</h2>

<p>Before you pay, compare the itemized bill to your ER record.</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Ask the hospital billing office for a bill that lists every line with its date, revenue code, CPT or HCPCS code and charge.</li>
    <li><strong>Request your ER records.</strong> Under the HIPAA Privacy Rule, you have a right to copies of your medical and billing records. The hospital must act on your request within 30 days and may take one 30-day extension if it tells you in writing. Ask for the triage note, nursing notes, any orders and test results, and the time you left. See <a href="/guides/how-to-request-medical-records/">how to request medical records</a>.</li>
    <li><strong>Write down your own timeline.</strong> Note when you arrived, whether a nurse took your vital signs, whether blood was drawn or any scan was done, and when you left.</li>
    <li><strong>Match each line to the record.</strong> For every charge, find the matching entry in your record. Mark any line that has no matching service, such as a lab test that was ordered but never drawn.</li>
    <li><strong>Check the visit level.</strong> Note the CPT code next to the 0450 line. If the record shows only triage and the level is above 99281, write that down as a question.</li>
    <li><strong>Check for a professional bill.</strong> If a separate bill came from a physician group, check your record for the name of a doctor, physician assistant or nurse practitioner who saw you.</li>
</ol>

<p><strong>Example:</strong> Your itemized bill shows an ER facility line (0450) at $650 and a blood test at $120, for a total of $770. Your record shows a triage note and a lab order, but no blood draw, and notes that you left before being called back. You would ask the hospital to remove the $120 lab charge, which would bring the bill to $650, and to explain how its policy supports the remaining ER visit charge and level.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Your records are the strongest evidence you have. When a charge has no matching service in the chart, you have a clear, specific question for the billing office. You can <a href="/scan">check your bill free</a> to flag codes and charges worth asking about.</p>
</div>

<h2 id="dispute">6. How to dispute charges for services you did not get</h2>

<p>Keep it in writing and factual: billing mistakes happen, and your goal is a corrected bill.</p>

<ol>
    <li><strong>Call to put the account on hold.</strong> Tell the billing office you are reviewing the bill and ask them to pause collection activity while you do. Write down the date and the name of the person you spoke with.</li>
    <li><strong>Send a written dispute.</strong> List each line you are questioning, the code and charge, and why (for example, &ldquo;no blood draw in my record&rdquo; or &ldquo;left after triage; no provider visit&rdquo;). Ask for the hospital&rsquo;s written policy on billing patients who leave before being seen.</li>
    <li><strong>Attach your evidence.</strong> Include copies (not originals) of the relevant record pages and your timeline.</li>
    <li><strong>Ask for a corrected claim.</strong> If you have insurance and the hospital agrees to change a charge, ask it to send a corrected claim to your insurer so your EOB updates too.</li>
    <li><strong>Contact your insurer if needed.</strong> If the hospital does not respond, call the number on your insurance card and ask for a review of the claim lines you are questioning.</li>
</ol>

<p>For a ready-to-use template, see our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter</a> guide. If the bill has gone to collections or you get court papers, consider talking to a consumer attorney or legal aid.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A clear written dispute, line by line, gives the hospital what it needs to fix a mistake and gives you a paper trail. Our step-by-step guide on <a href="/guides/how-to-dispute-a-medical-bill/">how to dispute a medical bill</a> covers what to include and when to follow up.</p>
</div>

<h2 id="financial-assistance">7. Financial assistance</h2>

<p>Even if the charges are correct, you may qualify for help. Under IRS rules for nonprofit hospitals (Section 501(r)), each nonprofit hospital must have a written financial assistance policy that covers all emergency and other medically necessary care. If you qualify, the hospital cannot charge you more than the amounts it generally bills to insured patients for that care.</p>

<p>Ask the billing office for the financial assistance policy and an application. Apply even if you are not sure you qualify, and ask that the account be put on hold while your application is reviewed. Our guide to <a href="/guides/hospital-financial-assistance-charity-care/">hospital financial assistance and charity care</a> explains how to apply, and our guide on <a href="/guides/financial-assistance-after-paying-hospital-bill/">financial assistance after paying</a> covers bills you already paid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can a hospital bill me if I left the ER without seeing a doctor?</h3>
        <p>Sometimes. No federal rule we found says a hospital can never bill in this situation, and none says it always can. It depends on what the hospital actually did (registration only, nurse triage, vital signs, tests) and on the hospital&rsquo;s own billing policy. A charge is easier to question when your records show no service was performed, or when the bill lists tests or a visit level that do not match what happened.</p>
    </div>
    <div class="faq-item">
        <h3>Does EMTALA mean my ER screening is free?</h3>
        <p>No. EMTALA, the federal emergency care law, requires hospitals with emergency departments to give a medical screening exam to anyone who asks, regardless of ability to pay, and it limits asking about insurance in ways that delay care. It does not say the screening is free. Billing questions are handled by the hospital&rsquo;s policies, your insurance plan, and the hospital&rsquo;s financial assistance program.</p>
    </div>
    <div class="faq-item">
        <h3>What is CPT code 99281?</h3>
        <p>99281 is the lowest of the five emergency department visit codes (99281 to 99285). Since 2023 the American Medical Association describes it as an ER visit for a patient that may not require the presence of a physician or other qualified health care professional. The AMA says the tasks can be done by clinical staff, but the code still requires physician supervision.</p>
    </div>
    <div class="faq-item">
        <h3>What does revenue code 0450 mean on my hospital bill?</h3>
        <p>Revenue codes are four-digit codes hospitals use to group charges by department. Medicare&rsquo;s claims manual says emergency room services are reported under the 045x revenue code family, and 0450 is the general emergency room line. A 0450 line is the hospital&rsquo;s facility charge for the ER visit. It is separate from any bill from the ER doctor&rsquo;s group.</p>
    </div>
    <div class="faq-item">
        <h3>How do I get my ER records to check what was done?</h3>
        <p>Ask the hospital&rsquo;s medical records (health information) department in writing. Under the HIPAA Privacy Rule you have a right to a copy of your medical and billing records. The hospital must act on your request within 30 days, with one possible 30-day extension if it tells you in writing.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get help paying an ER bill if I left early?</h3>
        <p>Possibly. Nonprofit hospitals must have a written financial assistance policy that covers emergency care, and they cannot charge eligible patients more than the amounts generally billed to insured patients. Ask the billing office for the policy and an application, even if you think your income is too high.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-489/subpart-B/section-489.24" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 489.24, Special responsibilities of Medicare hospitals in emergency cases (EMTALA)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/som107ap_v_emerg.pdf" target="_blank" rel="noopener">CMS &mdash; State Operations Manual, Appendix V: Responsibilities of Medicare Participating Hospitals in Emergency Cases</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4 (sections 160 and 180.6)</a></li>
    <li><a href="https://www.ama-assn.org/system/files/2023-e-m-descriptors-guidelines.pdf" target="_blank" rel="noopener">American Medical Association &mdash; 2023 CPT E/M descriptors and guidelines</a></li>
    <li><a href="https://www.ama-assn.org/system/files/cpt-e-m-advancing-landmark-webinar-faq.pdf" target="_blank" rel="noopener">American Medical Association &mdash; CPT E/M webinar FAQ (code 99281)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.501" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.501, Definitions (designated record set)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4" target="_blank" rel="noopener">IRS &mdash; Financial Assistance Policy and Emergency Medical Care Policy, Section 501(r)(4)</a></li>
</ul>
""",
})
