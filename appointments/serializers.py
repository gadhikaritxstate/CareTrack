from .models import Patient, Clinic, Doctor, Appointments
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


class ClinicGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        exclude = (
            "created_date",
            "modified_date",
        )


class DoctorGetSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer()
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



class AppointmentsGetSerializer(serializers.ModelSerializer):
    doctor = DoctorGetSerializer()
    clinic = ClinicGetSerializer()
    class Meta:
        model = Appointments
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



class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
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
