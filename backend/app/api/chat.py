from fastapi import APIRouter
from pydantic import BaseModel

from app.database.database import SessionLocal
from app.agent.persona_agent import PersonaAgent
from app.agent.prompt_builder import PromptBuilder
from app.services.llm_service import LLMService

router = APIRouter()


class ChatRequest(BaseModel):
    character_id: int
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    db = SessionLocal()

    persona = PersonaAgent(db).load_persona(
        request.character_id
    )

    if persona is None:
        return {
            "error": "Character not found"
        }

    prompt = PromptBuilder.build_prompt(
        persona=persona,
        memory="",
        documents="",
        user_question=request.message
    )

    llm = LLMService()

    answer = llm.chat(prompt)

    return {
        "character": persona["name"],
        "reply": answer
    }