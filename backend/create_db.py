from app.database.database import Base
from app.database.database import engine

from app.database.models.user import User
from app.database.models.character import Character
from app.database.models.persona import Persona
from app.database.models.conversation import Conversation
from app.database.models.message import Message
from app.database.models.memory import Memory
from app.database.models.document import Document
from app.database.models.citation import Citation


Base.metadata.create_all(bind=engine)

print("Database created successfully!")