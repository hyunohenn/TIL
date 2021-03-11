from django.urls import path
from . import views

# practice/
urlpatterns = [
    # practice/'' => 목록 보여주기 HTML(전체 조회)
    path('', views.index, name='index' ),
    # practice/1/ => 1번 학생 정보 보여주기 HTML(단일 조회)
    path('<int:pk>/', views.detail, name='detail'),

    # 기존의 데이터를 다루는 것이 아니라 이렇게만 해도 됨
    # practice/new/ => 새로운 데이터 입력용 HTML(생성 준비단계)
    path('new/', views.new, name='new'),
    # practice/create/ => 사용자 입쳑력 데이터 처리
    path('create/', views.create, name='create'),

    
    # 일종의 레거시이므로 특정한 데이터를 지정해주어야 한다
    # practice/1/edit/ => 기존의 데이터를 수정할 HTML
    path('<int:pk>/edit/', views.edit, name='edit'), 
    # practice/1/update/ => 사용자 입력 데이터 처리
    path('<int:pk>/update/', views.update, name='update'),
    
    # practice/1/delete/ => 데이터 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]
