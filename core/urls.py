from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from urlshortener import views
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshortener.urls')),
]
