from django.urls import path

from members.views import RegisterAPIView, verifyEmail

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify-email/", verifyEmail)
]