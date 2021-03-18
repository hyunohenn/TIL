from django.db import models
# 아래와 같은 패키지 깔아서 작동하게 할 수 있음
# from imagekit.models import ProcessedImageField
# from imagekit.processors import Thumbnail

class Article(models .Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)  # black => ORM 이 빈 것을 허용함.(.is_valid()통과) DB는 자동으로 ''가 저장됨
    # image = ProcessedImageField(
    #     upload_to='article/',
    #     blank=True,
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG'
    #     options={'quality': 90},
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
