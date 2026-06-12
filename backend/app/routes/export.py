from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.chat_message import ChatMessage
from app.models.user import User
from app.utils.auth import get_current_user
from app.services.pdf_service import build_chat_pdf

router = APIRouter()


@router.get("/chat-pdf")
def export_chat_pdf(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chats = (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.created_at.asc())
        .all()
    )

    pdf_buffer = build_chat_pdf(chats)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=chat_history.pdf"
        }
    )
