from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
