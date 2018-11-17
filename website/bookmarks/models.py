from django.db import models
from django.conf import settings

# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('Link', on_delete=models.CASCADE)
#    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.user
