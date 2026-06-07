from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Temporary memory storage
moods = []


class MoodRequest(BaseModel):
    mood: str


@router.post("/add")
def add_mood(data: MoodRequest):

    moods.append({
        "mood": data.mood
    })

    return {
        "success": True,
        "message": "Mood saved"
    }


@router.get("/list")
def mood_list():
    return moods