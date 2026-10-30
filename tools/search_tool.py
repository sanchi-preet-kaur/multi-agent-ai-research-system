from pathlib import Path
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(ROOT_DIR / ".env")

search_tool = TavilySearch(max_results=5)


def search_web(query: str):
    """Search the web using Tavily."""
    results = search_tool.invoke({
        "query": query
    })

    return results