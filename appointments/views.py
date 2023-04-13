from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from caretrack.configurations.utilities.api_response import CareTrackResponse

# Create your views here.

@api_view(["GET"])
@renderer_classes([JSONRenderer])
def welcome_api(request):
    """
    This functional component is used to display welcome API
    """

    return CareTrackResponse(message="Welcome to Care Track Core API v0.0.1").build_response()