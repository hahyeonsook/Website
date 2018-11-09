from django.urls import path
from django.conf.urls.static import static
from posts import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.PostView.as_view(), name='index'),

    # /posts/99/
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]
