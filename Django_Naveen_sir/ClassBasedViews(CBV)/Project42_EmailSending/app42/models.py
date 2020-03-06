from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField()
    email=models.CharField(max_length=10, default=False)
