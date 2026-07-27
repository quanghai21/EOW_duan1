from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Character(Base):

    __tablename__ = "characters"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(200),
        nullable=False
    )

    occupation = Column(
        String(100)
    )

    avatar = Column(
        String(255)
    )

    description = Column(
        Text
    )