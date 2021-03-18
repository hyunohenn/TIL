from django.urls import path
from . import views

app_name = 'uploader'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:article_pk>/detail', views.detail, name='detail'),
]
