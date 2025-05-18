from zenml import pipeline
from steps.ingest import fetch_papers
from steps.embed import generate_embeddings
from steps.update_vector_db import update_qdrant
from steps.recommend import recommend_similar_papers
from steps.notify import notify_results

@pipeline(name="daily_recommender_pipeline")
def daily_recommender_pipeline():
    papers = fetch_papers()
    embeddings = generate_embeddings(papers)
    update_qdrant(papers, embeddings)

    enriched_papers = [
        {**paper, "embedding": embedding.tolist()}
        for paper, embedding in zip(papers, embeddings)
    ]

    recommendations = recommend_similar_papers(enriched_papers)
    notify_results(recommendations)
