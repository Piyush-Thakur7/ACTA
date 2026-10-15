# ACTA — Small Acts. Big Impact.
> **Flagship Web Platform & Verified Micro-Donation Prototype**  
> **Team Resence** • Incubated at GLBCRI (GL Bajaj Center for Research and Incubation)  
> **Conclave Showcase:** Bharat Udyam Sangam 2026 — Student Innovation & Startup Pitch  
> **Live Platform:** [https://acta.resence.in](https://acta.resence.in) | **Ecosystem:** [https://www.resence.in](https://www.resence.in)  
> **GitHub Repository:** [https://github.com/Piyush-Thakur7/ACTA.git](https://github.com/Piyush-Thakur7/ACTA.git)

---

## 🌟 Executive Summary

**ACTA** is India's first direct-to-need, itemized micro-donation platform designed specifically for college students and everyday citizens. Built by **Team Resence**, ACTA democratizes grassroots philanthropy by allowing anyone to fund tangible, ground-level relief items starting at just **₹10** (a pack of biscuits or oral rehydration salts) up to **₹250** (winter blankets and school kits).

Unlike legacy crowdfunding platforms that focus on emotionally manipulative mega-campaigns with opaque fund pools, ACTA enforces an uncompromised **Proof-Lock Protocol**:
1. **Direct Itemization:** Donors don't give to abstract funds; they fund specific items (e.g., 5 hot meals @ ₹50 each).
2. **Hardware-Locked In-App Video Proof:** Volunteers must record distribution videos directly through the ACTA in-app camera (hardware locked, gallery uploads prohibited) with live GPS telemetry (`28.4744° N, 77.5040° E`) and NTP timestamps overlaid.
3. **Linked Wholesale GST Invoices:** Every distribution proof links directly to the vendor's wholesale GST tax invoice, ensuring zero fund phantomization.
4. **Transparent Zero-Leakage Unit Economics:** Every ₹100 is split strictly into **₹95 Direct Ground Aid** and **₹5 Platform Operations** (3% payment gateway/hosting + 2% volunteer logistics).
5. **Campus Impact Guilds:** Gamified collective action across college hostels, sections, and departments (e.g., *GL Bajaj Boys Hostel Block-B*, *BCA 3C*, *B.Tech CSE Clan*).

---

## 🔍 The Problem & The Policy Dilemma

### 1. The ₹30,000 Crore Domestic Blind Spot
In India, the Foreign Contribution Regulation Act (FCRA 2020) mandates stringent quarterly reporting, strict bank accounts at SBI New Delhi, and granular tracking for foreign philanthropic funds. However, the **₹30,000+ Crore domestic retail donation market** operates in a complete information vacuum. Over 68% of young donors report losing trust in traditional NGOs due to zero follow-up proof, spam calls, and opaque balance sheets.

### 2. High Barriers to Entry
Legacy platforms (Ketto, Milaap, Give.do) are optimized for large-scale medical emergencies with high donation tickets (₹500 to ₹5,000+), high platform commissions (8% to 15%), and zero micro-itemization suitable for a college student's daily pocket money.

### 3. The ACTA Solution
ACTA introduces **UPI 0% MDR micro-giving** with a deterministic 5-stage real-time progress tracker:
```
[1. Order Created] ➔ [2. Escrow Locked] ➔ [3. Ground Volunteer Dispatched] ➔ [4. Item Procured & Video Recorded] ➔ [5. Proof Verified & Audit Closed]
```

---

## 📊 Platform Comparison Matrix

| Feature | ACTA | Ketto | Milaap | Give.do |
| :--- | :---: | :---: | :---: | :---: |
| **Minimum Micro-Donation** | **₹10 (Direct Item)** | ₹500 | ₹500 | ₹1,000 |
| **Ground Video Verification** | **Hardware Locked + GPS HUD** | ❌ None | ❌ None | Optional photos |
| **Wholesale GST Bill Matching** | **✅ Verified 1-to-1** | ❌ Opaque | ❌ Opaque | ⚠️ Periodic audit |
| **Platform Deduction** | **Strict 5% Max** | 8% – 12% | 8% – 10% | 10% – 15% |
| **Campus / Youth Guilds** | **✅ Hostels & Sections** | ❌ None | ❌ None | ❌ None |
| **Audit Receipt Download** | **✅ Instant PDF/JSON** | ⚠️ Generic receipt | ⚠️ Generic receipt | ⚠️ Tax 80G only |

---

## 🚀 Key Features Built in this Flagship Prototype

### 1. Itemized Micro-Causes Catalog
- **Parle-G & Glucose Packets** — ₹10 / child
- **Fresh Toned Milk Pouch (500ml)** — ₹25 / child
- **Nutritious Hot Khichdi Lunch** — ₹50 / individual
- **Weekly Ration & Dal-Rice Pack** — ₹150 / family
- **Warm Winter Fleece Blanket** — ₹250 / pavement dweller

### 2. "My Donations" Live Transparency Dashboard
- Interactive list of user-funded items with unique donation hashes (e.g., `#ACTA-2026-98104`).
- Real-time 5-stage progress indicator with status badges (`Verified & Dispatched`, `Proof Verified`, `In Escrow`).
- **Interactive Video Proof Player:** Plays field distribution video with HUD telemetry overlay (Live GPS coordinates, UTC/IST timestamp, Verified Volunteer badge).
- **Wholesale GST Tax Invoice Modal:** Displays complete vendor breakdown (Taxable value, CGST 2.5%, SGST 2.5%, Total Bill amount, Supplier GSTIN).
- **Downloadable Audit Receipt:** One-click instant print/PDF generation of the complete audit trail.

### 3. Campus Impact Guilds & Leaderboards
- Students join their college hostel, batch, or club to pool their micro-acts.
- Live leaderboard tracking items distributed, verified impact points, and active guild ranks.
- Featured Guilds: *GL Bajaj Boys Hostel Block-B*, *BCA 3C Changemakers*, *B.Tech CSE Code4Good Clan*, *Girls Hostel Alpha*.

### 4. Volunteer In-App Camera Simulator
- Demonstrates ACTA's strict anti-fraud field protocol:
  - Hardware camera feed simulation / WebRTC integration.
  - Device GPS coordinate lock (`28.4744° N, 77.5040° E`).
  - Gallery upload intentionally disabled to prevent archival or stock photo fraud.
  - Video capture + GST receipt upload simulation.

### 5. Zero-Leakage Unit Economics Calculator
- Dynamic slider calculating exact rupee splits for any donation between ₹10 and ₹10,000:
  - **₹95 Direct Ground Aid (95%)**
  - **₹3 Secure Gateway & Cloud Server Infrastructure (3%)**
  - **₹2 Volunteer Stipend & Distribution Logistics (2%)**

### 6. Policy Dilemma: The FCRA 2020 Contrast
- Educational and advocacy section contrasting foreign FCRA audit standards with domestic giving realities, articulating why ACTA is building India's sovereign civic ledger.

---

## 🛠️ Technology Stack

- **Frontend:** Semantic HTML5, Modern CSS Design System (Dark Slate `#0B0F17`, Emerald `#10B981`, Glassmorphism, Inter & JetBrains Mono typography), Vanilla JavaScript SPA Controller with zero framework overhead.
- **Backend:** Node.js, Express.js (High-performance API and static delivery).
- **Security & Headers:** Compression, Helmet-style CSP, CORS protection, Strict Referrer Policy, Sentry Node telemetry.
- **Data Architecture:** Hybrid Supabase PostgreSQL + Resilient in-memory fallback state for 100% offline-first prototype reliability.
- **Deployment:** Vercel serverless runtime (`vercel.json`), custom domain `acta.resence.in`.

---

## 💻 Local Development & Quickstart

### Prerequisites
- Node.js 18.x or 20.x or 22.x
- npm or pnpm

### Installation & Run
```bash
# 1. Clone repository
git clone https://github.com/Piyush-Thakur7/ACTA.git
cd ACTA

# 2. Install dependencies
npm install

# 3. Start local development server
npm start
# Alternatively:
node index.js
```

Open your browser at:
👉 **`http://localhost:5000`**

---

## 👥 Team Resence

* **Piyush Singh** — Founder & Tech Lead (BCA 2nd Year, GL Bajaj Institute of Management)
* **Dimple Singh** — Co-Founder & Presentation Lead
* **Mayank Chauhan** — Co-Founder & Marketing Lead

---

## 📄 License & Intellectual Property

Copyright © 2026 Resence Ecosystem. All rights reserved.  
Part of the Resence Civic Tech & AI Engineering Initiative.
