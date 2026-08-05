from sqlalchemy import Column, Integer, ForeignKey

from app.database.database import Base


class Citation(Base):

    __tablename__ = "citations"

    id = Column(Integer, primary_key=True)

    message_id = Column(
        Integer,
        ForeignKey("messages.id")
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    page = Column(Integer)