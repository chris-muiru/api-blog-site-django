from django.urls import path
from .views import blogView, blogDetailView, likeView, commentView, commentDetailView
urlpatterns = [
    path('', blogView, name="blog"),
    path('<int:pk>/', blogDetailView, name="blogdetail"),
    path('comment/<int:blogid>/', commentView, name="comment"),
    path('comment/update/<int:commentid>/',
         commentDetailView, name="commentdetail"),
    path('like/<int:blogid>/', likeView, name="like"),
]
