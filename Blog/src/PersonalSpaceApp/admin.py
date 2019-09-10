from django.contrib import admin

# Register your models here.
from PersonalSpaceApp.models import  Mood


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['id','content','created_time']


