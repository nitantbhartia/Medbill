"""Guide: How Much Does Therapy Cost Per Session? (2026 Prices)."""

from guides import register, _embed

register("therapy-cost-per-session", {
    "title": "How Much Does Therapy Cost Per Session? (2026 Prices)",
    "meta_description": "Therapy costs $100–$200/session without insurance, $20–$50 with insurance. See 2026 rates by therapy type, billing codes, and how to find affordable care.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does therapy cost per session without insurance in 2026?",
            "a": "Without insurance, therapy costs $100 to $200 per session on average, though rates range from $65 to $300 depending on the therapist&rsquo;s credentials, location, and session length. Psychiatrists who also prescribe medication typically charge $200 to $400. Many therapists offer sliding scale fees based on income, which can reduce costs to $30 to $80 per session. Community mental health centers and training clinics often charge $0 to $50.",
        },
        {
            "q": "How much does therapy cost with insurance?",
            "a": "With insurance, your out-of-pocket therapy cost is typically a $20 to $50 copay per session once your deductible is met, or 20 to 40% coinsurance before you hit your out-of-pocket maximum. If your deductible has not been met, you pay the insurer&rsquo;s allowed amount&mdash;usually $80 to $150 per session. Mental health parity law requires insurers to cover therapy at the same level as medical care.",
        },
        {
            "q": "What CPT codes are used for therapy billing?",
            "a": "The most common therapy CPT codes are 90837 (individual psychotherapy, 60 minutes), 90834 (individual psychotherapy, 45 minutes), 90832 (individual psychotherapy, 30 minutes), and 90791 (psychiatric diagnostic evaluation, the first intake session). Couples therapy often uses 90847 (family psychotherapy with patient present). Check your Explanation of Benefits for these codes to verify you were billed for the correct session length.",
        },
        {
            "q": "Does Medicare cover therapy?",
            "a": "Yes. Medicare Part B covers outpatient mental health services, including individual therapy, group therapy, and psychiatric evaluations. Medicare pays 80% of the approved amount after your Part B deductible ($257 in 2026). Your 20% share for a 60-minute session typically runs $22 to $35. Therapists must be licensed clinical social workers, psychologists, or psychiatrists to bill Medicare.",
        },
        {
            "q": "Is online therapy cheaper than in-person therapy?",
            "a": "Online therapy platforms like BetterHelp and Talkspace charge $65 to $100 per week as a subscription, which works out to $65 to $100 per session if you have one session weekly. Traditional in-person therapy costs $100 to $200 per session. However, subscription platforms are often not covered by insurance, so the comparison depends on your coverage. If you have insurance, in-network in-person therapy with a $30 copay is usually the better value.",
        },
    ],
    "body": f"""
<div class="answer-box">
    <p><strong>Direct answer:</strong> Therapy costs <strong>$100 to $200 per session</strong> without insurance in 2026. With insurance, expect a <strong>$20 to $50 copay</strong> per session once your deductible is met. Sliding scale fees, community mental health centers, and online platforms can reduce costs to $30 to $100 per session for those who qualify.</p>
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#therapy-cost-by-type">Therapy cost by type</a></li>
        <li><a href="#insurance-coverage">How insurance covers therapy</a></li>
        <li><a href="#affordable-options">Affordable therapy options</a></li>
        <li><a href="#online-therapy">Online therapy cost comparison</a></li>
        <li><a href="#medicare-medicaid">Medicare and Medicaid coverage</a></li>
        <li><a href="#billing-codes">Therapy billing codes explained</a></li>
        <li><a href="#billing-errors">Common therapy billing errors</a></li>
        <li><a href="#find-therapist">How to find an in-network therapist</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="therapy-cost-by-type">1. Therapy cost by type</h2>

<p>The type of therapy you receive directly affects what you pay. A 60-minute individual session with a licensed clinical social worker (LCSW) costs far less than an hour with a psychiatrist, and group therapy runs a fraction of individual rates. Here are typical 2026 cost ranges by therapy type:</p>

<table>
    <thead>
        <tr>
            <th>Therapy Type</th>
            <th>CPT Code</th>
            <th>Without Insurance</th>
            <th>With Insurance (Copay)</th>
            <th>Medicare Rate (2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Individual psychotherapy, 60 min (CBT, psychotherapy)</td><td>90837</td><td>$100&ndash;$200</td><td>$20&ndash;$50</td><td>$114</td></tr>
        <tr><td>Individual psychotherapy, 45 min</td><td>90834</td><td>$80&ndash;$160</td><td>$20&ndash;$45</td><td>$88</td></tr>
        <tr><td>Individual psychotherapy, 30 min</td><td>90832</td><td>$60&ndash;$120</td><td>$15&ndash;$35</td><td>$63</td></tr>
        <tr><td>Psychiatric diagnostic evaluation (intake)</td><td>90791</td><td>$150&ndash;$300</td><td>$30&ndash;$75</td><td>$168</td></tr>
        <tr><td>EMDR therapy, 60 min</td><td>90837</td><td>$120&ndash;$250</td><td>$20&ndash;$50</td><td>$114</td></tr>
        <tr><td>Couples / family therapy with patient present</td><td>90847</td><td>$120&ndash;$250</td><td>$25&ndash;$60</td><td>$112</td></tr>
        <tr><td>Group psychotherapy</td><td>90853</td><td>$30&ndash;$80</td><td>$10&ndash;$30</td><td>$56</td></tr>
    </tbody>
</table>

<p>Note that EMDR, CBT, and DBT are modalities, not separate billing categories&mdash;they all bill under the same individual session CPT codes based on session length. A therapist who specializes in EMDR may charge a premium, but your insurance processes the claim the same way as any other 60-minute session (90837).</p>

<p>Look up the Medicare rate for your therapy session CPT code:</p>

{_embed(mode="cost", cpt="90837", title="Therapy Session Cost", subtitle="90837 – Individual psychotherapy, 60 min")}

<h2 id="insurance-coverage">2. How insurance covers therapy</h2>

<p>The Mental Health Parity and Addiction Equity Act (MHPAEA) requires most health plans to cover mental health services&mdash;including therapy&mdash;at the same level as comparable medical and surgical benefits. In practice, this means:</p>

<ul>
    <li><strong>Same copay structure:</strong> If your plan charges a $30 specialist copay for a cardiologist visit, it must apply the same copay to therapy.</li>
    <li><strong>Session limits are restricted:</strong> Insurers cannot arbitrarily cap the number of therapy sessions covered per year unless they impose the same cap on medical visits.</li>
    <li><strong>Prior authorization varies:</strong> Some plans require PA after a set number of sessions (typically 8 to 12). Ask your insurer upfront whether ongoing therapy requires authorization.</li>
</ul>

<p>Your actual out-of-pocket cost depends on your plan year status:</p>

<ol>
    <li><strong>Before your deductible:</strong> You pay the insurer&rsquo;s allowed amount&mdash;typically $80 to $150 per session for CPT 90837.</li>
    <li><strong>After your deductible, before out-of-pocket max:</strong> You pay your coinsurance (usually 20&ndash;40% of the allowed amount), roughly $16 to $60 per session.</li>
    <li><strong>After your out-of-pocket max:</strong> Your plan pays 100%. If you attend therapy weekly and expect to hit your max, front-load sessions earlier in the year when possible.</li>
</ol>

<div class="key-takeaway">
    <strong>Always verify your therapist is in-network before your first appointment.</strong> Out-of-network therapy can cost 2 to 5 times more, and some plans offer no out-of-network mental health benefits at all.
</div>

<h2 id="affordable-options">3. Affordable therapy options</h2>

<p>If you are uninsured, underinsured, or simply cannot afford standard therapy rates, several legitimate options can bring costs to $0 to $80 per session:</p>

<table>
    <thead>
        <tr>
            <th>Option</th>
            <th>Typical Cost</th>
            <th>How to Access</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Sliding scale private therapist</td><td>$30&ndash;$80/session</td><td>Ask directly; many therapists reserve slots but don&rsquo;t advertise them</td></tr>
        <tr><td>Community mental health center</td><td>$0&ndash;$40/session</td><td>Search SAMHSA&rsquo;s facility locator at findtreatment.gov</td></tr>
        <tr><td>Open Path Collective</td><td>$30&ndash;$80/session</td><td>openpathcollective.org &mdash; one-time $65 membership fee</td></tr>
        <tr><td>University training clinic</td><td>$0&ndash;$30/session</td><td>Graduate students supervised by licensed clinicians</td></tr>
        <tr><td>Federally Qualified Health Center (FQHC)</td><td>Sliding scale</td><td>findahealthcenter.hrsa.gov</td></tr>
        <tr><td>Employee Assistance Program (EAP)</td><td>Free (3&ndash;8 sessions)</td><td>Contact your HR department</td></tr>
    </tbody>
</table>

<p><strong>Open Path Collective</strong> is particularly valuable: for a one-time $65 membership fee, you gain access to a network of licensed therapists who charge $30 to $80 per session to Open Path members. That&rsquo;s a significant discount from standard rates.</p>

<p><strong>Employee Assistance Programs (EAPs)</strong> are free and frequently overlooked. Most employers offer 3 to 8 free confidential counseling sessions per year through their EAP. Check with HR before paying out of pocket for your first therapy sessions.</p>

<h2 id="online-therapy">4. Online therapy cost comparison</h2>

<p>Online therapy platforms have expanded access significantly, but the pricing model is very different from traditional therapy. Here is a direct comparison:</p>

<table>
    <thead>
        <tr>
            <th>Platform / Type</th>
            <th>Weekly Cost</th>
            <th>Insurance Accepted?</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>BetterHelp</td><td>$65&ndash;$100/wk</td><td>No (some FSA/HSA)</td><td>Flexible access, no waitlist</td></tr>
        <tr><td>Talkspace</td><td>$69&ndash;$109/wk</td><td>Some plans</td><td>Messaging + video combo</td></tr>
        <tr><td>Cerebral (therapy + prescribing)</td><td>$99&ndash;$325/mo</td><td>Some plans</td><td>Combined therapy and medication</td></tr>
        <tr><td>In-network telehealth therapist</td><td>$20&ndash;$50 copay/session</td><td>Yes</td><td>Best value with insurance</td></tr>
        <tr><td>In-person in-network therapist</td><td>$20&ndash;$50 copay/session</td><td>Yes</td><td>Full range of therapy types</td></tr>
    </tbody>
</table>

<p>The key distinction: subscription platforms like BetterHelp typically do not bill insurance, so you pay the full subscription cost regardless of your coverage. If you have insurance with mental health benefits, finding an in-network telehealth therapist through your insurer&rsquo;s directory is almost always cheaper. Many traditional therapists now offer video sessions at the same rate as in-person visits.</p>

<h2 id="medicare-medicaid">5. Medicare and Medicaid coverage</h2>

<p><strong>Medicare Part B</strong> covers outpatient mental health services at 80% of the approved amount after your deductible is met. Eligible providers include:</p>
<ul>
    <li>Psychiatrists and other physicians</li>
    <li>Clinical psychologists</li>
    <li>Licensed clinical social workers (LCSWs)</li>
    <li>Clinical nurse specialists</li>
    <li>Nurse practitioners and physician assistants</li>
</ul>

<p>Medicare&rsquo;s approved amount for CPT 90837 (60-minute individual therapy) is approximately $114 in 2026. After your $257 Part B deductible, you owe 20%, or roughly $23 per session. If you have a Medicare Supplement (Medigap) plan, it typically covers that 20% coinsurance, making therapy effectively free after the deductible.</p>

<p><strong>Medicaid</strong> covers mental health services in all 50 states, though the scope and cost sharing vary significantly by state. Most Medicaid plans cover therapy with $0 to $4 copays. If you are on Medicaid, use your state&rsquo;s Medicaid provider directory to find covered therapists&mdash;not all private therapists accept Medicaid.</p>

<h2 id="billing-codes">6. Therapy billing codes explained</h2>

<p>Understanding the CPT codes on your Explanation of Benefits (EOB) lets you verify you were billed correctly for the session you actually received. Therapists sometimes bill for a longer session than was provided&mdash;a form of upcoding that affects 19% of mental health claims according to BillKarma&rsquo;s data.</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Session Length</th>
            <th>Medicare Rate (2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>90791</td><td>Psychiatric diagnostic evaluation (intake)</td><td>45&ndash;75 min</td><td>$168</td></tr>
        <tr><td>90832</td><td>Individual psychotherapy</td><td>30 min</td><td>$63</td></tr>
        <tr><td>90834</td><td>Individual psychotherapy</td><td>45 min</td><td>$88</td></tr>
        <tr><td>90837</td><td>Individual psychotherapy</td><td>60 min</td><td>$114</td></tr>
        <tr><td>90847</td><td>Family psychotherapy, with patient present</td><td>50+ min</td><td>$112</td></tr>
        <tr><td>90846</td><td>Family psychotherapy, without patient present</td><td>50+ min</td><td>$101</td></tr>
        <tr><td>90853</td><td>Group psychotherapy</td><td>Variable</td><td>$56</td></tr>
    </tbody>
</table>

<p>After each session, note the actual length. If your therapist consistently runs 45-minute sessions but bills 90837 (60 minutes), that is upcoding. Your EOB will show the CPT code submitted. If the code does not match the session you received, contact your insurer&rsquo;s fraud and abuse hotline.</p>

<h2 id="billing-errors">7. Common therapy billing errors</h2>

<p>BillKarma&rsquo;s analysis finds that billing errors affect <strong>19% of mental health claims</strong>&mdash;a rate higher than most medical specialties. The most common errors include:</p>

<ol>
    <li><strong>Upcoded session length:</strong> Billing 90837 (60 min) for a 45-minute session. The difference is about $26 in Medicare rates&mdash;but insurers may pay $50 to $80 more for the longer code.</li>
    <li><strong>Wrong diagnosis code:</strong> Mental health billing requires a DSM-5 diagnosis code (ICD-10). If the wrong code is submitted, your claim may be denied or incorrectly categorized.</li>
    <li><strong>Billing 90791 for follow-up sessions:</strong> The psychiatric evaluation code is for the first intake appointment only. Some providers incorrectly bill it for standard sessions, which are more expensive.</li>
    <li><strong>Duplicate billing:</strong> The same session billed twice, or billed to both insurance and the patient for the same service.</li>
    <li><strong>No-show billed as a session:</strong> Missed appointments cannot be billed to insurance under therapy CPT codes (though a cancellation fee may be charged directly to the patient).</li>
</ol>

<div class="key-takeaway">
    <strong>Got a therapy bill that looks wrong?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we cross-reference each CPT code against session records and flag charges that exceed Medicare rates or appear inconsistent with standard billing practices.
</div>

<h2 id="find-therapist">8. How to find an in-network therapist</h2>

<p>Finding an in-network therapist takes more effort than finding an in-network physician, because mental health provider directories are notoriously inaccurate. Studies show that up to 45% of directory listings are outdated. Follow these steps to avoid surprise bills:</p>

<ol>
    <li><strong>Start with your insurer&rsquo;s online directory.</strong> Filter by specialty (e.g., licensed clinical social worker, psychologist), location, and whether they are accepting new patients.</li>
    <li><strong>Call the therapist&rsquo;s office directly</strong> before scheduling. Confirm they are still in-network with your specific plan (not just the insurer family&mdash;plans within the same insurer can have different networks).</li>
    <li><strong>Confirm the CPT codes they bill.</strong> Ask whether they bill 90837, 90834, or 90832 for standard sessions so you can estimate your cost share in advance.</li>
    <li><strong>Ask about prior authorization requirements.</strong> Call your insurer and ask whether your plan requires PA for ongoing therapy and after how many sessions.</li>
    <li><strong>Use Psychology Today&rsquo;s directory</strong> (psychologytoday.com/us/therapists) as a supplemental search tool&mdash;it allows filtering by insurance, specialty, and cost.</li>
    <li><strong>Verify after your first visit.</strong> Check your EOB after your first session to confirm the claim was processed in-network. Catching an out-of-network error early prevents larger bills later.</li>
</ol>

<div class="key-takeaway">
    <strong>Already received an unexpected therapy bill?</strong> <a href="/fight-debt">Use BillKarma&rsquo;s dispute tools</a> to challenge out-of-network charges, request itemized statements, and access letter templates to dispute billing errors with your provider and insurer.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does therapy cost per session without insurance in 2026?</h3>
        <p>Without insurance, therapy costs $100 to $200 per session on average, though rates range from $65 to $300 depending on the therapist&rsquo;s credentials, location, and session length. Psychiatrists who also prescribe medication typically charge $200 to $400. Many therapists offer sliding scale fees based on income, which can reduce costs to $30 to $80 per session. Community mental health centers and training clinics often charge $0 to $50.</p>
    </div>
    <div class="faq-item">
        <h3>How much does therapy cost with insurance?</h3>
        <p>With insurance, your out-of-pocket therapy cost is typically a $20 to $50 copay per session once your deductible is met, or 20 to 40% coinsurance before you hit your out-of-pocket maximum. If your deductible has not been met, you pay the insurer&rsquo;s allowed amount&mdash;usually $80 to $150 per session. Mental health parity law requires insurers to cover therapy at the same level as medical care.</p>
    </div>
    <div class="faq-item">
        <h3>What CPT codes are used for therapy billing?</h3>
        <p>The most common therapy CPT codes are 90837 (individual psychotherapy, 60 minutes), 90834 (individual psychotherapy, 45 minutes), 90832 (individual psychotherapy, 30 minutes), and 90791 (psychiatric diagnostic evaluation, the first intake session). Couples therapy often uses 90847 (family psychotherapy with patient present). Check your Explanation of Benefits for these codes to verify you were billed for the correct session length.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover therapy?</h3>
        <p>Yes. Medicare Part B covers outpatient mental health services, including individual therapy, group therapy, and psychiatric evaluations. Medicare pays 80% of the approved amount after your Part B deductible ($257 in 2026). Your 20% share for a 60-minute session typically runs $22 to $35. Therapists must be licensed clinical social workers, psychologists, or psychiatrists to bill Medicare.</p>
    </div>
    <div class="faq-item">
        <h3>Is online therapy cheaper than in-person therapy?</h3>
        <p>Online therapy platforms like BetterHelp and Talkspace charge $65 to $100 per week as a subscription, which works out to $65 to $100 per session if you have one session weekly. Traditional in-person therapy costs $100 to $200 per session. However, subscription platforms are often not covered by insurance, so the comparison depends on your coverage. If you have insurance, in-network in-person therapy with a $30 copay is usually the better value.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Mental Health</a></li>
    <li><a href="https://www.samhsa.gov/find-help/national-helpline" target="_blank" rel="noopener">SAMHSA: National Helpline and Treatment Locator</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">U.S. Department of Labor: Mental Health Parity and Addiction Equity Act</a></li>
    <li><a href="https://openpathcollective.org/" target="_blank" rel="noopener">Open Path Collective: Affordable Therapy Network</a></li>
    <li><a href="https://www.kff.org/mental-health/issue-brief/mental-health-care-costs-and-coverage/" target="_blank" rel="noopener">KFF: Mental Health Care Costs and Coverage</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.00337" target="_blank" rel="noopener">Health Affairs: Mental Health Provider Directory Accuracy</a></li>
    <li><a href="https://findtreatment.gov/" target="_blank" rel="noopener">SAMHSA: Find Treatment Facility Locator</a></li>
</ul>
""",
})
