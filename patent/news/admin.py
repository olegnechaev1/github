from django.contrib import admin
from .models import News, Comment, Like


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link',
        'published',
        'created_at',
        'source',
    )
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'comment',
        'date',
    )    
    

class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'comment_like',
    )
    
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)