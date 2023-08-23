from django.shortcuts import render
from .views import macbook, hp, asus, detail
from django.urls import path

urlpatterns = [
    path('MacBook/', macbook),
    path('HP/', hp),
    path('ASUS/', asus),
    path('detail/<int:noutbook_id>', detail)
]