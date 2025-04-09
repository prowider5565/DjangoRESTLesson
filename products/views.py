from re import M
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import ToDo


# @api_view(["GET"])
# def get_hello(request):
#     return Response({"msg": "asdasd"})


# @api_view(["POST"])
# def create_product(request: Request):
#     content = request.data  # payload
#     headers = request.query_params
#     print("Content: ", content)
#     print("Query Parameters: ", headers)
#     return Response({"status": "ok"}, status=status.HTTP_202_ACCEPTED)

@api_view(["POST"])
def create_todo(request: Request):
    data = request.data
    ToDo.objects.create(**data)
    return Response({"msg": "Success"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def todo_list(request):
    all_plans = ToDo.objects.all()
    return []