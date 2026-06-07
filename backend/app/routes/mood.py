from fastapi import APIRouter

router = APIRouter()

moods = []

@router.post("/add")
<<<<<<< HEAD
def add(mood: str):
    moods.append(mood)
=======
def add(data: MoodRequest):
>>>>>>> 1bdb669 (Initial commit: new)
    return {"status": "saved"}
