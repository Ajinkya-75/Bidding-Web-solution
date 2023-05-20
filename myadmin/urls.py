from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myadminhome),
    path('manageusers/', views.manageusers),
    path('manageusersstatus/', views.manageusersstatus),
    path('addcat/', views.addcat),
    path('addsubcat/', views.addsubcat),
]
