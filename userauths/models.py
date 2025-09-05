from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def validate_pin_length(val):
    if len(str(val)) != 6:
        raise ValidationError("The PIN code must be exactly 6 digits.")

STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal')
]


class Profile(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=1)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveBigIntegerField(help_text="Enter 6-digit pin code" ,validators=[validate_pin_length])
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    mobile=models.CharField(max_length=100,help_text="Enter a 11-digit mobile number.",validators=[RegexValidator(regex=r'^\d{11}$')])
    email=models.EmailField(max_length=100)
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimage',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)