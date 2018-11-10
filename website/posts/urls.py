from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.PostListView.as_view(), name='index'),

    # /posts/99/
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]
