import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

# Load environment variables
load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), ".env"),
    override=True
)

# Check configuration without exposing secrets
required_vars = ["GROQ_API_KEY", "TAVILY_API_KEY", "GROQ_MODEL"]

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"{var} is missing. Check your .env file.")

print("Environment variables loaded successfully!")

# Initialize Groq
llm = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    temperature=0
)

# Initialize Tavily
search_tool = TavilySearch(max_results=3)

# Test Groq
print("\nTesting Groq...")
response = llm.invoke("Say hello in one sentence.")
print(response.content)

# Test Tavily
print("\nTesting Tavily...")
results = search_tool.invoke({
    "query": "What is LangGraph?"
})

print(results)

print("\nBoth integrations tested!")