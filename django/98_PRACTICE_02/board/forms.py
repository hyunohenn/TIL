from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    # # 만일 각각 쓴다면 아래와 같이
    # name = forms.CharField(min_length=2)
    # number = forms.IntegerField(min_value=0, max_value=4, required=False, label="제목", widget=forms.TextInput(attrs={
    #     'class': 'form-control'  # 완전 부트스트랩
    # }))
    # widget 필요한걸 찾아서 쓴다

        
    class Meta:
        model = Reservation
        fields = "__all__"



    