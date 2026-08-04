from app.database.repository.character_repository import CharacterRepository
from app.database.repository.persona_repository import PersonaRepository


class PersonaAgent:

    def __init__(self, db):

        self.character_repo = CharacterRepository(db)
        self.persona_repo = PersonaRepository(db)

    def load_persona(self, character_id):

        character = self.character_repo.get(character_id)

        if character is None:
            return None

        persona = self.persona_repo.get_by_character_id(
            character_id
        )

        if persona is None:
            return None

        return {
            "name": character.name,
            "occupation": character.occupation,
            "description": character.description,
            "speaking_style": persona.speaking_style,
            "personality": persona.personality,
            "system_prompt": persona.system_prompt,
        }