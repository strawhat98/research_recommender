from sentence_transformers import SentenceTransformer
from zenml import step
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

@step
def generate_embeddings(papers: list) -> list:
    texts = [paper["summary"] for paper in papers]
    embeddings = model.encode(texts)
    # Add embedding back into each paper dict
    for paper, emb in zip(papers, embeddings):
        paper["embedding"] = emb.tolist()  # Convert to list for JSON compatibility if needed
    return papers
