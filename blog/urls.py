from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogPost"),
    path("delete_comment/<int:id>/", views.delete_comment, name="delete_comment"),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]