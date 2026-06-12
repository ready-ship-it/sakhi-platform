from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.database import get_db
from app.models.mood import Mood
from app.models.user import User
from app.utils.auth import get_current_user

from app.services.report_service import generate_weekly_report

router = APIRouter()


@router.get("/weekly")
def weekly_report(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    week_ago = datetime.utcnow() - timedelta(days=7)

    moods = (
        db.query(Mood)
        .filter(
            Mood.user_id == current_user.id,
            Mood.created_at >= week_ago
        )
        .all()
    )

    return generate_weekly_report(moods)
