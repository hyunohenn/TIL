from django.shortcuts import render

# Create your views here.

#workshop0309/dinner/ => dinner 뷰 함수를 실행
def dinner(request, menu, number):
    context = {
        'menu': menu,
        'number': number,
    }
    return render(request, 'practice0309/dinner.html', context)
