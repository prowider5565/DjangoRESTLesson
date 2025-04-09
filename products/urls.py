from django.urls import path

from products.views import create_todo, todo_list, update_todo, todo_delete


urlpatterns = [
    path("create/", create_todo),
    path("list/", todo_list),
    path("update/<int:id>/", update_todo),
    path("delete/<int:id>", todo_delete)
]