from django.contrib import admin
from django.urls import path
from pmhireapp import views

urlpatterns = [
    path('', views.index,name="home"),
    path('home', views.index,name="home"),
    path('about', views.about,name="about"),
    path('company', views.company,name="company"),
    path('candidate', views.candidate,name="candidate"),
    path('contact', views.contact,name="contact"),
]