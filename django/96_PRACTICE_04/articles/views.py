from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from . models import Article, Comment
from . forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        user = request.user
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)
    

def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', article_pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index') 

@login_required
@require_http_methods(['POST', 'GET'])
def create_comment(request, article_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = request.user
        article = get_object_or_404(Article, pk=article_pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.article = article
            comment.save()
            return redirect('articles:article_detail', article_pk=article.pk)
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/detail.html', context)
    
@require_POST  
def delete_comment(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:article_detail', article_pk=article_pk)
