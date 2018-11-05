from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class PostsView(TemplateView):
    template_name = "posts/posts.html"
