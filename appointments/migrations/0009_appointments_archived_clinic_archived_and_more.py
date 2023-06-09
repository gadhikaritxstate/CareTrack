# Generated by Django 4.2 on 2023-04-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_alter_clinic_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='archived',
            field=models.BooleanField(db_column='ARCHIVED', default=False),
        ),
        migrations.AddField(
            model_name='clinic',
            name='archived',
            field=models.BooleanField(db_column='ARCHIVED', default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='archived',
            field=models.BooleanField(db_column='ARCHIVED', default=False),
        ),
        migrations.AddField(
            model_name='doctorclinics',
            name='archived',
            field=models.BooleanField(db_column='ARCHIVED', default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='archived',
            field=models.BooleanField(db_column='ARCHIVED', default=False),
        ),
    ]
