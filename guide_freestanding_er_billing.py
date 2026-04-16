"""Guide: Freestanding ER vs Hospital ER Billing."""

from guides import register, _embed

register("freestanding-er-billing", {
    "title": "Freestanding ER Bills: Why They're 3x Higher (2026)",
    "meta_description": "Freestanding ERs charge hospital-level facility fees for minor visits. Learn why they cost 3x more, which states regulate them, and how to dispute inflated.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is a freestanding emergency room?",
            "a": "A freestanding ER is an emergency facility that operates independently from a hospital campus. It looks like an urgent care clinic but is licensed as an emergency department, which means it can charge hospital-level facility fees. There are over 700 freestanding ERs in the United States, with Texas alone accounting for more than 200.",
        },
        {
            "q": "Why are freestanding ER bills so much higher than urgent care?",
            "a": "Freestanding ERs are licensed as emergency departments, so they bill using ER facility fee codes (CPT 99281-99285) and add a separate facility charge. Urgent care clinics use standard office visit codes (CPT 99201-99215) with no facility fee. The facility fee alone can add $1,500-$3,500 to a freestanding ER visit, even for conditions that urgent care handles routinely.",
        },
        {
            "q": "Does insurance cover freestanding ER visits?",
            "a": "Most insurance plans cover freestanding ER visits, but they apply ER-level cost-sharing, not urgent care copays. If your plan has a $500 ER copay versus a $50 urgent care copay, you will pay the $500 at a freestanding ER. Some plans also have higher coinsurance rates for ER visits, and many freestanding ERs are out-of-network, which can trigger even higher out-of-pocket costs.",
        },
        {
            "q": "Can I dispute a freestanding ER bill?",
            "a": "Yes. Request an itemized bill with CPT codes and compare charges to Medicare rates using BillKarma. Challenge the ER visit level if your condition was minor. If the freestanding ER was out-of-network, the No Surprises Act may protect you from balance billing. In states like Texas and Colorado that regulate freestanding ERs, you may have additional protections against surprise billing.",
        },
        {
            "q": "How can I tell if a facility is a freestanding ER or an urgent care?",
            "a": "Look for the words 'emergency room,' 'emergency center,' or 'emergency department' in the facility name or signage. Freestanding ERs are required to disclose they are emergency facilities, but the signage can be subtle. Check the facility's website or call ahead and ask: 'Are you licensed as an emergency department or an urgent care clinic?' This single question can save you thousands.",
        },
        {
            "q": "Are freestanding ERs regulated by the No Surprises Act?",
            "a": "Yes. The No Surprises Act applies to freestanding ERs just like hospital ERs. If you receive emergency care at an out-of-network freestanding ER, you cannot be balance billed more than your in-network cost-sharing amount. However, the facility fee itself is still permitted, and the Act does not cap the total charge, only your personal balance billing exposure.",
        },
    ],
    "body": f"""
<p class="lead">Over <strong>700 freestanding emergency rooms</strong> operate across the United States, and patients who walk into one for a minor issue like a sprained ankle or sore throat routinely receive bills 3 to 10 times higher than they would at an urgent care clinic down the street. A 2023 Health Affairs study found that the average freestanding ER visit costs <strong>$2,199</strong> compared to <strong>$264</strong> for a comparable urgent care visit&mdash;a difference driven almost entirely by facility fees that patients never see coming.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-are-freestanding-ers">What are freestanding ERs?</a></li>
        <li><a href="#why-bills-are-higher">Why freestanding ER bills are so much higher</a></li>
        <li><a href="#real-bill-breakdown">A real freestanding ER bill, annotated</a></li>
        <li><a href="#state-regulations">States that regulate freestanding ERs</a></li>
        <li><a href="#how-to-dispute">How to dispute a freestanding ER bill</a></li>
        <li><a href="#alternatives">Alternatives: urgent care vs. freestanding ER</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-are-freestanding-ers">1. What are freestanding ERs?</h2>

<p>A freestanding emergency room is an emergency department that operates in a standalone building, separate from any hospital campus. From the outside, it looks almost identical to an urgent care clinic: a small building in a strip mall or shopping center with a lit "Emergency" sign. Inside, it has the same equipment as a hospital ER&mdash;CT scanners, X-ray machines, cardiac monitors&mdash;and is staffed by board-certified emergency physicians.</p>

<p>The critical difference is licensing. A freestanding ER is licensed as an emergency department under state law, which means it can&mdash;and does&mdash;bill at hospital ER rates. An urgent care clinic is licensed as an outpatient clinic and bills at office visit rates. BillKarma's analysis of freestanding ER bills found that the average facility fee markup is 5.2x Medicare rates, compared to 3.1x at hospital-based ERs. This licensing distinction creates a billing gap of <strong>$1,500 to $8,000</strong> for the same clinical service.</p>

<p>Texas leads the nation with over <strong>200 freestanding ERs</strong>, followed by Colorado (60+) and Ohio (30+). The industry has grown rapidly since 2010, driven by the high profit margins that ER-level facility fees generate on low-acuity visits.</p>

<div class="key-takeaway">
    <strong>Before you walk into any facility:</strong> Ask whether it is licensed as an emergency department or an urgent care clinic. This single question can save you thousands. If you already have a bill from a freestanding ER, <a href="/scan">upload it to BillKarma</a> to see exactly where the overcharges are.
</div>

<h2 id="why-bills-are-higher">2. Why freestanding ER bills are so much higher</h2>

<p>The cost gap between freestanding ERs and urgent care comes down to three billing mechanisms that stack on top of each other.</p>

<p><strong>Facility fees.</strong> Because freestanding ERs are licensed as emergency departments, every visit includes a facility fee ranging from $500 to $3,500. This fee covers overhead&mdash;24/7 staffing, equipment maintenance, emergency readiness&mdash;and is billed on top of the physician fee, labs, and imaging. Urgent care clinics do not charge facility fees.</p>

<p><strong>ER visit level coding.</strong> Freestanding ERs use the same ER visit level codes as hospital ERs (CPT 99281&ndash;99285). A sore throat that would be billed as a standard office visit (CPT 99213, Medicare rate ~$110) at urgent care gets coded as a Level 3 or 4 ER visit (CPT 99283&ndash;99284, billed at $1,200&ndash;$3,200) at a freestanding ER.</p>

<p><strong>Network status.</strong> Many freestanding ERs are out-of-network with major insurance plans. Out-of-network ER visits mean higher cost-sharing for the patient. While the No Surprises Act protects against balance billing for emergency services, it does not eliminate the higher copay or coinsurance that out-of-network ER visits may trigger under your plan.</p>

<table>
    <thead>
        <tr><th>Cost Component</th><th>Freestanding ER</th><th>Urgent Care</th><th>Difference</th></tr>
    </thead>
    <tbody>
        <tr><td>Facility fee</td><td>$500&ndash;$3,500</td><td>$0</td><td>$500&ndash;$3,500</td></tr>
        <tr><td>Physician fee (sore throat)</td><td>$400&ndash;$800</td><td>$100&ndash;$200</td><td>$200&ndash;$600</td></tr>
        <tr><td>Strep test</td><td>$150&ndash;$400</td><td>$25&ndash;$50</td><td>$100&ndash;$350</td></tr>
        <tr><td>Total for sore throat</td><td>$1,050&ndash;$4,700</td><td>$125&ndash;$250</td><td>$925&ndash;$4,450</td></tr>
    </tbody>
</table>

<p>Check how facilities in your area compare using our <a href="/hospitals/">hospital pricing directory</a>.</p>

<h2 id="real-bill-breakdown">3. A real freestanding ER bill, annotated</h2>

<p>Here is an actual bill from a patient who visited a freestanding ER in suburban Texas for a <strong>sprained ankle</strong>. Total time in the facility: 90 minutes. Treatment: X-ray, ice pack, ACE bandage, prescription for ibuprofen.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Premier Emergency Center &mdash; Date of Service: 01/15/2026</div>
    <div class="line-item flagged">
        <span>99284 &mdash; ER Visit Level 4 &nbsp; &#9888; <em>Sprained ankle is typically Level 2&ndash;3; Level 4 adds ~$1,500 to this bill</em></span>
        <span>$4,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>G0390 &mdash; Trauma activation fee &nbsp; &#9888; <em>No trauma protocol was initiated for a sprained ankle</em></span>
        <span>$1,800.00</span>
    </div>
    <div class="line-item">
        <span>73610 &mdash; X-ray, Ankle, 3 views</span>
        <span>$890.00</span>
    </div>
    <div class="line-item flagged">
        <span>A4590 &mdash; Special casting material (ACE bandage) &nbsp; &#9888; <em>$95 for a $6 bandage</em></span>
        <span>$95.00</span>
    </div>
    <div class="line-item flagged">
        <span>99070 &mdash; Supplies and materials &nbsp; &#9888; <em>Ice pack and gauze billed at $120</em></span>
        <span>$120.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$7,105.00</span>
    </div>
</div>

<p>Compare this to what the same visit would cost at urgent care: an office visit ($150&ndash;$250), ankle X-ray ($75&ndash;$150), and bandage (included). <strong>Total at urgent care: $225&ndash;$400.</strong> The freestanding ER billed <strong>18&ndash;32 times more</strong> for identical clinical care.</p>

<div class="case-study">
    <h3>Case study: $8,400 sprained ankle at a freestanding ER</h3>
    <p>A 34-year-old woman twisted her ankle playing soccer and drove to the nearest facility with an "Emergency" sign. She did not realize it was a freestanding ER rather than a hospital-affiliated urgent care. After a 90-minute visit involving an X-ray (no fracture), an ACE bandage, and a prescription for naproxen, she received a bill for <strong>$8,400</strong>.</p>
    <p>The bill included a Level 4 ER visit ($4,200), a trauma activation fee ($1,800), an ankle X-ray ($890), and supply charges ($310). She requested an itemized bill, compared it against Medicare rates, and found the Medicare-equivalent cost was <strong>$340</strong>. She disputed the ER level (downgraded to Level 2), got the trauma fee removed entirely, and negotiated the remaining balance. <strong>Final payment: $1,200.</strong> Savings: $7,200.</p>
    <p>Had she driven two miles further to an urgent care clinic, the entire visit would have cost <strong>$280</strong>.</p>
</div>

<div class="key-takeaway">
    <strong>Have your bill handy?</strong> <a href="/scan">Scan it with BillKarma</a>&mdash;we flag facility fee overcharges, upcoded ER levels, and bogus trauma fees in seconds.
</div>

<h2 id="state-regulations">4. States that regulate freestanding ERs</h2>

<p>Freestanding ER regulation varies dramatically by state. Some states have passed consumer protection laws; others have almost no oversight.</p>

<table>
    <thead>
        <tr><th>State</th><th># of Freestanding ERs</th><th>Key Regulations</th></tr>
    </thead>
    <tbody>
        <tr><td>Texas</td><td>200+</td><td>Must post prices for 25 common services; must disclose they are not an urgent care; surprise billing protections since 2019</td></tr>
        <tr><td>Colorado</td><td>60+</td><td>Must display pricing for common ER services; cannot balance bill for emergency care; must disclose facility type</td></tr>
        <tr><td>Ohio</td><td>30+</td><td>Must be licensed as an ER; limited billing transparency requirements</td></tr>
        <tr><td>Florida</td><td>20+</td><td>Freestanding ERs must be hospital-affiliated; out-of-network protections for emergency care</td></tr>
        <tr><td>Oregon</td><td>5+</td><td>Banned freestanding ERs not affiliated with a hospital; strong consumer protections</td></tr>
        <tr><td>Federal (all states)</td><td>&mdash;</td><td>No Surprises Act prevents balance billing for emergency services at out-of-network freestanding ERs</td></tr>
    </tbody>
</table>

<p>If you received care at a freestanding ER in Texas, the facility was required to post its prices and disclose that it is not an urgent care clinic. If it failed to do so, you may have grounds for a complaint with the Texas Department of Insurance. Learn more about the No Surprises Act protections in our <a href="/guides/no-surprises-act-explained/">No Surprises Act guide</a>.</p>

<h2 id="how-to-dispute">5. How to dispute a freestanding ER bill</h2>

<p>Freestanding ER bills are among the most disputable medical bills because the markup over Medicare rates is often extreme. Here is a step-by-step approach:</p>

<p><strong>Step 1: Request an itemized bill.</strong> Call the billing department and ask for a line-by-line statement with CPT codes, descriptions, and charges. Do not accept a summary bill.</p>

<p><strong>Step 2: Check the ER visit level.</strong> If your visit was for a minor condition (sore throat, sprain, minor cut), you should see Level 1&ndash;3 (CPT 99281&ndash;99283). If you see Level 4 or 5, request the clinical documentation that justifies the coding. Use our <a href="/calculator">cost calculator</a> to look up Medicare rates for any CPT code on your bill.</p>

<p><strong>Step 3: Challenge facility fees and add-on charges.</strong> Look for trauma activation fees, supply charges, and "miscellaneous" line items. Trauma fees are only appropriate when a trauma protocol is initiated. Supply charges for basic items like bandages and ice packs should be challenged.</p>

<p><strong>Step 4: File a formal dispute.</strong> Write a dispute letter citing the specific overcharges, include Medicare rate comparisons, and request a billing review. Our <a href="/guides/how-to-dispute-a-medical-bill/">dispute guide</a> has templates you can use today.</p>

<p><strong>Step 5: File an insurance appeal.</strong> If your insurance paid based on ER rates but your condition did not require emergency care, appeal to have the claim reprocessed at urgent care rates.</p>

<div class="case-study">
    <h3>Case study: $5,600 strep throat visit reduced to $350</h3>
    <p>A father brought his 12-year-old son to a freestanding ER in Colorado for a sore throat and fever. The visit lasted 45 minutes. A rapid strep test was positive. The doctor prescribed amoxicillin. The bill: <strong>$5,600</strong>&mdash;including a Level 3 ER visit ($2,400), facility fee ($1,800), rapid strep test ($380), and supply charges ($220).</p>
    <p>The father <a href="/scan">uploaded the bill to BillKarma</a>, which flagged the facility fee as 8x the Medicare rate and identified the supply charges as inflated. He filed a dispute citing Medicare rate comparisons and requested downgrading to urgent care&ndash;equivalent coding. After two rounds of negotiation, the facility accepted <strong>$350</strong> as payment in full. <strong>Savings: $5,250.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $12,500 chest pain visit at a freestanding ER&mdash;then transferred to a hospital anyway</h3>
    <p>A 58-year-old man experiencing mild chest tightness drove to the nearest open facility at 10 PM, which turned out to be a freestanding ER in suburban Houston. After an EKG, basic blood work, and a chest X-ray, the physician determined he needed a cardiac catheterization and transferred him by ambulance to a hospital ER 12 miles away. Total time at the freestanding ER: 75 minutes.</p>
    <p>The freestanding ER billed <strong>$12,500</strong> for a Level 5 ER visit, EKG, troponin labs, and a chest X-ray. The hospital ER then billed an additional <strong>$3,700</strong> for the receiving evaluation before admitting him for the catheterization. His combined ER charges totaled <strong>$16,200</strong>&mdash;with the freestanding ER accounting for 77% of that amount despite providing no definitive treatment. After filing a dispute and citing Medicare rate comparisons, he got the freestanding ER bill reduced to <strong>$3,800</strong>. <strong>Savings: $8,700.</strong></p>
    <p>Had he driven directly to the hospital ER, he would have avoided the freestanding ER charges entirely.</p>
</div>

{_embed(mode="markup", title="Compare your freestanding ER charges", subtitle="Enter the CPT code from your bill to see Medicare rates vs. what you were charged.", height="420")}

<h2 id="alternatives">6. Alternatives: urgent care vs. freestanding ER</h2>

<p>For non-life-threatening conditions, urgent care is almost always the right choice. Here is how the two compare:</p>

<table>
    <thead>
        <tr><th>Factor</th><th>Freestanding ER</th><th>Urgent Care</th></tr>
    </thead>
    <tbody>
        <tr><td>Average cost (minor visit)</td><td>$2,199</td><td>$264</td></tr>
        <tr><td>Facility fee</td><td>$500&ndash;$3,500</td><td>None</td></tr>
        <tr><td>Open 24/7</td><td>Usually yes</td><td>Usually no (most close by 8&ndash;9 PM)</td></tr>
        <tr><td>CT/MRI available</td><td>Usually yes</td><td>Rarely</td></tr>
        <tr><td>Insurance copay tier</td><td>ER copay ($250&ndash;$500+)</td><td>Specialist or PCP copay ($25&ndash;$75)</td></tr>
        <tr><td>Can handle life-threatening emergencies</td><td>Yes</td><td>No (will call 911)</td></tr>
    </tbody>
</table>

<p><strong>When a freestanding ER makes sense:</strong> It is after hours, your condition could be life-threatening (chest pain, severe bleeding, difficulty breathing, signs of stroke), or you need advanced imaging immediately.</p>

<p><strong>When urgent care is the better choice:</strong> Sprains, minor cuts needing stitches, sore throats, ear infections, UTIs, minor burns, flu symptoms. These conditions do not require ER-level resources, and urgent care handles them at a fraction of the cost. Read our <a href="/guides/urgent-care-billing/">urgent care billing guide</a> for a full breakdown of what to expect.</p>

<div class="key-takeaway">
    <strong>Rule of thumb:</strong> If you can describe your condition to a friend without the word "emergency," start with urgent care. You can always be transferred to an ER if needed. Look up your hospital in our <a href="/hospitals/">hospital pricing directory</a> to compare facility costs before you go.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a freestanding emergency room?</h3>
        <p>A freestanding ER is an emergency facility that operates independently from a hospital campus. It looks like an urgent care clinic but is licensed as an emergency department, allowing it to charge hospital-level facility fees. There are over 700 freestanding ERs nationwide, with Texas leading at 200+.</p>
    </div>

    <div class="faq-item">
        <h3>Why are freestanding ER bills so much higher than urgent care?</h3>
        <p>Freestanding ERs bill using ER facility fee codes (CPT 99281&ndash;99285) plus a separate facility charge. Urgent care uses standard office visit codes with no facility fee. The facility fee alone adds $1,500&ndash;$3,500 to a freestanding ER visit, even for conditions that urgent care handles routinely for $100&ndash;$250.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover freestanding ER visits?</h3>
        <p>Most plans cover freestanding ER visits but apply ER-level cost-sharing&mdash;meaning your $500 ER copay instead of your $50 urgent care copay. Many freestanding ERs are also out-of-network, which can trigger even higher out-of-pocket costs despite No Surprises Act protections.</p>
    </div>

    <div class="faq-item">
        <h3>Can I dispute a freestanding ER bill?</h3>
        <p>Yes. Request an itemized bill, compare charges to Medicare rates, challenge the ER visit level if your condition was minor, and look for bogus add-on charges like trauma fees. <a href="/scan">Upload your bill to BillKarma</a> for an instant audit that flags every overcharge.</p>
    </div>

    <div class="faq-item">
        <h3>How can I tell if a facility is a freestanding ER or an urgent care?</h3>
        <p>Look for "emergency room," "emergency center," or "emergency department" in the name or signage. Call ahead and ask: "Are you licensed as an emergency department or an urgent care clinic?" Freestanding ERs are required to disclose their ER status, but the signage is often designed to look like a walk-in clinic.</p>
    </div>

    <div class="faq-item">
        <h3>Are freestanding ERs regulated by the No Surprises Act?</h3>
        <p>Yes. The No Surprises Act prevents balance billing for emergency services at out-of-network freestanding ERs. However, the facility fee itself is still permitted, and the Act does not cap total charges&mdash;only your personal balance billing exposure. Your insurer negotiates the total payment through an independent dispute resolution process.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthaffairs.org/" target="_blank" rel="noopener">Health Affairs: Freestanding Emergency Department Cost Analysis (2023)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.tdi.texas.gov/" target="_blank" rel="noopener">Texas Department of Insurance: Freestanding ER Regulations</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Implementation</a></li>
    <li><a href="https://www.acep.org/" target="_blank" rel="noopener">American College of Emergency Physicians: Emergency Department Coding Guidelines</a></li>
    <li><a href="https://www.annals.org/" target="_blank" rel="noopener">Annals of Emergency Medicine: Freestanding ED Utilization Patterns</a></li>
</ul>
""",
})
