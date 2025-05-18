from zenml.client import Client
from pipelines.daily_recommender import daily_recommender_pipeline
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    Client().initialize()
    daily_recommender_pipeline()