from zenml import step
from qdrant_client import QdrantClient
import os

COLLECTION_NAME = "research_papers"
TOP_K = 5

qdrant_url = os.getenv("QDRANT_URL")
client = QdrantClient(url=qdrant_url)

@step
def recommend_similar_papers(papers: list):
    # For simplicity, recommend based on the latest paper's embedding
    print(client)
    latest_paper = papers[-1]
    query_vector = latest_paper.get("embedding")
    if query_vector is None:
        raise ValueError("Latest paper must contain an 'embedding' key.")

    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=TOP_K
    )
    
    recommendations = []
    for hit in hits:
        rec = {
            "title": hit.payload.get("title"),
            "summary": hit.payload.get("summary"),
            "url": hit.payload.get("url"),
            "score": hit.score
        }
        recommendations.append(rec)
    return recommendations
