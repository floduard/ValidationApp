# Generated by Django 5.0 on 2023-12-19 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+\\d{1,}$')]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter a valid plate number.', regex='^R[A-H]{2}\\d{3}[A-Z]$|^(RNP|RDF)\\d{3}[A-Z]$|^(IT|GR|\\w{1,6})$')]),
        ),
    ]
