from sqlalchemy.orm import Session

from app.database.models.message import Message


class MessageRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        conversation_id: int,
        sender: str,
        content: str
    ):

        message = Message(
            conversation_id=conversation_id,
            sender=sender,
            content=content
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message

    def get_by_conversation(
        self,
        conversation_id: int
    ):

        return (
            self.db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(
                Message.id.asc()
            )
            .all()
        )

    def get(self, message_id: int):

        return (
            self.db.query(Message)
            .filter(
                Message.id == message_id
            )
            .first()
        )