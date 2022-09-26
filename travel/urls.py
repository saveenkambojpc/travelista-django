

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('packages/',views.packages,name="packages"),
    path('hotels/',views.hotels ,name="hotels"),
    path('contact/',views.contact,name="contact"),
]
