import google.generativeai as genai

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "models/gemini-2.0-flash"
)


def get_reply(message, history=""):

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

Previous conversation:
{history}

Current user message:
{message}

Respond warmly and empathetically.
"""

     response = model.generate_content(prompt)

    if hasattr(response, "text") and response.text:
        return response.text

    return (
        "I'm here with you. "
        "Tell me a little more about how you're feeling."
    )