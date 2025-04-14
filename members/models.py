from django.db import models
from django.contrib.auth import get_user_model

from .enums import UserRole, UserStatus

BaseUser = get_user_model()


class Admin(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField(max_length=130)
    personal_email = models.EmailField(max_length=120)
    avatar = models.URLField(blank=True, null=True)
    banner = models.URLField(blank=True, null=True)
    join_date = models.DateField()

    def __str__(self):
        return self.full_name


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=UserRole)
    balance = models.IntegerField()

    def __str__(self):
        return self.full_name


class OrderModerator(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=UserStatus)
    rating = models.FloatField(null=False, default=0.0)
    avatar = models.URLField(blank=True, null=True)
    banner = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"OrderModerator({self.user.username})"
