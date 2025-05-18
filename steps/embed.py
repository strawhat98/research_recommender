from sentence_transformers import SentenceTransformer
from zenml import step

model = SentenceTransformer("all-MiniLM-L6-v2")

@step
def generate_embeddings(papers: list) -> list:
    texts = [paper["summary"] for paper in papers]
    embeddings = model.encode(texts)

    for i, embedding in enumerate(embeddings):
        papers[i]["embedding"] = embedding.tolist()  # Convert to list for JSON-compatibility

    return papers
