from graph.workflow import app_graph


initial_state = {
    "query": "How is Generative AI changing software engineering?"
}

print("\nStarting Multi-Agent Research System...")

result = app_graph.invoke(initial_state)

print("\n" + "=" * 50)
print("FINAL RESEARCH REPORT")
print("=" * 50)

print(result["final_report"])