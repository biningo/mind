from django.urls import path
from django.views.generic import TemplateView

from ArticleApp.views import Detail, article_lazy_load, Index, ImageUpload, BlogEdit, TagView, \
    CategoryView, ArticlePost, UpdateArticle, TopicView, CommentPost

app_name = 'article'
urlpatterns = [

    path('upload_image/',ImageUpload),
    path('blog-edit/', BlogEdit, name='blog-edit'),
    path('detail/<str:year>/<str:month>/<int:id>/',Detail,name='detail'),
    path('index/',Index,name='index'),
    path('article_list/<category_id>/<new_hot>/<page_number>/',article_lazy_load,name='article_lazy_load'),
    path('post/',ArticlePost,name="blog_post"),
    path('comment/',CommentPost,name="commentpost"),
    path('tags/<tag_name>/',TagView,name="tag"),
    path('category/<category_name>/',CategoryView,name="category"),
    path('topic/<topic_id>/',TopicView,name='topic'),
    path('update/<int:id>/',UpdateArticle,name='updateArticle'),
    

]