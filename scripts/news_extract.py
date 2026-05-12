import requests
from configs.config import NEWS_API_KEY

# Provided base url for fetching news articles about Tesla from NewsAPI
url="https://newsapi.org/v2/everything?q=tesla&from=2026-04-12&sortBy=publishedAt&apiKey=NEWS_API_KEY"

def fetch_news():
    response = requests.get(url)
    if response.status_code == 200:
        articles = []
        response = requests.get(url)

        data = response.json()

        # Getting the list of articles from the response
        raw_articles = data.get('articles', [])

        extracted_articles = []
        for article in raw_articles:

            # Extracting relevant fields from each article and storing them in a structured format
            extracted_articles.append({
                'source': article.get('source', {}).get('name', ''),
                'author': article.get('author', ''),
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'image_url': article.get('urlToImage', ''),
                'published_at': article.get('publishedAt', ''),
                'content': article.get('content', '')
            })
        return extracted_articles
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []