from django.urls import path
from django.views.generic import TemplateView

from OtherApp.views import FriendHtml, NotePost, NoteHtml, Beautiful, MyHeat

app_name='other'
urlpatterns=[
    path('friends/',FriendHtml,name='friends'),
    path('note/post/',NotePost,name="notepost"),
    path('note/show/',NoteHtml,name="noteshow"),
    path('beautiful/',Beautiful,name='beautiful'),
    path('heat/',MyHeat,name='heat'),
]