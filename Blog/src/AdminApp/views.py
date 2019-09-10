from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ArticleApp.models import Article


def MyAdmin(request):
    if request.user_account==None:
        return HttpResponse("想啥呢兄弟")
    elif request.user_account.email !="m19884605250@163.com":
        return HttpResponse("想啥呢兄弟")
    message={}
    articles = Article.objects.all().order_by("-created_time")
    message['articles'] = articles
    user = request.user_account
    if user:
        message['user_account'] = user
    message['sUser'] = request.sUser
    return render(request,"AdminApp/admin.html",message)
