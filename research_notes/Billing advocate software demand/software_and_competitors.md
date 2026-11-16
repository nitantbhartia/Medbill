# Software Used by US Patient/Medical Billing Advocates, and Vendors Selling to Them

Research date: 2026-11-16. Method: web search plus a few fetches. Several primary sites could not be fetched from this session because their domains are not on the network allowlist (vitafyhealth.com, geekwire.com, trysignalbase.com), so some findings rely on search snippets and aggregators. Reliability is flagged per item.

## Q1. What tools do advocates report using (generic, practice management/CRM, niche)?

### Takeaway
I found no survey or primary source listing advocates' actual tool stack. The guidance that does exist tells independent advocates they are usually not HIPAA-covered entities and can run on standard business tools: paid Google Workspace, cloud storage with 2FA, and a password manager. HIPAA email or messaging tools (Paubox, Spruce) are sold to clinical practices, not advocates. That points to a stack of generic tools plus spreadsheets, but it is not confirmed.

### Cited Findings
- An advocate-facing HIPAA guide (Tennessee Health Advocates) says independent patient advocates are generally **not HIPAA-covered entities**. It says most can protect client data with "standard business-level tools with proper security settings": paid Google Workspace email, cloud storage with two-factor authentication, and a password manager. — [Tennessee Health Advocates](https://tennesseehealthadvocates.com/independent-patient-advocate-hipaa-guide/)
- Paubox markets HIPAA-compliant email to patient advocacy organizations specifically. It encrypts outbound email by default and integrates with Google Workspace and Microsoft 365. This is vendor content. — [Paubox blog](https://www.paubox.com/blog/hipaa-compliant-email-in-patient-advocacy-organizations); [Paubox](https://www.paubox.com/)
- Patient-communication platforms often recommended to small practices (Spruce, Updox, OhMD) are built mainly for clinical practices, not advocates. — [patient-protect.com (2026)](https://patient-protect.com/post/top-7-hipaa-compliant-patient-communication-tools-2026)
- Greater National Advocates (GNA) runs a member platform branded "Patient Advocacy 360°" with a "Tools and Resources for Getting Started" section. A member "exclusive deals" area was marked "Coming Soon", and no named software partners were visible in results. — [GNA (gnanow.org)](https://gnanow.org/users/3799)
- Generic case-management and CRM tools that appear on "advocate practice case management" lists include Salesforce Health/Nonprofit Cloud, ETO Software, LegalServer, PlanStreet and Carepatron. These lists target social-work and nonprofit advocacy, not billing advocates, and are affiliate-style content. — [socialworkportal.com](https://www.socialworkportal.com/top-advocate-practice-case-management-software/); [casemanagementhub.org](https://casemanagementhub.org/software-for-health-advocacy-and-disease-support-nonprofits/)

### Inferences
- Because advocates are generally not covered entities, a vendor cannot use "HIPAA compliance" as a strong selling point to them. Confidentiality, organization and time savings are probably stronger hooks.
- No advocate association appears to endorse a vertical software vendor, which suggests no dominant incumbent.

### Gaps
- I found no survey, Reddit thread or podcast quote with advocates naming their tools: Google Sheets, Excel, QuickBooks, Trello, Notion, SimplePractice, Practice Better, HoneyBook, Dubsado, eFax or Hushmail. Primary interviews would be needed.
- I could not access the member-only GNA, PACB or NAHAC resource pages.

## Q2. Vendors built for patient/billing advocates, and adjacent consumer/B2B bill-review companies

### Takeaway
Almost no vendor sells software to independent billing advocates as its customer. The one advocate-labeled product found is VSuite by Vitafy, a HIPAA case-management tool with a page "for healthcare advocates"; its pricing and traction were not verifiable. Nearly all funded startups in this space sell **directly to consumers** (as a service or AI tool), **to employers, plans or TPAs** (Goodbill), or **to providers** (Fight Paperwork). That puts them in competition with advocates rather than serving them.

### Cited Findings

**Advocate-facing software**
- **VSuite (Vitafy Health):** markets a "for healthcare advocates" HIPAA-compliant case management system with notes, file uploads and case collaboration, positioned as cheaper than enterprise care management. The page could not be fetched; pricing, customers and launch date are unknown. — [Vitafy VSuite](https://www.vitafyhealth.com/vsuite/for-healthcare-advocates)
- I found nothing named "Health Advocate Software" or any AdvoConnection software product. AdvoConnection did not appear in any results (see Gaps).

**AI appeal and bill-review tools, mostly consumer-facing (2024–2026)**
- **Claimable:** launched October 2024 with AI-generated insurance appeal letters, founded by Warris Bokhari. Most appeals cost **$39.95 plus shipping** (2024–2025 reporting). It raised a seed round from Walkabout Ventures and Humanrace Capital (amount undisclosed) and had about 11 employees. It claims "hundreds" of appeals filed and an ~85% overturn rate (self-reported). It also runs a free program for PANS/PANDAS families. Customer: **consumers**. — [GlobeNewswire, Oct 2, 2024](https://www.globenewswire.com/news-release/2024/10/02/2956879/0/en/Claimable-Launches-First-Ever-AI-Powered-Appeals-Platform-to-Fight-Unjust-Healthcare-Denials.html); [Healthcare Brew, Dec 17, 2024](https://www.healthcare-brew.com/stories/2024/12/17/startup-appealing-insurance-denials-patients-behalf); [Business Insider via AOL](https://www.aol.com/news/ceo-using-ai-fight-insurance-145418263.html)
- **Counterforce Health** (Raleigh/RTP, NC; tied to CareYaya, co-founder Neal Shah): a **free** AI appeal-letter generator for patients, caregivers and small clinics. Beta launched January 2025 and "thousands" had used it by 2025. It is funded by grants: CBS17 reports $280K in grants, and other coverage cites a $2.47M PennAITech grant. Future clinic subscription fees have been floated. Customers: consumers and clinics, free. — [CBS17](https://www.cbs17.com/news/local-news/wake-county-news/raleigh-organization-helps-thousands-of-americans-appeal-health-insurance-denials-using-ai/); [PitchBook](https://pitchbook.com/profiles/company/969417-28); [Stateline, Nov 20, 2025](https://stateline.org/2025/11/20/patients-deploy-bots-to-battle-health-insurers-that-deny-care/); [Managed Healthcare Executive, Oct 6, 2025](https://managedhealthcareexecutive.com/view/power-to-the-patients-ai-for-fighting-insurance-denials). The $280K and $2.47M figures conflict, or may cover different periods.
- **Fight Health Insurance / Fight Paperwork** (Holden Karau): an **open-source, free** appeal generator for patients. The paid "Fight Paperwork" professional version (beta March 2025) is sold to **medical practices, health systems and pharma patient-access teams**, not advocates. No public pricing was found. — [PRWeb](https://www.prweb.com/releases/ai-tool-fight-health-insurance-goes-viral-empowering-everyone-to-challenge-denied-claims-302325638.html); [Managed Healthcare Executive, Oct 2025](https://managedhealthcareexecutive.com/view/power-to-the-patients-ai-for-fighting-insurance-denials)
- **Avelis Health:** YC Summer 2025, **$500K** raised. Its AI agents audit medical bills, find errors and negotiate with providers. Customer: consumers. — [People of Color in Tech, Jun 26, 2025](https://peopleofcolorintech.com/articles/y-combinator-invests-500k-in-ai-startup-helping-americans-save-money-on-medical-bills/); [noirpress](https://noirpress.org/avelis-health-launches-ai-powered-medical-bill-auditing-platform/)
- **Medbill AI** (legal entity Medical Bill AI Labs Inc.): a **$16.3M seed (July 2024)** from RRE Ventures, Red Sea Ventures and Factorial Capital, to "automate medical billing for consumers". Aggregators disagree: $16.25M per BounceWatch, and $17M across 11 rounds per Wellfound. Note the name overlap with this project ("Medbill"). — [VCBacked](https://www.vcbacked.co/company/medbill-ai); [Fundz](https://app.fundz.net/fundings/medical-bill-ai-labs-funding-round-7f9b27); [BounceWatch](https://bouncewatch.com/company/medbill-ai); [Wellfound](https://wellfound.com/company/medbill-ai/funding)
- **Sheer Health:** a consumer app that automates bill review, claim filing and insurer follow-up. PitchBook shows a **$13M Series A (Dec 2023)** and about $16.5M total. Its business model is unclear: one promotional source says it is free and monetized through partnerships, while another mentions membership plans. — [PitchBook](https://pitchbook.com/profiles/company/516159-55); [App Store](https://apps.apple.com/us/app/-/id6447633462); [Gerald guide (promotional)](https://joingerald.com/learn/financial-wellness/sheer-health-guide)

**Bill negotiation services (human advocates, consumer or B2B)**
- **Goodbill** (Seattle): raised **~$2M in April 2024** (Founders' Co-op, Maveron, Liquid 2), bringing its total to **$5.3M**. It is expanding "cost containment for plans and TPAs", which moves its focus to self-funded plans and TPAs. — [Goodbill blog](https://www.goodbill.com/blog/news-goodbill-raise-2m-funding-expands-cost-containment-plans-tpas); [GeekWire, 2024](https://www.geekwire.com/2024/goodbill-raises-2m-and-expands-customer-base-to-unearth-and-challenge-medical-billing-errors/); [FinSMEs, Apr 2024](https://www.finsmes.com/2024/04/goodbill-raises-2m-in-funding.html)
- **Resolve Medical Bills** (Hanover, NH; founded 2019): **$3.3M seed led by AlleyCorp (July 2022)**. It assigns a human advocate. Third-party reported terms (2026): bills of about $5K and up, a $249 deposit plus 25% of savings for $5–15K bills, and a $499 deposit plus 10% above $15K. It claims average reductions "up to 60%". It has partnered with StretchDollar, a small-business benefits provider. — [Seedtable](https://seedtable.com/companies/resolve-medical-bills); [Resolve FAQ](https://www.resolvemedicalbills.com/faq); [mediloop comparison (competitor, biased)](https://mediloop.ai/blog/mediloop-vs-resolve)
- **CoPatient** (Boston): raised **$3.6M in 2014** and took a 35% cut of identified savings. Crunchbase lists it as "Active", but I found no 2023–2026 activity. — [GeekWire 2014](https://www.geekwire.com/2014/copatient-raises-3-6m/); [Crunchbase](https://www.crunchbase.com/organization/copatient)
- **Medical Bill Gurus** (Denver): a contingency-fee billing advocacy firm (service, not software), listed as active. — [Crunchbase](https://www.crunchbase.com/organization/medical-bill-gurus); [BBB](https://www.bbb.org/us/co/denver/profile/medical-billing/medical-bill-gurus-1296-90257359)
- New 2026 AI entrants publish comparison pages: mediloop.ai, careroute.ai and CoveredUSA. Their content is self-interested. — [mediloop](https://mediloop.ai/blog/best-medical-bill-negotiation-services); [CoveredUSA](https://coveredusa.org/en/blog/medical-bill-negotiation-services-compared); [CareRoute](https://www.careroute.ai/bill-defense/compare-medical-bill-negotiation-services)

### Inferences
- The funded money (Medbill AI $16.3M, Sheer $16.5M, Goodbill $5.3M, Resolve $3.3M) is going to **consumer-direct or payer-side** models, so these companies are substitutes for independent advocates, not suppliers to them.
- Free AI appeal tools (Counterforce, Fight Health Insurance) push the price of an appeal letter toward $0, and Claimable has anchored it at $39.95. An advocate-facing appeal generator therefore cannot charge much for letters alone. Its value would have to come from bill audit, case workflow and time saved.
- The advocate-software niche looks largely empty. That could be an opportunity, or a sign the market is too small or fragmented to support a funded vendor.

### Gaps
- I found nothing on "Justpaid" or "Health Advocate Software" as advocate-software companies.
- I found no evidence of an AdvoConnection software product.
- VSuite pricing and traction are unknown because the page could not be fetched.
- Claimable's seed amount and Sheer Health's current pricing are unknown.
- Medbill AI's product and current traction are unverified, since the press release was not reachable.

## Q3. Advocate-facing tools for CPT/Medicare-rate lookup, bill auditing and appeals, and what they cost

### Takeaway
Advocates appear to rely on free consumer tools such as FAIR Health Consumer and the Medicare fee schedule, plus paid coder references (Find-A-Code, AAPC Codify) priced at roughly $45–66 per month. None of these is marketed to advocates specifically. No evidence was found of a tool that combines lookup, audit and appeal for advocates.

### Cited Findings
- **FAIR Health Consumer** cost lookup is free, and advocates and patients use it to compare billed charges to typical charges. FAIR Health publishes a guide on using its estimates to negotiate. — [FAIR Health Consumer](https://www.fairhealthconsumer.org/insurance-basics/your-costs/negotiating-your-costs); [FAIR Health PDF](https://www.fairhealthprovider.org/download/your-costs/Using%20FAIR%20Health%20Cost%20Estimates%20to%20Negotiate%20the%20Costs%20of%20Care.pdf)
- FAIR Health's licensed data for small practices (surprise-billing context) costs **$250 per clinical specialty plus $60 per extra user**. It is sold to providers, not advocates. Date unclear. — [FH Orders](https://surprisebilling.fairhealth.org/)
- **Find-A-Code:** Essentials, Professional and Facility plans are sold monthly or annually, per user. A third-party listing cites about **$45 per month** for a basic plan (date uncertain). A student "Essentials" special was $4.95 per month. It also has a "Compare-A-Fee" UCR/fee schedule comparison feature relevant to bill audit. — [Find-A-Code FAQ](https://www.findacode.com/account/faqs/how-much-does-this-service-cost-28500.html); [intuitionlabs listing](https://intuitionlabs.ai/software/medical-coding-computer-assisted-coding-cac/icd-10-cmpcs-encoders/find-a-code); [Find-A-Code Compare-A-Fee](https://www.findacode.com/news/compare-a-fee-customized-fee-schedules-analysis-comparison-ucr.html)
- **AAPC Codify:** tiers reported at **$10–54 per month for members and $15–66 for non-members**. Complete Coder is $54 or $66 per month on an annual plan (about $648–792 per year). The CPT Advanced Coding Pack add-on is $299 for members or $349 for non-members per year. Third-party figures conflict; confirm on aapc.com. — [hccbuddy comparison](https://hccbuddy.com/compare/hcc-buddy-vs-codify); [AAPC add-on page](https://www.aapc.com/codify/cpt-adavanced-coding-pack.aspx)
- Advocate pricing context: hiring an advocate to handle denials costs about **$80–150 per hour**. — [Managed Healthcare Executive, Oct 2025](https://managedhealthcareexecutive.com/view/power-to-the-patients-ai-for-fighting-insurance-denials)

### Inferences
- An advocate who wants to audit bills against Medicare rates likely pays $0, using FAIR Health Consumer and the CMS PFS lookup, or about $500–800 per year for a coder tool built for provider-side coders. A purpose-built audit tool would compete with that spend.

### Gaps
- I found no source showing what share of advocates subscribe to Find-A-Code, Codify or Healthcare Bluebook. I found no current Healthcare Bluebook pro pricing; it is sold to employers.
- I found no advocate-specific discounts from AAPC or Find-A-Code tied to PACB or GNA membership.

## Q4. Failed or shut-down startups in this space, and why

### Takeaway
I found no documented failure of a startup selling software *to advocates*. Consumer-facing bill startups have failed or pivoted for three reasons: provider billing offices refusing to deal with third parties, weak consumer economics, and the move toward hospitals or employers as payers.

### Cited Findings
- **Remedy** (San Francisco, consumer medical bill review): failed because providers would not cooperate. Billing offices refused to release records to third parties even though patients had a legal right to them. — [Fast Company, 2017](https://www.fastcompany.com/40483774/remedy-wanted-to-cut-peoples-medical-bills-but-the-health-care-system-wouldnt-let-it)
- **Simplee:** started as a "Mint for healthcare" consumer app ($6M Series A), then pivoted to selling software to hospitals. — [TechCrunch](https://techcrunch.com/?p=551531); [MedCity News, Nov 2017](https://medcitynews.com/2017/11/medical-billing-startups/)
- **DisputeBills** (Chicago, consumer bill disputes): ceased operations, citing "the challenges of today's healthcare climate". — [MedCity News, 2017](https://medcitynews.com/2017/11/medical-billing-startups/)
- **BillFixers** (consumer bill negotiation, not only medical): acquired by Experian in 2022. — [Wikipedia](https://en.wikipedia.org/wiki/BillFixers)
- **Goodbill** shifted emphasis to self-funded plans and TPAs in 2024 (see Q2). This fits the pattern of consumer-to-B2B moves. — [Goodbill blog](https://www.goodbill.com/blog/news-goodbill-raise-2m-funding-expands-cost-containment-plans-tpas)

### Inferences
- The repeated consumer-to-B2B pivots (Simplee to hospitals, Goodbill to plans and TPAs) suggest consumers are a hard paying customer. Independent advocates are a small, fragmented B2B segment, and no funded company appears to have targeted them. That fits a market too small for VC but possibly workable for a lean SaaS.

### Gaps
- I found no post-mortem of any advocate-targeted software product.
- These failure examples date from 2014–2018. I found no 2023–2026 shutdowns of AI bill-review startups.
