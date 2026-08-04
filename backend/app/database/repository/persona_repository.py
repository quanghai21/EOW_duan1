from sqlalchemy.orm import Session

from app.database.models.persona import Persona


class PersonaRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_character_id(self, character_id: int):
        return (
            self.db.query(Persona)
            .filter(Persona.character_id == character_id)
            .first()
        )