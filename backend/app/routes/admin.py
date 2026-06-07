from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def stats():
    return {
        "users": 1,
        "messages": 10,
        "moods": 3
    }

@router.get("/insights")
def insights():
    return [
        {"category": "loneliness", "sentiment": "medium"},
        {"category": "stress", "sentiment": "high"}
    ]
