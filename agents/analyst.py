import json
from utils.llm import llm


def analyst_agent(state):

    print("\n🧠 Analysis Agent is working...")

    query = state["query"]

    results = state["search_results"]

    prompt = f"""
    You are an expert research analyst.

    Research question:
    {query}

    Web search results:
    {json.dumps(results, ensure_ascii=False)}

    Instructions:
    1. Analyze the information.
    2. Identify the important findings.
    3. Compare information from different sources.
    4. Do not invent facts or sources.
    5. Include source URLs from the provided results.
    6. Mention when evidence is insufficient.

    Prepare a structured report with:
    - Introduction
    - Key Findings
    - Detailed Analysis
    - Conclusion
    - Sources
    """

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }