from django.urls import path
from .views import blogView,blogDetaillView
urlpatterns = [
    path('', blogView, name="blog"),
    path('<int:pk>/', blogDetaillView, name="blogdetail")
]
