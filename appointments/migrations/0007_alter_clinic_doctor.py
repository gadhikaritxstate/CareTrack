# Generated by Django 4.2 on 2023-04-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_clinic_clinic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='doctor',
            field=models.ManyToManyField(blank=True, db_column='DOCTOR_ID', related_name='mm_doctor_id', through='appointments.Appointments', to='appointments.doctor'),
        ),
    ]