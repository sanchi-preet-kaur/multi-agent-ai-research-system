
def supervisor_agent(state):
    print("\n🎯 Supervisor is deciding the next step...")

    if not state.get("search_results"):
        next_action = "research"

    elif not state.get("final_report"):
        next_action = "analyze"

    elif not state.get("fact_check_done", False):
        next_action = "fact_check"

    else:
        next_action = "finish"

    print(f"Supervisor decision: {next_action}")

    return {"next_action": next_action}
