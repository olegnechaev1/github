from django.contrib import admin
from .models import Film, Like, User


class FilmAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'comment',
        'date',
    )
    
     
class LikeAdmin(admin.ModelAdmin):
        list_display = (
        'pk',
        'user',
        'film',
    )
        

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'is_staff',
        'email',
        'is_superuser',
    )
            
           
admin.site.register(Film, FilmAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(User, UserAdmin)
