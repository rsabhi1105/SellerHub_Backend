from django.urls import path

from authentications.views import RegistrationView, LoginView, ForgetPasswordView, ResetPassword

urlpatterns = [
    path("registration", RegistrationView.as_view()),
    path("login", LoginView.as_view()),
    path("fp", ForgetPasswordView.as_view()),
    path("reset_pass/<int:uid>/<str:token>", ResetPassword.as_view())
]
