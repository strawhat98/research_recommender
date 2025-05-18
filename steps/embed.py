from sentence_transformers import SentenceTransformer
from zenml import step
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

@step
def generate_embeddings(papers: list) -> np.ndarray:
    texts = [paper["summary"] for paper in papers]
    embeddings = model.encode(texts)
    return embeddings
