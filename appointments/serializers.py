from .models import Patient
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            }
        }
