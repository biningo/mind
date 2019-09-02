import datetime
import json


import redis
from django.core import serializers
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods

from ArticleApp.models import Article, Category, Image, Tag, ArticleComment, SpecialTopic
from Blog2.decorators.ajax import ajax_required
from OtherApp.models import Notice, BroadCast
from UserApp.models import StrangeUser, UserAccount

def Main(request):
    return redirect(reverse("article:index"))


def Index(request):

    categories = Category.objects.all()
    notice_list = Notice.get_notices(1)  #取前N条 这里是取前1条通知 按时间排序
    tags = Tag.objects.all()
    message = {}
    message['categories'] = categories
    message['tags'] = tags
    message['topic_list'] = SpecialTopic.objects.all()
    message['notice_list'] = notice_list
    message['broadcasts'] = BroadCast.objects.all()
    user = request.user_account
    if user:
        message["user_account"] = user
    message['sUser'] = request.sUser

    #归档
    times = set()
    articles = Article.objects.all()
    for article in articles:
        s = str(article.created_time.year)+"-"+str(article.created_time.month)
        times.add(s)

    timeArticles_map = {}
    for t in times:
        year = int(t.split("-")[0])
        month = int(t.split("-")[1])

        dayMax = 30
        months = [1, 3, 5, 7, 8, 10, 12]
        if int(month) in months:
            dayMax = 31

        timeArticles_map[t] = Article.objects.filter(created_time__range=(datetime.date(int(year), int(month), 1),
                                                                        datetime.date(int(year), int(month), dayMax))).count()

    message['timeArticle_map'] = timeArticles_map #归档
    #网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count() #注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():

        access_count +=sUser.access_count
    message['access_count'] = access_count


    message['article_count'] = Article.objects.all().count()



    return render(request,'main.html',message)


@require_http_methods(["GET"])
def Detail(request,year,month,id):
    article=None
    pre_article = None
    next_article = None
    message = {}
    user = request.user_account
    if user:
        message['user_account'] = user
    message['sUser'] = request.sUser
    message['categories'] = Category.objects.all()
    message['tags'] = Tag.objects.all()
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    if id!=0:
        article =  Article.get_article(year,month,id)[0]
        article_list = Article.objects.all().order_by("created_time")
        if len(article_list)>1:
            for k,a in enumerate(article_list):
                if a.id == article.id:
                    if k==0:
                        pre_article = None
                        next_article = article_list[k+1]
                    elif k==(len(article_list)-1):
                        pre_article = article_list[k-1]
                        next_article = None
                    else:
                        pre_article = article_list[k-1]
                        next_article = article_list[k+1]
        article.access_count += 1
        article.save()
        message['pre_article'] = pre_article
        message['next_article'] = next_article
        message['article'] = article
        message['comment_list'] = article.articlecomment_set.all().order_by('-created_time')
        return render(request, "ArticleApp/blog-detail.html", message)
    else:
        dayMax = 30
        months = [1, 3, 5, 7, 8, 10, 12]
        if int(month) in months:
            dayMax = 31
        artile_findBy_time = Article.objects.filter(created_time__range=(datetime.date(int(year), int(month), 1),
datetime.date(int(year), int(month),dayMax)))

        # 归档
        times = set()
        articles = Article.objects.all()
        for article in articles:
            s = str(article.created_time.year) + "-" + str(article.created_time.month)
            times.add(s)

        timeArticles_map = {}
        for t in times:
            year = int(t.split("-")[0])
            month = int(t.split("-")[1])

            dayMax = 30
            months = [1, 3, 5, 7, 8, 10, 12]
            if int(month) in months:
                dayMax = 31

            timeArticles_map[t] = Article.objects.filter(created_time__range=(datetime.date(int(year), int(month), 1),
                                                                              datetime.date(int(year), int(month),
                                                                                            dayMax))).count()

        message['timeArticle_map'] = timeArticles_map


        message['article_findBy_time'] = artile_findBy_time
        message['year'] = year
        message['month'] = month



        message['article_count'] = Article.objects.all().count()

        return render(request,'ArticleApp/article_by_time.html',message)


@ajax_required #NB
def article_lazy_load(request,category_id,new_hot,page_number):
    NEW = "0"
    HOT = "1"
    if int(category_id) == 0:  #没有选类型的话传0 即表示全部
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category=Category.objects.get(id=int(category_id)))
    if new_hot == HOT:
        articles= articles.order_by('-access_count')
    else:
        articles= articles.all().order_by('-created_time')




    article_list = Article.article_list(articles,range=5,page=page_number)

    blog_html = render_to_response('ArticleApp/blog-list.html',{'article_list':article_list})

    json_data =bytes.decode(blog_html.content)+str(len(article_list.paginator.page_range))


    # json_data =serializers.serialize('json',article_list)
    # json_data = json_data[:-1]
    # s = ',' + '{"page_range":' + '"' + str(len(article_list.paginator.page_range)) + '"' + '}' + ']'
    # json_data += s
    return HttpResponse(json_data)



def BlogEdit(request):

    message={}
    message['categories'] = Category.objects.all()
    message['tags'] = Tag.objects.all()
    message['topic_list'] = SpecialTopic.objects.all()
    user = request.user_account

    message['user_account']=user



    return render(request,"ArticleApp/blog-edit.html",message)

#博客内容图片上传
def ImageUpload(request):
    img = Image(ImageFile=request.FILES.get('editormd-image-file'))
    img.save()
    data = {}
    data['success'] = 1
    data['message'] = '上传成功'
    data['url'] ='http://localhost:8000'+img.ImageFile.url
    return JsonResponse(data=data)

#博客上传
@require_http_methods(["POST"])
def ArticlePost(request):
    if request.user_account == None:
        return HttpResponse("想啥呢兄弟")
    elif request.user_account.email != "m19884605250@163.com":
        return HttpResponse("想啥呢兄弟")

    article = Article()

    article.title = request.POST.get("title")
    article.summary = request.POST.get("summary")
    article.content_html = request.POST.get("article_content_html")
    article.content_makedown = request.POST.get("article_content_makedown")

    copyright = request.POST.get("copyright")
    article.copyright =True
    article.category = Category.objects.get(id=request.POST.get("category"))
    article.topic = SpecialTopic.objects.get(id=request.POST.get('topic'))
    article.save()   #先保存再加标签 多对多需要id
    tags = Tag.objects.all()
    for tag in tags:
        if request.POST.get(tag.name)=="on":
            article.tags.add(tag)
    #print(article.id)
    return redirect(reverse("article:index"))

def UpdateArticle(request,id):
    if request.user_account == None:
        return HttpResponse("想啥呢兄弟")
    elif request.user_account.email != "m19884605250@163.com":
        return HttpResponse("想啥呢兄弟")
    article = Article.objects.get(id=id)
    message={}
    message['article'] = article
    message['categories'] = Category.objects.all()
    message['tags'] = Tag.objects.all()
    return render(request,'ArticleApp/blog-edit.html',message)

#文章评论提交
def CommentPost(request):

    if request.user_account == None:
        return HttpResponse("请先登录 想啥呢")

    user_email = request.user_account.email

    article_id = request.POST.get("article_id")
    article = Article.objects.get(id=article_id)
    content = request.POST.get("content")

    comment = ArticleComment()
    comment.content = content
    father_id = request.POST.get('comment_id')
    if(father_id):
        comment.father_comment =ArticleComment.objects.get(id=father_id)
        emails = []
        emails.append(comment.father_comment.user.email)
        send_mail('来着biningo的博客消息',str(UserAccount.objects.get(email=user_email).username)+'在'+'http://www.binnb.com/article/detail/'+str(article.created_time.year)+'/'+str(article.created_time.month)+'/'+str(article.id)+'/'+' 中回复了您：内容为【'+content+'】', 'm19884605250@163.com',
                  emails, fail_silently=True)
    else:
        send_mail('来着biningo的博客消息', str(
            UserAccount.objects.get(email=user_email).username) + '在' + 'http://www.binnb.com/article/detail/' + str(
            article.created_time.year) + '/' + str(article.created_time.month) + '/' + str(
            article.id) + '/' + ' 中给您评论了：内容为【' + content + '】', 'm19884605250@163.com',
                  ['m19884605250@163.com',], fail_silently=True)

    comment.user = UserAccount.objects.get(email=user_email)
    comment.article = article
    comment.save()

    return HttpResponseRedirect(
        "/article/detail/" + str(article.created_time.year) + '/' + str(article.created_time.month) + '/' + str(
            article.id) + '/')

def TagView(request,tag_name):
    articles = Article.objects.filter(tags__name__in=[tag_name])
    message={}
    user = request.user_account
    if user:
        message['user_account'] = user
    message['sUser'] = request.sUser
    message['categories'] = Category.objects.all()
    message['articles'] = articles
    message['tag'] = Tag.objects.get(name=tag_name)
    message['tags'] = Tag.objects.all()
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,"ArticleApp/tag-detail.html",message)

def CategoryView(request,category_name):
    print(category_name)
    if category_name =="全部":
        articles = Article.objects.all().order_by('access_count')
    else:
        articles = Article.objects.filter(category__name__in=[category_name])
    message = {}
    user = request.user_account
    if user:
        message['user_account'] = user
    message['sUser'] = request.sUser
    message['categories'] = Category.objects.all()
    message['articles'] = articles
    message['category_name'] = category_name
    message['tags'] = Tag.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()


    return render(request, "ArticleApp/category-detail.html", message)

def TopicView(request,topic_id):
    message={}
    topic = SpecialTopic.objects.get(id=int(topic_id))
    message['topic'] = topic
    user = request.user_account
    if user:
        message['user_account'] = user
    message['sUser'] = request.sUser
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,'ArticleApp/topic_detail.html',message)