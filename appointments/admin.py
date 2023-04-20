from django.contrib import admin
from .models import Appointments, Clinic,Doctor, Patient
# Register your models here.

admin.site.register(Appointments)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Patient)
