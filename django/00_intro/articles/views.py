from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is articles/index')


# 00_django_workshop
# articles/mail/ => 화면에 내 메일주소가 나오게(HTML 아니여도 됨!)

def mail(request):
    return HttpResponse('hyun.ohenn@gmail.com')