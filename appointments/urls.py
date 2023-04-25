from django.urls import path
from django.urls.conf import include
from .views import (
    welcome_api,
    PatientView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("patient", PatientView, basename="patients")

urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
]