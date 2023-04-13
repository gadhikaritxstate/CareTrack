from django.urls import path
from django.urls.conf import include
from .views import (
    welcome_api,
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', welcome_api),
]