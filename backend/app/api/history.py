from fastapi import APIRouter, HTTPException

from app.database.database import SessionLocal
from app.database.repository.message_repository import MessageRepository
from app.database.repository.conversation_repository import ConversationRepository


router = APIRouter()


@router.get("/history/{conversation_id}")
def get_history(conversation_id: int):

    db = SessionLocal()

    try:

        conversation_repo = ConversationRepository(db)
        message_repo = MessageRepository(db)

        conversation = conversation_repo.get(
            conversation_id
        )

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found"
            )

        messages = message_repo.get_by_conversation(
            conversation_id
        )

        result = []

        for message in messages:

            result.append({
                "id": message.id,
                "conversation_id": message.conversation_id,
                "sender": message.sender,
                "content": message.content,
                "created_at": message.created_at
            })

        return {
            "conversation_id": conversation_id,
            "messages": result
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to get conversation history"
        )

    finally:
        db.close()