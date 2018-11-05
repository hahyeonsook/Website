from django.urls import path
from posts import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.PostsView.as_view(), name='index'),

    # /posts/99/
]
