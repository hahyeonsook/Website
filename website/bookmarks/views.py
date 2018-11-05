from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from bookmarks.models import Bookmark, Link
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    model = Bookmark
    template_name = 'bookmarks/index.html'
    context_object_name = 'latest_links_list'

    def get_queryset(self):
        # 최신순으로 링크 나열
        return Link.objects.order_by('-id')
