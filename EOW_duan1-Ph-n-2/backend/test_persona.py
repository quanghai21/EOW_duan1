from app.database.database import SessionLocal
from app.agent.persona_agent import PersonaAgent

db = SessionLocal()

agent = PersonaAgent(db)

persona = agent.load_persona(1)

print(persona)