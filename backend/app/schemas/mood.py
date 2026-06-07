# backend/app/schemas/mood.py

from pydantic import BaseModel

class MoodRequest(BaseModel):
    mood: str