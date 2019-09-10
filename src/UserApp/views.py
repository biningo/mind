import random
from random import Random


from django.core.mail import send_mail
from django.db.models import F
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
<<<<<<< HEAD
from django.shortcuts import render
=======
<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render,redirect
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from Blog2.Utils.RedisUtil import getRedisClient
from UserApp.models import UserAccount


@require_http_methods(["POST"])
def Register(request):
    message = {}
    r = getRedisClient()
    if request.POST.get("captcha") == r.get("captcha"):
        user = UserAccount()
        user.email = request.POST.get("email")
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> '解决用户登录和前端样式调整'
        user.username = user.email

        user.password=666666
        user.save()
        request.session.set_expiry(60 * 60 * 3)  # 三小时
        request.session["user_email"] = user.email
        return HttpResponseRedirect("/article/index/")
<<<<<<< HEAD
=======
=======
        user.username = request.POST.get("username")

        user.password=666666
        user.save()
        request.session.set_expiry(60 * 60 * 24*30)  # 三小时
        request.session["user_email"] = user.email
        return redirect(reverse("article:index"))
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'
    else:
        return HttpResponse("验证码不正确")


@require_http_methods(["POST"]) #发送验证码
def Captcha(request):
    email = request.POST.get("email")
    print(email)
    emails = []
    emails.append(email)
    r = getRedisClient()
    if r.get("captcha")==None:
        number = random.randint(1000,9999)
        r.set("captcha",number,ex=60*60)
    else:
        number = r.get("captcha")

    #r.set("captcha",number,ex=60*5)  #设置验证码时间为5分钟
<<<<<<< HEAD
    send_mail('PB的博客','欢迎注册：验证码为---->'+str(number), 'm19884605250@163.com',
=======
<<<<<<< HEAD
    send_mail('PB的博客','欢迎注册：验证码为---->'+str(number), 'm19884605250@163.com',
=======
    send_mail('biningo的博客','验证码为---->'+str(number), 'm19884605250@163.com',
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'
             emails , fail_silently=True)

    return HttpResponse(number)





def Login(request):
    message = {}
    email = request.POST.get("email")

    captcha = request.POST.get("captcha")
    user = UserAccount.Check_Captcha_Access(email,captcha)
    if user:
        request.session.set_expiry(60 * 60 * 24*30)  # 一个月
        request.session["user_email"] = user.email
<<<<<<< HEAD
        return HttpResponseRedirect("/article/index")
=======
<<<<<<< HEAD
        return HttpResponseRedirect("/article/index")
=======
        return redirect(reverse("article:index"))
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'
    else:
        return HttpResponse("验证码不正确")




