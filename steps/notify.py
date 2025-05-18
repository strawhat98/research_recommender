from zenml import step

@step
def notify_results(recommendations: list):
    print("\nTop Recommendations:\n")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['title']} (Score: {rec['score']:.4f})")
        print(f"URL: {rec['url']}\n")
