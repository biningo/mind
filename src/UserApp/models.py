
from django.db import models

# Create your models here.
from django.db.models import F

from Blog2.Utils.RedisUtil import getRedisClient


class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64,null=False,blank=True,verbose_name='昵称')#默认是邮箱
    password = models.CharField(max_length=6,null=False,blank=False,verbose_name='密码')
    email = models.EmailField(unique=True,null=False,blank=False,verbose_name='邮箱')#唯一
    access_count = models.IntegerField(default=0, verbose_name='访问本站次数')
    created_time = models.DateField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return self.email


    @staticmethod
    def Check_Captcha_Access(email,captcha):
        r = getRedisClient()
        print(captcha == r.get("captcha"))
        if captcha == r.get("captcha"):
            user = UserAccount.objects.filter(email=email)
            if user.count==0:
                user = UserAccount()
                user.email = email
                user.username = email
                user.password=666666
                user.save()
                return user
            else:
                user.update(access_count=F('access_count')+1)
                user = user[0]
                return user
        else:
            return None


        





#用uuid来区分
class StrangeUser(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100,verbose_name='陌生用户的ip')
    access_count = models.IntegerField(default=0,verbose_name='访问本站次数')

    def __str__(self):
        return self.uid







