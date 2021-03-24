from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ContactForm, ArticleForm

"""
1. 사용자가 /crud/contact/ 로 접속 => GET /crud/contact/
2. 사용자가 HTML > form 에서 데이터 제출 => POST /crud/contact/
3. view 함수에서 contact 로 redirect 시킴 => GET /crud/contact/
""" 
def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'articles/contact.html', context)
    elif request.method == 'POST':
        contact_form = ContactForm(request.POST)  # {name: 'dsklfj', email: 'aslkdjfl', content: 'asdfkjl'}
        print(contact_form.is_valid())
        print(contact_form.errors)
        return redirect('articles:contact')

@login_required  # not logged_in 일 경우에 무작정 '/accounts/login/'으로 redirect한다.
@require_http_methods(['GET', 'POST'])
def new(request):
    # 사용자 요청이 GET일 경우
    if request.method == 'GET':
        # 비어있는 새로운 form 생성
        form = ArticleForm()
        context = {'form': form}
        # HTML 에 form 실어서 전송
        return render(request, 'articles/new.html', context)
    
    # 사용자 요청이 POST일 경우
    elif request.method == 'POST':
        # form 에 요청 DATA 를 입력
        print(request.POST)
        form = ArticleForm(request.POST)
        # form 을 통해 DATA 유효성검사(validation)
        if form.is_valid():
            # 유효하다면, 저장
            article = form.save()
            # 저장한 article 의 상세보기 페이지로 redirect
            return redirect('articles:detail', article_pk=article.pk)
        else:
            # 유효하지 않다면, 기존의 잘못된 DATA 를 담은 form(L34)을 담고
            context = {'form': form}
            # HTML 에 실어서 전송
            return render(request, 'articles/new.html', context)


def xx(request):
    if request.method == 'POST':
        pass


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        # new 와 다르게, 특정 article 에 대한 내용을 request.POST 로 덮어 쓰기.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        # 기존 게시글 내용을 포함한 HTML 을 만들기 위해 instance 추가
        form = ArticleForm(instance=article)
    
    context = {'form': form}
    return render(request, 'articles/edit.html', context)


def delete(request, article_pk):
    return redirect()
    