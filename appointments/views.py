from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from caretrack.configurations.utilities.api_response import CareTrackResponse
from caretrack.configurations.exceptions.caretrack_core_exception import CareTrackError
from rest_framework import viewsets
from .models import Patient,Appointments,Clinic, Doctor
from .serializers import PatientSerializer
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

    return CareTrackResponse(message="Welcome to Care Track Core API v0.0.1").build_response()



class PatientView(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    renderer_classes = [JSONRenderer]

    def list(self, request):

        result = Patient.objects.all()
        serializer = PatientSerializer(
            result, context={"request": request}, many=True
        )
        return CareTrackResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):

        try:
            result = Patient.objects.get(id=pk)
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

        serializer = PatientSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return CareTrackResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()


    def update(self, request, pk):
        try:
            instance = Patient.objects.get(id=pk)
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
            instance = Patient.objects.get(id=pk)
            instance.delete()
        except Patient.DoesNotExist:
            raise CareTrackError(
                http_status=BAD_REQUEST, message="No Matching Record found"
            )
        return CareTrackResponse(
            http_status=OK,
            message=SUCCESSFULLY_DELETED,
        ).build_response()
