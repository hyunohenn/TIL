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
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # /workshop0308/ => 'workshop0308.urls' | /workshop0308/lotto/ => lotto 추첨 페이지
    path('workshop0308/', include('workshop0308.urls')),

    # /practice0309/ => 'practice0309.urls'
    path('practice0309/', include('practice0309.urls')),

    # /workshop0309/ => 'workshop0309.urls'
    path('workshop0309/', include('workshop0309.urls')),


]
