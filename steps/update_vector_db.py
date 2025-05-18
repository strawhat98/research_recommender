from zenml import step
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import uuid
import os

COLLECTION_NAME = "research_papers"

qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
client = QdrantClient(url=qdrant_url)

@step
def update_qdrant(papers: list):
    client = QdrantClient(url=qdrant_url)

    if COLLECTION_NAME not in [col.name for col in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=len(papers[0]['embedding']), distance=Distance.COSINE),
        )

    points = []
    for paper in papers:
        point_id = str(uuid.uuid4())
        embedding = paper.get("embedding")
        payload = {
            "title": paper["title"],
            "summary": paper["summary"],
            "url": paper["url"],
        }
        points.append(PointStruct(id=point_id, vector=embedding, payload=payload))

    client.upsert(collection_name=COLLECTION_NAME, points=points)