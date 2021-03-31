from django.db import models
from faker import Faker

class Person(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def dummy_for(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(name=f.name())
    
    @classmethod
    def dummy_bulk(cls, n):
        f = Faker()
        clss = []
        for _ in range(n):
            clss.append(cls(name=f.name()))
            objects: BaseManager
        cls.objects.bulk_create(clss)


    def __str__(self):
        return f'{self.pk}: {self.name}'


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 원래 하던거 작성
    # 근데 로직에 따라서 이름을 변경하는 것 또한 가능하다
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='written_articles')
    editor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='edited_articles')
    # related_name 을 작성하지 않으면 이름이 겹쳐서 불가능
    likers = models.ManyToManyField(Person, related_name='likes')
    scrapers = models.ManyToManyField(Person, related_name='scraps')
    dislikers = models.ManyToManyField(Person, related_name='dislikes')


    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(title=f.address(), content='hello')

    def __str__(self):
        return f'{self.pk} {self.title}'