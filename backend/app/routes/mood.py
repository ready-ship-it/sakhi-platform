from fastapi import APIRouter

router = APIRouter()

moods = []

@router.post("/add")

def add(mood: str):
    moods.append(mood)
=======
def add(data: MoodRequest):
    return {"status": "saved"}
