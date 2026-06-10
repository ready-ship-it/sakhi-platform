from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import google.generativeai as genai

from app.config import settings
from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user


genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/send")
def send(
    data: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_message = data.message

    try:

        prompt = f"""
You are Sakhi, a compassionate emotional support companion.

Help women with:
- loneliness
- anxiety
- stress
- relationships
- self-esteem

User message:
{user_message}
"""

        response = model.generate_content(prompt)

        ai_reply = response.text

    except Exception as e:

        print("Gemini Error:", e)

        ai_reply = (
            "I'm here with you. "
            "Tell me a little more about how you're feeling."
        )

    chat = ChatMessage(
        user_id=current_user.id,
        message=user_message,
        reply=ai_reply
    )

    db.add(chat)
    db.commit()

    return {
        "success": True,
        "reply": ai_reply
    }


@router.get("/history")
def history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chats = db.query(ChatMessage).filter(
        ChatMessage.user_id == current_user.id
    ).all()

    return chats