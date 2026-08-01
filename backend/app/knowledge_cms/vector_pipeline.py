import os
import chromadb
from chromadb.utils import embedding_functions

VECTOR_DB_DIR = os.path.join(os.path.dirname(__file__), "../../../vector_db")
os.makedirs(VECTOR_DB_DIR, exist_ok=True)

chroma_client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
collection = chroma_client.get_or_create_collection(
    name="history_knowledge", 
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

class VectorPipeline:
    @staticmethod
    def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
        chunks = []
        start = 0
        while start < len(text):
            chunks.append(text[start : start + chunk_size])
            start += chunk_size - overlap
        return chunks

    @classmethod
    def index_document(cls, text: str, metadata: dict) -> int:
        chunks = cls.chunk_text(text)
        doc_id = f"doc_{os.urandom(3).hex()}"
        
        ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
        metadatas = [metadata for _ in chunks]

        collection.add(documents=chunks, metadatas=metadatas, ids=ids)
        return len(chunks)