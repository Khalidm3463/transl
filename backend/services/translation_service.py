import requests
import os
from dotenv import load_dotenv

load_dotenv()
TRANSLATE_API_KEY = os.getenv("TRANSLATE_API_KEY")

def translate_text(text: str, target_lang: str):
    url = "https://api.deepl.com/v2/translate"
    params = {
        "auth_key": TRANSLATE_API_KEY,
        "text": text,
        "target_lang": target_lang,
    }
    response = requests.post(url, data=params)
    return response.json()
