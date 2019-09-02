from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,verbose_name='标题')
    summary = models.CharField(max_length=300,verbose_name='概要',default=" ")
    content_makedown = models.TextField(verbose_name='makedown内容')
    content_html = models.TextField(verbose_name='翻译成html的内容')
    copyright = models.BooleanField(default=True,verbose_name='原创/转载') #是否原创
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间') #每次被储存就更新时间

    access_count = models.IntegerField(default=0,verbose_name='总访问量') #总访问量
    like_count = models.IntegerField(default=0,verbose_name='喜欢数')  #喜欢数

    topic =  models.ForeignKey('SpecialTopic',on_delete=models.DO_NOTHING,verbose_name='专题',null=True,default=None)
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING,verbose_name='文章类型')
    tags = models.ManyToManyField('Tag',verbose_name='标签')



    def get_absolute_url(self):
        year = self.created_time.strftime('%Y')
        month = self.created_time.strftime('%m')

        return reverse('article:detail',args=[year,month,self.id])

    @staticmethod
    def get_article(year,month,id=None):
        if id:
            return Article.objects.filter(id=id)
        else:
           return Article.objects.filter(created_time__year=year,created_time__month=month)
    @staticmethod
    def article_list(article_list,range:int,page:int): #range每页几条数据

        paginator = Paginator(article_list,range)  #每页五条
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages) #最后一页

        return articles

    def __str__(self):
        return self.title





class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)  #删除一个标签不应该把对应文章删除

    def __str__(self):
        return self.name

#专栏
class SpecialTopic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    access_count = models.IntegerField(default=0,verbose_name='访问数量')
    like_account = models.IntegerField(default=0,verbose_name='点赞')
    summary = models.CharField(max_length=1000,verbose_name='专题介绍')



    def __str__(self):
       return self.name



class ArticleComment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000,null=False,blank=False)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='评论文章',null=True)
    father_comment = models.ForeignKey('ArticleComment',on_delete=models.DO_NOTHING, null=True,default=None,verbose_name='回复') #为nul则不是对评论的回复 这是是自引用外键
    user = models.ForeignKey('UserApp.UserAccount',on_delete=models.DO_NOTHING,verbose_name='用户')







#文章上传图片处理
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    ImageFile = models.ImageField(upload_to="article/")








