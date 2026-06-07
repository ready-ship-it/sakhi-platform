from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_reply(message):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Sakhi, an emotional support AI for loneliness."},
            {"role": "user", "content": message}
        ]
    )
    return res.choices[0].message.content
