from django.urls import path

from AdminApp.views import MyAdmin

app_name = 'backstage'

urlpatterns=[
    path('admin/',MyAdmin,name="admin"),

]