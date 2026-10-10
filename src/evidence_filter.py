from retriever import retrieve
from feature_matcher import identify_feature


FEATURE_KEYWORDS = {

    "Payment Reliability": [
        "payment",
        "payments",
        "transaction",
        "failed payment",
        "payment reliability"
    ],

    "Offline Mode": [
        "offline mode",
        "offline",
        "without an internet connection",
        "internet connection while travelling"
    ],

    "Dark Mode": [
        "dark mode",
        "nighttime",
        "at night"
    ],

    "Report Export": [
        "report export",
        "export option",
        "download reports",
        "download report",
        "csv",
        "pdf"
    ],

    "Mobile Performance": [
        "load faster on mobile",
        "mobile application performance",
        "loading time",
        "slow loading",
        "large datasets"
    ],

    "Low-Battery Mode": [
        "low-battery mode",
        "low battery mode",
        "battery",
        "background activity"
    ]
}


def filter_evidence(evidence, feature):

    relevant_evidence = []

    keywords = FEATURE_KEYWORDS.get(feature, [])

    for item in evidence:

        content = item["content"].lower()

        for keyword in keywords:

            if keyword in content:
                relevant_evidence.append(item)
                break

    return relevant_evidence


if __name__ == "__main__":

    query = "Which feature should we prioritize for payment problems?"

    features = identify_feature(query)

    if not features:
        print("No matching feature found.")

    else:

        feature = features[0]

        evidence = retrieve(query)

        relevant_evidence = filter_evidence(
            evidence,
            feature
        )

        print("\nFeature:", feature)

        print("\nRelevant Evidence:\n")

        for item in relevant_evidence:

            print("Source:", item["source"])
            print(item["content"])
            print()