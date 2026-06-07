from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Temporary memory storage
chat_history = []


class ChatRequest(BaseModel):
    message: str


@router.post("/send")
def send(data: ChatRequest):

    user_message = data.message

    # Temporary AI response
    ai_reply = f"Sakhi: I understand. You said: {user_message}"

    chat_history.append({
        "user": user_message,
        "ai": ai_reply
    })

    return {
        "success": True,
        "reply": ai_reply
    }


@router.get("/history")
def history():
    return chat_history