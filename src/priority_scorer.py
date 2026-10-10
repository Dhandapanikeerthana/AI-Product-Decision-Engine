def calculate_priority_score(evidence):

    factors = {
        "Customer Impact": 0,
        "Bug Severity": 0,
        "Feature Demand": 0,
        "Previous Decision": 0
    }

    for item in evidence:

        source = item["source"]
        content = item["content"].lower()

        # Customer feedback
        if source == "customer_feedback.txt":
            factors["Customer Impact"] += 2

        # Bug reports
        elif source == "bug_reports.txt":
            factors["Bug Severity"] += 3

        # Feature requests
        elif source == "feature_requests.txt":
            factors["Feature Demand"] += 1

        # Previous product decisions
        elif source == "previous_decisions.txt":

            if "high-priority" in content:
                factors["Previous Decision"] += 5

            elif "low-priority" in content:
                factors["Previous Decision"] -= 2

            elif "planned" in content:
                factors["Previous Decision"] += 3

            elif "discussed" in content:
                factors["Previous Decision"] += 3

            elif "postponed" in content:
                factors["Previous Decision"] += 2

            elif "not been evaluated" in content:
                factors["Previous Decision"] += 0

    # Calculate total score
    score = sum(factors.values())

    return score, factors


def get_priority(score):

    if score >= 7:
        return "HIGH"

    elif score >= 4:
        return "MEDIUM"

    else:
        return "LOW"


def explain_score(factors):

    explanations = []

    if factors["Customer Impact"] > 0:
        explanations.append(
            "Customer feedback shows that users are affected by this problem."
        )

    if factors["Bug Severity"] > 0:
        explanations.append(
            "Bug reports indicate that the problem has technical impact."
        )

    if factors["Feature Demand"] > 0:
        explanations.append(
            "Feature requests show direct demand for this functionality."
        )

    if factors["Previous Decision"] > 0:
        explanations.append(
            "Previous product decisions provide additional evidence supporting the feature."
        )

    elif factors["Previous Decision"] < 0:
        explanations.append(
            "Previous product decisions indicate that this feature was considered lower priority."
        )

    if not explanations:
        explanations.append(
            "There is currently limited evidence supporting this feature."
        )

    return explanations


if __name__ == "__main__":

    print("Priority scorer is ready.")