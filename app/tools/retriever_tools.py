from langchain_classic.tools.retriever import create_retriever_tool
from app.infrastructure.embeddings import embedding
from app.infrastructure.vectorstores.chroma_store import ChromaStore
from app.infrastructure.vectorstores.pinecone_store import PineconeStore
from app.infrastructure.llm import model
## create retriever tool
# Pinecone has technical/cloud/ML data (from notebook ingestion)
technical_retriever = PineconeStore(index_name="agenticrag2", embedding=embedding).as_retriever(search_kwargs={"k": 3})

technicalretrievar = create_retriever_tool(
    technical_retriever,
    "technical_retriever",
    "search in data related to cloud and machine learning"
)

# Chroma has health data (from notebook ingestion)
health_retriever = ChromaStore(collection_name="health_collection", embedding=embedding, persist_directory="D:/agentic app/chroma_healh2_db").as_retriever()

healthretriever_tool = create_retriever_tool(
    health_retriever,
    "health_retriever",
    "search in data related to health and medicine"
)