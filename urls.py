"""textutex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import path
from django.contrib import admin
from . import v





urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.index, name="index"),
    path("removepunc", v.removepunc, name="rmvpnc"),
    path("first capital", v.capitalizefirst, name="first capital"),
    path("newline-remove", v.newlineremove, name="nlr"),
    path("spaceremove", v.spaceremove, name="spr"),
    path("charcount", v.charcount, name="chc"),
    path("analyze", v.analyze, name="analyze"),



]
