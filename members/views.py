from rest_framework.generics import GenericAPIView
from .serializers import CustomerSerializer
from .models import Customer
import random
from rest_framework.response import Response
from django.core.mail import send_mail
from core.settings import DEFAULT_FROM_EMAIL
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet

class CustomerRegisterAPIView(GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    cache = {}

    def create(self, request, *args, **kwargs):
        userDetails = self.get_serializer(data=request.data['user'])
        userDetails.is_valid(raise_exception=True)
        customerDetails = self.get_serializer(data=request.data['customer'])
        customerDetails.is_valid(raise_exception=True)
        for _ in range(0,300):
            otp = ''.join([random.choice("1234567890") for _ in range(1, 5)])
            if self.cache.get(otp) is None:
                self.cache[otp] = {'customer':customerDetails.data,'user':userDetails.data}
                break
        else:
            return Response({'details':'sorry too many requests'}, status=500)
        send_mail(
            subject="Sign in to your clothes-app account",
            message="secret pin is %(pin)s. We won't call you for this pin" % {'pin':otp}
            from_email=DEFAULT_FROM_EMAIL
            recipient_list=[request.data['user']['email']]
        )
        return Response({'detail':'sent the mail, check your inbox'})

class VerifyRegistrationAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        register_data = CustomerRegisterAPIView.cache.get(request.query_params['pin'])
        if register_data is None:
            # god forbid you do another request again, dirty hacker
            return Response(status=403)
        user = get_user_model().objects.get(id=pk)
        if user.username == register_data.user.username:
            # create user and customer
            userDetails = self.get_serializer(data=register_data['user'])
            customerDetails = self.get_serializer(data=register_data['customer'])
            userDetails.is_valid(raise_exception=True)
            userDetails.is_valid(raise_exception=True)
            customerDetails.save()
            customerDetails.save()
            CustomerRegisterAPIView.cache.clear()
            return Response({'user':userDetails.data,'customer':customerDetails.data}, status=201)
        else:
            # god forbid you do another request again, dirty hacker
            return Response(status=403)