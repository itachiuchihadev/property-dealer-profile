from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>', views.birthday, name='birthday')
]
