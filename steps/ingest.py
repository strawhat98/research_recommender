import arxiv
from zenml import step

@step
def fetch_papers():
    search = arxiv.Search(
        query="machine learning",
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id
        })
    return papers