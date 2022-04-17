from django.urls import path
from . import views

urlpatterns = [
    #localhost:5000/art/home
    path("home",views.home)
]