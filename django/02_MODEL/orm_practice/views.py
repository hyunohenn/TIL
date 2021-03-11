from django.shortcuts import render, redirect
from . models import Student

# Creat (생성)
## HTML 제공
## 바로 아래 구간에서는 HTML을 주는 것에 그친다
def new(request):
    return render(request, 'orm_practice/new.html')

## 실제 저장
def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        # redirect(RAW URL/ urls.py 의 name)
        return redirect('detail', pk=student.pk)  # 넘겨줄때 인자가 필요하므로
    return redirect('new')

# Retrieve / Read (조회)
## 여러개 조회
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request,'orm_practice/index.html', context)

## 단일 조회
def detail(request, pk):
    student = Student.objects.get(id=pk)
    context= {'student': student}
    return render(request,'orm_practice/detail.html', context)


# update
## 수정용 HTML 제공
def edit(request, pk):
    student = Student.objects.get(pk=pk)  # 기존의 내용을 보여주어야 함
    context = {'student': student}
    return render(request, 'orm_practice/edit.html', context)

## 실제 수정
def update(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        return redirect('detail', pk=student.pk)
    return redirect('edit', pk=pk)

# Delete
def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('index')
    return redirect('detail', pk=pk)