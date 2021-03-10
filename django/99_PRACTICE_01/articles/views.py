from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Articles.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Articles()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect('detail', pk=article.id)