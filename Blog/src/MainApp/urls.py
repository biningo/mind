from django.urls import path

from MainApp.views import Index

urlpatterns = [
    path('index/',Index),
]