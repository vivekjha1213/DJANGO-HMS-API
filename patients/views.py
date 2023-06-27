from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from patients.models import Patient
from patients.serializers import (
    # PatientIncreaseSerializer,
    PatientListIdSerializer,
    PatientListSerializer,
    PatientRegistrationSerializer,
    PatientSearchSerializer,
    PatientUpdateSerializer,
    TotalPatientCountSerializer,
)

# - Endpoint: POST `/api/patients/register`
# -Description: Creates a new patient with the provided details.
class PatientRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = PatientRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            if Patient.objects.filter(email=email).exists():
                return Response(
                    {"error": "this email already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(
                {"message": "registration successful"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# **List Patients**:
#    - Endpoint: GET `/api/patients/list`
#    - Description: Retrieves a list of all patients.
class PatientListView(APIView):
    def get(self, request, format=None):
        Patients = Patient.objects.all()
        serializer = PatientListSerializer(Patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#  **Retrieve Patient**:
#    - Endpoint: GET `/api/patients/{id}/`
#    - Description: Retrieves a specific patient by their ID.


class PatientListIdView(APIView):
    def get(self, request, patient_id, format=None):
        try:
            patient = Patient.objects.get(patient_id=patient_id)
            serializer = PatientListIdSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response(
                {"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND
            )


# **Update Patient**:
#    - Endpoint: PUT `/api/patients/{id}/`
#    - Description: Updates the details of a specific patient by their ID.
class PatientUpdateViewId(APIView):
    queryset = Patient.objects.all()
    serializer_class = PatientUpdateSerializer
    lookup_url_kwarg = (
        "patient_id"  # Specify the correct lookup  into Db  keyword argument
    )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_object(self, patient_id):
        try:
            return self.queryset.get(patient_id=patient_id)
        except Patient.DoesNotExist:
            return Response(
                {"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        patient_id = kwargs.get(self.lookup_url_kwarg)
        patient = self.get_object(patient_id)
        serializer = self.serializer_class(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Profile update success"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        patient_id = kwargs.get(self.lookup_url_kwarg)
        patient = self.get_object(patient_id)
        serializer = self.serializer_class(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Profile update success"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  **Delete Patient**:
#    - Endpoint: DELETE `/api/patients/{id}/`
#    - Description: Deletes a specific patient by their ID.


class PatientDeleteViewId(APIView):
    def delete(self, request, patient_id=None):
        try:
            patient = Patient.objects.get(patient_id=patient_id)
            patient.delete()
            return Response(
                {"message": " Profile Delete Successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Patient.DoesNotExist:
            return Response(
                {"message": "Profile not  Exits"}, status=status.HTTP_404_NOT_FOUND
            )
        
# **Search Patients**:
# - Endpoint: GET http://127.0.0.1:8000/api/patient/search/?query=rahul
# - Description: Searches for patients based on specific criteria, such as name, age, gender, etc.
class PatientSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get("query")
        if not search_query:
            return Response(
                {"error": "Search query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        patients = Patient.objects.filter(name__icontains=search_query)
        if not patients:
            return Response(
                {"message": "No patients found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PatientSearchSerializer(patients, many=True)
        response_data = {
            "count": len(patients),
            "results": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    
    
# @get Toatl Count doctor api
class TotalPateintCountView(APIView):
    def get(self, request):
        total_count =Patient.objects.count()
        serializer = TotalPatientCountSerializer({'total_count': total_count})
        return Response(serializer.data)
    


#@patient increase api
''' 
class PatientIncreaseView(APIView):
    def post(self, request):
        serializer = PatientIncreaseSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


'''