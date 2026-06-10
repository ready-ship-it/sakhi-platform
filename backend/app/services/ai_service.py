import google.generativeai as genai

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def get_reply(message):

    prompt = f"""
You are Sakhi, an emotional support AI.

Help users with:
- loneliness
- anxiety
- stress
- relationships
- self-esteem

User:
{message}
"""

    response = model.generate_content(prompt)

    return response.text