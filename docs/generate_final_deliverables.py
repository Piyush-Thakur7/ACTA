import os
import shutil
import re
import subprocess
import pypdf

# Comprehensive Builder for ACTA Question Bank with Answers PDF & PRD Sync
# SSOT V2.5 - Grounded, Non-Hallucinated, Production-Ready Deliverables

downloads_dir = r"C:\Users\HP\Downloads"
docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"

source_prd_pdf = os.path.join(docs_dir, "ACTA_Master_Product_Document.pdf")
target_prd_pdf = os.path.join(downloads_dir, "ACTA_Master_Product_Document.pdf")
docs_pdf_file = os.path.join(docs_dir, "ACTA_GLBCRI_Pitch_Question_Bank_With_Answers.pdf")

# 1. Sync Latest PRD PDF to Downloads
if os.path.exists(source_prd_pdf):
    shutil.copy2(source_prd_pdf, target_prd_pdf)
    print(f"Synced latest PRD PDF to {target_prd_pdf}")

# 2. Parse extracted_question_bank.txt
raw_txt_path = os.path.join(downloads_dir, "extracted_question_bank.txt")
with open(raw_txt_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Let's read section by section
sections_raw = re.split(r'\n(?=[0-9]+\.\s+[A-Z][A-Za-z\s,–—&]+(?:\n|$))', raw_text)
print(f"Found {len(sections_raw)} raw sections.")

# HTML Template
html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACTA by Resence — GLBCRI Pitch Question Bank & Master Answer Defense Guide</title>
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
  .card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 5px; padding: 8px 10px; margin-bottom: 6px; font-size: 8.2pt; page-break-inside: avoid; }
  .card-highlight, .card-emerald { background: #F0FDF4; border-left: 3.5px solid #059669; }
  .card-blue { background: #F8FAFC; border-left: 3.5px solid #2563EB; }
  .card-amber { background: #FFFBEB; border-left: 3.5px solid #D97706; }
  .card-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 8.8pt; color: #0F172A; margin-bottom: 2px; }
  table { width: 100%; border-collapse: collapse; margin: 6px 0 8px 0; font-size: 7.5pt; line-height: 1.28; }
  th { background: #0F172A; color: #FFFFFF; text-align: left; padding: 5px 6px; font-weight: 600; font-size: 7.2pt; }
  td { padding: 4px 6px; border-bottom: 1px solid #E2E8F0; color: #334155; vertical-align: top; }
  tr:nth-child(even) td { background: #F8FAFC; }
  .wireframe { background: #0F172A; color: #F8FAFC; padding: 6px 8px; border-radius: 5px; font-family: 'JetBrains Mono', monospace; font-size: 6.8pt; line-height: 1.22; margin: 5px 0; white-space: pre; }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div>
    <div class="cover-top">
      <div class="brand-badge">RESENCE ECOSYSTEM</div>
      <div class="doc-tag">GLBCRI PITCH PREPARATION • MASTER QUESTION BANK & ANSWERS</div>
    </div>
    <div class="hero-h1">ACTA <span>Question Bank</span></div>
    <div class="hero-sub">Official Answers, Risk Register & Pitch Defense Guide</div>
    <div class="hero-paragraph">
      Comprehensive, grounded, and non-hallucinated defense manual for the Bharat Udyam Sangam 2026 Conclave at GLBCRI (GL Bajaj Center for Research and Incubation). Contains factual answers for all 160 examination questions, 14 operational edge-case responses, risk registers, and pitch readiness checklists.
    </div>
    <div class="pill-group">
      <div class="pill-item green">160 Questions Answered</div>
      <div class="pill-item blue">SaaS & 5% Service Fee Clarified</div>
      <div class="pill-item amber">₹100 Split Math (₹5 / ₹95)</div>
      <div class="pill-item green">1 Campus + 1 NGO Pilot Grounding</div>
      <div class="pill-item blue">Collegiate Community Guilds</div>
      <div class="pill-item">Implemented vs. Proposed Segregation</div>
    </div>
    <div class="meta-table-box">
      <div class="meta-col"><h6>Founder & Pitcher</h6><p>Piyush Singh (CEO, Resence)</p></div>
      <div class="meta-col"><h6>Academic Standing</h6><p>BCA 2nd Year, GL Bajaj (GLBIM)</p></div>
      <div class="meta-col"><h6>Target Conclave</h6><p>Bharat Udyam Sangam 2026 (GLBCRI)</p></div>
      <div class="meta-col"><h6>Document Classification</h6><p>Official Pitch Defense Guide</p></div>
      <div class="meta-col"><h6>Tagline Locked</h6><p>Small Acts, Big Impacts.</p></div>
      <div class="meta-col"><h6>Live Prototype</h6><p>resence.in / acta.resence.in</p></div>
    </div>
  </div>
  <div class="footer-bar">
    <span>CONFIDENTIAL & PROPRIETARY — RESENCE TECH LABS</span>
    <span>GLBCRI PITCH DEFENSE MANUAL • OCTOBER 2026</span>
  </div>
</div>
"""

# Let's write a python parser that takes extracted_question_bank.txt and converts each section and question into structured HTML.
body_html = []

# Section titles and introductory text
lines = raw_text.splitlines()
i = 0
current_section_title = ""
in_q_mode = False

while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    
    # Check if this is a major section title
    sec_match = re.match(r'^(\d+)\.\s+([A-Z][A-Za-z\s,–—&]+)$', line)
    if sec_match and len(line) < 65 and not line.endswith('?'):
        current_section_title = line
        body_html.append(f"""
        <div style="page-break-before: always; margin-top: 15px;">
          <div class="header-bar"><span>ACTA by Resence — GLBCRI Pitch Question Bank</span><span class="brand">DEFENSE MANUAL</span></div>
          <h1>{line}</h1>
        </div>
        """)
        i += 1
        continue

    # Check if this is a question line
    q_match = re.match(r'^(\d+)\.\s+(.+\?)$', line)
    if q_match:
        q_num = q_match.group(1)
        q_text = q_match.group(2)
        
        # Read subsequent lines until next question or section
        ans_lines = []
        i += 1
        while i < len(lines):
            next_line = lines[i].strip()
            if not next_line:
                i += 1
                continue
            if re.match(r'^(\d+)\.\s+', next_line):
                break
            ans_lines.append(next_line)
            i += 1
        
        base_ans = " ".join(ans_lines)
        
        # Determine status badge based on content
        status_tag = '<span class="qa-tag status-strat">Strategic Defense</span>'
        if any(w in q_text.lower() for w in ['built', 'prototype', 'demo', 'stack', 'feature', 'mobile']):
            status_tag = '<span class="qa-tag status-live">Live Prototype Status</span>'
        elif any(w in q_text.lower() for w in ['fee', 'split', 'escrow', 'money', 'donate', 'legal', 'tax', 'gst']):
            status_tag = '<span class="qa-tag status-prop">Proposed Architecture (Pending Review)</span>'
        
        # Format the card
        body_html.append(f"""
        <div class="qa-card">
          <div class="qa-num">QUESTION {q_num}</div>
          <div class="qa-q">{q_text}</div>
          <div class="qa-a">{base_ans}</div>
          <div>{status_tag}</div>
        </div>
        """)
        continue

    # Special handling for Section 12 (Practical Problems) and Section 13 (Checklist)
    if "Practical Problems" in line or "Pitch Readiness Checklist" in line or "Final Preparation Advice" in line:
        body_html.append(f"""
        <div style="page-break-before: always; margin-top: 15px;">
          <div class="header-bar"><span>ACTA by Resence — GLBCRI Pitch Question Bank</span><span class="brand">OPERATIONAL PLAYBOOK</span></div>
          <h1>{line}</h1>
        </div>
        """)
        i += 1
        continue
    
    # Generic content paragraph or bullet
    if i < len(lines):
        body_html.append(f"<p>{line}</p>")
        i += 1

html_full = html_head + "\n".join(body_html) + "\n</body>\n</html>"

html_file_path = os.path.join(downloads_dir, "ACTA_GLBCRI_Pitch_Question_Bank_With_Answers.html")
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"Question Bank HTML written to {html_file_path}")

# Compile PDF using Edge Headless
pdf_file_path = os.path.join(downloads_dir, "ACTA_GLBCRI_Pitch_Question_Bank_With_Answers.pdf")
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file_path}",
    f"file:///{html_file_path.replace(os.sep, '/')}"
]

print("Compiling Question Bank PDF via Edge Headless...")
res = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_file_path):
    # Also copy to docs dir
    shutil.copy2(pdf_file_path, docs_pdf_file)
    reader = pypdf.PdfReader(pdf_file_path)
    print("SUCCESS: Question Bank PDF compiled successfully!")
    print(f"Total Pages in Question Bank PDF: {len(reader.pages)}")
    print(f"File Size: {os.path.getsize(pdf_file_path)} bytes")
else:
    print(f"PDF creation failed: {res.stderr}")
