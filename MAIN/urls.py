from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("account.urls")),
    path("api/doctor/", include("doctor.urls")),
    path("api/patient/", include("patients.urls")),
    path("api/appointment/", include("appointment.urls")),
]
