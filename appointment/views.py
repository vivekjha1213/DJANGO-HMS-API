import random
import string
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from appointment.models import Appointment, AppointmentNumber

from appointment.serializers import (
    AppointmentDetailSerializer,
    AppointmentListSerializer,
    BookAppointmentSerializer,
    UpdateAppointmentSerializer,
)


# - Book a new appointment
class BookAppointmentView(APIView):
    def post(self, request, format=None):
        serializer = BookAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()

            # Generate random appointment number
            appointment_number = generate_random_appointment_number()

            # Create AppointmentNumber instance and associate it with the appointment
            appointment_number_instance = AppointmentNumber.objects.create(
                appointment=appointment, appointment_number=appointment_number
            )

            return Response(
                {
                    "message": "Appointment booked successfully",
                    "Appointment_Number": appointment_number,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            if (
                "non_field_errors" in serializer.errors
                and "already_booked" in serializer.errors["non_field_errors"][0]
            ):
                return Response(
                    {"error": "Appointment already booked."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def generate_random_appointment_number():
    length = 8
    chars = string.ascii_uppercase + string.digits
    random_number = "".join(random.choice(chars) for _ in range(length))
    return random_number




# all list  of Appointment......
class AppointmentListView(APIView):
    def get(self, request, format=None):
        appointments = Appointment.objects.all()
        if not appointments:
            return Response(
                {"message": "No appointments found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AppointmentListSerializer(appointments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



#@get api  RetrieveAPIView its handle automatically....
class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentDetailSerializer



# appointment reschedule....
class UpdateAppointmentView(UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = UpdateAppointmentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {"message": "Appointment rescheduled successfully."},
            status=status.HTTP_200_OK,
        )


# cancel Apointment view..........
class CancelAppointmentView(DestroyAPIView):
    queryset = Appointment.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"error": "No appointment found."}, status=status.HTTP_404_NOT_FOUND
            )
        instance.delete()
        return Response(
            {"message": "Your Appointment canceled successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
