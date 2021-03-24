from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 상속을 받았기 때문에
    # username, password, is_activem is_staff ....etc columns
    address = models.CharField(max_length=100)
    

