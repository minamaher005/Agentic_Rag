### Tavily Search Tool
import os 
import getpass
from app.config import settings
os.environ['TAVILY_API_KEY'] = settings.tavily_api_key
from langchain_community.tools.tavily_search import TavilySearchResults

tavily = TavilySearchResults()