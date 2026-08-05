from fastapi import APIRouter
from app.database.database import SessionLocal
from app.database.models.character import Character

router = APIRouter()


@router.get("/characters")
def get_characters():
    db = SessionLocal()
    try:
        characters = db.query(Character).all()
        result = []
        for character in characters:
            result.append(
                {
                    "id": character.id,
                    "name": character.name,
                    "description": character.description,
                    "personality": character.personality,
                    "greeting": character.greeting,
                    "avatar_url": character.avatar_url,
                }
            )
        return result
    finally:
        db.close()