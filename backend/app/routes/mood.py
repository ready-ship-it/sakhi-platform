from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.mood import Mood
from app.models.user import User
from app.utils.auth import get_current_user
from app.services.coping_service import get_coping_suggestion

router = APIRouter()


class MoodRequest(BaseModel):
    mood: str


@router.post("/add")
def add_mood(
    data: MoodRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    mood = Mood(
        mood=data.mood,
        user_id=current_user.id
    )

    db.add(mood)
    db.commit()

    return {
        "success": True,
        "message": "Mood saved"
    }


@router.get("/list")
def mood_list(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    moods = (
        db.query(Mood)
        .filter(Mood.user_id == current_user.id)
        .order_by(Mood.created_at.desc())
        .all()
    )

    return moods


@router.get("/stats")
def mood_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    moods = (
        db.query(Mood)
        .filter(Mood.user_id == current_user.id)
        .all()
    )

    stats = {}

    for mood in moods:
        stats[mood.mood] = stats.get(mood.mood, 0) + 1

    return stats


@router.get("/trend")
def mood_trend(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    moods = (
        db.query(Mood)
        .filter(Mood.user_id == current_user.id)
        .order_by(Mood.created_at.asc())
        .all()
    )

    return [
        {
            "date": mood.created_at.strftime("%Y-%m-%d"),
            "mood": mood.mood
        }
        for mood in moods
    ]


@router.get("/coping")
def coping(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    latest = (
        db.query(Mood)
        .filter(Mood.user_id == current_user.id)
        .order_by(Mood.created_at.desc())
        .first()
    )

    if not latest:
        return {
            "tip": "Tell us how you're feeling first."
        }

    return {
        "mood": latest.mood,
        "tip": get_coping_suggestion(latest.mood)
    }


@router.get("/checkin")
def daily_checkin():
    return {
        "message": "How are you feeling today? Take a moment to check in with yourself 💜"
    }
