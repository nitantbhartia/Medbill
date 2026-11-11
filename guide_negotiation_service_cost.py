"""Guide: What medical bill negotiation services cost."""

from guides import register, _embed

register("medical-bill-negotiation-service-cost", {
    "title": "Medical Bill Negotiation Services: What They Really Cost",
    "meta_description": "Negotiators charge 10–25% of savings, often with a $1,000 cap or minimum fee. See what Resolve, Goodbill, CareRoute and BillKarma cost on real bill sizes.",
    "published": "2026-11-11",
    "author": "BillKarma Team",
    "category": "Negotiating Bills",
    "faqs": [
        {
            "q": "How much do medical bill negotiation services charge?",
            "a": "Most charge a share of what they save you, usually 10% to 25%. Goodbill charges 20% capped at $1,000, CareRoute 18% to 25% capped at $1,000, and Resolve 25% on bills of $5,000 to $15,000 with a minimum fee of up to $1,000. BillKarma charges a flat $29 to $149 based on bill size.",
        },
        {
            "q": "Is a medical bill negotiator worth it for a small bill?",
            "a": "Often not. Resolve only takes bills of $5,000 or more. On a $2,400 bill reduced by $900, Goodbill's 20% fee would be $180, while a flat-fee written dispute is $49. Doing it yourself costs nothing but your time.",
        },
        {
            "q": "Do I have to pay if they don't lower my bill?",
            "a": "Not with the major services. Goodbill, CareRoute and Resolve charge only when they find savings, and Resolve refunds its deposit. BillKarma refunds its flat fee in full if the bill isn't reduced within 45 days.",
        },
        {
            "q": "What's the difference between a flat fee and a contingency fee?",
            "a": "A contingency fee is a percentage of the savings, so it grows as the savings grow. A flat fee is the same no matter how much is saved. Flat fees win on small and mid-size bills; a contingency service with a cap can make sense on very large, complicated bills.",
        },
        {
            "q": "Is there a free way to get a hospital bill reduced?",
            "a": "Yes. Nonprofit hospitals must have a financial assistance policy, and patients under the income limit can get free or discounted care. The nonprofit Dollar For helps people apply for free. You can also request an itemized bill and dispute errors yourself.",
        },
        {
            "q": "How long does medical bill negotiation take?",
            "a": "Resolve says the average case takes about 4 months. CareRoute quotes 4 to 8 weeks. BillKarma sends the dispute right away and follows up on days 7, 14, 30 and 45.",
        },
    ],
    "body": f"""
<p class="lead">Medical bill negotiation services usually keep <strong>10% to 25% of what they save you</strong>, and several add a cap or a minimum fee of about <strong>$1,000</strong> (prices published by <a href="https://help.goodbill.com/en/articles/254209" target="_blank" rel="noopener">Goodbill</a> and <a href="https://resolvemedicalbills.com/faqs/how-much-does-it-cost-to-work-with-resolve" target="_blank" rel="noopener">Resolve</a>, checked November 2026). On a large bill that can be a fair trade. On a $2,000 bill, a minimum fee can take half of what you save.</p>

<p>This guide lays out what each type of service charges, works the math on three real-world bill sizes, and shows when to use a service, when to use a free option and when to do it yourself. Head-to-head: <a href="/guides/billkarma-vs-resolve-medical-bills/">BillKarma vs Resolve</a> and <a href="/guides/billkarma-vs-goodbill-medical-bills/">BillKarma vs Goodbill</a>.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#fee-models">The three ways bill help is priced</a></li>
        <li><a href="#compare">What the main services charge</a></li>
        <li><a href="#math">The math on three bill sizes</a></li>
        <li><a href="#example-bill">What a negotiator is actually looking for</a></li>
        <li><a href="#which">Which option fits your bill</a></li>
        <li><a href="#free">Free options to try first</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="fee-models">1. The three ways bill help is priced</h2>

<table>
    <thead>
        <tr><th>Model</th><th>How you pay</th><th>Best for</th><th>Watch out for</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Contingency</strong> (percentage of savings)</td><td>10%&ndash;25% of the amount saved, only if there are savings</td><td>Large or complicated bills where a person negotiates by phone</td><td>Minimum fees that take a big share of small savings</td></tr>
        <tr><td><strong>Flat fee</strong></td><td>One set price, whatever the savings</td><td>Small and mid-size bills with clear errors or high prices</td><td>Whether the fee is refunded when nothing changes</td></tr>
        <tr><td><strong>Free</strong> (nonprofit or do it yourself)</td><td>Nothing</td><td>Low-income patients at nonprofit hospitals; anyone with time</td><td>Your own time, and charity care only covers some patients</td></tr>
    </tbody>
</table>

<p>A contingency fee (a fee that depends on the result) means the service only gets paid if you save money. That's fair, but the percentage and any minimum decide how much of the win you keep.</p>

<h2 id="compare">2. What the main services charge</h2>

<p>These are the fees each company publishes on its own site, as of November 2026. Prices change, so confirm on the company's page before you sign up. Some services offer different prices through employer or insurance partners.</p>

<table>
    <thead>
        <tr><th>Service</th><th>Fee</th><th>Cap or minimum</th><th>Upfront</th><th>How it works</th></tr>
    </thead>
    <tbody>
        <tr><td><a href="https://resolvemedicalbills.com/faqs/how-much-does-it-cost-to-work-with-resolve" target="_blank" rel="noopener">Resolve</a></td><td>25% of savings ($5k&ndash;$15k bills); 10% (over $15k)</td><td>Minimum fee: the lower of $1,000 or half the savings ($2,500 on bills over $15k)</td><td>$249 or $499 deposit, refunded if no savings</td><td>Personal advocate; bills of $5,000 or more</td></tr>
        <tr><td><a href="https://help.goodbill.com/en/articles/254209" target="_blank" rel="noopener">Goodbill</a></td><td>20% of savings</td><td>Capped at $1,000</td><td>None</td><td>Software plus experts, hospital bills</td></tr>
        <tr><td><a href="https://www.careroute.ai/bill-defense" target="_blank" rel="noopener">CareRoute</a></td><td>18%&ndash;25% of savings</td><td>Capped at $1,000</td><td>None</td><td>Handles provider and insurer side</td></tr>
        <tr><td><a href="/">BillKarma</a></td><td>Flat: $29, $49, $99 or $149 by bill size</td><td>Refunded in full if not reduced in 45 days</td><td>The flat fee</td><td>Written dispute sent to billing, automatic follow-ups</td></tr>
        <tr><td><a href="https://triagecancer.org/dollar-for-charity-care" target="_blank" rel="noopener">Dollar For</a></td><td>Free</td><td>&mdash;</td><td>None</td><td>Nonprofit; applies for charity care for you</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Check the bill before you hire anyone.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we compare every line to what Medicare pays and flag duplicates for free, so you know whether there's anything worth negotiating.
</div>

<h2 id="math">3. The math on three bill sizes</h2>

<p>Here is what each service would charge on three example bills, using only the published prices above. The savings amounts are examples to show the math, not promises of what any service will get you.</p>

<div class="case-study">
    <h3>Example 1: $2,400 ER bill, reduced by $900</h3>
    <p>Goodbill: 20% of $900 = <strong>$180</strong>. CareRoute: 18%&ndash;25% = <strong>$162&ndash;$225</strong>. Resolve: takes bills of $5,000 or more only, so <strong>not an option</strong>. BillKarma: flat fee for a $1,000&ndash;$5,000 bill = <strong>$49</strong>.</p>
    <p>You keep $851 with BillKarma and $720 with Goodbill. <strong>On small bills, many advocate services won't take the case, and fees take a bigger share of the savings.</strong></p>
</div>

<div class="case-study">
    <h3>Example 2: $12,000 surgery bill, reduced by $4,000</h3>
    <p>Goodbill: 20% = <strong>$800</strong>. CareRoute: <strong>$720&ndash;$1,000</strong>. Resolve: 25% = <strong>$1,000</strong>. BillKarma: flat fee for a $5,000&ndash;$20,000 bill = <strong>$99</strong>.</p>
    <p>The gap is $700&ndash;$900. A human negotiator is worth that only if they would get a bigger reduction than a written dispute would.</p>
</div>

<div class="case-study">
    <h3>Example 3: $40,000 inpatient bill, reduced by $15,000</h3>
    <p>Goodbill and CareRoute hit their caps = <strong>$1,000</strong>. Resolve: 10% is $1,500, but with savings under $25,000 its minimum fee is the lower of $2,500 or half the savings = <strong>$2,500</strong>. BillKarma = <strong>$149</strong>.</p>
    <p>On a bill this size, a capped contingency service is a reasonable choice if you want someone on the phone. An extra few thousand dollars of reduction would cover the fee.</p>
</div>

<div class="key-takeaway">
    <strong>Know the fair price first.</strong> Use our <a href="/calculator">free calculator</a> to see what Medicare pays for the services on your bill &mdash; it's the number negotiators anchor on, and you can use it too.
</div>

<h2 id="example-bill">4. What a negotiator is actually looking for</h2>

<p>Every service, paid or free, starts with the itemized bill (the version that lists every charge and its billing code). Most of the savings come from two things: errors and prices far above what Medicare pays for the same code.</p>

<div class="bill-example">
    <div class="bill-header">Itemized ER bill &mdash; example</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency visit, level 4</span>
        <span>$1,380</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive metabolic panel</span>
        <span>$310</span>
    </div>
    <div class="line-item error">
        <span>80053 &mdash; Comprehensive metabolic panel &nbsp; &#10060; <em>Same test, same day: likely duplicate</em></span>
        <span>$310</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete blood count</span>
        <span>$140</span>
    </div>
    <div class="line-item flagged">
        <span>71046 &mdash; Chest X-ray, 2 views &nbsp; &#9888; <em>Compare to the Medicare rate for this code</em></span>
        <span>$260</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$2,400</span>
    </div>
</div>

<p>Removing the duplicate is a $310 fix that needs one letter, not a negotiator. The price questions take more pushing. See <a href="/guides/common-hospital-billing-errors/">common hospital billing errors</a> and <a href="/guides/medical-bill-audit-checklist/">the audit checklist</a> to find these yourself.</p>

{_embed(mode="markup", title="Is this charge fair?", subtitle="Enter a code and the amount charged to compare it to Medicare.", height="420")}

<h2 id="which">5. Which option fits your bill</h2>

<table>
    <thead>
        <tr><th>Your situation</th><th>Start with</th></tr>
    </thead>
    <tbody>
        <tr><td>Income near or below the hospital's limit, nonprofit hospital</td><td>Financial assistance (charity care). It's free and can erase the bill.</td></tr>
        <tr><td>Bill under about $5,000 with errors or high prices</td><td>Do it yourself, or a flat-fee written dispute</td></tr>
        <tr><td>Bill of $5,000&ndash;$20,000</td><td>Written dispute first; a capped contingency service if the hospital won't move</td></tr>
        <tr><td>Bill over $20,000, or insurance denials mixed in</td><td>A human advocate on contingency with a cap is often worth it</td></tr>
        <tr><td>Already in collections</td><td>A <a href="/guides/debt-validation-letter-medical-debt/">debt validation letter</a> within 30 days of the first notice</td></tr>
    </tbody>
</table>

<p>BillKarma doesn't negotiate by phone or handle insurance denials. If your case needs that, a human advocate is the better fit. Our guide to <a href="/guides/medical-billing-advocate/">medical billing advocates</a> explains how to choose one.</p>

<div class="key-takeaway">
    <strong>See how your hospital prices.</strong> Check our <a href="/hospitals/">hospital directory</a> &mdash; every hospital's billing phone number, financial assistance rules and how its prices compare to Medicare.
</div>

<h2 id="free">6. Free options to try first</h2>

<ol>
    <li><strong>Ask for financial assistance.</strong> Nonprofit hospitals must publish a financial assistance policy under <a href="https://www.irs.gov/charities-non-profits/financial-assistance-policies-faps" target="_blank" rel="noopener">IRS rules (Section 501(r))</a>. See <a href="/guides/hospital-financial-assistance-charity-care/">who qualifies</a>.</li>
    <li><strong>Get the itemized bill.</strong> Use our <a href="/guides/how-to-get-itemized-hospital-bill/">free request letter</a>.</li>
    <li><strong>Dispute errors in writing.</strong> Our <a href="/guides/medical-bill-dispute-letter/">dispute letter template</a> covers duplicates, wrong quantities and services you didn't get.</li>
    <li><strong>Ask for a prompt-pay or self-pay discount.</strong> The <a href="/guides/medical-bill-negotiation-script/">negotiation script</a> has the exact words.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much do medical bill negotiation services charge?</h3>
        <p>Most charge 10% to 25% of what they save you. Goodbill charges 20% capped at $1,000, CareRoute 18% to 25% capped at $1,000, and Resolve 25% on bills of $5,000 to $15,000 with a minimum fee of up to $1,000. BillKarma charges a flat $29 to $149 based on bill size.</p>
    </div>
    <div class="faq-item">
        <h3>Is a medical bill negotiator worth it for a small bill?</h3>
        <p>Often not. Resolve only takes bills of $5,000 or more. On a $2,400 bill reduced by $900, Goodbill's 20% fee would be $180, while a flat-fee written dispute is $49. Doing it yourself costs nothing but your time.</p>
    </div>
    <div class="faq-item">
        <h3>Do I have to pay if they don't lower my bill?</h3>
        <p>Not with the major services. Goodbill, CareRoute and Resolve charge only when they find savings, and Resolve refunds its deposit. BillKarma refunds its flat fee in full if the bill isn't reduced within 45 days.</p>
    </div>
    <div class="faq-item">
        <h3>What's the difference between a flat fee and a contingency fee?</h3>
        <p>A contingency fee is a percentage of the savings, so it grows as the savings grow. A flat fee stays the same. Flat fees win on small and mid-size bills; a capped contingency service can make sense on very large, complicated ones.</p>
    </div>
    <div class="faq-item">
        <h3>Is there a free way to get a hospital bill reduced?</h3>
        <p>Yes. Nonprofit hospitals must offer financial assistance to patients under their income limits, and the nonprofit Dollar For helps people apply for free. You can also <a href="/guides/how-to-dispute-a-medical-bill/">dispute the bill yourself</a>.</p>
    </div>
    <div class="faq-item">
        <h3>How long does medical bill negotiation take?</h3>
        <p>Resolve says the average case takes about 4 months, and CareRoute quotes 4 to 8 weeks. BillKarma sends the dispute right away and follows up on days 7, 14, 30 and 45.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://resolvemedicalbills.com/faqs/how-much-does-it-cost-to-work-with-resolve" target="_blank" rel="noopener">Resolve: How much does it cost to work with Resolve? (checked Nov 2026)</a></li>
    <li><a href="https://www.resolvemedicalbills.com/how-we-work" target="_blank" rel="noopener">Resolve: How we work, services and bill sizes covered (checked Nov 2026)</a></li>
    <li><a href="https://www.resolvemedicalbills.com/faq" target="_blank" rel="noopener">Resolve: FAQ, average time to resolve a bill (checked Nov 2026)</a></li>
    <li><a href="https://help.goodbill.com/en/articles/254209" target="_blank" rel="noopener">Goodbill: How much does it cost? (checked Nov 2026)</a></li>
    <li><a href="https://www.careroute.ai/bill-defense" target="_blank" rel="noopener">CareRoute: Bill Defense pricing (checked Nov 2026)</a></li>
    <li><a href="https://www.careroute.ai/bill-defense/compare-medical-bill-negotiation-services" target="_blank" rel="noopener">CareRoute: Medical bill negotiation services compared, turnaround times (June 2026)</a></li>
    <li><a href="https://triagecancer.org/dollar-for-charity-care" target="_blank" rel="noopener">Triage Cancer: Dollar For helps with hospital bills through charity care</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/financial-assistance-policies-faps" target="_blank" rel="noopener">IRS: Financial assistance policies for nonprofit hospitals (Section 501(r))</a></li>
</ul>
""",
})
