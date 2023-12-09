"""
URL configuration for sustainrbr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # commenting this out to use djangos built in login form
    # path("login/", views.loginView.as_view(), name="login"),
    # this would be used if register was a class
    #path("register/", views.registerView.as_view(), name="register"),
    path("register/", views.register, name="register"),
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
]
