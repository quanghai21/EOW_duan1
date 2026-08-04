from sqlalchemy.orm import Session

from app.database.models.character import Character


class CharacterRepository:

    def __init__(self, db: Session):

        self.db = db


    def get_all(self):

        return self.db.query(Character).all()


    def get(self, character_id: int):

        return (

            self.db.query(Character)

            .filter(

                Character.id == character_id

            )

            .first()

        )