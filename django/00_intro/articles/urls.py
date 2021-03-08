from django.urls import path
from . import views  # articles 위치

urlpatterns = [
    path('index/', views.index),
    path('mail/', views.mail)
]
