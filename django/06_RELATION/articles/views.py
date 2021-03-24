from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from . models import Article, Comment
from . forms import ArticleForm, CommentForm

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/detail.html', request)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article, 
        'commnets': comments,
        'comment_form': comment_form
        }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['POST', 'GET'])
def update(request, article_pk):
    article = get_object_or_404(Article, article_pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, article_pk)
    article.delete()
    return redirect('articles:index')

def create_comment(request, article_pk):
    pass

def delete_comment(request, article_pk, comment_pk):
    pass