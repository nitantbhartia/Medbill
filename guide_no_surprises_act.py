"""Guide: The No Surprises Act: What It Covers and What It Doesn't."""

from guides import register, _embed

register("no-surprises-act-explained", {
    "title": "The No Surprises Act: What It Covers and What It Doesn't",
    "meta_description": "The No Surprises Act bans most surprise medical bills, but has important gaps. Learn what's covered, what isn't, and what to do if you're balance billed illegally.",
    "published": "2026-04-06",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Does the No Surprises Act cover ground ambulance bills?",
            "a": "No&mdash;not yet. Ground ambulance was explicitly excluded from the original No Surprises Act while a federal advisory committee studied the issue. As of 2026, CMS has proposed rules to extend protections to ground ambulance, but the final rule has not been issued. Air ambulance (helicopter and fixed-wing) is fully protected under the NSA. Check your state&rsquo;s insurance commissioner website for any state-level ground ambulance balance billing protections.",
        },
        {
            "q": "What do I do if a provider illegally balance bills me under the No Surprises Act?",
            "a": "File a complaint immediately. You can submit complaints to the federal No Surprises Help Desk at 1-800-985-3059 or online at CMS.gov. You can also file with your state insurance commissioner. Providers who violate the NSA can face civil monetary penalties of up to $10,000 per violation. Keep records of the bill, any EOB from your insurer, and all communications with the provider.",
        },
        {
            "q": "Does the No Surprises Act apply to self-pay patients?",
            "a": "The NSA&rsquo;s balance billing protections primarily apply to patients with insurance. However, the NSA also established Good Faith Estimate requirements: providers must give uninsured and self-pay patients a written cost estimate before scheduled services. If your actual bill exceeds the estimate by more than $400, you have the right to dispute it through the Patient-Provider Dispute Resolution process.",
        },
    ],
    "body": f"""<article>

<div class="answer-box" style="border-left: 4px solid #22c55e; padding: 1rem 1.25rem; background: #f0fdf4; margin-bottom: 1.5rem;">
    <strong>The short answer:</strong> The No Surprises Act (effective January 2022) bans balance billing in emergencies and from out-of-network providers at in-network facilities&mdash;covering surprise bills from anesthesiologists, radiologists, and other providers you didn&rsquo;t choose. But it has significant gaps: ground ambulance, out-of-network facilities you voluntarily chose, and certain plan types are not covered.
</div>

<p class="lead">Before 2022, receiving emergency care at an out-of-network hospital&mdash;or even choosing an in-network hospital and unknowingly receiving care from an out-of-network anesthesiologist&mdash;could result in a surprise bill for thousands of dollars. The No Surprises Act changed that for many situations. But the law has important gaps, and knowing the difference between what&rsquo;s protected and what isn&rsquo;t could save you significant money.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-it-covers">What the No Surprises Act covers</a></li>
        <li><a href="#what-it-doesnt-cover">What it does NOT cover</a></li>
        <li><a href="#cost-sharing-rules">How cost-sharing works under the NSA</a></li>
        <li><a href="#idr-process">The Independent Dispute Resolution process</a></li>
        <li><a href="#good-faith-estimates">Good Faith Estimates for self-pay patients</a></li>
        <li><a href="#if-balance-billed">What to do if you&rsquo;re balance billed illegally</a></li>
    </ol>
</nav>

<h2 id="what-it-covers">What the No Surprises Act covers</h2>

<p>The NSA applies to emergency services and to non-emergency services from out-of-network providers at in-network facilities. Here is a precise breakdown of each protected scenario:</p>

<h3>Emergency care at any facility</h3>
<p>If you receive emergency care at any hospital emergency department&mdash;regardless of whether that hospital is in your insurance network&mdash;you cannot be billed more than your in-network cost-sharing (deductible, copay, coinsurance) for the emergency services. This applies even if:</p>
<ul>
    <li>You were transported to the nearest hospital, which happened to be out of network</li>
    <li>Your condition was stabilized at an out-of-network facility before transfer</li>
    <li>You received post-stabilization care as an inpatient after an emergency admission</li>
</ul>
<p>Once you are stabilized and can safely be transferred, the post-stabilization rules apply: the provider must notify you of your out-of-network status and give you the option to transfer to an in-network facility. If you consent in writing to stay at the out-of-network facility for continued care, the NSA balance billing protection ends for that portion of your stay.</p>

<h3>Out-of-network providers at in-network facilities</h3>
<p>This provision eliminates the &ldquo;phantom provider&rdquo; problem. When you schedule a procedure at an in-network hospital or surgery center, you cannot always control which individual providers treat you. The NSA protects you from surprise bills from:</p>
<ul>
    <li><strong>Anesthesiologists</strong> you didn&rsquo;t choose and couldn&rsquo;t have reasonably avoided</li>
    <li><strong>Radiologists</strong> who read your imaging studies</li>
    <li><strong>Pathologists</strong> who analyzed your lab samples</li>
    <li><strong>Hospitalists</strong> or consulting physicians your treating doctor brought in</li>
    <li><strong>Neonatologists</strong> who cared for a newborn during delivery</li>
    <li><strong>Assistant surgeons</strong> assigned by the facility rather than chosen by you</li>
</ul>
<p>For all of these providers, you pay only your in-network cost-sharing. The provider and your insurer resolve their payment dispute directly, without involving you in the financial gap.</p>

<h3>Air ambulance</h3>
<p>Air ambulance (helicopter and fixed-wing aircraft) is fully protected under the NSA. Regardless of whether the air ambulance company is in your insurance network, you pay only your in-network cost-sharing. This protection applies to all non-grandfathered group and individual health plans.</p>

{_embed(mode="cost", cpt="A0431", title="Air ambulance Medicare rates", subtitle="See what Medicare pays for helicopter ambulance transport.")}

<h2 id="what-it-doesnt-cover">What the No Surprises Act does NOT cover</h2>

<p>Understanding the gaps in the NSA is just as important as knowing what it covers. These are the situations where you remain vulnerable to surprise bills:</p>

<h3>Ground ambulance</h3>
<p>Ground ambulance was explicitly carved out of the original NSA. Congress directed a federal advisory committee to study ground ambulance balance billing separately. CMS published proposed rules in 2024, but as of 2026 the final rule has not been issued. If you receive a ground ambulance bill with a balance beyond your cost-sharing, you are not automatically protected under federal law&mdash;unless your state has its own ground ambulance balance billing statute.</p>

<h3>Out-of-network facilities you voluntarily chose</h3>
<p>If you chose an out-of-network hospital or facility for a non-emergency procedure&mdash;and you received and signed a proper consent form acknowledging the out-of-network status at least 72 hours before the service&mdash;the NSA does not protect you from balance billing by that facility. The individual out-of-network providers at that facility may still be protected if you didn&rsquo;t specifically choose them.</p>

<h3>Out-of-network providers when you had a genuine choice</h3>
<p>If the facility offered you an in-network provider as an alternative and you voluntarily chose an out-of-network provider instead, you can be balance billed for that provider&rsquo;s services. The key legal question is whether you received and signed valid consent in writing at least 72 hours before the service&mdash;a provider who fails to get proper written consent cannot balance bill you.</p>

<h3>Dental-only and vision-only plans</h3>
<p>Standalone dental and vision plans are not subject to the NSA. Behavioral health services have complex coverage rules that depend on your specific plan type. If you have a standalone dental or vision plan, the NSA does not apply to those bills.</p>

<h3>Short-term health plans and grandfathered plans</h3>
<p>Short-term limited duration health insurance plans and grandfathered health plans (plans that predated the ACA and have not made significant changes) are generally exempt from the NSA. If you have one of these plan types, review your plan documents carefully or contact your state insurance commissioner to understand your protections.</p>

<h2 id="cost-sharing-rules">How cost-sharing works under the NSA</h2>

<p>When the NSA applies, your cost-sharing is calculated as if the out-of-network provider were in-network. In practice:</p>

<ul>
    <li>The charge applies to your <strong>in-network deductible</strong>, not your higher out-of-network deductible</li>
    <li>You pay your <strong>in-network coinsurance or copay</strong> rate</li>
    <li>The charges count toward your <strong>in-network out-of-pocket maximum</strong></li>
</ul>

<p>If your insurer processes the claim at out-of-network rates and charges you more than your in-network cost-sharing, that is a violation of the NSA. File an internal appeal with your insurer first&mdash;this is often a processing error that can be corrected. If your insurer refuses to correct it, file a complaint with your state insurance commissioner or the federal No Surprises Help Desk.</p>

<h2 id="idr-process">The Independent Dispute Resolution (IDR) process</h2>

<p>When an out-of-network provider and an insurer cannot agree on payment under the NSA, they can take the dispute to federal Independent Dispute Resolution (IDR). Here is how the process works:</p>

<ol>
    <li><strong>Open negotiation (30 days):</strong> After the insurer issues payment, the provider has 30 days to negotiate directly with the insurer. You are not a party to these negotiations.</li>
    <li><strong>IDR initiation:</strong> If negotiation fails, either party can initiate federal IDR within 4 days of the negotiation deadline. An independent certified IDR entity is selected by both parties or assigned by default.</li>
    <li><strong>Baseball arbitration:</strong> Each party submits a single payment amount. The IDR entity must choose one of the two amounts&mdash;it cannot split the difference. The entity must give substantial weight to the Qualifying Payment Amount (QPA), which is the insurer&rsquo;s median in-network contracted rate for the service in the geographic area.</li>
    <li><strong>Binding decision:</strong> The losing party pays the IDR administrative fee (typically $350&ndash;$600 per dispute). The result is final and binding.</li>
</ol>

<p><strong>What this means for you as a patient:</strong> You are not a party to IDR. Whatever the outcome between the provider and the insurer, you pay only your in-network cost-sharing. The process fully insulates you from the payment gap&mdash;which is the entire point of the NSA&rsquo;s structure.</p>

<h2 id="good-faith-estimates">Good Faith Estimates for self-pay patients</h2>

<p>The NSA created a separate protection for uninsured and self-pay patients through the Good Faith Estimate (GFE) requirement. Any provider scheduling a non-emergency service for an uninsured or self-pay patient must provide a written GFE at least one business day before the service. The GFE must include:</p>

<ul>
    <li>Expected charges for the primary service and all anticipated ancillary services (labs, anesthesia, assistant surgeons)</li>
    <li>Diagnosis codes, service codes, and expected charge for each item</li>
    <li>The name, NPI, and tax identification number of each provider included</li>
</ul>

<p>If your actual bill exceeds the GFE by more than $400, you can initiate a Patient-Provider Dispute Resolution (PPDR) within 120 days of receiving the bill. The filing fee is $25. If the dispute is decided in your favor, the provider refunds the filing fee and must accept a payment at or near the GFE amount.</p>

<h2 id="if-balance-billed">What to do if you&rsquo;re balance billed illegally</h2>

<p>If you receive a bill that you believe violates the No Surprises Act, take these steps in order:</p>

<ol>
    <li><strong>Pull your EOB.</strong> Verify that your insurer processed the claim at in-network rates. Many apparent NSA violations are actually insurer processing errors. Call your insurer first&mdash;ask them to reprocess the claim under NSA guidelines.</li>
    <li><strong>Contact the provider in writing.</strong> State that the service is subject to the No Surprises Act, that your cost-sharing should be calculated at in-network rates, and request a corrected bill. Send via certified mail and keep the tracking number.</li>
    <li><strong>File a federal complaint.</strong> Call the No Surprises Help Desk at <strong>1-800-985-3059</strong> or file online at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>. CMS and DOL share enforcement responsibility. Providers who violate the NSA face civil monetary penalties up to $10,000 per violation.</li>
    <li><strong>File a state complaint.</strong> Your state insurance commissioner may have concurrent enforcement authority. Many states have expedited complaint processes for surprise billing violations.</li>
    <li><strong>Do not pay the disputed balance while the complaint is pending.</strong> Request a billing hold from the provider. Paying the balance does not waive your rights, but it complicates the refund process.</li>
</ol>

<div class="key-takeaway" style="border-left: 4px solid #22c55e; padding: 1rem 1.25rem; background: #f0fdf4; margin: 1.5rem 0;">
    <strong>Not sure if your bill violates the No Surprises Act?</strong> <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll identify whether NSA protections apply to your situation and help you draft a dispute letter.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Resources and Consumer Tools</a></li>
    <li><a href="https://www.hhs.gov/sites/default/files/surprise-billing-consumer-protections.pdf" target="_blank" rel="noopener">HHS: No Surprises Act Consumer Protections Fact Sheet</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">KFF: No Surprises Act Implementation and Consumer Impact (2024)</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/no-surprises-act" target="_blank" rel="noopener">DOL: No Surprises Act &mdash; Group Health Plan Requirements</a></li>
    <li><a href="https://www.cms.gov/files/document/idr-process-overview.pdf" target="_blank" rel="noopener">CMS: Independent Dispute Resolution Process Overview</a></li>
</ul>

</article>""",
})
