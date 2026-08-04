from fastapi import APIRouter, HTTPException

from app.database.database import SessionLocal
from app.database.repository.conversation_repository import ConversationRepository


router = APIRouter()


@router.get("/conversations")
def get_conversations():

    db = SessionLocal()

    try:
        repository = ConversationRepository(db)

        conversations = repository.get_all()

        result = []

        for conversation in conversations:
            result.append({
                "id": conversation.id,
                "character_id": conversation.character_id,
                "created_at": conversation.created_at
            })

        return result

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to get conversations"
        )

    finally:
        db.close()


@router.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: int):

    db = SessionLocal()

    try:
        repository = ConversationRepository(db)

        conversation = repository.get(conversation_id)

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found"
            )

        return {
            "id": conversation.id,
            "character_id": conversation.character_id,
            "created_at": conversation.created_at
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to get conversation"
        )

    finally:
        db.close()


@router.delete("/conversations/{conversation_id}")
def delete_conversation(conversation_id: int):

    db = SessionLocal()

    try:
        repository = ConversationRepository(db)

        conversation = repository.get(conversation_id)

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found"
            )

        repository.delete(conversation_id)

        return {
            "message": "Conversation deleted successfully",
            "conversation_id": conversation_id
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to delete conversation"
        )

    finally:
        db.close()