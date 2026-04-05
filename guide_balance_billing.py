"""Guide: Balance Billing."""

from guides import register, _embed

register("balance-billing", {
    "title": "Balance Billing: What It Is and How to Fight It (2026)",
    "meta_description": "Balance billing happens when a provider charges you the gap between their rate and what insurance paid. Learn when it's illegal under the No Surprises Act and how to dispute it.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What is balance billing?",
            "a": "Balance billing occurs when an out-of-network provider charges you the difference between their billed rate and the amount your insurance paid. For example, if a provider charges $500, your insurance pays $300 (the allowed amount), and the provider bills you the remaining $200&mdash;that $200 is a balance bill. Whether this is legal depends on the type of care, where it was received, and your state&rsquo;s laws.",
        },
        {
            "q": "What is the No Surprises Act?",
            "a": "The No Surprises Act (NSA), effective January 1, 2022, is a federal law that protects patients from unexpected out-of-network bills in specific situations: emergency care at any facility, non-emergency care at in-network facilities by out-of-network providers (like anesthesiologists) when you did not choose them, and air ambulance services. In these situations, you can only be charged in-network cost-sharing rates, and the provider cannot balance bill you for the rest.",
        },
        {
            "q": "Can I waive my No Surprises Act protections?",
            "a": "For non-emergency, non-ancillary services, an out-of-network provider can ask you to sign a consent form waiving your NSA protections. You are never required to sign. If you sign, you give up your right to in-network cost-sharing and can be balance billed. Never sign an NSA waiver unless you have fully compared the out-of-network cost to what in-network providers charge and made an informed choice.",
        },
        {
            "q": "How do I report an illegal balance bill?",
            "a": "File a complaint with the Centers for Medicare &amp; Medicaid Services (CMS) at 1-800-985-3059 or online at cms.gov/nosurprises. You can also file with your state insurance commissioner, which may be faster if your state has additional protections. Keep all documentation: the bill, your EOB, any consent forms (or lack thereof), and records of your calls with the provider.",
        },
        {
            "q": "Does the No Surprises Act apply to ground ambulance?",
            "a": "No. Ground ambulance is the most significant gap in the No Surprises Act&mdash;it is explicitly excluded. Air ambulance is covered by the NSA, but ground ambulance billing remains largely unregulated at the federal level. Some states (California, New York, Texas) have enacted state-level ground ambulance balance billing protections. Check your state insurance commissioner&rsquo;s website for current rules.",
        },
    ],
    "body": f"""
<p class="lead">You went to an in-network hospital. You followed all the rules. Then a bill arrived from an anesthesiologist, radiologist, or ER doctor you never chose&mdash;for thousands of dollars your insurance refuses to pay in full. This is balance billing, and it has been one of the most common and damaging medical billing abuses in the US. <strong>NSA violations resulted in an estimated $1.2 billion in illegal charges intercepted in 2025.</strong> Here is exactly what balance billing is, when it is illegal under the No Surprises Act, and how to fight it step by step.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-balance-billing">What balance billing is (with a real example)</a></li>
        <li><a href="#when-legal">When balance billing is legal</a></li>
        <li><a href="#when-illegal">When balance billing is illegal: the No Surprises Act</a></li>
        <li><a href="#consent-forms">NSA consent forms: what to do if asked to sign</a></li>
        <li><a href="#how-to-spot">How to spot an illegal balance bill</a></li>
        <li><a href="#dispute-steps">Step-by-step dispute process</a></li>
        <li><a href="#state-protections">State protections beyond the NSA</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-balance-billing">1. What balance billing is (with a real example)</h2>

<p>Balance billing is the practice of charging a patient the gap between a provider&rsquo;s full billed rate and the amount the insurance company paid. It happens almost exclusively with out-of-network providers, because in-network providers have signed contracts agreeing to accept the insurance-allowed amount as payment in full.</p>

<div class="bill-example">
    <div class="bill-header">Balance Billing Example &mdash; Out-of-Network Anesthesiologist</div>
    <div class="line-item">
        <span>Anesthesiologist billed amount</span>
        <span>$4,800.00</span>
    </div>
    <div class="line-item">
        <span>Your insurance&rsquo;s allowed amount</span>
        <span>$1,900.00</span>
    </div>
    <div class="line-item">
        <span>Insurance paid (80% of allowed amount, after deductible met)</span>
        <span>$1,520.00</span>
    </div>
    <div class="line-item">
        <span>Your coinsurance (20% of allowed amount)</span>
        <span>$380.00</span>
    </div>
    <div class="line-item error">
        <span>Balance bill: what the provider bills you beyond your coinsurance</span>
        <span>$2,900.00</span>
    </div>
    <div class="line-total">
        <span>WHAT YOU SHOULD LEGALLY OWE (if NSA applies)</span>
        <span>$380.00</span>
    </div>
</div>

<p>In this example, the patient went to an in-network hospital for surgery and never chose the anesthesiologist&mdash;the hospital assigned one who was out-of-network. Under the No Surprises Act, the patient owes only their in-network cost-sharing ($380). The $2,900 balance bill is illegal.</p>

<h2 id="when-legal">2. When balance billing is legal</h2>

<p>Balance billing is legally permitted when you <strong>knowingly and voluntarily choose an out-of-network provider for non-emergency care</strong>: you have a PPO plan that allows out-of-network benefits, you select a specific out-of-network specialist with full knowledge of their status, the provider is not an ancillary provider at an in-network facility, and you did not sign an NSA consent waiver under duress. In this scenario, the provider can charge you their full rate minus what insurance pays.</p>

<h2 id="when-illegal">3. When balance billing is illegal: the No Surprises Act</h2>

<p>The No Surprises Act (NSA), effective January 1, 2022, prohibits balance billing in three specific situations:</p>

<table>
    <thead>
        <tr><th>Situation</th><th>NSA Protection</th><th>What You Owe</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Emergency care at any facility</strong></td><td>Full protection regardless of network status</td><td>In-network cost-sharing only</td></tr>
        <tr><td><strong>Non-emergency care at in-network facility by out-of-network provider you did not choose</strong></td><td>Protected unless you sign a valid consent waiver</td><td>In-network cost-sharing only</td></tr>
        <tr><td><strong>Air ambulance services</strong></td><td>Full protection</td><td>In-network cost-sharing only</td></tr>
        <tr><td><strong>Ground ambulance</strong></td><td>NOT covered by NSA (major gap)</td><td>Subject to state law; may be balance billed</td></tr>
        <tr><td><strong>Voluntary out-of-network care</strong></td><td>Not protected (you chose OON provider)</td><td>Full balance bill allowed</td></tr>
    </tbody>
</table>

<p>The most common NSA situation is the <strong>ancillary provider trap</strong>: you choose an in-network hospital and surgeon, but an out-of-network anesthesiologist, radiologist, pathologist, or ER physician is assigned without your input. Under the NSA, these providers cannot balance bill you. The NSA also requires insurers to send you an <strong>Advanced Explanation of Benefits (AEOB)</strong> before scheduled non-emergency care showing your estimated costs.</p>

<h2 id="consent-forms">4. NSA consent forms: what to do if asked to sign</h2>

<p>The NSA allows out-of-network providers to ask you to waive your protections for non-emergency, non-ancillary services only. Key rules:</p>

<ol>
    <li><strong>You are never required to sign.</strong> Refusing does not mean losing access to care at the facility.</li>
    <li><strong>Consent must be informed.</strong> The provider must give you a good-faith cost estimate showing what you&rsquo;ll owe out-of-network vs. in-network.</li>
    <li><strong>72-hour notice required.</strong> For scheduled procedures, the form must be provided at least 72 hours before the service (or 3 hours before for same-day scheduling).</li>
    <li><strong>Emergency providers cannot ask you to sign.</strong> Any consent form presented in an emergency setting is invalid and unenforceable.</li>
    <li><strong>Ancillary providers cannot ask you to sign.</strong> An anesthesiologist assigned by the hospital cannot use the consent waiver process.</li>
</ol>

<div class="key-takeaway">
    <strong>If you signed under pressure in a pre-op area or emergency department:</strong> The waiver may be invalid. File a complaint with CMS at 1-800-985-3059. Consent obtained without the required advance notice or in an emergency setting is not enforceable.
</div>

<h2 id="how-to-spot">5. How to spot an illegal balance bill</h2>

<p>Ask these questions when reviewing any bill from a provider you did not explicitly choose:</p>

<ul>
    <li>Was this an emergency visit? If yes, the NSA applies and balance billing is prohibited.</li>
    <li>Was this an ancillary provider at an in-network facility (anesthesiologist, radiologist, pathologist, ER physician, hospitalist) that you did not personally select? If yes, NSA likely applies.</li>
    <li>Was this an air ambulance? If yes, NSA applies.</li>
    <li>Did you sign an NSA consent waiver with proper 72-hour advance notice? If no, and the provider is balance billing you, that is likely illegal.</li>
    <li>Does the bill exceed your in-network deductible, coinsurance, or copay? Compare to your EOB&mdash;the EOB shows your correct patient responsibility.</li>
</ul>

<h2 id="dispute-steps">6. Step-by-step dispute process</h2>

<ol>
    <li><strong>Get your EOB from your insurer.</strong> The EOB shows the claim, the allowed amount, what insurance paid, and what you legitimately owe.</li>
    <li><strong>Compare the EOB to the provider&rsquo;s bill.</strong> If the bill exceeds your &ldquo;patient responsibility&rdquo; on the EOB, you may have an illegal balance bill.</li>
    <li><strong>Call the provider&rsquo;s billing department.</strong> Reference the NSA and ask whether a valid NSA consent waiver was obtained. Many billing departments reduce or eliminate the balance when challenged directly.</li>
    <li><strong>Send a written dispute.</strong> Use the template below. Send via certified mail. This creates a paper trail and may trigger hold periods under state law.</li>
    <li><strong>File a complaint with CMS.</strong> Call 1-800-985-3059 or go to CMS.gov/nosurprises. CMS investigates and can fine providers violating the NSA.</li>
    <li><strong>File with your state insurance commissioner.</strong> State regulators often act faster and may have additional remedies. Find your commissioner at NAIC.org.</li>
    <li><strong>Use BillKarma.</strong> <a href="/fight-debt">Upload your bill</a> to generate a customized dispute letter and get guidance specific to your state.</li>
</ol>

<div class="case-study">
    <h3>Dispute letter template for an illegal balance bill</h3>
    <p><em>&ldquo;I am writing to dispute the balance of $[AMOUNT] on account [ACCOUNT NUMBER]. Under the No Surprises Act (42 U.S.C. &sect; 300gg-111), I am entitled to pay only my in-network cost-sharing amount for [emergency care / services provided by an out-of-network provider at an in-network facility]. My Explanation of Benefits from [INSURER NAME] shows my patient responsibility is $[EOB AMOUNT]. I did not sign an NSA consent waiver authorizing out-of-network billing. I request that you correct this bill to $[EOB AMOUNT] within 30 days. If unresolved, I will file a complaint with CMS and the [STATE] Department of Insurance.&rdquo;</em></p>
</div>

{_embed(mode="scan", title="Is your balance bill legal?", subtitle="Upload your bill and EOB to BillKarma for a free review.")}

<h2 id="state-protections">7. State protections beyond the NSA</h2>

<table>
    <thead>
        <tr><th>State</th><th>Key Protection Beyond NSA</th><th>Ground Ambulance</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>New York</strong></td><td>NSA-style protections for fully-insured state-regulated plans; additional arbitration rights</td><td>Protected</td></tr>
        <tr><td><strong>California</strong></td><td>AB 72 protects against OON billing at in-network facilities; comprehensive since 2017</td><td>Partially protected</td></tr>
        <tr><td><strong>Texas</strong></td><td>SB 1264 provides strong protections for state-regulated plans</td><td>Partially protected</td></tr>
        <tr><td><strong>Illinois</strong></td><td>State surprise billing law for state-regulated plans, aligned with NSA</td><td>Not protected</td></tr>
        <tr><td><strong>All other states</strong></td><td>Federal NSA applies; no additional state protections</td><td>Generally not protected</td></tr>
    </tbody>
</table>

<p>Note: The NSA applies to employer self-funded plans (ERISA plans) and federally-regulated insurance. State laws primarily cover fully-insured state-regulated plans. If your insurance is through a large employer, it is likely self-funded and governed only by federal law.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is balance billing?</h3>
        <p>Balance billing occurs when an out-of-network provider charges you the difference between their billed rate and the amount your insurance paid. Whether this is legal depends on the type of care, where it was received, and state law. The No Surprises Act made balance billing illegal for emergency care, ancillary providers at in-network facilities, and air ambulance.</p>
    </div>

    <div class="faq-item">
        <h3>What is the No Surprises Act?</h3>
        <p>The No Surprises Act (effective January 2022) prohibits balance billing for emergency care, out-of-network ancillary providers at in-network facilities, and air ambulance. Patients pay only their in-network cost-sharing. Providers must resolve payment disputes through an independent dispute resolution process, not by billing the patient for the difference.</p>
    </div>

    <div class="faq-item">
        <h3>Can I waive my No Surprises Act protections?</h3>
        <p>Only for non-emergency, non-ancillary services, with proper 72-hour advance notice and a good-faith cost estimate. You are never required to sign. Emergency providers and ancillary providers (anesthesiologists, radiologists) cannot ask you to waive NSA protections under any circumstances.</p>
    </div>

    <div class="faq-item">
        <h3>How do I report an illegal balance bill?</h3>
        <p>File a complaint with CMS at 1-800-985-3059 or cms.gov/nosurprises. Also file with your state insurance commissioner. Keep all documentation: the bill, your EOB, any consent forms, and records of your communications with the provider.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act apply to ground ambulance?</h3>
        <p>No. Ground ambulance is explicitly excluded from the NSA. Some states (New York, California, Texas) have enacted their own ground ambulance balance billing protections. Check with your state insurance commissioner for current rules. For unprotected ground ambulance bills, asking for the Medicare rate as a negotiating anchor is often effective.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: No Surprises Act Overview</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Complaint Process (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: No Surprises Act Implementation Update (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">New York State Department of Financial Services: Surprise Bill Protections</a></li>
    <li><a href="#" target="_blank" rel="noopener">California Department of Managed Health Care: AB 72 Balance Billing Protections</a></li>
    <li><a href="#" target="_blank" rel="noopener">BillKarma Internal Data: NSA Violation Tracking Report (2026)</a></li>
</ul>
""",
})
