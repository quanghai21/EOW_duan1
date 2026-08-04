class RetrievalAgent:

    def __init__(self, documents=None):

        self.documents = documents or []

    def search(self, query: str):

        if not query:
            return []

        # Khung Retrieval.
        # Sau này tích hợp ChromaDB / FAISS.

        return []