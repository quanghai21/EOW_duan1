from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    character_id = Column(Integer, ForeignKey("characters.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())