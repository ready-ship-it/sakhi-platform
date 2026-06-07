from fastapi import APIRouter
from app.services.ai_service import get_reply

router = APIRouter()

chat_history = []


@router.post("/send")
def send(message: str):
    reply = get_reply(message)
    chat_history.append({"user": message, "ai": reply})
    return {"reply": reply}
=======
from app.schemas.chat import ChatRequest

@router.post("/send")
def send(data: ChatRequest):

    reply = get_reply(data.message)

    return {"reply": reply}
