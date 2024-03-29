# Generated by Django 2.2.2 on 2019-06-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='博文标题', max_length=50)),
                ('data', models.DateField(default='2000/00/00')),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='正文')),
            ],
        ),
    ]
