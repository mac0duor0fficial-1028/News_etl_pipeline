from airflow.decorators import dag, task
from datetime import datetime, timedelta
from scripts.news_extract import fetch_news
from scripts.news_transform import transform_news
from scripts.news_load import load_news
from scripts.init_db import init_db
import sys
import os

sys.path.insert(0, '/opt/airflow/scripts')

default_args = {
    "owner": "Macphalen Oduor",
    "depends_on_past": False,
    "start_date": datetime(2026, 5, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    schedule_interval="@daily",
    default_args=default_args,
    description="ETL pipeline for News API data using TaskFlow API",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["news", "etl", "pipeline"]
)
def news_pipeline():
    
    @task
    def extract():
        return fetch_news()
    
    @task
    def transform(extracted_articles):
        return transform_news(extracted_articles)
    
    @task
    def load(transformed_articles):
        load_news(transformed_articles)

    extracted_articles = extract()
    transformed_articles = transform(extracted_articles)
    load_articles = load(transformed_articles)

    extracted_articles >> transformed_articles >> load_articles