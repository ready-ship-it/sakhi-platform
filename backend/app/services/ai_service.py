import google.generativeai as genai

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

def get_reply(message):

    response = model.generate_content(message)

    return response.text