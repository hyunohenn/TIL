from django.shortcuts import render, redirect
from . models import Student

# Retrieve / Read (조회)
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request,'orm_practice/index.html', context)


def detail(request, pk):
    student = Student.objects.get(id=pk)
    context= {'student': student}
    return render(request,'orm_practice/detail.html', context)


# Creat (생성)
# 바로 아래 구간에서는 HTML을 주는 것에 그친다
def new(request):
    return render(request, 'orm_practice/new.html')


def create(request):
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.hobby = request.GET.get('hobby')
    student.save()
    # redirect(RAW URL/ urls.py 의 name)
    return redirect('detail', pk=student.pk)  # 넘겨줄때 인자가 필요하므로