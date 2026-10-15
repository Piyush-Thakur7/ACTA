import os
import subprocess
import pypdf

# Master 33-Page PRD Builder Script for ACTA by Resence
# SSOT V2.0 - High-Level Product Specifications & Implementation-Ready Engineering Architecture

html_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document_33P.html"
pdf_file = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs\ACTA_Master_Product_Document.pdf"

print("Compiling Master 33-Page Implementation-Ready PRD (Apple Style, Zero Free Fire)...")

pages_content = [
    # PAGE 1: COVER PAGE
    """
    <div class="cover-page">
      <div class="cover-top">
        <div class="brand-badge">RESENCE ECOSYSTEM</div>
        <div class="doc-tag">INTERNAL TEAM MASTER BIBLE • SSOT V2.0</div>
      </div>
      <div class="cover-body">
        <div class="hero-h1">ACTA <span>by Resence</span></div>
        <div class="hero-sub">Small Acts, Big Impacts.</div>
        <div class="hero-paragraph">
          The Definitive Master Product Requirements Document (PRD) & Implementation Architecture Specification. Designed as the internal core engineering bible for prototype development, escrow custody logic, pitch scripts, and the Bharat Udyam Sangam 2026 conclave at GLBCRI.
        </div>
        <div class="pill-group">
          <div class="pill-item green">0% MDR UPI Micro-Giving (₹10+)</div>
          <div class="pill-item blue">Milestone Escrow Vault Engine</div>
          <div class="pill-item">4-Day Geotagged Video Proof</div>
          <div class="pill-item green">Campus Impact Communities</div>
          <div class="pill-item blue">90/10 NGO Split Accounting</div>
          <div class="pill-item">DPDP Act 2023 Compliant</div>
          <div class="pill-item green">Multimodal Gemini AI Audits</div>
        </div>
        <div class="meta-table-box">
          <div class="meta-col"><h6>Founder & Architect</h6><p>Piyush Singh (CEO, Resence)</p></div>
          <div class="meta-col"><h6>Academic Standing</h6><p>BCA 2nd Year, GL Bajaj (GLBIM)</p></div>
          <div class="meta-col"><h6>Target Conclave</h6><p>Bharat Udyam Sangam 2026 (GLBCRI)</p></div>
          <div class="meta-col"><h6>Document Classification</h6><p>Internal Engineering & Pitch SSOT</p></div>
          <div class="meta-col"><h6>Pilot Hub</h6><p>Greater Noida & Delhi NCR Hub</p></div>
          <div class="meta-col"><h6>Implementation Standard</h6><p>Production-Ready Full-Stack Spec</p></div>
        </div>
      </div>
      <div class="footer-bar">
        <span>CONFIDENTIAL & PROPRIETARY — RESENCE TECH LABS</span>
        <span>PAGE 01 OF 33</span>
      </div>
    </div>
    """,

    # PAGE 2: TABLE OF CONTENTS & SYSTEM OVERVIEW
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">DIRECTORY</span></div>
        <h1>Table of Contents & System Architecture</h1>
        <div class="card card-highlight">
          <p>This document preserves every operational workflow, financial rule, database schema, API contract, and user journey of ACTA by Resence without simplification.</p>
        </div>
        <div class="grid-2" style="font-size: 8pt;">
          <div>
            <p><strong>Executive Summary</strong> ........................................................... Page 03</p>
            <p><strong>01. Project Overview & Core Mission</strong> ............................. Page 04</p>
            <p><strong>02. Meaning of ACTA & Historical Role</strong> ......................... Page 05</p>
            <p><strong>03. Market Ground Reality & The 67.5% Deficit</strong> ............... Page 06</p>
            <p><strong>04. Gen Z Giving & The Embarrassment Barrier</strong> ............ Page 07</p>
            <p><strong>05. Competitor Analysis: ACTA vs. Milaap & Ketto</strong> ....... Page 08</p>
            <p><strong>06. 3-Portal Architecture & Security Model</strong> .................. Page 09</p>
            <p><strong>07. User Dashboard Architecture & Impact UX</strong> ............ Page 10</p>
            <p><strong>08. Payment Logic: ₹10+ UPI & 0% MDR Math</strong> ............. Page 11</p>
            <p><strong>09. Milestone Escrow Vault & Pooling Windows</strong> ........... Page 12</p>
            <p><strong>10. Curated NGO Strategy (18–20 Partners)</strong> ................. Page 13</p>
            <p><strong>11. White-Glove Onboarding & 4-Step Vetting</strong> ............ Page 14</p>
            <p><strong>12. NGO Hierarchy: Director vs. Field Volunteers</strong> ........ Page 15</p>
            <p><strong>13. The 1 Lead + 2 Substitutes Redundancy Model</strong> ......... Page 16</p>
            <p><strong>14. The 90/10 Fund Allocation Split Rule</strong> .................... Page 17</p>
            <p><strong>15. 2-Phase Ground Proof Verification Pipeline</strong> ........... Page 18</p>
            <p><strong>16. In-App Camera Only & Anti-Tamper Telemetry</strong> ........ Page 19</p>
          </div>
          <div>
            <p><strong>17. Zero-Cost Video Cloud & Instagram Flywheel</strong> ......... Page 20</p>
            <p><strong>18. DPDP Act 2023 Beneficiary Privacy Protocol</strong> .......... Page 21</p>
            <p><strong>19. Campaign System: The 7 Standard Causes</strong> .............. Page 22</p>
            <p><strong>20. Gamification: The ₹1 = 10 XP Economy</strong> .................... Page 23</p>
            <p><strong>21. The 10-Level Exponential Giving Ladder</strong> ................. Page 24</p>
            <p><strong>22. Campus Communities & Institutional Guilds</strong> ........... Page 25</p>
            <p><strong>23. Top 25 Leaderboard & Anti-Shaming Privacy</strong> ........... Page 26</p>
            <p><strong>24. The AI Layer: AI Advisor & Gemini Vision</strong> ................ Page 27</p>
            <p><strong>25. Zero-Liability Volunteer Safety Shield</strong> ................... Page 28</p>
            <p><strong>26. NGO Performance Scoring & 2-Strike Contract</strong> ......... Page 29</p>
            <p><strong>27. Business Model & 5% Maintenance Fee Math</strong> ........... Page 30</p>
            <p><strong>28. Technology Stack & Database Schemas</strong> ................. Page 31</p>
            <p><strong>29. 90-Day Execution Roadmap & Campus Pilot</strong> .............. Page 32</p>
            <p><strong>Appendix: Founder Profile & GLBCRI Asks</strong> ................... Page 33</p>
          </div>
        </div>
        <h2>System Architecture Overview</h2>
        <p>ACTA is architected across three core pillars: (1) <strong>The Micro-Giving Client</strong> allowing ₹10 instant UPI donations with zero gateway loss, (2) <strong>The Milestone Escrow Engine</strong> freezing funds until 100% campaign completion, and (3) <strong>The Multi-Sensor Ground Telemetry Pipeline</strong> guaranteeing verifiable video proof within 96 hours before disbursement.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Directory</span><span>PAGE 02 OF 33</span></div>
    </div>
    """,

    # PAGE 3: EXECUTIVE SUMMARY & STRATEGIC PROBLEM STATEMENT
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">EXECUTIVE SUMMARY</span></div>
        <h1>Executive Summary & Problem Statement</h1>
        <p><strong>ACTA by Resence</strong> is an institutional-grade, transparency-first micro-donation and civic engagement network connecting university students with manually vetted local non-profits across India. It directly resolves three structural dysfunctions in the Indian social giving ecosystem:</p>
        <div class="card card-emerald">
          <div class="card-title">1. The Ground Proof Deficit (67.5% Trust Collapse)</div>
          <p>Donors receive generic email thank-yous or 80G tax slips, but zero visual evidence that food reached a hungry child or a tree was planted. ACTA introduces mandatory in-app geotagged video proof delivered within 96 hours.</p>
        </div>
        <div class="card card-blue">
          <div class="card-title">2. The "Chillar" Stigma & Minimum Ticket Barrier</div>
          <p>Traditional non-profits ignore donations below ₹500, alienating 40 Million college students. ACTA builds a democratic micro-giving engine starting at ₹10 via UPI, leveraging India's 0% MDR mandate to make small contributions economically viable.</p>
        </div>
        <div class="card card-amber">
          <div class="card-title">3. The Retention & Community Void</div>
          <p>Charity in India is treated as a one-time transaction driven by guilt. ACTA introduces an engaging community architecture—institutional campus guilds, streaks, experience points (XP), and dignified impact tiers—transforming giving into an uplifting collegiate habit.</p>
        </div>
        <h2>High-Level Operational Flywheel</h2>
        <div class="wireframe">
[STUDENT: ₹10 UPI Micro-Donation] ──► [ESCROW VAULT: 100% Frozen Batch Pool]
                                                         │
                                                         ▼ (Target Reached)
[PERMANENT YOUTUBE PROOF ARCHIVE] ◄── [VETTED LOCAL NGO: 96h Ground Delivery]
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Executive Summary</span><span>PAGE 03 OF 33</span></div>
    </div>
    """,

    # PAGE 4: PROJECT OVERVIEW & USER PERSONAS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 01</span></div>
        <h1>01. Project Overview & Stakeholder Personas</h1>
        <h2>1.1 Project Specification</h2>
        <p>ACTA is an autonomous civic-tech network developed under parent entity <strong>Resence</strong> (`https://resence.in`). It bridges the trust chasm between India's 400M+ youth and genuine grassroots non-profits through cryptographic verification, video telemetry, and escrow custody.</p>
        <h2>1.2 Primary Stakeholder Personas</h2>
        <table>
          <thead>
            <tr><th>Stakeholder</th><th>Profile & Constraints</th><th>Key Motivations & Pain Points</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Rahul (Student Donor)</strong></td>
              <td>19, BCA 2nd Year, monthly hostel pocket money ₹3,500. Uses UPI daily.</td>
              <td>Wants to do good but cannot donate ₹500. Fears scams. Motivated by college pride and verifiable video proof.</td>
            </tr>
            <tr>
              <td><strong>Sunita (NGO Director)</strong></td>
              <td>52, Runs registered animal shelter in Greater Noida. 12A/80G certified.</td>
              <td>Struggles with digital marketing and unstable individual donations. Desires reliable bulk milestone disbursements.</td>
            </tr>
            <tr>
              <td><strong>Priya (Campus Guild Lead)</strong></td>
              <td>20, Student Council Lead at GL Bajaj. Manages hostel club WhatsApp group.</td>
              <td>Wants to rally her batch for social causes; motivated by inter-college leaderboard rankings and campus prestige.</td>
            </tr>
            <tr>
              <td><strong>Platform Admin</strong></td>
              <td>Resence Core Operations & Compliance team. Manages audits & escrow.</td>
              <td>Needs automated fraud detection, receipt OCR, and immutable state machines to prevent operational leakage.</td>
            </tr>
          </tbody>
        </table>
        <h2>1.3 Corporate Ecosystem Architecture</h2>
        <p>ACTA mirrors an Alphabet-Google structure: <strong>Resence</strong> is the parent technology lab providing AI, design, and escrow governance; <strong>ACTA</strong> (`https://acta.resence.in`) is the consumer-facing civic platform.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 01: Project Overview</span><span>PAGE 04 OF 33</span></div>
    </div>
    """,

    # PAGE 5: MEANING OF ACTA & HISTORICAL ROLE
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 02</span></div>
        <h1>02. The Meaning of ACTA & Historical Role</h1>
        <div class="card card-highlight">
          <div class="card-title">Etymology & Historical Heritage</div>
          <p>The name <strong>ACTA</strong> is not an arbitrary startup buzzword or an AI-generated acronym. It is a historic, linguistic anchor for our entire product philosophy.</p>
        </div>
        <h2>2.1 Classical Latin Root & Roman Origin</h2>
        <p>In Classical Latin, <strong>Acta</strong> is the plural form of <em>Actum</em>, translating to <strong>"Things Done"</strong>, <strong>"Deeds Accomplished"</strong>, or <strong>"Official Public Records."</strong></p>
        <p>Around 131 BC, the Roman Republic established the <strong>Acta Diurna</strong> (<em>"Daily Deeds"</em>). Carved in stone or metal and hung in the public Forum, it was civilization's very first daily public bulletin, ensuring citizens could verify daily state announcements, grain allotments, and civic decrees with their own eyes.</p>
        <h2>2.2 Strategic Role in Our Product Architecture</h2>
        <ul>
          <li><strong>Every Contribution is an "Acta":</strong> On our platform, a ₹10 donation is not an anonymous financial entry; it is an individual <em>Acta</em>—a recorded, verified deed of human compassion.</li>
          <li><strong>The Modern Public Ledger:</strong> Just as ancient Rome had the <em>Acta Diurna</em>, our platform acts as India's digital public transparency ledger. Every rupee donated is proven with video before the record is permanently published.</li>
          <li><strong>Linguistic Fusion with Our Locked Tagline:</strong> The locked tagline is <strong>"Small Acts, Big Impacts."</strong> The word <em>"Acts"</em> in the tagline is the exact English translation of the Latin root <em>Acta</em>. The brand name and the tagline are linguistically fused.</li>
        </ul>
        <div class="card card-emerald">
          <div class="card-title">Brand Architecture Equation</div>
          <p><strong>ACTA (Deeds Done) + ACTA DIURNA (Public Ledger) = Small Acts, Big Impacts.</strong></p>
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 02: Meaning of ACTA</span><span>PAGE 05 OF 33</span></div>
    </div>
    """,

    # PAGE 6: MARKET REALITY & TRUST DEFICIT
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 03</span></div>
        <h1>03. Market Reality & The 67.5% Trust Deficit</h1>
        <div class="grid-3">
          <div class="stat-card"><div class="stat-val">67.5%</div><div class="stat-lbl">Donor Trust Deficit</div></div>
          <div class="stat-card"><div class="stat-val">5,25,179</div><div class="stat-lbl">Registered Darpan NGOs</div></div>
          <div class="stat-card"><div class="stat-val">₹540 B</div><div class="stat-lbl">India Philanthropy Pool</div></div>
        </div>
        <h2>3.1 The Epidemic of Cynicism</h2>
        <p>India represents one of the largest charitable cultures globally, with religious and retail giving exceeding ₹540 Billion annually. Yet, independent research reveals that <strong>67.5% of educated urban citizens actively refuse to donate to online charities</strong>. Donors routinely witness news exposés detailing corrupt non-profit executives, phantom beneficiaries, and astronomical administrative overheads. Donors are left with profound cynicism, asking: <em>"Did my money actually buy food, or did it sponsor an NGO director's car fuel?"</em></p>
        <h2>3.2 Market Sizing (TAM / SAM / SOM)</h2>
        <table>
          <thead>
            <tr><th>Metric</th><th>Scope</th><th>Financial Value</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>TAM</strong></td><td>Total Indian Retail & Micro-Philanthropy Pool</td><td>₹54,000 Cr ($6.5 Billion)</td></tr>
            <tr><td><strong>SAM</strong></td><td>Gen Z & Higher Education Student Micro-Giving (40M Youth)</td><td>₹4,200 Cr ($500 Million)</td></tr>
            <tr><td><strong>SOM (Phase 1)</strong></td><td>Delhi NCR Collegiate Hub (120+ Universities & Colleges)</td><td>₹36 Cr ($4.3 Million)</td></tr>
          </tbody>
        </table>
        <h2>3.3 The Verification Moat</h2>
        <p>ACTA replaces blind faith with cryptographically verified ground proof. Funds remain in escrow until in-app video telemetry proves delivery within 96 hours.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 03: Market Reality</span><span>PAGE 06 OF 33</span></div>
    </div>
    """,

    # PAGE 7: GEN Z GIVING & THE EMBARRASSMENT BARRIER
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 04</span></div>
        <h1>04. Gen Z Giving & The Embarrassment Barrier</h1>
        <h2>4.1 The Psychology of the College Donor</h2>
        <p>Gen Z represents India's most socially conscious demographic. They care intensely about animal welfare, hunger eradication, and environmental greening. Yet, traditional charity fails to engage them due to a critical barrier: <strong>The Social Embarrassment of Small Money</strong>.</p>
        <div class="card card-amber">
          <div class="card-title">The "Chillar" Stigma</div>
          <p>A college student surviving on a monthly hostel allowance of ₹3,000 cannot donate ₹500 to a hospital campaign. Walking up to an offline donation desk to give ₹20 feels embarrassing because traditional non-profits dismiss small sums as petty change.</p>
        </div>
        <h2>4.2 The Dignity of Micro-Giving</h2>
        <p>ACTA completely reframes small contributions. On ACTA, <strong>a ₹10 donation is celebrated with full dignity and 100 XP</strong>! We educate youth on democratic micro-giving: <em>"Your ₹10 alone may be small, but when 1,000 GL Bajaj students pool ₹10, it creates ₹10,000—delivering 285 hot meals or planting 50 trees."</em></p>
        <h2>4.3 UPI 0% MDR: The Technical Enabler</h2>
        <p>This micro-giving economy is powered by a massive regulatory breakthrough: <strong>The Government of India mandates 0% Merchant Discount Rate (MDR) on UPI P2M transactions</strong> under Section 10A of the Payment and Settlement Systems Act, 2007. A ₹10 donation incurs <strong>₹0.00 gateway cost</strong>, allowing 100% of the student's money to reach the escrow vault intact.</p>
        <div class="wireframe">
CREDIT CARD DONATION:  ₹10.00  ──►  [ Gateway Fee: ₹2.20 ]  ──►  NET: ₹7.80 (22% Loss!)
ACTA UPI DONATION:     ₹10.00  ──►  [ NPCI 0% MDR: ₹0.00 ]   ──►  NET: ₹10.00 (100% Intact!)
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 04: Gen Z Giving</span><span>PAGE 07 OF 33</span></div>
    </div>
    """,

    # PAGE 8: COMPETITOR ANALYSIS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 05</span></div>
        <h1>05. Competitor Analysis: ACTA vs. Milaap & Ketto</h1>
        <div class="card card-highlight">
          <div class="card-title">The Fundamental Paradigm Shift</div>
          <p>Legacy platforms like <strong>Milaap and Ketto</strong> were built 15 years ago for working professionals making high-ticket donations via credit cards. They operate as <em>unmonitored payment pipelines</em>. ACTA is designed for <strong>Gen Z on UPI</strong>, operating as a <em>zero-trust verification engine</em>.</p>
        </div>
        <table>
          <thead>
            <tr><th>Feature Parameter</th><th>Legacy Platforms (Milaap / Ketto)</th><th>ACTA by Resence</th><th>Why Donors Choose ACTA</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Minimum Ticket</strong></td>
              <td>₹500 to ₹1,000+ (High friction)</td>
              <td><strong>₹10 to ₹50 via UPI</strong></td>
              <td>Zero pocket money guilt; everyday student giving habit.</td>
            </tr>
            <tr>
              <td><strong>Proof of Work</strong></td>
              <td>Opaque email thank-you text.</td>
              <td><strong>Mandatory 4-day geotagged video + store bills.</strong></td>
              <td>Donors see the actual meal delivered within 96 hours.</td>
            </tr>
            <tr>
              <td><strong>Fund Custody</strong></td>
              <td>100% released upfront without proof.</td>
              <td><strong>100% frozen in Escrow Vault.</strong> Disbursed post-proof.</td>
              <td>Zero risk of campaigner absconding with donor funds.</td>
            </tr>
            <tr>
              <td><strong>Audience Vibe</strong></td>
              <td>Older adults; driven by medical sadness.</td>
              <td><strong>Gen Z, college youth; driven by community pride.</strong></td>
              <td>Charity becomes an engaging, uplifting collegiate culture.</td>
            </tr>
            <tr>
              <td><strong>Fee Structure</strong></td>
              <td>5–10% fee + 2% gateway + tipping prompts.</td>
              <td><strong>5% flat platform fee; 0% UPI gateway cut.</strong></td>
              <td>Complete financial transparency; no hidden tipping tricks.</td>
            </tr>
            <tr>
              <td><strong>NGO Vetting</strong></td>
              <td>Open marketplace; unvetted campaigns.</td>
              <td><strong>Curated 18–20 local NGOs, verified offline.</strong></td>
              <td>Eliminates fake NGOs and phantom beneficiary scams.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 05: Competitor Analysis</span><span>PAGE 08 OF 33</span></div>
    </div>
    """,

    # PAGE 9: 3-PORTAL ARCHITECTURE & SECURITY MODEL
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 06</span></div>
        <h1>06. 3-Portal Architecture & Security Model</h1>
        <p>To ensure bulletproof operational security and prevent data contamination, ACTA strictly isolates user roles into <strong>three independent operational portals</strong>:</p>
        <div class="card card-emerald">
          <div class="card-title">1. Public User Portal (`acta.resence.in`)</div>
          <p>Publicly accessible to any user worldwide via modern web browsers and mobile devices. Zero barriers to entry. Users browse the 7 active causes, execute 1-click UPI donations, review personal impact counters, and view the public YouTube proof archive.</p>
        </div>
        <div class="card card-blue">
          <div class="card-title">2. NGO Partner Portal (Invite-Only via Magic Link)</div>
          <p>Completely invisible to the general public. No open registration button. Once an NGO is vetted physically offline, a cryptographically signed magic link is dispatched to their official email. Houses the Director Financial Dashboard and the Volunteer Field Team Dashboard.</p>
        </div>
        <div class="card card-amber">
          <div class="card-title">3. Secret Admin Control Panel (Internal Security Engine)</div>
          <p>Operates on an unindexed, obscure route protected by strong credentials, IP whitelisting, and two-factor authentication. Core team manages causes, inspects AI frame audits, verifies merchant receipts, and triggers escrow disbursements or automated refunds.</p>
        </div>
        <h2>Access Control & Session Security Matrix</h2>
        <table>
          <thead>
            <tr><th>Portal Component</th><th>Authentication Method</th><th>Session Lifetime</th><th>Network Isolation</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Public User</strong></td><td>Phone OTP / Google OAuth / Guest View</td><td>30 Days Persistent JWT</td><td>Public CDN Edge</td></tr>
            <tr><td><strong>NGO Partner</strong></td><td>Magic Email Link + Device Fingerprint</td><td>7 Days Secure Token</td><td>Restricted Origin</td></tr>
            <tr><td><strong>Admin Panel</strong></td><td>Hardware 2FA + IP Whitelisting</td><td>4 Hours Strict Inactivity</td><td>Zero-Trust Internal Network</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 06: 3-Portal Architecture</span><span>PAGE 09 OF 33</span></div>
    </div>
    """,

    # PAGE 10: USER DASHBOARD ARCHITECTURE & UX
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 07</span></div>
        <h1>07. User Dashboard Architecture & Impact UX</h1>
        <p>Charity must never look like an intrusive arcade game. The User Dashboard is architected around dignity, clean metrics, and purposeful actions:</p>
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
│  [ 🏆 COMMUNITY & LEADERBOARD ] ──► Opens Campus Guild view, college clan │
│                                    score & Top 25 competitive board.   │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│  CURRENT VERIFIED CAUSES (7 Cards)                                     │
│  [ 🍲 Zero Hunger ]  [ 🌳 Green Earth ]  [ 📚 Child Education ] ...    │
└────────────────────────────────────────────────────────────────────────┘
        </div>
        <h2>Component Architecture & State Machine</h2>
        <ul>
          <li><code>TotalImpactCard</code>: Displays lifetime metrics, streak count, and verified contribution total.</li>
          <li><code>ActionPillars</code>: 3 clean navigation triggers keeping secondary screens modular and clutter-free.</li>
          <li><code>CausesCarousel</code>: Renders the 7 verified active causes with real-time pooling progress bars.</li>
        </ul>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 07: User Dashboard Architecture</span><span>PAGE 10 OF 33</span></div>
    </div>
    """,

    # PAGE 11: PAYMENT ARCHITECTURE & RECONCILIATION
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 08</span></div>
        <h1>08. Payment Logic: ₹10+ UPI & 0% MDR Math</h1>
        <h2>8.1 Razorpay Smart UPI Integration Protocol</h2>
        <p>ACTA integrates directly with Razorpay Smart UPI Gateway. When a student taps <em>"Donate ₹10"</em>, the app triggers a native UPI Intent flow, launching Google Pay, PhonePe, Paytm, or BHIM directly without demanding card numbers or bank passwords.</p>
        <h2>8.2 Webhook Reconciliation Handler (Implementation Spec)</h2>
        <p>Network drops during UPI payments are handled through an asynchronous edge webhook listener. If a student's app closes before confirmation, Razorpay's <code>payment.captured</code> webhook reconciles the transaction within 60 seconds.</p>
        <div class="wireframe">
// POST /api/v1/donations/webhook-razorpay
{
  "entity": "event",
  "event": "payment.captured",
  "payload": {
    "payment": {
      "entity": {
        "id": "pay_O9x8Yz123456",
        "amount": 1000,              // 1000 paise = ₹10.00 INR
        "currency": "INR",
        "status": "captured",
        "method": "upi",
        "vpa": "piyush@okaxis",
        "notes": {
          "user_id": "usr_99182",
          "cause_id": "cause_hunger_01",
          "guild_id": "guild_glbajaj_bca"
        }
      }
    }
  }
}
        </div>
        <h2>8.3 Escrow Crediting & Retroactive XP Algorithm</h2>
        <p>Upon signature verification (HMAC SHA-256), the server increments <code>causes.pooled_amount</code>, logs the donation into the immutable escrow ledger, and increments <code>users.xp</code> by <code>amount * 10</code>.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 08: Payment Logic</span><span>PAGE 11 OF 33</span></div>
    </div>
    """,

    # PAGE 12: MILESTONE ESCROW VAULT & STATE MACHINE
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 09</span></div>
        <h1>09. Milestone Escrow Vault & State Machine</h1>
        <h2>9.1 The Milestone Batch Pooling Concept</h2>
        <p>Unlike traditional charities that disburse money immediately upon receipt, ACTA operates on <strong>Batch Pooling</strong>: donations collect inside an isolated Escrow Vault until a campaign hits 100% of its target (e.g. ₹50,000 to feed 1,000 stray animals).</p>
        <h2>9.2 Escrow Batch Finite State Machine (8 States)</h2>
        <table>
          <thead>
            <tr><th>State Code</th><th>State Description</th><th>Trigger Condition</th></tr>
          </thead>
          <tbody>
            <tr><td><code>POOLING</code></td><td>Open for student micro-donations.</td><td>Initial campaign launch.</td></tr>
            <tr><td><code>MILESTONE_LOCKED</code></td><td>100% target met. Escrow vault frozen.</td><td><code>pooled_amount >= target_amount</code></td></tr>
            <tr><td><code>DISBURSED_PHASE_1</code></td><td>Funds transferred to NGO bank account.</td><td>Admin approval; 96h countdown begins.</td></tr>
            <tr><td><code>PROOF_SUBMITTED</code></td><td>NGO uploads Phase 1 bills & Phase 2 video.</td><td>Volunteer Head hits submit in app.</td></tr>
            <tr><td><code>AI_VERIFIED</code></td><td>Gemini Vision audits bills & video frames.</td><td>Automated background worker job.</td></tr>
            <tr><td><code>ADMIN_APPROVED</code></td><td>Core team gives final sign-off.</td><td>Manual audit passes with zero defects.</td></tr>
            <tr><td><code>COMPLETED</code></td><td>Proof published to YouTube & donors notified.</td><td>Batch closed permanently.</td></tr>
            <tr><td><code>REFUNDED</code></td><td>100% funds returned to donors' ACTA Wallets.</td><td>96h + 24h grace period expires without proof.</td></tr>
          </tbody>
        </table>
        <h2>9.3 Automated Refund SLAs</h2>
        <p>If the 96-hour deadline expires without valid proof submission, the escrow engine triggers an automated <strong>100% refund credited to every donor's in-app ACTA Wallet</strong>, while blacklisting the defaulting NGO.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 09: Milestone Escrow Vault</span><span>PAGE 12 OF 33</span></div>
    </div>
    """,

    # PAGE 13: CURATED NGO STRATEGY
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 10</span></div>
        <h1>10. The Curated NGO Strategy (18–20 Partners)</h1>
        <div class="card card-blue">
          <div class="card-title">Quality Over Unmonitored Scale</div>
          <p>Amateur platforms claim they will onboard 10,000 NGOs on Day 1. ACTA enforces a tight, curated pilot of <strong>only 18 to 20 verified local NGOs</strong> across Greater Noida and Delhi NCR.</p>
        </div>
        <h2>10.1 Capacity Modeling for 20 Curated Non-Profits</h2>
        <p>A network of 20 active grassroots non-profits possesses the physical capacity to execute over <strong>₹20 Lakhs to ₹50 Lakhs</strong> in ground humanitarian delivery annually. By curating 20 partners, ACTA can maintain 100% human-verified quality, visit offices personally, and build deep institutional relationships.</p>
        <h2>10.2 Cohort Allocation Breakdown (Pilot Phase)</h2>
        <table>
          <thead>
            <tr><th>Cause Sector</th><th>Partner Quota</th><th>Target Operations (Greater Noida / NCR)</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Zero Hunger & Food Rations</strong></td><td>6 Partner NGOs</td><td>Homeless night shelters, slum food kitchens, stray feeding networks.</td></tr>
            <tr><td><strong>Green Earth & Campus Cleanliness</strong></td><td>4 Partner NGOs</td><td>Tree plantation along Yamuna Expressway, college park greening drives.</td></tr>
            <tr><td><strong>Child Education & School Kits</strong></td><td>4 Partner NGOs</td><td>Underprivileged school kit distribution, orphan support centers.</td></tr>
            <tr><td><strong>Elder Care & Health Aid</strong></td><td>3 Partner NGOs</td><td>Senior citizen medical checkups, old-age home ration support.</td></tr>
            <tr><td><strong>Crisis & Animal Rescue</strong></td><td>3 Partner NGOs</td><td>Emergency veterinary trauma care, winter cold wave blanket distribution.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 10: Curated NGO Strategy</span><span>PAGE 13 OF 33</span></div>
    </div>
    """,

    # PAGE 14: WHITE-GLOVE ONBOARDING & 4-STEP VETTING
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 11</span></div>
        <h1>11. White-Glove Onboarding & 4-Step Vetting</h1>
        <h2>11.1 The White-Glove Physical Setup Protocol</h2>
        <p>Grassroots NGO directors are typically older individuals who struggle with modern digital tools. ACTA eliminates onboarding friction through <strong>In-Person Physical Setup</strong>:</p>
        <ul>
          <li>An ACTA representative personally visits the NGO's registered office.</li>
          <li>The representative inspects physical facilities (kitchens, animal shelters, school centers).</li>
          <li>The representative verifies physical documents and assists the director in bookmarking their private portal access link.</li>
        </ul>
        <h2>11.2 The 4-Step Statutory Vetting Gate</h2>
        <table>
          <thead>
            <tr><th>Verification Step</th><th>Audit Standard</th><th>Verification Mechanism</th><th>Failure Action</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Darpan & 12A/80G</strong></td>
              <td>Active NITI Aayog Darpan ID + valid Section 12A & 80G certificates.</td>
              <td>Automated portal check + manual cross-verification.</td>
              <td>Instant rejection.</td>
            </tr>
            <tr>
              <td><strong>2. Physical Premises</strong></td>
              <td>In-person physical inspection of active shelters, kitchens, or centers.</td>
              <td>On-site visit by Resence field representative.</td>
              <td>Mandatory re-audit in 7d.</td>
            </tr>
            <tr>
              <td><strong>3. Bank Penny Drop</strong></td>
              <td>₹1 automated IMPS validation of registered NGO bank account.</td>
              <td>Razorpay Fund Account Validation API.</td>
              <td>Disbursement blocked.</td>
            </tr>
            <tr>
              <td><strong>4. Legal MoU Sign</strong></td>
              <td>Signed 2-strike contract binding director to 96h proof delivery rules.</td>
              <td>Physical wet-ink / e-Sign agreement.</td>
              <td>Access link withheld.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 11: White-Glove Onboarding</span><span>PAGE 14 OF 33</span></div>
    </div>
    """,

    # PAGE 15: NGO HIERARCHY: DIRECTOR VS VOLUNTEERS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 12</span></div>
        <h1>12. NGO Hierarchy: Director vs. Field Volunteers</h1>
        <h2>12.1 Segmented Dashboard Architecture (RBAC)</h2>
        <p>Exposing financial accounts and payout ledgers to temporary field volunteers causes non-profit disputes. The NGO Partner Portal strictly segments access into two sub-dashboards:</p>
        <div class="grid-2">
          <div class="card card-emerald">
            <div class="card-title">Sub-Dashboard A: NGO Director / Owner</div>
            <ul>
              <li>Views gross donations received & 90/10 split tracking.</li>
              <li>Oversees NGO Trust Score and historical execution ratings.</li>
              <li>Assigns Volunteer Leads and Substitutes for upcoming campaigns.</li>
              <li>Direct in-dashboard priority support chat channel to ACTA core team.</li>
            </ul>
          </div>
          <div class="card card-blue">
            <div class="card-title">Sub-Dashboard B: Volunteer Field Team</div>
            <ul>
              <li>Clean task view: Cause name, execution venue, delivery quota.</li>
              <li>In-App Camera access (gallery upload permanently locked).</li>
              <li>Expense receipt scanner for wholesale ration/food bills.</li>
              <li>Team roster showing names of assigned members.</li>
            </ul>
          </div>
        </div>
        <h2>12.2 Role-Based Access Control (RBAC) Schema</h2>
        <table>
          <thead>
            <tr><th>Permission Attribute</th><th>NGO Director</th><th>Volunteer Head</th><th>Field Substitutes</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Bank Account & Payout View</strong></td><td>Full Read/Write</td><td>No Access (Hidden)</td><td>No Access (Hidden)</td></tr>
            <tr><td><strong>Assign Campaign Leads</strong></td><td>Full Authority</td><td>No Authority</td><td>No Authority</td></tr>
            <tr><td><strong>Capture & Upload Proof</strong></td><td>View Only</td><td>Primary Rights</td><td>Backup Rights</td></tr>
            <tr><td><strong>Direct Admin Support Chat</strong></td><td>Full Access</td><td>No Access</td><td>No Access</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 12: NGO Hierarchy</span><span>PAGE 15 OF 33</span></div>
    </div>
    """,

    # PAGE 16: 1+2 REDUNDANCY MODEL
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 13</span></div>
        <h1>13. The 1 Lead + 2 Substitutes Redundancy Model</h1>
        <div class="card card-amber">
          <div class="card-title">Eliminating Single Points of Failure</div>
          <p>In grassroots social work, volunteer unreliability causes 80% of missed deadlines. If an assigned volunteer falls ill, attends a family wedding, or misplaces their phone, execution halts.</p>
        </div>
        <h2>13.1 Mandatory 1+2 Redundancy Protocol</h2>
        <p>For every active campaign, the NGO Director <strong>must designate 1 Primary Volunteer Head + 2 Substitute Leads</strong>. All three are provisioned with camera and receipt submission rights:</p>
        <ul>
          <li><strong>Volunteer Head (Primary):</strong> Primary operative responsible for purchasing supplies, recording ground distribution, and uploading proof.</li>
          <li><strong>Substitute Lead 1 (Backup A):</strong> System sends auto-alert at Hour 48 if Phase 1 proof is pending; steps in if Primary Head is unresponsive.</li>
          <li><strong>Substitute Lead 2 (Backup B):</strong> System escalates at Hour 72; authorized to complete delivery to prevent the 96-hour deadline breach.</li>
        </ul>
        <h2>13.2 Automated Escalation Workflow</h2>
        <div class="wireframe">
HOUR 00: Funds Disbursed ──► Primary Lead Notified (96h Clock Starts)
HOUR 48: No Bills Submitted? ──► WhatsApp Alert sent to Lead + Substitute 1
HOUR 72: Still Pending? ──► SMS/Call Escalation to NGO Director + Substitute 2
HOUR 96: Final Deadline ──► SLA Check: If proof submitted, approve; else Grace Period.
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 13: 1+2 Redundancy Model</span><span>PAGE 16 OF 33</span></div>
    </div>
    """,

    # PAGE 17: THE 90/10 FUND ALLOCATION SPLIT RULE
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 14</span></div>
        <h1>14. The 90/10 Fund Allocation Split Rule</h1>
        <div class="card card-emerald">
          <div class="card-title">The Foundation of Radical Financial Honesty</div>
          <p>Legacy non-profit platforms tell donors that "100% goes to the poor," while knowing that NGOs secretly siphon money to pay for transport tempos and packaging. ACTA replaces hypocrisy with formal, audited operational budgeting.</p>
        </div>
        <h2>14.1 The 90/10 Allocation Framework</h2>
        <table>
          <thead>
            <tr><th>Fund Bucket</th><th>Share</th><th>Eligible Expenses & Auditing Standard</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Direct Cause Execution</strong></td><td><strong>90% Mandatory</strong></td><td>Raw food items, ration bags, school kits, blankets, veterinary medicines. Must match vendor invoices & GST bills.</td></tr>
            <tr><td><strong>NGO Operational Allowance</strong></td><td><strong>10% Audited</strong></td><td>Tempo/van fuel, packaging sacks, volunteer hydration & basic transport. Audited via fuel bills & transport slips.</td></tr>
          </tbody>
        </table>
        <h2>14.2 Real Unit Economics Across 3 Campaign Tiers</h2>
        <table>
          <thead>
            <tr><th>Campaign Tier</th><th>Target (INR)</th><th>Direct Cause (90%)</th><th>NGO Ops (10%)</th><th>ACTA Fee (5%)</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Micro Campaign</strong></td><td>₹5,000.00</td><td>₹4,275.00</td><td>₹475.00</td><td>₹250.00</td></tr>
            <tr><td><strong>Community Drive</strong></td><td>₹20,000.00</td><td>₹17,100.00</td><td>₹1,900.00</td><td>₹1,000.00</td></tr>
            <tr><td><strong>Mega Campus Drive</strong></td><td>₹50,000.00</td><td>₹42,750.00</td><td>₹4,750.00</td><td>₹2,500.00</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 14: 90/10 Split Rule</span><span>PAGE 17 OF 33</span></div>
    </div>
    """,

    # PAGE 18: 2-PHASE GROUND PROOF PIPELINE
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 15</span></div>
        <h1>15. 2-Phase Ground Proof Verification Pipeline</h1>
        <p>To eliminate fraud, ACTA mandates a comprehensive <strong>2-Phase Proof Bundle</strong> before any escrow payout is authorized:</p>
        <div class="grid-2">
          <div class="card card-blue">
            <div class="card-title">Phase 1: Supply Purchase Proof</div>
            <p><strong>Captured:</strong> At wholesale merchant / retail store.</p>
            <ul>
              <li>In-app video showing purchased raw supplies (50 kg rice, stationery boxes, blankets).</li>
              <li>High-res photo of merchant GST bill showing itemized quantities and shop stamp.</li>
            </ul>
          </div>
          <div class="card card-emerald">
            <div class="card-title">Phase 2: Ground Distribution Proof</div>
            <p><strong>Captured:</strong> At actual field execution site.</p>
            <ul>
              <li>In-app video showing service delivery (hot food served, trees planted, notebooks handed over).</li>
              <li>Hardware GPS coordinates and network timestamps burned into video metadata.</li>
            </ul>
          </div>
        </div>
        <h2>15.2 Proof Bundle JSON Schema (Backend Contract)</h2>
        <div class="wireframe">
{
  "bundle_id": "pb_88129",
  "campaign_id": "cmp_hunger_gl_04",
  "ngo_id": "ngo_saksham_gn",
  "submitted_by": "usr_lead_ashish",
  "phase_1": {
    "merchant_bill_url": "https://s3.../bills/gst_invoice_881.jpg",
    "supplies_video_url": "https://s3.../raw/supplies_881.mp4",
    "merchant_gstin": "07AAACS1429B1ZB",
    "invoice_total": 4275.00
  },
  "phase_2": {
    "distribution_video_url": "https://s3.../raw/distribution_881.mp4",
    "gps_latitude": 28.4744,
    "gps_longitude": 77.5040,
    "beneficiary_count": 120
  }
}
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 15: 2-Phase Proof Pipeline</span><span>PAGE 18 OF 33</span></div>
    </div>
    """,

    # PAGE 19: IN-APP CAMERA LOCK & HARDWARE TELEMETRY
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 16</span></div>
        <h1>16. In-App Camera Lock & Hardware Telemetry</h1>
        <div class="card card-amber">
          <div class="card-title">Gallery Uploads are Permanently Disabled</div>
          <p>Scammers typically upload pre-downloaded stock videos or recycled footage from past years. ACTA's volunteer dashboard <strong>completely disables file gallery access</strong>.</p>
        </div>
        <h2>16.1 Hardware Sensor Telemetry Verification</h2>
        <p>Videos and receipts must be captured live through the browser/app camera stream (WebRTC <code>getUserMedia</code>). During capture, the telemetry engine verifies:</p>
        <ul>
          <li><strong>Network Time Protocol (NTP) Sync:</strong> Synchronizes with atomic clock servers to prevent local phone clock rollbacks.</li>
          <li><strong>GPS Geofencing Check:</strong> Confirms latitude/longitude falls within registered NGO operational radius (e.g. Greater Noida $\pm 15$ km).</li>
          <li><strong>Gyroscope & Accelerometer Telemetry:</strong> Evaluates hand tremors and angle shifts to verify the camera is filming physical reality rather than a computer monitor.</li>
        </ul>
        <h2>16.2 Client-Side Cryptographic Stamping</h2>
        <div class="wireframe">
// In-App Video Capture Stream Hook (React PWA)
navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
  .then((stream) => {
    const canvas = document.createElement("canvas");
    // Inject dynamic watermark overlay into video canvas frame
    ctx.fillText(`ACTA • ${campaignId} • ${new Date().toISOString()}`, 20, 40);
    ctx.fillText(`GPS: ${currentLat.toFixed(4)}, ${currentLng.toFixed(4)}`, 20, 60);
  });
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 16: In-App Camera Lock</span><span>PAGE 19 OF 33</span></div>
    </div>
    """,

    # PAGE 20: ZERO-COST VIDEO CLOUD & INSTAGRAM FLYWHEEL
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 17</span></div>
        <h1>17. Zero-Cost Video Cloud & Instagram Flywheel</h1>
        <h2>17.1 Eliminating High Private Video Hosting Costs</h2>
        <p>Streaming thousands of hours of video on private AWS S3 / Cloudflare Stream generates monthly bills exceeding ₹50,000, quickly exhausting startup capital. ACTA bypasses this entirely using existing global infrastructure:</p>
        <div class="grid-2">
          <div class="card card-blue">
            <div class="card-title">Channel A: YouTube Proof Cloud (₹0 Cost)</div>
            <p><strong>Role:</strong> Permanent Transparency Archive</p>
            <ul>
              <li>Raw proof videos are uploaded to the official ACTA YouTube channel via YouTube Data API v3.</li>
              <li>YouTube provides global CDN caching, auto-transcoding, and infinite hosting for <strong>₹0</strong>!</li>
              <li>Direct YouTube unlisted link embedded in donor's <em>"My Donations"</em> dashboard.</li>
            </ul>
          </div>
          <div class="card card-emerald">
            <div class="card-title">Channel B: Instagram Reels (₹0 CAC)</div>
            <p><strong>Role:</strong> Organic Viral Acquisition Engine</p>
            <ul>
              <li>Media interns edit 30-second emotional highlight clips from proof footage.</li>
              <li>Vertical 9:16 format with verified impact tags.</li>
              <li>Donors share reels on WhatsApp status, driving new students at <strong>₹0 ad spend</strong>.</li>
            </ul>
          </div>
        </div>
        <h2>17.2 Operational Realism</h2>
        <p>At 18–20 partner NGOs, the platform executes only <strong>4 to 6 campaigns per week</strong>, generating 4 to 6 videos. A 2-person student media team easily reviews and edits these in 3 hours weekly, serving tens of thousands of student donors!</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 17: Zero-Cost Video Cloud</span><span>PAGE 20 OF 33</span></div>
    </div>
    """,

    # PAGE 21: DPDP ACT 2023 COMPLIANCE
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 18</span></div>
        <h1>18. DPDP Act 2023 Beneficiary Privacy Protocol</h1>
        <div class="card card-amber">
          <div class="card-title">Statutory Compliance Mandate</div>
          <p>India's <strong>Digital Personal Data Protection Act (DPDP Act 2023)</strong> imposes severe financial penalties for unauthorized publication of imagery of minors, medical patients, and socio-economically vulnerable persons.</p>
        </div>
        <h2>18.1 Automated Face-Blurring Pipeline Architecture</h2>
        <ul>
          <li><strong>Minors (<18 Years Old):</strong> In all school kit distributions, orphanage drives, and slum educational projects, facial features of children are <strong>100% blurred by default</strong>.</li>
          <li><strong>Destitute & Hospitalized Beneficiaries:</strong> Faces of patients, destitute elderly individuals, and hospital case files are automatically masked to safeguard human dignity.</li>
          <li><strong>Field Workers & Authorized Staff:</strong> Adult NGO operatives and volunteer heads remain unblurred as official institutional representatives.</li>
        </ul>
        <h2>18.2 Computer Vision Blur Execution Algorithm</h2>
        <div class="wireframe">
# Automated Beneficiary Privacy Filter (OpenCV + MediaPipe)
def process_proof_privacy(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        faces = face_detector.detect(frame)
        for face in faces:
            if face.is_minor or face.is_vulnerable:
                (x, y, w, h) = face.bounding_box
                sub_face = frame[y:y+h, x:x+w]
                frame[y:y+h, x:x+w] = cv2.GaussianBlur(sub_face, (51, 51), 30)
        writer.write(frame)
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 18: DPDP Act Privacy</span><span>PAGE 21 OF 33</span></div>
    </div>
    """,

    # PAGE 22: CAMPAIGN SYSTEM: 7 STANDARD CAUSES
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 19</span></div>
        <h1>19. Campaign System: The 7 Standard Causes</h1>
        <p>ACTA maintains <strong>strictly 7 causes on the platform at any given time</strong> to prevent UI clutter and cognitive fatigue:</p>
        <table>
          <thead>
            <tr><th>Slot Type</th><th>Cause Title & Unit Cost</th><th>Lifecycle & Rotation Logic</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Permanent 1</strong></td><td>🍲 <strong>Zero Hunger</strong> (₹35 per hot meal)</td><td>Infinite cyclic pool. When target completes, next verified NGO takes over immediately.</td></tr>
            <tr><td><strong>Permanent 2</strong></td><td>🌳 <strong>Green Earth</strong> (₹150 per sapling & guard)</td><td>Infinite cyclic pool. Runs year-round across NCR educational campuses.</td></tr>
            <tr><td><strong>Permanent 3</strong></td><td>📚 <strong>Child Education</strong> (₹250 per school kit)</td><td>Infinite cyclic pool. Partners with orphanages and slum learning centers.</td></tr>
            <tr><td><strong>Permanent 4</strong></td><td>👴 <strong>Elder Care</strong> (₹300 per medicine/hygiene pack)</td><td>Infinite cyclic pool. Supports registered old-age homes and destitute seniors.</td></tr>
            <tr><td><strong>Permanent 5</strong></td><td>🧵 <strong>Women Empowerment</strong> (₹500 dry ration kit)</td><td>Infinite cyclic pool. Delivers monthly dry ration hampers to low-income widows.</td></tr>
            <tr><td><strong>Temporary 1</strong></td><td>🚨 <strong>Disaster & Crisis Relief</strong> (Dynamic)</td><td>Dynamic slot. Activates during emergency seasons (winter blankets, flood rations).</td></tr>
            <tr><td><strong>Temporary 2</strong></td><td>🐾 <strong>Emergency Stray Rescue</strong> (₹1,500 surgery)</td><td>Dynamic slot. Dedicated to urgent animal trauma cases; rotates as needs arise.</td></tr>
          </tbody>
        </table>
        <h2>Why NGOs Cannot Self-Create Campaigns</h2>
        <p>On ACTA, <strong>only the ACTA Admin creates campaigns based on standardized unit costs</strong>. NGOs merely apply to execute approved campaigns. This guarantees audited financial targets and eliminates inflated fundraising goals.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 19: 7 Standard Causes</span><span>PAGE 22 OF 33</span></div>
    </div>
    """,

    # PAGE 23: GAMIFICATION XP ECONOMY
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 20</span></div>
        <h1>20. Gamification: The ₹1 = 10 XP Economy</h1>
        <h2>20.1 The Master XP Math</h2>
        <p>Students thrive on instant positive reinforcement. On ACTA, every single rupee donated immediately translates into platform experience points:</p>
        <div class="card card-emerald">
          <div class="card-title">The Master XP Formula</div>
          <p><strong>1 Rupee Donated = 10 Acta XP</strong></p>
          <p>A ₹10 donation triggers an immediate +100 XP reward animation, activating genuine user dopamine!</p>
        </div>
        <h2>20.2 Additional XP Earning Triggers (Beyond Direct Money)</h2>
        <table>
          <thead>
            <tr><th>Action / Trigger</th><th>XP Reward</th><th>Strategic Purpose</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Direct Micro-Donation</strong></td><td>Amount × 10 XP (e.g. ₹20 = 200 XP)</td><td>Base micro-giving incentive.</td></tr>
            <tr><td><strong>Guild Milestone Bonus</strong></td><td>+200 XP for all active members</td><td>Encourages teamwork within the campus community.</td></tr>
            <tr><td><strong>Top 25 City Rank Boost</strong></td><td>+500 XP bonus</td><td>Drives healthy inter-college competitive pride.</td></tr>
            <tr><td><strong>3-Week Consistency Streak</strong></td><td>+150 XP bonus</td><td>Builds a recurring weekly giving habit.</td></tr>
            <tr><td><strong>Watch & Verify Proof Video</strong></td><td>+20 XP bonus</td><td>Incentivizes donors to inspect transparency footage.</td></tr>
          </tbody>
        </table>
        <h2>20.3 Anti-Exploit Guardrails</h2>
        <p>To prevent artificial XP farming, non-financial triggers (video watching, streaks) have a hard ceiling of 500 bonus XP per user per calendar week. All primary XP is strictly backed by verified UPI transaction hashes.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 20: Gamification XP Economy</span><span>PAGE 23 OF 33</span></div>
    </div>
    """,

    # PAGE 24: 10-LEVEL EXPONENTIAL LADDER
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 21</span></div>
        <h1>21. The 10-Level Exponential Giving Ladder</h1>
        <p>In modern community design, leveling up follows an <strong>exponential progression curve</strong>. Level 2 requires at least ₹500 (5,000 XP), ensuring prestige:</p>
        <table>
          <thead>
            <tr><th>Level</th><th>Level Title</th><th>XP Required</th><th>Direct Equiv.</th><th>Profile Recognition & Perks</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Level 01</strong></td><td><strong>Seed Giver</strong> 🌱</td><td>0 – 4,999 XP</td><td>₹0 – ₹499</td><td>Bronze Seed Tag. Unlocks upon very first ₹10 act.</td></tr>
            <tr><td><strong>Level 02</strong></td><td><strong>Kind Giver</strong> 🤝</td><td>5,000 – 11,999 XP</td><td><strong>₹500+</strong></td><td>Silver Border Ring. Community chat access unlocked.</td></tr>
            <tr><td><strong>Level 03</strong></td><td><strong>Active Giver</strong> ⭐</td><td>12,000 – 24,999 XP</td><td>₹1,200+</td><td>Polished Silver Ring + Guild shoutout badge.</td></tr>
            <tr><td><strong>Level 04</strong></td><td><strong>Impact Giver</strong> 🔷</td><td>25,000 – 49,999 XP</td><td>₹2,500+</td><td>Sapphire Blue Ring + Voting power on next cause.</td></tr>
            <tr><td><strong>Level 05</strong></td><td><strong>Dedicated Giver</strong> 🛡️</td><td>50,000 – 99,999 XP</td><td>₹5,000+</td><td>Gold Shield Ring + Featured on Campus Board.</td></tr>
            <tr><td><strong>Level 06</strong></td><td><strong>Community Pillar</strong> 🏛️</td><td>1,00,000 – 1,99,999 XP</td><td>₹10,000+</td><td>Radiant Gold Ring + Authority to create Campus Guilds.</td></tr>
            <tr><td><strong>Level 07</strong></td><td><strong>Change Maker</strong> ⚔️</td><td>2,00,000 – 3,99,999 XP</td><td>₹20,000+</td><td>Emerald Ring + Direct invite to annual NGO field audits.</td></tr>
            <tr><td><strong>Level 08</strong></td><td><strong>Master Benefactor</strong> 💎</td><td>4,00,000 – 6,99,999 XP</td><td>₹40,000+</td><td>Ruby Ring + Priority sponsor matching on contributions.</td></tr>
            <tr><td><strong>Level 09</strong></td><td><strong>Grand Philanthropist</strong> 🌟</td><td>7,00,000 – 9,99,999 XP</td><td>₹70,000+</td><td>Glowing Amethyst Ring + City Hall of Fame Top Tier.</td></tr>
            <tr><td><strong>Level 10</strong></td><td><strong>The Crown Legend</strong> 👑</td><td>10,00,000+ XP</td><td>₹1,00,000+</td><td><strong>Animated Diamond Crown Ring</strong> + National Resence Impact Award.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 21: 10-Level Ladder</span><span>PAGE 24 OF 33</span></div>
    </div>
    """,

    # PAGE 25: CAMPUS COMMUNITIES & INSTITUTIONAL GUILDS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 22</span></div>
        <h1>22. Campus Communities & Institutional Guilds</h1>
        <h2>22.1 The Power of Guild Mechanics in College Culture</h2>
        <p>Donating alone feels isolated. Donating as an organized <strong>ACTA Campus Community / Guild</strong> creates powerful, positive peer momentum:</p>
        <ul>
          <li>Students join their institutional community (e.g., <em>GL Bajaj BCA 2nd Year</em>, <em>Galgotias CS Club</em>, <em>Hostel Block B</em>).</li>
          <li>When a member donates ₹10, both their personal score and their <strong>Guild Score increase simultaneously</strong>.</li>
          <li>Students naturally urge their peers on WhatsApp: <em>"We are #3 in Greater Noida, just 30 of us donating ₹10 will push us past Bennett University to #2!"</em></li>
        </ul>
        <h2>22.2 Guild Tier Progression Ladder</h2>
        <table>
          <thead>
            <tr><th>Guild Tier</th><th>Total Guild Funding</th><th>Perks & Visual Unlocks</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Tier 1: Rising Clan</strong></td><td>₹0 – ₹4,999</td><td>Standard Guild tag; private clan discussion feed.</td></tr>
            <tr><td><strong>Tier 2: Impact Brigade</strong></td><td>₹5,000 – ₹19,999</td><td>Silver Clan Shield; featured in departmental newsletter.</td></tr>
            <tr><td><strong>Tier 3: Campus Titans</strong></td><td>₹20,000 – ₹49,999</td><td>Gold Clan Shield; custom cause sponsorship rights.</td></tr>
            <tr><td><strong>Tier 4: Apex Guild</strong></td><td>₹50,000+</td><td>Crown Diamond Shield; official campus trophy from Resence.</td></tr>
          </tbody>
        </table>
        <h2>22.3 Community Creation Verification Guardrail</h2>
        <p>To prevent spam, arbitrary individuals cannot create hundreds of fake guilds. A student leader must submit their college ID card or verified institutional email (<code>@glbajaj.org</code>) to instantiate an official Campus Community.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 22: Campus Communities</span><span>PAGE 25 OF 33</span></div>
    </div>
    """,

    # PAGE 26: TOP 25 LEADERBOARD & ANTI-SHAMING PRIVACY
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 23</span></div>
        <h1>23. Top 25 Leaderboard & Anti-Shaming Privacy</h1>
        <div class="card card-emerald">
          <div class="card-title">The Anti-Shaming Design Philosophy</div>
          <p>Publicly listing every individual's exact score creates toxic humiliation. A student who could only afford ₹10 feels ashamed seeing a peer with ₹500. ACTA solves this through a brilliant privacy rule.</p>
        </div>
        <h2>23.1 The Anti-Shaming Privacy Rule</h2>
        <ul>
          <li><strong>Individual scores remain completely private.</strong> A student only sees their own personal progress, level, and unlocked badges.</li>
          <li>The public leaderboard showcases <strong>strictly the Top 25</strong> performers at two geographical tiers:
            <ol>
              <li><strong>Top 25 Communities / Guilds (City & National Level)</strong></li>
              <li><strong>Top 25 Donors (City & National Level — Hall of Fame)</strong></li>
            </ol>
          </li>
          <li>Casual donors are never exposed to public ranking, preserving dignity and emotional comfort.</li>
        </ul>
        <h2>23.2 Geographical Scoping: City vs. Country</h2>
        <p>Students care far more about local college rivalry than distant national figures. The leaderboard defaults to the <strong>City Level (Greater Noida / Delhi NCR)</strong>: GL Bajaj vs. Galgotias vs. Sharda vs. Bennett.</p>
        <div class="wireframe">
// Redis Sorted Set Caching Schema for High-Throughput Leaderboards
ZADD leaderboard:city:greater_noida:guilds 25400 "guild_glbajaj_bca"
ZREVRANGE leaderboard:city:greater_noida:guilds 0 24 WITHSCORES
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 23: Top 25 Leaderboard</span><span>PAGE 26 OF 33</span></div>
    </div>
    """,

    # PAGE 27: THE AI LAYER: GEMINI LLM & VISION
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 24</span></div>
        <h1>24. The AI Layer: AI Advisor & Gemini Vision</h1>
        <p>ACTA integrates Google Gemini API across two specialized operational roles:</p>
        <div class="grid-2">
          <div class="card card-blue">
            <div class="card-title">Student Facing: Gemini 1.5 Flash (LLM)</div>
            <ul>
              <li><strong>Pocket Money Planner:</strong> Student asks: <em>"I have ₹35 left in UPI, where does it help most?"</em> Gemini directs funds to the cause nearest completion.</li>
              <li><strong>Personalized Monthly Story:</strong> Generates beautiful impact narratives: <em>"Piyush, this month your small acts funded 14 meals and 2 trees."</em></li>
              <li><strong>Cause Discovery:</strong> Conversational matching based on student interest (animals, nature, schools).</li>
            </ul>
          </div>
          <div class="card card-emerald">
            <div class="card-title">Admin Facing: Gemini Vision Multimodal</div>
            <ul>
              <li><strong>Receipt OCR Analysis:</strong> Extracts GSTIN, itemized quantities, and cross-checks totals against campaign line budgets.</li>
              <li><strong>Frame Fraud Detection:</strong> Generates perceptual hashes (pHash) on proof video frames to detect reused footage or online stock clips.</li>
              <li><strong>Face Coordinate Extraction:</strong> Feeds bounding box coordinates to the automated privacy blur filter.</li>
            </ul>
          </div>
        </div>
        <h2>Gemini System Prompt Contract (Admin Multimodal Frame Auditor)</h2>
        <div class="wireframe">
SYSTEM: You are the ACTA Fraud Auditor. Analyze the attached bill photo & video frame.
TASK: 1. Extract Merchant GSTIN and total amount.
      2. Verify items match campaign category: "Zero Hunger".
      3. Flag any artifacts indicating digital editing or screen recording.
OUTPUT FORMAT: JSON { gstin: string, total: float, match_score: float, flags: [] }
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 24: The AI Layer</span><span>PAGE 27 OF 33</span></div>
    </div>
    """,

    # PAGE 28: ZERO-LIABILITY VOLUNTEER SAFETY SHIELD
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 25</span></div>
        <h1>25. Zero-Liability Volunteer Safety Shield</h1>
        <div class="card card-emerald">
          <div class="card-title">The Legal Firewall That Protects the Startup</div>
          <p>Early prototypes frequently collapse because student founders attempt to recruit, manage, and dispatch volunteers directly to slums, accident zones, or flood relief camps. This creates massive criminal and civil liability risks.</p>
        </div>
        <h2>25.1 Why ACTA Dropped Direct Volunteer Recruitment</h2>
        <ul>
          <li><strong>Physical Safety & Accidents:</strong> If an 18-year-old student gets injured traveling to a dangerous location, the platform faces severe civil and criminal negligence suits.</li>
          <li><strong>Police Verification Overhead:</strong> Verifying criminal background checks for thousands of student volunteers across cities is operationally impossible for a seed-stage startup.</li>
          <li><strong>Harassment Liabilities:</strong> Managing mixed-gender volunteer field teams without corporate security infrastructure creates unacceptable risk.</li>
        </ul>
        <h2>25.2 The Operational Firewall Mechanism</h2>
        <p>ACTA operates strictly as a <strong>Technology, Escrow, and Verification Infrastructure Layer</strong>:</p>
        <ul>
          <li>ACTA never hires, dispatches, or directs individual volunteers.</li>
          <li>On-ground execution is conducted <strong>100% by the verified partner NGO</strong> using their own pre-existing, registered staff and vetted volunteers.</li>
          <li>The partner NGO assumes <strong>100% legal, physical, and insurance liability</strong> for all ground activities under signed legal MoUs.</li>
        </ul>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 25: Volunteer Safety Shield</span><span>PAGE 28 OF 33</span></div>
    </div>
    """,

    # PAGE 29: NGO PERFORMANCE SCORING & 2-STRIKE CONTRACT
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 26</span></div>
        <h1>26. NGO Performance Scoring & 2-Strike Contract</h1>
        <h2>26.1 The NGO Performance Index Formula (0 to 100)</h2>
        <p>Every partner NGO is continuously evaluated across four objective metrics:</p>
        <div class="card card-highlight">
          <p><strong>Score = (SLA Compliance × 0.40) + (Proof Quality × 0.30) + (Beneficiary Feedback × 0.20) + (Audit Compliance × 0.10)</strong></p>
        </div>
        <ul>
          <li><strong>SLA Compliance (40% Weight):</strong> Delivering proof within 96 hours (+25 pts per on-time delivery; -25 pts per grace period entry).</li>
          <li><strong>Proof Quality Score (30% Weight):</strong> Clear vendor GST bills, stable in-app video capture, audible voiceover.</li>
          <li><strong>Beneficiary Feedback (20% Weight):</strong> Community satisfaction ratings from ground spot-checks.</li>
          <li><strong>Audit Compliance (10% Weight):</strong> Accurate fuel slips for the 10% operational allowance.</li>
        </ul>
        <h2>26.2 The 2-Strike Legal Contract (MoU)</h2>
        <table>
          <thead>
            <tr><th>Violation Tier</th><th>Offense Scope</th><th>Statutory Action</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Strike 1</strong></td><td>Late proof (>96h), illegible bills, or unblurred minor faces.</td><td>Held escrow payout. Performance docked 25 points. Mandatory offline physical review with founder.</td></tr>
            <tr><td><strong>Strike 2</strong></td><td>Deliberate submission of tampered/recycled video or fake bills.</td><td>Immediate permanent blacklisting on ACTA + Legal recovery under the signed binding MoU.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 26: NGO Performance Scoring</span><span>PAGE 29 OF 33</span></div>
    </div>
    """,

    # PAGE 30: BUSINESS MODEL & 5% MAINTENANCE FEE MATH
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 27</span></div>
        <h1>27. Business Model & 5% Maintenance Fee Math</h1>
        <h2>27.1 The 5% Platform Maintenance Fee</h2>
        <p>ACTA is structured as a sustainable social technology enterprise. The 5% maintenance fee is deducted only upon successful campaign delivery. It covers server bandwidth, database hosting, AI multimodal frame audits, and field team travel expenses. It ensures the platform survives independently without begging for philanthropic grants.</p>
        <h2>27.2 Annualized Financial Projection (Pilot Cohort: 20 NGOs)</h2>
        <table>
          <thead>
            <tr><th>Metric Parameter</th><th>Monthly Volume</th><th>Annualized Run-Rate</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Active Campaigns Completed</strong></td><td>20 Campaigns</td><td>240 Campaigns</td></tr>
            <tr><td><strong>Average Campaign Value</strong></td><td>₹25,000.00</td><td>₹25,000.00</td></tr>
            <tr><td><strong>Gross Donation Volume (GMV)</strong></td><td>₹5,00,000.00</td><td>₹60,00,000.00</td></tr>
            <tr><td><strong>Disbursed to NGOs (95%)</strong></td><td>₹4,75,000.00</td><td>₹57,00,000.00</td></tr>
            <tr><td><strong>ACTA Platform Revenue (5%)</strong></td><td><strong>₹25,000.00</strong></td><td><strong>₹3,00,000.00</strong></td></tr>
            <tr><td><strong>Operating Infrastructure Cost</strong></td><td>₹4,500.00</td><td>₹54,000.00</td></tr>
            <tr><td><strong>Net Platform Operating Surplus</strong></td><td><strong>₹20,500.00</strong></td><td><strong>₹2,46,000.00</strong></td></tr>
          </tbody>
        </table>
        <h2>27.3 3-Year Scaling Projections</h2>
        <p>By Year 3 (expanding across 10 educational clusters in Uttar Pradesh and Delhi NCR), GMV reaches ₹4.8 Cr, generating ₹24 Lakhs in platform revenue, fully self-funding operational growth.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 27: Business Model</span><span>PAGE 30 OF 33</span></div>
    </div>
    """,

    # PAGE 31: TECHNICAL ARCHITECTURE & DATABASE SCHEMAS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 28</span></div>
        <h1>28. Technology Stack & Database Schemas</h1>
        <h2>28.1 Production Stack Components</h2>
        <p>Frontend: React 18 / Vite / Tailwind CSS • Backend: Node.js 22 LTS / Express • DB: PostgreSQL (Supabase) • Cache: Upstash Redis • AI: Google Gemini 1.5 • Gateway: Razorpay Smart UPI.</p>
        <h2>28.2 Relational Database Schema (PostgreSQL DDL)</h2>
        <div class="wireframe">
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone VARCHAR(15) UNIQUE NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  college_id VARCHAR(50),
  guild_id UUID REFERENCES campus_guilds(id),
  xp INT DEFAULT 0,
  level INT DEFAULT 1,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE escrow_batches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cause_id UUID REFERENCES causes(id),
  ngo_id UUID REFERENCES ngos(id),
  total_target NUMERIC(10,2) NOT NULL,
  direct_cause_90 NUMERIC(10,2) NOT NULL,
  ngo_ops_10 NUMERIC(10,2) NOT NULL,
  acta_fee_5 NUMERIC(10,2) NOT NULL,
  deadline_at TIMESTAMPTZ NOT NULL,
  status VARCHAR(30) DEFAULT 'POOLING' -- MILESTONE_LOCKED, DISBURSED, COMPLETED, REFUNDED
);
        </div>
        <h2>28.3 Core REST API Endpoints</h2>
        <ul>
          <li><code>POST /api/v1/donations/intent</code>: Initiates ₹10 UPI payment session.</li>
          <li><code>POST /api/v1/ngo/proof/submit</code>: Commits 2-phase video telemetry and bills.</li>
          <li><code>POST /api/v1/admin/escrow/release</code>: Validates audit and releases payout.</li>
        </ul>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 28: Technology Stack</span><span>PAGE 31 OF 33</span></div>
    </div>
    """,

    # PAGE 32: 90-DAY EXECUTION ROADMAP
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">CHAPTER 29</span></div>
        <h1>29. 90-Day Execution Roadmap & Campus Pilot</h1>
        <table>
          <thead>
            <tr><th>Sprint Phase</th><th>Execution Window</th><th>Key Operational Deliverables</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Phase 1: Incubation & Partner MoUs</strong></td><td>Days 1 – 30</td><td>Secure GLBCRI incubation letterhead; onboard first 10 local Greater Noida NGOs via offline visits.</td></tr>
            <tr><td><strong>Phase 2: Closed Campus Pilot</strong></td><td>Days 31 – 60</td><td>Deploy 30-day pilot across GL Bajaj Knowledge Park hostels; target 1,000 student givers & 10 completed campaigns.</td></tr>
            <tr><td><strong>Phase 3: Inter-College League</strong></td><td>Days 61 – 90</td><td>Expand to Galgotias, Sharda, and Bennett University; activate the Top 25 City Guild leaderboard.</td></tr>
          </tbody>
        </table>
        <h2>29.2 Success Metrics for Pilot Phase (GL Bajaj Campus)</h2>
        <ul>
          <li><strong>Student Participation:</strong> 1,000+ verified active student donors across BCA, B.Tech, and MBA departments.</li>
          <li><strong>Micro-Donations Completed:</strong> ₹50,000+ gross funds raised across 10 campaigns with 0% SLA failure.</li>
          <li><strong>Proof Delivery:</strong> 10 verified YouTube proof videos archived with 100% vendor bill compliance.</li>
        </ul>
        <h2>29.3 Risk Mitigation Matrix</h2>
        <p>In case of student exams, campaign targets are lowered to ₹5,000 micro-drives; in case of rain delays, 24-hour weather grace extension is approved by platform admin with mandatory ground photos.</p>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Chapter 29: Execution Roadmap</span><span>PAGE 32 OF 33</span></div>
    </div>
    """,

    # PAGE 33: APPENDIX & INCUBATION ASKS
    """
    <div class="page">
      <div>
        <div class="header-bar"><span>ACTA by Resence — Product Requirements Document</span><span class="brand">APPENDIX & SIGN-OFF</span></div>
        <h1>Appendix: Founder Profile & GLBCRI Incubation Asks</h1>
        <h2>A. Founder Ground Truth Profile</h2>
        <ul>
          <li><strong>Founder & CEO:</strong> Piyush Singh (18 Years Old).</li>
          <li><strong>Academic Standing:</strong> BCA 2nd Year (3rd Semester), GL Bajaj Institute of Management, Greater Noida.</li>
          <li><strong>Technical Competencies:</strong> Google Student Ambassador (GSA '26), Google Cloud Gen AI Academy Cohort 3.</li>
          <li><strong>Current Stage:</strong> Functional interactive web prototype deployed at <code>resence.in</code> / <code>acta.resence.in</code>. Complete system architecture, escrow rules, and 33-page PRD specifications locked.</li>
        </ul>
        <h2>B. The Specific Asks from GLBCRI (Bharat Udyam Sangam 2026)</h2>
        <ol>
          <li><strong>Institutional Credibility & Letterhead:</strong> Introducing ACTA under GL Bajaj / GLBCRI official backing to 18–20 verified NGOs in Greater Noida and Noida.</li>
          <li><strong>Campus Pilot Authorization:</strong> Permission to run an official 30-day student micro-giving pilot across GL Bajaj Knowledge Park hostels and academic departments.</li>
          <li><strong>Pre-Incubation Mentorship:</strong> Legal structuring for NGO MoUs, Section 8/Pvt Ltd formalization, and seed grant guidance.</li>
        </ol>
        <div class="card card-emerald" style="margin-top: 14px; text-align: center;">
          <div class="card-title">ACTA by Resence — Small Acts, Big Impacts.</div>
          <p>Master Product Specification & Architecture Bible • Approved by Piyush Singh, Founder & CEO</p>
        </div>
      </div>
      <div class="footer-bar"><span>ACTA by Resence • Appendix & Sign-Off</span><span>PAGE 33 OF 33</span></div>
    </div>
    """
]

# Assemble the full HTML
full_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — Master Product Specification & Architecture Bible (33-Page SSOT)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #111827; background-color: #FFFFFF; line-height: 1.38; font-size: 8.8pt;
    -webkit-font-smoothing: antialiased;
  }
  .page { 
    height: 270mm; max-height: 270mm; overflow: hidden;
    display: flex; flex-direction: column; justify-content: space-between; 
    page-break-after: always; break-after: page; 
  }
  .cover-page { 
    height: 270mm; max-height: 270mm; overflow: hidden;
    display: flex; flex-direction: column; justify-content: space-between; 
    padding: 10px 5px; page-break-after: always; break-after: page; 
  }
  .header-bar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 8px; font-size: 7.2pt; text-transform: uppercase; letter-spacing: 1px; color: #64748B; font-weight: 600; }
  .header-bar .brand { color: #0F172A; font-weight: 800; }
  .footer-bar { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #E2E8F0; padding-top: 4px; margin-top: 6px; font-size: 7.2pt; color: #94A3B8; }
  .brand-badge { background: #0F172A; color: #FFFFFF; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 9pt; letter-spacing: 2px; padding: 4px 10px; border-radius: 4px; }
  .doc-tag { font-size: 7.5pt; text-transform: uppercase; letter-spacing: 1px; color: #64748B; font-weight: 700; }
  .cover-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px; }
  .cover-body { margin-top: 24px; margin-bottom: 24px; }
  .hero-h1 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 34pt; font-weight: 800; letter-spacing: -1.5px; line-height: 1.05; color: #0F172A; margin-bottom: 8px; }
  .hero-h1 span { color: #059669; }
  .hero-sub { font-family: 'Space Grotesk', sans-serif; font-size: 14pt; color: #334155; font-weight: 600; margin-bottom: 16px; letter-spacing: -0.5px; }
  .hero-paragraph { font-size: 9.8pt; color: #475569; max-width: 600px; line-height: 1.5; margin-bottom: 20px; }
  .pill-group { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 20px; }
  .pill-item { background: #F1F5F9; color: #334155; font-size: 7.2pt; font-weight: 600; padding: 3px 8px; border-radius: 999px; border: 1px solid #E2E8F0; }
  .pill-item.green { background: #ECFDF5; color: #065F46; border-color: #A7F3D0; }
  .pill-item.blue { background: #EFF6FF; color: #1E40AF; border-color: #BFDBFE; }
  .meta-table-box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .meta-col h6 { font-size: 6.8pt; text-transform: uppercase; color: #64748B; letter-spacing: 1px; margin-bottom: 2px; }
  .meta-col p { font-size: 8.5pt; font-weight: 600; color: #0F172A; }
  h1 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13.5pt; font-weight: 800; color: #0F172A; letter-spacing: -0.4px; margin-bottom: 6px; padding-bottom: 4px; border-bottom: 1.5px solid #E2E8F0; }
  h2 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9.8pt; font-weight: 700; color: #1E293B; margin-top: 6px; margin-bottom: 4px; letter-spacing: -0.2px; }
  p { margin-bottom: 5px; color: #334155; line-height: 1.38; }
  ul, ol { margin-left: 14px; margin-bottom: 6px; color: #334155; }
  li { margin-bottom: 2px; }
  strong { color: #0F172A; font-weight: 600; }
  .card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 5px; padding: 8px 10px; margin-bottom: 6px; font-size: 8.2pt; }
  .card-highlight, .card-emerald { background: #F0FDF4; border-left: 3.5px solid #059669; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #059669; }
  .card-blue { background: #F8FAFC; border-left: 3.5px solid #2563EB; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #2563EB; }
  .card-amber { background: #FFFBEB; border-left: 3.5px solid #D97706; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #D97706; }
  .card-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 8.8pt; color: #0F172A; margin-bottom: 2px; }
  table { width: 100%; border-collapse: collapse; margin: 6px 0 6px 0; font-size: 7.5pt; line-height: 1.28; }
  th { background: #0F172A; color: #FFFFFF; text-align: left; padding: 5px 6px; font-weight: 600; font-size: 7.2pt; letter-spacing: 0.5px; }
  td { padding: 4px 6px; border-bottom: 1px solid #E2E8F0; color: #334155; vertical-align: top; }
  tr:nth-child(even) td { background: #F8FAFC; }
  .wireframe { background: #0F172A; color: #F8FAFC; padding: 7px 9px; border-radius: 5px; font-family: 'Courier New', Courier, monospace; font-size: 6.8pt; line-height: 1.25; margin: 5px 0; white-space: pre; overflow-x: hidden; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-bottom: 6px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; margin-bottom: 6px; }
  .stat-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 5px; padding: 6px; text-align: center; }
  .stat-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13pt; font-weight: 800; color: #059669; }
  .stat-lbl { font-size: 6.8pt; text-transform: uppercase; letter-spacing: 0.5px; color: #64748B; font-weight: 600; }
</style>
</head>
<body>
""" + "\n".join(pages_content) + """
</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML written to {html_file}")

# Compile with Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Compiling Master 33-Page PDF via Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    page_count = len(reader.pages)
    print(f"SUCCESS: Master PDF compiled successfully!")
    print(f"EXACT PAGE COUNT: {page_count} Pages")
    print(f"FILE SIZE: {os.path.getsize(pdf_file)} bytes")
else:
    print(f"PDF creation failed: {result.stderr}")
