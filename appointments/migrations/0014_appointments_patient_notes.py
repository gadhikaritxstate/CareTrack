# Generated by Django 4.2 on 2023-04-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0013_remove_clinic_doctors_doctor_clinic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='patient_notes',
            field=models.TextField(blank=True, db_column='PATIENT_NOTES', max_length=600, null=True),
        ),
    ]