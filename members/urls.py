from django.urls import path
from .views import CustomerRegisterAPIView, VerifyRegistrationAPIView

urlpatterns = [
    path("customers/register/", CustomerRegisterAPIView),
    path("customers/sign-in/", VerifyRegistrationAPIView)
]