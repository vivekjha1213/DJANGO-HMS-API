from django.db import models


class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Gynecology', 'Gynecology'),
        ('Urology', 'Urology'),
        ('Oncology', 'Oncology'),
        ('Psychiatry', 'Psychiatry'),
        ('ENT', 'ENT'),   
    ]
    
    
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES)
    qualifications = models.TextField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/', blank=True)
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

