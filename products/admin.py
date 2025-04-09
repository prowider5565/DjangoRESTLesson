from django.contrib import admin

from products.models import Category, ToDo

# Register your models here.
admin.site.register(ToDo)
admin.site.register(Category)
