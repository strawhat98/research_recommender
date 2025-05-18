import streamlit as st
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = "research_papers"
TOP_K = 5

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def fetch_latest_papers(top_k=TOP_K):
    # Fetch the latest papers by search on metadata or just top points (simple approach)
    results = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=top_k
    )
    return results.points

def recommend_similar_to_paper(paper_id, top_k=TOP_K):
    point = client.retrieve(
        collection_name=COLLECTION_NAME,
        ids=[paper_id]
    )
    if not point or not point[0].vector:
        return []
    query_vector = point[0].vector
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k,
        with_payload=True
    )
    return hits

st.title("Research Paper Recommender")

papers = fetch_latest_papers()

st.header("Latest Papers")
for p in papers:
    st.markdown(f"### {p.payload['title']}")
    st.write(p.payload['summary'])
    st.write(f"[Read more]({p.payload['url']})")

selected_paper_id = st.selectbox("Select a paper to find similar recommendations", [p.id for p in papers])

if st.button("Show Recommendations"):
    recommendations = recommend_similar_to_paper(selected_paper_id)
    st.header("Recommended Similar Papers")
    for rec in recommendations:
        st.markdown(f"#### {rec.payload['title']} (Score: {rec.score:.4f})")
        st.write(rec.payload['summary'])
        st.write(f"[Read more]({rec.payload['url']})")
