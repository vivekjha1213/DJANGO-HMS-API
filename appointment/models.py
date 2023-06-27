import random
import string
from django.db import models
from doctor.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment ID: {self.appointment_id} | Doctor: {self.doctor} | Patient: {self.patient}"


class AppointmentNumber(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, primary_key=True)
    appointment_number = models.CharField(max_length=255, unique=True)

    @staticmethod
    def generate_random_appointment_number():
        length = 8
        chars = string.ascii_uppercase + string.digits
        random_number = ''.join(random.choice(chars) for _ in range(length))
        return random_number

    @classmethod
    def create(cls, appointment):
        appointment_number = cls.generate_random_appointment_number()
        return cls.objects.create(appointment=appointment, appointment_number=appointment_number)