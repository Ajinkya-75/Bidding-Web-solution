from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome),
    path('addproduct/', views.addproduct),
    path('userbuy/', views.userbuy),
    path('biddingproduct/', views.biddingproduct),
    path('biddingoption/', views.biddingoption),
    path('mybid/', views.mybid),
    path('bidhistory/', views.bidhistory),
    path('viewbiddingproduct/', views.viewbiddingproduct),
]
