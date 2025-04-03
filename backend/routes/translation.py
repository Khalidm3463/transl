from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TRANSLATE_API_KEY = os.getenv("TRANSLATE_API_KEY")

router = APIRouter(prefix="/translate", tags=["Translation"])

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/")
def translate_text(request: TranslationRequest):
    url = "https://api.deepl.com/v2/translate"
    params = {
        "auth_key": TRANSLATE_API_KEY,
        "text": request.text,
        "target_lang": request.target_lang,
    }
    response = requests.post(url, data=params)
    return response.json()
