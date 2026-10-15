import os
import sys
import subprocess
import pypdf
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"
downloads_dir = r"C:\Users\HP\Downloads"

docx_path = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.docx")
html_path = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.html")
pdf_path = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.pdf")

print("Building ACTA Master PRD v2.6 Revised (.docx and .pdf)...")

# ==============================================================================
# PART 1: BUILD DOCX DOCUMENT
# ==============================================================================
doc = docx.Document()

# Page Margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Styling Helpers
def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def add_header(title, level=1):
    h = doc.add_heading(title, level=level)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    run = h.runs[0]
    run.font.name = 'Arial'
    if level == 1:
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(15, 23, 42)
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(30, 41, 59)
    else:
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(51, 65, 85)
    return h

def add_p(text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix + " ")
        r_bold.font.bold = True
        r_bold.font.name = 'Arial'
        r_bold.font.size = Pt(9.5)
        r_bold.font.color.rgb = RGBColor(15, 23, 42)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.italic = italic
    r.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix + " ")
        r_bold.font.bold = True
        r_bold.font.name = 'Arial'
        r_bold.font.size = Pt(9.5)
        r_bold.font.color.rgb = RGBColor(15, 23, 42)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_callout(text, title="KEY NOTE", bg_hex="F8FAFC", border_color="059669"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_hex)
    cell.width = Inches(6.8)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r_title = p.add_run(f"[{title}] ")
    r_title.bold = True
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(9)
    r_title.font.color.rgb = RGBColor(5, 150, 105)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

# Title & Metadata
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(10)
p_title.paragraph_format.space_after = Pt(2)
run_title = p_title.add_run("ACTA by Resence — Product Requirements Document (PRD v2.6 Revised)")
run_title.font.name = 'Arial'
run_title.font.size = Pt(20)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(15, 23, 42)

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(12)
r_sub = p_sub.add_run("Internal Product Bible & Technical Single Source of Truth (SSOT)\nTagline: Small Acts. Big Impact. | Parent: Resence (resence.in)")
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(11)
r_sub.font.color.rgb = RGBColor(5, 150, 105)

# Meta Box Table
tbl_meta = doc.add_table(rows=3, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    [("Founder & Architect", "Piyush Singh (CEO, Resence - BCA 2nd Year, GLBIM)"), ("Conclave", "Bharat Udyam Sangam 2026 (GLBCRI)")],
    [("Document Classification", "PRD v2.6 Revised (Implementation-Ready)"), ("Status", "Audited, Grounded, Zero 105% Error, Zero Free Fire")],
    [("Pilot Footprint", "1 Campus (GL Bajaj) + 1-2 Curated Local NGOs"), ("Live Prototype", "resence.in / acta.resence.in")]
]
for row_idx, row in enumerate(meta_data):
    for col_idx, (k, v) in enumerate(row):
        c = tbl_meta.cell(row_idx, col_idx)
        set_cell_background(c, "F1F5F9" if row_idx % 2 == 0 else "FFFFFF")
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r_k = p.add_run(k + ": ")
        r_k.bold = True
        r_k.font.size = Pt(8.5)
        r_v = p.add_run(v)
        r_v.font.size = Pt(8.5)

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# Section 1: Executive Summary & Historical Progression
add_header("1. Executive Summary & Authentic Founder Origin", level=1)
add_p("ACTA by Resence is a social-impact technology platform designed to transform societal challenges into evidence-driven, trackable collective action. The platform connects collegiate students, institutional campus communities (Impact Guilds), eligible verified non-profits (NGOs), and micro-donors.", "Core Mission:")
add_p("ACTA was not conceived overnight as a high-tech platform with AI and escrow systems. It began over 12 months ago with grassroots volunteer recruitment by founder Piyush Singh for animal feeding drives and slum relief around Greater Noida. Through firsthand field execution, the founder experienced severe structural roadblocks:", "Historical Progression:")
add_bullet("Volunteers faced coordination bottlenecks and safety liabilities during unsupervised fieldwork.", "Volunteer Fatigue:")
add_bullet("Student donors felt strong cynicism, with 67.5% reporting a trust deficit regarding whether funds reached real beneficiaries.", "Donor Cynicism:")
add_bullet("Traditional fundraising platforms imposed prohibitive minimum amounts (₹500–₹1,000), alienating college students with micro-budgets.", "Wealth Exclusion:")
add_p("Recognizing that volunteer coordination alone could not scale without structural accountability, the initiative evolved into a pure Technology-as-a-Service (SaaS) platform where technology guarantees transparency, micro-giving enables broad participation, and verified partner NGOs execute delivery on the ground.", "Platform Evolution:")

# Section 2: Product Status Classification Guide
add_header("2. Product Development Status Classification Guide", level=1)
add_p("To uphold uncompromising engineering and business integrity, all features, partnerships, and capabilities are strictly categorized into five factual states:", "Classification Standard:")
add_bullet("Mobile-first Web PWA (acta.resence.in), 3-Pillar Clean Dashboard, 7 Curated Cause Cards, simulated ₹10 UPI intent triggers, balanced action gamification formulas (XP rings), Student Impact Planner UI.", "1. Implemented & Tested (Prototype):")
add_bullet("Webhook listener with HMAC-SHA256 signature verification and Redis 24h event deduplication, WebRTC camera telemetry watermark, YouTube Data API v3 unlisted pipeline, Gemini Vision receipt OCR parser.", "2. Partially Implemented (Validation):")
add_bullet("Offline IndexedDB 2MB video chunking and Service Worker Background Sync API, automated MediaPipe Gaussian facial blur pipeline, City & National Leaderboard Redis Sorted Sets, 12-Step Default Workflow engine.", "3. Designed But Not Implemented (Specs):")
add_bullet("Automated 5%/95% split settlement via payment aggregators (Razorpay Route / Cashfree Split), dedicated Scheduled Commercial Bank Virtual Escrow/Nodal accounts, automated gateway refunds, formal NGO Master Service Agreements.", "4. Proposed & Awaiting External Approval:")
add_bullet("67.5% donor trust deficit in collegiate demographics (to be measured via GL Bajaj pilot), ₹10 repeat giving frequency (target: 35%+ monthly retention), inter-hostel guild viral loops.", "5. Hypotheses Awaiting Market Validation:")

# Section 3: Corrected Financial & Payment Allocation Architecture
add_header("3. Corrected Financial & Payment Allocation Architecture", level=1)
add_callout("The previous PRD phrasing of '90% direct cause + 10% NGO ops + 5% ACTA fee' produced a 105% mathematical contradiction. This error has been permanently excised. The canonical allocation model is defined below as a proposed accounting illustration.", "CRITICAL MATHEMATICAL CORRECTION", "FEF2F2", "DC2626")

add_p("For every gross donation of ₹100.00, the allocation is structured as follows:", "Canonical Allocation Specification:")
add_bullet("ACTA retains an agreed 5% commercial service fee for providing platform software, verification infrastructure, telemetry processing, and donor reporting.", "ACTA Proposed Service Fee: ₹5.00 (5%) —")
add_bullet("The full remaining balance is transferred directly to the verified partner NGO's account via an authorized payment aggregator settlement arrangement.", "Eligible Partner NGO Share: ₹95.00 (95%) —")
add_bullet("The partner NGO may allocate up to 10% of its received ₹95.00 for permitted, audited logistics (e.g. tempo fuel, packing bags) only if the campaign terms, donor restrictions, and NGO legal obligations permit it.", "Permitted NGO Operations: ₹9.50 (10% of NGO Share) —")
add_bullet("The full remaining balance must be spent directly on verified campaign supplies (e.g. grains, notebooks, saplings) backed by itemized vendor GST invoices.", "Direct Campaign Purpose: ₹85.50 (90% of NGO Share) —")

add_p("Gross Contribution (₹100.00) = ACTA Service Fee (₹5.00) + Permitted NGO Operations (₹9.50) + Direct Campaign Supplies (₹85.50) = ₹100.00 (Exactly 100%).", "Mathematical Verification:")
add_p("ACTA earns revenue strictly as Technology-as-a-Service (SaaS). ACTA does not operate as a donation-holding trust, bank, or payment aggregator. Payment processing is conducted via domestic Indian UPI (0% Merchant Discount Rate), RuPay, and domestic net banking. Foreign transactions are strictly prohibited under FCRA controls.", "Regulatory Clarification:")

# Section 4: Revenue & Continuity Reserve Policy
add_header("4. Platform Revenue & Internal Continuity Reserve Policy", level=1)
add_p("ACTA does not expend all earned platform service fees immediately. To guarantee platform stability and protect beneficiaries in case of partner default, ACTA establishes an internal Continuity Reserve Policy:", "Reserve Governance:")
add_bullet("Service fee revenue (₹5 per ₹100) is booked into ACTA's corporate operating accounts, completely segregated from donor payment flows and NGO settlement accounts.", "1. Segregated Accounting:")
add_bullet("Resence management earmarks a recommended 20% of earned platform fees (e.g., ₹1.00 out of ₹5.00 earned) to build an internal business continuity reserve.", "2. Reserve Allocation:")
add_bullet("In the rare event that a partner NGO defaults after receiving mobilization funds, ACTA may, subject to board approval and available reserve balances, utilize continuity reserve funds to sponsor a verified substitute NGO to complete the aid delivery.", "3. Emergency Replacement Funding:")
add_bullet("Restricted donor contributions, third-party NGO settlements, or escrow balances are strictly prohibited from being used as reserve capital. No open-ended platform guarantees are made beyond approved reserve funds.", "4. Strict Statutory Guardrail:")

# Section 5: NGO Default Management & 12-Step Replacement Workflow
add_header("5. NGO Default Management & 12-Step Replacement Workflow", level=1)
add_p("ACTA enforces category-specific SLAs and a structured failure escalation matrix:", "Operational Governance:")
add_bullet("Food distribution: 96 hours | School kits: 7–10 days | Tree plantation: 10 days | Emergency medical: 24–48 hours.", "Dynamic SLAs by Category:")
add_bullet("Categorized into Category A (Logistical delay: in-app extension), Category B (Insufficient evidence: 48h cure notice), Category C (Operational negligence: Warning 1 + substitute lead), Category D (Contractual breach: Default review & replacement), and Category E (Suspected fraud: Emergency freeze & legal referral).", "5 Failure Tiers:")
add_p("The 12-Step Replacement Workflow executes as follows: (1) Freeze further disbursement, (2) Audit spent vs unspent balances, (3) Dispatch transparent donor notice, (4) Evaluate replacement feasibility, (5) Assign replacement NGO from the 1 Lead + 2 Substitutes roster, (6) Secure itemized procurement evidence, (7) Execute on-ground delivery, (8) Upload WebRTC video proof, (9) Compliance desk dual-signoff audit, (10) Disburse remaining funds to substitute, (11) Dispatch completion notification to donors, and (12) Record permanent penalty in the NGO risk register.", "12-Step Replacement Protocol:")

# Section 6: Standard Donor Communication Templates
add_header("6. Standard Donor Communication & Transparency Policy", level=1)
add_p("ACTA establishes 7 empathy-first, truthful communication templates: (1) Delivery Delayed (weather/logistics), (2) Warning Issued to Partner NGO (audit review), (3) NGO Unresponsive (formal escalation), (4) Replacement NGO Selected, (5) Replacement Delivery Completed, (6) Campaign Cancelled & Refund Initiated, and (7) Suspected Misuse Under Review. Communication strictly prohibits unverified accusations, conceals no operational delays, and protects beneficiary dignity under the DPDP Act 2023.", "Customer Experience Standards:")

# Section 7: 10-Point Legal, Regulatory & Fintech Review Checklist
add_header("7. 10-Point Legal, Regulatory & Fintech Review Checklist", level=1)
add_p("Prior to commercial deployment, this 10-point checklist governs legal and financial compliance:", "Governance Gateway:")
add_bullet("Operate as a SaaS technology provider under Section 79 of the IT Act 2000, not a donation-holding entity.", "1. SaaS Intermediary Status:")
add_bullet("Validate Razorpay Route / Cashfree Split automated settlement for non-profit and commercial splits.", "2. RBI PA Split Permissibility:")
add_bullet("Section 80G receipts issued strictly by partner NGOs; Form 10BD data extraction pipeline.", "3. Section 80G Tax Deductions:")
add_bullet("18% GST applicability on ACTA's ₹5 service fee; SAC code classification and B2B invoicing.", "4. GST on Technology Fees:")
add_bullet("Compliance of escrow/nodal custody and milestone disbursement under RBI Master Directions.", "5. Escrow Nodal Custody:")
add_bullet("Enforceability of 5% fee, 10% ops cap, dynamic SLAs, and 2-strike default replacement clause.", "6. NGO Master Service Agreement:")
add_bullet("Dispute liability, rolling reserve buffers, and chargeback recovery protocols.", "7. Chargeback & Dispute Liability:")
add_bullet("Balance sheet classification of Continuity Reserve under ICAI AS 29 / Ind AS 37.", "8. Continuity Reserve Governance:")
add_bullet("MediaPipe automated minor facial blur pipeline (<18 years) and beneficiary consent under DPDP Act 2023.", "9. DPDP Act & Minor Privacy:")
add_bullet("Domestic INR transactions only; programmatic blocking of international cards and accounts under FCRA.", "10. FCRA Ring-Fencing:")

# Section 8: Technical Architecture & System Specifications
add_header("8. Technical Architecture & Database Specifications", level=1)
add_p("The system is engineered on a modern cloud stack: React 18 Mobile-First PWA, Node.js 22 REST/Webhook API, Supabase PostgreSQL, Redis event cache, WebRTC camera pipeline, MediaPipe face blur, and YouTube Data API v3 unlisted archive.", "Tech Stack Overview:")

add_p("Complete database schema definitions with relational integrity and audit logging:", "Database Schema Architecture:")
add_bullet("Stores authentication credentials, phone numbers, role (donor, ngo_lead, reviewer, admin), and privacy settings.", "users Table:")
add_bullet("Stores title, category, target_amount, raised_amount, status, ngo_id, execution_sla_hours, and deadline.", "campaigns Table:")
add_bullet("Stores donation_id, campaign_id, user_id, gross_amount, acta_fee (5%), ngo_net (95%), payment_status, and gateway_ref.", "donations Table:")
add_bullet("Tracks milestone escrow state, mobilization advance, proof submission timestamps, and dual-authorization signoffs.", "escrow_batches Table:")
add_bullet("Stores WebRTC video hashes, GPS coordinates, NTP timestamps, YouTube unlisted video URL, and OCR invoice logs.", "verifications Table:")
add_bullet("Ledger tracking 20% continuity reserve allocations from earned platform fees and emergency replacement disbursements.", "continuity_reserve_ledger Table:")
add_bullet("Manages campus collegiate communities, hostel blocks, and aggregated collective impact scores.", "guilds Table:")

# Section 9: Gamification & Collegiate Impact Guilds
add_header("9. Gamification & Collegiate Impact Guilds", level=1)
add_p("ACTA rejects pay-to-win dynamics. Donations are strictly private, eliminating wealth shaming. XP is awarded based on positive social actions: +20 XP for verifying ground proof, +150 XP for weekly giving streaks, and +250 XP for campus volunteering.", "Ethical Gamification Engine:")
add_p("Collegiate students organize into Campus Impact Guilds (e.g. GLBIM Tech Warriors, Hostel Block A Impact Guild). Guilds compete on aggregate participation and collective impact, unlocking campus-wide tree planting or digital achievement badges. All gaming references are strictly collegiate; zero third-party game branding is utilized.", "Campus Guild Architecture:")

# Section 10: Pilot Roadmap & GLBCRI Incubation Objectives
add_header("10. Pilot Roadmap & GLBCRI Incubation Objectives", level=1)
add_p("The operational launch focuses on a tightly controlled, high-fidelity pilot:", "Pilot Scope:")
add_bullet("GL Bajaj Institute of Management (GLBIM), Greater Noida (500–1,000 active student micro-donors).", "Pilot Campus:")
add_bullet("1–2 verified local grassroots non-profits operating in Greater Noida (Zero Hunger / Stray Feeding).", "Pilot NGO Partners:")
add_bullet("Month 1: Legal/fintech sign-off. Month 2: Webhook and camera hardening. Month 3: Live ₹10,000 pilot campaign with full video proof delivery and donor satisfaction audit.", "90-Day Execution Plan:")
add_p("Piyush Singh respectfully requests incubation support from GLBCRI (Bharat Udyam Sangam 2026): (1) Incubation desk and campus pilot facilitation, (2) Legal and fintech mentorship clinic, (3) Cloud server infrastructure credits, and (4) Institutional introduction to CSR corporate partners.", "GLBCRI Incubation Ask:")

# Save DOCX
doc.save(docx_path)
print(f"DOCX created successfully at {docx_path}")
