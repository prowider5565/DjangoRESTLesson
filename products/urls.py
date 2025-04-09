from django.urls import path

from products.views import create_todo
from products.views import todo_list
from products.views import todo_delete

urlpatterns = [
    path("create/", create_todo),
    path("list/", todo_list),
    path("delete/<int:pk>", todo_delete),
]