from django.contrib import admin
from django.urls import include, path
from .views import home,test,register
urlpatterns = [
    path('',home, name="home"),
    path('register/',register,name='register'),
    path('test/', test,name="test")
]