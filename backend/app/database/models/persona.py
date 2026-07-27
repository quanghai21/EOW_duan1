from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Persona(Base):

    __tablename__ = "personas"

    id = Column(
        Integer,
        primary_key=True
    )

    character_id = Column(
        Integer,
        ForeignKey("characters.id")
    )

    speaking_style = Column(
        String(255)
    )

    personality = Column(
        Text
    )

    system_prompt = Column(
        Text
    )