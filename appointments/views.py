from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from caretrack.configurations.utilities.api_response import CareTrackResponse
from caretrack.configurations.exceptions.caretrack_core_exception import CareTrackError
from rest_framework import viewsets
from .models import Patient, Appointments, Clinic, Doctor
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    ClinicSerializer,
    ClinicGetSerializer,
    DoctorGetSerializer,
    AppointmentsGetSerializer,
    AppointmentsSerializer,
)
from caretrack.configurations.utilities.global_constants import (
    SUCCESSFULLY_CREATED,
    SUCCESSFULLY_DELETED,
    SUCCESSFULLY_UPDATED,
)
from caretrack.configurations.utilities.http_codes import (
    BAD_REQUEST,
    CREATED,
    OK,
    UPDATED,
)

# Create your views here.


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def welcome_api(request):
    """
    This functional component is used to display welcome API
    """

    return CareTrackResponse(
        message="Welcome to Care Track Core API v0.0.1"
    ).build_response()


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    renderer_classes = [JSONRenderer]

    def list(self, request):
        result = Patient.objects.filter(archived=False)
        serializer = PatientSerializer(result, context={"request": request}, many=True)
        return CareTrackResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):
        try:
            result = Patient.objects.get(id=pk, archived=False)
        except Patient.DoesNotExist:
            raise CareTrackResponse(
                http_status=BAD_REQUEST,
                message="No Matching Record found",
            )

        serializer = PatientSerializer(result, context={"request": request})
        return CareTrackResponse(data=serializer.data).build_response()

    def create(self, request):
        user_email = request.data.get("email")
        if Patient.objects.filter(email=user_email).exists():
            raise CareTrackError(http_status=BAD_REQUEST, message="User already exists")

        serializer = PatientSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = Patient.objects.get(id=pk, archived=False)
        except Patient.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        serializer = PatientSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()

    def destroy(self, request, pk):
        try:
            instance = Patient.objects.get(id=pk, archived=False)
            instance.archived = True
            instance.save()
        except Patient.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        return CareTrackResponse(
            http_status=OK,
            message=SUCCESSFULLY_DELETED,
        ).build_response()


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    renderer_classes = [JSONRenderer]

    def list(self, request):
        result = Doctor.objects.filter(archived=False)
        serializer = DoctorGetSerializer(
            result, context={"request": request}, many=True
        )
        return CareTrackResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):
        try:
            result = Doctor.objects.get(id=pk, archived=False)
        except Doctor.DoesNotExist:
            raise CareTrackResponse(
                http_status=BAD_REQUEST,
                message="No Matching Record found",
            )

        serializer = DoctorGetSerializer(result, context={"request": request})
        return CareTrackResponse(data=serializer.data).build_response()

    def create(self, request):
        user_email = request.data.get("email")
        if Doctor.objects.filter(email=user_email).exists():
            raise CareTrackError(http_status=BAD_REQUEST, message="User already exists")

        serializer = DoctorSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = Doctor.objects.get(id=pk, archived=False)
        except Doctor.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        serializer = DoctorSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()

    def destroy(self, request, pk):
        try:
            instance = Doctor.objects.get(id=pk, archived=False)
            instance.archived = True
        except Doctor.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        return CareTrackResponse(
            http_status=OK,
            message=SUCCESSFULLY_DELETED,
        ).build_response()


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    renderer_classes = [JSONRenderer]

    def list(self, request):
        result = Clinic.objects.all()
        serializer = ClinicGetSerializer(
            result, context={"request": request}, many=True
        )
        return CareTrackResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):
        try:
            result = Clinic.objects.get(id=pk, archived=False)
        except Clinic.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST,
                message="No Matching Record found",
            )

        serializer = ClinicSerializer(result, context={"request": request})
        return CareTrackResponse(data=serializer.data).build_response()

    def create(self, request):
        serializer = ClinicSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = Clinic.objects.get(id=pk, archived=False)
        except Clinic.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        serializer = ClinicSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()

    def destroy(self, request, pk):
        try:
            instance = Clinic.objects.get(id=pk, archived=False)
            instance.archived = True
            instance.save()

        except Clinic.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        return CareTrackResponse(
            http_status=OK,
            message=SUCCESSFULLY_DELETED,
        ).build_response()


class AppointmentsView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = AppointmentsSerializer
    renderer_classes = [JSONRenderer]

    def list(self, request):
        result = Appointments.objects.all()
        serializer = AppointmentsGetSerializer(
            result, context={"request": request}, many=True
        )
        return CareTrackResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):
        try:
            result = Appointments.objects.get(id=pk, archived=False)
        except Appointments.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST,
                message="No Matching Record found",
            )

        serializer = AppointmentsGetSerializer(result, context={"request": request})
        return CareTrackResponse(data=serializer.data).build_response()

    def create(self, request):
        if not request.data.get("patient") or request.data.get("patient") is None:
            raise CareTrackError(http_status=BAD_REQUEST, message="Patient is required")
        elif not request.data.get("doctor") or request.data.get("patient") is None:
            raise CareTrackError(http_status=BAD_REQUEST, message="Doctor is required")
        elif not request.data.get("clinic") or request.data.get("patient") is None:
            raise CareTrackError(http_status=BAD_REQUEST, message="Clinic is required")

        serializer = AppointmentsSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = Appointments.objects.get(id=pk, archived=False)
        except Appointments.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        serializer = AppointmentsSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()

    def destroy(self, request, pk):
        try:
            instance = Appointments.objects.get(id=pk, archived=False)
            instance.archived = True
            instance.save()

        except Appointments.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        return CareTrackResponse(
            http_status=OK,
            message=SUCCESSFULLY_DELETED,
        ).build_response()
