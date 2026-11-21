"""Guide: Typo Denied Your Claim? Fix Wrong Name, Birthday or Member ID."""

from guides import register

register("wrong-info-hospital-bill-claim-denied", {
    "title": "Claim Denied for a Typo? Fix Wrong Name, DOB or Member ID",
    "meta_description": "A wrong name, birth date or member ID can stop an insurance claim cold. See where the error hides, who fixes it, and what to say to get it resubmitted.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "Can a typo in my name or birth date really cause a claim denial?",
            "a": "Yes. Insurers match each claim to a member by ID number, name and birth date. Medicare contractor Noridian says a patient name that is not an identical match will cause the claim to be rejected as unprocessable.",
        },
        {
            "q": "What is the difference between a rejected claim and a denied claim?",
            "a": "A denied claim was processed and not paid, and can usually be appealed. A rejected or returned claim was not processed because information was missing or invalid. Medicare says such a claim is not denied and has no appeal rights; the fix is a corrected claim.",
        },
        {
            "q": "Who has to fix the claim, me or the hospital?",
            "a": "The hospital billing office sends the claim, so it corrects and resubmits it. Your part is to spot the error, give them the correct details from your card, and fix the source if it sits with your insurer, employer or Social Security.",
        },
        {
            "q": "Is there a deadline to resubmit a corrected claim?",
            "a": "Yes. Medicare generally requires a claim within 1 calendar year after the date of service (42 CFR 424.44). Private plans and Medicaid set their own limits. Ask the billing office which deadline applies.",
        },
        {
            "q": "Can I make the hospital correct my records?",
            "a": "You can ask. Under the HIPAA Privacy Rule (45 CFR 164.526), a hospital or health plan must act on a request to amend your information within 60 days, with one possible 30-day extension. It can deny the request if it finds the record accurate and complete.",
        },
        {
            "q": "What if the wrong information is not a typo at all?",
            "a": "If you see a name, visit or service you don’t recognize, someone else may have used your insurance. The FTC suggests getting your medical records, reporting errors in writing and checking your credit reports. See our medical identity theft guide.",
        },
    ],
    "body": f"""
<p class="lead">If your claim came back because of a wrong name, birth date or member ID, the fix is usually simple: give the hospital billing office the correct details from your insurance card and ask them to correct and resubmit the claim. Move quickly, because insurers have filing deadlines, and a claim that was never accepted does not stop that clock.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#rejected-or-denied">Rejected or denied? Why the word matters</a></li>
        <li><a href="#why-typos-matter">Why one wrong letter can stop a claim</a></li>
        <li><a href="#spot-it-fix-it">Spot it, fix it: the table</a></li>
        <li><a href="#steps">What to do, step by step</a></li>
        <li><a href="#script">A quick script and a written request</a></li>
        <li><a href="#deadlines">The clock: filing deadlines</a></li>
        <li><a href="#life-changes">New card, new baby, new name</a></li>
        <li><a href="#not-a-typo">When it&rsquo;s not a typo</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="rejected-or-denied">1. Rejected or denied? Why the word matters</h2>

<p>Billing offices often split unpaid claims into two different things:</p>

<ul>
    <li><strong>Denied:</strong> the insurer processed the claim and decided not to pay all or part of it. You usually get an Explanation of Benefits (EOB, the statement your insurer sends after it processes a claim) and the right to appeal.</li>
    <li><strong>Rejected or returned:</strong> the claim never made it into processing because something was missing or invalid, like a member ID that doesn&rsquo;t exist in the insurer&rsquo;s system.</li>
</ul>

<p>Medicare&rsquo;s claims manual says a claim returned as unprocessable for incomplete or invalid information &ldquo;is not denied, and, as such, is not afforded appeal rights.&rdquo; It can be corrected and resubmitted instead. Private plans use their own terms, but the idea is similar: a data error is fixed with a corrected claim, not an appeal. That&rsquo;s good news. You just need the right data on the form.</p>

<h2 id="why-typos-matter">2. Why one wrong letter can stop a claim</h2>

<p>An insurer&rsquo;s first check is simple: is this person our member? It matches the member ID, name and birth date against its enrollment file. If they don&rsquo;t line up, the claim can stop there.</p>

<p>Hospitals bill on a form called the UB-04 (also called the CMS-1450). Doctors and many outpatient services bill on the CMS-1500. Both have fixed boxes for who you are:</p>

<table>
    <thead>
        <tr>
            <th>What it identifies</th>
            <th>Hospital claim (UB-04)</th>
            <th>Doctor claim (CMS-1500)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Patient name</td>
            <td>Form Locator 8</td>
            <td>Item 2</td>
        </tr>
        <tr>
            <td>Patient birth date</td>
            <td>Form Locator 10</td>
            <td>Item 3</td>
        </tr>
        <tr>
            <td>Policyholder (insured) name</td>
            <td>Form Locator 58</td>
            <td>Item 4</td>
        </tr>
        <tr>
            <td>Patient&rsquo;s relationship to the policyholder</td>
            <td>Form Locator 59</td>
            <td>Item 6</td>
        </tr>
        <tr>
            <td>Member or subscriber ID</td>
            <td>Form Locator 60</td>
            <td>Item 1a</td>
        </tr>
    </tbody>
</table>

<p>CMS tells providers to enter the patient&rsquo;s name as shown on the Medicare card. Medicare contractor Noridian says a name that isn&rsquo;t an identical match will be rejected as unprocessable, and an invalid Medicare ID can cause a denial or rejection.</p>

<p>Look for these standard reason codes on the insurer&rsquo;s notice:</p>
<ul>
    <li><strong>Code 31:</strong> &ldquo;Patient cannot be identified as our insured.&rdquo;</li>
    <li><strong>Code 140:</strong> &ldquo;Patient/Insured health identification number and name do not match.&rdquo;</li>
</ul>

<h2 id="spot-it-fix-it">3. Spot it, fix it: the table</h2>

<p>Put your insurance card next to your bill and any EOB, then work down this table. A rejected claim may not produce an EOB, so the bill may be your only clue.</p>

<table>
    <thead>
        <tr>
            <th>Error type</th>
            <th>Where it shows up</th>
            <th>Who fixes it</th>
            <th>What to send</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Misspelled name, missing middle initial, wrong suffix (Jr., Sr.)</td>
            <td>Patient name on the bill; member name on the EOB</td>
            <td>Hospital billing office</td>
            <td>Copy of the front of your insurance card; ask that the name match the card exactly</td>
        </tr>
        <tr>
            <td>Wrong birth date (often swapped month and day)</td>
            <td>Date of birth on the bill or patient portal</td>
            <td>Hospital registration and billing</td>
            <td>Card copy plus a photo ID showing your birth date</td>
        </tr>
        <tr>
            <td>Wrong or old member ID</td>
            <td>&ldquo;Insurance billed&rdquo; or &ldquo;policy number&rdquo; section of the bill; reason code 31 or 140</td>
            <td>Hospital billing office</td>
            <td>Current card, front and back, and the date your coverage started</td>
        </tr>
        <tr>
            <td>Wrong policyholder or relationship (child billed as the policyholder, spouse listed as self)</td>
            <td>&ldquo;Subscriber&rdquo; or &ldquo;guarantor&rdquo; on the bill</td>
            <td>Hospital billing office</td>
            <td>Policyholder&rsquo;s name and birth date as shown on the card, and your relationship to them</td>
        </tr>
        <tr>
            <td>Wrong insurer billed (old plan, wrong plan as primary)</td>
            <td>Payer name on the bill; denial from a plan you no longer have</td>
            <td>Hospital billing office; your current insurer if it disputes coverage</td>
            <td>New card and its start date; ask them to bill the right plan</td>
        </tr>
        <tr>
            <td>Your info is right on the claim but wrong in the insurer&rsquo;s file</td>
            <td>Card or member portal shows a different spelling or birth date</td>
            <td>Your insurer (member services); for employer plans, also HR</td>
            <td>Request to correct enrollment data; then ask the hospital to resubmit</td>
        </tr>
        <tr>
            <td>Name change not yet on Medicare</td>
            <td>Medicare card shows your old name</td>
            <td>Social Security, then the hospital</td>
            <td>Update your name with Social Security; give the hospital the name on the card</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Most of these fixes are paperwork, not a fight. Once the claim is corrected and processed, <a href="/scan">check the new bill free</a> to see how its charges compare with Medicare rates.</p>
</div>

<h2 id="steps">4. What to do, step by step</h2>

<ol>
    <li><strong>Gather your card, bill and any EOB.</strong> New to EOBs? See our <a href="/guides/explanation-of-benefits-eob/">EOB guide</a>.</li>
    <li><strong>Find the mismatch.</strong> Compare name, birth date, member ID and policyholder with your card. Write down exactly what&rsquo;s wrong.</li>
    <li><strong>If unsure, call your insurer.</strong> Ask: &ldquo;Did you get this claim? Was it denied or rejected, and why?&rdquo; Confirm they have your details right.</li>
    <li><strong>Call the hospital billing office.</strong> Give the correct details, ask them to correct and resubmit the claim, and ask when it will go out.</li>
    <li><strong>Ask for a billing hold</strong> while the corrected claim is pending, so the balance isn&rsquo;t sent to collections.</li>
    <li><strong>Put it in writing.</strong> Send the letter below with a copy of your card. Keep a copy.</li>
    <li><strong>Fix the source.</strong> Ask the hospital to amend its registration record, or your insurer to fix its file, so it doesn&rsquo;t happen again.</li>
    <li><strong>Follow up in two to three weeks.</strong> Look for the new claim in your insurer&rsquo;s portal, then an EOB showing what you owe.</li>
</ol>

<p>If the corrected claim is then <em>denied</em> for another reason, that&rsquo;s a real denial with appeal rights. Our guide on <a href="/guides/insurance-claim-denied-what-to-do/">what to do when a claim is denied</a> walks through it.</p>

<h2 id="script">5. A quick script and a written request</h2>

<p>Sample phone script for the billing office:</p>

<pre>
Hi, I'm calling about account number [ACCOUNT NUMBER] for
[PATIENT NAME], date of service [DATE].

My insurance didn't pay this claim because of a data error.
The claim shows [WRONG INFO]. The correct information,
from my insurance card, is [CORRECT INFO].

Can you correct the claim and resubmit it to [INSURER NAME]?
What date will it go out?

Can you hold my account until it's processed, and update
my registration record?

May I have your name and a reference number for this call?
</pre>

<p>Sample written request to send after the call:</p>

<blockquote>
<p>[DATE]</p>
<p>[HOSPITAL NAME] Billing Office<br>[ADDRESS]</p>
<p>Re: Account [ACCOUNT NUMBER], patient [PATIENT NAME], date of service [DATE]</p>
<p>My claim for this visit listed [WRONG INFO]. The correct information is [CORRECT INFO], as shown on the enclosed copy of my insurance card. Please correct and resubmit the claim to [INSURER NAME], member ID [MEMBER ID], and hold billing until it is processed.</p>
<p>I also ask that you amend my record to show the correct information (45 CFR 164.526). On [CALL DATE], [REP NAME] gave me reference number [REFERENCE NUMBER].</p>
<p>Thank you,<br>[YOUR NAME], [PHONE]</p>
</blockquote>

<p>Why cite that rule? Under the HIPAA Privacy Rule, you can ask a hospital or health plan to amend information about you. It may require a written request, and must act within 60 days, with one possible 30-day extension. It can say no if it finds the record accurate and complete; you can then submit a written statement of disagreement.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Call, then confirm in writing. A dated letter is your proof you reported the error on time. Our <a href="/guides/medical-bill-dispute-phone-scripts/">billing phone scripts</a> cover other calls you may need to make.</p>
</div>

<h2 id="deadlines">6. The clock: filing deadlines</h2>

<p>Every insurer sets a timely filing limit: the deadline for a provider to submit a claim. A rejected claim may not count as filed, so the clock can keep running while the error sits there.</p>

<ul>
    <li><strong>Medicare:</strong> the claim must generally be filed no later than 1 calendar year after the date of service (42 CFR 424.44). The rule allows a few exceptions, such as when the delay was caused by an error of a Medicare contractor or when Medicare coverage was granted retroactively.</li>
    <li><strong>Private plans and Medicaid:</strong> limits vary by plan, state and the hospital&rsquo;s contract. Ask the billing office what limit applies.</li>
</ul>

<p><strong>Example:</strong> a Medicare patient&rsquo;s visit on March 3, 2026 is rejected for a misspelled name. The corrected claim should be filed by about March 3, 2027. The sooner you call, the more room everyone has. If a deadline is missed because of a registration error, ask the hospital in writing how it will handle the balance.</p>

<h2 id="life-changes">7. New card, new baby, new name</h2>

<h3>New insurance card after open enrollment</h3>
<p>If you switched plans or got a new ID number, the hospital may still have your old card on file. Show the new card at every visit. See our <a href="/guides/open-enrollment-health-insurance/">open enrollment guide</a> for what changes each year.</p>

<h3>A newborn added to your plan</h3>
<p>A baby may be billed under a parent&rsquo;s name or ID, or before being added to the plan. Birth is a qualifying event for a special enrollment period (a window to add someone outside open enrollment):</p>
<ul>
    <li><strong>Employer group plans:</strong> the plan must give you at least 30 days after the birth to request enrollment, and coverage must begin on the date of birth (29 CFR 2590.701-6).</li>
    <li><strong>Marketplace (HealthCare.gov and state exchange) plans:</strong> you generally have 60 days after the birth to pick a plan, and coverage must be effective on the date of birth (45 CFR 155.420).</li>
</ul>
<p>Once the baby is enrolled, ask the hospital to rebill the baby&rsquo;s claims with the baby&rsquo;s own name, birth date and member ID.</p>

<h3>A name change</h3>
<p>Tell your insurer and the hospital. For Medicare, your card shows the name on file with Social Security, so update Social Security first. Until then, give the hospital the name exactly as it appears on your card.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>After a plan change, a birth or a name change, check the first bill closely. If the claim was corrected and you still owe more than expected, <a href="/scan">scan your bill free</a> to look for duplicate charges and prices far above Medicare rates.</p>
</div>

<h2 id="not-a-typo">8. When it&rsquo;s not a typo</h2>

<p>Sometimes the &ldquo;wrong info&rdquo; isn&rsquo;t a slip of the keyboard. Watch for:</p>
<ul>
    <li>A name, address or birth date that isn&rsquo;t yours or a family member&rsquo;s</li>
    <li>A visit, test or medicine you never got</li>
    <li>A note from your insurer that you&rsquo;ve reached a benefit limit you didn&rsquo;t use</li>
    <li>A medical collection on your credit report you don&rsquo;t recognize</li>
</ul>

<p>The FTC lists these as warning signs of medical identity theft. It suggests getting your medical records, reporting errors in writing, checking your credit reports and making a recovery plan at IdentityTheft.gov. Our <a href="/guides/medical-identity-theft-bills/">medical identity theft guide</a> and our guide on <a href="/guides/how-to-request-medical-records/">how to request medical records</a> walk through each step. If the debt has gone to collections or you&rsquo;re being taken to court, consider talking to a consumer attorney or legal aid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can a typo in my name or birth date really cause a claim denial?</h3>
        <p>Yes. Insurers match each claim to a member by ID number, name and birth date. Medicare contractor Noridian says a patient name that is not an identical match will cause the claim to be rejected as unprocessable.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between a rejected claim and a denied claim?</h3>
        <p>A denied claim was processed and not paid, and can usually be appealed. A rejected or returned claim was not processed because information was missing or invalid. Medicare says such a claim is not denied and has no appeal rights; the fix is a corrected claim.</p>
    </div>
    <div class="faq-item">
        <h3>Who has to fix the claim, me or the hospital?</h3>
        <p>The hospital billing office sends the claim, so it corrects and resubmits it. Your part is to spot the error, give them the correct details from your card, and fix the source if it sits with your insurer, employer or Social Security.</p>
    </div>
    <div class="faq-item">
        <h3>Is there a deadline to resubmit a corrected claim?</h3>
        <p>Yes. Medicare generally requires a claim within 1 calendar year after the date of service (42 CFR 424.44). Private plans and Medicaid set their own limits. Ask the billing office which deadline applies.</p>
    </div>
    <div class="faq-item">
        <h3>Can I make the hospital correct my records?</h3>
        <p>You can ask. Under the HIPAA Privacy Rule (45 CFR 164.526), a hospital or health plan must act on a request to amend your information within 60 days, with one possible 30-day extension. It can deny the request if it finds the record accurate and complete.</p>
    </div>
    <div class="faq-item">
        <h3>What if the wrong information is not a typo at all?</h3>
        <p>If you see a name, visit or service you don&rsquo;t recognize, someone else may have used your insurance. The FTC suggests getting your medical records, reporting errors in writing and checking your credit reports. See our <a href="/guides/medical-identity-theft-bills/">medical identity theft guide</a> for steps.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 1: General Billing Requirements (incomplete or invalid claims, section 80.3)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25: Completing and Processing the Form CMS-1450 (UB-04)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c26pdf.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 26: Completing and Processing Form CMS-1500</a></li>
    <li><a href="https://www.cms.gov/outreach-and-education/mln/wbt/mln4462429-mln-wbt-1500/1500/lesson04/15/index.html" target="_blank" rel="noopener">CMS MLN &mdash; CMS-1500: Key Patient and Claim Information</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jeb/topics/claim-submission/instructions-02-12" target="_blank" rel="noopener">Noridian Medicare (JE Part B) &mdash; CMS-1500 Claim Form Instructions</a></li>
    <li><a href="https://x12.org/codes/claim-adjustment-reason-codes" target="_blank" rel="noopener">X12 &mdash; Claim Adjustment Reason Codes</a></li>
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 424.44, Time limits for filing claims</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.526" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 164.526, Amendment of protected health information</a></li>
    <li><a href="https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-B/part-2590/subpart-B/section-2590.701-6" target="_blank" rel="noopener">eCFR &mdash; 29 CFR 2590.701-6, Special enrollment periods (group health plans)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-155/subpart-E/section-155.420" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 155.420, Special enrollment periods (Marketplace)</a></li>
    <li><a href="https://www.medicare.gov/basics/get-started-with-medicare/using-medicare/your-medicare-card" target="_blank" rel="noopener">Medicare.gov &mdash; Your Medicare card</a></li>
    <li><a href="https://consumer.ftc.gov/articles/what-know-about-medical-identity-theft" target="_blank" rel="noopener">FTC &mdash; What To Know About Medical Identity Theft</a></li>
</ul>
""",
})
