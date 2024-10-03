from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import AuthLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client.urls'),name='user'),
    path('accounts/login/', AuthLoginView.as_view(), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
