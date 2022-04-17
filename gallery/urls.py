from django.urls import path
from . import views

urlpatterns = [
    #localhost:5000/gallery/home
    path("home",views.home)
]