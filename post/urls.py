from django.contrib import admin
from django.urls import path,include
from .views import show_post

urlpatterns = [
    path('', show_post),
    
]
