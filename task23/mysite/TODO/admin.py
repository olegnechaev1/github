from django.contrib import admin
from .models import Task


class TaskListModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'status',
        'photo',
        'created',
    )
    

admin.site.register(Task, TaskListModelAdmin)    
