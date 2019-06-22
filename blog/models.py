from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(default ='博文标题', max_length=50)
    data = models.DateField(default ='2000/00/00', auto_now=False, auto_now_add=False)#上传日期
    image = models.ImageField(default ='default.png', upload_to='images/', height_field=None, width_field=None, max_length=None)
    text = models.TextField(default ='正文')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:60] + '......'