from django.shortcuts import render, redirect, get_object_or_404
# dvd h
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from . models import Reservation
from . forms import ReservationForm

# Create your views here.
# new, edit, delete의 핵심 로직은 POST 요청으로 구성

@require_GET
def index(request):
    reservations = Reservation.objects.order_by('-pk')
    context = {'reservations': reservations}
    return render(request, 'board/index.html', context)

# GET, POST 요청에만 응답하겠다. 다른 요청 방식 bad request
@require_http_methods(['GET', 'POST'])  # 405 Method Not Allowed
def new(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)  # form으로 사용자가 제출한 내용을 확인해볼게
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)

    # else: GET, PATCH, PUL, DELETE
    else:
        form = ReservationForm()
    
    context = {'form': form}
    return render(request, 'board/form.html', context)

@require_GET
def detail(request, reservation_pk):
    reservation = get_object_or_404(reservation, pk=reservation_pk)
    context = {'reservation': reservation}
    return render(request, 'board/detail.html', context)

@require_http_methods(['GET', 'POST'])
def edit(request, reservation_pk ):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)  # form으로 사용자가 제출한 내용을 확인해볼게
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)

    # GET 요청 => 사용자한테 
    else:
        form = ReservationForm(instance=reservation)
    
    context = {'form': form}
    return render(request, 'board/form.html', context)

@require_POST
def delete(request, reservation_pk):
    reservation = get_object_or_404(Reservation, pk=reservation_pk)
    reservation = delete()
    return redirect('board:index')