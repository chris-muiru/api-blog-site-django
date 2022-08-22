from django.urls import path
from .views import loginView, registerView,logoutView
urlpatterns = [
    path('login/', loginView),
    path('logout/', logoutView),
    path('signup/', registerView)
]
