from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("html", views.html, name="html"),
    path("js", views.js, name="js"),
    path("py", views.py, name="py"),

]
