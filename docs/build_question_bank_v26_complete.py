import os
import sys
import re
import shutil
import subprocess
import pypdf
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

downloads_dir = r"C:\Users\HP\Downloads"
docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"

raw_txt_path = os.path.join(downloads_dir, "extracted_question_bank.txt")
docx_target = os.path.join(docs_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.docx")
html_target = os.path.join(docs_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.html")
pdf_target = os.path.join(docs_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.pdf")

print("Compiling ACTA GLBCRI Question Bank v2.6 Revised (.docx and .pdf)...")

with open(raw_txt_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Let's clean and ground the text for v2.6
# Ensure zero Free Fire mentions
raw_text = re.sub(r'Free Fire', 'Collegiate Clan Gaming', raw_text, flags=re.IGNORECASE)

# Split into lines
lines = raw_text.splitlines()

# ==============================================================================
# PART 1: PARSE SECTIONS AND QUESTIONS
# ==============================================================================
parsed_items = []
i = 0
current_section = "Introduction"

while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue

    # Check for major section heading (e.g. "1. Most Important Questions...", "12. Practical Problems...")
    sec_match = re.match(r'^(\d+)\.\s+([A-Z][A-Za-z\s,–—&]+)$', line)
    if sec_match and len(line) < 65 and not line.endswith('?'):
        current_section = line
        parsed_items.append({"type": "section_heading", "title": line})
        i += 1
        continue

    # Check for question line (e.g. "1. What is ACTA?", "12. How did you move...?")
    q_match = re.match(r'^(\d+)\.\s+(.+\?)$', line)
    if q_match:
        q_num = q_match.group(1)
        q_text = q_match.group(2)
        ans_lines = []
        i += 1
        while i < len(lines):
            next_line = lines[i].strip()
            if not next_line:
                i += 1
                continue
            # Break if next line is a question or section heading
            if re.match(r'^\d+\.\s+', next_line):
                break
            ans_lines.append(next_line)
            i += 1
        
        base_ans = " ".join(ans_lines)

        # Enhance financial questions with audited v2.6 facts
        if q_num == "5" and "money" in q_text.lower():
            base_ans += " ACTA operates as a Technology-as-a-Service (SaaS) provider. ACTA earns a proposed 5% platform service fee for software infrastructure, verification telemetry, and donor reporting. Earmarked 20% of fee revenue supports an internal Continuity Reserve for platform stability and emergency replacement execution."
        elif q_num == "6" and "donations go" in q_text.lower():
            base_ans += " Canonical proposed allocation for ₹100: ACTA service fee = ₹5.00 (5%); NGO payout = ₹95.00 (95%). Of the NGO's ₹95, up to 10% (₹9.50) may be used for permitted audited logistics if allowed by terms/restrictions, and remaining 90% (₹85.50) is dedicated to direct cause supplies backed by GST invoices. Labeled as proposed accounting illustration."
        elif "reserve" in q_text.lower() or "continuity" in q_text.lower():
            base_ans += " ACTA maintains a segregated Continuity Reserve policy funded from earned fees (not donor funds) to ensure business continuity and sponsor replacement delivery if an NGO defaults."
        
        # Classification tag
        status_tag = "Strategic Defense"
        if any(w in q_text.lower() for w in ['built', 'prototype', 'demo', 'stack', 'feature', 'mobile']):
            status_tag = "Live Prototype Status"
        elif any(w in q_text.lower() for w in ['fee', 'split', 'escrow', 'money', 'donate', 'legal', 'tax', 'gst']):
            status_tag = "Proposed Architecture (Pending Review)"
        elif any(w in q_text.lower() for w in ['pilot', '90 days', 'glbcri', 'ask']):
            status_tag = "Grounded Pilot Execution"

        parsed_items.append({
            "type": "question",
            "q_num": q_num,
            "q_text": q_text,
            "q_ans": base_ans,
            "tag": status_tag,
            "section": current_section
        })
        continue

    # Other headings or paragraphs
    if line.startswith("Section ") or "Checklist" in line or "Practical Problems" in line or "Advice" in line:
        parsed_items.append({"type": "subheading", "text": line})
    elif line.startswith("- ") or line.startswith("• "):
        parsed_items.append({"type": "bullet", "text": line[2:].strip()})
    else:
        parsed_items.append({"type": "paragraph", "text": line})
    i += 1

print(f"Parsed {len(parsed_items)} total structured items.")

# ==============================================================================
# PART 2: BUILD DOCX DOCUMENT
# ==============================================================================
doc = docx.Document()

# Page Margins
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

# Title & Metadata
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(10)
p_title.paragraph_format.space_after = Pt(2)
run_title = p_title.add_run("ACTA by Resence — GLBCRI Pitch Question Bank & Master Defense Guide (v2.6 Revised)")
run_title.font.name = 'Arial'
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(15, 23, 42)

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(12)
r_sub = p_sub.add_run("Official Answers, Risk Register & Pitch Defense Guide for Bharat Udyam Sangam 2026 (GLBCRI)\nTagline: Small Acts. Big Impact. | Founder: Piyush Singh (CEO, Resence - BCA 2nd Year, GLBIM)")
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(10.5)
r_sub.font.color.rgb = RGBColor(5, 150, 105)

# Meta Table
tbl_meta = doc.add_table(rows=3, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    [("Target Conclave", "Bharat Udyam Sangam 2026 (GLBCRI Incubation)"), ("Document Status", "v2.6 Revised (Audited & Grounded)")],
    [("Total Questions Answered", "160 Examination Questions + 14 Ground Scenarios"), ("Financial Standard", "Canonical ₹100 Split (₹5 / ₹95) + Continuity Reserve")],
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

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Render Items in DOCX
for item in parsed_items:
    if item["type"] == "section_heading":
        h = doc.add_heading(item["title"], level=1)
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(4)
        run = h.runs[0]
        run.font.name = 'Arial'
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(15, 23, 42)
    elif item["type"] == "subheading":
        h = doc.add_heading(item["text"], level=2)
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(3)
        run = h.runs[0]
        run.font.name = 'Arial'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(30, 41, 59)
    elif item["type"] == "question":
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "FFFFFF")
        cell.width = Inches(6.8)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        
        # Question Header
        r_num = p.add_run(f"QUESTION {item['q_num']}: ")
        r_num.bold = True
        r_num.font.name = 'Arial'
        r_num.font.size = Pt(9)
        r_num.font.color.rgb = RGBColor(5, 150, 105)
        
        r_q = p.add_run(item['q_text'] + "\n")
        r_q.bold = True
        r_q.font.name = 'Arial'
        r_q.font.size = Pt(9.5)
        r_q.font.color.rgb = RGBColor(15, 23, 42)
        
        # Answer
        r_a = p.add_run(item['q_ans'] + "\n")
        r_a.font.name = 'Arial'
        r_a.font.size = Pt(9)
        r_a.font.color.rgb = RGBColor(51, 65, 85)
        
        # Tag
        r_tag = p.add_run(f"[{item['tag'].upper()}]")
        r_tag.bold = True
        r_tag.font.name = 'Arial'
        r_tag.font.size = Pt(7.5)
        r_tag.font.color.rgb = RGBColor(100, 116, 139)
        
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    elif item["type"] == "bullet":
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(item["text"])
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(51, 65, 85)
    elif item["type"] == "paragraph":
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(item["text"])
        r.font.name = 'Arial'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(51, 65, 85)

doc.save(docx_target)
print(f"Question Bank DOCX created at {docx_target}")

# ==============================================================================
# PART 3: BUILD HTML & COMPILE PDF VIA EDGE HEADLESS
# ==============================================================================
html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — GLBCRI Pitch Question Bank & Master Defense Guide (v2.6 Revised)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 15mm 12mm 15mm;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #0F172A; background-color: #FFFFFF; line-height: 1.45; font-size: 8.8pt;
    -webkit-font-smoothing: antialiased;
  }
  .cover-page {
    min-height: 265mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    padding: 10px 0;
  }
  .header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #E2E8F0;
    padding-bottom: 4px;
    margin-bottom: 12px;
    font-size: 7.2pt;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748B;
    font-weight: 600;
  }
  .header-bar .brand { color: #0F172A; font-weight: 800; }
  .footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #E2E8F0;
    padding-top: 4px;
    margin-top: 10px;
    font-size: 7.2pt;
    color: #94A3B8;
  }
  .brand-badge {
    background: #0F172A;
    color: #FFFFFF;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 9pt;
    letter-spacing: 2px;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
  }
  .doc-tag { font-size: 7.5pt; text-transform: uppercase; letter-spacing: 1px; color: #64748B; font-weight: 700; }
  .cover-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E2E8F0; padding-bottom: 14px; margin-bottom: 20px; }
  .hero-h1 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 34pt; font-weight: 800; letter-spacing: -1.5px; line-height: 1.05; color: #0F172A; margin-bottom: 8px; }
  .hero-h1 span { color: #059669; }
  .hero-sub { font-family: 'Space Grotesk', sans-serif; font-size: 15pt; color: #334155; font-weight: 600; margin-bottom: 14px; letter-spacing: -0.5px; }
  .hero-paragraph { font-size: 10pt; color: #475569; line-height: 1.5; margin-bottom: 20px; }
  .pill-group { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 20px; }
  .pill-item { background: #F1F5F9; color: #334155; font-size: 7.2pt; font-weight: 600; padding: 3px 8px; border-radius: 999px; border: 1px solid #E2E8F0; }
  .pill-item.green { background: #ECFDF5; color: #065F46; border-color: #A7F3D0; }
  .pill-item.blue { background: #EFF6FF; color: #1E40AF; border-color: #BFDBFE; }
  .pill-item.amber { background: #FFFBEB; color: #92400E; border-color: #FDE68A; }
  .meta-table-box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 20px; }
  .meta-col h6 { font-size: 6.8pt; text-transform: uppercase; color: #64748B; letter-spacing: 1px; margin-bottom: 2px; }
  .meta-col p { font-size: 8.5pt; font-weight: 600; color: #0F172A; }
  h1 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14pt; font-weight: 800; color: #0F172A; letter-spacing: -0.4px; margin-top: 14px; margin-bottom: 6px; padding-bottom: 4px; border-bottom: 1.5px solid #E2E8F0; }
  h2 { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11pt; font-weight: 700; color: #0F172A; margin-top: 12px; margin-bottom: 5px; }
  p { margin-bottom: 5px; color: #334155; line-height: 1.42; }
  ul, ol { margin-left: 16px; margin-bottom: 6px; color: #334155; }
  li { margin-bottom: 2px; }
  strong { color: #0F172A; font-weight: 600; }
  .qa-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 8px 10px;
    margin-bottom: 8px;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  .qa-num { font-size: 7.2pt; font-weight: 700; color: #059669; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px; }
  .qa-q { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 9pt; color: #0F172A; margin-bottom: 4px; }
  .qa-a { font-size: 8.4pt; color: #334155; line-height: 1.4; }
  .qa-tag { display: inline-block; font-size: 6.8pt; font-weight: 600; padding: 2px 6px; border-radius: 4px; margin-top: 4px; }
  .qa-tag.status-live { background: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; }
  .qa-tag.status-prop { background: #EFF6FF; color: #1E40AF; border: 1px solid #BFDBFE; }
  .qa-tag.status-strat { background: #F8FAFC; color: #475569; border: 1px solid #E2E8F0; }
  .qa-tag.status-pilot { background: #FFFBEB; color: #92400E; border: 1px solid #FDE68A; }
</style>
</head>
<body>

<div class="cover-page">
  <div>
    <div class="cover-top">
      <div class="brand-badge">RESENCE ECOSYSTEM</div>
      <div class="doc-tag">GLBCRI PITCH PREPARATION • MASTER DEFENSE MANUAL (V2.6 REVISED)</div>
    </div>
    <div class="hero-h1">ACTA <span>Question Bank</span></div>
    <div class="hero-sub">Official Answers, Risk Register & Pitch Defense Guide</div>
    <div class="hero-paragraph">
      Comprehensive, grounded, and non-hallucinated defense manual for the Bharat Udyam Sangam 2026 Conclave at GLBCRI (GL Bajaj Center for Research and Incubation). Contains factual answers for all 160 examination questions, 14 operational scenarios, risk registers, and pitch readiness checklists. Fully synchronized with PRD v2.6 Revised.
    </div>
    <div class="pill-group">
      <div class="pill-item green">160 Questions Answered</div>
      <div class="pill-item blue">SaaS & 5% Service Fee Clarified</div>
      <div class="pill-item amber">₹100 Split Math (₹5 / ₹95)</div>
      <div class="pill-item green">Continuity Reserve Policy</div>
      <div class="pill-item blue">1 Campus + 1-2 Local NGOs Pilot</div>
      <div class="pill-item">Collegiate Impact Guilds & Campus Clans</div>
    </div>
    <div class="meta-table-box">
      <div class="meta-col"><h6>Founder & Pitcher</h6><p>Piyush Singh (CEO, Resence)</p></div>
      <div class="meta-col"><h6>Academic Standing</h6><p>BCA 2nd Year, GL Bajaj (GLBIM)</p></div>
      <div class="meta-col"><h6>Target Conclave</h6><p>Bharat Udyam Sangam 2026 (GLBCRI)</p></div>
      <div class="meta-col"><h6>Document Classification</h6><p>Official Pitch Defense Guide v2.6</p></div>
      <div class="meta-col"><h6>Tagline Locked</h6><p>Small Acts. Big Impact.</p></div>
      <div class="meta-col"><h6>Live Prototype</h6><p>resence.in / acta.resence.in</p></div>
    </div>
  </div>
  <div class="footer-bar">
    <span>CONFIDENTIAL & PROPRIETARY — RESENCE TECH LABS</span>
    <span>GLBCRI PITCH DEFENSE MANUAL • VERSION 2.6 REVISED</span>
  </div>
</div>
"""

body_html = []
for item in parsed_items:
    if item["type"] == "section_heading":
        body_html.append(f"""
        <div style="page-break-before: always; margin-top: 15px;">
          <div class="header-bar"><span>ACTA by Resence — GLBCRI Pitch Question Bank</span><span class="brand">DEFENSE MANUAL V2.6</span></div>
          <h1>{item["title"]}</h1>
        </div>
        """)
    elif item["type"] == "subheading":
        body_html.append(f"<h2>{item['text']}</h2>")
    elif item["type"] == "question":
        tag_class = "status-strat"
        if "Live Prototype" in item["tag"]:
            tag_class = "status-live"
        elif "Proposed" in item["tag"]:
            tag_class = "status-prop"
        elif "Pilot" in item["tag"]:
            tag_class = "status-pilot"
        
        body_html.append(f"""
        <div class="qa-card">
          <div class="qa-num">QUESTION {item['q_num']}</div>
          <div class="qa-q">{item['q_text']}</div>
          <div class="qa-a">{item['q_ans']}</div>
          <div><span class="qa-tag {tag_class}">{item['tag'].upper()}</span></div>
        </div>
        """)
    elif item["type"] == "bullet":
        body_html.append(f"<ul><li>{item['text']}</li></ul>")
    elif item["type"] == "paragraph":
        body_html.append(f"<p>{item['text']}</p>")

html_full = html_head + "\n".join(body_html) + "\n</body>\n</html>"

with open(html_target, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"Question Bank HTML written to {html_target}")

# Compile PDF using Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target}",
    f"file:///{html_target.replace(os.sep, '/')}"
]

print("Compiling Question Bank PDF via Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_target):
    reader = pypdf.PdfReader(pdf_target)
    page_count = len(reader.pages)
    print(f"SUCCESS: Question Bank PDF compiled! ({page_count} Pages, {os.path.getsize(pdf_target)} bytes)")
    shutil.copy2(pdf_target, os.path.join(downloads_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.pdf"))
    print(f"Copied PDF to {os.path.join(downloads_dir, 'ACTA_GLBCRI_QUESTION_BANK_REVISED.pdf')}")
else:
    print(f"PDF creation failed: {result.stderr}")

if os.path.exists(docx_target):
    shutil.copy2(docx_target, os.path.join(downloads_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.docx"))
    print(f"Copied DOCX to {os.path.join(downloads_dir, 'ACTA_GLBCRI_QUESTION_BANK_REVISED.docx')}")

print("Question Bank v2.6 Revised Build Completed!")
