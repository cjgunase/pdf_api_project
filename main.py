import io
from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    """
    Extracts raw text from an uploaded PDF file.
    Returns the text as a string.
    """
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return {"text": text}

