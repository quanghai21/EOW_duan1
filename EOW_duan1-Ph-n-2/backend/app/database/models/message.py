from sqlalchemy import Column, Integer, ForeignKey, Text, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    conversation_id = Column(Integer, ForeignKey("conversations.id"))

    sender = Column(String(20))

    content = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())