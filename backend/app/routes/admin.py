from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
def stats():

    return {
        "users": 1,
        "messages": 10,
        "moods": 5
    }


@router.get("/insights")
def insights():

    return [
        {
            "category": "loneliness",
            "sentiment": "medium",
            "summary": "Users frequently discuss loneliness."
        },
        {
            "category": "stress",
            "sentiment": "high",
            "summary": "Many users mention family-related stress."
        }
    ]