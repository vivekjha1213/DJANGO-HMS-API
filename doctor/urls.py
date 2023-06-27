from django.urls import path
from doctor.views import (
    DoctorDeleteViewId,
    DoctorListView,
    DoctorUpdateViewId,
    TotalDoctorCountView,
)
from doctor.views import (
    DoctorListView,
    DoctorListViewId,
    DoctorRegistrationView,
)

from doctor.views import DoctorSearchView

urlpatterns = [
    path("register/", DoctorRegistrationView.as_view(), name="register"),
    path("list/", DoctorListView.as_view(), name="list"),
    path("doctors/<int:doctor_id>/", DoctorListViewId.as_view(), name="doctors"),
    path(
        "doctorUpdate/<int:doctor_id>/",
        DoctorUpdateViewId.as_view(),
        name="doctorupdate",
    ),
    path("delete/<int:doctor_id>/", DoctorDeleteViewId.as_view(), name="delete-doctor"),
    path("search/", DoctorSearchView.as_view(), name="search"),
    path(
        "count/",
        TotalDoctorCountView.as_view(),
        name="Total-doctors",
    ),
    
]
