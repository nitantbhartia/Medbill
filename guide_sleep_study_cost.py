"""Guide: Sleep Study Cost in 2026: In-Lab vs. Home Test."""

from guides import register, _embed

register("sleep-study-cost", {
    "title": "Sleep Study Cost in 2026: In-Lab vs. Home Test",
    "meta_description": "In-lab sleep studies cost $1,000&ndash;$7,000; home sleep tests run $150&ndash;$500. Medicare covers both. See CPT codes, prior auth rules, and billing errors found in 23% of sleep medicine claims.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does a sleep study cost without insurance in 2026?",
            "a": "Without insurance, an in-lab polysomnography (PSG) costs $1,000 to $7,000 depending on the facility type. Hospital-based sleep labs charge $3,000&ndash;$7,000; freestanding sleep centers charge $1,000&ndash;$3,500. A home sleep apnea test (HSAT) costs $150&ndash;$500 without insurance and is the lower-cost alternative for patients whose symptoms suggest straightforward obstructive sleep apnea. With insurance, your out-of-pocket after the deductible is typically $300&ndash;$800 for an in-lab PSG.",
        },
        {
            "q": "Does Medicare cover sleep studies?",
            "a": "Yes. Medicare Part B covers in-lab polysomnography (CPT 95810) for patients with moderate-to-severe obstructive sleep apnea symptoms at 80% after the Part B deductible. Medicare also covers the home sleep apnea test (CPT 95806) as a less expensive alternative&mdash;CMS generally requires HSAT to be tried first for uncomplicated OSA before approving an in-lab study. Both require a physician order. Prior authorization is common for PSG under Medicare Advantage plans.",
        },
        {
            "q": "What symptoms does insurance require before covering a sleep study?",
            "a": "Most insurance plans require documented symptoms consistent with obstructive sleep apnea before approving a sleep study. Typical requirements include at least two of the following: loud or disruptive snoring, witnessed apneas (pauses in breathing observed by a bed partner), excessive daytime sleepiness, morning headaches, or impaired concentration. Your physician should document these symptoms in a clinical note before ordering the study to support insurance coverage.",
        },
        {
            "q": "What is the difference between CPT 95810 and CPT 95806?",
            "a": "CPT 95810 is an attended in-laboratory polysomnography&mdash;a comprehensive overnight sleep study with a technologist present monitoring EEG, EKG, oxygen saturation, airflow, respiratory effort, and limb movements. CPT 95806 is a home sleep apnea test (HSAT)&mdash;an unattended portable device worn at home that measures a subset of signals (airflow, oxygen saturation, respiratory effort). The HSAT is appropriate for patients with high pre-test probability of uncomplicated OSA. It cannot detect non-apnea sleep disorders and is not appropriate for patients with suspected narcolepsy, REM sleep behavior disorder, or severe comorbidities.",
        },
        {
            "q": "How does a sleep study diagnosis lead to CPAP coverage?",
            "a": "A sleep study that documents an apnea-hypopnea index (AHI) of 5 or more events per hour (with symptoms) or 15 or more events per hour (without symptoms) establishes the diagnosis of obstructive sleep apnea. This diagnosis then triggers insurance coverage for a CPAP machine, mask, and supplies. Medicare covers CPAP as durable medical equipment (DME) under Part B. Compliance is required for ongoing coverage: Medicare requires patients to show the CPAP is being used for at least 4 hours per night on 70% of nights during the first 90-day trial period.",
        },
    ],
    "body": f"""
<p class="lead">Sleep studies diagnose obstructive sleep apnea (OSA), the most common sleep disorder in the United States&mdash;affecting an estimated 30 million Americans, most of them undiagnosed. A single overnight sleep study is the gateway to CPAP coverage, and the test itself is covered by Medicare and most commercial insurance. But facility type, billing codes, and prior authorization rules create a surprisingly complicated billing landscape. BillKarma finds billing errors in <strong>23% of sleep medicine claims</strong>. This guide shows you what each test costs, what insurance covers, and how to avoid paying for a test you shouldn&rsquo;t have been billed for.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> In-lab polysomnography costs <strong>$1,000&ndash;$7,000</strong> without insurance; a home sleep apnea test costs <strong>$150&ndash;$500</strong>. With insurance, expect <strong>$300&ndash;$800 out of pocket</strong> for an in-lab study after your deductible. Medicare covers both under Part B at 80% after the deductible with a physician order. Prior authorization is common for the in-lab study&mdash;insurers often require an HSAT first for straightforward OSA. Billing errors in 23% of claims include billing PSG when only an HSAT was done and unbundled scoring charges.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#psg-vs-hsat">In-lab PSG vs. home sleep apnea test: which one do you need?</a></li>
        <li><a href="#cost-table">Cost comparison by facility type</a></li>
        <li><a href="#insurance-requirements">What insurance requires before covering a sleep study</a></li>
        <li><a href="#medicare">Medicare coverage: PSG and HSAT</a></li>
        <li><a href="#facility-types">Hospital-based lab vs. freestanding sleep center</a></li>
        <li><a href="#cpt-codes">CPT codes on your sleep study bill</a></li>
        <li><a href="#billing-errors">Common billing errors to look for</a></li>
        <li><a href="#cpap-connection">How your diagnosis triggers CPAP coverage</a></li>
        <li><a href="#action-steps">Action steps before and after your sleep study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="psg-vs-hsat">1. In-lab PSG vs. home sleep apnea test: which one do you need?</h2>

<p>Two very different types of tests carry the &ldquo;sleep study&rdquo; label, and they cost and reimburse very differently.</p>

<p>A <strong>polysomnography (PSG)</strong> is an attended, in-laboratory study. You sleep overnight in a sleep center while a trained technologist monitors your brain waves (EEG), heart rhythm (EKG), eye movements, muscle activity, oxygen saturation, airflow, and chest/abdominal movement. It can diagnose the full range of sleep disorders: obstructive sleep apnea, central sleep apnea, narcolepsy, periodic limb movement disorder, REM sleep behavior disorder, and more.</p>

<p>A <strong>home sleep apnea test (HSAT)</strong> is an unattended portable test you wear while sleeping in your own bed. It measures a subset of signals&mdash;typically airflow, oxygen saturation, and respiratory effort. It is appropriate only for patients with a high pre-test likelihood of moderate-to-severe obstructive sleep apnea and no significant comorbidities. It cannot diagnose non-apnea sleep disorders.</p>

<p>Insurers increasingly require an HSAT first for uncomplicated OSA and will only approve an in-lab PSG if the HSAT is inconclusive, technically inadequate, or if the clinical presentation suggests a disorder other than standard OSA. Know which test your physician ordered before you show up at the facility.</p>

<h2 id="cost-table">2. Cost comparison by facility type</h2>

<table>
    <thead>
        <tr>
            <th>Test Type / Facility</th>
            <th>Cash Price (No Insurance)</th>
            <th>With Insurance (After Deductible)</th>
            <th>Medicare Rate (2026, approx.)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>In-lab PSG &mdash; freestanding sleep center</td><td>$1,000&ndash;$3,500</td><td>$300&ndash;$700</td><td>~$700&ndash;$900 total</td></tr>
        <tr><td>In-lab PSG &mdash; hospital-based lab</td><td>$3,000&ndash;$7,000</td><td>$600&ndash;$1,400</td><td>Higher (facility fee applies)</td></tr>
        <tr><td>In-lab PSG with CPAP titration (split-night)</td><td>$2,000&ndash;$6,000</td><td>$400&ndash;$1,200</td><td>~$800&ndash;$1,100 total</td></tr>
        <tr><td>CPAP titration-only night</td><td>$1,500&ndash;$4,000</td><td>$300&ndash;$800</td><td>~$600&ndash;$800</td></tr>
        <tr><td>Home sleep apnea test (HSAT)</td><td>$150&ndash;$500</td><td>$50&ndash;$150</td><td>~$150&ndash;$300</td></tr>
    </tbody>
</table>

<p>Hospital-based sleep labs apply a facility fee surcharge&mdash;exactly as hospital outpatient departments do for other procedures. A freestanding, accredited sleep center can perform an identical in-lab PSG for 50&ndash;60% of what a hospital-based lab charges. If your physician&rsquo;s office schedules you at a hospital sleep lab by default, ask whether an accredited freestanding center is available and in-network.</p>

{_embed(mode="cost", cpt="95810", title="Look up sleep study CPT costs", subtitle="See what Medicare pays for in-lab polysomnography (CPT 95810).")}

<h2 id="insurance-requirements">3. What insurance requires before covering a sleep study</h2>

<p>Insurance plans do not automatically approve sleep study claims. Most require documented evidence that the study is medically necessary. Typical documentation requirements include:</p>

<ul>
    <li><strong>Symptom documentation:</strong> At least two OSA symptoms documented by your physician in a clinical note: snoring, witnessed apneas, excessive daytime sleepiness, morning headaches, or impaired concentration.</li>
    <li><strong>Physician order:</strong> A written order from a licensed physician (not a nurse practitioner in all states, depending on plan language).</li>
    <li><strong>Prior authorization:</strong> Most commercial plans and many Medicare Advantage plans require prior auth before an in-lab PSG. Your sleep center should obtain this before your study date. If they did not, call your insurer before the appointment.</li>
    <li><strong>HSAT first:</strong> Many plans require a home sleep apnea test to be completed and either inconclusive or technically failed before approving an in-lab study for standard OSA symptoms. Know what your plan requires.</li>
    <li><strong>Non-apnea disorder screening:</strong> If your physician suspects narcolepsy, REM sleep behavior disorder, or another non-apnea disorder, insurers typically cover the in-lab PSG without requiring an HSAT first, because the HSAT cannot diagnose those conditions.</li>
</ul>

<h2 id="medicare">4. Medicare coverage: PSG and HSAT</h2>

<p>Medicare Part B covers sleep studies when ordered by a treating physician for a Medicare beneficiary with documented OSA symptoms. Coverage details:</p>

<ul>
    <li><strong>In-lab PSG (CPT 95810):</strong> Covered at 80% after the Part B deductible for patients with moderate-to-severe OSA symptoms. Often requires prior authorization under Medicare Advantage plans.</li>
    <li><strong>HSAT (CPT 95806):</strong> Covered at 80% after deductible as the preferred first-line test for straightforward OSA symptoms. CMS has actively encouraged HSAT use to reduce costs.</li>
    <li><strong>Split-night study (CPT 95811):</strong> Covered when the first part of the night documents OSA and the second part is used for CPAP titration, avoiding a second separate visit.</li>
    <li><strong>CPAP titration night (CPT 95811 or 95810 with titration modifier):</strong> Covered after PSG confirms OSA diagnosis.</li>
</ul>

<p>Medicare does not require an HSAT before approving a PSG if the treating physician documents a clinical reason why in-lab testing is necessary (complex comorbidities, suspected non-apnea disorder, technically challenging HSAT candidate).</p>

<h2 id="facility-types">5. Hospital-based lab vs. freestanding sleep center</h2>

<p>The facility type determines how the sleep study is billed under Medicare and commercial insurance.</p>

<p>A <strong>hospital-based sleep lab</strong> bills the technical component of the sleep study (equipment, technologist, scoring) under the hospital outpatient prospective payment system (OPPS). This means a facility fee is applied on top of the procedure rate, increasing your cost-sharing. The interpreting physician bills separately under the physician fee schedule.</p>

<p>A <strong>freestanding accredited sleep center</strong> bills the technical and professional components under the physician/outpatient fee schedule without a hospital facility surcharge. The total allowed amount is lower, meaning your deductible and coinsurance dollars go further.</p>

<p>Accreditation matters: the American Academy of Sleep Medicine (AASM) accredits sleep centers to defined quality standards. Most insurers require AASM accreditation for coverage of in-lab PSG. Before scheduling, verify your sleep center is AASM-accredited and in-network with your plan.</p>

<h2 id="cpt-codes">6. CPT codes on your sleep study bill</h2>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Rate (2026, approx.)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>95810</td><td>Polysomnography, age 6+, w/ CPAP titration&mdash;attended (full PSG)</td><td>~$800&ndash;$900 (combined tech + professional)</td></tr>
        <tr><td>95808</td><td>Polysomnography without CPAP titration, 4+ additional parameters</td><td>~$700&ndash;$800</td></tr>
        <tr><td>95806</td><td>Sleep study, unattended (HSAT), minimum 3 channels</td><td>~$150&ndash;$300</td></tr>
        <tr><td>95811</td><td>Polysomnography, CPAP titration night (separate night from diagnostic PSG)</td><td>~$750&ndash;$900</td></tr>
        <tr><td>95782</td><td>Polysomnography, under age 6 (pediatric)</td><td>Higher than adult rate</td></tr>
        <tr><td>95800</td><td>Sleep study, unattended, 4+ channels including O2 and airflow</td><td>~$200&ndash;$350</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">7. Common billing errors to look for</h2>

<p>BillKarma identifies billing errors in <strong>23% of sleep medicine claims</strong>. The most common:</p>

<ul>
    <li><strong>Billing PSG (95810) when only an HSAT (95806) was performed:</strong> The PSG code pays significantly more than the HSAT code. If you wore a portable home device rather than spending the night in a sleep lab with monitoring leads, the claim should use 95806 or 95800, not 95810.</li>
    <li><strong>Unbundled sleep scoring charges:</strong> Physician interpretation and scoring of PSG results is included in the professional component of CPT 95810/95808. Billing a separate scoring or interpretation fee on top of the PSG code is unbundling and violates Medicare bundling rules.</li>
    <li><strong>Duplicate facility and professional component billing:</strong> In a hospital-based lab, the facility and physician bill separately. Some billing systems generate duplicate claims for the same professional service. Review your EOB to confirm you are not being billed twice for the interpretation.</li>
    <li><strong>Billing a full PSG when a split-night study was performed:</strong> A split-night study (CPT 95811) combines the diagnostic and titration components in one night. Some facilities bill two separate PSG codes (diagnostic + titration) as though these were two separate nights. If your study was a split-night, there should be one claim, not two.</li>
    <li><strong>Billing the wrong CPT code for the patient&rsquo;s age:</strong> The pediatric PSG code (95782 for patients under age 6) pays differently from the adult code. Age-code mismatches can result in either overpayment or underpayment depending on direction.</li>
</ul>

<h2 id="cpap-connection">8. How your diagnosis triggers CPAP coverage</h2>

<p>A sleep study that confirms obstructive sleep apnea is the first step in a coverage chain that includes CPAP equipment. Medicare and commercial insurance cover CPAP as durable medical equipment (DME) once OSA is diagnosed. The key thresholds:</p>

<ul>
    <li><strong>Apnea-Hypopnea Index (AHI) &ge; 5 with symptoms,</strong> or AHI &ge; 15 without symptoms, qualifies for CPAP coverage under Medicare.</li>
    <li>Medicare covers CPAP rental for the first 3 months, then requires a face-to-face physician visit documenting continued use and benefit. If documented, coverage continues through month 13, after which Medicare continues coverage for the duration of need.</li>
    <li><strong>Compliance requirement:</strong> Medicare requires the patient to use CPAP for at least 4 hours per night on 70% of nights during the first 90-day trial. Non-compliance triggers coverage termination. Keep your data downloads from your CPAP device to document compliance.</li>
    <li>The home sleep apnea test (95806) and the in-lab PSG (95810) both qualify as the diagnostic study for CPAP coverage&mdash;the type of study does not affect CPAP eligibility, only the AHI result matters.</li>
</ul>

<p>See our companion guide on CPAP machine costs for a full breakdown of what Medicare and commercial insurance cover for the device, masks, and supplies.</p>

<h2 id="action-steps">9. Action steps before and after your sleep study</h2>

<ol>
    <li><strong>Confirm prior authorization was obtained.</strong> Before your appointment, call your insurer to verify a prior auth is in place for the specific CPT code (95810 for in-lab PSG or 95806 for HSAT). Note the reference number.</li>
    <li><strong>Verify the facility type and network status.</strong> Confirm whether the sleep lab is hospital-based or freestanding, and confirm it is in-network with your specific insurance plan. Freestanding AASM-accredited centers typically cost significantly less.</li>
    <li><strong>Clarify which test you are having.</strong> Before you complete intake paperwork, confirm whether you are having an in-lab study (you sleep there overnight) or a home sleep apnea test (you take a portable device home). This determines which CPT code should appear on your bill.</li>
    <li><strong>Request your sleep study report after the visit.</strong> You are entitled to the full polysomnography report, not just the summary. The report documents the AHI, the number of channels recorded, and the technologist&rsquo;s notes&mdash;all of which should match the CPT code billed.</li>
    <li><strong>Review your EOB carefully.</strong> Match the CPT codes on the facility bill and physician bill to what the study report documents. A home study billed as 95810 (in-lab PSG) is a common error worth disputing.</li>
    <li><strong>Document CPAP compliance from day one.</strong> If your study confirms OSA and you are prescribed a CPAP, download your compliance data from the device&rsquo;s app or patient portal monthly. You will need this data to maintain Medicare coverage past the 90-day trial period.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a sleep study cost without insurance in 2026?</h3>
        <p>An in-lab polysomnography costs $1,000&ndash;$7,000 without insurance depending on whether it is at a freestanding sleep center or a hospital-based lab. A home sleep apnea test costs $150&ndash;$500. With insurance, expect $300&ndash;$800 out of pocket for an in-lab study after meeting your deductible.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover sleep studies?</h3>
        <p>Yes. Medicare Part B covers both in-lab polysomnography (CPT 95810) and home sleep apnea tests (CPT 95806) at 80% after the Part B deductible when ordered by a physician for documented OSA symptoms. Medicare generally prefers the lower-cost HSAT first for uncomplicated OSA. Both tests qualify a patient for CPAP coverage if OSA is confirmed.</p>
    </div>
    <div class="faq-item">
        <h3>What is the most common sleep study billing error?</h3>
        <p>Billing the in-lab PSG code (CPT 95810) when the patient actually took a portable home sleep apnea test device home (which should be billed as CPT 95806) is the most common error BillKarma finds. The PSG code pays substantially more. If you slept in your own bed with a portable device rather than spending the night at a sleep center, your bill should not show CPT 95810.</p>
    </div>
    <div class="faq-item">
        <h3>Do I need prior authorization for a sleep study?</h3>
        <p>Most commercial plans and Medicare Advantage plans require prior authorization for an in-lab PSG. HSAT (home sleep test) prior auth requirements vary by plan. Always verify PA was obtained before your study date&mdash;a denied claim for lack of prior auth can leave you responsible for the full cost.</p>
    </div>
    <div class="faq-item">
        <h3>How does a sleep study connect to CPAP coverage?</h3>
        <p>A sleep study documenting an AHI of 5+ with symptoms (or 15+ without symptoms) establishes the OSA diagnosis that triggers CPAP coverage under Medicare and most commercial plans. Medicare covers CPAP rental initially, then continued coverage if you demonstrate compliance (4+ hours/night on 70% of nights in the first 90 days). The CPAP device is covered as durable medical equipment under Medicare Part B.</p>
    </div>
</div>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;border-radius:6px;padding:1.25rem 1.5rem;margin:2rem 0;">
    <strong>Got a sleep study bill that seems too high?</strong><br>
    BillKarma finds billing errors in 23% of sleep medicine claims&mdash;including PSG upcoding, unbundled scoring, and duplicate billing. Upload your bill and we&rsquo;ll show you what you actually owe.
    <br><br>
    <a href="/fight-debt" style="background:#2563eb;color:#fff;padding:0.5rem 1.25rem;border-radius:4px;text-decoration:none;font-weight:600;">Fight your bill &rarr;</a>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/sleep-disorders" target="_blank" rel="noopener">CMS Medicare Coverage: Sleep Studies and CPAP</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Sleep Medicine</a></li>
    <li><a href="https://aasm.org/clinical-resources/practice-standards/" target="_blank" rel="noopener">American Academy of Sleep Medicine: Clinical Practice Guidelines</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient PPS 2026 &mdash; Sleep Lab Facility Fees</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-coverage-of-dme/" target="_blank" rel="noopener">KFF: Medicare Coverage of Durable Medical Equipment (CPAP)</a></li>
    <li><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6226278/" target="_blank" rel="noopener">NCBI: Home Sleep Testing vs. PSG Comparative Effectiveness</a></li>
</ul>
""",
})
