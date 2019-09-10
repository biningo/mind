"""Blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from ArticleApp.views import Main

urlpatterns = [
    path('',Main,name='main'), #空url直接转到首页
    path('admin/', admin.site.urls),
    url('main/',include('MainApp.urls'),name='main'), #分发 聚合
    path('article/',include('ArticleApp.urls',namespace='article')),
    path('user/',include('UserApp.urls',namespace='user')),
    path('backstage/',include('AdminApp.urls',namespace='backstage')), #后台
    path('my_space/',include('PersonalSpaceApp.urls',namespace='my_space')), #个人主页
    path('other/',include('OtherApp.urls',namespace='other')) , #其它模块 零零散散

    url(r'^media/(?P<path>.*)', serve, {"document_root":settings.MEDIA_ROOT}), #访问图片需要
]
