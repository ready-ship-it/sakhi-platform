import google.generativeai as genai

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_reply(message: str):

    prompt = f"""
You are Sakhi, a compassionate emotional support companion.

Your role:
- Listen carefully
- Be warm and empathetic
- Encourage healthy coping
- Keep responses short (2-5 sentences)
- Sound natural and conversational
- Do not sound overly poetic or dramatic
- Never claim to be a therapist
- Never diagnose mental health conditions

User message:
{message}
"""

    response = model.generate_content(prompt)

    return response.text