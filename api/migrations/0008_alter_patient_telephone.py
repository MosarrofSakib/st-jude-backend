# Generated by Django 4.0.1 on 2022-03-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_processpayments_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
