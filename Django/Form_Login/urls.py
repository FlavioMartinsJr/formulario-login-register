
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginPage, name='login'),
    path('', views.HomePage, name='home'),
    path('logout/',views.LogoutPage,name='logout'),
]
