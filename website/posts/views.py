from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Post, Comment

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class CommentListView(ListView):
    model = Comment

class CommentDetailView(DetailView):
    model = Comment

#--Function-based View
