# from fastapi import APIRouter
# from pydantic import BaseModel
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()
# TRANSLATE_API_KEY = os.getenv("TRANSLATE_API_KEY")

# router = APIRouter(prefix="/translate", tags=["Translation"])

# class TranslationRequest(BaseModel):
#     text: str
#     target_lang: str

# @router.post("/")
# def translate_text(request: TranslationRequest):
#     url = "https://api.deepl.com/v2/translate"
#     params = {
#         "auth_key": TRANSLATE_API_KEY,
#         "text": request.text,
#         "target_lang": request.target_lang,
#     }
#     response = requests.post(url, data=params)
#     return response.json()



# from fastapi import APIRouter
# from pydantic import BaseModel
# import requests
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the DeepL API key from environment variables
# TRANSLATE_API_KEY = os.getenv("TRANSLATE_API_KEY")

# # Raise an error if API key is not found
# if not TRANSLATE_API_KEY:
#     raise ValueError("TRANSLATE_API_KEY not found in environment variables")

# # Define the input schema
# class TranslationRequest(BaseModel):
#     text: str
#     target_lang: str  # Example: "EN", "DE", "FR"

# # Create the router
# router = APIRouter(
#     prefix="/translate",
#     tags=["Translation"]
# )

# # Define the translation endpoint
# @router.post("/")
# def translate_text(request: TranslationRequest):
#     url = "https://api.deepl.com/v2/translate"
#     params = {
#         "auth_key": TRANSLATE_API_KEY,
#         "text": request.text,
#         "target_lang": request.target_lang.upper()
#     }

#     try:
#         response = requests.post(url, data=params)
#         response.raise_for_status()
#         result = response.json()

#         translation = result.get("translations", [{}])[0]
#         return {
#             "translated_text": translation.get("text"),
#             "detected_source_lang": translation.get("detected_source_language")
#         }

#     except requests.RequestException as e:
#         return {
#             "error": "Translation failed",
#             "details": str(e)
#         }



from fastapi import APIRouter
from pydantic import BaseModel
from googletrans import Translator

# Define request schema
class TranslationRequest(BaseModel):
    text: str
    target_lang: str  # e.g., 'en', 'fr', 'de'

# Create router
router = APIRouter(
    prefix="/translate",
    tags=["Translation"]
)

translator = Translator()

# Translation endpoint
@router.post("/")
def translate_text(request: TranslationRequest):
    try:
        result = translator.translate(request.text, dest=request.target_lang.lower())
        return {
            "translated_text": result.text,
            "detected_source_lang": result.src
        }
    except Exception as e:
        return {
            "error": "Translation failed",
            "details": str(e)
        }
