from django.db import models
from django.conf import settings
from django.utils import timezone

from tagging.fields import TagField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='post_images', verbose_name='Image')
    content = models.TextField(default=None)

    # Open Library Tagging
    tags = TagField('태그', help_text='tag1, tag2, tag3')

    # 이미지 이름 지정 post_images 폴더에 이름 지정해서 넣기
    def get_image_filename(instance, filename):
        title = instance.post.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, filename)

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey('Post', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', verbose_name='Image')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(default=None)

    def __str__(self):
        return self.content
