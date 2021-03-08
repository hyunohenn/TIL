from django.http.response import HttpResponse  # 확인해보자


def test(request):
    return HttpResponse('hoi')