# ACTA by Resence — NGO Verification, Default Management & Delivery Continuity Workflow
**Document Classification:** Standard Operating Procedure (SOP) & Engineering Specification • Version 2.6  
**Parent Entity:** Resence (`https://resence.in`) | **Product:** ACTA (`https://acta.resence.in`)  
**Tagline:** *"Small Acts. Big Impact."*

---

## 1. NGO Onboarding & Verification Protocol

To prevent fraudulent entities from launching campaigns or accessing donor funds, ACTA enforces a rigorous, multi-step onboarding gate. Live campaigns and donations are strictly prohibited for unverified non-profits.

```
[NGO APPLICATION] ──► [DOC COLLECTION] ──► [PHYSICAL & BANK CHECKS] ──► [REVIEWER SIGN-OFF] ──► [STATUS: APPROVED]
                                                                                   │
                                                                                   └──► [STATUS: REJECTED / ON_HOLD]
```

### 1.1 The 5-Step Verification Gate
1. **Document Intake:**
   - Active NITI Aayog NGO Darpan Registration ID.
   - Income Tax Section 12A registration & valid Section 80G tax-exemption certificate.
   - Official Society / Trust / Section 8 Company Registration Certificate & PAN Card.
   - Authorized Representative identity proof (Aadhaar / Passport of Director / President).
2. **Bank Account Ownership Validation:**
   - Submission of cancelled cheque / official bank statement matching the NGO's registered legal name.
   - ₹1 automated Penny-Drop IMPS validation via payment aggregator API to verify active beneficiary name match.
3. **Physical Premises & Capacity Inspection:**
   - In-person site inspection conducted by a Resence field representative (or authorized GLBCRI student ambassador).
   - Inspection covers physical shelter, community kitchen, office facilities, and past ground activity logs.
4. **Formal Legal MoU Execution:**
   - Signing of the ACTA Master Service Agreement (MSA) defining service scope, 5% technology fee, reporting rules, DPDP Act 2023 compliance, and the 2-strike default contract.
5. **Auditable Reviewer Sign-Off:**
   - Every verification record stores: Reviewer Name, Verification Date, Document Hash, Status (`PENDING`, `APPROVED`, `REJECTED`), and Explicit Approval Rationale.
   - Status remains `UNVERIFIED` until all 5 steps are signed off. No campaign can be published or receive donations while unverified.

---

## 2. Campaign Execution & Failure Classification

Social-impact operations face diverse ground realities. ACTA strictly distinguishes between ordinary logistical delays and deliberate fraud, applying tailored operational protocols for each:

| Failure Classification | Operational Scenario | Primary Trigger | Immediate System Action | Resolution Protocol |
| :--- | :--- | :--- | :--- | :--- |
| **Category A: Ordinary Logistical Delay** | Heavy rainfall, transport breakdown, merchant out of stock. | Volunteer fails to execute within baseline SLA (e.g. 96h). | Campaign marked `DELAYED_PENDING_REVIEW`. Payout held. | In-app extension request with ground photo proof; max +72h approved by Admin. |
| **Category B: Insufficient / Inconclusive Evidence** | Blurry receipt photos, inaudible audio, camera glare obscuring face. | Submitted evidence fails technical clarity standards. | Campaign marked `PROOF_REVISION_REQUIRED`. | Documented notice issued; 48-hour correction window granted to upload clear GST invoice. |
| **Category C: Operational Negligence** | Volunteer uncontactable, multiple missed deadlines without notice. | SLA expired; no extension filed; volunteer unresponsive at Hour 72. | Formal Warning 1 issued. Campaign escalated to Director. | 24-hour urgent cure notice. Substitute Lead 1/2 assigned immediately. |
| **Category D: Contractual Breach** | Defaulting on corrected deadline, refusing audit, unauthorized 10% spend. | Failure to cure Category B/C within window; unverified expenditure. | Escalated to `DEFAULT_REVIEW`. NGO temporarily suspended. | Formal default notice issued. Escrow frozen. Transition to Replacement Workflow. |
| **Category E: Suspected Fraud / Material Misuse** | Recycled stock video, fabricated GST invoices, phantom beneficiaries. | AI frame hash collision, invalid GSTIN, or failed random physical spot-check. | Immediate Emergency Freeze. Status: `SUSPECTED_FRAUD_LOCKED`. | Internal investigation, evidence preservation, referral to legal counsel for recovery. |

---

## 3. The 12-Step NGO Default & Replacement Delivery Workflow

When a partner NGO defaults or cannot complete an active campaign, ACTA's paramount objective is **to ensure beneficiaries are not abandoned and donors receive verifiable proof of impact**.

```
[ORIGINAL NGO DEFAULT] ──► [1. FREEZE DISBURSEMENT] ──► [2. AUDIT SPENT / UNSPENT] ──► [3. DONOR TRANSPARENCY NOTICE]
                                                                                               │
[COMPLETED & PROVEN] ◄── [6. SECURE EVIDENCE] ◄── [5. ASSIGN REPLACEMENT] ◄── [4. FEASIBILITY EVALUATION]
          │
          └──► (IF NOT FEASIBLE) ──► [AUTOMATED DONOR REFUND INITIATED]
```

### 3.1 Step-by-Step Replacement Protocol
1. **Immediate Disbursement Freeze:** Contractually and technically freeze all remaining escrow/nodal disbursements to the defaulting NGO.
2. **Ledger Audit & Balance Reconciliation:** Calculate exact amount disbursed, verified work completed on the ground, unspent balance, and remaining deliverables (e.g. 100 meals funded, 40 delivered, 60 outstanding).
3. **Honest Donor Notification:** Transparently inform affected donors that delivery is delayed and undergoing formal operational review (using Template D-1/D-3).
4. **Feasibility & Safety Assessment:** Assess whether the original campaign can safely proceed under a substitute lead, requires an approved replacement NGO, or must be cancelled.
5. **Replacement NGO Eligibility Screening:** Identify a pre-vetted, active partner NGO operating in the same geographical hub (e.g. Greater Noida) with verified capacity to execute the remaining deliverables.
6. **Campaign & Donor Term Verification:** Confirm that campaign terms, donor restrictions, and regulatory norms permit replacement execution for the stated social cause.
7. **Cost Reconciliation & Lawful Funding Allocation:**
   - If unspent funds remain in escrow, transfer the remaining allocation to the replacement NGO under a documented agreement.
   - If funds were lost due to the original default, ACTA evaluates using its **Continuity Reserve** (funded strictly from ACTA's legitimately earned service-fee revenue) to fund the replacement delivery.
   - **Strict Financial Shield:** ACTA **NEVER** redirects restricted donations from other campaigns or uses funds owed to another NGO as an undisclosed reserve substitute.
8. **Replacement Execution Agreement:** Formal documented addendum signed with the replacement NGO detailing remaining deliverables, timeline, and reporting standards.
9. **Execution & Dual-Phase Evidence Submission:** Replacement NGO executes on the ground and submits wholesale purchase bills and geotagged distribution video.
10. **Evidence Audit & Review:** Compliance Officer audits proof footage and invoices against the original campaign scope.
11. **Donor Transparency & Impact Closure:** Publish verified video proof to the permanent YouTube archive. Notify donors detailing the replacement partner, revised timeline, funding source, and verified outcome.
12. **Permanent Audit Trail & Record Retention:** Archive all records of the original default, warning notices, reserve allocations, replacement agreements, payment transfers, and final evidence for statutory compliance.

---

## 4. End-to-End Campaign Lifecycle State Machine

The complete state machine governs all campaigns from initial pooling to successful completion or terminal failure:

```
[POOLING] ──► [MILESTONE_LOCKED] ──► [DISBURSED_PHASE_1] ──► [ON_TRACK] ──► [PROOF_REVIEW] ──► [COMPLETED]
                                                                │                   ▲
                                                                ▼                   │
                                                            [DELAYED] ──────────────┤
                                                                │                   │
                                                                ▼                   │
                                                        [WARNING_ISSUED]            │
                                                                │                   │
                                                                ▼                   │
                                                      [CORRECTION_WINDOW] ──────────┘
                                                                │
                                                                ▼
                                                        [DEFAULT_REVIEW]
                                                                │
                                    ┌───────────────────────────┴───────────────────────────┐
                                    ▼                                                       ▼
                        [REPLACEMENT_ASSESSMENT]                                   [CANCELLED]
                                    │                                                       │
                                    ▼                                                       ▼
                        [REPLACEMENT_APPROVED]                                     [REFUND_PENDING]
                                    │                                                       │
                                    ▼                                                       ▼
                        [DELIVERY_IN_PROGRESS]                                         [REFUNDED]
                                    │
                                    ▼
                            [PROOF_REVIEW] ──► [COMPLETED]
```

### 4.1 State Definitions & Transition Matrix
| Current State | Next Valid State | Authorized Role | Trigger Event / Requirement | Audit Log Event |
| :--- | :--- | :--- | :--- | :--- |
| `ON_TRACK` | `DELAYED` | System Cron / Field Lead | Deadline reached without Phase 1/2 proof upload. | `CAMPAIGN_DEADLINE_BREACHED` |
| `DELAYED` | `WARNING_ISSUED` | Compliance Officer | Grace period (24h) expired without valid extension request. | `FORMAL_WARNING_1_DISPATCHED` |
| `WARNING_ISSUED` | `CORRECTION_WINDOW` | Compliance Officer | Notice delivered; 48-hour cure window starts. | `CORRECTION_WINDOW_OPENED` |
| `CORRECTION_WINDOW`| `PROOF_REVIEW` | Field Lead | Missing bills / footage successfully re-uploaded. | `REVISED_PROOF_SUBMITTED` |
| `CORRECTION_WINDOW`| `DEFAULT_REVIEW` | Compliance Officer | 48h cure window expired with no response or invalid proof. | `DEFAULT_ESCALATION_TRIGGERED` |
| `DEFAULT_REVIEW` | `REPLACEMENT_ASSESSMENT` | Platform Lead | NGO formally declared in default; feasibility review initiated. | `REPLACEMENT_FEASIBILITY_STARTED` |
| `REPLACEMENT_ASSESSMENT` | `REPLACEMENT_APPROVED` | Platform Lead + Legal | Replacement NGO vetted and agreement signed. | `REPLACEMENT_NGO_CONTRACTED` |
| `REPLACEMENT_APPROVED` | `DELIVERY_IN_PROGRESS` | Replacement NGO Lead | Execution commenced on the ground. | `REPLACEMENT_EXECUTION_STARTED` |
| `DELIVERY_IN_PROGRESS` | `PROOF_REVIEW` | Replacement NGO Lead | New 2-phase proof bundle submitted. | `REPLACEMENT_PROOF_SUBMITTED` |
| `PROOF_REVIEW` | `COMPLETED` | Two-Person Sign-Off | Proof verified; YouTube archive updated; donors notified. | `CAMPAIGN_SUCCESSFULLY_CLOSED` |
| `DEFAULT_REVIEW` | `CANCELLED` | Platform Lead | Replacement unfeasible or cause no longer viable. | `CAMPAIGN_CANCELLED_UNFEASIBLE` |
| `CANCELLED` | `REFUND_PENDING` | System Engine | Refund batch initiated for all affected donors. | `REFUND_BATCH_QUEUED` |
| `REFUND_PENDING` | `REFUNDED` | Payment Aggregator | Gateway confirms settlement reversal / wallet credit. | `DONOR_FUNDS_REFUNDED_COMPLETE` |
| `DEFAULT_REVIEW` | `LEGAL_REVIEW` | Legal Counsel | Confirmed fraud, forged bills, or intentional misappropriation. | `LEGAL_RECOVERY_PROCEEDINGS_INITIATED` |
