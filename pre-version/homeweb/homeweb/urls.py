from django.contrib import admin
from django.urls import path, include

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 로그인, 비밀번호
    path('accounts/', include('allauth.urls')),
    path('', include('posts.urls')),
    # 검색
#    path('search/', include('haystack.urls')),
]
