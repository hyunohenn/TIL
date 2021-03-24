from django import forms
from .models import Article
"""
Why Form?
1. Data Validation
2. HTML easy
"""

# forms.Form => 특정 모델과 연동 X 단순히 데이터 검증/HTML생성용
class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=5)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField(widget=forms.Textarea)  # widget => HTML 생성시 주는 옵션


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(min_length=1)
    class Meta:
        model = Article
        fields = '__all__'
