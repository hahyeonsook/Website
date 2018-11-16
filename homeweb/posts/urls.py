from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    # /
    path('', views.PostListView.as_view(), name='index'),

    # /99/
    # /99/update/
    # /99/delete/

    # /add/
#    path('add/', views.PostFormView.as_view(), name='post_form')
    path('add/', views.post, name='post_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
