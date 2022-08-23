from django.urls import path
from .views import blogView, blogDetaillView, likeView, commentView, commentDetailView
urlpatterns = [
    path('', blogView, name="blog"),
    path('<int:pk>/', blogDetaillView, name="blogdetail"),
    path('comment/<int:blogid>/', commentView, name="comment"),
    path('comment/update/<int:commentid>/',
         commentDetailView, name="commentdetail"),
    path('like/<int:blogid>/', likeView, name="like"),
]
