# Generated by Django 4.2 on 2023-04-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_doctor_clinic_clinic_doctor_doctorclinics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='middle_name',
            field=models.CharField(blank=True, db_column='MIDDLE_NAME', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(blank=True, db_column='MIDDLE_NAME', max_length=300, null=True),
        ),
    ]
