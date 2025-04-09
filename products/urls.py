from django.urls import path

from products.views import create_todo, todo_list, update_todo


urlpatterns = [
    path("create/", create_todo),
    path("list/", todo_list),
    path("update/<int:id>/", update_todo),
]