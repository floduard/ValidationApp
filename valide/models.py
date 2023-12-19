# validationApp/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from datetime import datetime

class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)  # Remove choices to allow custom input
    license = models.CharField(max_length=20)
    manufacture_date = models.DateField(validators=[
        MinValueValidator(datetime(2000, 1, 1).date())
    ])
    plate_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^RA[A-H]{1}\d{3}[A-Z]$|^(RNP|RDF)\d{3}[A-Z]$|^(IT|GR|GP|\w{1,6})$',
                message='Enter a valid plate number.',
            )
        ]
    )
    
    def __str__(self):
        return f"{self.model} - {self.plate_number}"


class Participant(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[RegexValidator(r'@ur\.ac\.rw$')],unique=True)
    phone = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+250\d{1,9}$',
                message='Enter a valid phone number starting with +250 and followed by  9 digits.',
            )
        ]
    )
    date_of_birth = models.DateField()
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"