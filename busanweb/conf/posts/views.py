from django.shortcuts import render
from django.views.generic import ListView

from .models import *

# Create your views here.

#--View vlass
# Post
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')
