from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register,name='register'),
    path('client-dashboard/',views.client_dashboard,name="client-dashboard"),
    path('test/', views.test,name="test")
]