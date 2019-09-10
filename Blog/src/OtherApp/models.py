from django.db import models

# Create your models here.
class FriendLink(models.Model):  #友链
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    friendUrl = models.CharField(max_length=400)


#公告
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500,verbose_name='公告')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='通知时间')

    @staticmethod
    def get_notices(count:int): #返回notice list
        notice_list = Notice.objects.all().order_by('-created_time')[:count] #越界不会出错
        return notice_list

#广播
class BroadCast(models.Model):
    id  = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)


#留言
class Note(models.Model):

    PUBLIC = 1   #公开普通留言
    PRIVATE = 0  #私信
    SUGGEST = 2  #建议
    NOTE_TYPE = (
        (PUBLIC,'公开留言'),
        (PRIVATE,'私信'),
        (SUGGEST,'建议')
    )


    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    user = models.ForeignKey('UserApp.UserAccount',on_delete=models.DO_NOTHING,verbose_name='用户')
    father = models.ForeignKey('Note',on_delete=models.DO_NOTHING,default=None,null=True,verbose_name='回复留言的id')
    type = models.PositiveIntegerField(default=PUBLIC,choices=NOTE_TYPE,null=True,verbose_name='留言类型')

