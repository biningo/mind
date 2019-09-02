from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ArticleApp.models import ArticleComment, Article, SpecialTopic
from OtherApp.models import Note, FriendLink
from UserApp.models import UserAccount, StrangeUser


def FriendHtml(request):
    message={}
    message['sUser'] = request.sUser
    message['user_account'] = request.user_account

    message['topic_list'] = SpecialTopic.objects.all()

    friend_list = FriendLink.objects.all()
    message['friend_list'] = friend_list

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,"OtherApp/friends.html",message)

def NoteHtml(request):

    note_list = Note.objects.all().order_by('-created_time')
    message={}
    message['sUser'] = request.sUser
    message['user_account'] = request.user_account
    message['note_list'] = note_list
    message['topic_list'] = SpecialTopic.objects.all()

    # 网站信息
    message['access_people_count'] = StrangeUser.objects.all().count()
    message['user_people_account'] = UserAccount.objects.all().count()  # 注册人数

    access_count = 0
    for sUser in StrangeUser.objects.all():
        access_count += sUser.access_count
    message['access_count'] = access_count

    message['article_count'] = Article.objects.all().count()

    return render(request,"OtherApp/note.html",message)


def NotePost(request):
    if request.user_account == None:
        return HttpResponse("想啥呢兄弟")


    email = request.user_account.email

    user = UserAccount.objects.get(email=email)

    note = Note()
    note.user = user
    note.content = request.POST.get('content')
    note.type = request.POST.get('type')

    father = request.POST.get('note_id')
    if(father):
        note.father = Note.objects.get(id=int(father))
        emails = []
        emails.append(note.father.user.email)
        send_mail('来着biningo的博客消息', str(user.username) + '在' + 'http://www.binnb.com/other/note/show/' + ' 中回复了您：内容为【' + note.content + '】', 'm19884605250@163.com',
                  emails, fail_silently=True)
    else:
        send_mail('来着biningo的博客消息', str(
            user.username) + '在' + 'http://www.binnb.com/other/note/show/' + ' 中给您留言了：内容为【' + note.content + '】',
                  'm19884605250@163.com',
                  ['m19884605250@163.com',], fail_silently=True)
    note.save()
    return HttpResponse("Ok")

def Beautiful(request):
    return render(request,'OtherApp/beautiful.html')

def MyHeat(request):

    return render(request,'OtherApp/heat.html')



