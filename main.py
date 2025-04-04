import io
import re
from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    """
    Extracts raw text from an uploaded PDF file and returns it as JSON.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    try:
        contents = await file.read()
        reader = PdfReader(io.BytesIO(contents))
        if not reader.pages:
            raise HTTPException(status_code=400, detail="PDF has no readable pages.")
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if not text.strip():
            raise HTTPException(status_code=400, detail="No extractable text found in PDF.")
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {str(e)}")

def extract_invoice_fields(text: str) -> dict:
    """
    Extracts structured invoice fields from text using regular expressions.
    This is a simple demonstration and may need adjustments for different formats.
    """
    invoice_number_pattern = re.compile(r"Invoice Number:\s*(\S+)")
    date_pattern = re.compile(r"Date:\s*([0-9]{2}/[0-9]{2}/[0-9]{4})")
    total_pattern = re.compile(r"Total:\s*\$?(\d+\.\d{2})")

    invoice_number = invoice_number_pattern.search(text)
    date = date_pattern.search(text)
    total = total_pattern.search(text)
    
    return {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "date": date.group(1) if date else None,
        "total": total.group(1) if total else None,
    }

@app.post("/extract-invoice/")
async def extract_invoice(file: UploadFile = File(...)):
    """
    Extracts structured invoice data from an uploaded PDF file.
    Returns both the extracted invoice fields and the raw text.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    try:
        contents = await file.read()
        reader = PdfReader(io.BytesIO(contents))
        if not reader.pages:
            raise HTTPException(status_code=400, detail="PDF has no readable pages.")
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if not text.strip():
            raise HTTPException(status_code=400, detail="No extractable text found in PDF.")

        invoice_data = extract_invoice_fields(text)
        return {"invoice_data": invoice_data, "raw_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {str(e)}")
    