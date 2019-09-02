from django.shortcuts import render

# Create your views here.
from ArticleApp.models import SpecialTopic, Article
from PersonalSpaceApp.models import Mood
from UserApp.models import StrangeUser, UserAccount


def Index(request):
    message={}
    message['sUser'] = request.sUser
    message['user_account'] = request.user_account
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,"my.html",message)

def MoodView(request):

    mood_list = Mood.objects.all().order_by("-created_time")

    message={}
    message['mood_list'] = mood_list
    message['sUser'] = request.sUser
    message['user_account'] = request.user_account
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,'OtherApp/mood.html',message)