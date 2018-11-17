from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post, Comment

# Create your views here.

#--Post View
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'image', 'content']

#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('posts:index')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:index')


#--Comment View
class CommentListView(ListView):
    model = Comment
    content_object_name = 'latest_comment_list'

    def get_queryset(self):
        return Comment.objects.order_by('-pub_date')

class CommentDetailView(DetailView):
    model = Comment

#--Function-based View
