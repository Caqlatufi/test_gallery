from django.db import models

# Create your models here.


class Gallery(models.Model):
    #限制字数
    desciption = models.CharField(max_length = 100)