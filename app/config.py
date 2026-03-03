
from pydantic_settings import BaseSettings
## here basesetting us to override values from the .env files
class Settings(BaseSettings):
    google_api_key: str
    pinecone_api_key: str
    tavily_api_key: str
    pinecone_index_name: str = "agenticrag2"
    llm_model: str = "gemini-2.5-flash-lite"
    llm_temperature: float = 0.2
    embedding_model: str = "embeddinggemma:latest"
    pdf_data_path: str = "./data/pdf"
    chroma_db_path: str = "./chroma_db"

    class Config:
        env_file = ".env"

settings = Settings()  