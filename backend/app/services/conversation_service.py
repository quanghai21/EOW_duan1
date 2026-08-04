class ConversationService:

    def __init__(self, repo):
        self.repo = repo

    def create(self, character_id):
        return self.repo.create(character_id)

    def get(self, conversation_id):
        return self.repo.get(conversation_id)

    def list(self):
        return self.repo.list()

    def delete(self, conversation_id):
        return self.repo.delete(conversation_id)