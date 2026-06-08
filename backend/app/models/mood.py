from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from app.database import Base


class Mood(Base):

    __tablename__ = "moods"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    mood = Column(String(50))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )