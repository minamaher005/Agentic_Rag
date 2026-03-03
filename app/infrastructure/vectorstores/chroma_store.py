from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

from app.infrastructure.vectorstores.base import BaseVectorStore


class ChromaStore(BaseVectorStore):
    """Chroma-backed vector store."""

    def __init__(self, collection_name: str, embedding, persist_directory: str):
        self._store = Chroma(
            collection_name=collection_name,
            embedding_function=embedding,
            persist_directory=persist_directory,
        )

    def add_documents(self, documents: list, **kwargs) -> None:
        self._store.add_documents(documents, **kwargs)

    def as_retriever(self, **kwargs) -> VectorStoreRetriever:
        return self._store.as_retriever(**kwargs)
