from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
app_name='main'
def Index(request):
    return HttpResponse("Index")