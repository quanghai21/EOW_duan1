from app.services.llm_service import LLMService

llm = LLMService()

response = llm.chat(
    "Xin chào! Hãy giới thiệu bản thân trong 2 câu."
)

print("\n===== PHẢN HỒI TỪ GEMINI =====\n")
print(response)