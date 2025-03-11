from django.contrib import admin
from django.urls import path
from .views import GoogleAPIView

urlpatterns = [
    path('googling', GoogleAPIView().as_view(), name="Google-Chat"),
]