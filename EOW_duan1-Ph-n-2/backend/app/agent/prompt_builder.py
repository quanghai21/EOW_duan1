class PromptBuilder:

    @staticmethod
    def build_prompt(persona, memory, documents, user_question):

        prompt = f"""
Bạn là:

{persona['name']}

Nghề nghiệp:

{persona['occupation']}

Mô tả:

{persona['description']}

Phong cách nói:

{persona['speaking_style']}

Tính cách:

{persona['personality']}

========================

System Prompt

{persona['system_prompt']}

========================

Lịch sử hội thoại

{memory}

========================

Tài liệu lịch sử

{documents}

========================

Người dùng hỏi

{user_question}

========================

Yêu cầu:

- Chỉ trả lời dựa trên tài liệu.
- Không bịa đặt.
- Nếu không có thông tin hãy nói rõ.
- Giữ đúng phong cách nhân vật.
- Trả lời tự nhiên như đang trò chuyện.
"""

        return prompt