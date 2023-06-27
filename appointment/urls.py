from django.urls import path
from appointment.serializers import CancelAppointmentView
from appointment.views import (
    AppointmentDetailView,
    AppointmentListView,
    BookAppointmentView,
    UpdateAppointmentView,
)

urlpatterns = [
    # Book a new appointment
    path("book/", BookAppointmentView.as_view(), name="book-appointment"),
    # Get all appointments
    path("appointments/", AppointmentListView.as_view(), name="appointment-list"),
    ## Get details of a specific appointment
    path(
        "appointments/<int:pk>/",
        AppointmentDetailView.as_view(),
        name="appointment-detail",
    ),
    #Update details of a specific appointment
    path(
        "appointments/<int:pk>/update/",
        UpdateAppointmentView.as_view(),
        name="update-appointment",
    ),
    ## Cancel a specific appointment
    path(
        "appointments/<int:pk>/cancel/",
        CancelAppointmentView.as_view(),
        name="cancel-appointment",
    ),
]
