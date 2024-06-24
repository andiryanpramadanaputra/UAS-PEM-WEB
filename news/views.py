from django.shortcuts import render
from .models import Article
from .utils import fetch_news

def home(request):
    fetch_news()
    articles = Article.objects.all()
    return render(request, 'news/home.html', {'articles': articles})

def about(request):
    return render(request, 'news/about.html')
