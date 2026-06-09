from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/send")
def send(
    data: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    ai_reply = (
        f"Sakhi: I understand. You said: "
        f"{data.message}"
    )

    chat = ChatMessage(
        user_id=current_user.id,
        message=data.message,
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