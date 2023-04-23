from django.db import models

from django.urls import path
from django.urls.conf import include
from . import constants as c
from .views import (
    welcome_api,
)
from rest_framework.routers import DefaultRouter
from django.utils import timezone

urlpatterns = [
    path('', welcome_api),

]

class Patient(models.Model):
    class Meta:
        db_table = "PATIENT"
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    id = models.BigAutoField(db_column="ID", primary_key=True, default=0)

    created_date = models.DateTimeField(db_column="CREATED_DATE", default=timezone.now)

    modified_date = models.DateTimeField(db_column="MODIFIED_DATE", auto_now=True)

    first_name =  models.CharField(db_column="FIRST_NAME", max_length=300, null=True, blank=False)

    middle_name =  models.CharField(db_column="MIDDLE_NAME", max_length=300, null=True, blank=True)

    last_name =  models.CharField(db_column="LAST_NAME", max_length=300, null=True, blank=False)

    email = models.EmailField(db_column="EMAIL", null=True, blank=True, max_length=254)

    street = models.CharField(db_column="STREET", null=True, blank=False, max_length=300)
    
    city = models.CharField(db_column="CITY", null=True, blank=False, max_length=300)

    state = models.CharField(db_column="STATE", null=True, blank=False, max_length=300)

    zipcode = models.CharField(db_column="ZIPCODE", null=True, blank=False, max_length=7)

    phone = models.CharField(db_column="PHONE", null=True, blank=False, max_length=20)

    date_of_birth = models.DateField(db_column="DATE_OF_BIRTH", null=True, blank=False, max_length=8)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    @property
    def full_address(self):
        return f"{self.street} {self.city} {self.state} {self.zipcode}"
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Clinic(models.Model):
    class Meta:
        db_table = "CLINIC"

    id = models.BigAutoField(db_column="ID", primary_key=True, default=0)

    created_date = models.DateTimeField(db_column="CREATED_DATE", default=timezone.now)

    modified_date = models.DateTimeField(db_column="MODIFIED_DATE", auto_now=True)


    clinic_name =  models.CharField(db_column="CLINIC_NAME", max_length=300, null=True, blank=False)

    street = models.CharField(db_column="STREET", null=True, blank=False, max_length=300)
    
    city = models.CharField(db_column="CITY", null=True, blank=False, max_length=300)

    state = models.CharField(db_column="STATE", null=True, blank=False, max_length=300)

    zipcode = models.CharField(db_column="ZIPCODE", null=True, blank=False, max_length=7)

    phone = models.CharField(db_column="PHONE", null=True, blank=False, max_length=20)

    @property
    def full_name(self):
        return f"{self.clinic_name}"
    
    @property
    def full_address(self):
        return f"{self.street} {self.city} {self.state} {self.zipcode}"
    
    def __str__(self):
        return f"{self.clinic_name}"


class Doctor(models.Model):
    class Meta:
        db_table = "DOCTOR"


    SPECIALIZATION_CHOICES = (
        (c.PHISIOTHERAPY, c.PHISIOTHERAPY),
        (c.GYNECOLOGIST, c.GYNECOLOGIST),
        (c.DENTIST, c.DENTIST),
        (c.CARDIOLOGIST, c.CARDIOLOGIST),
        (c.DERMATOLOGIST, c.DERMATOLOGIST),
        (c.NEUROLOGIST, c.NEUROLOGIST),
        (c.PEDIATRICIAN, c.PEDIATRICIAN),
        (c.PSYCHIATRIST, c.PSYCHIATRIST),
        (c.PSYCHOLOGIST, c.PSYCHOLOGIST),
        (c.RADIOLOGIST, c.RADIOLOGIST),
        (c.SURGEON, c.SURGEON),
        (c.UROLOGIST, c.UROLOGIST),
    )

    id = models.BigAutoField(db_column="ID", primary_key=True, default=0)

    created_date = models.DateTimeField(db_column="CREATED_DATE", default=timezone.now)

    modified_date = models.DateTimeField(db_column="MODIFIED_DATE", auto_now=True)

    first_name =  models.CharField(db_column="FIRST_NAME", max_length=300, null=True, blank=False)

    middle_name =  models.CharField(db_column="MIDDLE_NAME", max_length=300, null=True, blank=False)

    last_name =  models.CharField(db_column="LAST_NAME", max_length=300, null=True, blank=False)

    email = models.EmailField(db_column="EMAIL", null=True, blank=True, max_length=254)

    street = models.CharField(db_column="STREET", null=True, blank=False, max_length=300)
    
    city = models.CharField(db_column="CITY", null=True, blank=False, max_length=300)

    state = models.CharField(db_column="STATE", null=True, blank=False, max_length=300)

    zipcode = models.CharField(db_column="ZIPCODE", null=True, blank=False, max_length=7)

    phone = models.CharField(db_column="PHONE", null=True, blank=False, max_length=20)

    specialization = models.CharField(db_column="SPECIALIZATION",max_length=20,choices=SPECIALIZATION_CHOICES,null=True,unique=False)

    # clinic_FK
    clinic = models.ManyToManyField(Clinic,db_column="CLINIC_ID",related_name="clinic_id")

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    @property
    def full_address(self):
        return f"{self.street} {self.city} {self.state} {self.zipcode}"
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Appointments(models.Model):
    class Meta:
        db_table = "APPOINTMENTS"

    id = models.BigAutoField(db_column="ID", primary_key=True, default=0)

    created_date = models.DateTimeField(db_column="CREATED_DATE", default=timezone.now)

    modified_date = models.DateTimeField(db_column="MODIFIED_DATE", auto_now=True)

    clinic = models.ForeignKey(Clinic, db_column="CLINIC_ID", on_delete=models.CASCADE, blank=True, null=True, related_name="appointment_clinic_id")

    doctor = models.ForeignKey(Doctor,db_column="DOCTOR_ID",on_delete=models.CASCADE, blank=True, null=True, related_name="doctor_clinic_id",)

    patient = models.ForeignKey(Patient, db_column="PATIENT_ID", blank=True, null=True, on_delete=models.CASCADE, related_name="patient_clinic_id")

    appointment_datetime = models.DateTimeField(db_column="APPOINTMENT_DATETIME", blank=False, null=False,)

    def __str__(self):
        return f"Patient: {self.patient}, Doctor: {self.doctor}, Appointment Date: {self.appointment_datetime}"
