from tools.search_tool import search_web


def researcher_agent(state):

    print("\n🔎 Research Agent is working...")

    query = state["query"]

    results = search_web(query)

    return {
        "search_results": results
    }