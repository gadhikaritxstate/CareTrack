from django.urls import path
from django.urls.conf import include
from .views import (
    welcome_api,
    PatientView,
    ClinicView,
    DoctorView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("patient", PatientView, basename="patients")
router.register("doctor", DoctorView, basename="doctors")
router.register("clinic", ClinicView, basename="clinic")

urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
]