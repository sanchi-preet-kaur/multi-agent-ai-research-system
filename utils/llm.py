import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Find the project's root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(ROOT_DIR / ".env")

# Initialize Groq model
llm = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    temperature=0
)