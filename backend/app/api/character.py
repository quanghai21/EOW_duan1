from fastapi import APIRouter
from app.database.database import SessionLocal
from app.database.models.character import Character

router = APIRouter()


@router.get("/characters")
def get_characters():
    db = SessionLocal()

    characters = db.query(Character).all()

    result = []

    for character in characters:
        result.append(
            {
                "id": character.id,
                "name": character.name,
                "occupation": character.occupation,
                "avatar": character.avatar,
                "description": character.description,
            }
        )

    db.close()

    return result