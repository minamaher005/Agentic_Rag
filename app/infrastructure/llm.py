import os 
import getpass
from app.config import settings
## setup gemini api key 
os.environ["GOOGLE_API_KEY"] = settings.google_api_key
from langchain_google_genai import ChatGoogleGenerativeAI

model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.2)