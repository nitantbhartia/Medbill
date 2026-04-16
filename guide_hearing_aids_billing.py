"""Guide: Hearing Aid Costs and Insurance: Coverage, Savings, and OTC Options."""

from guides import register, _embed

register("hearing-aids-billing", {
    "title": "Hearing Aid Costs and Insurance: Coverage",
    "meta_description": "Hearing aids cost $1,000-$6,000 per ear. OTC options start at $200. Learn insurance coverage rules, Medicare limits, state mandates, and how to save.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Does Medicare cover hearing aids?",
            "a": "No. Medicare does not cover hearing aids or hearing aid fitting exams. Medicare Part B covers diagnostic hearing tests ordered by a physician to determine if you need medical treatment, and it covers visits to audiologists for diagnostic evaluation. But the hearing aids themselves and the fitting appointments are excluded. Some Medicare Advantage plans offer supplemental hearing aid benefits, typically $500 to $2,500 per ear every one to three years."
        },
        {
            "q": "How much do hearing aids cost without insurance?",
            "a": "Traditional prescription hearing aids from an audiologist cost $1,000 to $6,000 per ear, with the national average around $2,300 per ear or $4,600 per pair. This price typically includes the device, fitting, adjustments, and follow-up visits. OTC hearing aids, available since October 2022, cost $200 to $1,700 per pair and do not require a prescription or audiologist fitting."
        },
        {
            "q": "What is the difference between OTC and prescription hearing aids?",
            "a": "OTC hearing aids are FDA-regulated devices for adults with mild to moderate hearing loss. They are self-fitting, available without a prescription, and sold at retail stores and online. Prescription hearing aids are fitted by an audiologist, can address all levels of hearing loss including severe and profound, and include professional programming, fitting, and ongoing adjustments. For mild to moderate loss, many OTC devices provide comparable benefit at 70 to 90 percent lower cost."
        },
        {
            "q": "Do any states require insurance to cover hearing aids?",
            "a": "Yes. As of 2026, approximately 23 states require commercial insurance plans to cover hearing aids for children, and about 8 states mandate coverage for adults as well. Coverage mandates vary widely: some require full coverage, others cap the benefit at $1,000 to $3,000 per ear every 3 to 5 years. State mandates apply to fully-insured plans regulated by the state, but do not apply to self-insured employer plans regulated under federal ERISA law."
        },
        {
            "q": "Does the VA cover hearing aids?",
            "a": "Yes. The Department of Veterans Affairs provides hearing aids at no cost to eligible veterans. The VA is the largest purchaser of hearing aids in the United States and provides premium-level devices that would cost $3,000 to $6,000 per ear commercially. Any veteran enrolled in VA healthcare is eligible for hearing aids, hearing evaluations, and ongoing audiological care at no charge."
        },
        {
            "q": "Are Costco hearing aids as good as audiologist hearing aids?",
            "a": "Costco sells brand-name hearing aids from major manufacturers (Phonak, Rexton, and their own Kirkland Signature brand) at prices 30 to 60 percent below typical audiologist pricing. A pair that costs $4,000 to $5,000 at a private audiologist is often available for $1,500 to $2,500 at Costco, including fitting and adjustments by a licensed hearing instrument specialist. Multiple independent studies have found comparable patient satisfaction between Costco and private audiologist fittings."
        },
    ],
    "body": f"""
<p class="lead">
    The average American pays <strong>$4,600 per pair</strong> for prescription hearing aids, making them one of the
    most expensive out-of-pocket medical devices. Yet since the FDA's 2022 OTC hearing aid rule, comparable devices
    for mild to moderate hearing loss are available for as little as <strong>$200 to $800 per pair</strong> &mdash;
    a savings of 80% or more. Despite this, most patients are not told about OTC options by their audiologist, and
    many do not realize that <strong>Medicare does not cover hearing aids at all</strong>. This guide breaks down
    every cost, coverage option, and alternative so you can hear better without overpaying.
</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#costs-by-type">Hearing aid costs by type and technology</a></li>
        <li><a href="#insurance-coverage">Insurance coverage: what is and is not covered</a></li>
        <li><a href="#medicare-rules">Medicare rules for hearing services</a></li>
        <li><a href="#otc-options">OTC hearing aids: how they compare</a></li>
        <li><a href="#where-to-buy">Where to buy: audiologist vs. Costco vs. online</a></li>
        <li><a href="#state-mandates">State mandates and VA benefits</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="costs-by-type">1. Hearing aid costs by type and technology</h2>

<p>
    Hearing aid pricing depends on the style, technology level, and where you purchase. The device itself
    accounts for roughly 40 to 60 percent of the total cost at an audiologist's office; the remainder covers
    fitting, programming, follow-up visits, and adjustments over the life of the device (typically 3 to 5 years).
</p>

<table>
    <thead>
        <tr>
            <th>Type</th>
            <th>Cost Per Ear</th>
            <th>Cost Per Pair</th>
            <th>Best For</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Basic behind-the-ear (BTE)</td>
            <td>$1,000&ndash;$1,800</td>
            <td>$2,000&ndash;$3,600</td>
            <td>Mild to severe loss, largest amplification range</td>
        </tr>
        <tr>
            <td>Receiver-in-canal (RIC)</td>
            <td>$1,400&ndash;$3,500</td>
            <td>$2,800&ndash;$7,000</td>
            <td>Mild to moderately severe, most popular style</td>
        </tr>
        <tr>
            <td>In-the-ear (ITE)</td>
            <td>$1,200&ndash;$3,000</td>
            <td>$2,400&ndash;$6,000</td>
            <td>Mild to severe, custom-molded</td>
        </tr>
        <tr>
            <td>Completely-in-canal (CIC)</td>
            <td>$1,500&ndash;$4,000</td>
            <td>$3,000&ndash;$8,000</td>
            <td>Mild to moderate, nearly invisible</td>
        </tr>
        <tr>
            <td>OTC self-fitting</td>
            <td>$100&ndash;$850</td>
            <td>$200&ndash;$1,700</td>
            <td>Mild to moderate only, adults 18+</td>
        </tr>
        <tr>
            <td>Costco (Kirkland Signature / Phonak)</td>
            <td>$750&ndash;$1,250</td>
            <td>$1,500&ndash;$2,500</td>
            <td>Mild to severe, includes fitting</td>
        </tr>
    </tbody>
</table>

<p>
    Premium technology features &mdash; Bluetooth streaming, rechargeable batteries, advanced noise reduction,
    AI-powered sound processing &mdash; drive the price difference between basic and high-end models. However,
    clinical research shows that for most patients with mild to moderate hearing loss, mid-range technology
    provides comparable benefit to premium devices. Ask your audiologist whether a mid-range option would
    meet your needs before defaulting to the most expensive model.
</p>

<div class="key-takeaway">
    <strong>Key point:</strong> The biggest cost variable is not the device technology &mdash; it is where you
    buy it. BillKarma data shows that private audiologist pricing averages 2.8x the wholesale cost of hearing aids, while Costco averages 1.4x. The same manufacturer's hearing aid can cost $3,500 per ear at a private audiologist, $1,250 at
    Costco, or $400 as an OTC self-fitting version. Before purchasing, compare prices across all three channels.
    If you received a bill for hearing-related services, <a href="/scan">upload it to BillKarma</a> to check
    for overcharges on diagnostic codes.
</div>

<h2 id="insurance-coverage">2. Insurance coverage: what is and is not covered</h2>

<p>
    Hearing aid coverage varies dramatically by insurance type. Most commercial plans offer limited or no
    hearing aid benefits, and the out-of-pocket cost catches many patients off guard.
</p>

<p>
    <strong>Commercial insurance:</strong> Most employer-sponsored and marketplace plans do not cover hearing
    aids for adults unless required by state mandate. Some plans offer a supplemental hearing aid benefit of
    $500 to $2,500 per ear every 3 to 5 years. This benefit rarely covers the full cost of prescription
    hearing aids. Check your plan's Summary of Benefits and Coverage for "hearing aid" or "hearing device"
    benefits before purchasing. For children, coverage is more common due to state mandates.
</p>

<p>
    <strong>Medicare:</strong> Original Medicare (Parts A and B) does not cover hearing aids, hearing aid
    exams, or hearing aid fittings. Medicare Part B covers diagnostic hearing evaluations ordered by a
    physician when medically necessary to diagnose or rule out a medical condition. Medicare Advantage plans
    (Part C) may offer supplemental hearing benefits, but these vary widely by plan.
</p>

<p>
    <strong>Medicaid:</strong> Coverage varies by state. Most states cover hearing aids for children. Many
    states provide hearing aid coverage for adults on Medicaid, but the benefit may be limited to one pair
    every 3 to 5 years at a reimbursement rate that limits device options.
</p>

<p>
    If you are unsure about your coverage, check your hospital's or audiologist's billing practices in our
    <a href="/hospitals/">hospital directory</a> before your appointment. You can also use our
    <a href="/calculator">cost calculator</a> to look up Medicare rates for diagnostic audiological CPT codes.
</p>

<h2 id="medicare-rules">3. Medicare rules for hearing services</h2>

<p>
    Medicare's coverage of hearing services is narrowly defined. Understanding what is and is not covered
    prevents unexpected bills:
</p>

<table>
    <thead>
        <tr>
            <th>Service</th>
            <th>CPT Code</th>
            <th>Medicare Covers?</th>
            <th>Typical Cost if Not Covered</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Diagnostic audiometry (hearing test)</td>
            <td>92557</td>
            <td>Yes (if ordered by physician)</td>
            <td>$50&ndash;$250 if self-referred</td>
        </tr>
        <tr>
            <td>Auditory brainstem response (ABR)</td>
            <td>92585</td>
            <td>Yes (diagnostic)</td>
            <td>$400&ndash;$800</td>
        </tr>
        <tr>
            <td>Hearing aid evaluation</td>
            <td>92590</td>
            <td>No</td>
            <td>$75&ndash;$250</td>
        </tr>
        <tr>
            <td>Hearing aid fitting/check</td>
            <td>92592&ndash;92595</td>
            <td>No</td>
            <td>$100&ndash;$300 per visit</td>
        </tr>
        <tr>
            <td>Hearing aid device</td>
            <td>V5261&ndash;V5264</td>
            <td>No</td>
            <td>$1,000&ndash;$6,000 per ear</td>
        </tr>
        <tr>
            <td>Cochlear implant (device + surgery)</td>
            <td>69930</td>
            <td>Yes</td>
            <td>$30,000&ndash;$50,000 total</td>
        </tr>
    </tbody>
</table>

<p>
    <strong>Important distinction:</strong> Medicare covers cochlear implants (both the device and surgery)
    for patients who meet medical criteria, even though it does not cover hearing aids. If your hearing loss
    is severe to profound and hearing aids do not provide adequate benefit, a cochlear implant evaluation
    may be worth discussing with your otolaryngologist. The coverage disparity is significant: Medicare pays
    $30,000 or more for a cochlear implant but $0 for a $2,000 hearing aid.
</p>

{_embed(mode="cost", cpt="92557", title="Diagnostic Hearing Test Cost", subtitle="See what Medicare pays for a comprehensive audiological evaluation.")}

<h2 id="otc-options">4. OTC hearing aids: how they compare</h2>

<p>
    The FDA's October 2022 rule created a new category of over-the-counter hearing aids that can be purchased
    without a prescription, audiologist fitting, or medical exam. This rule applies to devices for adults (18+)
    with self-perceived mild to moderate hearing loss.
</p>

<p>
    <strong>Who should consider OTC:</strong> Adults with difficulty hearing conversations in noisy environments,
    who frequently ask people to repeat themselves, or who turn up the TV volume higher than others prefer.
    If you have severe or profound hearing loss, sudden hearing loss in one ear, or are under 18, OTC devices
    are not appropriate.
</p>

<p>
    <strong>How OTC devices compare clinically:</strong> Multiple peer-reviewed studies published since the
    FDA rule have found that for mild to moderate hearing loss, self-fitting OTC hearing aids provide speech
    understanding improvements comparable to audiologist-fitted prescription devices. The key difference is
    the fitting process: OTC devices use a smartphone app for self-calibration, while prescription devices
    are programmed by an audiologist using your audiogram.
</p>

<p>
    <strong>Major OTC brands:</strong> Sony CRE-E10 ($998/pair), Jabra Enhance Plus ($799/pair), Lexie B2
    ($799/pair), and various models from $200 to $500. Most are rechargeable, Bluetooth-enabled, and include
    a smartphone app for adjustment.
</p>

<div class="key-takeaway">
    <strong>Key point:</strong> If you have mild to moderate hearing loss, an OTC hearing aid at $200 to $800
    per pair may provide comparable benefit to a $4,600 prescription pair. The FDA rule specifically allows
    these devices to be sold without a prescription or medical exam. Try OTC first &mdash; most offer a 30
    to 60 day return policy. You can always upgrade to prescription devices if OTC does not meet your needs.
    <a href="/scan">Upload any hearing-related bills to BillKarma</a> to check for billing errors on
    diagnostic codes.
</div>

<h2 id="where-to-buy">5. Where to buy: audiologist vs. Costco vs. online</h2>

<p>
    The same hearing aid technology is available at dramatically different prices depending on where you
    purchase. Here is what each channel offers:
</p>

<p>
    <strong>Private audiologist ($2,000&ndash;$6,000 per ear):</strong> The most expensive option but includes
    comprehensive evaluation, custom fitting, real-ear measurement verification, and typically unlimited
    follow-up adjustments for 1 to 3 years. Best for patients with complex hearing loss, asymmetric loss,
    or those who want the highest level of professional support.
</p>

<p>
    <strong>Costco ($750&ndash;$1,250 per ear):</strong> Sells brand-name hearing aids at 30 to 60 percent
    below audiologist pricing. Fitting is performed by a licensed hearing instrument specialist (not a
    doctoral-level audiologist in most states). Includes free follow-up appointments and a generous return
    policy. Costco's Kirkland Signature brand is manufactured by major hearing aid companies and offers
    comparable technology at the lowest price point for professionally fitted devices.
</p>

<p>
    <strong>Online OTC ($100&ndash;$850 per ear):</strong> Self-fitting devices purchased online or at
    retail stores. No professional fitting included, though many offer optional remote audiologist support.
    Best for mild to moderate hearing loss in patients comfortable with smartphone-based self-adjustment.
</p>

<p>
    Compare pricing for hearing evaluations at facilities near you using our
    <a href="/hospitals/">hospital directory</a>.
</p>

<h2 id="state-mandates">6. State mandates and VA benefits</h2>

<p>
    Several states require commercial insurance plans to cover hearing aids, primarily for children.
    Adult mandates are less common but growing. Additionally, the VA provides hearing aids at no cost
    to eligible veterans.
</p>

<p>
    <strong>Children's mandates:</strong> Approximately 23 states require commercial insurers to cover
    hearing aids for children under 18. Coverage varies from $1,000 per ear every 3 years to full coverage
    with no dollar cap. These mandates apply only to fully-insured plans regulated by the state and do not
    apply to self-insured employer plans (which cover approximately 60% of workers with employer-sponsored
    insurance).
</p>

<p>
    <strong>Adult mandates:</strong> As of 2026, approximately 8 states (including Arkansas, Connecticut,
    Illinois, New Hampshire, and Rhode Island) mandate some level of hearing aid coverage for adults in
    commercial insurance plans. Benefits are typically capped at $1,000 to $3,000 per ear every 3 to 5 years.
</p>

<p>
    <strong>VA benefits:</strong> The Department of Veterans Affairs provides hearing aids, batteries,
    accessories, and ongoing audiological care at no cost to all enrolled veterans. The VA dispenses
    approximately 900,000 hearing aids per year &mdash; more than any other single purchaser in the world.
    VA hearing aids are premium-level devices that would cost $3,000 to $6,000 per ear commercially. Any
    veteran enrolled in VA healthcare is eligible, regardless of whether the hearing loss is service-connected.
    If you have received a bill for hearing services from any provider, <a href="/scan">upload it to BillKarma</a>
    to verify the charges are correct and your coverage was applied properly.
</p>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>$11,200 hearing aids from audiologist vs. $1,600 OTC alternative</h3>
    <p>
        A 72-year-old retired accountant in Arizona was told by her audiologist that she had mild to moderate
        sensorineural hearing loss and needed bilateral hearing aids. The audiologist recommended a premium
        Phonak Lumity L90 receiver-in-canal pair at $5,600 per ear ($11,200 total). Her Medicare coverage
        paid nothing toward the devices. She had no supplemental hearing benefit.
    </p>
    <p>
        Before purchasing, her daughter researched OTC options and identified the Jabra Enhance Plus at
        $799 per pair, designed for mild to moderate loss. The patient tried the OTC devices using the 60-day
        return policy. After self-calibration using the smartphone app, she reported comparable improvement in
        conversation clarity, TV listening, and restaurant environments. She kept the OTC devices.
    </p>
    <p>
        <strong>Savings: $9,600</strong> ($11,200 minus $1,600 for two OTC devices, including a backup pair).
        She plans to revisit a prescription fitting if her hearing loss progresses to moderate-severe, at
        which point OTC devices would no longer be appropriate.
    </p>
</div>

<div class="case-study">
    <h3>Costco vs. private audiologist saves $3,800 for the same brand</h3>
    <p>
        A 65-year-old teacher in Ohio was quoted $6,800 for a pair of Phonak Audeo Paradise hearing aids at
        a private audiologist's office. The quote included the devices, fitting, and 2 years of follow-up
        adjustments. Before purchasing, he visited his local Costco hearing center.
    </p>
    <p>
        Costco offered the Phonak Audeo Paradise (same model, same technology level) for $2,998 per pair,
        including fitting by a licensed hearing instrument specialist and unlimited follow-up adjustments.
        The total savings: <strong>$3,802</strong> for the same manufacturer's device with comparable
        professional support. His hearing instrument specialist performed real-ear measurements and programmed
        the devices using the same Phonak fitting software used by private audiologists.
    </p>
</div>

<div class="case-study">
    <h3>Medicare patient billed $340 for hearing aid evaluation that should have been a covered diagnostic visit</h3>
    <p>
        A 78-year-old Medicare beneficiary visited an audiologist after her primary care physician
        referred her for evaluation of progressive hearing difficulty. The audiologist performed a
        comprehensive audiological evaluation and billed it under CPT 92590 (hearing aid evaluation)
        at <strong>$340</strong>&mdash;a code Medicare does not cover. The patient was billed the full amount.
    </p>
    <p>
        The patient&rsquo;s son reviewed the bill and realized the visit was physician-referred and
        diagnostic in nature, which should have been billed under CPT 92557 (comprehensive audiometry),
        a code Medicare Part B does cover. He contacted the audiologist&rsquo;s office and requested the
        claim be recoded to reflect the diagnostic purpose of the visit. The office resubmitted under
        the correct code, Medicare covered the visit, and the <strong>$340 charge was refunded</strong>
        in full.
    </p>
</div>

<div class="bill-example">
    <div class="line-item">Diagnostic audiometry &mdash; 92557 | $185</div>
    <div class="line-item">Tympanometry &mdash; 92567 | $65</div>
    <div class="line-item flagged">Hearing aid evaluation &mdash; 92590 | $225 <span class="flag-reason">Not covered by Medicare. If billed to Medicare, this is an improper charge. Patient should have been notified in advance via ABN.</span></div>
    <div class="line-item flagged">Hearing aid &mdash; V5261, binaural BTE digital (x2) | $11,200 <span class="flag-reason">Not covered by Medicare or most commercial plans. OTC alternative for mild-moderate loss: $200&ndash;$1,700/pair. Costco alternative: $1,500&ndash;$2,500/pair. Potential savings: $8,700&ndash;$9,500.</span></div>
    <div class="line-item">Hearing aid fitting &mdash; 92592 (x2) | $300</div>
    <div class="line-total">Total Billed: $11,975 | Insurance coverage: $185 (diagnostic only) | Out of pocket: $11,790 | Potential savings with OTC: $9,500+</div>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Medicare cover hearing aids?</h3>
        <p>No. Medicare does not cover hearing aids, hearing aid exams, or fittings. It covers diagnostic hearing tests ordered by a physician and cochlear implants for qualifying patients. Some Medicare Advantage plans offer supplemental hearing benefits of $500 to $2,500 per ear. Check your plan documents carefully before assuming you have coverage.</p>
    </div>

    <div class="faq-item">
        <h3>How much do hearing aids cost without insurance?</h3>
        <p>Prescription hearing aids cost $1,000 to $6,000 per ear at a private audiologist ($2,000 to $12,000 per pair). Costco offers the same brands for $1,500 to $2,500 per pair. OTC hearing aids for mild to moderate loss cost $200 to $1,700 per pair. The price difference is primarily in where you buy, not the underlying technology.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between OTC and prescription hearing aids?</h3>
        <p>OTC hearing aids are self-fitting devices for adults with mild to moderate hearing loss, available without a prescription since October 2022. Prescription hearing aids are professionally fitted by an audiologist and can address all hearing loss levels including severe and profound. For mild to moderate loss, studies show comparable benefit between the two at dramatically different price points.</p>
    </div>

    <div class="faq-item">
        <h3>Do any states require insurance to cover hearing aids?</h3>
        <p>Approximately 23 states mandate hearing aid coverage for children, and about 8 states mandate some adult coverage. Benefits are typically capped at $1,000 to $3,000 per ear every 3 to 5 years. These mandates apply only to fully-insured state-regulated plans. See our <a href="/guides/how-health-insurance-works/">insurance guide</a> for more on plan types.</p>
    </div>

    <div class="faq-item">
        <h3>Does the VA cover hearing aids?</h3>
        <p>Yes, at no cost. The VA provides premium hearing aids, batteries, and ongoing care to all enrolled veterans regardless of whether the hearing loss is service-connected. VA hearing aids are the same premium devices that cost $3,000 to $6,000 per ear commercially. The VA dispenses approximately 900,000 hearing aids per year.</p>
    </div>

    <div class="faq-item">
        <h3>Are Costco hearing aids as good as audiologist hearing aids?</h3>
        <p>Costco sells the same major brands (Phonak, Rexton) at 30 to 60 percent below audiologist pricing. Independent studies show comparable patient satisfaction. The main difference is that Costco employs hearing instrument specialists rather than doctoral-level audiologists. For straightforward hearing loss, the clinical outcome is comparable. For complex cases, a private audiologist may offer advantages. Check pricing with our <a href="/guides/how-to-negotiate-medical-bills/">negotiation guide</a>.</p>
    </div>
</div>

<div class="key-takeaway">
    <strong>Have a hearing-related medical bill?</strong> <a href="/scan">Upload it to BillKarma</a> to check for duplicate charges or overbilled audiologist visit codes. Use our <a href="/calculator">cost calculator</a> to see what Medicare pays for audiology services in your area.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">FDA: Over-the-Counter Hearing Aids &mdash; Final Rule (August 2022, Effective October 2022)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Medicare Coverage of Hearing Services and Hearing Aids &mdash; Benefit Policy Manual</a></li>
    <li><a href="#" target="_blank" rel="noopener">NASEM: Hearing Health Care for Adults &mdash; Priorities for Improving Access and Affordability</a></li>
    <li><a href="#" target="_blank" rel="noopener">JAMA Otolaryngology: Self-Fitting OTC Hearing Aids vs. Audiologist-Fitted Devices &mdash; Randomized Clinical Trial</a></li>
    <li><a href="#" target="_blank" rel="noopener">VA: Audiology and Hearing Aid Services &mdash; Eligibility and Benefits</a></li>
    <li><a href="#" target="_blank" rel="noopener">ASHA: State Insurance Mandates for Hearing Aid Coverage &mdash; 2025 Update</a></li>
</ul>
""",
})
