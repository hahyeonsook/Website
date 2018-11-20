from django.urls import path
from bookmarks import views

app_name = 'bookmarks'
urlpatterns = [
    # /bookmarks/
    path('', views.IndexView.as_view(), name='index'),

    # /bookmarks/99/
]
