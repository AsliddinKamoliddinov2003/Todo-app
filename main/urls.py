from django.urls import path

from .views import *



urlpatterns = [
    path("", index, name="index"),
    path("post_detail/<int:pk>/", post_detail, name="post-detail"),
    path("create_post/", create_post, name="create-post"),
    path("update_post/<int:pk>/", update_post, name="update-post"),
    path("delete_post/<int:pk>/", delete_post, name="delete-post"),
]