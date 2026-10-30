
from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.supervisor import supervisor_agent
from agents.fact_checker import fact_checker_agent


workflow = StateGraph(ResearchState)

workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("researcher", researcher_agent)
workflow.add_node("analyst", analyst_agent)
workflow.add_node("fact_checker", fact_checker_agent)


def route_next(state):
    return state["next_action"]


workflow.add_edge(START, "supervisor")

workflow.add_conditional_edges(
    "supervisor",
    route_next,
    {
        "research": "researcher",
        "analyze": "analyst",
        "fact_check": "fact_checker",
        "finish": END
    }
)

workflow.add_edge("researcher", "supervisor")
workflow.add_edge("analyst", "supervisor")
workflow.add_edge("fact_checker", "supervisor")


app_graph = workflow.compile()
