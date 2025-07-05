from django.contrib import admin
from blog.models import Category, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category','user','created_at']
    list_display_links = ['title']
    list_editable = ['category']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','text']

admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)


