from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    title = Column(String(255))

    source = Column(String(255))

    content = Column(Text)