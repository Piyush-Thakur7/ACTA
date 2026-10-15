import os
import subprocess
import pypdf

# Build Complete Master PRD System for ACTA by Resence
# Generates comprehensive Markdown and Apple-grade Master PDF

md_path = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_MASTER_CONCEPT_PRD.md"
html_path = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.html"
pdf_path = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.pdf"

print("Building Complete Master PRD Specification (Markdown + HTML + PDF)...")

# We will construct the comprehensive markdown and the HTML structure.
# Let's write the markdown first.

markdown_content = """# ACTA by Resence — Master Product Requirements Document (PRD) & System Specification
**Internal Single Source of Truth (SSOT) & Engineering Bible • Version 2.5**  
**Classification:** Confidential & Proprietary — Resence Tech Labs  
**Date:** October 2026 | **Author:** Piyush Singh (Founder & CEO, Resence)  
**Target Conclave:** Bharat Udyam Sangam 2026 (GL Bajaj Center for Research and Incubation - GLBCRI)  
**Parent Entity:** Resence (`https://resence.in`) | **Product:** ACTA (`https://acta.resence.in`)  
**Locked Tagline:** *"Small Acts, Big Impacts."*

---

## Executive Summary
**ACTA by Resence** is an institutional-grade, transparency-first micro-donation and civic engagement network connecting university students with manually vetted local non-profits across India. It addresses three structural crises in the Indian social giving ecosystem:
1. **The Ground Proof Deficit (67.5% Trust Collapse):** Donors receive generic 80G tax receipts and emails, but zero verifiable evidence of ground impact. ACTA mandates geotagged video proof within 96 hours before escrow release.
2. **The "Chillar" Stigma & Minimum Ticket Barrier:** Traditional non-profits ignore donations below ₹500, alienating 40 Million college students. ACTA builds a democratic micro-giving engine starting at ₹10 via UPI, leveraging India's 0% MDR mandate.
3. **The Retention & Community Void:** Traditional giving is episodic and guilt-driven. ACTA introduces an engaging collegiate habit loop—institutional campus communities, streaks, action-based experience points (XP), and dignified impact tiers.

---

## 01. Product Overview, Brand Heritage & Corporate Ecosystem

### 1.1 Project Specification
- **Product Name:** ACTA by Resence
- **Repository:** `https://github.com/Piyush-Thakur7/ACTA`
- **Live Prototype:** `https://resence.in` / `https://acta.resence.in`
- **Mission:** To democratize philanthropy in India by turning micro-donations into an accountable, transparent, and rewarding daily habit for youth.

### 1.2 Meaning of ACTA & Historical Heritage
- **Classical Latin Root:** In Classical Latin, *Acta* is the plural of *Actum*, translating to *"Things Done"*, *"Deeds Accomplished"*, or *"Official Public Records."*
- **The Roman Acta Diurna (131 BC):** Civilization's very first daily public bulletin, carved in stone and hung in the Roman Forum so citizens could verify grain allotments, decrees, and civic deeds.
- **The Modern Public Ledger:** On ACTA, every ₹10 donation is an individual *Acta*—a recorded, verified deed of human compassion.
- **Fusion with Locked Tagline:** *"Small Acts, Big Impacts."* The word *"Acts"* is the direct English translation of the Latin root *Acta*.

### 1.3 Corporate Ecosystem Architecture
ACTA operates under an Alphabet-Google corporate structure:
- **Resence (`resence.in`):** Master holding entity providing governance, shared AI infrastructure, visual design systems, and legal/financial oversight.
- **ACTA (`acta.resence.in`):** Flagship civic-tech product executing public donations, campus communities, and NGO escrow management.

---

## 02. Users, Roles, Personas & Permission Matrix (RBAC)

### 2.1 Target Stakeholder Personas
| Persona | Profile & Demographics | Key Goals | Pain Points & Constraints |
| :--- | :--- | :--- | :--- |
| **Rahul (Student Donor)** | 19, BCA 2nd Year, GL Bajaj. Monthly allowance: ₹3,500. Heavy UPI user. | Wants to do social good; desires transparency and college recognition. | Cannot afford ₹500; fears charity scams; feels small money is unwelcomed. |
| **Sunita (NGO Director)** | 52, Founder of registered animal shelter in Greater Noida. 12A/80G certified. | Reliable bulk funding; professional video marketing for her NGO. | Wastes 60% of time fundraising; struggles with digital tech; erratic donations. |
| **Priya (Campus Guild Lead)** | 20, Student Council Lead at GL Bajaj. Manages hostel club WhatsApp groups. | Rally batchmates for social drives; achieve top campus rank. | Disorganized donation tracking; cash collection chaos; zero visibility. |
| **Admin (Compliance Lead)** | Core Resence Operations team. Manages audits, escrow, and NGO compliance. | Zero-defect escrow release; fraud prevention; strict SLA adherence. | Needs automated receipt OCR, duplicate video detection, and audit trails. |

### 2.2 The 3-Portal Architecture
1. **Public User Portal (`acta.resence.in`):** High-throughput edge-cached client. Allows browsing 7 active causes, 1-click UPI donations, viewing personal impact stats, checking guild leaderboards, and watching verified YouTube proof videos.
2. **NGO Partner Portal (Invite-Only via Magic Link):** Restricted origin. Houses two isolated sub-dashboards:
   - *Sub-Dashboard A (NGO Director):* Financial allocations, 90/10 split ledger, field lead assignments, priority support.
   - *Sub-Dashboard B (Volunteer Field Team):* Task details, in-app camera recording, bill scanner, offline sync queue.
3. **Secret Admin Control Panel (Zero-Trust Route):** Hidden route with 2FA and IP whitelisting. Multi-modal frame auditing, receipt OCR inspection, escrow release trigger, and dispute resolution.

### 2.3 Role-Based Access Control (RBAC) Matrix
| Action / Resource | Public Donor | NGO Director | Volunteer Field Lead | Platform Admin |
| :--- | :---: | :---: | :---: | :---: |
| Browse Causes & Donate | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| View Personal Impact & Proof | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| View NGO Bank & Payout Ledgers | ❌ No Access | ✅ Full | ❌ No Access | ✅ Full |
| Assign Campaign Volunteer Leads | ❌ No Access | ✅ Full | ❌ No Access | ✅ Full |
| Access In-App Camera & Capture Proof | ❌ No Access | 👁️ View Only | ✅ Full | 👁️ View Only |
| Submit Expense Bills & Receipts | ❌ No Access | 👁️ View Only | ✅ Full | 👁️ View Only |
| Authorize Escrow Disbursement | ❌ No Access | ❌ No Access | ❌ No Access | ✅ Full |
| Create / Edit Verified Causes | ❌ No Access | ❌ No Access | ❌ No Access | ✅ Full |

---

## 03. MVP Scope Matrix: Implemented vs. Partially Implemented vs. Planned

| Feature Area | Module Specification | Status in Prototype | MVP Launch Target |
| :--- | :--- | :---: | :---: |
| **Donor UX** | Responsive Mobile-First Web Client (`acta.resence.in`) | ✅ Implemented | Live in Pilot |
| **Donor UX** | Total Impact Summary Card & Lifetime Stats | ✅ Implemented | Live in Pilot |
| **Donor UX** | 3-Pillar Navigation: Proof, Badges, Community | ✅ Implemented | Live in Pilot |
| **Payments** | Razorpay Smart UPI 1-Click Intent Flow | 🟡 Partially Implemented | Live in Pilot |
| **Payments** | Idempotent Webhook Listener & Escrow Ledger | 🟡 Partially Implemented | Live in Pilot |
| **Escrow** | Batch Pooling Engine & 100% Target Vault Freeze | 🟡 Partially Implemented | Live in Pilot |
| **Escrow** | Automated In-App Wallet Refund Routine | 🔵 Planned | Pilot Phase 2 |
| **NGO Portal** | Invite-Only Magic Link Authentication | 🟡 Partially Implemented | Live in Pilot |
| **NGO Portal** | Director Financial Overview & 90/10 Split View | 🟡 Partially Implemented | Live in Pilot |
| **Ground Proof** | In-App WebRTC Camera Lock (Gallery Locked) | 🟡 Partially Implemented | Live in Pilot |
| **Ground Proof** | Offline Video Capture & Auto-Sync Queue | 🔵 Planned | Pilot Phase 2 |
| **Ground Proof** | YouTube Data API v3 Unlisted Video Ingestion | 🟡 Partially Implemented | Live in Pilot |
| **AI Layer** | Gemini 1.5 Flash Student Impact Planner | ✅ Implemented | Live in Pilot |
| **AI Layer** | Gemini Vision Receipt OCR & Frame Audit Tool | 🟡 Partially Implemented | Pilot Phase 2 |
| **Gamification** | ₹1 = 10 XP Engine & Action XP Multipliers | ✅ Implemented | Live in Pilot |
| **Gamification** | 10-Level Exponential Giving Ladder & Rings | ✅ Implemented | Live in Pilot |
| **Community** | Campus Guild Creation & Clan Score Tracking | 🟡 Partially Implemented | Live in Pilot |
| **Community** | Top 25 City & National Leaderboards (Redis Cache) | 🟡 Partially Implemented | Live in Pilot |

---

## 04. Screen-by-Screen Functional Requirements & UI States

### 4.1 User Dashboard ASCII Wireframe
```text
┌────────────────────────────────────────────────────────────────────────┐
│                        ACTA USER DASHBOARD (CLEAN UX)                  │
├────────────────────────────────────────────────────────────────────────┤
│  👤 Piyush Singh (GL Bajaj Institute of Management)                    │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  TOTAL IMPACT SUMMARY                                            │  │
│  │  ₹ 140 Donated  •  14 Meals Funded  •  2 Trees Planted           │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  [ 📹 MY DONATIONS & PROOF ]   ──► Itemized ledger, merchant bills,    │
│                                    and verified YouTube proof video.   │
│                                                                        │
│  [ 🎖️ XP & BADGES ]            ──► Level progression (Level 1 to 10),  │
│                                    streak ring, and action badges.     │
│                                                                        │
│  [ 🏆 COMMUNITY & LEADERBOARD ] ──► Campus Guild clan score, inter-hostel│
│                                    ranks, and Top 25 City Leaderboard. │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│  ACTIVE VERIFIED CAUSES (7 Cards)                                      │
│  [ 🍲 Zero Hunger ]  [ 🌳 Green Earth ]  [ 📚 Child Education ] ...    │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Comprehensive UI State Machine Specifications

#### A. Loading State
- **Trigger:** Initial page load, network query, or async transaction.
- **Behavior:** Subtle pulse skeleton loaders matching exact layout dimensions. No generic spinning wheels. Shimmer duration: 1.2s.

#### B. Empty States
- **New Donor (Zero Donations):** Displays an uplifting illustration with copy: *"Your journey starts with ₹10. Select a cause below to create your first Acta."*
- **NGO Field Team (No Assigned Tasks):** Displays: *"No active ground campaigns assigned today. Stand by for Director dispatch."*
- **Guild Leaderboard (New Community):** Displays: *"Be the founding contributor of your Campus Guild. Pool ₹10 to unlock your clan badge."*

#### C. Failed States
- **Payment Dropped / Failed:** Displays clear diagnostic card: *"UPI transaction could not be completed by your bank. Zero money was deducted. [Retry ₹10 via UPI] or [Choose Another App]."*
- **Hardware Camera Access Denied:** In NGO field app, displays: *"Camera access is required to record verified ground proof. Please enable camera permissions in your browser settings. [Test Camera Access]."*

#### D. What Happens When a Campaign Has No Evidence Yet? ("Proof in Progress")
- **Problem Statement:** A donor contributes, but the NGO is currently executing on the ground (within the 96-hour window).
- **UX Treatment:** The campaign detail view renders an active **"Proof in Progress"** card:
  - *Dynamic Status Pill:* `[🟡 Ground Execution in Progress]`
  - *Execution Countdown:* Displays real-time countdown timer: *"Execution Clock: 54 Hours 12 Mins Remaining"*.
  - *Assigned NGO Badge:* Shows verified NGO name, registration Darpan ID, and location (e.g. *Saksham Foundation, Greater Noida*).
  - *Volunteer Check-in Indicator:* Shows timestamp of supplies purchased: *"Supplies Purchased at Wholesale Merchant: Oct 11, 10:30 AM"*.
  - *Clear Explanation:* Informs the donor: *"Your funds are safely held in the Escrow Vault. As soon as the NGO completes distribution and submits footage, your YouTube proof link will unlock here."*

#### E. What Happens If the Proof Video Fails to Load?
- **Problem Statement:** Network throttling, CDN error, or YouTube API outage prevents the embedded video player from playing.
- **UX Fallback Hierarchy:**
  1. **Primary Video Player:** Embedded YouTube IFrame / HTML5 video player.
  2. **Automatic Fallback on Error (`onError` event):**
     - Renders an **Inspected Frame Thumbnail Carousel**: 4 high-resolution verified video frame captures with burned-in telemetry (time, GPS, watermark).
     - Renders a prominent button: **[Watch Directly on YouTube ↗]** (opens official unlisted YouTube link in native YouTube app).
     - Displays an itemized table of verified vendor GST invoices and receipt scans.
     - Provides a **[Retry Video Stream]** button.

---

## 05. Field Execution, Offline Video Sync & Telemetry

### 5.1 In-App Camera Lockout Specification
- **Hardware Lockout:** The file gallery picker (`<input type="file">`) is strictly disabled on the client.
- **Live Stream Capture:** Media stream captured live via WebRTC `navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" }, audio: true })`.
- **Canvas Cryptographic Overlay:** Every video frame is rendered through an HTML5 canvas overlay that embeds an immutable cryptographic watermark containing:
  - Campaign Batch ID
  - NGO Darpan Registration ID
  - Network Time Protocol (NTP) Synchronized UTC Timestamp
  - High-precision GPS Latitude & Longitude coordinates.

### 5.2 Offline Video Capture & Automatic Background Sync Queue
- **Problem Statement:** Grassroots NGOs often distribute meals or blankets in rural slums, flood plains, or remote orphanages where 4G/5G mobile internet is non-existent.
- **Technical Architecture:**
  1. **Client-Side Chunking & Local Storage:** As the volunteer records via the in-app camera, video blobs are chunked into 2MB fragments and encrypted using AES-GCM, stored in the browser's persistent **IndexedDB (`acta_offline_media_store`)**.
  2. **Metadata Envelope:** Stored alongside raw hardware telemetry: device GPS coordinates, orientation gyroscope data, and capture timestamp.
  3. **Service Worker Background Sync:** Registers a sync tag with the browser's `ServiceWorkerRegistration.sync.register('acta-sync-proof-bundle')`.
  4. **Automatic Resume on Connectivity:**
     - The Service Worker listens to `window.addEventListener('online')` and `sync` events.
     - As soon as the field device reconnects to mobile data or Wi-Fi, the sync worker activates automatically in the background.
     - Uploads chunks sequentially to the pre-signed S3/Cloud Storage upload URL.
     - Computes SHA-256 hash on device and confirms hash match with backend.
  5. **Volunteer Confirmation:** The field lead receives a push notification and in-app modal: *"Ground proof footage successfully synced to ACTA Cloud. Submission ID #88129 confirmed."*

---

## 06. Campaign Lifecycle, 7 Standard Causes & Dynamic SLAs

### 6.1 The 7 Standard Causes & Standardized Unit Costs
ACTA maintains strictly 7 causes on the platform at any given time to eliminate cognitive fatigue and maintain audited unit economics:

| Slot Type | Cause Title & Scope | Unit Cost | Rotation Logic |
| :--- | :--- | :---: | :--- |
| **Permanent 1** | 🍲 **Zero Hunger** (Homeless & stray feeding) | ₹35 / meal | Infinite cyclic pool. When target completes, next verified NGO takes over immediately. |
| **Permanent 2** | 🌳 **Green Earth** (Tree plantation & campus cleanups) | ₹150 / sapling & guard | Infinite cyclic pool. Runs year-round across NCR educational campuses. |
| **Permanent 3** | 📚 **Child Education** (School kits & notebooks) | ₹250 / kit | Infinite cyclic pool. Partners with orphanages and slum learning centers. |
| **Permanent 4** | 👴 **Elder Care** (Medicines & hygiene packs) | ₹300 / pack | Infinite cyclic pool. Supports registered old-age homes and destitute seniors. |
| **Permanent 5** | 🧵 **Women Empowerment** (Dry ration hampers) | ₹500 / hamper | Infinite cyclic pool. Delivers monthly dry ration hampers to low-income widows. |
| **Temporary 1** | 🚨 **Disaster & Crisis Relief** (Floods, winter blankets) | Dynamic | Dynamic slot. Activates during emergency seasons; retires upon completion. |
| **Temporary 2** | 🐾 **Emergency Stray Rescue** (Veterinary trauma surgery) | ₹1,500 / surgery | Dynamic slot. Dedicated to urgent animal surgeries; rotates as needs arise. |

### 6.2 Ground Execution SLAs: Dynamic Deadlines by Cause Type
A rigid 96-hour deadline does not work for all social work. ACTA establishes **cause-specific Service Level Agreements (SLAs)**:
- **Food Distribution & Hot Meals:** **96 Hours (4 Days)**. (Emergency perishable food must be distributed rapidly).
- **School Kits & Educational Stationery:** **7 to 10 Days**. (Bulk procurement, packaging, and coordinated school distribution requires scheduling).
- **Tree Plantation Drives:** **10 Days**. (Site preparation, sapling transportation, guard installation).
- **Emergency Veterinary Trauma Surgery:** **24 to 48 Hours**. (Critical medical interventions require immediate execution).

### 6.3 Formal SLA Extension Request Protocol
- If unpreventable ground obstacles occur (e.g., severe rainfall, supplier stockout), the NGO Director must file an **In-App Extension Request** before the initial deadline expires.
- The request requires: (1) Reason selection, (2) Mandatory ground photo proof of the obstacle, (3) Revised delivery date (max +72 hours).
- Requires explicit approval from the Platform Admin. Donors receive an automated notification explaining the delay and updated delivery timeline.

---

## 07. Complete Payment & Fund Lifecycle Specification

### 7.1 End-to-End Payment & Escrow State Flow
```text
[STUDENT] ──(₹10 UPI Intent)──► [RAZORPAY GATEWAY] ──(Webhook)──► [ACTA ESCROW ENGINE]
                                                                        │
                                                                        ▼
                                                         [STATUS: POOLING IN VAULT]
                                                                        │
                                                                        ▼ (100% Target Met)
                                                         [STATUS: MILESTONE_LOCKED]
                                                                        │
                                                                        ▼ (Admin Disbursement)
                                                         [STATUS: DISBURSED_TO_NGO]
                                                                        │
                                                                        ▼ (NGO 96h Execution)
                                                         [STATUS: PROOF_SUBMITTED]
                                                                        │
                                    ┌───────────────────────────────────┴───────────────────────────────────┐
                                    ▼ (Verified)                                                            ▼ (Default / Breach)
                        [STATUS: COMPLETED & RELEASED]                                          [STATUS: 100% WALLET REFUND]
```

### 7.2 Razorpay Smart UPI Webhook Idempotency & Deduplication
- **Gateway Signature Validation:** Every incoming webhook is authenticated via HMAC SHA-256 against Razorpay Webhook Secret.
- **Idempotency Key Cache:** The webhook transaction ID (`x-razorpay-event-id`) is checked against Redis with a 24-hour TTL:
  ```typescript
  const eventId = req.headers['x-razorpay-event-id'];
  const exists = await redis.set(`webhook:processed:${eventId}`, '1', 'EX', 86400, 'NX');
  if (!exists) {
    return res.status(200).json({ status: 'already_processed' });
  }
  ```
- **Network Drop Reconciliation:** If a student's mobile app crashes or internet drops during payment, the backend reconciles the payment asynchronously via `payment.captured` webhook within 60 seconds, retroactively awarding XP and crediting the campaign escrow ledger.

### 7.3 Campaign Underfunding & Cancellation Handling
- **Pooling Window:** Campaigns have an open pooling window of 30 days.
- **Underfunding Handling:** If a campaign reaches only 60% of its target after 30 days, the Platform Admin evaluates:
  1. *Option A (Partial Batch Execution):* If the cause allows modular execution (e.g. 60 meals instead of 100 meals), the budget is adjusted down, the milestone is locked, and execution commences.
  2. *Option B (Automated Donor Refund):* If the campaign requires atomic funding (e.g. ₹1,500 surgery), 100% of donor funds are instantly credited to donors' in-app ACTA Wallets to reallocate to other active causes.

### 7.4 5% Platform Maintenance Fee Accounting
- **Transparent Disclosure:** 100% of the donor's ₹10 reaches the campaign escrow vault intact.
- **Deduction Timing:** The 5% maintenance fee is deducted **only upon successful post-verification delivery** from the gross campaign batch.
- **Allocation:**
  - 90% Direct Cause Supplies (Paid against vendor GST invoice).
  - 10% NGO Operational Allowance (Audited tempo fuel & packaging).
  - 5% Platform Maintenance Fee (Covers server bandwidth, Gemini AI tokens, verification staff travel).

### 7.5 Legal & Regulatory Custody
- ACTA does not operate as an unregulated bank. All donor contributions flow into a dedicated **Virtual Escrow / Nodal Account** managed under RBI Nodal Account Guidelines and NPCI regulations.
- Payouts to NGOs are initiated via automated IMPS/NEFT only upon dual-approval cryptographic authorization.

---

## 08. Trust, Verification, Human-in-the-Loop & Dispute Policy

### 8.1 The 2-Phase Ground Proof Bundle
1. **Phase 1: Wholesale Supply Purchase Proof**
   - In-app video showing purchased raw supplies (bags of rice, stationery boxes, blankets).
   - High-resolution photograph of merchant tax invoice showing GSTIN, itemized quantities, and store stamp.
2. **Phase 2: Ground Distribution Proof**
   - In-app video showing actual service delivery (food served, trees planted, notebooks handed to students).
   - Hardware GPS coordinates and NTP timestamps burned into frame metadata.

### 8.2 Human-in-the-Loop Verification & Two-Person Rule
- **AI Assistive Role:** Google Gemini Vision performs automated pre-screening:
  - Extracts merchant GSTIN and mathematical totals from invoices.
  - Computes perceptual frame hashes (pHash) to detect reused stock video clips.
  - Generates bounding box coordinates for face-blurring.
- **Human Authorization:** No AI model can unilaterally authorize escrow payout. A certified Resence Compliance Officer reviews the AI report, verifies physical merchant phone records if necessary, and approves the disbursement.
- **The Two-Person Rule:** For campaign disbursements exceeding **₹25,000**, dual authorization is mandatory: both the Compliance Officer and the Platform Lead must sign off with independent 2FA tokens.

### 8.3 Inconclusive Evidence & Dispute Handling
- **First Rejection / Information Request:** If bills are blurred or video quality is inconclusive, the submission enters `PROOF_REVISION_REQUESTED`. The NGO has 48 hours to upload clear invoices or field logs.
- **NGO Appeal Window:** The NGO Director has a formal 48-hour appeal window to request an in-person physical audit by a Resence field representative.
- **Irreconcilable Default:** If proof is confirmed fraudulent or the NGO fails to respond, the escrow batch enters `DEFAULT_TERMINATED`. The NGO is blacklisted, and 100% of funds are refunded to donor wallets.

---

## 09. DPDP Act 2023 Compliance & Zero-Liability Volunteer Safety

### 9.1 DPDP Act 2023 Compliance Architecture
- **Statutory Mandate:** India's Digital Personal Data Protection Act (DPDP Act 2023) prohibits unauthorized publication of identifiable imagery of minors and vulnerable persons.
- **Automated Face-Blurring Pipeline:**
  - *Minors (<18 Years Old):* All children in school drives, orphanages, or slum centers are detected using MediaPipe Face Detection and masked using Gaussian Blur ($ksize=51, \sigma=30$) by default.
  - *Distressed Beneficiaries:* Faces of hospital patients and destitute seniors are automatically masked to safeguard human dignity.
  - *Authorized NGO Staff:* Adult field workers and volunteer leads remain unblurred as official institutional representatives.

### 9.2 Zero-Liability Volunteer Safety Shield
- **Legal Firewall:** ACTA operates strictly as a **Technology, Escrow, and Verification Infrastructure Layer**.
- **No Direct Volunteer Hiring:** ACTA never directly recruits, dispatches, or employs field volunteers.
- **Partner NGO Indemnification:** Under signed institutional MoUs, the partner NGO assumes **100% legal, physical, medical, and insurance liability** for all on-ground activities.
- **Safety Guidelines:** Ground distributions are restricted to daylight hours (8:00 AM to 5:30 PM). Volunteers must wear official NGO identification badges.

---

## 10. Balanced Gamification, Campus Communities & Privacy

### 10.1 Balanced Gamification: Beyond Spending
To prevent wealth-shaming and pay-to-win dynamics, ACTA balances monetary XP with meaningful civic actions:

| Action / Trigger | XP Awarded | Cap / Limit | Strategic Purpose |
| :--- | :---: | :---: | :--- |
| **Direct Micro-Donation** | ₹1 = 10 XP | None | Base micro-giving incentive. |
| **Watch & Verify Proof Video** | +20 XP | 1 per campaign | Incentivizes donors to inspect transparency footage. |
| **3-Week Consistency Streak** | +150 XP | Weekly | Encourages recurring collegiate habits. |
| **Campus Guild Milestone Boost**| +200 XP | Per campaign | Collective pride within the college clan. |
| **Campus Green / Social Drive** | +250 XP | Verified offline | Rewards active student volunteering on campus. |

### 10.2 The 10-Level Exponential Giving Ladder
| Level | Title | XP Required | Direct Giving Equiv. | Visual Profile Perks |
| :---: | :--- | :---: | :---: | :--- |
| **L01** | **Seed Giver** 🌱 | 0 – 4,999 XP | ₹0 – ₹499 | Bronze Seed Tag. Unlocks on first ₹10 donation. |
| **L02** | **Kind Giver** 🤝 | 5,000 – 11,999 XP | ₹500+ | Silver Border Ring. Guild chat unlocked. |
| **L03** | **Active Giver** ⭐ | 12,000 – 24,999 XP | ₹1,200+ | Polished Silver Ring + Guild shoutout badge. |
| **L04** | **Impact Giver** 🔷 | 25,000 – 49,999 XP | ₹2,500+ | Sapphire Blue Ring + Voting power on next cause. |
| **L05** | **Dedicated Giver** 🛡️ | 50,000 – 99,999 XP | ₹5,000+ | Gold Shield Ring + Featured on Campus Board. |
| **L06** | **Community Pillar** 🏛️ | 1,00,000 – 1,99,999 XP | ₹10,000+ | Radiant Gold Ring + Authority to create Campus Guilds. |
| **L07** | **Change Maker** ⚔️ | 2,00,000 – 3,99,999 XP | ₹20,000+ | Emerald Ring + Invite to annual NGO field audits. |
| **L08** | **Master Benefactor** 💎 | 4,00,000 – 6,99,999 XP | ₹40,000+ | Ruby Ring + Priority sponsor matching on donations. |
| **L09** | **Grand Philanthropist** 🌟 | 7,00,000 – 9,99,999 XP | ₹70,000+ | Glowing Amethyst Ring + City Hall of Fame Top Tier. |
| **L10** | **The Crown Legend** 👑 | 10,00,000+ XP | ₹1,00,000+ | Animated Diamond Crown Ring + Resence Impact Award. |

### 10.3 Campus Communities & Institutional Guilds
- **Collective Momentum:** Students join institutional communities (e.g. *GL Bajaj BCA 2nd Year*, *Galgotias CS Club*, *Hostel Block B*).
- **Simultaneous Crediting:** Every ₹10 donation increments both the student's personal score and the collective Guild Score.
- **Verification Guardrail:** Instantiating a Campus Community requires a verified college email domain (`@glbajaj.org`) or student ID card verification.

### 10.4 Anti-Shaming Privacy Rule
- **Individual Casual Scores Kept Private:** To prevent humiliation, individual student scores are visible only to themselves.
- **Public Leaderboards Scope Strictly Top 25:**
  1. *Top 25 Communities / Guilds (City & National Level)*
  2. *Top 25 Donors (City & National Hall of Fame)*

---

## 11. Production Technical Architecture, Database Schemas & API Contracts

### 11.1 PostgreSQL Relational DDL Schemas
```sql
-- 1. Users Table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone VARCHAR(15) UNIQUE NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  college_name VARCHAR(150),
  college_id VARCHAR(50),
  guild_id UUID REFERENCES campus_guilds(id),
  wallet_balance NUMERIC(10,2) DEFAULT 0.00,
  xp INT DEFAULT 0,
  level INT DEFAULT 1,
  streak_weeks INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Campus Communities / Guilds Table
CREATE TABLE campus_guilds (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guild_name VARCHAR(120) NOT NULL,
  college_domain VARCHAR(100) NOT NULL,
  lead_user_id UUID REFERENCES users(id),
  total_pooled NUMERIC(12,2) DEFAULT 0.00,
  member_count INT DEFAULT 1,
  tier VARCHAR(30) DEFAULT 'RISING_CLAN',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Curated Partner NGOs Table
CREATE TABLE ngos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  legal_name VARCHAR(200) NOT NULL,
  darpan_id VARCHAR(50) UNIQUE NOT NULL,
  section_12a_80g_valid BOOLEAN DEFAULT TRUE,
  bank_account_verified BOOLEAN DEFAULT FALSE,
  trust_score INT DEFAULT 100,
  strikes_count INT DEFAULT 0,
  status VARCHAR(30) DEFAULT 'ACTIVE', -- ACTIVE, PROBATION, BLACKLISTED
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Escrow Batches Table
CREATE TABLE escrow_batches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cause_id UUID REFERENCES causes(id),
  ngo_id UUID REFERENCES ngos(id),
  target_amount NUMERIC(10,2) NOT NULL,
  pooled_amount NUMERIC(10,2) DEFAULT 0.00,
  direct_cause_90 NUMERIC(10,2) NOT NULL,
  ngo_ops_10 NUMERIC(10,2) NOT NULL,
  acta_fee_5 NUMERIC(10,2) NOT NULL,
  execution_deadline_at TIMESTAMPTZ,
  status VARCHAR(30) DEFAULT 'POOLING', -- POOLING, MILESTONE_LOCKED, DISBURSED, PROOF_SUBMITTED, COMPLETED, REFUNDED
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Proof Bundles Table
CREATE TABLE proof_bundles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_batch_id UUID REFERENCES escrow_batches(id),
  submitted_by UUID REFERENCES users(id),
  merchant_gstin VARCHAR(20),
  phase_1_bill_url TEXT NOT NULL,
  phase_1_video_url TEXT,
  phase_2_video_url TEXT NOT NULL,
  gps_latitude NUMERIC(9,6) NOT NULL,
  gps_longitude NUMERIC(9,6) NOT NULL,
  ntp_timestamp TIMESTAMPTZ NOT NULL,
  ai_fraud_score NUMERIC(5,2),
  human_reviewer_id UUID REFERENCES users(id),
  youtube_video_id VARCHAR(50),
  status VARCHAR(30) DEFAULT 'PENDING_REVIEW'
);
```

### 11.2 Core REST API Endpoints Specification

#### A. Initiate Donation Session (`POST /api/v1/donations/intent`)
- **Headers:** `Authorization: Bearer <jwt_token>`
- **Request Body:**
  ```json
  {
    "cause_id": "cause_hunger_01",
    "amount_inr": 10.00,
    "guild_id": "guild_glbajaj_bca"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "order_id": "order_H8912xYz",
    "amount": 1000,
    "currency": "INR",
    "upi_intent_url": "upi://pay?pa=acta@icici&pn=ACTA&am=10.00&tr=order_H8912xYz",
    "escrow_batch_id": "batch_99214"
  }
  ```

#### B. Submit Field Proof Bundle (`POST /api/v1/ngo/proof/submit-bundle`)
- **Headers:** `Authorization: Bearer <ngo_magic_token>`
- **Request Body:**
  ```json
  {
    "escrow_batch_id": "batch_99214",
    "merchant_gstin": "07AAACS1429B1ZB",
    "phase_1_bill_url": "https://storage.acta.resence.in/bills/gst_881.jpg",
    "phase_2_video_url": "https://storage.acta.resence.in/raw/video_881.mp4",
    "telemetry": {
      "gps_lat": 28.4744,
      "gps_lng": 77.5040,
      "ntp_timestamp": "2026-10-11T11:45:00Z"
    }
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "proof_bundle_id": "pb_88129",
    "status": "QUEUED_FOR_AI_AND_HUMAN_AUDIT",
    "estimated_review_window_hours": 12
  }
  ```

---

## 12. Operational FAQ, 90-Day Roadmap & Incubation Asks

### 12.1 Real-World Operational FAQ

**Q1: What happens if an NGO is executing in a rural slum with zero mobile connectivity?**  
**A:** The in-app camera records offline. Video blobs and telemetry are stored encrypted in local IndexedDB. The Service Worker Background Sync engine automatically queues and syncs the upload the instant the device re-enters 4G/Wi-Fi coverage.

**Q2: What happens if a campaign's proof video fails to load on the student's phone?**  
**A:** The app detects player error and immediately displays an inspected frame thumbnail carousel (with burned-in GPS and time telemetry), accompanied by a direct button to watch on YouTube, and full itemized vendor GST receipts.

**Q3: What if an NGO defaults on the execution deadline?**  
**A:** If the deadline expires without an approved extension, the escrow vault triggers an automatic 100% refund credited to all donors' virtual wallets. The NGO receives Strike 1 on their permanent record.

**Q4: How does ACTA ensure youth micro-giving doesn't turn into a pay-to-win game?**  
**A:** XP is balanced across verifying proof (+20 XP), weekly consistency streaks (+150 XP), and verified campus volunteering (+250 XP), alongside direct micro-giving. All individual donation totals are kept strictly private.

### 12.2 90-Day Execution Roadmap
- **Phase 1: Incubation & Partner MoUs (Days 1–30):** Secure GLBCRI incubation letterhead; onboard first 10 verified local Greater Noida NGOs via white-glove offline visits.
- **Phase 2: Closed Campus Pilot (Days 31–60):** Deploy 30-day pilot across GL Bajaj Knowledge Park hostels; target 1,000 active student givers & 10 completed campaigns (₹50,000 gross).
- **Phase 3: Inter-College League (Days 61–90):** Expand to Galgotias, Sharda, and Bennett University; activate the Top 25 City Guild leaderboard.

### 12.3 Specific Asks from GLBCRI (Bharat Udyam Sangam 2026)
1. **Institutional Credibility & Letterhead:** Official GL Bajaj / GLBCRI introduction letter to 18–20 verified local non-profits in Greater Noida.
2. **Campus Pilot Authorization:** Approval to run an official 30-day student micro-giving pilot across GL Bajaj departments and hostels.
3. **Pre-Incubation Mentorship:** Legal formalization for NGO MoUs, Section 8/Pvt Ltd structuring, and seed grant guidance.

---

## Document Sign-Off & Approval
- **Product Architect & Founder:** Piyush Singh (CEO, Resence)
- **Academic Standing:** BCA 2nd Year, GL Bajaj Institute of Management, Greater Noida
- **Document Status:** Approved & Locked Single Source of Truth (SSOT v2.5)
"""

with open(md_path, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Markdown PRD written to {md_path}")
print(f"Markdown character length: {len(markdown_content)}, lines: {len(markdown_content.splitlines())}")
