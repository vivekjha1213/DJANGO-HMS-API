
import logging
from django.http import JsonResponse
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from doctor.models import Doctor
from doctor.serializers import (
    DoctorListSerializer,
    DoctorRegistrationSerializer,
    DoctorSearchSerializer,
    DoctorUpdateSerializer,
    TotalDoctorCountSerializer,
)

logger = logging.getLogger(__name__)


# Rest-Api---DRF...
# Dr-Register Api......
class DoctorRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = DoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            if Doctor.objects.filter(email=email).exists():
                return Response(
                    {"error": "A doctor with this email already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()

            return Response(
                {"message": "Doctor registration successful"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all doctor list
class DoctorListView(APIView):
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data)



# get all doctor list by:  doctor_id

class DoctorListViewId(APIView):
    def get(self, request, doctor_id=None, format=None):
        if doctor_id:
            try:
                doctor = Doctor.objects.get(doctor_id=doctor_id)
                serializer = DoctorListSerializer(doctor)
                return Response(serializer.data)
            except Doctor.DoesNotExist:
                return Response(
                    {"message": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            doctors = Doctor.objects.all()
            serializer = DoctorListSerializer(doctors, many=True)
            return Response(serializer.data)



# Update all dr by doctor_id :
class DoctorUpdateViewId(UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUpdateSerializer
    lookup_field = "doctor_id"

    def perform_update(self, serializer):
        instance = serializer.save()
        return Response({"message": "Profile updated"}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data["message"] = "Profile updated"
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data["message"] = "Profile updated"
        return response



# **Delete Doctor**: DELETE `/api/doctors/{id}/` - Deletes a specific doctor by ID.
class DoctorDeleteViewId(APIView):
    def delete(self, request, doctor_id=None):
        try:
            dr = Doctor.objects.get(doctor_id=doctor_id)
            dr.delete()
            return Response(
                {"message": "Delete Successful"}, status=status.HTTP_204_NO_CONTENT
            )
        except Doctor.DoesNotExist:
            return Response(
                {"message": "Doctor not  Exits"}, status=status.HTTP_404_NOT_FOUND
            )


# **Search Doctors**: GET `/api/doctors/search/?query={search_query}` - Retrieves a list of doctors based on a search query.
class DoctorSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query')

        if not search_query:
            return Response({'error': 'Search query parameter is required.'},status=status.HTTP_400_BAD_REQUEST)

        doctors = Doctor.objects.filter(
            first_name__icontains=search_query
          
        )

        if not doctors:
            return Response({'message': 'No doctors found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSearchSerializer(doctors, many=True)
        return Response({'results': serializer.data},status=status.HTTP_200_OK)
    


# @get Toatl Count doctor api
class TotalDoctorCountView(APIView):
    def get(self, request):
        total_count =Doctor.objects.count()
        serializer = TotalDoctorCountSerializer({'total_count': total_count})
        return Response(serializer.data)