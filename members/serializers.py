from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import (
    Customer, Admin
)

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
