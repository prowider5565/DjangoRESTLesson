from django.urls import path

from products.views import create_todo
from products.views import todo_list

urlpatterns = [
    path("create/", create_todo),
    path("list/", todo_list),
]