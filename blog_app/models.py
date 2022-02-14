from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Criando gerenciador personalizado para a class Post
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')

class Post(models.Model):
    
    Status_Choice = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    title = models.CharField(max_length=300)
    label = models.SlugField(max_length=300, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status_Choice, default='rascunho')


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    objects = models.Manager()
    publisehd = PublishedManager()
