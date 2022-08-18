from django.urls import path
from .views import loginView, registerView
urlpatterns = [
    path('login/', loginView),
    path('signup/', registerView)
]
