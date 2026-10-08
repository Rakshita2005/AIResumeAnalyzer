import pdfplumber
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    """Extracts text from uploaded PDF."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def analyze_resume(text, job_keywords):
    """Analyzes resume text and compares with job keywords."""
    doc = nlp(text)

    # Extract entities (skills/orgs/keywords)
    skills = set([ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "NORP", "GPE"]])

    # Check missing job keywords
    missing_keywords = [kw.strip() for kw in job_keywords if kw.lower() not in text.lower()]

    return {
        "word_count": len(text.split()),
        "skills_found": list(skills),
        "missing_keywords": missing_keywords
    }