from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, unique=True)
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.title}, {self.link}, {self.published}, {self.created_at}, {self.source}'
    
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author',blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, blank=True, related_name='liked')
    
    def __str__(self):
        return f'{self.comment}, {self.date}, {self.author}'       
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    comment_like = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_ike')
    value = models.CharField(default='Like', max_length=10)
    
    def __str__(self):
        return f'{self.comment_like}'
