# ACTA by Resence — 10-Point Legal, Regulatory & Fintech Review Checklist
**Document Classification:** Legal & Financial Governance Standard • Version 2.6  
**Parent Entity:** Resence (`https://resence.in`) | **Product:** ACTA (`https://acta.resence.in`)  
**Tagline:** *"Small Acts. Big Impact."*  
**Founder & Product Architect:** Piyush Singh (18, BCA 2nd Year, GL Bajaj Institute of Management)  
**Target Conclave:** Bharat Udyam Sangam 2026 (GL Bajaj Center for Research and Incubation - GLBCRI)  
**Intended Reviewers:** Qualified Indian Corporate Advocate, Chartered Accountant (FCA), and Payment Aggregator Risk/Compliance Committee.

---

## Executive Summary & Statutory Context

ACTA by Resence is engineered strictly as a **Technology-as-a-Service (SaaS)** platform and technical intermediary. It connects institutional student communities ("Campus Impact Guilds"), verified non-governmental organizations (NGOs), and micro-donors. 

ACTA does not solicit, pool, deposit, or hold charitable donations in its own corporate or personal bank accounts. Donations are transferred directly from donors to verified recipient NGOs via RBI-authorized Payment Aggregators (PAs). For providing campaign infrastructure, real-time verification tooling, telemetry tracking, and donor communication services, ACTA earns a proposed commercial platform service fee of 5% on gross transactions.

Before initiating live commercial pilots at GL Bajaj Institute of Management and Greater Noida non-profits, this 10-point checklist must be formally evaluated and signed off by qualified legal, accounting, and banking counsel.

---

## The 10-Point Review Checklist

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   ACTA FINTECH & LEGAL GOVERNANCE GATEWAY                       │
├───────────────────────┬──────────────────────────┬───────────────────────────────┤
│ 1. Intermediary / SaaS│ 2. RBI PA Split Rules    │ 3. Section 80G Tax Reciprocity│
│ 4. GST on Tech Fees   │ 5. Escrow Nodal Custody  │ 6. NGO Master Service Agrmt   │
│ 7. Chargeback & Dispute│ 8. Continuity Reserve   │ 9. DPDP Minor & Beneficiary   │
│ 10. FCRA Ring-Fencing │                          │                               │
└───────────────────────┴──────────────────────────┴───────────────────────────────┘
```

---

### Item 1: Legal Characterization as a Technology Intermediary (SaaS), Not a Fund-Holding Charity or Financial Entity

* **Statutory Framework:** Information Technology Act, 2000 (Section 79); Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021; Reserve Bank of India (RBI) Guidelines.
* **Proposed Product Architecture:**
  - ACTA operates exclusively as a technology service provider facilitating campaign coordination, verification proof ingestion, and donor engagement analytics.
  - ACTA is neither a Section 8 charitable company nor a trust; it does not present itself as a charitable recipient.
  - ACTA holds no proprietary banking license, prepaid payment instrument (PPI) authorization, or NBFC charter.
* **Key Questions for Legal Counsel:**
  1. Does ACTA's platform architecture satisfy the "safe harbor" provisions of Section 79 of the IT Act, 2000 as a network service intermediary?
  2. Does the presentation of cause campaigns on `acta.resence.in` create any risk of constructive misrepresentation that ACTA is soliciting donations on its own behalf?
  3. What mandatory disclosures, terms of service clauses, and UI disclaimers must appear on checkout pages to establish that the donor is contracting directly with the eligible partner NGO?
* **Required Counsel Action / Artifact:** Draft Platform Terms of Use, Privacy Policy, and Intermediary Disclaimer confirming SaaS status.

---

### Item 2: Regulatory Permissibility of Automated 5%/95% Payment Split Settlement under RBI Payment Aggregator Guidelines

* **Statutory Framework:** RBI Guidelines on Regulation of Payment Aggregators and Payment Gateways (DPSS.CO.PD.No.1810/02.14.008/2019-20 dated March 17, 2020, as updated).
* **Proposed Product Architecture:**
  - Gross ₹100 donation is processed via an RBI-authorized Payment Aggregator (e.g., Razorpay Route, Cashfree Split, or Paytm Split).
  - The gateway programmatically splits the transaction: ₹5.00 settled to ACTA's corporate bank account as a platform service fee, and ₹95.00 settled into the verified partner NGO's designated bank account.
  - Funds do not route through ACTA's account before reaching the NGO.
* **Key Questions for Fintech / Legal Counsel & Aggregator:**
  1. Under RBI PA directions, can a marketplace/SaaS vendor split micro-donations where one party is a charitable non-profit and the other is a commercial tech vendor?
  2. Does facilitating split settlement require ACTA to obtain an independent Payment Aggregator license from the RBI, or is operating as an integrated merchant under an authorized PA legally sufficient?
  3. If automated split settlement is restricted for charitable donations, is a fallback model compliant where 100% (₹100) settles to the NGO, followed by ACTA issuing a monthly B2B service invoice for ₹5 per ₹100 raised?
* **Required Counsel Action / Artifact:** Written opinion on RBI PA compliance; formal written integration approval from the partner payment aggregator's compliance team.

---

### Item 3: Section 80G and 12A Income Tax Compliance for Donor Deductions

* **Statutory Framework:** Income-tax Act, 1961 (Section 80G, Section 12A/12AB, Section 115BBI); Income-tax Rules, 1962 (Rule 18AB - Form 10BE / Certificate 10BD).
* **Proposed Product Architecture:**
  - ACTA generates an automated donation acknowledgement receipt for donors.
  - Section 80G tax certificates are issued strictly in the name, PAN, and 80G registration number of the recipient NGO.
  - ACTA discloses that it cannot issue tax deductions on its own authority.
* **Key Questions for Chartered Accountant (CA):**
  1. For a gross ₹100 contribution, what is the exact amount eligible for Section 80G deduction by the donor: the full gross amount (₹100.00) or the net NGO payout (₹95.00)?
  2. Since ACTA deducts a 5% technology fee, does the NGO reporting the full ₹100 in Form 10BD and recording the ₹5 as a deductible operational/administrative expense satisfy Income Tax rules without compromising its 80G status?
  3. How should the 10% operational allowance (₹9.50) be treated under Section 11(1) of the Income-tax Act regarding application of income for charitable purposes (85% minimum application rule)?
* **Required Counsel Action / Artifact:** Formal tax advisory memo defining the exact 80G reporting workflow and automated Form 10BD data extraction pipeline.

---

### Item 4: Goods and Services Tax (GST) Applicability on Technology Fees and NGO Payments

* **Statutory Framework:** Central Goods and Services Tax Act, 2017 (CGST Act); Integrated Goods and Services Tax Act, 2017 (IGST Act); Notification No. 12/2017-Central Tax (Rate) (exemptions for charitable activities).
* **Proposed Product Architecture:**
  - Charitable donations received by registered non-profits for exempt charitable activities are generally outside GST or exempt.
  - ACTA's 5% platform service fee is commercial revenue earned for technology provision.
* **Key Questions for Chartered Accountant (CA):**
  1. Is ACTA liable to charge 18% GST (SAC code 998313 / 998439 - IT software support / online information services) on the ₹5.00 service fee, resulting in ₹5.00 + 18% GST (₹0.90) = ₹5.90, or is the ₹5 inclusive of GST?
  2. Does ACTA qualify for threshold exemption under Section 22 of the CGST Act (₹20 Lakhs aggregate annual turnover) during early pilot operations?
  3. How should B2B tax invoices from ACTA to the partner NGO be structured, and can the NGO claim Input Tax Credit (ITC) if it does not engage in taxable outward supplies?
* **Required Counsel Action / Artifact:** GST billing classification schedule, SAC code determination, and automated invoice generation template.

---

### Item 5: Escrow / Milestone Nodal Account Custody and Banking Directives

* **Statutory Framework:** RBI Master Directions on Intermediaries and Digital Payment Settlements; Section 45-IA of Reserve Bank of India Act, 1934.
* **Proposed Product Architecture:**
  - Prototype designs refer to a "Milestone Escrow Vault" where funds are held until on-ground video proof is submitted.
  - ACTA currently does not hold a dedicated banking escrow trustee arrangement.
* **Key Questions for Fintech Counsel:**
  1. Can ACTA legally instruct a payment aggregator to "hold" or "delay" settlement to an NGO's bank account beyond normal T+1 / T+2 settlement cycles without violating RBI settlement timelines?
  2. Does a conditional milestone release mechanism require a formal tripartite Escrow Agreement with a Scheduled Commercial Bank and an RBI-registered Escrow Trustee (e.g., ICICI Bank, Axis Bank, or IDBI Trusteeship)?
  3. For pilot operations, is a 2-stage milestone release (e.g. 50% mobilization advance + 50% upon proof approval) permissible via standard payment gateway delayed payout mechanisms?
* **Required Counsel Action / Artifact:** Tripartite Escrow Agreement draft or validated aggregator delayed settlement agreement.

---

### Item 6: Partner NGO Master Service Agreement (MSA) and 2-Strike Default Contract Enforceability

* **Statutory Framework:** Indian Contract Act, 1872; Specific Relief Act, 1963.
* **Proposed Product Architecture:**
  - All verified NGOs execute a legally binding Master Service Agreement (MSA) prior to launching campaigns.
  - MSA incorporates: 5% platform fee deduction, 10% operational allowance cap, category-specific execution SLAs (24h to 10 days), mandatory WebRTC proof submission, 48h cure notices, and the 2-Strike Default Policy.
  - Default clause grants ACTA contractual authorization to reassign unspent funds to an approved substitute NGO from the 1 Lead + 2 Substitutes roster.
* **Key Questions for Legal Counsel:**
  1. Is the clause authorizing ACTA to redirect unspent funds to a substitute NGO legally enforceable under the Indian Contract Act, or could the defaulting NGO claim contractual conversion?
  2. What indemnification language protects ACTA from civil or criminal claims if a partner NGO misappropriates funds after disbursement?
  3. Does the 2-Strike Default Policy require an arbitration clause under the Arbitration and Conciliation Act, 1996, and what jurisdiction should govern disputes (e.g., Gautam Buddha Nagar / Greater Noida)?
* **Required Counsel Action / Artifact:** Standardized ACTA NGO Master Service Agreement (MSA) with Schedule of Work, SLA Annexure, and Default Remedies.

---

### Item 7: Chargebacks, Payment Disputes, and Aggregator Indemnification Liabilities

* **Statutory Framework:** RBI Card and Digital Payment Guidelines; Payment Aggregator Merchant Operating Agreements.
* **Proposed Product Architecture:**
  - A donor contributes via credit card or UPI and subsequently files a chargeback or dispute claiming unauthorized transaction or non-delivery of service.
* **Key Questions for Legal Counsel & Aggregator:**
  1. Who bears ultimate liability for a disputed chargeback: ACTA, the partner NGO, or the payment aggregator?
  2. If the ₹95 has already been disbursed to the NGO and spent on physical supplies, how does ACTA recover the chargeback amount from the NGO if the aggregator debits ACTA's settlement account?
  3. Does ACTA's platform agreement require a mandatory rolling reserve (e.g., 5-10% of disbursements held for 30 days) to buffer against fraud disputes?
* **Required Counsel Action / Artifact:** Dispute Resolution & Chargeback Recovery Policy embedded in the NGO MSA and platform merchant terms.

---

### Item 8: Continuity Reserve Accounting Treatment and Corporate Governance

* **Statutory Framework:** Companies Act, 2013 (Section 135, Section 179); Institute of Chartered Accountants of India (ICAI) Accounting Standards (AS 29 - Provisions, Contingent Liabilities and Contingent Assets / Ind AS 37).
* **Proposed Product Architecture:**
  - ACTA retains a recommended 20% of its earned 5% tech fees (e.g., ₹1.00 out of ₹5.00) in an internal Continuity Reserve.
  - Reserve funds are earmarked for emergency substitute fulfillment if an NGO defaults after funds are exhausted, ensuring beneficiaries receive aid.
  - Donor funds and restricted non-profit receipts are strictly excluded from this reserve.
* **Key Questions for Chartered Accountant (CA):**
  1. How should the Continuity Reserve be reflected on Resence / ACTA's balance sheet: as an earmarked capital reserve, an operating contingency provision, or general retained earnings?
  2. Are disbursements made from the Continuity Reserve to fund emergency relief supplies tax-deductible as business operational expenses (Section 37 of the Income-tax Act) or classified as non-deductible donations?
  3. What corporate board resolutions and accounting ledger controls must be maintained to demonstrate strict separation between earned fee reserves and donor funds?
* **Required Counsel Action / Artifact:** Internal Reserve Accounting Policy SOP and Ledger Chart of Accounts structure.

---

### Item 9: Digital Personal Data Protection Act, 2023 (DPDP Act) and Minor Beneficiary Safeguards

* **Statutory Framework:** Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023); Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011.
* **Proposed Product Architecture:**
  - ACTA collects personal data: donor name, email, phone, PAN (for 80G); volunteer Aadhaar/KYC; and video footage of ground distributions.
  - Video footage often features vulnerable beneficiaries, including school children, hospital patients, and slum residents.
* **Key Questions for Legal Counsel / Data Protection Officer (DPO):**
  1. Under Section 9 of the DPDP Act, processing personal data of children requires verifiable parental consent and prohibits tracking or targeted advertising. How does this apply to public video footage of child beneficiaries receiving school kits or food?
  2. Does the automated MediaPipe Gaussian facial blur pipeline legally satisfy the requirement to prevent identification of minors before video archiving?
  3. What explicit notice and verifiable consent forms must partner NGOs execute with adult beneficiaries before recording distribution footage for YouTube unlisted hosting?
* **Required Counsel Action / Artifact:** DPDP Compliance Architecture Document, Minor Privacy Safeguard Protocol, and Field Consent Forms.

---

### Item 10: Foreign Contribution Regulation Act (FCRA) Ring-Fencing and Currency Controls

* **Statutory Framework:** Foreign Contribution (Regulation) Act, 2010 (FCRA) and Foreign Contribution (Regulation) Amendment Act, 2020; Foreign Exchange Management Act, 1999 (FEMA).
* **Proposed Product Architecture:**
  - Most grassroots Indian NGOs lack active FCRA registration and are legally prohibited from receiving foreign funds.
  - ACTA operates primarily in the domestic Indian student and collegiate sphere.
* **Key Questions for Legal Counsel:**
  1. If an Indian student or NRI living abroad attempts to donate ₹10 using an international credit card or foreign bank account, does this constitute a "foreign contribution" under Section 2(1)(j) of FCRA?
  2. What technical controls are required at the payment aggregator gateway to programmatically block all international cards, foreign IP addresses, and NRE/NRO accounts?
  3. How should the platform verify donor Indian residency (e.g., domestic INR UPI intent, domestic SMS OTP, or Indian mobile number verification) to guarantee 100% FCRA immunity?
* **Required Counsel Action / Artifact:** Payment Gateway FCRA Lockdown Specification enforcing domestic INR settlement only.

---

## Action Plan & Review Execution Sign-Off Matrix

| Review Phase | Target Specialist | Required Output / Deliverable | Status / Timeline |
| :--- | :--- | :--- | :--- |
| **Phase 1: Corporate & IT Intermediary** | Corporate Advocate (High Court) | SaaS Intermediary Terms of Service & Disclaimer | Pre-Pilot Gate |
| **Phase 2: Payment Gateway & RBI Rules** | Payment Aggregator Compliance Lead | Razorpay Route / Cashfree Split Written Approval | Pre-Pilot Gate |
| **Phase 3: Direct Tax & 80G/12A** | Chartered Accountant (FCA - Taxation) | Form 10BD & 80G Operational Tax Memorandum | Pre-Pilot Gate |
| **Phase 4: GST & SAC Billing** | Chartered Accountant (FCA - Indirect Tax) | SAC Classification & Automated B2B Invoice Setup | Pre-Pilot Gate |
| **Phase 5: Ground Operations & DPDP** | Technology Lead & DPO | MediaPipe Automated Minor Face Blur Pipeline | Production Launch |

---

*Verified and Prepared by:*  
**Piyush Singh**  
Founder & CEO, Resence • Product Architect, ACTA  
Greater Noida, Uttar Pradesh, India • October 2026
