from django.contrib.auth.models import User
from django.db import models

from .constants import STATUS


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='task'
    )
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='To-Do',  max_length=20)
    
    class Meta: 
        ordering = ["-created"] 
    
    def __str__(self):
        return f'{self.title}, {self.content}, {self.created}, {self.photo}'
