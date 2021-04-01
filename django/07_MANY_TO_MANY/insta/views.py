# insta/view.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# /insta/<int:article_pk>/like
def like(request, article_pk):
    # user_id, article_id
    # Create / Delete
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    if user.is_authenticated:
        # 인증된 사용자가 좋아요를 눌렀다면, 지운다
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
        else:
            article.like_users.add(user)
    
    return redirect('insta:article_detail', article.pk)