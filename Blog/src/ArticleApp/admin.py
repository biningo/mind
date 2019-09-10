from django.contrib import admin

# Register your models here.
from ArticleApp.models import Article, Category, Tag, ArticleComment, Image, SpecialTopic
from OtherApp.models import FriendLink


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    def show_all_tags(self, obj):
        return [a.name for a in obj.tags.all()]

    list_display = ['title','copyright',
                    'created_time','access_count',
                    'like_count','category','show_all_tags']
    ordering=('-created_time',)
    search_fields = ('title','id')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['id','content','created_time','article','father_comment','user']



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','ImageFile']

@admin.register(SpecialTopic)
class TopicAdmin(admin.ModelAdmin):

    list_display = ['id','name','created_time','summary','like_account']

@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ['id','name','friendUrl']
