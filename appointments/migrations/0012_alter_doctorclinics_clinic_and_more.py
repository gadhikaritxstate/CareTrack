# Generated by Django 4.2 on 2023-04-26 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_remove_clinic_doctor_clinic_clinic_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorclinics',
            name='Clinic',
            field=models.ForeignKey(db_column='CLINIC', on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='appointments.clinic'),
        ),
        migrations.AlterField(
            model_name='doctorclinics',
            name='doctor',
            field=models.ForeignKey(db_column='Doctor', on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='appointments.doctor'),
        ),
    ]
