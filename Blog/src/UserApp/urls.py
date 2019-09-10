
from django.urls import path

from UserApp.views import Register, Captcha, Login

app_name = 'user'
urlpatterns = [
    path('register/',Register,name="register"),
    path('captcha/',Captcha,name="captcha"),
    path('login/',Login,name="login")
]