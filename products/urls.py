from django.urls import path

from products.views import create_todo


urlpatterns = [
    path("create/", create_todo)
]