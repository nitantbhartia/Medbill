"""Guide: Hearing Aid Cost & Insurance Coverage in 2026."""

from guides import register, _embed

register("hearing-aid-cost", {
    "title": "Hearing Aid Cost & Insurance Coverage in 2026",
    "meta_description": "Hearing aids cost $200–$7,000/pair in 2026. Medicare covers $0 for traditional aids, but OTC options are now legal. See HCPCS codes, state Medicaid coverage, and how to spot billing fraud.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much do hearing aids cost in 2026?",
            "a": "Traditional prescription hearing aids dispensed by an audiologist cost $2,000 to $7,000 per pair, including professional fitting services. Over-the-counter (OTC) hearing aids&mdash;now legal in the US since October 2022&mdash;cost $200 to $1,500 per pair and are available without a prescription at pharmacies and online retailers. OTC aids are appropriate only for adults with mild-to-moderate hearing loss.",
        },
        {
            "q": "Does Medicare cover hearing aids?",
            "a": "Original Medicare (Parts A and B) does not cover hearing aids or the routine hearing exams used to fit them. This is one of the largest coverage gaps in Medicare. However, many Medicare Advantage (Part C) plans offer hearing aid benefits, typically covering one pair every one to three years with an allowance of $500 to $2,500. If you have Medicare Advantage, call your plan to verify your specific hearing benefit.",
        },
        {
            "q": "What is the difference between OTC and prescription hearing aids?",
            "a": "OTC hearing aids are self-fitting devices intended for adults with perceived mild-to-moderate hearing loss. They do not require a hearing exam or audiologist fitting. Prescription hearing aids are professionally programmed to match your specific audiogram results and are appropriate for all levels of hearing loss including moderate-to-severe and severe-to-profound. Children and anyone with sudden hearing loss, ear drainage, or asymmetric hearing loss should see an audiologist rather than using OTC devices.",
        },
        {
            "q": "What HCPCS codes are used for hearing aid billing?",
            "a": "Hearing aids are billed using HCPCS (Healthcare Common Procedure Coding System) V codes: V5244 (monaural hearing aid, analog), V5247 (monaural hearing aid, digital), V5261 (binaural digital hearing aids), and related codes for batteries (V5266), earmolds (V5264), and repairs (V5268). These codes appear on Medicare Advantage and Medicaid claims. Audiologist services use CPT codes 92550&ndash;92552 for audiometric exams.",
        },
        {
            "q": "How can I get hearing aids at low or no cost?",
            "a": "Several assistance programs help patients with limited income access hearing aids at reduced or no cost: the Starkey Hear Now foundation, Lions Club International, the Hearing Loss Association of America (HLAA) chapter networks, and the VA for eligible veterans. Many states have vocational rehabilitation programs that cover hearing aids for working-age adults whose hearing loss affects employment. Medicaid covers hearing aids for adults in 37 states.",
        },
    ],
    "body": f"""
<p class="lead">Traditional hearing aids cost <strong>$2,000 to $7,000 per pair</strong>&mdash;and Original Medicare covers <strong>none of it</strong>. That coverage gap affects 38 million Americans with hearing loss, making hearing aids one of the most out-of-pocket-intensive healthcare expenditures a senior faces. The good news: over-the-counter hearing aids became legal in October 2022, creating a $200&ndash;$1,500 option for mild-to-moderate loss, and Medicare Advantage plans, state Medicaid programs, and veterans&rsquo; benefits cover far more than most patients realize. This guide maps every coverage option, explains the billing codes, and flags the fraud patterns that Medicare targets heavily in this category.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:16px 20px;margin:24px 0;border-radius:4px;">
    <strong>Quick answer:</strong> OTC hearing aids ($200&ndash;$1,500/pair) work well for mild-to-moderate loss in adults. Traditional prescription aids ($2,000&ndash;$7,000/pair) are needed for moderate-to-severe loss. Medicare covers $0 for traditional aids; check your Medicare Advantage plan, state Medicaid, or VA benefits before paying out of pocket.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#hearing-aid-cost-table">Hearing aid costs: OTC vs. prescription</a></li>
        <li><a href="#otc-vs-prescription">Who qualifies for OTC hearing aids?</a></li>
        <li><a href="#medicare-coverage">Medicare coverage: the major gap explained</a></li>
        <li><a href="#medicaid-va">Medicaid, VA, and state coverage options</a></li>
        <li><a href="#assistance-programs">Assistance programs for low-income patients</a></li>
        <li><a href="#hcpcs-codes">HCPCS codes and how hearing aids are billed</a></li>
        <li><a href="#billing-fraud">Billing fraud: Medicare&rsquo;s most-targeted category</a></li>
        <li><a href="#action-steps">Action steps to access coverage</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="hearing-aid-cost-table">1. Hearing aid costs: OTC vs. prescription</h2>

<p>The FDA&rsquo;s 2022 rule creating the OTC hearing aid category fundamentally changed the market. Here is how costs compare across device categories in 2026:</p>

<table>
    <thead>
        <tr>
            <th>Category</th>
            <th>Cost per Pair</th>
            <th>Examples</th>
            <th>Fitting</th>
            <th>Appropriate For</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>OTC basic</td><td>$200&ndash;$500</td><td>Lexie B2, Sony CRE-20</td><td>Self-fitting app</td><td>Mild loss, adults 18+</td></tr>
        <tr><td>OTC mid-tier</td><td>$500&ndash;$1,000</td><td>Jabra Enhance Plus, Lexie Lumen</td><td>Self-fitting app</td><td>Mild-to-moderate loss</td></tr>
        <tr><td>OTC premium</td><td>$1,000&ndash;$1,500</td><td>Sony CRE-HX, Eargo 7</td><td>Self-fitting app</td><td>Mild-to-moderate loss</td></tr>
        <tr><td>Prescription entry-level</td><td>$2,000&ndash;$3,500</td><td>Widex Moment 110, Phonak Virto B70</td><td>Audiologist fitting</td><td>All loss levels</td></tr>
        <tr><td>Prescription mid-tier</td><td>$3,500&ndash;$5,500</td><td>Oticon More 2, Phonak Audeo L70</td><td>Audiologist fitting</td><td>All loss levels</td></tr>
        <tr><td>Prescription premium</td><td>$5,500&ndash;$7,000+</td><td>Widex Moment 440, Oticon Real 1</td><td>Audiologist fitting</td><td>Severe-to-profound loss</td></tr>
    </tbody>
</table>

<p>Traditional audiology dispensing bundles the cost of the device, fitting, and follow-up appointments into a single price. When comparison shopping, ask whether the quoted price is &ldquo;bundled&rdquo; (includes all follow-up) or &ldquo;unbundled&rdquo; (device only, services billed separately). Unbundled pricing averages $200&ndash;$400 per follow-up visit.</p>

{_embed(mode="cost", cpt="92550", title="Look up audiology exam rates", subtitle="See what Medicare pays for audiometric testing (CPT 92550).")}

<h2 id="otc-vs-prescription">2. Who qualifies for OTC hearing aids?</h2>

<p>OTC hearing aids are FDA-regulated for adults aged 18 and older with perceived mild-to-moderate hearing loss. They are not appropriate for:</p>

<ul>
    <li>Children under 18 (a hearing exam and audiologist fitting is required regardless of loss severity)</li>
    <li>Adults with moderate-to-severe or severe-to-profound hearing loss</li>
    <li>Anyone with sudden hearing loss (onset within 90 days), which requires medical evaluation</li>
    <li>Patients with asymmetric hearing loss (significant difference between ears), dizziness, or ear drainage</li>
    <li>Anyone who has not had a hearing test and does not know the degree of their loss</li>
</ul>

<p>A baseline audiogram (CPT 92550 or 92552) costs $50&ndash;$200 at an audiology clinic or community hearing center. This investment is worthwhile before purchasing OTC devices because it tells you whether OTC is clinically appropriate and gives you a baseline for future comparison.</p>

<h2 id="medicare-coverage">3. Medicare coverage: the major gap explained</h2>

<p>Original Medicare Part B covers medically necessary diagnostic hearing exams ordered by a physician (CPT 92550&ndash;92557 at roughly $50&ndash;$90 Medicare rate). But it explicitly excludes routine hearing exams and hearing aids. This exclusion has been in place since Medicare was created in 1965 and has not been changed by legislation as of 2026.</p>

<p>Medicare Advantage (Part C) plans may voluntarily offer hearing benefits. Coverage varies widely:</p>

<table>
    <thead>
        <tr>
            <th>Medicare Advantage Hearing Benefit Type</th>
            <th>Typical Coverage</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>No hearing benefit</td><td>$0 (same as original Medicare)</td></tr>
        <tr><td>Basic hearing allowance</td><td>$500&ndash;$1,000 per pair every 2&ndash;3 years</td></tr>
        <tr><td>Enhanced hearing benefit</td><td>$1,500&ndash;$2,500 per pair, sometimes annually</td></tr>
        <tr><td>Premium hearing benefit (select plans)</td><td>$2,500&ndash;$5,000 allowance, includes OTC</td></tr>
    </tbody>
</table>

<p>During Medicare open enrollment (October 15 &ndash; December 7), compare plans specifically on hearing benefits if you have hearing loss. A plan with a $2,000 hearing allowance can offset a significant portion of prescription aid cost every year.</p>

<h2 id="medicaid-va">4. Medicaid, VA, and state coverage options</h2>

<p><strong>Medicaid:</strong> 37 states cover hearing aids for adults through their Medicaid programs. Coverage limits vary by state&mdash;some cover one aid every three to five years, others cover binaural aids annually. Children are covered in all states under the EPSDT (Early and Periodic Screening, Diagnostic, and Treatment) mandate. Check your state Medicaid program&rsquo;s hearing benefit by calling the member services number on your Medicaid card.</p>

<p><strong>VA Benefits:</strong> The Department of Veterans Affairs provides hearing aids at no cost to eligible veterans with service-connected hearing loss or tinnitus. VA hearing aid benefits are among the most comprehensive available, covering premium prescription devices and batteries. Veterans with any VA disability rating should check their eligibility through the VA audiology program.</p>

<p><strong>State mandates for children:</strong> Arkansas, Minnesota, and several other states mandate insurance coverage for hearing aids specifically for children. Coverage typically runs $1,400&ndash;$3,000 per aid for minors. Check your state insurance commissioner&rsquo;s website for current mandate status.</p>

<h2 id="assistance-programs">5. Assistance programs for low-income patients</h2>

<p>When insurance does not cover hearing aids and the out-of-pocket cost is prohibitive, these programs provide direct assistance:</p>

<table>
    <thead>
        <tr>
            <th>Program</th>
            <th>Who It Serves</th>
            <th>How to Apply</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Starkey Hear Now (Starkey Hearing Foundation)</td><td>US adults with financial need</td><td>starkey.com/foundation</td></tr>
        <tr><td>Lions Club International</td><td>All ages; local chapter assistance</td><td>lionsclubs.org; contact local club</td></tr>
        <tr><td>HLAA Hearing Aid Assistance</td><td>Adults with financial need</td><td>hearingloss.org</td></tr>
        <tr><td>Audient Alliance</td><td>Low-income adults, age 18+</td><td>audientalliance.org</td></tr>
        <tr><td>State Vocational Rehabilitation</td><td>Working-age adults whose loss affects employment</td><td>Contact state VR agency</td></tr>
    </tbody>
</table>

<p>Most programs require documentation of hearing loss (audiogram), proof of financial need, and a referral from an audiologist or physician. Processing times range from two to eight weeks.</p>

<h2 id="hcpcs-codes">6. HCPCS codes and how hearing aids are billed</h2>

<p>Hearing aids are classified as durable medical equipment (DME) and billed using HCPCS V codes. These codes appear on Medicare Advantage and Medicaid claims:</p>

<table>
    <thead>
        <tr>
            <th>HCPCS Code</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>V5244</td><td>Hearing aid, monaural, analog, binaural fitting</td></tr>
        <tr><td>V5247</td><td>Hearing aid, monaural, digital</td></tr>
        <tr><td>V5248</td><td>Hearing aid, monaural, digital, binaural</td></tr>
        <tr><td>V5249</td><td>Hearing aid, binaural, digital</td></tr>
        <tr><td>V5261</td><td>Hearing aid, binaural, digital, fully digital</td></tr>
        <tr><td>V5264</td><td>Earmold / insert, not disposable, any type</td></tr>
        <tr><td>V5266</td><td>Battery for use in hearing device</td></tr>
        <tr><td>V5268</td><td>Assistive listening device, telephone amplifier</td></tr>
        <tr><td>V5274</td><td>Assistive listening device, not otherwise specified</td></tr>
        <tr><td>92550</td><td>Tympanometry and reflex threshold measurements (CPT)</td></tr>
        <tr><td>92552</td><td>Pure tone audiometry, air only (CPT)</td></tr>
    </tbody>
</table>

<p>The hearing exam (audiogram) is billed under CPT codes, not HCPCS codes, and is covered by Medicare Part B when ordered by a physician for diagnostic purposes. The hearing aid itself is billed under HCPCS V codes to Medicare Advantage or Medicaid only.</p>

<h2 id="billing-fraud">7. Billing fraud: Medicare&rsquo;s most-targeted category</h2>

<p>Hearing aid billing fraud is among the most actively investigated categories in Medicare Advantage audits. BillKarma&rsquo;s data confirms this pattern&mdash;hearing aid billing fraud is one of Medicare&rsquo;s most targeted fraud categories, with the OIG issuing multiple enforcement actions annually.</p>

<p>Common fraud patterns to watch for on your EOB:</p>

<ul>
    <li><strong>Billing for aids not delivered:</strong> The most prevalent scheme involves providers billing insurance for hearing aids that were never actually dispensed to the patient. If your EOB shows a hearing aid claim for a date you did not receive aids, dispute it immediately and report to your plan&rsquo;s fraud hotline.</li>
    <li><strong>Billing a higher-tier device when a lower tier was dispensed:</strong> A provider bills for a premium binaural digital aid (V5261) but dispenses a basic analog device. Ask for documentation of the exact make, model, and technology level of the aids dispensed at every appointment.</li>
    <li><strong>Billing for replacement aids on accelerated schedules:</strong> Most plans cover aids every two to three years. Billing for replacement aids before the coverage period ends by manipulating the date of service is a documented fraud pattern.</li>
    <li><strong>Unbundling fitting services:</strong> When a plan pays a bundled allowance that includes fitting, programming, and follow-up, separately billing for audiologist services (CPT 92590, 92591) that are already covered by the hearing aid benefit constitutes double-billing.</li>
</ul>

<p>If you suspect fraud, report it to your plan&rsquo;s member services fraud line, the CMS fraud hotline (1-800-HHS-TIPS), or your state Medicaid fraud control unit.</p>

<div class="key-takeaway">
    <strong>Got a hearing aid claim on your Medicare Advantage EOB you don&rsquo;t recognize?</strong> <a href="/scan">Upload your EOB to BillKarma</a> &mdash; we flag hearing aid claims that show signs of common fraud patterns and show you exactly how to dispute them.
</div>

<h2 id="action-steps">8. Action steps to access coverage</h2>

<ol>
    <li><strong>Get a diagnostic audiogram first.</strong> Before shopping for any hearing aid, a professional audiogram tells you the degree and type of your hearing loss, confirms whether OTC aids are appropriate, and provides documentation for insurance claims.</li>
    <li><strong>Call your Medicare Advantage plan before your audiology appointment.</strong> Ask specifically: What is my hearing aid benefit? What is the allowance amount? How often can I receive new aids? Which providers are in the hearing aid network?</li>
    <li><strong>Check Medicaid eligibility if your income qualifies.</strong> If you are dual-eligible (both Medicare and Medicaid), your state Medicaid program may cover the hearing aid costs that Medicare Advantage does not.</li>
    <li><strong>Veterans: contact the VA audiology program.</strong> VA coverage for hearing loss is comprehensive and free for eligible veterans. Tinnitus is one of the most common service-connected disabilities; if you have ringing in your ears from military service, you may be eligible for VA hearing care.</li>
    <li><strong>Compare OTC options if appropriate for your loss level.</strong> If your audiogram confirms mild-to-moderate loss, OTC aids from established brands (Jabra, Sony, Lexie) can deliver meaningful benefit at 70&ndash;90% lower cost than prescription aids.</li>
    <li><strong>Review your Medicare Advantage EOB for every hearing aid claim.</strong> Cross-reference the device billed (HCPCS code and description) against the actual device you received. Keep the product box and documentation from your audiologist.</li>
</ol>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;padding:20px 24px;margin:28px 0;border-radius:6px;">
    <strong>Got a hearing aid bill or EOB that doesn&rsquo;t look right?</strong><br>
    BillKarma reviews hearing aid claims, identifies fraud patterns, and helps you dispute billing errors with your Medicare Advantage plan or audiologist. <a href="/fight-debt"><strong>Start your free review &rarr;</strong></a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much do hearing aids cost in 2026?</h3>
        <p>Traditional prescription hearing aids dispensed by an audiologist cost $2,000 to $7,000 per pair, including professional fitting services. Over-the-counter hearing aids cost $200 to $1,500 per pair and are available without a prescription at pharmacies and online retailers. OTC aids are appropriate only for adults with mild-to-moderate hearing loss.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover hearing aids?</h3>
        <p>Original Medicare (Parts A and B) does not cover hearing aids or the routine hearing exams used to fit them. This is one of the largest coverage gaps in Medicare. However, many Medicare Advantage (Part C) plans offer hearing aid benefits, typically covering one pair every one to three years with an allowance of $500 to $2,500. Call your plan to verify your specific hearing benefit.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between OTC and prescription hearing aids?</h3>
        <p>OTC hearing aids are self-fitting devices intended for adults with perceived mild-to-moderate hearing loss. They do not require a hearing exam or audiologist fitting. Prescription hearing aids are professionally programmed to your specific audiogram results and are appropriate for all levels of hearing loss including moderate-to-severe. Children and anyone with sudden hearing loss should see an audiologist rather than using OTC devices.</p>
    </div>
    <div class="faq-item">
        <h3>What HCPCS codes are used for hearing aid billing?</h3>
        <p>Hearing aids are billed using HCPCS V codes: V5244 (monaural analog), V5247 (monaural digital), V5261 (binaural digital), and related codes for batteries (V5266), earmolds (V5264), and repairs (V5268). These codes appear on Medicare Advantage and Medicaid claims. Audiologist services use CPT codes 92550&ndash;92552 for audiometric exams.</p>
    </div>
    <div class="faq-item">
        <h3>How can I get hearing aids at low or no cost?</h3>
        <p>Several programs help patients with limited income access hearing aids: the Starkey Hear Now foundation, Lions Club International, the Hearing Loss Association of America (HLAA) networks, and the VA for eligible veterans. Medicaid covers hearing aids for adults in 37 states. State vocational rehabilitation programs cover hearing aids for working-age adults whose hearing loss affects employment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.fda.gov/medical-devices/hearing-aids/otc-hearing-aids-what-you-should-know" target="_blank" rel="noopener">FDA: Over-the-Counter Hearing Aids: What You Should Know</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/hearing-eye-dental-care" target="_blank" rel="noopener">CMS Medicare: Hearing, Eye, and Dental Care Coverage</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-and-hearing-coverage/" target="_blank" rel="noopener">KFF: Medicare and Hearing Coverage</a></li>
    <li><a href="https://oig.hhs.gov/fraud/consumer-alerts/hearing-aids/" target="_blank" rel="noopener">HHS Office of Inspector General: Hearing Aid Fraud Alert</a></li>
    <li><a href="https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing" target="_blank" rel="noopener">NIDCD: Quick Statistics About Hearing</a></li>
    <li><a href="https://www.va.gov/health-care/about-va-health-benefits/hearing-aid-and-prosthetic-limb-benefits/" target="_blank" rel="noopener">VA: Hearing Aid and Prosthetic Limb Benefits</a></li>
    <li><a href="https://www.medicaid.gov/medicaid/benefits/index.html" target="_blank" rel="noopener">CMS Medicaid: Benefits Information by State</a></li>
</ul>
""",
})
