from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.PostListView.as_view(), name='index'),

    # /posts/99/
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # /posts/add/
    path('add/', views.PostCreateView.as_view(), name='post_create'),

    # /posts/99/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]
