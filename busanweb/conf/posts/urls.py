from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    # /
    path('', views.PostListView.as_view(), name='index'),

    # /99/
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # /99/comment/add/
    path('<int:pk>/comment/add', views.comment_form, name='comment_form'),

    # /search/
    path('search/', include('haystack.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
