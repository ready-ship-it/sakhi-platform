import google.generativeai as genai

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "models/gemini-2.0-flash"
)


def get_reply(message, history=""):

    text = message.lower()

    crisis_keywords = [
        "suicide",
        "kill myself",
        "end my life",
        "want to die",
        "self harm",
        "hurt myself"
    ]

    if any(word in text for word in crisis_keywords):
        return (
            "I'm really concerned about your safety. "
            "If you feel you may harm yourself, please contact local emergency services "
            "or a trusted person immediately. You do not have to face this alone."
        )

    prompt = f"""
You are Sakhi, a compassionate emotional support companion.

Your role:
- Listen carefully
- Be warm and empathetic
- Encourage healthy coping
- Keep responses short (2-5 sentences)
- Sound natural and conversational
- Never claim to be a therapist
- Never diagnose mental health conditions

Previous conversation:
{history}

Current user message:
{message}

Respond warmly and empathetically.
"""

    response = model.generate_content(prompt)

    return response.text
