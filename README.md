# Multi-Agent AI Research & Analysis System

An AI-powered research system built using **LangChain, LangGraph, Groq, and Tavily**. It uses multiple specialized agents to search the web, analyze information, and fact-check generated research reports.

## Project Overview

The system automates the research process through a coordinated multi-agent workflow. Each agent performs a specific task, while a Supervisor Agent manages the execution flow.

## Architecture

```text
User Research Query
        |
        v
  Supervisor Agent
        |
        v
  Research Agent
   (Tavily Search)
        |
        v
  Analysis Agent
    (Groq LLM)
        |
        v
 Fact Checker Agent
    (Groq LLM)
        |
        v
 Final Research Report
```

## Features

- **Web Research:** Retrieves relevant information using Tavily Search.
- **AI-Powered Analysis:** Uses Groq LLM to analyze search results and generate structured reports.
- **Fact Checking:** Checks important report claims against the original search results.
- **Workflow Orchestration:** Uses LangGraph to coordinate agents and control execution.
- **Modular Architecture:** Separates agents, tools, graph workflow, and utility modules.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration |
| LangGraph | Multi-agent workflow orchestration |
| Groq | LLM inference |
| Tavily | Web search |
| Pydantic | Data validation |
| python-dotenv | Environment variable management |

## Project Structure

```text
multi_agent_research/
│
├── agents/
│   ├── __init__.py
│   ├── researcher.py
│   ├── analyst.py
│   ├── supervisor.py
│   └── fact_checker.py
│
├── tools/
│   ├── __init__.py
│   └── search_tool.py
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   └── workflow.py
│
├── utils/
│   ├── __init__.py
│   └── llm.py
│
├── .env
├── .gitignore
├── requirements.txt
├── test_connection.py
├── test_fact_checker.py
└── test_graph.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd multi_agent_research
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Get API keys from:

- [Groq Console](https://console.groq.com/)
- [Tavily](https://tavily.com/)

**Important:** Never upload your `.env` file or expose API keys publicly.

### 6. Run the project

```bash
python test_graph.py
```

## Workflow

1. The Supervisor Agent receives the research query and determines the next workflow step.
2. The Research Agent searches the web using Tavily.
3. The Analysis Agent processes the retrieved information using Groq.
4. The Fact Checker Agent evaluates claims against the original search results.
5. The Supervisor detects completion and terminates the workflow.

## Future Enhancements

- Report Generator Agent
- Improved source and URL verification
- Critic and revision agents
- Persistent research history
- Error handling and logging
- Evaluation of research quality

## Current Limitations

- Fact-checking depends on the quality and coverage of retrieved search results.
- LLM-generated reports may contain unsupported claims.
- Search results do not guarantee comprehensive coverage of a research topic.

## Author

Developed as a Generative AI and multi-agent systems project.