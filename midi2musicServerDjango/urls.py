"""midi2musicServerDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.urls import include
"""
主路由设置
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    #loacalhost:5000/home
    path("home",views.test_html),
    #localhost:5000/gallery
    path("gallery",views.gallery),
    #localhost:5000/art
    path("art",views.art),
    #localhost:5000/gallery/home
    path('gallery/',include('gallery.urls')),
    #localhost:5000/art/home
    path('art/',include('art.urls')),
]
