from django.contrib import admin
from .form import PostForm
from .models import Post, Comment, Image

# Register your models here.

class ImageAdmin(admin.StackedInline):
    model = Post
    extra = 5

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [ ImageAdmin, ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
#admin.site.register(Image)
