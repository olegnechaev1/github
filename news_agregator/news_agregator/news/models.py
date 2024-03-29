from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, default="", unique=True)
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=30, default="", blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return f'{self.title},{self.link},{self.published},{self.created_at},{self.source}'    
