
from django.urls import path

from . import views

urlpatterns = [

    path('', views.my_login, name="my-login"),

    path('register', views.register, name="register"),

    path('home', views.home, name="home"),

    path('user-logout', views.user_logout, name="user-logout"),
]






