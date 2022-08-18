from django.urls import path
from .views import writterView
urlpatterns = [
    path("", writterView, name="blog-view")
]
