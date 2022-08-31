from django.urls import path
from .views import blogView, blogDetailView, likeView, commentView, commentDetailView, userIsWritter, accessToCrudFunctionalityOnBlogId, getBlogTypeView
urlpatterns = [
    path('', blogView, name="blog"),
    path('<int:pk>/', blogDetailView, name="blogdetail"),
    path('isPermitted/', userIsWritter),
    path('isPermitted/<int:blogId>/', accessToCrudFunctionalityOnBlogId),
    path('comment/<int:blogId>/', commentView, name="comment"),
    path('comment/update/<int:commentId>/',
         commentDetailView, name="commentDetail"),
    path('like/<int:blogId>/', likeView, name="like"),
    path('type/', getBlogTypeView, name="blog-type")
]
