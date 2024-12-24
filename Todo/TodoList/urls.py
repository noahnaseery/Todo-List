from django.urls import path
from .views import Login, SignUp, Logout

urlpatterns = [
    path("", Login, name = 'Login'),
    path("signup/", SignUp, name = 'SignUp'),
    path("logout/", Logout, name = 'logout')

]
