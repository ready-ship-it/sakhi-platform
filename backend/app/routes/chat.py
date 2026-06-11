from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user
from app.services.ai_service import get_reply
from app.schemas.chat import ChatRequest

router = APIRouter()


@router.post("/send")
def send(
    data: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_message = data.message

    history_records = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.id.desc())
        .limit(5)
        .all()
    )

    history_text = ""

    for chat in reversed(history_records):
        history_text += f"User: {chat.message}\nSakhi: {chat.reply}\n\n"

    try:
        ai_reply = get_reply(user_message, history_text)

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
        .order_by(ChatMessage.created_at.desc())
        .all()
    )

    return chats
