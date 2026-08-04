class CharacterNotFoundError(Exception):

    def __init__(self, character_id: int):

        self.character_id = character_id

        super().__init__(
            f"Character {character_id} not found"
        )


class ConversationNotFoundError(Exception):

    def __init__(self, conversation_id: int):

        self.conversation_id = conversation_id

        super().__init__(
            f"Conversation {conversation_id} not found"
        )


class PersonaNotFoundError(Exception):

    def __init__(self, character_id: int):

        self.character_id = character_id

        super().__init__(
            f"Persona for character {character_id} not found"
        )


class LLMError(Exception):

    def __init__(self, message: str):

        super().__init__(message)