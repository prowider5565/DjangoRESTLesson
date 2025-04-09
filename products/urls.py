from django.urls import path

from products.views import create_todo, update_todo


urlpatterns = [
    path("create/", create_todo),
    path("update/<int:id>/", update_todo)
]