from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/latest")
def latest_mood(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    last_chat = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.id.desc())
        .first()
    )

    if not last_chat:
        return {
            "success": False,
            "message": "No chats found"
        }

    text = last_chat.message.lower()

    mood = "neutral"

    if any(word in text for word in [
        "lonely",
        "alone",
        "isolated"
    ]):
        mood = "lonely"

    elif any(word in text for word in [
        "sad",
        "cry",
        "depressed"
    ]):
        mood = "sad"

    elif any(word in text for word in [
        "anxious",
        "worried",
        "panic"
    ]):
        mood = "anxious"

    elif any(word in text for word in [
        "stress",
        "stressed",
        "pressure"
    ]):
        mood = "stressed"

    elif any(word in text for word in [
        "happy",
        "great",
        "excited"
    ]):
        mood = "happy"

    return {
        "success": True,
        "mood": mood
    }