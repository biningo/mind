from django.urls import path

from PersonalSpaceApp.views import Index, MoodView

app_name='my_space'
urlpatterns=[
    path('index/',Index,name="index"),
    path('mood/',MoodView,name='mood'),

]