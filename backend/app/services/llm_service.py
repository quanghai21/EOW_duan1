import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class LLMService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY chưa được cấu hình trong file .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-flash-latest"

    def chat(self, prompt: str):

        if not prompt or not prompt.strip():
            return ""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        if not response or not response.text:
            return "Xin lỗi, tôi chưa thể trả lời câu hỏi này."

        return response.text