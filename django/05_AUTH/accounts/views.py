from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm  # ModelForm이 아니다 어떠한 model과도 연결되어 있지 않음
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# 모델을 만들어 사용하는건 똑같은데 user만큼은 프로젝트 당 하나만 고정되야 하므로(유지보수를 위해) 이렇게 관리
# settings에 한번만 등록/ 관리하면 돼
from django.contrib.auth import get_user_model  # accounts.User을 가져옴 (settings에 쓰여져 있는) 
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

# R => 전체 목록 / 단일 조회 (/articles/1/)
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {'user_profile': user_profile}

    """
    request.user => /profile/<username>/ 으로 요청을 보낸 사람
    user_profile => /profile/<usernema>/ 에서 username에 해당하는 사람
    둘이 같을 때, update 로직(form, valid등..)이 실행됨 / 그게 아니라면 단순 조회 페이지
    """

    if request.user == user_profile:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', username=user_profile.username)
        else:
            form = CustomUserChangeForm(instance=user_profile)

        context['form'] = form

    return render(request, 'accounts/profile.html', context) 
    
@login_required
def change_password(request):  # 비밀번호 변경
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', form.user.username)
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form, }
    return render(request, 'accounts/change_password.html', context)
        

def signup(request):
    # anonymous user가 아니라면 == login한 사용자라면
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 검증 없이 바로 로그인
            return redirect('accounts:profile', username=user.username)
    
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }

    return render(request, 'accounts/signup.html', context)


def login(request):
    # login 검증 / HTML 만드는 forms.Form을 써서 완료
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # 설계가 이래
        if form.is_valid():  # 아마 DB에서 필터링해서 가져올 것
            # 로그인을 시켜야 하는데..
            auth_login(request, form.get_user())  # 사용자 객체가 튀어나왔을 것
            next_url = request.GET.get('next')  # value / None (딕셔너리 이므로)
            return redirect(next_url or 'articles:index')
            
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):  # 팔찌떼기, 팔지에 써있는 말을 DB에서 삭제 2가지 일을 함
    # logout()
    auth_logout(request)
    return redirect('articles:index')

@login_required
def withdraw(request):
    request.user.delete()  # 팔찌를 차고 있는 사람을 삭제한다 =
    auth_logout(request)  # cookie(팔찌) 회수 + session 테이블에서 레코드 삭제
    return redirect('articles:index')



