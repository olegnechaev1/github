#from django.contrib.auth import settings
#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
       
class Film(models.Model):
    author = models.ForeignKey('films.User', on_delete=models.CASCADE, related_name='authors',blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField('films.User', default=None, blank=True, related_name='liked')
    
    def __str__(self):
        return f'Film comment:{self.comment}, Film date:{self.date}'
    
    @property
    def num_likes(self):
        return str(self.liked.all().count())
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
) 


class Like(models.Model):
    user = models.ForeignKey('films.User', on_delete=models.CASCADE, related_name='user')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str(self.film)