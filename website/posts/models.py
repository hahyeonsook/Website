from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default='Title')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post')
#    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    content = models.CharField(max_length=100, default='Content')
    pub_date = models.DateTimeField(default=timezone.now)
#    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return 'Post (Title: {self.title}, User: {self.user.username})'

class Image(models.Model):
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.pk
"""
class Tag(models.Model):
    post = models.ManyToManyField('Tag')
"""

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField(default='Comment')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Comment (PK: {self.pk}, User: {self.user.username})'
