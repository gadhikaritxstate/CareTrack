# Generated by Django 4.2 on 2023-04-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('clinic_name', models.CharField(db_column='FIRST_NAME', max_length=300)),
                ('street', models.CharField(db_column='STREET', max_length=300)),
                ('city', models.CharField(db_column='CITY', max_length=300)),
                ('state', models.CharField(db_column='STATE', max_length=300)),
                ('zipcode', models.CharField(db_column='ZIPCODE', max_length=7)),
                ('phone', models.CharField(db_column='PHONE', max_length=20)),
            ],
            options={
                'db_table': 'CLINIC',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('first_name', models.CharField(db_column='FIRST_NAME', max_length=300)),
                ('middle_name', models.CharField(db_column='MIDDLE_NAME', max_length=300)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=300)),
                ('email', models.EmailField(blank=True, db_column='EMAIL', max_length=254, null=True)),
                ('street', models.CharField(db_column='STREET', max_length=300)),
                ('city', models.CharField(db_column='CITY', max_length=300)),
                ('state', models.CharField(db_column='STATE', max_length=300)),
                ('zipcode', models.CharField(db_column='ZIPCODE', max_length=7)),
                ('phone', models.CharField(db_column='PHONE', max_length=20)),
                ('date_of_birth', models.DateField(db_column='DATE_OF_BIRTH', max_length=8)),
            ],
            options={
                'db_table': 'PATIENT',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('first_name', models.CharField(db_column='FIRST_NAME', max_length=300)),
                ('middle_name', models.CharField(db_column='MIDDLE_NAME', max_length=300)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=300)),
                ('email', models.EmailField(blank=True, db_column='EMAIL', max_length=254, null=True)),
                ('street', models.CharField(db_column='STREET', max_length=300)),
                ('city', models.CharField(db_column='CITY', max_length=300)),
                ('state', models.CharField(db_column='STATE', max_length=300)),
                ('zipcode', models.CharField(db_column='ZIPCODE', max_length=7)),
                ('phone', models.CharField(db_column='PHONE', max_length=20)),
                ('date_of_birth', models.DateField(db_column='DATE_OF_BIRTH', max_length=8)),
                ('specialization', models.CharField(choices=[('PHISIOTHERAPY', 'PHISIOTHERAPY'), ('GYNECOLOGIST', 'GYNECOLOGIST'), ('DENTIST', 'DENTIST'), ('CARDIOLOGIST', 'CARDIOLOGIST'), ('DERMATOLOGIST', 'DERMATOLOGIST'), ('NEUROLOGIST', 'NEUROLOGIST'), ('PEDIATRICIAN', 'PEDIATRICIAN'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PSYCHOLOGIST', 'PSYCHOLOGIST'), ('RADIOLOGIST', 'RADIOLOGIST'), ('SURGEON', 'SURGEON'), ('UROLOGIST', 'UROLOGIST')], db_column='SPECIALIZATION', max_length=20)),
                ('clinic', models.ManyToManyField(db_column='CLINIC_ID', related_name='clinic_id', to='appointments.clinic')),
            ],
            options={
                'db_table': 'DOCTOR',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('appointment_datetime', models.DateTimeField(blank=True, db_column='APPOINTMENT_DATETIME', null=True)),
                ('clinic', models.ForeignKey(blank=True, db_column='CLINIC_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_clinic_id', to='appointments.clinic')),
                ('doctor', models.ForeignKey(blank=True, db_column='DOCTOR_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_clinic_id', to='appointments.doctor')),
            ],
            options={
                'db_table': 'APPOINTMENTS',
            },
        ),
    ]