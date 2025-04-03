from fastapi import APIRouter, UploadFile, File
import pytesseract
from PIL import Image
import io

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    extracted_text = pytesseract.image_to_string(image)
    return {"extracted_text": extracted_text}
