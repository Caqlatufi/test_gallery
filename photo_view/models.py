from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='默认的描述', max_length = 100)
    image = models.ImageField(default='default.png', upload_to='images/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(default='作品标题', max_length = 50)

    def __str__(self):
        return self.title
