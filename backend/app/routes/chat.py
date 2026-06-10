from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from openai import OpenAI
from app.config import settings

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are Sakhi, a compassionate emotional support companion.
You help women dealing with loneliness, anxiety, stress,
relationships, self-esteem and life challenges.

Be warm, empathetic and encouraging.
Keep responses concise.
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_reply = response.choices[0].message.content

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