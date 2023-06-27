from django.urls import path

from patients.views import (
    PatientDeleteViewId,
    # PatientIncreaseView,
    PatientListIdView,
    PatientListView,
    PatientRegistrationView,
    PatientSearchView,
    PatientUpdateViewId,
    TotalPateintCountView,
)


urlpatterns = [
    path("register/", PatientRegistrationView.as_view(), name="register"),
    path("list/", PatientListView.as_view(), name="patientdetail"),
    path(
        "list/<int:patient_id>/", PatientListIdView.as_view(), name="patientdetailbyid"
    ),
    path(
        "update/<int:patient_id>", PatientUpdateViewId.as_view(), name="patient-update"
    ),
    path(
        "delete/<int:patient_id>", PatientDeleteViewId.as_view(), name="patient-delete"
    ),
    path("search/", PatientSearchView.as_view(), name="patient-search"),

    path(
        "count/",
        TotalPateintCountView.as_view(),
        name="Total-Patients",
    ),
    
#   path(
#         "increase/",
#         PatientIncreaseView.as_view(),
#         name="increase-Patients",
#     ),


]
