from sqlalchemy.orm import Session

from app.database.models.memory import Memory


class MemoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get(self, memory_id: int):

        return (
            self.db.query(Memory)
            .filter(Memory.id == memory_id)
            .first()
        )

    def get_by_conversation_id(
        self,
        conversation_id: int
    ):

        return (
            self.db.query(Memory)
            .filter(
                Memory.conversation_id == conversation_id
            )
            .order_by(Memory.id.asc())
            .all()
        )

    def create(
        self,
        conversation_id: int,
        content: str
    ):

        memory = Memory(
            conversation_id=conversation_id,
            content=content
        )

        self.db.add(memory)
        self.db.commit()
        self.db.refresh(memory)

        return memory

    def delete(self, memory_id: int):

        memory = self.get(memory_id)

        if memory is None:
            return False

        self.db.delete(memory)
        self.db.commit()

        return True