from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
#    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.pk
"""
class Tag(models.Model):
    post = models.ManyToManyField('Tag')
"""
