from django.urls import path
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, makeshorturl, redirectUrl
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('shortenurl/', views.makeshorturl),
    path('<str:shorturl>', views.redirectUrl),
    path('urllist/', login_required(views.UrlList.as_view())),

]
