class MemoryService:

    def __init__(self, history_service):
        self.history_service = history_service

    def build_memory(self, conversation_id):

        history = self.history_service.get_history(
            conversation_id
        )

        if not history:
            return ""

        memory_lines = []

        for message in history:

            sender = message.get("sender")
            content = message.get("content", "").strip()

            if not content:
                continue

            if sender == "user":
                memory_lines.append(
                    f"Người dùng: {content}"
                )

            elif sender == "assistant":
                memory_lines.append(
                    f"Nhân vật: {content}"
                )

        return "\n".join(memory_lines)