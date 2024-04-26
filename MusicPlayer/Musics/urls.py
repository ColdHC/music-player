from django.contrib import admin
from django.urls import include, path
from .views import HomeView, musicView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('music/<int:pk>', musicView.as_view(), name='music'),
    
]