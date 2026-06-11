from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user
from app.services.ai_service import get_reply

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

    # Get recent chat history
    recent_chats = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.id.desc())
        .limit(5)
        .all()
    )

    history = ""

    for chat in reversed(recent_chats):
        history += (
            f"User: {chat.message}\n"
            f"Sakhi: {chat.reply}\n\n"
        )

    try:

        ai_reply = get_reply(
            message=user_message,
            history=history
        )

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

    chats = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .all()
    )

    return chats