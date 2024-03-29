from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('plot', views.index, name="showplot"),
    path('', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('home', views.home, name='home'),
    path('process_form', views.create_project, name='create_project'),

]
