import requests
from .models import Article
from datetime import datetime

def fetch_news():
    api_key = '63a02d6d28784d3794f6c215efb2285c'
    url = f'https://newsapi.org/v2/top-headlines?country=id&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    articles = data.get('articles', [])

    for article in articles:
        title = article['title']
        description = article.get('description', 'No description available')
        url = article['url']
        published_at = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")

        Article.objects.get_or_create(
            title=title,
            description=description,
            url=url,
            published_at=published_at
        )
