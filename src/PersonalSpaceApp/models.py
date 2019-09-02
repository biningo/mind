from django.db import models

# Create your models here.
class Mood(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True)


