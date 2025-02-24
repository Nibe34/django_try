from django.shortcuts import render
from .models import Article

def news_home(request):
    news = Article.objects.order_by('-date')[:5]
    return render(request, 'news/news_home.html', {'news' : news})

# Create your views here.
