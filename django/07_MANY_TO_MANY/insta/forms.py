# insta forms.py

from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', )


class CommentForm(forms.ModelForm):
    # Form => HTML 만들기, 데이터 검증하기
    # fields에 없는 속성은, HTML X & validation x

    # wow 라는 이름의 input tag => 원래 안나옴
    # 넘어온 데이터는 검증함 => 당연
    # 넘어온 데이터 검증 0, DB에 들어갈 곳 없음..
    # wow = forms.CharField(min_length=2, max_length=100)
    
    # content 라는 이름의 input tag => 원래 나옴
    # 넘어온 데이터의 최대/최소 길이 추가 검증 => 원래 안함
    # 이름 맞는 컬럼이 있음 => DB에 들어감 
    content = forms.CharField(min_length=1, max_length=100)

    class Meta:
        model = Comment
        fields = ('content', )