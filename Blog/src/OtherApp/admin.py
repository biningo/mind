from django.contrib import admin

# Register your models here.
from OtherApp.models import Notice, BroadCast, Note


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','content','created_time']

@admin.register(BroadCast)
class BroadCastAdmin(admin.ModelAdmin):
    list_display = ['id','content']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','content','created_time','user','type']