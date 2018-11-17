from django.contrib import admin
from .forms import PostForm
from .models import Post, Comment, Image

# Register your models here.

class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 5

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [ImageAdmin, ]

    def save_model(self, request, obj, form, change):
        super(PostAdmin, self).save_model(request, obj, form, change)
        obj.save()

        for afile in request.FILES.getlist('images_multiple'):
            obj.images.create(file=afile)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
