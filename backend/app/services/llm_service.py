import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class LLMService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(api_key=api_key)

        # Đổi model
        self.model = "gemini-3.5-flash"

    def chat(self, prompt: str):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text