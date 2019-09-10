from django.contrib import admin

# Register your models here.
from UserApp.models import StrangeUser, UserAccount


@admin.register(StrangeUser)
class StrangeUserAdmin(admin.ModelAdmin):
    list_display = ['id','uid','access_count']

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','email','created_time']