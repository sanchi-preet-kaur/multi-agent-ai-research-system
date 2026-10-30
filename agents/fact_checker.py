import json
from utils.llm import llm


def fact_checker_agent(state):
    print("\n🔍 Fact Checker Agent is working...")

    query = state["query"]
    results = state["search_results"]
    report = state["final_report"]

    prompt = f"""
    You are a strict fact-checking agent.

    Research question:
    {query}

    Original web search results:
    {json.dumps(results, ensure_ascii=False)}

    Research report:
    {report}

    Your tasks:
    1. Check important factual claims against the search results.
    2. Identify unsupported claims.
    3. Check whether cited URLs appear in the search results.
    4. Do not treat a claim as verified merely because the report states it.
    5. Do not introduce new sources or facts.
    6. If evidence is insufficient, clearly say so.

    Return your findings in this structure:

    VERIFIED CLAIMS:
    - ...

    UNSUPPORTED CLAIMS:
    - ...

    SOURCE ISSUES:
    - ...

    RECOMMENDATIONS:
    - ...
    """

    response = llm.invoke(prompt)

    fact_check = response.content

    print("\nFact checking completed!")

    return {
       "fact_check": fact_check,
       "fact_check_done": True
}