from sqlalchemy.orm import Session

from app.database.models.character import Character
from app.database.models.persona import Persona


class PersonaAgent:

    def __init__(self, db: Session):
        self.db = db

    def load_persona(self, character_id: int):
        character = (
            self.db.query(Character)
            .filter(Character.id == character_id)
            .first()
        )

        persona = (
            self.db.query(Persona)
            .filter(Persona.character_id == character_id)
            .first()
        )

        if not character or not persona:
            return None

        return {
            "name": character.name,
            "occupation": character.occupation,
            "description": character.description,
            "speaking_style": persona.speaking_style,
            "personality": persona.personality,
            "system_prompt": persona.system_prompt,
        }