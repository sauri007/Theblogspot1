from django.contrib import admin
from django.urls import path
from . import views
from .views import Search_User




urlpatterns = [
    path("", views.userhome, name="userhome"),
    path("post", views.post, name="post"),
    path("like_dislike", views.likePost, name="like_dislike_post"),
    path("delete/<int:ID>", views.delpost, name="deletepost"),
    path("comment", views.comment, name="comment"),
    path("user/follow/<str:username>", views.follow, name="follow"),
    path("search/",Search_User.as_view(), name="search_user"),
    path("<str:username>", views.userprofile, name="userprofile"),





]