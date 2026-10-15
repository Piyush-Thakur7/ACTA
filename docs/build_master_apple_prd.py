import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — Master Product Specification & Architecture Bible</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
    @bottom-right {
      content: counter(page);
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #111827;
    background-color: #FFFFFF;
    line-height: 1.55;
    font-size: 11pt;
    -webkit-font-smoothing: antialiased;
  }

  .page-break {
    page-break-after: always;
  }

  /* Cover Page */
  .cover {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 40px 20px 20px 20px;
    page-break-after: always;
    border-bottom: 2px solid #E5E7EB;
  }

  .cover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 20px;
  }

  .brand-badge {
    background: #0F172A;
    color: #FFFFFF;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 11pt;
    letter-spacing: 2px;
    padding: 6px 16px;
    border-radius: 6px;
    display: inline-block;
  }

  .doc-type {
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #6B7280;
    font-weight: 600;
  }

  .cover-center {
    margin-top: 60px;
    margin-bottom: 60px;
  }

  .hero-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 42pt;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.08;
    color: #0F172A;
    margin-bottom: 12px;
  }

  .hero-title span {
    color: #059669;
  }

  .hero-tagline {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18pt;
    color: #374151;
    font-weight: 600;
    margin-bottom: 24px;
    letter-spacing: -0.5px;
  }

  .hero-desc {
    font-size: 12pt;
    color: #4B5563;
    max-width: 650px;
    line-height: 1.6;
    margin-bottom: 30px;
  }

  .pill-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 40px;
  }

  .pill {
    background: #F3F4F6;
    color: #1F2937;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 100px;
    border: 1px solid #E5E7EB;
  }

  .pill.emerald {
    background: #ECFDF5;
    color: #065F46;
    border-color: #A7F3D0;
  }

  .pill.indigo {
    background: #EEF2FF;
    color: #3730A3;
    border-color: #C7D2FE;
  }

  .cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    background: #F9FAFB;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
  }

  .meta-item h5 {
    font-size: 7.5pt;
    text-transform: uppercase;
    color: #6B7280;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }

  .meta-item p {
    font-size: 9.5pt;
    font-weight: 600;
    color: #111827;
  }

  /* Document Typography */
  h1 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 20pt;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.5px;
    margin-top: 24px;
    margin-bottom: 14px;
    border-bottom: 2px solid #E5E7EB;
    padding-bottom: 8px;
  }

  h2 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14pt;
    font-weight: 700;
    color: #1E293B;
    margin-top: 20px;
    margin-bottom: 8px;
    letter-spacing: -0.3px;
  }

  h3 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 11.5pt;
    font-weight: 700;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
  }

  p {
    margin-bottom: 10px;
    color: #374151;
  }

  ul, ol {
    margin-left: 20px;
    margin-bottom: 12px;
    color: #374151;
  }

  li {
    margin-bottom: 4px;
  }

  strong {
    color: #0F172A;
    font-weight: 600;
  }

  /* Apple-Style Cards */
  .card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }

  .card-highlight {
    background: #F8FAFC;
    border-left: 4px solid #059669;
  }

  .card-blue {
    background: #F8FAFC;
    border-left: 4px solid #2563EB;
  }

  .card-amber {
    background: #FFFBEB;
    border-left: 4px solid #D97706;
  }

  .card-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 11pt;
    color: #0F172A;
    margin-bottom: 6px;
  }

  /* Clean Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 18px 0;
    font-size: 9pt;
  }

  th {
    background: #0F172A;
    color: #FFFFFF;
    text-align: left;
    padding: 9px 12px;
    font-weight: 600;
    font-size: 8.5pt;
    letter-spacing: 0.5px;
    border-top: 1px solid #0F172A;
  }

  td {
    padding: 8px 12px;
    border-bottom: 1px solid #E5E7EB;
    color: #374151;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background: #F9FAFB;
  }

  /* Wireframe Container */
  .wireframe {
    background: #0F172A;
    color: #F8FAFC;
    padding: 18px;
    border-radius: 10px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    margin: 14px 0;
    white-space: pre;
    overflow-x: hidden;
  }

  /* Metrics Grid */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }

  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 14px;
  }

  .stat-box {
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 12px;
    text-align: center;
  }

  .stat-number {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18pt;
    font-weight: 800;
    color: #059669;
    margin-bottom: 2px;
  }

  .stat-label {
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #6B7280;
    font-weight: 600;
  }

  /* Badges */
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .badge-success { background: #DCFCE7; color: #166534; }
  .badge-danger { background: #FEE2E2; color: #991B1B; }
  .badge-info { background: #DBEAFE; color: #1E40AF; }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="cover-top">
    <div class="brand-badge">RESENCE ECOSYSTEM</div>
    <div class="doc-type">INTERNAL PRODUCT BIBLE & SSOT • v2.0</div>
  </div>

  <div class="cover-center">
    <div class="hero-title">ACTA <span>by Resence</span></div>
    <div class="hero-tagline">Small Acts, Big Impacts.</div>
    <div class="hero-desc">
      A Proof-Verified Micro-Donation & Civic Accountability Network. Transforming everyday pocket change into 100% verified grassroots impact through 0% MDR UPI micro-giving, conditional milestone escrow, and 4-day geotagged video proof.
    </div>

    <div class="pill-row">
      <div class="pill emerald">0% MDR UPI Micro-Giving</div>
      <div class="pill indigo">Milestone Escrow Vault</div>
      <div class="pill">96-Hour Geotagged Video Proof</div>
      <div class="pill">Free Fire Style Guild Wars</div>
      <div class="pill emerald">DPDP Act 2023 Compliant</div>
    </div>
  </div>

  <div class="cover-meta-grid">
    <div class="meta-item">
      <h5>Author & Founder</h5>
      <p>Piyush Singh (CEO, Resence)</p>
    </div>
    <div class="meta-item">
      <h5>Academic & Campus Base</h5>
      <p>BCA 2nd Year, GL Bajaj (GLBIM)</p>
    </div>
    <div class="meta-item">
      <h5>Primary Incubation Target</h5>
      <p>Bharat Udyam Sangam 2026 (GLBCRI)</p>
    </div>
    <div class="meta-item">
      <h5>Document Classification</h5>
      <p>Core Engineering & Strategy SSOT</p>
    </div>
    <div class="meta-item">
      <h5>Pilot Territory</h5>
      <p>Greater Noida & Delhi NCR</p>
    </div>
    <div class="meta-item">
      <h5>Release Date</h5>
      <p>October 2026 (Release v2.0)</p>
    </div>
  </div>
</div>

<!-- CHAPTER 1 -->
<h1>01. The Identity, Etymology & Meaning of ACTA</h1>

<div class="card card-highlight">
  <div class="card-title">What Does ACTA Mean, and What is its Role in Our Project?</div>
  <p>The name <strong>ACTA</strong> is not an arbitrary startup buzzword or an AI-generated acronym. It is a historic, linguistic anchor for our entire philosophy.</p>
</div>

<h3>1. Classical Latin Origin & Roman History</h3>
<p>In Classical Latin, <strong>Acta</strong> is the plural of <em>Actum</em>, which literally translates to <strong>"Things Done"</strong>, <strong>"Deeds Accomplished"</strong>, or <strong>"Official Records."</strong></p>
<p>Historically, around 131 BC, the Roman Republic instituted the <strong>Acta Diurna</strong> (literally <em>"Daily Deeds / Daily Acts"</em>). Carved in stone or metal and hung in the public Forum, it was civilization's very first public transparency gazette, ensuring citizens could verify daily state announcements, grain distributions, and legal decisions with their own eyes.</p>

<h3>2. The Exact Role of ACTA in Our Architecture</h3>
<ul>
  <li><strong>Every Donation is an "Acta":</strong> On our platform, a ₹10 donation is not an anonymous financial transaction; it is an individual <em>Acta</em>—a recorded, verified deed of human compassion.</li>
  <li><strong>The Modern Public Ledger:</strong> Just as ancient Rome had the <em>Acta Diurna</em>, our platform acts as India's digital public transparency ledger. Every rupee donated is proven with video before the record is permanently published.</li>
  <li><strong>Fusion with the Locked Tagline:</strong> The locked tagline is <strong>"Small Acts, Big Impacts."</strong> The word <em>"Acts"</em> in the tagline is the exact English meaning of the Latin root <em>Acta</em>. The brand name and the tagline are linguistically fused.</li>
</ul>

<div class="card card-blue">
  <div class="card-title">Corporate Parent Structure: Alphabet & Google Architecture</div>
  <p><strong>Resence</strong> is the parent umbrella company (`https://www.resence.in`). It holds the technical infrastructure, governance, and multi-product roadmap. <strong>ACTA</strong> is the flagship civic-fintech product (`https://acta.resence.in`), operating as <em>"ACTA by Resence."</em></p>
</div>

<!-- CHAPTER 2 -->
<h1>02. Ground Reality & The Gen Z Micro-Giving Opportunity</h1>

<div class="grid-3">
  <div class="stat-box">
    <div class="stat-number">67.5%</div>
    <div class="stat-label">Donor Trust Deficit</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">₹540 B</div>
    <div class="stat-label">India Giving Market</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">0% MDR</div>
    <div class="stat-label">Govt Mandated UPI Cut</div>
  </div>
</div>

<h3>The Two Critical Failures in Indian Charity:</h3>
<ol>
  <li><strong>The 67.5% Cynicism Chasm:</strong> India has 5,25,000+ registered NGOs, but 67.5% of educated urban youth refuse to donate online. News of embezzlement, luxury NGO administrative spending, and phantom beneficiaries has broken trust. Donors ask one question: <em>"Where did my money actually go?"</em> Traditional platforms answer with a text email. ACTA answers with in-app video proof.</li>
  <li><strong>The "Small Money" Embarrassment Barrier for Gen Z:</strong> College students survive on pocket money. A student walking into a physical donation drive with ₹20 or ₹40 feels embarrassed because traditional charities dismiss small amounts as petty change. ACTA eliminates this embarrassment by providing <strong>dignity to micro-giving</strong>. When 1,000 GL Bajaj students pool ₹10, it creates ₹10,000—enough to feed 200 stray animals or provide school kits to 50 children.</li>
</ol>

<!-- CHAPTER 3 -->
<div class="page-break"></div>
<h1>03. Direct Competitor Analysis: Why ACTA Wins Over Milaap & Ketto</h1>

<div class="card card-amber">
  <div class="card-title">The Fundamental Paradigm Shift</div>
  <p>Legacy platforms like <strong>Milaap, Ketto, and GiveIndia</strong> were built 15 years ago for working professionals donating high amounts through credit cards. They operate as <em>unmonitored payment pipelines</em>. ACTA is built for <strong>Gen Z on UPI</strong>, operating as a <em>zero-trust verification engine</em>.</p>
</div>

<table>
  <thead>
    <tr>
      <th>Comparison Parameter</th>
      <th>Legacy Crowdfunding (Milaap, Ketto)</th>
      <th>ACTA by Resence</th>
      <th>Why Donors Choose ACTA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Minimum Ticket Size</strong></td>
      <td>₹500 to ₹1,000+ (High financial friction)</td>
      <td><strong>₹10 to ₹50 via UPI</strong></td>
      <td>Zero pocket money guilt; every student can participate daily.</td>
    </tr>
    <tr>
      <td><strong>Proof of Ground Execution</strong></td>
      <td>Opaque. Only a tax receipt & generic email update.</td>
      <td><strong>Mandatory 4-day geotagged video + store receipts.</strong></td>
      <td>You see the exact food plate delivered within 96 hours.</td>
    </tr>
    <tr>
      <td><strong>Fund Custody & Escrow</strong></td>
      <td>100% money released upfront to campaigner without execution proof.</td>
      <td><strong>100% frozen in Escrow Vault.</strong> Disbursed only after proof verification.</td>
      <td>Zero risk of campaigner running away with donor funds.</td>
    </tr>
    <tr>
      <td><strong>Target Audience & Culture</strong></td>
      <td>Older adults, HNIs; driven by emotional guilt.</td>
      <td><strong>Gen Z, college youth; driven by Free Fire Guild pride.</strong></td>
      <td>Charity becomes an engaging, uplifting campus habit.</td>
    </tr>
    <tr>
      <td><strong>Fee Structure & Deductions</strong></td>
      <td>5% to 10% platform cut + 2% payment gateway + guilt-trip tipping prompts.</td>
      <td><strong>5% flat platform maintenance fee; 0% UPI gateway cut.</strong></td>
      <td>Complete financial transparency; no hidden tipping tricks.</td>
    </tr>
    <tr>
      <td><strong>NGO Onboarding Quality</strong></td>
      <td>Open marketplace; anyone can submit a cause with unverified claims.</td>
      <td><strong>Curated 18–20 local NGOs, verified physically offline.</strong></td>
      <td>Eliminates fake NGOs and phantom beneficiary scams.</td>
    </tr>
  </tbody>
</table>

<!-- CHAPTER 4 -->
<h1>04. The 3-Portal Architecture & Role-Based Access</h1>

<div class="card">
  <p>To ensure bulletproof operational security, ACTA strictly segregates user flows into <strong>three independent dashboards</strong>:</p>
</div>

<div class="grid-3">
  <div class="card card-highlight">
    <div class="card-title">1. Public User Portal</div>
    <p><strong>URL:</strong> `acta.resence.in`</p>
    <p>Publicly accessible worldwide. Browse 7 curated causes, 1-click UPI checkout, access personal impact counters, and view the YouTube public proof ledger.</p>
  </div>
  <div class="card card-blue">
    <div class="card-title">2. NGO Partner Portal</div>
    <p><strong>Access:</strong> Invite-Only Magic Link</p>
    <p>Accessible only via unique authenticated link sent to verified NGO official email. Houses the Director Dashboard and the Volunteer Field Team Dashboard.</p>
  </div>
  <div class="card card-amber">
    <div class="card-title">3. Admin Control Panel</div>
    <p><strong>Route:</strong> Hidden & Role-Protected</p>
    <p>Unindexed URL with 2FA. Core team manages causes, inspects AI frame audits, verifies receipts, and triggers escrow disbursements or refunds.</p>
  </div>
</div>

<!-- CHAPTER 5 -->
<div class="page-break"></div>
<h1>05. Curated NGO Partner Ecosystem & 1+2 Redundancy Model</h1>

<h3>5.1 The 18–20 Curated NGO Pilot Strategy</h3>
<p>Amateur platforms claim they will onboard 10,000 NGOs on Day 1. ACTA focuses on <strong>extreme quality over unmonitored quantity</strong>:</p>
<ul>
  <li>We pilot exclusively with <strong>18 to 20 verified local NGOs</strong> in Greater Noida and Delhi NCR.</li>
  <li><strong>White-Glove Physical Setup:</strong> An ACTA representative visits each NGO office in person, inspects physical facilities, verifies NGO Darpan ID and 12A/80G tax exemptions, and assists them in setting up their dashboard.</li>
</ul>

<h3>5.2 NGO Internal Hierarchy: Owner vs. Field Volunteers</h3>
<div class="wireframe">
┌────────────────────────────────────────────────────────────────────────┐
│                   NGO INTERNAL DASHBOARD ARCHITECTURE                  │
├────────────────────────────────────────────────────────────────────────┤
│  [ SUB-DASHBOARD A: NGO DIRECTOR / OWNER ]                             │
│  • Total campaign funds received & 90/10 split tracking                │
│  • Direct priority ACTA support chat channel                           │
│  • NGO Trust Score & performance rating metrics                        │
│  • Ability to invite Volunteer Head and 2 Substitutes                  │
├────────────────────────────────────────────────────────────────────────┤
│  [ SUB-DASHBOARD B: VOLUNTEER FIELD TEAM ]                             │
│  • Clean view: Task name, execution location & team roster             │
│  • IN-APP CAMERA ACCESS ONLY (Gallery uploads permanently locked)       │
│  • Receipt upload scanner & Proof Bundle submission button             │
└────────────────────────────────────────────────────────────────────────┘
</div>

<h3>5.3 The "1 Primary Lead + 2 Mandatory Substitutes" Operational Rule</h3>
<p>The single greatest operational vulnerability in Indian grassroots charity is volunteer unreliability. If a volunteer gets sick, loses their phone, or attends a family emergency, the entire execution stalls.</p>
<p><strong>ACTA Mandate:</strong> For every campaign, the NGO Director must assign <strong>1 Primary Volunteer Head + 2 Substitute Leads</strong>. All three hold app camera permissions. If the primary Head drops out, either substitute immediately records footage, ensuring the <strong>4-day deadline is never missed</strong>.</p>

<h3>5.4 The 2-Strike Legal MoU Agreement</h3>
<ul>
  <li><strong>Strike 1 (Faulty/Unclear Proof):</strong> Funds frozen. Official warning issued. Mandatory offline meeting with ACTA founder.</li>
  <li><strong>Strike 2 (Fraud / Tampered Proof):** Immediate permanent blacklisting on ACTA + legal action initiated under the signed binding agreement.</li>
</ul>

<!-- CHAPTER 6 -->
<h1>06. Financial Architecture, Escrow Vault & The 90/10 Split Rule</h1>

<h3>6.1 The Pooling Vault & 4-Day Execution Countdown</h3>
<p>Campaigns run on fixed financial targets (e.g. ₹50,000 for 1,000 stray dog meals). While donations are being gathered, <strong>100% of student funds are frozen in the Escrow Vault</strong>. The moment the target reaches 100%, the funds are unlocked, dispatched to the NGO, and a strict <strong>4-Day (96-Hour) execution clock</strong> begins.</p>

<h3>6.2 The 90% / 10% Fund Allocation Rule</h3>
<p>Legacy charities pretend that 100% of money goes to food, while NGOs secretly siphon money for transportation. ACTA introduces radical operational honesty:</p>

<table>
  <thead>
    <tr>
      <th>Fund Component</th>
      <th>Percentage</th>
      <th>Permitted Usage & Auditing Criteria</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Direct Cause Delivery</strong></td>
      <td><strong>90% Mandatory</strong></td>
      <td>Raw ration, food materials, saplings, notebooks, blankets, medicines. Verified via merchant bills & GST receipts.</td>
    </tr>
    <tr>
      <td><strong>NGO Operational Allowance</strong></td>
      <td><strong>10% Audited</strong></td>
      <td>Tempo/van fuel, packaging materials, volunteer water/tea. Audited via transport receipts. Eliminates hidden corruption.</td>
    </tr>
  </tbody>
</table>

<h3>6.3 Unit Economics Breakdown (Example: ₹50,000 Campaign)</h3>
<ul>
  <li><strong>Gross Student Donations Raised:</strong> ₹50,000.00</li>
  <li><strong>Payment Gateway Fee (0% MDR UPI):</strong> ₹0.00</li>
  <li><strong>Disbursed to NGO Execution Pool:</strong> ₹47,500.00 (₹42,750 for Direct Cause + ₹4,750 for Operations)</li>
  <li><strong>ACTA Platform Maintenance Fee (5%):</strong> ₹2,500.00 (Covers cloud storage, AI frame audits, and staff travel)</li>
</ul>

<!-- CHAPTER 7 -->
<div class="page-break"></div>
<h1>07. The 2-Phase Proof Pipeline, YouTube Archive & Instagram Flywheel</h1>

<h3>7.1 The 2-Phase Ground Proof Bundle</h3>
<p>To guarantee complete authenticity, the NGO field team must record two mandatory video stages:</p>
<ol>
  <li><strong>Phase 1: Raw Supply Purchase Proof:</strong> In-app video showing purchased raw supplies at the vendor shop + physical bill receipts.</li>
  <li><strong>Phase 2: Live Distribution Proof:</strong> In-app video showing ground delivery (food being served, trees being planted).</li>
</ol>

<h3>7.2 The Cost-Free YouTube Archive & Instagram ₹0 CAC Flywheel</h3>
<p>Hosting gigabytes of video streaming on private AWS S3 servers would destroy our startup with heavy cloud bills. We leverage a dual-channel architecture:</p>
<ul>
  <li><strong>Channel 1: Permanent YouTube Archive (Transparency):</strong> The raw, full proof video is uploaded to the official ACTA YouTube channel. YouTube handles video transcoding, global CDN, and bandwidth for <strong>₹0</strong>! The link is embedded directly in the donor's <em>"My Donations"</em> dashboard.</li>
  <li><strong>Channel 2: Instagram Reels (Viral Marketing):</strong> Our media team edits 30-second emotional highlight clips from the proof footage, posting them to Instagram Reels and YouTube Shorts. This delivers <strong>viral student acquisition at ₹0 ad spend</strong>!</li>
</ul>

<h3>7.3 Compliance with the Digital Personal Data Protection Act (DPDP Act 2023)</h3>
<p>India's DPDP Act 2023 strictly regulates public imagery of minors and vulnerable individuals. ACTA enforces built-in privacy protection:</p>
<ul>
  <li><strong>Minors (<18 Years) & Medical Patients:</strong> Faces are blurred by default before footage is published to YouTube or Instagram.</li>
  <li><strong>Field Workers & Adult Operatives:</strong> Displayed unblurred as authorized organizational representatives.</li>
</ul>

<!-- CHAPTER 8 -->
<h1>08. Campaign Architecture & The 7 Standard Causes</h1>

<p>ACTA maintains <strong>strictly 7 causes on the platform at any given time</strong> to prevent clutter:</p>

<table>
  <thead>
    <tr>
      <th>Cause Slot</th>
      <th>Category Name</th>
      <th>Lifecycle & Rotation Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Permanent 1</strong></td>
      <td>🍲 Zero Hunger (Homeless & Stray Feeding)</td>
      <td>Infinite cyclic pool. When target completes, next verified NGO takes over immediately.</td>
    </tr>
    <tr>
      <td><strong>Permanent 2</strong></td>
      <td>🌳 Green Earth (Tree Plantation & Cleanup)</td>
      <td>Infinite cyclic pool. Runs year-round across NCR educational campuses.</td>
    </tr>
    <tr>
      <td><strong>Permanent 3</strong></td>
      <td>📚 Child Education (School Kits & Books)</td>
      <td>Infinite cyclic pool. Partners with orphanages and slum learning centres.</td>
    </tr>
    <tr>
      <td><strong>Permanent 4</strong></td>
      <td>👴 Elder & Senior Care (Medicines & Essentials)</td>
      <td>Infinite cyclic pool. Supports old-age homes and destitute seniors.</td>
    </tr>
    <tr>
      <td><strong>Permanent 5</strong></td>
      <td>🧵 Women & Widow Support (Ration & Self-Help)</td>
      <td>Infinite cyclic pool. Delivers monthly dry ration kits to low-income women.</td>
    </tr>
    <tr>
      <td><strong>Temporary 1</strong></td>
      <td>🚨 Disaster & Crisis Relief</td>
      <td>Dynamic slot. Activates during floods, earthquakes, or severe winter cold-waves; retires upon completion.</td>
    </tr>
    <tr>
      <td><strong>Temporary 2</strong></td>
      <td>🐾 Emergency Stray & Medical Animal Rescue</td>
      <td>Dynamic slot. Dedicated to urgent animal surgeries or specialized rescue cases; rotates as needs arise.</td>
    </tr>
  </tbody>
</table>

<!-- CHAPTER 9 -->
<div class="page-break"></div>
<h1>09. User Dashboard Architecture & The Dignified Impact UX</h1>

<p>To avoid feeling like a cheap casino or gaming app, the User Dashboard is built around <strong>dignity, impact, and clean information architecture</strong>:</p>

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
│  [ 🏆 COMMUNITY & LEADERBOARD ] ──► Opens Free Fire style Guild view,   │
│                                    college clan score & Top 25 board.  │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│  CURRENT VERIFIED CAUSES (7 Cards)                                     │
│  [ 🍲 Zero Hunger ]  [ 🌳 Green Earth ]  [ 📚 Child Education ] ...    │
└────────────────────────────────────────────────────────────────────────┘
</div>

<ul>
  <li><strong>For Casual & Mature Donors:</strong> The hero screen displays pure, clean impact. No gaming noise.</li>
  <li><strong>For Gamified College Students:</strong> Tapping <em>[XP & Badges]</em> or <em>[Community & Leaderboard]</em> unlocks the competitive clan loop!</li>
</ul>

<!-- CHAPTER 10 -->
<h1>10. The Free Fire Guild Gamification & 10-Level Exponential Ladder</h1>

<h3>10.1 The Core XP Formula</h3>
<p><strong>₹1 Donated = 10 XP</strong> (Immediate dopamine feedback: ₹10 gives 100 XP!). Extra XP is awarded for Guild milestones (+200 XP), Top 25 city rank (+500 XP), and 3-week streaks (+150 XP).</p>

<h3>10.2 The 10-Level Exponential Giving Ladder</h3>
<p>Following real gaming principles, leveling up requires an <strong>exponential XP curve</strong>. Level 2 requires at least ₹500 (5,000 XP), ensuring prestige:</p>

<table>
  <thead>
    <tr>
      <th>Level</th>
      <th>Level Title</th>
      <th>XP Required</th>
      <th>Min. Direct Giving</th>
      <th>Visual Ring & Recognition Unlock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Level 01</strong></td>
      <td><strong>Seed Giver</strong> 🌱</td>
      <td>0 – 4,999 XP</td>
      <td>₹0 – ₹499</td>
      <td>Bronze Seed Tag. Unlocks upon very first ₹10 donation.</td>
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
      <td>Gold Shield Ring + Profile featured on Campus Board.</td>
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
      <td>Ruby Ring + Priority sponsor matching on your contributions.</td>
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

<h3>10.3 Free Fire Guild System & The Anti-Shaming Rule</h3>
<ul>
  <li><strong>The Guild Mechanics:</strong> Students join institutional communities (e.g. <em>GL Bajaj BCA 2nd Year Guild</em>). When a member donates ₹10, both their personal score and their Guild score increase!</li>
  <li><strong>The Anti-Shaming Privacy Rule:</strong> Individual donor points are kept private. The public board showcases <strong>only the Top 25 Communities and Top 25 Donors</strong> at City and National levels. Casual givers are never shamed.</li>
</ul>

<!-- CHAPTER 11 & 12 -->
<div class="page-break"></div>
<h1>11. The AI Layer — ACTA AI Advisor & Gemini Vision Engine</h1>

<div class="grid-2">
  <div class="card card-blue">
    <div class="card-title">Student Facing: ACTA AI Advisor (Gemini LLM)</div>
    <ul>
      <li><strong>Pocket Money Planner:</strong> Student asks: <em>"I have ₹30 left this week, where can I make the biggest impact?"</em> AI analyzes current causes and suggests matching donations.</li>
      <li><strong>Monthly Impact Demystifier:</strong> Generates beautiful shareable summaries: <em>"This month, you helped fund 14 stray animal meals and planted 1 neem tree in Greater Noida."</em></li>
    </ul>
  </div>
  <div class="card card-highlight">
    <div class="card-title">Admin Facing: Gemini Vision Multimodal Engine</div>
    <ul>
      <li><strong>Receipt & Bill OCR Analysis:</strong> Scans submitted vendor receipts, extracts line-item totals, and matches math against the campaign budget.</li>
      <li><strong>Video Frame Tamper Detection:</strong> Extracts frames from in-app camera video, checks for duplicate footage hashes, and flags recycled internet clips.</li>
      <li><strong>Automated Face Detection:</strong> Identifies minors and vulnerable beneficiaries to assist the automated face-blurring pipeline.</li>
    </ul>
  </div>
</div>

<h1>12. The Zero-Liability Volunteer Safety Shield</h1>

<div class="card card-highlight">
  <div class="card-title">Legal & Operational Risk Firewall</div>
  <p>Early prototypes failed because platforms tried to recruit student volunteers directly. ACTA eliminates physical, medical, and police liabilities through a strict firewall:</p>
  <ul>
    <li>ACTA is strictly a <strong>Technology, Escrow, and Verification Platform</strong>.</li>
    <li>ACTA never hires, directs, or dispatches individual volunteers.</li>
    <li>Ground execution is conducted 100% by the <strong>verified partner NGO using their own authorized staff and registered volunteers</strong>.</li>
    <li>If a student clicks <em>"Volunteer in Person"</em>, ACTA redirects them to the NGO's official intake portal. The NGO assumes 100% legal and insurance responsibility.</li>
  </ul>
</div>

<h1>13. Founder Ground Reality, Stage & GLBCRI Incubation Ask</h1>

<h3>13.1 Ground Reality (No Sugarcoating)</h3>
<ul>
  <li><strong>The Founder:</strong> Piyush Singh (18-year-old BCA 2nd Year student at GL Bajaj Institute of Management, Greater Noida).</li>
  <li><strong>Current Stage:</strong> Functional interactive web prototype live at `resence.in` / `acta.resence.in`. Complete system architecture, escrow logic, and PRD specifications locked.</li>
  <li><strong>NGO Partner Status:</strong> No active formal MoUs currently signed. Cold outreach as an independent student lacks institutional weight.</li>
</ul>

<h3>13.2 The Specific Ask from GLBCRI (Bharat Udyam Sangam 2026)</h3>
<p>At Bharat Udyam Sangam on 31 October 2026, ACTA will not ask for coding help. We ask GLBCRI for:</p>
<ol>
  <li><strong>Institutional Credibility & Letterhead:</strong> Introducing ACTA under GL Bajaj / GLBCRI official backing to 18–20 verified NGOs in Greater Noida and Noida.</li>
  <li><strong>Campus Pilot Authorization:</strong> Permission to run an official 30-day student micro-giving pilot across GL Bajaj Knowledge Park hostels and academic departments.</li>
  <li><strong>Pre-Incubation Mentorship:</strong> Legal structuring for NGO MoUs, Section 8/Pvt Ltd formalization, and seed grant guidance.</li>
</ol>

<div class="card card-highlight" style="margin-top: 30px; text-align: center;">
  <div class="card-title">ACTA by Resence — Small Acts, Big Impacts.</div>
  <p>Internal Product & Engineering Master Specification • Approved by Piyush Singh, Founder & CEO</p>
</div>

</body>
</html>
"""

html_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.html"
pdf_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.pdf"

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_file}")

# Compile to PDF using Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Compiling Apple-style PDF via Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_file):
    print(f"SUCCESS: Master PDF compiled successfully! Size: {os.path.getsize(pdf_file)} bytes")
else:
    print(f"PDF creation failed: {result.stderr}")
