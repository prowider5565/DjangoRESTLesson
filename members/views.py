import random
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework import status
import uuid

BaseUser = get_user_model()
cache = {}


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        userDetails = self.get_serializer(data=request.data)
        userDetails.is_valid(raise_exception=True)
        otpCode = "".join([str(random.choice(range(1, 10))) for _ in range(4)])
        # send_mail
        randomUUID = str(uuid.uuid4())
        userDetails.validated_data.update({"otp": otpCode})
        cache[randomUUID] = userDetails.validated_data
        return Response(
            data={
                "msg": "OTP code sent to your email, check your inbox!",
                "otp": otpCode,
                "randomId": randomUUID,
            }
        )


@api_view(["POST"])
def verifyEmail(request):
    otpCode, randomId = request.data.get("otpCode", None), request.data.get("randomId")
    if not otpCode or not randomId:
        return Response(
            data={
                "error": "One of the fields `otpCode` or `randomId` is not specified"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    userDetails = cache.get(randomId, None)
    print(cache)
    if userDetails is None:
        return Response(
            data={"error": "User not found in cache!"}, status=status.HTTP_404_NOT_FOUND
        )
    if userDetails["otp"] != otpCode:
        return Response(
            {"error": "Incorrect otp code provided!"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    del cache[randomId]
    del userDetails["otp"]
    password = userDetails.pop("password", None)
    user = BaseUser(**userDetails)
    user.set_password(password)
    user.objects.create()
    return Response({"msg": "JWT TOKEN HERE"})
