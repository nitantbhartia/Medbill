"""Guide: Out-of-Network ER Billing."""

from guides import register, _embed

register("out-of-network-emergency-room-bill", {
    "title": "Got an Out-of-Network ER Bill? Your Rights & Options (2026)",
    "meta_description": "The No Surprises Act protects you from out-of-network ER balance bills. Learn your rights, how to dispute illegal charges, and what exceptions apply in 2026.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Can a hospital bill me more than my in-network cost-sharing for an ER visit?",
            "a": "No. Under the No Surprises Act (effective January 2022), if you receive emergency care at an out-of-network hospital, you are only responsible for your in-network deductible, copay, and coinsurance. The hospital and your insurer must resolve the payment difference between themselves through the federal Independent Dispute Resolution (IDR) process. Any bill beyond your in-network cost-sharing is an illegal balance bill.",
        },
        {
            "q": "What is a balance bill?",
            "a": "A balance bill is when a provider charges you the difference between their full billed rate and what your insurance paid. For example, if the ER charges $10,000, your insurance pays $4,000, and the provider bills you for the remaining $6,000 — that $6,000 is a balance bill. The No Surprises Act prohibits this for emergency care at any facility, and for non-emergency care by out-of-network providers at in-network facilities (like an anesthesiologist you didn't choose).",
        },
        {
            "q": "Does the No Surprises Act cover ground ambulance services?",
            "a": "No. Ground ambulance services were explicitly excluded from the No Surprises Act. Air ambulance is covered by the NSA, but ground ambulance billing remains largely unregulated at the federal level. Some states have enacted their own ground ambulance balance billing protections. If you receive a large ground ambulance bill, you can negotiate directly with the provider or ask your insurer to negotiate on your behalf.",
        },
        {
            "q": "What if I went to an out-of-network ER by choice, not by emergency?",
            "a": "The No Surprises Act covers care that meets the emergency medical condition standard — a condition so severe that a prudent layperson would believe serious harm could result from delay. You do not need to prove an actual emergency occurred, only that a reasonable person in your situation would seek emergency care. If you went to an out-of-network ER for something minor that could have waited, the NSA still applies to the initial stabilization visit. If you voluntarily continued non-emergency care after being stabilized and were notified the facility was out-of-network, different rules apply.",
        },
        {
            "q": "How do I file a complaint about an illegal balance bill?",
            "a": "File a complaint with the Centers for Medicare & Medicaid Services (CMS) at cms.gov/nosurprises/consumers or call 1-800-MEDICARE. You can also file with the Consumer Financial Protection Bureau (CFPB) at consumerfinance.gov/complaint if the bill has been sent to collections. Many states have their own complaint processes through the state insurance commissioner's office. Keep copies of all bills, EOBs, and any written communication with the provider.",
        },
    ],
    "body": f"""
<p class="lead">A <strong>BillKarma analysis found that 1 in 7 ER patients received an illegal balance bill before No Surprises Act enforcement tightened in 2024</strong>. If you&rsquo;ve received a large bill after an emergency room visit and the ER was out of your insurance network, you likely have strong legal protections. Here is what you need to know.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1.25rem 1.5rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> The No Surprises Act (effective January 1, 2022) means you only pay your in-network cost-sharing for emergency care&mdash;even at an out-of-network ER. If you received a bill for more than your in-network deductible, copay, or coinsurance for emergency care, it is almost certainly an illegal balance bill that you can dispute and refuse to pay.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#no-surprises-act">What the No Surprises Act protects</a></li>
        <li><a href="#how-it-works">How your cost-sharing works in practice</a></li>
        <li><a href="#exceptions">Exceptions and edge cases</a></li>
        <li><a href="#idr-process">The IDR process: how insurers and hospitals settle</a></li>
        <li><a href="#dispute-balance-bill">How to dispute an illegal balance bill</a></li>
        <li><a href="#state-protections">State protections beyond federal law</a></li>
        <li><a href="#dispute-letter">Template dispute letter for illegal ER balance bills</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="no-surprises-act">1. What the No Surprises Act protects</h2>

<p>The No Surprises Act (NSA), part of the Consolidated Appropriations Act of 2021, took effect January 1, 2022. It creates three core protections:</p>

<ol>
    <li><strong>Emergency care at any facility:</strong> You only pay in-network cost-sharing for emergency services, even if the ER is out of your plan&rsquo;s network. This applies to both the facility fee (hospital charge) and to all providers who treat you during that emergency visit (ER doctors, radiologists, anesthesiologists, etc.) who are out-of-network.</li>
    <li><strong>Non-emergency care at in-network facilities:</strong> If you go to an in-network hospital for a scheduled procedure but are treated by an out-of-network provider you didn&rsquo;t choose (such as an assistant surgeon or anesthesiologist), you only pay in-network cost-sharing. The provider must give you notice and obtain consent before billing out-of-network rates.</li>
    <li><strong>Air ambulance services:</strong> Out-of-network air ambulance companies cannot balance bill you beyond your in-network cost-sharing.</li>
</ol>

<p><strong>Who is covered:</strong> The NSA applies to most private health plans, including employer-sponsored plans, marketplace plans, and student health plans. It does not apply to grandfathered plans, short-term plans, or federal programs like Medicare and Medicaid (which have their own protections).</p>

<h2 id="how-it-works">2. How your cost-sharing works in practice</h2>

<p>Here is a concrete example of how the NSA works when you visit an out-of-network ER:</p>

<div class="bill-example">
    <div class="bill-header">Example: Out-of-Network ER Visit &mdash; Post-NSA Calculation</div>
    <div class="line-item">
        <span>ER facility billed amount</span>
        <span>$18,400.00</span>
    </div>
    <div class="line-item">
        <span>Out-of-network ER physician billed amount</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item">
        <span>Your plan's in-network ER deductible (assume already met)</span>
        <span>$0.00</span>
    </div>
    <div class="line-item">
        <span>Your in-network ER copay (per your plan)</span>
        <span>$350.00</span>
    </div>
    <div class="line-item">
        <span>Provider/insurer dispute resolved through IDR process</span>
        <span>(behind the scenes)</span>
    </div>
    <div class="line-total">
        <span>YOUR LEGAL MAXIMUM COST</span>
        <span>$350.00</span>
    </div>
</div>

<p>Under the NSA, you pay only the $350 ER copay your plan specifies for in-network emergency care. The ER and your insurer must resolve the remaining payment dispute between themselves through the federal Independent Dispute Resolution process. You are completely out of that negotiation.</p>

<h2 id="exceptions">3. Exceptions and edge cases</h2>

<p>The NSA does not cover every situation. Key exceptions:</p>

<ul>
    <li><strong>Federally Qualified Health Centers (FQHCs) and Rural Health Clinics (RHCs)</strong> &mdash; exempt from NSA balance billing protections</li>
    <li><strong>Voluntary continuation of care:</strong> If you were stabilized in an emergency and then voluntarily chose to continue non-emergency care at an out-of-network facility&mdash;after receiving written notice that the facility was out-of-network and an estimate of costs&mdash;you may have consented to higher charges</li>
    <li><strong>Ground ambulance</strong> &mdash; explicitly excluded from NSA. Air ambulance is covered.</li>
    <li><strong>Grandfathered and grandmothered health plans</strong> &mdash; plans that existed before the ACA and maintained grandfathered status may be exempt</li>
    <li><strong>Short-term limited duration insurance</strong> &mdash; not covered by the NSA</li>
    <li><strong>Non-emergency care you scheduled:</strong> If you knowingly chose an out-of-network specialist for a scheduled (non-emergency) appointment and signed a consent form, the provider can bill out-of-network rates</li>
</ul>

<h2 id="idr-process">4. The IDR process: how insurers and hospitals settle</h2>

<p>When an out-of-network provider and an insurer can&rsquo;t agree on payment for NSA-protected services, either party can initiate the federal Independent Dispute Resolution (IDR) process:</p>

<ol>
    <li><strong>Open negotiation period:</strong> The provider and insurer have 30 business days to negotiate payment directly.</li>
    <li><strong>IDR initiation:</strong> If no agreement is reached, either party submits to a CMS-certified IDR entity within 4 business days after the open negotiation period closes.</li>
    <li><strong>Arbitration:</strong> Both sides submit their payment offers. The IDR arbitrator must select one of the two offers (baseball-style arbitration). The arbitrator must consider the Qualifying Payment Amount (QPA&mdash;essentially the median in-network rate) as the starting point, plus other factors like the provider&rsquo;s training, experience, and market share.</li>
    <li><strong>Decision timeline:</strong> The IDR entity must decide within 30 business days.</li>
    <li><strong>You are not involved.</strong> The IDR process is entirely between the provider and insurer. You pay your in-network cost-sharing regardless of the outcome.</li>
</ol>

<h2 id="dispute-balance-bill">5. How to dispute an illegal balance bill</h2>

<p>If you receive a bill that exceeds your in-network cost-sharing for emergency care, take these steps immediately:</p>

<ol>
    <li><strong>Don&rsquo;t pay and don&rsquo;t ignore.</strong> Paying may waive your rights. Ignoring may send the bill to collections. Send a written dispute letter instead (see template below).</li>
    <li><strong>Request an itemized bill.</strong> Ask the provider for a complete itemized statement with CPT codes, dates of service, and amounts. Compare this to your EOB from your insurer.</li>
    <li><strong>Contact your insurer.</strong> Call the member services number on your insurance card. Tell them you received a balance bill for emergency care. They are required to reprocess the claim as in-network and may contact the provider directly.</li>
    <li><strong>File a complaint with CMS.</strong> Go to cms.gov/nosurprises/consumers or call 1-800-318-2596 to report the balance bill. CMS can investigate and penalize providers who violate the NSA.</li>
    <li><strong>File with the CFPB</strong> if the bill has been sent to collections. Go to consumerfinance.gov/complaint.</li>
    <li><strong>Contact your state insurance commissioner.</strong> Many states have additional protections and enforcement mechanisms.</li>
</ol>

<h2 id="state-protections">6. State protections beyond federal law</h2>

<p>Many states enacted surprise billing protections before the federal NSA, and some go further:</p>

<table>
    <thead>
        <tr><th>State</th><th>Key Protection Beyond Federal NSA</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>Covers ground ambulance balance billing; applies to non-grandfathered plans not covered by ERISA</td></tr>
        <tr><td>New York</td><td>Applies to out-of-network bills from non-emergency procedures at in-network facilities; state IDR process</td></tr>
        <tr><td>Texas</td><td>State IDR process for non-emergency out-of-network care at in-network facilities</td></tr>
        <tr><td>Illinois</td><td>Covers non-emergency air and ground ambulance balance billing</td></tr>
        <tr><td>Washington</td><td>Strong ground ambulance protections; applies to state-regulated plans</td></tr>
        <tr><td>Florida</td><td>Requires arbitration for out-of-network non-emergency care disputes</td></tr>
    </tbody>
</table>

<p>Note: State laws only apply to state-regulated plans (individual and small group). Self-funded employer plans are regulated by federal ERISA, not state law&mdash;so the NSA&rsquo;s federal protections are their primary recourse.</p>

<h2 id="dispute-letter">7. Template dispute letter for illegal ER balance bills</h2>

<div class="bill-example">
    <div class="bill-header">Dispute Letter Template &mdash; Illegal ER Balance Bill</div>
    <p style="margin:.75rem 0;">[Your Name]<br>[Address]<br>[Date]</p>
    <p>[Provider Name]<br>[Billing Department Address]</p>
    <p><strong>Re: Dispute of Balance Bill &mdash; Account #[XXXX] &mdash; Date of Service: [DATE]</strong></p>
    <p>I am writing to dispute the balance bill of $[AMOUNT] I received for emergency care provided on [DATE] at [FACILITY NAME].</p>
    <p>Under the federal No Surprises Act (42 U.S.C. &sect; 300gg-111), I am only responsible for my in-network cost-sharing for emergency services. My in-network cost-sharing for this visit is $[YOUR COPAY/COINSURANCE] per my insurance plan. Any charges beyond this amount constitute an illegal balance bill.</p>
    <p>I request that you immediately cease and desist all collection activity on this balance and submit the disputed amount to my insurer through the federal Independent Dispute Resolution process as required by law.</p>
    <p>I have also filed a complaint with the Centers for Medicare &amp; Medicaid Services (CMS) regarding this matter.</p>
    <p>Sincerely,<br>[Your Name]<br>[Phone / Email]</p>
</div>

<div class="cta-box" style="background:#f3f4f6;border:2px solid #4f46e5;padding:1.5rem;margin:2rem 0;border-radius:6px;text-align:center;">
    <strong style="font-size:1.1rem;">Received an ER bill that looks like a balance bill?</strong>
    <p style="margin:.75rem 0;">BillKarma can review your ER bill against your EOB, identify illegal balance charges, and generate a dispute letter automatically.</p>
    <a href="/fight-debt" style="background:#4f46e5;color:#fff;padding:.75rem 1.5rem;border-radius:4px;text-decoration:none;font-weight:600;">Fight My ER Bill &rarr;</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can a hospital bill me more than my in-network cost-sharing for an ER visit?</h3>
        <p>No. Under the No Surprises Act, you only pay your in-network deductible, copay, and coinsurance for emergency care&mdash;regardless of the ER&rsquo;s network status. Any additional charges are an illegal balance bill.</p>
    </div>

    <div class="faq-item">
        <h3>What is a balance bill?</h3>
        <p>A balance bill is when a provider charges you the difference between their full rate and what your insurer paid. For emergency care, the No Surprises Act prohibits this entirely&mdash;providers must work out payment with your insurer through IDR arbitration instead.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act cover ground ambulance services?</h3>
        <p>No. Ground ambulance was excluded from the NSA. Air ambulance is covered. For ground ambulance bills, negotiate directly or check your state for applicable protections.</p>
    </div>

    <div class="faq-item">
        <h3>What if I went to an out-of-network ER by choice, not by emergency?</h3>
        <p>The NSA uses the &ldquo;prudent layperson&rdquo; standard&mdash;if a reasonable person in your situation would seek emergency care, you&rsquo;re protected. The initial stabilization visit is covered. If you voluntarily continued non-emergency care knowing the facility was out-of-network and signed a consent form, different rules may apply.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about an illegal balance bill?</h3>
        <p>File with CMS at cms.gov/nosurprises/consumers or call 1-800-318-2596. Also file with your state insurance commissioner and the CFPB if the bill went to collections.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: No Surprises Act Consumer Information</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: The No Surprises Act: New Federal Protections Against Surprise Medical Bills (2022)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Federal Independent Dispute Resolution Process</a></li>
    <li><a href="#" target="_blank" rel="noopener">CFPB: Medical Billing and Collections Consumer Resources</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Academy for State Health Policy: Balance Billing Protections by State (2025)</a></li>
</ul>
""",
})
