from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class ToDo(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    ]
    category = models.ForeignKey(null=True, to=Category, on_delete=models.SET_NULL)
    content = models.TextField()
    status = models.CharField(choices=STATUS)
