# accounts.models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 위 아래의 두가지 코드는 완전히 같은 것이다. 
    # from_user_id / to_user_id는 여기서는 의미가 없다. 변수명에 따라 고정값으로 일관적으로 사용
    # fans = models.ManyToManyField('self', symmetric=False, related_name='starts')  # 이렇게 쓰는 것은 django3에서 처음 나옴
    # starts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='fans') => 추가 데이터 없을 때
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars', through='Relationship')

    def __str__(self):
        return f'{self.pk}: {self.username}'


# class Gallery(model.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
#     imgae = models.ImageField()


class Relationship(models.Model):
    star = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fan')
    fan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='star')
    # 추가 데이터가 필요하지 않다면, 만들 Relationship 모델 자체가 존재 이유 x
    created_at = models.DateTimeField(auto_now_add=True)
    follow_reason = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'fan: {self.fan} => star: {self.star}'