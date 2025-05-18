Here’s the full `README.md` file content ready to add directly to your repo. You can copy this markdown text into a file named `README.md`:

````markdown
# 🧠 Research Recommender

<p>
  <img src="https://blog.zenml.io/assets/logo_sq.png" alt="ZenML Badge"/>
  <img src="https://seeklogo.com/images/Q/qdrant-icon-logo-843D18553D-seeklogo.com.png"/>
</p>

> An automated pipeline that fetches the latest open-access Machine Learning research papers daily from arXiv, generates embeddings, stores them in a vector database, and recommends similar papers.

---

## 🗂 Project Structure

```bash
research_recommender/
│
├── Dockerfile.qdrant              # For deploying Qdrant container (for Railway or local use)
├── docker-compose.yml             # Run Qdrant locally
├── requirements.txt               # Python dependencies
├── run_pipeline.py                # Entry point to trigger ZenML pipeline
├── streamlit_app.py               # Optional Streamlit UI
│
├── .zenml/
│   └── schedules/
│       └── cron_schedule.yaml     # ZenML schedule config (optional)
│
├── pipelines/
│   └── daily_recommender.py       # Orchestration pipeline
│
├── steps/
│   ├── ingest.py                  # Arxiv paper fetcher
│   ├── embed.py                   # Embedding generator
│   ├── update_vector_db.py        # Push to Qdrant
│   ├── recommend.py               # Recommend similar papers
│   └── notify.py                  # Print or alert top picks
````

---

## ⚙️ Features

* ⏰ **Scheduled ingestion** of new arXiv ML papers
* 🧠 **Embeddings** using SentenceTransformers
* 📦 **Vector storage** using Qdrant (open-source)
* 🔍 **Content-based recommendations**
* 🎨 **Streamlit UI** for interaction

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/strawhat/research_recommender.git
cd research_recommender
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

---

### 🛠️ Running Locally

Start Qdrant locally:

```bash
docker-compose up
```

Trigger the pipeline:

```bash
python run_pipeline.py
```

---

### 💻 Launch Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📌 Tech Stack

| Tool                     | Purpose                       |
| ------------------------ | ----------------------------- |
| **ZenML**                | ML pipeline orchestration     |
| **Qdrant**               | Vector DB for semantic search |
| **arXiv API**            | Fetching ML research papers   |
| **SentenceTransformers** | Embedding generation          |
| **Streamlit**            | Web app / frontend UI         |

---

## 🧪 Sample Output

```json
[
  {
    "title": "A Transformer-based Approach to Continual Learning",
    "summary": "This paper proposes...",
    "url": "https://arxiv.org/abs/xxxx.xxxxx"
  }
]
```

---

## 🧠 Future Work

* ✅ Add user personalization
* ✅ Deploy to free cloud platforms (Railway, Render)
* ✅ Email / Discord / Slack notifications
* 🕐 Save reading history

---

## 🙌 Contributions

Feel free to fork and submit PRs or raise issues!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ✉️ Contact

* GitHub: [@strawhat](https://github.com/strawhat)
* Email: [arkdeepsengupta@gmail.com](mailto:your.email@example.com)

