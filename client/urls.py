from django.contrib import admin
from django.urls import include, path
from .views import home,test
urlpatterns = [
    path('',home, name="home"),
    path('test/', test,name="test")
]