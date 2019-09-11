# Biningo-Blog
个人博客网站

## 搭建个人博客

## 前言：
**我为什么要写博客？**
[我为什么开始写博客，我又不是什么大犇？](%EF%BC%9Ahttps://blog.csdn.net/qq_40733911/article/details/94760047)

这篇文章说出了我，不止我，以及和我一样的刚入行的菜鸟的心声
写博客，建网站，不是为了炫耀啥知识，更不是为了消遣，而是总结自己的知识，完善结构体系，抒发自己的感受罢了
<br><br>
## 进入正题
<br>

### 1、目录结构
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911225816981.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
其中最主要的模块为**ArticleApp**有关文章的模块
然后就是**UserApp** 有关用户的模块，**登录**、**注册**、**评论关联**、**留言**等
其次就是**OtherApp和PersonalSpaceApp**包括**个人动态**、**公告** 、**广播消息、友链 、等**
其它模块本来想做完善点的，但是由于各种原因，看以后有没有时间吧,本来想建立一个分层的架构，类似**mvc**的，想想一个小博客网站，加上自己能力不足，就放弃了
<br><br>
### 2、表结构
先上图

**核心模块**
从左到右从上到下

 1. 用户表
 2. 评论表：**faher_comment_id是自连接，代表是评论还是回复，有father说明是回复**
 3. 分类表
 4. 文章表
 5. 标签文章多对多中间表
 6. 标签表
 7. 专题表

![核心](https://img-blog.csdnimg.cn/20190911231540468.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)

**边缘模块**

 1. 友链表
 2. 个人动态表
 3. 公告表
 4. 用户表
 5. 留言表
 6. 陌生用户表：根据ip自动建立，用于统计访问人数和访问量

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911231551755.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)

### 3、访问量统计

```
import uuid

from django.db.models import F

from UserApp.models import StrangeUser, UserAccount

USER_KEY = 'uid'


class UserAccessMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):

        email = request.session.get('user_email')
        if email:       //如果用户已经登录 则增加访问量
            UserAccount.objects.filter(email=email).update(access_count = F('access_count')+1)
            request.user_account = UserAccount.objects.filter(email=email)[0]
        else:
            request.user_account = None


        sUser = self.get_sUser(request)
        request.sUser = sUser

        response = self.get_response(request)
        return response

    def get_sUser(self,request)://获取陌生用户ip 并且入库
        uid = request.session.get(USER_KEY)
        if uid!=None:
            sUser = StrangeUser.objects.filter(uid=uid)
            sUser.update(access_count=F('access_count') + 1)
            return sUser[0]
        else:
            uid = request.META.get('REMOTE_ADDR')
            request.session.set_expiry(60*60*24*10)
            request.session[USER_KEY] = uid
            sUser = StrangeUser.objects.filter(uid=uid)

            if len(sUser):  //如果是新用户 则入库
                sUser.update(access_count=F('access_count')+1)
            else:
                sUser=[]
                ssUser = StrangeUser()
                ssUser.uid = uid
                ssUser.access_count = 1
                ssUser.save()
                sUser.append(ssUser)
            return sUser[0]

```
<br>
<br>

### 4、项目截图

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911233249808.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911233323855.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019091123335413.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911233419590.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190911233508798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDU4NDI5Mw==,size_16,color_FFFFFF,t_70)
演示地址：[http://www.binnb.top](http://www.binnb.top)
github地址：[ https://github.com/biningo/Biningo-Blog](https://github.com/biningo/Biningo-Blog)
欢迎star！
