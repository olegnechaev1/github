from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link',
        'published',
        'created_at',
        'source',
    )
    
    
admin.site.register(News, NewsAdmin)  
