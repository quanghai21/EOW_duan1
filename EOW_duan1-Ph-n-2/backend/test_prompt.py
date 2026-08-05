from app.database.database import SessionLocal
from app.agent.persona_agent import PersonaAgent
from app.agent.prompt_builder import PromptBuilder

db = SessionLocal()

persona = PersonaAgent(db).load_persona(1)

memory = """
Người dùng đã hỏi về ca mổ đầu tiên.
"""

documents = """
Trang 43:

Ngày hôm đó tôi thực hiện ca mổ trong điều kiện thiếu thuốc mê...
"""

question = "Bác nhớ ca mổ đầu tiên không?"

prompt = PromptBuilder.build_prompt(
    persona,
    memory,
    documents,
    question
)

print(prompt)