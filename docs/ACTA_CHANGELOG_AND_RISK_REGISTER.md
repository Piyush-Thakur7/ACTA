# ACTA by Resence — Comprehensive Changelog & Risk Register (v2.6 Upgrade)
**Document Classification:** Confidential & Internal Engineering Standard • Version 2.6  
**Parent Entity:** Resence (`https://resence.in`) | **Product:** ACTA (`https://acta.resence.in`)  
**Tagline:** *"Small Acts. Big Impact."*  
**Founder & Product Architect:** Piyush Singh (18, BCA 2nd Year, GL Bajaj Institute of Management)  
**Target Conclave:** Bharat Udyam Sangam 2026 (GL Bajaj Center for Research and Incubation - GLBCRI)

---

## 1. Material Change Log (v2.0 / v2.5 → v2.6 Revised)

| Section / Topic | Previous Text / Flaw (v2.0 / v2.5) | Material Revision & Justification in v2.6 | Status / Classification |
| :--- | :--- | :--- | :--- |
| **Financial Allocation Math** | Described "90% direct cause + 10% NGO ops + 5% ACTA fee" = **105% mathematical contradiction**. | **Corrected Everywhere to Non-Contradictory Allocation:**<br>• ACTA proposed platform service fee: **5% (₹5.00)**.<br>• Eligible NGO allocation: **95% (₹95.00)**.<br>• NGO operational allowance: **10% of NGO's ₹95 = ₹9.50** (only if campaign terms/donor restrictions allow).<br>• Direct campaign cause execution: **90% of NGO's ₹95 = ₹85.50**.<br>• Labeled clearly as a *proposed accounting illustration*, not confirmed legal settlement. | **Corrected & Locked** |
| **Revenue & Continuity Reserve** | No reserve policy existed; implied ACTA might spend all fee revenue immediately or make open-ended guarantees. | **Designed Proposed Internal Continuity Reserve:**<br>• ACTA records earned service fees separately from donation flows.<br>• Illustrative reserve scenario: 20% of fee revenue allocated toward business continuity & emergency replacement execution.<br>• Explicit rule: Restricted donations or other NGO funds are **NEVER** used as undisclosed reserve substitutes.<br>• No open-ended guarantee beyond approved reserves. | **New Policy Design** |
| **NGO Default & Replacement Delivery** | Rigid claim that an NGO would simply be "blacklisted" and 100% refunded, or vague replacement promises. | **Designed 12-Step Replacement & Delivery-Continuity Workflow:**<br>• Complete state machine (`ON_TRACK` to `COMPLETED` / `REFUNDED`).<br>• Distinct tiers for ordinary delays, insufficient evidence, negligence, contractual breach, and suspected fraud.<br>• Donor transparency: donors informed of replacement NGO, revised timeline, and funding source. | **Operational Standard** |
| **Donor Communication & Apologies** | No standardized templates; risk of panic or admitting unverified legal facts during delays. | **7 Empathy-First, Factual Communication Templates:**<br>• Delivery delayed, warning issued, NGO unresponsive, replacement NGO selected, replacement completed, campaign cancelled/refunded, suspected misuse under review.<br>• Strict guardrail: Do not falsely accuse NGOs before formal review; protect minor/beneficiary privacy. | **Communication Standard** |
| **Escrow & Payment Legality** | Claimed an "Escrow Vault" and "Nodal Accounts" were active partnerships; promised automatic wallet refunds. | **Reclassified as Proposed Architecture Awaiting External Approval:**<br>• Created an explicit 10-point checklist for review by an Indian legal counsel, chartered accountant, and payment provider.<br>• Clarified ACTA is a **Technology-as-a-Service (SaaS)** platform, not a bank or fund-holding trust.<br>• Wallet refund promise replaced with provider-compatible gateway reversals pending legal approval. | **Compliance Realism** |
| **Verification & AI Capabilities** | Claimed "guaranteed fraud detection" via AI and "immutable database records". | **Reclassified AI & Telemetry as Assistive Signals:**<br>• Gemini Vision OCR and video hashes treated as *signals*, not infallible proof.<br>• Mandatory **Human-in-the-Loop** verification with the **Two-Person Rule** for disbursements >₹25,000.<br>• Replaced absolute claims with testable verification protocols. | **Technical Integrity** |
| **Market Data & Statistics** | Quoted 67.5% donor trust deficit, TAM/SAM/SOM, and 20 NGOs as settled facts. | **Grounded as Research Hypotheses & Pilot Scenarios:**<br>• 67.5% marked as an indicative student/urban survey hypothesis.<br>• Pilot capacity modeled for 1 Campus (GL Bajaj) + 1-2 curated local NGOs (not a fictitious 20-NGO national network).<br>• Projections labeled as financial planning scenarios. | **Factual Grounding** |
| **Gamification & Status Incentives** | Rewarded spending alone (₹1 = 10 XP), creating a "wealth game" / pay-to-win dynamic. | **Balanced Action-Based Gamification:**<br>• XP awarded for verifying proof (+20 XP), weekly streaks (+150 XP), and campus volunteering (+250 XP).<br>• Individual donation totals kept strictly private to eliminate social embarrassment and wealth comparisons. | **Ethical Product Design** |
| **Execution Deadlines & SLAs** | Enforced a rigid, unworkable 96-hour deadline across all cause types with zero exceptions. | **Dynamic SLAs by Campaign Category:**<br>• Food distribution: 96h.<br>• School kits / educational drives: 7–10 days.<br>• Tree plantation: 10 days.<br>• Emergency trauma surgery: 24–48 hours.<br>• Formal in-app extension protocol with photo justification. | **Operational Flexibility** |
| **Founder History & Evolution** | Implied the complete ecosystem (AI, Escrow, Guilds) existed from Day 1. | **Truthful Historical Progression:**<br>• Began with ground volunteer recruitment for animal feeding and slum drives.<br>• Evolved into a platform after encountering liability and coordination bottlenecks.<br>• Features built progressively over 1 year of prototyping. | **Historical Honesty** |

---

## 2. ACTA Comprehensive Risk Register

| Risk ID | Risk Description | Category | Inherent Severity | Likelihood | Mitigation Strategy & Operational Safeguard | Residual Risk | Owner |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **RSK-01** | **Payment Aggregator Split Settlement Disapproval**<br>Selected payment gateway refuses automated 5%/95% split settlement for micro-donations. | Regulatory / Fintech | **Critical** | Medium | Maintain fallback billing workflow: direct NGO payment processing with monthly or post-campaign tech platform service invoicing. Review Razorpay Route and Cashfree Split terms with qualified legal counsel. | Moderate | Product Architect & Legal Counsel |
| **RSK-02** | **NGO Milestone Delivery Breach / Abandonment**<br>Partner NGO receives funds or starts campaign but fails to deliver supplies or submit proof. | Operational / Ground | **High** | Medium | Implement the 1 Lead + 2 Substitutes roster, dynamic SLAs, 48h warning escalation, and the 12-Step Default & Replacement Workflow funded via the Continuity Reserve where permitted. | Low | Ground Ops Lead |
| **RSK-03** | **Fabricated or Reused Verification Evidence**<br>Field volunteer attempts to upload stock footage, old video clips, or manipulated receipts. | Trust & Safety | **High** | Low | Gallery upload permanently disabled (WebRTC in-app camera only). Embedded NTP timestamp and GPS coordinates. Gemini Vision frame hashing + mandatory human reviewer inspection before payout. | Low | Compliance Reviewer |
| **RSK-04** | **Regulatory Misclassification (Unregulated Intermediary)**<br>Authorities classify ACTA as an unregulated payment aggregator or donation-holding charity. | Regulatory / Legal | **Critical** | Low | Clearly position ACTA as a Technology-as-a-Service (SaaS) provider. Ensure donor funds flow directly to eligible NGOs. Execute formal legal review of terms and merchant agreements prior to live launch. | Low | Legal Advisor |
| **RSK-05** | **DPDP Act 2023 Violation (Minor Privacy)**<br>Unauthorized publication of identifiable facial footage of children or distressed beneficiaries. | Legal / Privacy | **High** | Low | Automated MediaPipe / OpenCV Gaussian blur filter for minors (<18) applied by default before public archive ingestion. Mandatory consent protocols in partner NGO agreements. | Low | Tech Lead & Data Protection Officer |
| **RSK-06** | **Student Donor Churn After First Micro-Donation**<br>Students donate ₹10 once but do not return due to lack of collegiate momentum. | Product / Growth | **Medium** | Medium | Deploy Institutional Campus Guilds, inter-hostel clan leaderboards, weekly streak XP boosts, and verifiable YouTube proof links delivered directly to donor inboxes. | Low | Campus Community Lead |
| **RSK-07** | **Volunteer Field Liability & Accidents**<br>Field volunteer injured during disaster relief or food distribution, exposing platform to claims. | Legal / Safety | **Critical** | Low | Platform never recruits or manages field volunteers directly. Partner NGO assumes 100% legal, physical, and medical liability under signed institutional MoUs. Execution limited to daylight hours. | Low | Legal Counsel |
| **RSK-08** | **Negative Public Perception of 5% Tech Service Fee**<br>Donors or student critics perceive the 5% platform fee as siphoning charity funds. | Public Relations | **Medium** | Low | Radical upfront transparency: Disclose the fee before checkout. Educate that 0% MDR on UPI saves 2-3% compared to credit cards, and the 5% fee funds server bandwidth, AI audits, and ground verification. | Low | Founder & Communications |

---

## 3. Product Development Status Classification Guide

To preserve absolute integrity in all investor decks, conclave pitches, and engineering specifications, all product capabilities are strictly mapped to the following 5 statuses:

1. **Implemented & Tested (Live in Prototype):**
   - Mobile-First Web Client (`acta.resence.in` / `resence.in`)
   - 3-Pillar Clean Dashboard UX (Proof Archive, XP Rings, Guild Board)
   - 7 Curated Cause Cards with Dynamic Funding Progress Bars
   - Client-Side ₹10 UPI Intent trigger simulation
   - Gamification Engine (Balanced Action XP formulas & 10-Level progression curve)
   - Student Impact Planner conversational UI.

2. **Partially Implemented (Under Engineering Validation):**
   - Webhook listener with HMAC SHA-256 validation & Redis 24h event deduplication
   - WebRTC in-app camera stream with dynamic HTML5 canvas telemetry watermark
   - YouTube Data API v3 unlisted upload integration
   - Gemini Vision receipt OCR parser & perceptual frame hash comparator.

3. **Designed But Not Implemented (Detailed in PRD Specs):**
   - Offline IndexedDB 2MB video chunking & Service Worker Background Sync API
   - Automated MediaPipe Gaussian face-blurring pipeline
   - Top 25 City & National Leaderboard Redis Sorted Sets (`zset`) caching layer
   - Automated 12-Step Default & Replacement execution workflow.

4. **Proposed & Awaiting External Approval (Fintech / Legal Roadmap):**
   - Payment provider automated 5%/95% split settlement (Razorpay Route / Cashfree Split)
   - Dedicated Scheduled Commercial Bank Virtual Escrow / Nodal Account integration
   - Automated in-app virtual wallet refund routine
   - Institutional Service Agreement MoUs with Greater Noida non-profits.

5. **Hypotheses Awaiting Market Validation (Pilot Objectives):**
   - 67.5% donor trust deficit in collegiate demographics (to be measured via GL Bajaj pilot)
   - ₹10 micro-giving repeat frequency (target: 35%+ monthly retention)
   - Campus Guild competitive viral loop across hostel blocks
   - NGO willingness to accept audited 90/10 operational split and 96-hour execution SLAs.
