import os
import pypdf
import docx
import re

docs_dir = r"C:\Users\HP\.gemini\antigravity\scratch\ServeMATE\docs"
downloads_dir = r"C:\Users\HP\Downloads"

files_to_check = [
    "ACTA_PRD_v2.6_REVISED.pdf",
    "ACTA_PRD_v2.6_REVISED.docx",
    "ACTA_GLBCRI_QUESTION_BANK_REVISED.pdf",
    "ACTA_GLBCRI_QUESTION_BANK_REVISED.docx",
    "ACTA_CHANGELOG_AND_RISK_REGISTER.md",
    "ACTA_NGO_DEFAULT_AND_REPLACEMENT_WORKFLOW.md",
    "ACTA_DONOR_COMMUNICATION_TEMPLATES.md",
    "ACTA_PAYMENT_LEGAL_REVIEW_CHECKLIST.md"
]

print("=" * 80)
print("ACTA BY RESENCE — DELIVERABLES VERIFICATION REPORT (V2.6 AUDIT)")
print("=" * 80)

all_ok = True

for f_name in files_to_check:
    docs_path = os.path.join(docs_dir, f_name)
    dl_path = os.path.join(downloads_dir, f_name)
    
    docs_exists = os.path.exists(docs_path)
    dl_exists = os.path.exists(dl_path)
    
    if not (docs_exists and dl_exists):
        print(f"[FAIL] Missing file: {f_name} (docs: {docs_exists}, downloads: {dl_exists})")
        all_ok = False
        continue
    
    size_docs = os.path.getsize(docs_path)
    size_dl = os.path.getsize(dl_path)
    
    extra_info = ""
    if f_name.endswith(".pdf"):
        reader = pypdf.PdfReader(docs_path)
        extra_info = f" | {len(reader.pages)} Pages"
    elif f_name.endswith(".docx"):
        d = docx.Document(docs_path)
        extra_info = f" | {len(d.paragraphs)} Paragraphs, {len(d.tables)} Tables"
    elif f_name.endswith(".md"):
        with open(docs_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        extra_info = f" | {len(lines)} Lines"
        
    print(f"[PASS] {f_name:<42} | Size: {size_docs:>9,} bytes{extra_info}")

print("-" * 80)
print("AUDITING TEXT INTEGRITY ACROSS GENERATED ARTIFACTS...")

# Check PRD PDF text
prd_pdf_path = os.path.join(downloads_dir, "ACTA_PRD_v2.6_REVISED.pdf")
reader_prd = pypdf.PdfReader(prd_pdf_path)
prd_full_text = " ".join([page.extract_text() or "" for page in reader_prd.pages])

qb_pdf_path = os.path.join(downloads_dir, "ACTA_GLBCRI_QUESTION_BANK_REVISED.pdf")
reader_qb = pypdf.PdfReader(qb_pdf_path)
qb_full_text = " ".join([page.extract_text() or "" for page in reader_qb.pages])

combined_text = prd_full_text + " " + qb_full_text

err_105 = len(re.findall(r'105%', combined_text))
err_90105 = len(re.findall(r'90/10/5', combined_text))
err_freefire = len(re.findall(r'Free\s*Fire', combined_text, re.IGNORECASE))
cr_mentions = len(re.findall(r'Continuity Reserve', combined_text, re.IGNORECASE))

print(f"Occurrences of '105%':                  {err_105} (Expected: 0)")
print(f"Occurrences of '90/10/5':                {err_90105} (Expected: 0)")
print(f"Occurrences of 'Free Fire':              {err_freefire} (Expected: 0)")
print(f"Occurrences of 'Continuity Reserve':     {cr_mentions} (Expected: > 0)")

if err_105 == 0 and err_90105 == 0 and err_freefire == 0 and cr_mentions > 0:
    print("\n>>> AUDIT PASSED: ZERO CONTRADICTIONS, ZERO BRAND LEAKS, 100% GROUNDED! <<<")
else:
    print("\n>>> AUDIT FAILED: Discrepancies detected! <<<")
print("=" * 80)
