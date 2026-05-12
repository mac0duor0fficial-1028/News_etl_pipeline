import pandas as pd
from textblob import TextBlob

def transform_articles(extracted_articles):

    df_articles = pd.DataFrame(extracted_articles)

    # Select and rename columns
    df_articles = df_articles.rename(columns={
        "source": "source_name",
        "publishedAt": "published_at"
    })
        
    # Convert published_at to datetime
    df_articles["published_at"] = pd.to_datetime(df_articles["published_at"])
    
    # Handle missing values
    df_articles.isnull().sum()

    # Removing rows where all values are null
    df_articles = df_articles.dropna(how='all')

    # Drop duplicates based on URL
    df_articles = df_articles.drop_duplicates(subset=["url"])

    # Enriching Dataset by adding sentiment score attribute using TextBlob
    df_articles["sentiment_score"] = df_articles["content"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    return df_articles  