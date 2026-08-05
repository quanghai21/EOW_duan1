from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database.database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    personality = Column(String, nullable=True)
    greeting = Column(Text, nullable=True)
    avatar_url = Column(String, nullable=True)

    # Thêm dòng này để khớp với back_populates hoặc quan hệ từ model Persona
    personas = relationship("Persona", back_populates="character")
