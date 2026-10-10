from decision_engine import make_decision


test_queries = [
    "Which feature should we prioritize for payment problems?",
    "Which feature should we prioritize for users with no internet?",
    "Should we prioritize dark mode?",
    "Which feature should we prioritize for report downloads?",
    "Which feature should we prioritize for slow mobile loading?",
    "Should we prioritize low battery mode?"
]


for query in test_queries:

    print("\n" + "=" * 60)
    print("QUESTION:")
    print(query)

    result = make_decision(query)

    print("\nRESULT:")
    print(result)