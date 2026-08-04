from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import logging

from app.database.database import SessionLocal

from app.agent.persona_agent import PersonaAgent
from app.agent.prompt_builder import PromptBuilder

from app.services.llm_service import LLMService
from app.services.conversation_service import ConversationService
from app.services.history_service import HistoryService
from app.services.memory_service import MemoryService

from app.database.repository.conversation_repository import ConversationRepository
from app.database.repository.message_repository import MessageRepository


router = APIRouter()

logger = logging.getLogger("echoes_of_war.chat")


class ChatRequest(BaseModel):
    character_id: int = Field(gt=0)
    message: str = Field(min_length=1, max_length=2000)
    conversation_id: int | None = None


@router.post("/chat")
def chat(request: ChatRequest):
    db = SessionLocal()

    try:
        conversation_repo = ConversationRepository(db)
        message_repo = MessageRepository(db)

        conversation_service = ConversationService(
            conversation_repo
        )

        history_service = HistoryService(
            message_repo
        )

        memory_service = MemoryService(
            history_service
        )

        if request.conversation_id is None:
            conversation = conversation_service.create(
                character_id=request.character_id
            )
        else:
            conversation = conversation_service.get(
                request.conversation_id
            )

            if conversation is None:
                raise HTTPException(
                    status_code=404,
                    detail="Conversation not found"
                )

            if conversation.character_id != request.character_id:
                raise HTTPException(
                    status_code=400,
                    detail="Conversation does not belong to this character"
                )

        persona = PersonaAgent(db).load_persona(
            request.character_id
        )

        if persona is None:
            raise HTTPException(
                status_code=404,
                detail="Character or persona not found"
            )

        history_service.save_user_message(
            conversation.id,
            request.message
        )

        memory = memory_service.build_memory(
            conversation.id
        )

        prompt = PromptBuilder.build_prompt(
            persona=persona,
            memory=memory,
            documents="",
            user_question=request.message
        )

        logger.info(
            "Sending chat request to LLM. conversation_id=%s",
            conversation.id
        )

        answer = LLMService().chat(prompt)

        if not answer:
            raise HTTPException(
                status_code=500,
                detail="AI did not return a response"
            )

        history_service.save_ai_message(
            conversation.id,
            answer
        )

        return {
            "conversation_id": conversation.id,
            "character": persona["name"],
            "reply": answer
        }

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception(
            "Chat error: %s",
            exc
        )

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )

    finally:
        db.close()