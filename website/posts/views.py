from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Post, Comment

# Create your views here.
class PostView(ListView):
    model = Post
    context_object_name = 'latest_post_list'

    def get_context_data(self, **kwargs):
        return Post.objects.order_by('-pub_date')

class PostDetail(DetailView):
    model = Post
    template_name = 'posts/detail.html'
