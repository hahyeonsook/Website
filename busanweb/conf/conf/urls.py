from django.contrib import admin
from django.urls import path, include

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('posts.urls')),

    # 로그인
    path('accounts/', include('allauth.urls')),
]


