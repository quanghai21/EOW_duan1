class HistoryService:

    def __init__(self, message_repository):
        self.message_repository = message_repository

    def save_user_message(self, conversation_id, content):
        return self.message_repository.create(
            conversation_id=conversation_id,
            sender="user",
            content=content
        )

    def save_ai_message(self, conversation_id, content):
        return self.message_repository.create(
            conversation_id=conversation_id,
            sender="assistant",
            content=content
        )

    def get_history(self, conversation_id):

        messages = self.message_repository.get_by_conversation(
            conversation_id
        )

        result = []

        for message in messages:
            result.append({
                "id": message.id,
                "sender": message.sender,
                "content": message.content,
                "created_at": message.created_at.isoformat()
                if message.created_at
                else None
            })

        return result

    def get_messages(self, conversation_id):
        return self.get_history(conversation_id)