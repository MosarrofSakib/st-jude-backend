# Generated by Django 4.0.1 on 2022-03-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_patient_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='processpayments',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
