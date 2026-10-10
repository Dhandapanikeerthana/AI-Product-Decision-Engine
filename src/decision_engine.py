from langchain_ollama import ChatOllama

from retriever import retrieve
from feature_matcher import identify_feature
from evidence_filter import filter_evidence
from priority_scorer import (
    calculate_priority_score,
    get_priority,
    explain_score
)


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    num_ctx=2048,
    num_predict=256
)


def make_decision(query):

    # Step 1: Identify the feature
    features = identify_feature(query)

    if not features:
        return "No matching feature found."

    feature = features[0]

    # Step 2: Retrieve evidence
    retrieved_evidence = retrieve(query)

    # Step 3: Filter evidence for the feature
    relevant_evidence = filter_evidence(
        retrieved_evidence,
        feature
    )

    # Step 4: Calculate priority
    score, factors = calculate_priority_score(
        relevant_evidence
    )

    priority = get_priority(score)

    # Step 5: Generate score explanation
    score_explanations = explain_score(factors)

    explanation_text = "\n".join(
        f"- {explanation}"
        for explanation in score_explanations
    )

    # Step 6: Prepare evidence for Llama
    evidence_text = "\n\n".join(
        f"Source: {item['source']}\n"
        f"{item['content']}"
        for item in relevant_evidence
    )

    # Step 7: Ask Llama to explain the decision
    prompt = f"""
You are an evidence-based product decision assistant.

The decision engine has already calculated the priority.

Feature:
{feature}

Priority:
{priority}

Priority Score:
{score}

Score Breakdown:
- Customer Impact: {factors["Customer Impact"]}
- Bug Severity: {factors["Bug Severity"]}
- Feature Demand: {factors["Feature Demand"]}
- Previous Decision: {factors["Previous Decision"]}

Score Explanation:
{explanation_text}

Use ONLY the evidence below to explain the decision.

Do not change the priority.
Do not introduce new facts.
Do not make assumptions.

Return exactly this format:

Feature: {feature}

Priority: {priority}

Priority Score: {score}

Score Breakdown:
- Customer Impact: {factors["Customer Impact"]}
- Bug Severity: {factors["Bug Severity"]}
- Feature Demand: {factors["Feature Demand"]}
- Previous Decision: {factors["Previous Decision"]}

Reason:
<short explanation>

Supporting Evidence:
- <evidence point 1>
- <evidence point 2>
- <evidence point 3>

Evidence:

{evidence_text}
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    query = input(
        "Enter your product decision question: "
    )

    result = make_decision(query)

    print("\n--- AI Product Decision ---\n")
    print(result)