from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


def profile(request, username):
    me = request.user # 보려는 사람
    you - get_object_or_404(User, username=username)  # 보고자 하는 대상
    
    # 만약 차단 테이블을 만들어 뒀다면,
    if you.haters.filter(pk=me.)


# /accounts/<str:username>/follow/
def follow(request, username):
    # user_id, article_id
    # Create / Delete
    fan = request.user  # follow 요청 보낸 사람
    star = get_object_or_404(User, username=username)  # follow 요청 받는 사람

    if fan.is_authenticated:
        # 인증된 사용자가 좋아요를 눌렀다면, 지운다
        if fan.stars.filter(pk=star.pk).exists():
            fan.stars.remove(star)
        else:
            fan.stars.add(star)
    
    return redirect('accounts:profile', star.pk)


