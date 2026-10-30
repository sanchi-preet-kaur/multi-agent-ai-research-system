from agents.fact_checker import fact_checker_agent

sample_state = {
    "query": "How is Generative AI changing software engineering?",

    "search_results": {
        "results": [
            {
                "title": "Example research source",
                "url": "https://example.com/research",
                "content": "Generative AI can help developers generate code."
            }
        ]
    },

    "final_report": """
    Generative AI can help developers generate code.
    Generative AI has eliminated all software engineering jobs.
    """
}

result = fact_checker_agent(sample_state)

print("\n" + "=" * 50)
print("FACT CHECK RESULTS")
print("=" * 50)

print(result["fact_check"])