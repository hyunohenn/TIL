from django.urls import path
from . import views

# app_name = 'practice0309'

# /practice0309/
urlpatterns = [
    # /practice0309/var_route/뭐든지들어옴/
    path('var_route/<int:value>/', views.var_route),
    # /practice0309/lotto/<회차>/
    path('lotto/<int:no>/', views.lotto),

    # /practice0309/ping/  =>  <form> 으로 사용자 입력 받기
    path('ping/', views.ping, name='ping'),
    # /practice0309/pong/  =>  처리 결과 보여주기
    path('pong/', views.pong, name='pong'),
]