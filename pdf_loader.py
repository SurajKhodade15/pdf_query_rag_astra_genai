from PyPDF2 import PdfReader
import io

def extract_pdf_text(file):
    if hasattr(file, 'read'):
        pdf = PdfReader(io.BytesIO(file.read()))
    else:
        pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        content = page.extract_text()
        if content:
            text += content
    return text
