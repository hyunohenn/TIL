from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from . models import User  # 직접참조
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    # little customize
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'  # 이러면 다 나와 안돼
        fields = ('username', )  # pw는 암호화 해서 관리해야 하기 때문에 따로


class CustomUserChangeForm(UserChangeForm):
    address = forms.CharField(min_length=3, max_length=200)
    first_name = forms.CharField(min_length=1, max_length=100)
    last_name = forms.CharField(min_length=1, max_length=100)
    email = forms.EmailField(min_length=1)
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'address', 'email', )