from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    like=models.IntegerField(default=0)
    unlike=models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class UploadBlog(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='new_blog')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    like=models.IntegerField(default=0)
    unlike=models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class ModifyBlog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    modify = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title