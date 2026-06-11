from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.mood import Mood
from app.models.user import User
from app.utils.auth import get_current_user

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
