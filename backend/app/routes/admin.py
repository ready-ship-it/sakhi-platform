from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.chat_message import ChatMessage
from app.models.mood import Mood

router = APIRouter()


@router.get("/stats")
def stats(db: Session = Depends(get_db)):

    return {
        "users": db.query(User).count(),
        "messages": db.query(ChatMessage).count(),
        "moods": db.query(Mood).count()
    }


@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):

    return {
        "total_users": db.query(User).count(),
        "total_messages": db.query(ChatMessage).count(),
        "total_moods": db.query(Mood).count()
    }


@router.get("/insights")
def insights(db: Session = Depends(get_db)):

    loneliness_count = (
        db.query(ChatMessage)
        .filter(ChatMessage.message.ilike("%lonely%"))
        .count()
    )

    stress_count = (
        db.query(ChatMessage)
        .filter(ChatMessage.message.ilike("%stress%"))
        .count()
    )

    return [
        {
            "category": "loneliness",
            "sentiment": "medium" if loneliness_count > 0 else "low",
            "summary": f"{loneliness_count} messages mention loneliness."
        },
        {
            "category": "stress",
            "sentiment": "high" if stress_count > 5 else "medium" if stress_count > 0 else "low",
            "summary": f"{stress_count} messages mention stress."
        }
    ]
