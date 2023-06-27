from rest_framework import serializers

from rest_framework.generics import DestroyAPIView

from rest_framework.response import Response
from rest_framework import status

from doctor.models import Doctor
from patients.models import Patient
from appointment.models import Appointment, AppointmentNumber


class BookAppointmentSerializer(serializers.ModelSerializer):
    doctor_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()

    class Meta:
        model = Appointment
        fields = [
            "appointment_id",
            "doctor_id",
            "patient_id",
            "appointment_date",
            "appointment_time",
        ]

    def validate(self, attrs):
        doctor_id = attrs.get("doctor_id")
        patient_id = attrs.get("patient_id")

        # Check if doctor with the given ID exists
        if not Doctor.objects.filter(doctor_id=doctor_id).exists():
            raise serializers.ValidationError(
                "Doctor with the provided ID does not exist."
            )

        # Check if patient with the given ID exists
        if not Patient.objects.filter(patient_id=patient_id).exists():
            raise serializers.ValidationError(
                "Patient with the provided ID does not exist."
            )

        return attrs

    def create(self, validated_data):
        doctor_id = validated_data.get("doctor_id")
        patient_id = validated_data.get("patient_id")

        doctor = Doctor.objects.get(doctor_id=doctor_id)
        patient = Patient.objects.get(patient_id=patient_id)

        appointment_date = validated_data.get("appointment_date")
        appointment_time = validated_data.get("appointment_time")

        # Check if an appointment already exists for the given doctor, patient, date, and time
        if Appointment.objects.filter(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
        ).exists():
            raise serializers.ValidationError(
                "Appointment already booked for the given doctor, patient, date, and time."
            )

        appointment = Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
        )

        return appointment


# All Appointment list..
class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "appointment_id",
            "doctor_id",
            "patient_id",
            "appointment_date",
            "appointment_time",
        ]


class AppointmentDetailSerializer(serializers.ModelSerializer):
    appointment_number = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = [
            "appointment_number",
            "doctor_id",
            "patient_id",
            "appointment_date",
            "appointment_time",
        ]

    def get_appointment_number(self, obj):
        try:
            appointment_number = AppointmentNumber.objects.get(
                appointment=obj
            ).appointment_number
        except AppointmentNumber.DoesNotExist:
            appointment_number = None
        return appointment_number


class UpdateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["doctor_id", "patient_id", "appointment_date", "appointment_time", "appointment_id"]


#Cancel Appointment..
class CancelAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = []



class CancelAppointmentView(DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = CancelAppointmentSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Appointment canceled successfully."}, status=status.HTTP_204_NO_CONTENT)