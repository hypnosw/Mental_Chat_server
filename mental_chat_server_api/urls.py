from django.contrib import admin
from django.urls import path
from .views import HelloWorldAPIView

urlpatterns = [
    path('hello/', HelloWorldAPIView(), name="hello-world"),
]