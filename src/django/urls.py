
from django.urls import path
from .views import *


urlpatterns = [
    path("library/", library_view),
    path("albums/", albums_view),
    path("comments/", comments_view),
    path("photos/", photos_view),
    path("posts/", posts_view),
    path("todos/", todos_view),
    path("users/", users_view),
]