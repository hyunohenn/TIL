from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def index(request):
    numbers = range(1, 46)
    lotto = random.sample(numbers, 6)
    return HttpResponse(f'Pick: {sorted(lotto)}')


# 00_django_workshop
# articles/mail/ => 화면에 내 메일주소가 나오게(HTML 아니여도 됨!)

def mail(request):
    return HttpResponse('hyun.ohenn@gmail.com')