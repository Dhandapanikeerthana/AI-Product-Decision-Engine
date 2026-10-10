def identify_feature(query):

    query = query.lower()

    feature_keywords = {

        "Payment Reliability": [
            "payment",
            "payments",
            "transaction",
            "payment failure",
            "payment problem"
        ],

        "Offline Mode": [
            "offline",
            "no internet",
            "internet connection",
            "network connection"
        ],

        "Dark Mode": [
            "dark mode",
            "nighttime",
            "night"
        ],

        "Report Export": [
            "report download",
            "report downloads",
            "download report",
            "download reports",
            "export",
            "report export",
            "csv",
            "pdf"
        ],

        "Mobile Performance": [
            "slow",
            "slow mobile",
            "slow loading",
            "loading",
            "performance",
            "load faster",
            "loading time"
        ],

        "Low-Battery Mode": [
            "battery",
            "battery mode",
            "low battery",
            "background activity"
        ]
    }


    matched_features = []


    for feature, keywords in feature_keywords.items():

        for keyword in keywords:

            if keyword in query:
                matched_features.append(feature)
                break


    return matched_features


if __name__ == "__main__":

    query = input("Enter your question: ")

    features = identify_feature(query)

    print("Query:", query)
    print("Matched Features:", features)