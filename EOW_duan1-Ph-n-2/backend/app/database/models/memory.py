from sqlalchemy import Column, Integer, ForeignKey, Text

from app.database.database import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )

    summary = Column(Text)