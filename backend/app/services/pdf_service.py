from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def build_chat_pdf(chats):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    for chat in chats:
        elements.append(
            Paragraph(
                f"<b>User:</b> {chat.message}",
                styles["BodyText"]
            )
        )
        elements.append(
            Paragraph(
                f"<b>Sakhi:</b> {chat.reply}",
                styles["BodyText"]
            )
        )
        elements.append(Spacer(1, 12))

    doc.build(elements)

    buffer.seek(0)
    return buffer
