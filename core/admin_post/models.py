from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='name', unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Post(models.Model):
    
    class PostObjetcs(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    options = (
        ('draft', 'Draft'),            
        ('published', 'Published')
    )
        
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    fracmento = models.TextField(null=True)
    content = models.SlugField(max_length=200, unique_for_date='published', null=False,unique=True)
    published = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=20, choices=options, default='draft')
    postobjects = PostObjetcs()
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self) -> str:
        return self.title
    
    
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentario')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ("publish",)
        
        def __str__(self):
            return f"Comentario de {self.name}"
    
    