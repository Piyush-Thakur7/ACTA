import os
import sys
import shutil
import subprocess
import pypdf
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"
downloads_dir = r"C:\Users\HP\Downloads"

docx_target = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.docx")
html_target = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.html")
pdf_target = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.pdf")

print("Compiling ACTA Master PRD v2.6 Revised (.docx and .pdf)...")

# ==============================================================================
# HTML BUILDER (45 Curated, Upgraded, Grounded Pages)
# ==============================================================================

# Let's import pages from build_42_page_master_prd.py and upgrade them
with open(os.path.join(docs_dir, "build_42_page_master_prd.py"), "r", encoding="utf-8") as f:
    source_code = f.read()

# Execute source_code in a clean dictionary to extract pages_content
namespace = {}
# Replace the file targets inside source_code so it doesn't overwrite old files prematurely
exec(source_code, namespace)
raw_pages = namespace.get("pages_content", [])
print(f"Loaded {len(raw_pages)} raw pages from master template.")

upgraded_pages = []

for idx, page_html in enumerate(raw_pages):
    p = page_html
    page_num = idx + 1
    
    # 1. Update Version and Document Badges
    p = p.replace("SSOT V2.5", "SSOT V2.6 REVISED")
    p = p.replace("v2.5", "v2.6")
    p = p.replace("Small Acts, Big Impacts.", "Small Acts. Big Impact.")
    p = p.replace("Small Acts, Big Impacts", "Small Acts. Big Impact.")
    
    # 2. Fix 105% and 90/10/5 Contradictions
    p = p.replace("90/10 NGO Split Accounting", "Canonical ₹100 Split (₹5 Fee / ₹95 NGO Share)")
    p = p.replace("90/10/5 Rule", "Canonical Fund Allocation Model (₹5 Service Fee / ₹95 NGO Share)")
    p = p.replace("The 90/10 Fund Allocation Split Rule", "Canonical Fund Allocation Specification (₹5 Service Fee / ₹95 NGO Share)")
    p = p.replace("90/10 ledger", "Fund allocation ledger")
    p = p.replace("90/10 Ledgers", "Allocation Ledgers")
    p = p.replace("90/10 split tracking", "Fund allocation tracking")
    
    # 3. Chapter 15.2 Allocation Upgrade (Page 19)
    if "15. Complete Payment & Fund Lifecycle Engine" in p:
        p = p.replace("""        <h2>15.2 Fund Allocation Breakdown (90/10/5 Rule)</h2>
        <p>100% of donor micro-donations pool intact in the Escrow Vault. Upon milestone completion and verification:</p>
        <ul>
          <li><strong>90% Direct Cause Supplies:</strong> Paid against wholesale vendor GST tax invoice (food grains, saplings, notebooks).</li>
          <li><strong>10% NGO Operational Allowance:</strong> Audited tempo fuel bills, packing sacks, and basic volunteer logistics.</li>
          <li><strong>5% Platform Maintenance Fee:</strong> Deducted from the campaign gross post-verification to fund cloud hosting and AI auditing.</li>
        </ul>""", """        <h2>15.2 Canonical Fund Allocation Specification (Proposed Accounting)</h2>
        <p>100% of donor micro-donations pool intact in the Escrow Vault. The financial allocation model permanently resolves the previous 105% mathematical contradiction:</p>
        <ul>
          <li><strong>ACTA Proposed Service Fee: ₹5.00 (5% of gross):</strong> Retained by ACTA for providing software platform, verification telemetry, and donor reporting services.</li>
          <li><strong>Eligible Partner NGO Share: ₹95.00 (95% of gross):</strong> Transferred directly to the verified partner NGO's account via payment aggregator settlement.</li>
          <li><strong>Permitted NGO Operational Allowance: ₹9.50 (10% of NGO share):</strong> The NGO may utilize up to 10% of its ₹95 for audited transport and packaging ONLY if campaign terms, donor restrictions, and legal obligations permit it.</li>
          <li><strong>Direct Campaign Cause Execution: ₹85.50 (90% of NGO share):</strong> Spent directly on wholesale vendor supplies backed by itemized GST invoices.</li>
        </ul>
        <p><em>*Note: This is a proposed accounting illustration, not confirmation of an approved payment provider settlement. Taxes, refunds, and gateway fees are excluded.</em></p>""")

    # 4. Chapter 18 Upgrade (Page 22) - Add Continuity Reserve
    if "18. 5% Platform Maintenance Fee Unit Economics" in p:
        p = p.replace("""        <h2>18.3 3-Year Scaling Projections</h2>
        <p>By Year 3 (expanding across 10 educational clusters in Uttar Pradesh and Delhi NCR), GMV reaches ₹4.8 Cr, generating ₹24 Lakhs in platform revenue, fully self-funding operational growth.</p>""", """        <h2>18.3 ACTA Business Continuity Reserve Policy</h2>
        <div class="card card-emerald">
          <div class="card-title">Continuity Reserve & Emergency Delivery Safeguard</div>
          <p>ACTA records earned service fee revenue separately from donor funds and NGO settlements. Management earmarks <strong>20% of earned service fees</strong> (e.g., ₹1.00 out of ₹5.00 earned) into an internal Continuity Reserve. In the rare event that an NGO defaults after funds are disbursed, reserve funds may be deployed to fund an approved substitute NGO, ensuring beneficiaries are never abandoned. <strong>Restricted donor donations are strictly never used as reserve substitutes.</strong></p>
        </div>
        <h2>18.4 3-Year Scaling Projections</h2>
        <p>By Year 3, GMV reaches ₹4.8 Cr across 10 educational clusters, generating ₹24 Lakhs in fee revenue and maintaining a ₹4.8 Lakh internal continuity reserve.</p>""")

    # 5. Chapter 19 Upgrade (Page 23) - Legal Custody & 10-Point Checklist
    if "19. Legal Custody, Virtual Accounts & 80G" in p:
        p = p.replace("""        <h2>19.2 Consolidated Section 80G Tax Certificates</h2>
        <p>Because micro-donations are ₹10 to ₹50, issuing individual 80G receipts per transaction is computationally inefficient. At the close of each financial year, ACTA generates an automated **Consolidated Annual 80G Impact Certificate** aggregating all contributions made by the student to registered 80G partner NGOs, downloadable with one click from their profile.</p>""", """        <h2>19.2 10-Point Legal, Regulatory & Fintech Review Checklist</h2>
        <p>Before launching live pilots, the platform undergoes formal review across 10 governance domains:</p>
        <ol style="font-size: 7.2pt; line-height: 1.25; margin-left: 14px;">
          <li><strong>SaaS Status:</strong> Technical intermediary under IT Act 2000 Section 79, not a donation-holding entity.</li>
          <li><strong>Split Settlement:</strong> RBI PA guideline review for Razorpay Route / Cashfree Split automated payouts.</li>
          <li><strong>Section 80G Receipts:</strong> Issued exclusively by partner NGOs; Form 10BD automated data extraction.</li>
          <li><strong>GST on Tech Fees:</strong> 18% GST applicability on ACTA's ₹5 service fee and B2B invoicing.</li>
          <li><strong>Escrow / Nodal Custody:</strong> Compliance with RBI Master Directions on digital payment intermediaries.</li>
          <li><strong>NGO Master Service Agreement:</strong> Enforceability of 5% fee, 10% ops cap, dynamic SLAs, and 2-strike default.</li>
          <li><strong>Dispute Liabilities:</strong> Clear chargeback recovery protocols and rolling reserve buffers.</li>
          <li><strong>Reserve Accounting:</strong> Earmarked continuity reserve classification under ICAI AS 29 / Ind AS 37.</li>
          <li><strong>DPDP Act 2023:</strong> MediaPipe automated minor facial blurring (<18 years) for video archive privacy.</li>
          <li><strong>FCRA Ring-Fencing:</strong> Programmatic blocking of foreign cards and non-INR accounts; domestic UPI only.</li>
        </ol>""")

    # 6. Chapter 24 Upgrade (Page 28) - Canonical Fund Allocation Detailed Table
    if "24. The 90/10 Fund Allocation Split Rule" in p or "Chapter 24: 90/10 Split Rule" in p:
        p = p.replace("24. The 90/10 Fund Allocation Split Rule", "24. Canonical Fund Allocation Specification")
        p = p.replace("Chapter 24: 90/10 Split Rule", "Chapter 24: Canonical Fund Allocation")
        p = p.replace("""        <h2>24.1 The 90/10 Allocation Framework</h2>
        <p>A fatal flaw of traditional Indian charities is the administrative black hole. Some organizations consume 40% to 60% of public donations on executive salaries, plush corporate offices, and PR agencies. ACTA legally limits non-profit overheads through the immutable **90/10 Allocation Rule** enforced at the database level.</p>
        <div class="grid-2">
          <div class="card card-emerald">
            <div class="card-title">90% Direct Cause Supplies</div>
            <p>At least 90% of every rupee must be paid directly to wholesale vendors for tangible relief materials (e.g. rice bags, medical bandages, textbooks, saplings). Backed by GST invoices.</p>
          </div>
          <div class="card card-amber">
            <div class="card-title">10% NGO Operational Allowance</div>
            <p>A maximum of 10% may be claimed for operational logistics: local tempo/auto fuel, loading labor, packing sacks. Receipts required.</p>
          </div>
        </div>""", """        <h2>24.1 Canonical Fund Allocation Specification (₹5 / ₹95 Split)</h2>
        <p>ACTA permanently resolves all mathematical ambiguity by locking the exact allocation formula across every transaction tier. For every ₹100 donation: ACTA receives ₹5 (5%), NGO receives ₹95 (95%), NGO permitted operations are capped at ₹9.50 (10% of NGO share), and direct cause supplies receive ₹85.50 (90% of NGO share).</p>
        <table>
          <thead>
            <tr><th>Gross Donation</th><th>ACTA Fee (5%)</th><th>NGO Payout (95%)</th><th>NGO Permitted Ops (Max 10%)</th><th>Direct Cause Supplies (Min 90%)</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>₹10.00</strong></td><td>₹0.50</td><td>₹9.50</td><td>₹0.95</td><td>₹8.55</td></tr>
            <tr><td><strong>₹50.00</strong></td><td>₹2.50</td><td>₹47.50</td><td>₹4.75</td><td>₹42.75</td></tr>
            <tr><td><strong>₹100.00</strong></td><td><strong>₹5.00</strong></td><td><strong>₹95.00</strong></td><td><strong>₹9.50</strong></td><td><strong>₹85.50</strong></td></tr>
            <tr><td><strong>₹1,000.00</strong></td><td>₹50.00</td><td>₹950.00</td><td>₹95.00</td><td>₹855.00</td></tr>
            <tr><td><strong>₹10,000.00</strong></td><td>₹500.00</td><td>₹9,500.00</td><td>₹950.00</td><td>₹8,550.00</td></tr>
            <tr><td><strong>₹25,000.00</strong></td><td>₹1,250.00</td><td>₹23,750.00</td><td>₹2,375.00</td><td>₹21,375.00</td></tr>
          </tbody>
        </table>
        <p><em>*Note: This is a proposed accounting illustration, not confirmation of an approved payment provider settlement. UPI transactions feature 0% MDR. Taxes and chargebacks apply per legal terms.</em></p>""")

    # 7. Chapter 35 Upgrade (Page 38) - 12-Step Replacement Workflow & Communication
    if "35. NGO Performance Scoring & 2-Strike Contract" in p:
        p = p.replace("""        <h2>35.2 The 2-Strike Default Contract & Permanent Blacklisting</h2>
        <p>ACTA maintains a zero-tolerance policy regarding unverified funds. Non-profits sign a binding institutional agreement containing the **2-Strike Default Rule**:</p>
        <ul>
          <li><strong>Strike 1 (Operational Breach):</strong> If an NGO misses their cause SLA without filing an extension, or submits rejected evidence, they receive Strike 1. The campaign is 100% refunded to donors. The NGO is frozen from creating new campaigns for 60 days.</li>
          <li><strong>Strike 2 (Permanent Termination):</strong> If an NGO breaches an SLA a second time, they receive Strike 2. Their account is permanently deactivated, legal notices are dispatched for recovery of unverified funds, and their Darpan ID is published to the public NGO Blacklist.</li>
        </ul>""", """        <h2>35.2 The 12-Step NGO Default & Replacement Delivery Workflow</h2>
        <p>When an NGO defaults or breaches its SLA, ACTA executes an auditable 12-step delivery-continuity workflow:</p>
        <div class="wireframe">
[1. FREEZE DISBURSEMENT] ──► [2. AUDIT SPENT / UNSPENT] ──► [3. DONOR TRANSPARENCY NOTICE]
                                                                        │
[6. SECURE EVIDENCE] ◄── [5. ASSIGN REPLACEMENT NGO] ◄── [4. FEASIBILITY EVALUATION]
         │
         ▼
[7. DELIVER AID] ──► [8. WEBRTC VIDEO PROOF] ──► [9. COMPLIANCE AUDIT] ──► [10. DISBURSE TO REPLACEMENT]
                                                                                        │
                                                                                        ▼
                                                                  [11. DONOR COMPLETION UPDATE]
                                                                  [12. NGO RISK REGISTER STRIKE]
        </div>
        <p><strong>Standard Donor Communication:</strong> Donors receive empathetic, factual alerts (7 standard templates) explaining delays, replacement assignment, or refunds without unverified accusations.</p>""")

    # 8. Chapter 39 Database Schemas Upgrade (Page 43) - Add continuity_reserve_ledger
    if "39. Technical Architecture & Database DDL" in p:
        p = p.replace("""CREATE TABLE escrow_batches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cause_id UUID REFERENCES causes(id),
  ngo_id UUID REFERENCES ngos(id),
  target_amount NUMERIC(10,2) NOT NULL,
  pooled_amount NUMERIC(10,2) DEFAULT 0.00,
  direct_cause_90 NUMERIC(10,2) NOT NULL,
  ngo_ops_10 NUMERIC(10,2) NOT NULL,
  platform_fee_5 NUMERIC(10,2) NOT NULL,
  status VARCHAR(30) DEFAULT 'POOLING',
  created_at TIMESTAMPTZ DEFAULT NOW()
);""", """CREATE TABLE escrow_batches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cause_id UUID REFERENCES causes(id),
  ngo_id UUID REFERENCES ngos(id),
  target_amount NUMERIC(10,2) NOT NULL,
  pooled_amount NUMERIC(10,2) DEFAULT 0.00,
  acta_fee_5 NUMERIC(10,2) NOT NULL,
  ngo_gross_95 NUMERIC(10,2) NOT NULL,
  ngo_ops_permitted NUMERIC(10,2) DEFAULT 0.00,
  direct_cause_supplies NUMERIC(10,2) NOT NULL,
  status VARCHAR(30) DEFAULT 'POOLING',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE continuity_reserve_ledger (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_donation_id UUID REFERENCES donations(id),
  reserve_contribution NUMERIC(10,2) NOT NULL,
  reserve_balance_after NUMERIC(10,2) NOT NULL,
  emergency_replacement_id UUID,
  created_at TIMESTAMPTZ DEFAULT NOW()
);""")

    # 9. Ensure Zero Free Fire Mentions
    p = p.replace("Free Fire", "Collegiate Gaming & Clan")
    p = p.replace("free fire", "collegiate gaming")

    upgraded_pages.append(p)

print(f"Upgraded {len(upgraded_pages)} pages successfully.")

# Reassemble HTML
full_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — Master Product Requirements Document (PRD v2.6 Revised) & SSOT</title>
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
  .pill-item.amber { background: #FFFBEB; color: #92400E; border-color: #FDE68A; }
  .meta-table-box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .meta-col h6 { font-size: 6.8pt; text-transform: uppercase; color: #64748B; letter-spacing: 1px; margin-bottom: 2px; }
  .meta-col p { font-size: 8.5pt; font-weight: 600; color: #0F172A; }
  h1 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13.5pt; font-weight: 800; color: #0F172A; letter-spacing: -0.4px; margin-top: 6px; margin-bottom: 4px; padding-bottom: 2px; border-bottom: 1px solid #E2E8F0; }
  h2 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9.8pt; font-weight: 700; color: #0F172A; margin-top: 6px; margin-bottom: 3px; }
  p { margin-bottom: 4px; color: #334155; line-height: 1.38; }
  ul, ol { margin-left: 14px; margin-bottom: 4px; color: #334155; }
  li { margin-bottom: 2px; }
  strong { color: #0F172A; font-weight: 600; }
  .card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 5px; padding: 8px 10px; margin-bottom: 6px; font-size: 8.2pt; }
  .card-highlight, .card-emerald { background: #F0FDF4; border-left: 3.5px solid #059669; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #059669; }
  .card-blue { background: #F8FAFC; border-left: 3.5px solid #2563EB; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #2563EB; }
  .card-amber { background: #FFFBEB; border-left: 3.5px solid #D97706; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #D97706; }
  .card-rose { background: #FFF1F2; border-left: 3.5px solid #E11D48; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #E11D48; }
  .card-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 8.8pt; color: #0F172A; margin-bottom: 2px; }
  table { width: 100%; border-collapse: collapse; margin: 6px 0 6px 0; font-size: 7.5pt; line-height: 1.28; }
  th { background: #0F172A; color: #FFFFFF; text-align: left; padding: 5px 6px; font-weight: 600; font-size: 7.2pt; letter-spacing: 0.5px; }
  td { padding: 4px 6px; border-bottom: 1px solid #E2E8F0; color: #334155; vertical-align: top; }
  tr:nth-child(even) td { background: #F8FAFC; }
  .wireframe, .code-block { background: #0F172A; color: #F8FAFC; padding: 7px 9px; border-radius: 5px; font-family: 'Courier New', Courier, monospace; font-size: 6.8pt; line-height: 1.25; margin: 5px 0; white-space: pre; overflow-x: hidden; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-bottom: 6px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; margin-bottom: 6px; }
  .stat-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 5px; padding: 6px; text-align: center; }
  .stat-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13pt; font-weight: 800; color: #059669; }
  .stat-lbl { font-size: 6.8pt; text-transform: uppercase; letter-spacing: 0.5px; color: #64748B; font-weight: 600; }
</style>
</head>
<body>
""" + "\n".join(upgraded_pages) + """
</body>
</html>
"""

# Write HTML file
with open(html_target, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Upgraded HTML written to {html_target}")

# Compile PDF using Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target}",
    f"file:///{html_target.replace(os.sep, '/')}"
]

print("Compiling ACTA_PRD_v2.6_REVISED.pdf via Microsoft Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_target):
    reader = pypdf.PdfReader(pdf_target)
    page_count = len(reader.pages)
    print(f"SUCCESS: ACTA_PRD_v2.6_REVISED.pdf compiled successfully! ({page_count} Pages, {os.path.getsize(pdf_target)} bytes)")
    # Copy to downloads
    shutil.copy2(pdf_target, os.path.join(downloads_dir, "ACTA_PRD_v2.6_REVISED.pdf"))
    print(f"Copied to {os.path.join(downloads_dir, 'ACTA_PRD_v2.6_REVISED.pdf')}")
else:
    print(f"Error creating PDF: {result.stderr}")

# Copy DOCX to downloads as well
if os.path.exists(docx_target):
    shutil.copy2(docx_target, os.path.join(downloads_dir, "ACTA_PRD_v2.6_REVISED.docx"))
    print(f"Copied to {os.path.join(downloads_dir, 'ACTA_PRD_v2.6_REVISED.docx')}")

print("Master PRD v2.6 Revised Build Completed!")
