from django.db import models

class Article(models.Model):
    # ORM 은 models.py 내부의 class 에서, class var 만 확인하여 DB의 Column으로 만든다.
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} => {self.title}'
