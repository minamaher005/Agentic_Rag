from abc import ABC, abstractmethod
from langchain_core.vectorstores import VectorStoreRetriever


class BaseVectorStore(ABC):
    """Contract: every vector store must implement these."""

    @abstractmethod
    def add_documents(self, documents: list, **kwargs) -> None:
        """Store documents into the vector DB."""
        ...

    @abstractmethod
    def as_retriever(self, **kwargs) -> VectorStoreRetriever:
        """Return a LangChain retriever from this store."""
        ...