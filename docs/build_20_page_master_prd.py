import os
import subprocess
import pypdf

html_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.html"
pdf_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.pdf"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — Master Product Specification & Architecture Bible (20-Page SSOT)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 14mm 14mm 14mm 14mm;
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #111827;
    background-color: #FFFFFF;
    line-height: 1.5;
    font-size: 10pt;
    -webkit-font-smoothing: antialiased;
  }

  .page-break {
    page-break-after: always;
    break-after: page;
  }

  .page {
    min-height: 260mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding-bottom: 5mm;
  }

  .header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #E5E7EB;
    padding-bottom: 6px;
    margin-bottom: 16px;
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748B;
    font-weight: 600;
  }

  .header-bar .brand {
    color: #0F172A;
    font-weight: 800;
  }

  .footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #E5E7EB;
    padding-top: 6px;
    margin-top: 14px;
    font-size: 7.5pt;
    color: #94A3B8;
  }

  /* Cover Page */
  .cover-page {
    min-height: 265mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 10px;
  }

  .cover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 18px;
  }

  .brand-badge {
    background: #0F172A;
    color: #FFFFFF;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 10pt;
    letter-spacing: 2px;
    padding: 6px 14px;
    border-radius: 6px;
  }

  .doc-tag {
    font-size: 8.5pt;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #64748B;
    font-weight: 700;
  }

  .cover-body {
    margin-top: 40px;
    margin-bottom: 40px;
  }

  .hero-h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 38pt;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.05;
    color: #0F172A;
    margin-bottom: 10px;
  }

  .hero-h1 span {
    color: #059669;
  }

  .hero-sub {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16pt;
    color: #334155;
    font-weight: 600;
    margin-bottom: 20px;
    letter-spacing: -0.5px;
  }

  .hero-paragraph {
    font-size: 11pt;
    color: #475569;
    max-width: 620px;
    line-height: 1.6;
    margin-bottom: 28px;
  }

  .pill-group {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 30px;
  }

  .pill-item {
    background: #F1F5F9;
    color: #334155;
    font-size: 8pt;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 999px;
    border: 1px solid #E2E8F0;
  }

  .pill-item.green {
    background: #ECFDF5;
    color: #065F46;
    border-color: #A7F3D0;
  }

  .pill-item.blue {
    background: #EFF6FF;
    color: #1E40AF;
    border-color: #BFDBFE;
  }

  .meta-table-box {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 16px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
  }

  .meta-col h6 {
    font-size: 7.5pt;
    text-transform: uppercase;
    color: #64748B;
    letter-spacing: 1px;
    margin-bottom: 2px;
  }

  .meta-col p {
    font-size: 9.5pt;
    font-weight: 600;
    color: #0F172A;
  }

  /* Typography */
  h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16pt;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.4px;
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 2px solid #E2E8F0;
  }

  h2 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 11.5pt;
    font-weight: 700;
    color: #1E293B;
    margin-top: 10px;
    margin-bottom: 6px;
    letter-spacing: -0.2px;
  }

  p {
    margin-bottom: 8px;
    color: #334155;
    line-height: 1.5;
  }

  ul, ol {
    margin-left: 18px;
    margin-bottom: 10px;
    color: #334155;
  }

  li {
    margin-bottom: 3px;
  }

  strong {
    color: #0F172A;
    font-weight: 600;
  }

  /* Cards & Containers */
  .card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 10px;
  }

  .card-emerald {
    background: #F0FDF4;
    border-left: 4px solid #059669;
    border-color: #E2E8F0 #E2E8F0 #E2E8F0 #059669;
  }

  .card-blue {
    background: #F8FAFC;
    border-left: 4px solid #2563EB;
    border-color: #E2E8F0 #E2E8F0 #E2E8F0 #2563EB;
  }

  .card-amber {
    background: #FFFBEB;
    border-left: 4px solid #D97706;
    border-color: #E2E8F0 #E2E8F0 #E2E8F0 #D97706;
  }

  .card-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 10pt;
    color: #0F172A;
    margin-bottom: 4px;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 12px 0;
    font-size: 8.5pt;
  }

  th {
    background: #0F172A;
    color: #FFFFFF;
    text-align: left;
    padding: 7px 10px;
    font-weight: 600;
    font-size: 8pt;
    letter-spacing: 0.5px;
  }

  td {
    padding: 6px 10px;
    border-bottom: 1px solid #E2E8F0;
    color: #334155;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background: #F8FAFC;
  }

  /* Terminal Mockup */
  .wireframe {
    background: #0F172A;
    color: #F8FAFC;
    padding: 12px 14px;
    border-radius: 8px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 8pt;
    line-height: 1.4;
    margin: 10px 0;
    white-space: pre;
    overflow-x: hidden;
  }

  /* Stat Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 10px;
  }

  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 10px;
  }

  .stat-card {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 10px;
    text-align: center;
  }

  .stat-val {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15pt;
    font-weight: 800;
    color: #059669;
  }

  .stat-lbl {
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #64748B;
    font-weight: 600;
  }
</style>
</head>
<body>

<!-- ==========================================
     PAGE 01: COVER PAGE
     ========================================== -->
<div class="page cover-page">
  <div class="cover-top">
    <div class="brand-badge">RESENCE ECOSYSTEM</div>
    <div class="doc-tag">INTERNAL TEAM MASTER BIBLE • SSOT v2.0</div>
  </div>

  <div class="cover-body">
    <div class="hero-h1">ACTA <span>by Resence</span></div>
    <div class="hero-sub">Small Acts, Big Impacts.</div>
    <div class="hero-paragraph">
      The Complete 20-Page Product Requirements & Architectural Specification Bible. Built to serve as the binding Single Source of Truth for frontend prototyping, backend escrow logic, pitch decks, and incubation execution.
    </div>

    <div class="pill-group">
      <div class="pill-item green">0% MDR UPI Micro-Giving (₹10+)</div>
      <div class="pill-item blue">Milestone Escrow Vault</div>
      <div class="pill-item">4-Day Geotagged Video Proof</div>
      <div class="pill-item green">Inter-College Campus Impact Guilds</div>
      <div class="pill-item blue">90/10 NGO Split Rule</div>
      <div class="pill-item">DPDP Act 2023 Compliant</div>
    </div>

    <div class="meta-table-box">
      <div class="meta-col">
        <h6>Founder & Architect</h6>
        <p>Piyush Singh (CEO, Resence)</p>
      </div>
      <div class="meta-col">
        <h6>Academic Standing</h6>
        <p>BCA 2nd Year, GL Bajaj (GLBIM)</p>
      </div>
      <div class="meta-col">
        <h6>Target Conclave</h6>
        <p>Bharat Udyam Sangam 2026 (GLBCRI)</p>
      </div>
      <div class="meta-col">
        <h6>Document Intent</h6>
        <p>Internal Engineering & Pitch SSOT</p>
      </div>
      <div class="meta-col">
        <h6>Pilot Geography</h6>
        <p>Greater Noida & Delhi NCR Hub</p>
      </div>
      <div class="meta-col">
        <h6>Release Version</h6>
        <p>Release v2.0 (Complete 20-Page)</p>
      </div>
    </div>
  </div>

  <div class="footer-bar">
    <span>CONFIDENTIAL & PROPRIETARY — RESENCE TECH LABS</span>
    <span>PAGE 01 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 02: CHAPTER 01 — IDENTITY & ETYMOLOGY
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 01</span>
    </div>

    <h1>01. The Identity, Meaning & Etymology of ACTA</h1>

    <div class="card card-emerald">
      <div class="card-title">What Does ACTA Mean, and What is its Role in Our Startup?</div>
      <p>The name <strong>ACTA</strong> was deliberately chosen to provide deep historical weight, legal dignity, and brand defensibility. It is the literal foundation of our product.</p>
    </div>

    <h2>1. Classical Latin Origin & Roman History</h2>
    <p>In Classical Latin, <strong>Acta</strong> is the plural form of <em>Actum</em>, which literally translates to <strong>"Things Done"</strong>, <strong>"Deeds Accomplished"</strong>, or <strong>"Official Public Records."</strong></p>
    <p>Historically, around 131 BC, the Roman Republic instituted the famous <strong>Acta Diurna</strong> (literally <em>"Daily Deeds / Daily Acts"</em>). Carved in stone or metal and hung in the public Forum, it was civilization's very first public transparency gazette, ensuring that everyday citizens could verify government distributions, grain allotments, and civic decrees with their own eyes.</p>

    <h2>2. The Exact Role of ACTA in Our Project Architecture</h2>
    <ul>
      <li><strong>Every Donation is an "Acta":</strong> On our platform, a ₹10 donation is not an anonymous financial transaction; it is an individual <em>Acta</em>—a recorded, verified deed of human compassion.</li>
      <li><strong>The Modern Public Ledger:</strong> Just as ancient Rome had the <em>Acta Diurna</em>, our platform acts as India's digital public transparency ledger. Every rupee donated is proven with video before the record is permanently published.</li>
      <li><strong>Linguistic Fusion with Our Locked Tagline:</strong> The locked tagline is <strong>"Small Acts, Big Impacts."</strong> The word <em>"Acts"</em> in the tagline is the exact English translation of the Latin root <em>Acta</em>. The brand name and the tagline are linguistically fused.</li>
    </ul>

    <h2>3. Parent Organization: Alphabet & Google Structure</h2>
    <div class="card card-blue">
      <div class="card-title">Resence as Parent Company</div>
      <p><strong>Resence</strong> is the parent umbrella company (`https://www.resence.in`). It holds the technical infrastructure, governance, and multi-product roadmap. <strong>ACTA</strong> is the flagship civic-fintech product (`https://acta.resence.in`), operating as <em>"ACTA by Resence."</em></p>
    </div>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 01: Identity & Etymology</span>
    <span>PAGE 02 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 03: CHAPTER 02 — MARKET REALITY
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 02</span>
    </div>

    <h1>02. Market Ground Reality & The Gen Z Opportunity</h1>

    <div class="grid-3">
      <div class="stat-card">
        <div class="stat-val">67.5%</div>
        <div class="stat-lbl">Donor Trust Deficit</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">₹540 B</div>
        <div class="stat-lbl">India Giving Market</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">0% MDR</div>
        <div class="stat-lbl">Govt Mandated UPI Cut</div>
      </div>
    </div>

    <h2>1. The 67.5% Cynicism Chasm in Indian Charity</h2>
    <p>India houses over <strong>5,25,000+ registered NGOs</strong> on the government NGO Darpan portal. However, extensive data reveals that **67.5% of potential Indian donors do not donate online**. The root cause is a catastrophic trust deficit. Indian donors regularly read news stories regarding corrupt non-profit directors, inflated administrative bills, and phantom beneficiaries. Donors ask one single question: <em>"Where did my ₹100 actually go?"</em> Traditional platforms fail to answer this question.</p>

    <h2>2. The "Small Money" Embarrassment Barrier for Gen Z</h2>
    <p>College students (Gen Z) represent the most socially conscious generation in modern history. They care deeply about stray animal rescue, environmental greening, and child education. However, they are blocked by two psychological walls:</p>
    <ul>
      <li><strong>Embarrassment:</strong> Walking up to a traditional charity stall with ₹20 or ₹40 feels humiliating. Traditional NGOs treat amounts below ₹500 as "chillar" (loose change).</li>
      <li><strong>Fear of Fraud:</strong> Students surviving on tight monthly allowances refuse to give blindly to unverified organizations.</li>
    </ul>

    <h2>3. The ACTA Unlock: Dignity in Micro-Giving</h2>
    <div class="card card-emerald">
      <div class="card-title">Collective Democratic Power</div>
      <p>ACTA eliminates the embarrassment of small amounts. A ₹10 donation is celebrated with full dignity and 100 XP! When 1,000 students at GL Bajaj pool ₹10, it creates ₹10,000—delivering 200 fresh meals to stray animals or school kits to 50 children. Micro-giving becomes a respected daily campus habit.</p>
    </div>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 02: Market Ground Reality</span>
    <span>PAGE 03 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 04: CHAPTER 03 — COMPETITOR TEARDOWN
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 03</span>
    </div>

    <h1>03. Competitor Tear-Down: Why ACTA Beats Milaap & Ketto</h1>

    <div class="card card-amber">
      <div class="card-title">The Fundamental Paradigm Shift</div>
      <p>Legacy platforms like <strong>Milaap, Ketto, and GiveIndia</strong> were designed 15 years ago for working professionals making high-ticket donations via cards. They operate as <em>unmonitored payment pipelines</em>. ACTA is designed for <strong>Gen Z on UPI</strong>, operating as a <em>zero-trust verification engine</em>.</p>
    </div>

    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Legacy Platforms (Milaap / Ketto)</th>
          <th>ACTA by Resence</th>
          <th>Why Donors Choose ACTA</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Minimum Ticket</strong></td>
          <td>₹500 to ₹1,000+ (High financial friction)</td>
          <td><strong>₹10 to ₹50 via UPI</strong></td>
          <td>Zero pocket money guilt; every student can give daily.</td>
        </tr>
        <tr>
          <td><strong>Proof of Work</strong></td>
          <td>Opaque. Only a tax receipt & generic email update.</td>
          <td><strong>Mandatory 4-day geotagged video + store bills.</strong></td>
          <td>You see the actual food plate delivered within 96 hours.</td>
        </tr>
        <tr>
          <td><strong>Fund Custody</strong></td>
          <td>100% money released upfront to campaigner without execution proof.</td>
          <td><strong>100% frozen in Escrow Vault.</strong> Disbursed only after proof verification.</td>
          <td>Zero risk of campaigner running away with donor funds.</td>
        </tr>
        <tr>
          <td><strong>Audience & Culture</strong></td>
          <td>Older adults, HNIs; driven by emotional guilt & medical sadness.</td>
          <td><strong>Gen Z, college youth; driven by campus community pride & collective purpose.</strong></td>
          <td>Charity becomes an engaging, uplifting campus habit.</td>
        </tr>
        <tr>
          <td><strong>Fee Structure</strong></td>
          <td>5% to 10% cut + 2% gateway + guilt-trip tipping prompts.</td>
          <td><strong>5% flat platform maintenance fee; 0% UPI gateway cut.</strong></td>
          <td>Complete financial transparency; no hidden tipping tricks.</td>
        </tr>
        <tr>
          <td><strong>NGO Vetting</strong></td>
          <td>Open marketplace; anyone can submit a cause with unverified claims.</td>
          <td><strong>Curated 18–20 local NGOs, verified physically offline.</strong></td>
          <td>Eliminates fake NGOs and phantom beneficiary scams.</td>
        </tr>
      </tbody>
    </table>

    <h2>The Core Differentiation Moat</h2>
    <p>On Ketto, you give money and hope for the best. On ACTA, <strong>the escrow vault guarantees execution, or your money is automatically returned to your wallet.</strong></p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 03: Competitor Tear-Down</span>
    <span>PAGE 04 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 05: CHAPTER 04 — 3-PORTAL ARCHITECTURE
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 04</span>
    </div>

    <h1>04. The 3-Portal Architecture & Access Security</h1>

    <p>To eliminate security risks and maintain absolute operational separation, ACTA divides all platform interactions into <strong>three distinct, isolated portals</strong>:</p>

    <div class="card card-emerald">
      <div class="card-title">1. Public User Portal (`acta.resence.in`)</div>
      <p>Accessible to any user worldwide via modern web browsers and mobile devices. Zero barriers to entry. Users can browse the 7 active causes, execute 1-click UPI donations, review their personal impact summary, inspect verified YouTube proof archives, and track their college's standing on the Top 25 leaderboard.</p>
    </div>

    <div class="card card-blue">
      <div class="card-title">2. Dedicated NGO Partner Portal (Invite-Only via Magic Link)</div>
      <p>Completely invisible to the public. There is no open registration button. Once an NGO is verified physically offline, an authenticated setup guide and unique magic link are dispatched to their official email. Houses the Director Financial Dashboard and the Volunteer Field Team Dashboard.</p>
    </div>

    <div class="card card-amber">
      <div class="card-title">3. Secret Admin Control Panel (Internal Security Engine)</div>
      <p>Operates on an unindexed, obscure route protected by strong credentials and two-factor authentication. Accessible solely by the core ACTA operations and audit team. Controls campaign publishing, frame-by-frame proof inspection, escrow release triggers, automated refunds, and NGO strike enforcement.</p>
    </div>

    <h2>Access Control & Session Security Matrix</h2>
    <table>
      <thead>
        <tr>
          <th>Portal Component</th>
          <th>Authentication Method</th>
          <th>Session Lifetime</th>
          <th>Network Isolation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Public User</strong></td>
          <td>Phone OTP / Google OAuth / Guest View</td>
          <td>30 Days Persistent</td>
          <td>Public CDN Edge</td>
        </tr>
        <tr>
          <td><strong>NGO Partner</strong></td>
          <td>Magic Email Link + Device Fingerprint</td>
          <td>7 Days Secure Token</td>
          <td>Restricted Origin</td>
        </tr>
        <tr>
          <td><strong>Admin Panel</strong></td>
          <td>Hardware 2FA + IP Whitelisting</td>
          <td>4 Hours Strict Inactivity</td>
          <td>Zero-Trust Internal Network</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 04: 3-Portal Architecture</span>
    <span>PAGE 05 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 06: CHAPTER 05 — USER DASHBOARD UX
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 05</span>
    </div>

    <h1>05. User Dashboard Architecture & Dignified Impact UX</h1>

    <p>A critical founder insight: <strong>Charity must never look like a cheap gambling app or an intrusive casino.</strong> The User Dashboard is architected around dignity, clean metrics, and purposeful actions:</p>

    <div class="wireframe">
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
│  [ 📹 MY DONATIONS & PROOF ]   ──► Opens personal donation receipts    │
│                                    and direct YouTube video links.     │
│                                                                        │
│  [ 🎖️ XP & BADGES ]            ──► Opens Level progression (L1 to L10) │
│                                    and unlocked visual impact badges.  │
│                                                                        │
│  [ 🏆 COMMUNITY & LEADERBOARD ] ──► Opens ACTA Community Guild view,   │
│                                    college clan score & Top 25 board.  │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│  CURRENT VERIFIED CAUSES (7 Cards)                                     │
│  [ 🍲 Zero Hunger ]  [ 🌳 Green Earth ]  [ 📚 Child Education ] ...    │
└────────────────────────────────────────────────────────────────────────┘
    </div>

    <h2>The Three Dedicated Action Portals:</h2>
    <ul>
      <li><strong>1. [My Donations & Proof]:</strong> Displays an itemized ledger of every ₹10 contributed, including merchant GST bills, exact execution date, and a 1-click link to the official YouTube proof video.</li>
      <li><strong>2. [XP & Badges]:</strong> Houses the personal gamification engine. Displays current level (e.g. Level 2: Kind Giver), XP progress bar, and unlocked achievement rings.</li>
      <li><strong>3. [Community & Leaderboard]:</strong> Opens the competitive guild ecosystem, showing the student's campus clan (e.g. GL Bajaj BCA 2nd Year) and the City Top 25 leaderboard.</li>
    </ul>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 05: User Dashboard Architecture</span>
    <span>PAGE 06 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 07: CHAPTER 06 — NGO PARTNER ECOSYSTEM
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 06</span>
    </div>

    <h1>06. The Curated NGO Partner Ecosystem (18–20 Partners)</h1>

    <div class="card card-blue">
      <div class="card-title">The Pilot Strategy: Extreme Quality Over Unmonitored Scale</div>
      <p>While competitor platforms boast of thousands of unverified listings, ACTA enforces a tight, curated pilot of <strong>only 18 to 20 verified local NGOs</strong> across Greater Noida and Delhi NCR.</p>
    </div>

    <h2>1. The Scale Mathematics of 20 Curated Partners</h2>
    <p>A network of 20 active, dedicated grassroots NGOs possesses the logistical capacity to execute over **₹20 Lakhs to ₹50 Lakhs** in ground humanitarian delivery annually. By focusing on 20 partners, ACTA can maintain 100% human-verified quality, visit offices personally, and build deep institutional relationships.</p>

    <h2>2. White-Glove Physical Onboarding Protocol</h2>
    <p>Grassroots NGO directors are often older individuals who struggle with complex enterprise software. ACTA solves this through **White-Glove In-Person Setup**:</p>
    <ul>
      <li>An ACTA campus representative personally travels to the NGO's registered office.</li>
      <li>The representative physically verifies original registration documents: NITI Aayog NGO Darpan ID, 12A/80G certificates, and PAN card.</li>
      <li>The representative installs the partner portal, tests camera permissions on the director's device, and conducts a 30-minute training session on submitting video proof.</li>
    </ul>

    <h2>3. The 4-Step Verification Gate</h2>
    <table>
      <thead>
        <tr>
          <th>Verification Step</th>
          <th>Requirement</th>
          <th>Failure Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Darpan & 80G</strong></td>
          <td>Active registration on NGO Darpan portal.</td>
          <td>Instant rejection of application.</td>
        </tr>
        <tr>
          <td><strong>2. Physical Visit</strong></td>
          <td>Inspection of physical shelter, kitchen, or office.</td>
          <td>Mandatory re-audit within 7 days.</td>
        </tr>
        <tr>
          <td><strong>3. Bank Penny Drop</strong></td>
          <td>Automated ₹1 penny-drop validation of official NGO account.</td>
          <td>Disbursement gateway blocked.</td>
        </tr>
        <tr>
          <td><strong>4. Legal MoU Sign</strong></td>
          <td>Signed 2-strike contract binding director to proof rules.</td>
          <td>Access link withheld.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 06: Curated NGO Partner Ecosystem</span>
    <span>PAGE 07 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 08: CHAPTER 07 — NGO OPERATIONAL HIERARCHY
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 07</span>
    </div>

    <h1>07. NGO Operations: The 1+2 Redundancy Model</h1>

    <h2>1. Separation of Responsibilities: Director vs. Field Volunteers</h2>
    <p>Exposing financial accounts and payout ledgers to temporary field volunteers creates internal non-profit disputes. The NGO Partner Portal strictly segments access:</p>

    <div class="grid-2">
      <div class="card card-emerald">
        <div class="card-title">Sub-Dashboard A: NGO Director / Owner</div>
        <ul>
          <li>Views gross donations received & 90/10 split breakdown.</li>
          <li>Oversees NGO Trust Score and historical execution ratings.</li>
          <li>Assigns Volunteer Leads and Substitutes for upcoming campaigns.</li>
          <li>Direct in-dashboard priority support channel to ACTA core team.</li>
        </ul>
      </div>
      <div class="card card-blue">
        <div class="card-title">Sub-Dashboard B: Volunteer Field Team</div>
        <ul>
          <li>Clean task view: Cause name, execution venue, delivery quota.</li>
          <li>In-App Camera access (gallery upload locked).</li>
          <li>Expense receipt scanner for food/ration bills.</li>
          <li>Team roster showing names of assigned members.</li>
        </ul>
      </div>
    </div>

    <h2>2. The "1 Primary Lead + 2 Mandatory Substitutes" Operational Rule</h2>
    <p>In grassroots social work, single points of failure cause 80% of missed deadlines. If an assigned volunteer falls ill, attends a wedding, or damages their smartphone, campaigns get delayed.</p>
    <div class="card card-amber">
      <div class="card-title">Mandatory 1+2 Redundancy Protocol</div>
      <p>For every active campaign, the NGO Director <strong>must designate 1 Primary Volunteer Head + 2 Substitute Leads</strong>. All three are provisioned with camera and receipt submission rights. If the primary Head is unreachable at Hour 48, either substitute can take command, record distribution footage, and submit the proof bundle. The 4-day deadline is protected.</p>
    </div>

    <h2>3. The 2-Strike Legal Contract (MoU)</h2>
    <ul>
      <li><strong>Strike 1:</strong> Faulty or incomplete proof results in held escrow payout, Trust Score docked by 25 points, and a mandatory offline physical review.</li>
      <li><strong>Strike 2:</strong> Any deliberate submission of tampered or fake footage triggers immediate permanent blacklisting and legal recovery proceedings under the signed MoU.</li>
    </ul>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 07: NGO Operations & Redundancy</span>
    <span>PAGE 08 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 09: CHAPTER 08 — FINANCIAL ARCHITECTURE
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 08</span>
    </div>

    <h1>08. Financial Architecture & The Escrow Vault Engine</h1>

    <h2>1. The ₹10 Micro-Donation Mathematics</h2>
    <p>Traditional credit card and net banking payment gateways make micro-donations unfeasible due to fixed transaction cuts (e.g. ₹2 + 2%). ACTA exploits a massive regulatory breakthrough: **The Government of India and NPCI mandate 0% MDR on UPI peer-to-merchant payments.**</p>
    <ul>
      <li>A ₹10 donation made via Google Pay or PhonePe incurs **₹0.00 payment gateway deduction**.</li>
      <li>100% of the student's money arrives intact inside the campaign pooling vault.</li>
    </ul>

    <h2>2. The Escrow Vault & Pooling Window</h2>
    <p>Campaigns run on fixed targets (e.g. ₹50,000 for 1,000 Stray Animal Meals). Donations collect within an escrow vault over a 7-to-10 day pooling window:</p>

    <div class="wireframe">
[STUDENT DONATION: ₹10 via UPI] 
         │
         ▼
[ACTA ESCROW VAULT: 100% FROZEN] ──► Target: ₹50,000
         │
         ▼ (Target Reached 100%!)
[FUNDS UNLOCKED & DISPATCHED TO NGO]
         │
         ▼ (4-DAY EXECUTION CLOCK STARTS: 96 HOURS)
[NGO EXECUTES ON GROUND & SUBMITS PROOF]
         │
         ├─► PROOF VERIFIED: Payout Released & Closed.
         └─► SLA FAILED: 100% Refund credited to Donor Wallets!
    </div>

    <h2>3. The Automated Refund SLA</h2>
    <p>If an NGO accepts a campaign but fails to deliver verifiable video proof within the stipulated 96 hours (plus 24h grace period), the escrow engine automatically executes **100% wallet refunds to all contributing students**, and blacklists the defaulting NGO.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 08: Financial Architecture & Escrow</span>
    <span>PAGE 09 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 10: CHAPTER 09 — THE 90/10 SPLIT RULE
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 09</span>
    </div>

    <h1>09. The 90/10 Fund Split Rule & Operational Reality</h1>

    <div class="card card-emerald">
      <div class="card-title">The Foundation of Radical Financial Honesty</div>
      <p>Legacy non-profit platforms tell donors that "100% goes to the poor," while knowing that NGOs secretly siphon money to pay for transport tempos and packaging. ACTA replaces hypocrisy with formal, audited operational budgeting.</p>
    </div>

    <h2>1. The 90/10 Allocation Framework</h2>
    <table>
      <thead>
        <tr>
          <th>Bucket</th>
          <th>Share</th>
          <th>Eligible Expenses & Verification Standard</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Direct Cause Execution</strong></td>
          <td><strong>90% Mandatory</strong></td>
          <td>Raw food items, ration bags, school kits, blankets, veterinary medicines. Must match vendor invoices & GST bills.</td>
        </tr>
        <tr>
          <td><strong>NGO Operational Allowance</strong></td>
          <td><strong>10% Audited</strong></td>
          <td>Tempo/van fuel, packaging sacks, volunteer hydration & basic transport. Audited via fuel bills & transport slips.</td>
        </tr>
      </tbody>
    </table>

    <h2>2. Real Unit Economics Across 3 Campaign Tiers</h2>
    <table>
      <thead>
        <tr>
          <th>Campaign Tier</th>
          <th>Target (INR)</th>
          <th>Direct Cause (90%)</th>
          <th>NGO Ops (10%)</th>
          <th>ACTA Platform Fee (5%)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Micro Campaign</strong></td>
          <td>₹5,000.00</td>
          <td>₹4,275.00</td>
          <td>₹475.00</td>
          <td>₹250.00</td>
        </tr>
        <tr>
          <td><strong>Community Drive</strong></td>
          <td>₹20,000.00</td>
          <td>₹17,100.00</td>
          <td>₹1,900.00</td>
          <td>₹1,000.00</td>
        </tr>
        <tr>
          <td><strong>Mega Campus Drive</strong></td>
          <td>₹50,000.00</td>
          <td>₹42,750.00</td>
          <td>₹4,750.00</td>
          <td>₹2,500.00</td>
        </tr>
      </tbody>
    </table>

    <h2>3. The 5% ACTA Maintenance Fee</h2>
    <p>ACTA is structured as a sustainable social enterprise. The 5% maintenance fee is deducted only upon successful campaign delivery. It covers server bandwidth, database hosting, AI multimodal frame audits, and field team travel expenses. It ensures the platform survives independently without begging for philanthropic grants.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 09: The 90/10 Split Rule</span>
    <span>PAGE 10 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 11: CHAPTER 10 — 2-PHASE PROOF PIPELINE
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 10</span>
    </div>

    <h1>10. The 2-Phase Ground Proof Verification Pipeline</h1>

    <p>To eliminate fraud, ACTA mandates a comprehensive **2-Phase Proof Bundle** before any escrow payout is authorized:</p>

    <div class="grid-2">
      <div class="card card-blue">
        <div class="card-title">Phase 1: Supply Purchase Proof</div>
        <p><strong>Captured:</strong> At the wholesale merchant / vendor shop.</p>
        <ul>
          <li>In-app video showing the raw materials purchased (e.g. 50 kg rice, stationery boxes, blankets).</li>
          <li>High-resolution photo of the physical merchant invoice showing itemized costs and shop stamp.</li>
        </ul>
      </div>
      <div class="card card-emerald">
        <div class="card-title">Phase 2: Ground Distribution Proof</div>
        <p><strong>Captured:</strong> At the ground execution site.</p>
        <ul>
          <li>In-app video showing the actual service delivery (food being served, trees planted, notebooks given).</li>
          <li>Hardware GPS coordinates and network timestamps burned into the video metadata.</li>
        </ul>
      </div>
    </div>

    <h2>Anti-Tampering Hardware Lock: In-App Camera Only</h2>
    <div class="card card-amber">
      <div class="card-title">Gallery Uploads are Permanently Disabled</div>
      <p>Scammers typically upload pre-downloaded stock videos or recycled footage from past years. ACTA's volunteer dashboard <strong>completely disables file gallery access</strong>. Videos and receipts must be captured live through the browser/app camera API. The camera module checks camera sensor telemetry and location services in real time.</p>
    </div>

    <h2>The Proof Review Hierarchy</h2>
    <ol>
      <li><strong>Automated AI Frame Audit:</strong> Google Gemini Vision scans video frames for duplicate clip hashes, checks scene relevance, and flags tampered receipts.</li>
      <li><strong>Human Admin Review:</strong> An ACTA operations specialist verifies receipt mathematics, confirms beneficiary dignity, and approves the payout.</li>
    </ol>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 10: 2-Phase Proof Pipeline</span>
    <span>PAGE 11 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 12: CHAPTER 11 — ZERO-COST VIDEO CLOUD
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 11</span>
    </div>

    <h1>11. The Zero-Cost Video Cloud & Viral Marketing Engine</h1>

    <h2>1. The Cost Trap of Private Video Streaming</h2>
    <p>A fatal mistake made by early-stage tech startups is hosting video files on private AWS S3 buckets and streaming them via custom CDNs. Streaming thousands of hours of high-resolution video to mobile users generates monthly server bills exceeding ₹50,000, quickly exhausting startup capital. ACTA bypasses this entirely.</p>

    <h2>2. Dual-Channel Architecture (YouTube + Instagram)</h2>
    <div class="grid-2">
      <div class="card card-blue">
        <div class="card-title">Channel A: YouTube Proof Cloud (₹0 Cost)</div>
        <p><strong>Role:</strong> Permanent Transparency Archive</p>
        <ul>
          <li>Once approved, raw proof videos are uploaded to the official ACTA YouTube channel.</li>
          <li>YouTube provides global CDN caching, automatic mobile resolution scaling, and infinite hosting for **₹0**!</li>
          <li>The YouTube link is embedded directly into the donor's <em>"My Donations"</em> dashboard.</li>
        </ul>
      </div>
      <div class="card card-emerald">
        <div class="card-title">Channel B: Instagram Reels (₹0 CAC)</div>
        <p><strong>Role:</strong> Organic Viral Acquisition Engine</p>
        <ul>
          <li>ACTA media interns extract the best 30-to-45 second emotional highlights from ground footage.</li>
          <li>Formatted into vertical 9:16 Reels with high-tempo music and verified impact tags.</li>
          <li>Donors share reels on WhatsApp status, driving new students to the platform at **₹0 ad cost**.</li>
        </ul>
      </div>
    </div>

    <h2>3. Operational Realism for a Student Team</h2>
    <p>At an operating scale of 18–20 partner NGOs, the platform executes approximately **4 to 6 campaigns per week**. This generates only 4 to 6 short videos weekly. A 2-person student media team can review, verify, and edit these videos in under 3 hours a week, yet they serve **tens of thousands of student donors**!</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 11: Zero-Cost Video Cloud</span>
    <span>PAGE 12 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 13: CHAPTER 12 — DPDP ACT PRIVACY
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 12</span>
    </div>

    <h1>12. DPDP Act 2023 Compliance & Beneficiary Privacy</h1>

    <div class="card card-amber">
      <div class="card-title">Regulatory Compliance Mandate</div>
      <p>India's **Digital Personal Data Protection Act (DPDP Act 2023)** imposes stringent financial penalties for the unauthorized publication of personal visual data, particularly concerning minors, medical patients, and socio-economically vulnerable persons.</p>
    </div>

    <h2>1. The Mandatory Face-Blurring Protocol</h2>
    <p>ACTA implements a strict, automated privacy protection pipeline before any ground footage is released to the public YouTube proof archive or social media channels:</p>
    <ul>
      <li><strong>Minors (<18 Years Old):</strong> In all school kit distributions, orphanage drives, and slum educational projects, facial features of children are <strong>100% blurred by default</strong>.</li>
      <li><strong>Destitute & Hospitalized Beneficiaries:</strong> Faces of patients, destitute elderly individuals, and hospital case files are automatically masked to safeguard dignity and medical privacy.</li>
      <li><strong>Field Workers & Authorized Staff:</strong> Adult NGO operatives and volunteer heads remain unblurred as official institutional representatives.</li>
    </ul>

    <h2>2. Beneficiary Consent Acquisition</h2>
    <p>Where feasible, the partner NGO acquires verbal or written visual consent from adult beneficiaries. If explicit consent is absent, the footage is routed through the privacy filter, guaranteeing zero regulatory liability for the platform.</p>

    <h2>3. Donor Privacy Protection</h2>
    <p>Donors' sensitive financial details, phone numbers, and full legal names are never publicly exposed. On the Public Proof Ledger, contributions appear as anonymous or abbreviated identifiers (e.g., <em>"P.S. — ₹10 • GL Bajaj"</em>), maintaining complete individual privacy.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 12: DPDP Act Privacy Compliance</span>
    <span>PAGE 13 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 14: CHAPTER 13 — THE 7 STANDARD CAUSES
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 13</span>
    </div>

    <h1>13. Campaign Architecture: The 7 Standardized Causes</h1>

    <p>To maintain maximum quality and eliminate campaign clutter, ACTA strictly limits the platform to **exactly 7 causes at any given moment**:</p>

    <table>
      <thead>
        <tr>
          <th>Slot Type</th>
          <th>Cause Title & Scope</th>
          <th>Lifecycle & Infinite Rotation Logic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Permanent 1</strong></td>
          <td>🍲 <strong>Zero Hunger</strong> (Meals for homeless, daily wagers, stray animals)</td>
          <td>Infinite cyclic pool. When target completes, the next verified NGO takes over immediately.</td>
        </tr>
        <tr>
          <td><strong>Permanent 2</strong></td>
          <td>🌳 <strong>Green Earth</strong> (Tree plantation, cleanup drives & sapling care)</td>
          <td>Infinite cyclic pool. Runs continuously across educational and urban belts in NCR.</td>
        </tr>
        <tr>
          <td><strong>Permanent 3</strong></td>
          <td>📚 <strong>Child Education</strong> (School bags, notebooks, study kits)</td>
          <td>Infinite cyclic pool. Partners with verified orphanages and slum learning centers.</td>
        </tr>
        <tr>
          <td><strong>Permanent 4</strong></td>
          <td>👴 <strong>Elder Care</strong> (Medicines, hygiene kits & shelter support)</td>
          <td>Infinite cyclic pool. Dedicated to supporting destitute senior citizens and old-age homes.</td>
        </tr>
        <tr>
          <td><strong>Permanent 5</strong></td>
          <td>🧵 <strong>Women Empowerment</strong> (Monthly ration kits & vocational aids)</td>
          <td>Infinite cyclic pool. Provides essential nutrition and self-help tools to low-income widows.</td>
        </tr>
        <tr>
          <td><strong>Temporary 1</strong></td>
          <td>🚨 <strong>Disaster & Crisis Relief</strong> (Floods, winter cold waves, earthquakes)</td>
          <td>Dynamic slot. Activates during emergency seasons (e.g. winter blanket drive); retires upon completion.</td>
        </tr>
        <tr>
          <td><strong>Temporary 2</strong></td>
          <td>🐾 <strong>Emergency Stray Rescue</strong> (Urgent animal surgeries & trauma care)</td>
          <td>Dynamic slot. Rotates based on critical, time-sensitive veterinary rescue operations.</td>
        </tr>
      </tbody>
    </table>

    <h2>Why NGOs Cannot Self-Create Campaigns</h2>
    <p>On legacy crowdfunding sites, anyone can write an unverified story and request arbitrary amounts. On ACTA, **only the ACTA Admin creates campaigns based on standardized unit costs** (e.g. ₹35 per meal, ₹150 per stationery kit). NGOs merely apply to execute approved campaigns. This guarantees audited financial targets.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 13: 7 Standardized Causes</span>
    <span>PAGE 14 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 15: CHAPTER 14 — GAMIFICATION ENGINE
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 14</span>
    </div>

    <h1>14. Gamification Engine: The ₹1 = 10 XP Economy</h1>

    <h2>1. The Psychology of Experience Points (XP)</h2>
    <p>Students thrive on instant positive reinforcement. Donating ₹10 and receiving nothing in return feels cold. On ACTA, every single rupee donated immediately translates into platform experience points:</p>
    <div class="card card-emerald">
      <div class="card-title">The Master XP Formula</div>
      <p><strong>1 Rupee Donated = 10 Acta XP</strong></p>
      <p>A ₹10 donation triggers an immediate +100 XP reward animation, activating genuine user dopamine!</p>
    </div>

    <h2>2. Additional XP Earning Triggers (Beyond Direct Money)</h2>
    <p>To ensure that students with limited pocket money can still compete through leadership and dedication, XP is awarded across multiple activity vectors:</p>
    <table>
      <thead>
        <tr>
          <th>Action / Trigger</th>
          <th>XP Reward</th>
          <th>Strategic Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Direct Micro-Donation</strong></td>
          <td>Amount × 10 XP (e.g. ₹20 = 200 XP)</td>
          <td>Base micro-giving incentive.</td>
        </tr>
        <tr>
          <td><strong>Guild Milestone Bonus</strong></td>
          <td>+200 XP for all active members</td>
          <td>Encourages teamwork within the college clan.</td>
        </tr>
        <tr>
          <td><strong>Top 25 City Rank Boost</strong></td>
          <td>+500 XP bonus</td>
          <td>Drives healthy inter-college competitive pride.</td>
        </tr>
        <tr>
          <td><strong>3-Week Consistency Streak</strong></td>
          <td>+150 XP bonus</td>
          <td>Builds a recurring weekly giving habit.</td>
        </tr>
        <tr>
          <td><strong>Watch & Verify Proof Video</strong></td>
          <td>+20 XP bonus</td>
          <td>Incentivizes donors to inspect transparency footage.</td>
        </tr>
      </tbody>
    </table>

    <h2>3. Dual Personality UX: Gamers vs. Silent Givers</h2>
    <p>The platform never forces gaming on donors who prefer quiet charity. The main screen displays clean impact metrics. Gamification triggers only when a student enters the <em>[XP & Badges]</em> or <em>[Community]</em> sections.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 14: Gamification & XP Economy</span>
    <span>PAGE 15 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 16: CHAPTER 15 — 10-LEVEL PROGRESSION LADDER
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 15</span>
    </div>

    <h1>15. The 10-Level Exponential Giving Ladder</h1>

    <p>In game design (modern community systems), leveling up follows an **exponential progression curve**. If Level 2 is unlocked at just ₹50, the achievement loses prestige. On ACTA, **Level 2 requires at least ₹500 (5,000 XP)**, demanding sustained commitment:</p>

    <table>
      <thead>
        <tr>
          <th>Level</th>
          <th>Level Title</th>
          <th>XP Required</th>
          <th>Direct Giving Equiv.</th>
          <th>Profile Recognition & Perks</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Level 01</strong></td>
          <td><strong>Seed Giver</strong> 🌱</td>
          <td>0 – 4,999 XP</td>
          <td>₹0 – ₹499</td>
          <td>Bronze Seed Tag. Unlocks upon very first ₹10 act.</td>
        </tr>
        <tr>
          <td><strong>Level 02</strong></td>
          <td><strong>Kind Giver</strong> 🤝</td>
          <td>5,000 – 11,999 XP</td>
          <td><strong>₹500+</strong></td>
          <td>Silver Border Ring. Community chat access unlocked.</td>
        </tr>
        <tr>
          <td><strong>Level 03</strong></td>
          <td><strong>Active Giver</strong> ⭐</td>
          <td>12,000 – 24,999 XP</td>
          <td>₹1,200+</td>
          <td>Polished Silver Ring + Guild shoutout badge.</td>
        </tr>
        <tr>
          <td><strong>Level 04</strong></td>
          <td><strong>Impact Giver</strong> 🔷</td>
          <td>25,000 – 49,999 XP</td>
          <td>₹2,500+</td>
          <td>Sapphire Blue Ring + Voting power on next cause.</td>
        </tr>
        <tr>
          <td><strong>Level 05</strong></td>
          <td><strong>Dedicated Giver</strong> 🛡️</td>
          <td>50,000 – 99,999 XP</td>
          <td>₹5,000+</td>
          <td>Gold Shield Ring + Featured on Campus Board.</td>
        </tr>
        <tr>
          <td><strong>Level 06</strong></td>
          <td><strong>Community Pillar</strong> 🏛️</td>
          <td>1,00,000 – 1,99,999 XP</td>
          <td>₹10,000+</td>
          <td>Radiant Gold Ring + Authority to create Campus Guilds.</td>
        </tr>
        <tr>
          <td><strong>Level 07</strong></td>
          <td><strong>Change Maker</strong> ⚔️</td>
          <td>2,00,000 – 3,99,999 XP</td>
          <td>₹20,000+</td>
          <td>Emerald Ring + Direct invite to annual NGO field audits.</td>
        </tr>
        <tr>
          <td><strong>Level 08</strong></td>
          <td><strong>Master Benefactor</strong> 💎</td>
          <td>4,00,000 – 6,99,999 XP</td>
          <td>₹40,000+</td>
          <td>Ruby Ring + Priority sponsor matching on contributions.</td>
        </tr>
        <tr>
          <td><strong>Level 09</strong></td>
          <td><strong>Grand Philanthropist</strong> 🌟</td>
          <td>7,00,000 – 9,99,999 XP</td>
          <td>₹70,000+</td>
          <td>Glowing Amethyst Ring + City Hall of Fame Top Tier.</td>
        </tr>
        <tr>
          <td><strong>Level 10</strong></td>
          <td><strong>The Crown Legend</strong> 👑</td>
          <td>10,00,000+ XP</td>
          <td>₹1,00,000+</td>
          <td><strong>Animated Diamond Crown Ring</strong> + National Resence Impact Award.</td>
        </tr>
      </tbody>
    </table>

    <p>Higher levels are achievable not just through personal money, but by leading a successful Guild and maintaining weekly consistency streaks!</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 15: 10-Level Progression Ladder</span>
    <span>PAGE 16 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 17: CHAPTER 16 — CAMPUS GUILD WARS
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 16</span>
    </div>

    <h1>16. The ACTA Campus Guild Campus Guilds & Clan Wars</h1>

    <h2>1. The Power of Guild Mechanics in College Culture</h2>
    <p>Donating alone feels isolated. Donating as an organized **Guild** creates powerful, positive peer momentum. In collegiate campus culture, students unite around shared pride and collective achievement. On ACTA:</p>
    <ul>
      <li>Students join their institutional community (e.g., <em>GL Bajaj BCA 2nd Year</em>, <em>Galgotias CS Club</em>, <em>Hostel Block B</em>).</li>
      <li>When a member donates ₹10, both their personal score and their **Guild Score increase simultaneously**.</li>
      <li>Students naturally urge their friends on WhatsApp: <em>"We are #3 in Greater Noida, just 30 of us donating ₹10 will push us past Bennett University to #2!"</em></li>
    </ul>

    <h2>2. Guild Tier Progression Ladder</h2>
    <table>
      <thead>
        <tr>
          <th>Guild Tier</th>
          <th>Total Guild Funding</th>
          <th>Perks & Visual Unlocks</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Tier 1: Rising Clan</strong></td>
          <td>₹0 – ₹4,999</td>
          <td>Standard Guild tag; private clan discussion feed.</td>
        </tr>
        <tr>
          <td><strong>Tier 2: Impact Brigade</strong></td>
          <td>₹5,000 – ₹19,999</td>
          <td>Silver Clan Shield; featured in departmental newsletter.</td>
        </tr>
        <tr>
          <td><strong>Tier 3: Campus Titans</strong></td>
          <td>₹20,000 – ₹49,999</td>
          <td>Gold Clan Shield; custom cause sponsorship rights.</td>
        </tr>
        <tr>
          <td><strong>Tier 4: Apex Guild</strong></td>
          <td>₹50,000+</td>
          <td>Crown Diamond Shield; official campus trophy from Resence.</td>
        </tr>
      </tbody>
    </table>

    <h2>3. Community Creation Verification Guardrail</h2>
    <p>To prevent spam, arbitrary individuals cannot create 500 fake guilds. A student leader must submit their college ID card or verified institutional email (`@glbajaj.org`) to instantiate an official Campus Guild.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 16: Campus Guild Wars</span>
    <span>PAGE 17 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 18: CHAPTER 17 — LEADERBOARDS & ANTI-SHAMING
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 17</span>
    </div>

    <h1>17. The Top 25 Leaderboard & Anti-Shaming Privacy Rule</h1>

    <div class="card card-emerald">
      <div class="card-title">The Anti-Shaming Design Philosophy</div>
      <p>Publicly listing every individual's exact score creates toxic humiliation. A student who could only afford ₹10 feels ashamed seeing a peer with ₹500. ACTA solves this through a brilliant privacy rule.</p>
    </div>

    <h2>1. The Anti-Shaming Privacy Rule</h2>
    <ul>
      <li><strong>Individual scores remain completely private.</strong> A student only sees their own personal progress, level, and unlocked badges.</li>
      <li>The public leaderboard showcases **strictly the Top 25** performers at two geographical tiers:
        <ol>
          <li><strong>Top 25 Communities / Guilds (City & National Level)</strong></li>
          <li><strong>Top 25 Donors (City & National Level — Hall of Fame)</strong></li>
        </ol>
      </li>
      <li>Casual donors are never exposed to public ranking, preserving dignity and emotional comfort.</li>
    </ul>

    <h2>2. Geographical Scoping: City vs. Country</h2>
    <p>Students care far more about local college rivalry than distant national figures. The leaderboard defaults to the **City Level (Greater Noida / Delhi NCR)**:</p>
    <ul>
      <li>Local Rivalry: GL Bajaj vs. Galgotias University vs. Sharda University vs. Bennett University.</li>
      <li>National Tier: Highlights top performing institutional guilds across India during major festival giving campaigns (e.g. Diwali Hunger Relief).</li>
    </ul>

    <h2>3. Monthly Season Resets</h2>
    <p>To prevent legacy accounts from permanently monopolizing the Top 25, the competitive board resets every 30 days. Top performing guilds receive permanent trophy pins in their clan showcase, while giving new student batches an equal chance to win the current month's race.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 17: Leaderboards & Anti-Shaming</span>
    <span>PAGE 18 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 19: CHAPTER 18 — THE AI LAYER
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 18</span>
    </div>

    <h1>18. The AI Layer: ACTA AI Advisor & Gemini Vision Engine</h1>

    <p>ACTA integrates Google Gemini API across two specialized operational roles:</p>

    <div class="grid-2">
      <div class="card card-blue">
        <div class="card-title">Student Facing: ACTA AI Advisor (Gemini LLM)</div>
        <ul>
          <li><strong>Pocket Money Impact Planner:</strong> A student chats: <em>"I have ₹35 left in my UPI wallet, where does it help most?"</em> Gemini analyzes current campaign progress and directs the funds to the cause closest to completion.</li>
          <li><strong>Personalized Monthly Story Generator:</strong> Generates beautiful, emotional impact stories: <em>"Piyush, this month your small acts provided 14 stray dog meals and funded stationery for 2 orphan children."</em></li>
          <li><strong>Cause Discovery:</strong> Matches causes to student interests (animal welfare, green campus, education).</li>
        </ul>
      </div>
      <div class="card card-emerald">
        <div class="card-title">Admin Facing: Gemini Vision Multimodal Engine</div>
        <ul>
          <li><strong>Receipt & Bill OCR Analysis:</strong> Scans submitted vendor invoices, extracts GST numbers, item costs, and checks mathematical totals against campaign budget lines.</li>
          <li><strong>Video Frame Tamper Detection:</strong> Extracts frames from in-app camera footage, computes perceptual image hashes, and cross-checks against online stock video clips to detect fraud.</li>
          <li><strong>Automated Face Detection:</strong> Identifies minors and vulnerable individuals to assist the automated face-blurring pipeline before YouTube export.</li>
        </ul>
      </div>
    </div>

    <h2>Technical Integration Architecture</h2>
    <div class="wireframe">
[STUDENT INPUT] ──► Gemini 1.5 Flash API ──► Instant Conversational Impact Advice
[NGO VIDEO]     ──► Gemini Vision API    ──► Frame Hash Verification & Receipt Math
    </div>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 18: The AI Layer</span>
    <span>PAGE 19 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 20: CHAPTER 19 — VOLUNTEER SAFETY SHIELD
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 19</span>
    </div>

    <h1>19. The Zero-Liability Volunteer Safety Shield</h1>

    <div class="card card-emerald">
      <div class="card-title">The Legal Firewall That Protects the Startup</div>
      <p>Early prototypes frequently collapse because student founders attempt to recruit, manage, and dispatch volunteers directly to slums, accident zones, or flood relief camps. This creates massive criminal and civil liability risks.</p>
    </div>

    <h2>1. Why ACTA Dropped Direct Volunteer Recruitment</h2>
    <ul>
      <li><strong>Physical Safety & Accidents:</strong> If an 18-year-old student gets injured traveling to a dangerous location, the platform faces severe civil and criminal negligence suits.</li>
      <li><strong>Police Verification Overhead:</strong> Verifying criminal background checks for thousands of student volunteers across cities is operationally impossible for a seed-stage startup.</li>
      <li><strong>Harassment Liabilities:</strong> Managing mixed-gender volunteer field teams without corporate security infrastructure creates unacceptable risk.</li>
    </ul>

    <h2>2. The Operational Firewall Mechanism</h2>
    <p>ACTA operates strictly as a **Technology, Escrow, and Verification Infrastructure Layer**:</p>
    <ul>
      <li>ACTA never hires, dispatches, or directs individual volunteers.</li>
      <li>On-ground execution is conducted **100% by the verified partner NGO** using their own pre-existing, registered staff and vetted volunteers.</li>
      <li>The partner NGO assumes **100% legal, physical, and insurance liability** for all ground activities.</li>
    </ul>

    <h2>3. When a Student Clicks "Volunteer in Person"</h2>
    <p>If a student user taps the <em>"Volunteer on Ground"</em> link on ACTA, the platform displays a clear legal notice: <em>"Ground volunteering is organized directly by our registered partner NGOs."</em> The student is redirected to the NGO's official portal. ACTA remains completely insulated from physical liability.</p>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 19: Volunteer Safety Shield</span>
    <span>PAGE 20 OF 21</span>
  </div>
</div>
<div class="page-break"></div>

<!-- ==========================================
     PAGE 21: CHAPTER 20 — ROADMAP & INCUBATION ASK
     ========================================== -->
<div class="page">
  <div>
    <div class="header-bar">
      <span>ACTA by Resence — Master Product Bible</span>
      <span class="brand">CHAPTER 20</span>
    </div>

    <h1>20. Founder Ground Reality, Roadmap & GLBCRI Ask</h1>

    <h2>1. Founder Profile & Current Stage (100% Ground Truth)</h2>
    <ul>
      <li><strong>Founder:</strong> Piyush Singh (18 Years Old, BCA 2nd Year, GL Bajaj Institute of Management, Greater Noida).</li>
      <li><strong>Current Stage:</strong> Functional interactive web prototype live at `resence.in` / `acta.resence.in`. Complete system architecture, escrow rules, and 20-page PRD specifications locked.</li>
      <li><strong>NGO Status:</strong> No formal NGO MoUs currently active. Cold outreach as an independent student lacks institutional weight.</li>
    </ul>

    <h2>2. The 90-Day Execution Roadmap</h2>
    <table>
      <thead>
        <tr>
          <th>Phase</th>
          <th>Timeline</th>
          <th>Core Milestones</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Phase 1: Incubation & Partner MoUs</strong></td>
          <td>Days 1 – 30</td>
          <td>Secure GLBCRI incubation letterhead; onboard first 10 local Greater Noida NGOs via offline visits.</td>
        </tr>
        <tr>
          <td><strong>Phase 2: Closed Campus Pilot</strong></td>
          <td>Days 31 – 60</td>
          <td>Deploy 30-day pilot across GL Bajaj Knowledge Park hostels; target 1,000 student givers & 10 completed campaigns.</td>
        </tr>
        <tr>
          <td><strong>Phase 3: Inter-College Campus Impact League</strong></td>
          <td>Days 61 – 90</td>
          <td>Expand to Galgotias, Sharda, and Bennett University; activate the Top 25 City Guild leaderboard.</td>
        </tr>
      </tbody>
    </table>

    <h2>3. The Specific Ask from GLBCRI (Bharat Udyam Sangam 2026)</h2>
    <ol>
      <li><strong>Institutional Credibility & Letterhead:</strong> Introducing ACTA under GL Bajaj / GLBCRI official backing to 18–20 verified NGOs in Greater Noida and Noida.</li>
      <li><strong>Campus Pilot Authorization:</strong> Permission to run an official 30-day student micro-giving pilot across GL Bajaj Knowledge Park hostels and academic departments.</li>
      <li><strong>Pre-Incubation Mentorship:</strong> Legal structuring for NGO MoUs, Section 8/Pvt Ltd formalization, and seed grant guidance.</li>
    </ol>

    <div class="card card-emerald" style="margin-top: 18px; text-align: center;">
      <div class="card-title">ACTA by Resence — Small Acts, Big Impacts.</div>
      <p>Master Product Specification & Architecture Bible • Approved by Piyush Singh, Founder & CEO</p>
    </div>
  </div>

  <div class="footer-bar">
    <span>ACTA by Resence • Chapter 20: Roadmap & Incubation Ask</span>
    <span>PAGE 21 OF 21</span>
  </div>
</div>

</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_file}")

# Compile to PDF via Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Compiling Master 20-Page PDF via Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    page_count = len(reader.pages)
    print(f"SUCCESS: Master PDF compiled successfully!")
    print(f"Exact Page Count: {page_count} Pages")
    print(f"File Size: {os.path.getsize(pdf_file)} bytes")
else:
    print(f"PDF creation failed: {result.stderr}")
