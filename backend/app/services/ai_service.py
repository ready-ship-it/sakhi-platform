import google.generativeai as genai

for m in genai.list_models():
    print(m.name)

from app.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-pro"
)


def get_reply(message: str):

    prompt = f"""
You are Sakhi, a compassionate emotional support companion.

Help women with:
- loneliness
- anxiety
- stress
- relationships
- self-esteem

Be warm, supportive, empathetic and concise.

User message:
{message}
"""

    response = model.generate_content(prompt)

    return response.text