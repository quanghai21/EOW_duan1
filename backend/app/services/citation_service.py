class ConversationService:

    def __init__(self, repo):
        self.repo = repo

    def create(self, character_id: int):
        return self.repo.create(character_id)

    def get(self, conversation_id: int):
        return self.repo.get(conversation_id)

    def get_all(self):
        return self.repo.get_all()

    def delete(self, conversation_id: int):
        return self.repo.delete(conversation_id)