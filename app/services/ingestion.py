# app/services/ingestion.py
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.infrastructure.vectorstores.base import BaseVectorStore


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    separators=[" "],
)


def ingest_from_directory(path: str, store: BaseVectorStore, glob: str = "**/*.pdf") -> int:

    loader = DirectoryLoader(path=path, glob=glob, loader_cls=PyMuPDFLoader)
    docs = loader.load()
    chunks = text_splitter.split_documents(docs)
    store.add_documents(chunks)
    return len(chunks)


def ingest_single_pdf(pdf_path: str, store: BaseVectorStore) -> int:

    docs = PyMuPDFLoader(pdf_path).load()
    chunks = text_splitter.split_documents(docs)
    store.add_documents(chunks)
    return len(chunks)
