from zenml import step
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import os

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = "research_papers"

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

@step
def update_qdrant(papers: list, embeddings):
    points = []
    for idx, (paper, embedding) in enumerate(zip(papers, embeddings)):
        point = PointStruct(
            id=idx,
            vector=embedding.tolist(),
            payload={
                "title": paper["title"],
                "summary": paper["summary"],
                "url": paper["url"]
            }
        )
        points.append(point)
    
    if COLLECTION_NAME not in client.get_collections().collections:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vector_size=len(embeddings[0]),
            distance="Cosine"
        )
    
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
