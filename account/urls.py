from django.urls import path
from account.admin import UserModelAdmin
from account.views import (
    LogoutAPIView,
    SendPasswordResetEmailView,
    UserChangePasswordView,
    UserLoginView,
    UserPasswordResetView,
    UserProfileView,
    UserRegistrationView,
)

urlpatterns = [
    path('admin/login/', UserModelAdmin, name='admin_login'),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),


   path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]
