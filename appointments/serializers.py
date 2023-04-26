from .models import Patient, Clinic, Doctor
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "created_date": {
                "read_only": True,
            },
            "modified_date": {
                "read_only": True,
            }
        }


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "created_date": {
                "read_only": True,
            },
            "modified_date": {
                "read_only": True,
            }
        }



class ClinicSerializer(serializers.ModelSerializer):
    # doctor = serializers.ReadOnlyField(source='author.name')
    doctor = serializers.ListField(write_only=True)
    # doctor = DoctorSerializer(many=True)
    class Meta:
        model = Clinic
        fields = "__all__"
        # extra_kwargs = {
        #     "id": {
        #         "read_only": True,
        #         "required": False,
        #     },
        #     "created_date": {
        #         "read_only": True,
        #     },
        #     "modified_date": {
        #         "read_only": True,
        #     }
        # }
    
    def create(self, validated_data):

        doctor_data = validated_data.pop('doctor')
        clinic = Clinic.objects.create(**validated_data)
        clinic.doctor.set(doctor_data)
        return clinic
    
