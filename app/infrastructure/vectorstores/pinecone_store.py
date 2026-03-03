from pinecone import Pinecone as PineconeClient
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain_core.vectorstores import VectorStoreRetriever

from app.infrastructure.vectorstores.base import BaseVectorStore

from app.config import settings
class PineconeStore(BaseVectorStore):
    """Pinecone-backed vector store."""

    def __init__(self, index_name: str, embedding, dimension: int = 128):
        pc = PineconeClient(api_key=settings.pinecone_api_key)
        existing = [idx.name for idx in pc.list_indexes()]
        if index_name not in existing:
            from pinecone import ServerlessSpec
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        index = pc.Index(index_name)
        self._store = LangchainPinecone(index=index, embedding=embedding)

    def add_documents(self, documents: list, **kwargs) -> None:
        self._store.add_documents(documents, **kwargs)

    def as_retriever(self, **kwargs) -> VectorStoreRetriever:
        return self._store.as_retriever(**kwargs)
