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

docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"
downloads_dir = r"C:\Users\HP\Downloads"

pdf_name = "ACTA PRD.pdf"
docx_name = "ACTA PRD.docx"
html_name = "ACTA PRD.html"

pdf_target_docs = os.path.join(docs_dir, pdf_name)
docx_target_docs = os.path.join(docs_dir, docx_name)
html_target_docs = os.path.join(docs_dir, html_name)

pdf_target_dl = os.path.join(downloads_dir, pdf_name)
docx_target_dl = os.path.join(downloads_dir, docx_name)

print("Building ACTA PRD PDF and DOCX (Full-Page Coverage Guaranteed)...")

# Load existing upgraded HTML from ACTA_PRD_v2.6_REVISED.html
html_src_path = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.html")
with open(html_src_path, "r", encoding="utf-8") as f:
    html_src = f.read()

# We need to transform the CSS and structure from artificial 270mm fixed boxes to continuous full-page flow!
# Let's inspect the CSS in html_src
# Replace the CSS in html_src to enable continuous full-page coverage
old_style_marker = "<style>"
new_css = """<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #111827; background-color: #FFFFFF; line-height: 1.40; font-size: 8.7pt;
    -webkit-font-smoothing: antialiased;
  }
  .cover-page { 
    min-height: 265mm;
    display: flex; flex-direction: column; justify-content: space-between; 
    padding: 10px 5px; page-break-after: always; break-after: page; 
  }
  .header-bar { display: none; }
  .footer-bar { display: none; }
  .page { 
    margin-bottom: 12px;
    page-break-after: auto;
    break-after: auto;
  }
  .page > div {
    display: block;
  }
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
  h1 { 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: 13.5pt; font-weight: 800; color: #0F172A; 
    letter-spacing: -0.4px; margin-top: 14px; margin-bottom: 5px; 
    padding-bottom: 3px; border-bottom: 1.5px solid #E2E8F0; 
    page-break-after: avoid; break-after: avoid; 
  }
  h2 { 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: 10.2pt; font-weight: 700; color: #0F172A; 
    margin-top: 10px; margin-bottom: 4px; 
    page-break-after: avoid; break-after: avoid; 
  }
  p { margin-bottom: 4px; color: #334155; line-height: 1.40; }
  ul, ol { margin-left: 14px; margin-bottom: 4px; color: #334155; }
  li { margin-bottom: 2px; }
  strong { color: #0F172A; font-weight: 600; }
  .card { 
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 5px; 
    padding: 7px 10px; margin-bottom: 6px; font-size: 8.3pt; 
    page-break-inside: avoid; break-inside: avoid; 
  }
  .card-highlight, .card-emerald { background: #F0FDF4; border-left: 3.5px solid #059669; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #059669; }
  .card-blue { background: #F8FAFC; border-left: 3.5px solid #2563EB; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #2563EB; }
  .card-amber { background: #FFFBEB; border-left: 3.5px solid #D97706; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #D97706; }
  .card-rose { background: #FFF1F2; border-left: 3.5px solid #E11D48; border-color: #E2E8F0 #E2E8F0 #E2E8F0 #E11D48; }
  .card-title { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 8.8pt; color: #0F172A; margin-bottom: 2px; }
  table { 
    width: 100%; border-collapse: collapse; margin: 6px 0 6px 0; 
    font-size: 7.6pt; line-height: 1.30; 
    page-break-inside: avoid; break-inside: avoid; 
  }
  th { background: #0F172A; color: #FFFFFF; text-align: left; padding: 5px 6px; font-weight: 600; font-size: 7.2pt; letter-spacing: 0.5px; }
  td { padding: 4px 6px; border-bottom: 1px solid #E2E8F0; color: #334155; vertical-align: top; }
  tr:nth-child(even) td { background: #F8FAFC; }
  .wireframe, .code-block { 
    background: #0F172A; color: #F8FAFC; padding: 7px 9px; 
    border-radius: 5px; font-family: 'Courier New', Courier, monospace; 
    font-size: 6.8pt; line-height: 1.25; margin: 5px 0; 
    white-space: pre; overflow-x: hidden; 
    page-break-inside: avoid; break-inside: avoid; 
  }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-bottom: 6px; page-break-inside: avoid; break-inside: avoid; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; margin-bottom: 6px; page-break-inside: avoid; break-inside: avoid; }
  .stat-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 5px; padding: 6px; text-align: center; }
  .stat-val { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13pt; font-weight: 800; color: #059669; }
  .stat-lbl { font-size: 6.8pt; text-transform: uppercase; letter-spacing: 0.5px; color: #64748B; font-weight: 600; }
</style>"""

# Replace the style block
style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
html_full_page = style_pattern.sub(new_css, html_src)

# Update Title in HTML
html_full_page = html_full_page.replace("<title>ACTA by Resence — Master Product Requirements Document (PRD v2.6 Revised) & SSOT</title>",
                                        "<title>ACTA PRD — Master Product Requirements Document (SSOT V2.6 Revised)</title>")

# Expand Appendix on the final page so it completely covers the page
appendix_expansion = """        <h2>B. Specific Asks from GLBCRI (Bharat Udyam Sangam 2026)</h2>
        <ol>
          <li><strong>Institutional Credibility & Letterhead:</strong> Introducing ACTA under GL Bajaj / GLBCRI official backing to 18–20 verified local NGOs.</li>
          <li><strong>Campus Pilot Authorization:</strong> Permission to run an official 30-day student micro-giving pilot across GL Bajaj Knowledge Park hostels.</li>
          <li><strong>Pre-Incubation Mentorship:</strong> Legal structuring for NGO MoUs, Section 8/Pvt Ltd formalization, and seed grant guidance.</li>
        </ol>
        <h2>C. Conclave Pitch Readiness Checklist (Bharat Udyam Sangam 2026)</h2>
        <div class="card card-blue">
          <p><strong>1. Problem Articulation:</strong> Clear defense of the 67.5% student trust deficit and traditional minimum ticket barrier.</p>
          <p><strong>2. Solution Mechanics:</strong> Live PWA demo, 0% MDR UPI intent flow, and transparent video proof archive.</p>
          <p><strong>3. Financial Model:</strong> Canonical ₹100 split (₹5 ACTA fee, ₹95 NGO payout, ₹9.50 permitted ops, ₹85.50 direct cause supplies) and internal Continuity Reserve governance.</p>
          <p><strong>4. Ground Verification:</strong> WebRTC camera-only lock, GPS/NTP telemetry watermark, and 12-step default replacement protocol.</p>
          <p><strong>5. Legal Safe Harbor:</strong> Positioned as SaaS technical intermediary under IT Act 2000 Section 79, with 10-point governance checklist.</p>
        </div>
        <h2>D. Executive Sign-Off & Corporate Governance Seal</h2>
        <table style="margin-top: 6px;">
          <thead>
            <tr><th>Governance Parameter</th><th>Official Engineering Record</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Founder & CEO</strong></td><td>Piyush Singh (BCA 2nd Year, GL Bajaj Institute of Management)</td></tr>
            <tr><td><strong>Parent Organization</strong></td><td>Resence Tech Labs (<code>resence.in</code>) | Product: ACTA (<code>acta.resence.in</code>)</td></tr>
            <tr><td><strong>Incubation Target</strong></td><td>GL Bajaj Center for Research and Incubation (GLBCRI), Greater Noida</td></tr>
            <tr><td><strong>Document Classification</strong></td><td>Master Product Requirements Document (PRD v2.6 Revised - SSOT)</td></tr>
            <tr><td><strong>Locked Brand Tagline</strong></td><td>Small Acts. Big Impact.</td></tr>
            <tr><td><strong>Verification Standard</strong></td><td>Cryptographic Frame Hashing, WebRTC Telemetry, Two-Person Approval</td></tr>
          </tbody>
        </table>"""

old_appendix_b = """        <h2>B. Specific Asks from GLBCRI (Bharat Udyam Sangam 2026)</h2>
        <ol>
          <li><strong>Institutional Credibility & Letterhead:</strong> Introducing ACTA under GL Bajaj / GLBCRI official backing to 18–20 verified local NGOs.</li>
          <li><strong>Campus Pilot Authorization:</strong> Permission to run an official 30-day student micro-giving pilot across GL Bajaj Knowledge Park hostels.</li>
          <li><strong>Pre-Incubation Mentorship:</strong> Legal structuring for NGO MoUs, Section 8/Pvt Ltd formalization, and seed grant guidance.</li>
        </ol>"""

html_full_page = html_full_page.replace(old_appendix_b, appendix_expansion)

with open(html_target_docs, "w", encoding="utf-8") as f:
    f.write(html_full_page)

print(f"ACTA PRD HTML written to {html_target_docs}")

# Compile PDF using Edge Headless
edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target_docs}",
    f"file:///{html_target_docs.replace(os.sep, '/')}"
]

print("Compiling ACTA PRD.pdf via Edge Headless...")
result = subprocess.run(edge_cmd, capture_output=True, text=True)

if os.path.exists(pdf_target_docs):
    reader = pypdf.PdfReader(pdf_target_docs)
    page_count = len(reader.pages)
    print(f"SUCCESS: ACTA PRD.pdf compiled! ({page_count} Pages, {os.path.getsize(pdf_target_docs)} bytes)")
    shutil.copy2(pdf_target_docs, pdf_target_dl)
    # Also update ACTA_PRD_v2.6_REVISED.pdf
    shutil.copy2(pdf_target_docs, os.path.join(downloads_dir, "ACTA_PRD_v2.6_REVISED.pdf"))
    shutil.copy2(pdf_target_docs, os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.pdf"))
    print(f"Copied to {pdf_target_dl}")
else:
    print(f"PDF creation failed: {result.stderr}")

# Copy DOCX to ACTA PRD.docx
src_docx = os.path.join(docs_dir, "ACTA_PRD_v2.6_REVISED.docx")
if os.path.exists(src_docx):
    shutil.copy2(src_docx, docx_target_docs)
    shutil.copy2(src_docx, docx_target_dl)
    print(f"Copied DOCX to {docx_target_dl}")

print("ACTA PRD Build Completed!")
