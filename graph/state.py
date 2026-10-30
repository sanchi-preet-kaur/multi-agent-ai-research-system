
from typing import TypedDict


class ResearchState(TypedDict, total=False):
    query: str
    search_results: dict
    final_report: str
    next_action: str
    fact_check: str
    fact_check_done: bool
