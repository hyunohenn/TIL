"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views  # 명시해서 사용한다

urlpatterns = [
    # path('test/', views.test)  # 뭐라고 request가 왔을 때, views로 뭘 해! 함수를 출력하는 것이 아니고, 알아서 특정 시점에 사용된다
    path('articles/', include('articles.urls')),
]
