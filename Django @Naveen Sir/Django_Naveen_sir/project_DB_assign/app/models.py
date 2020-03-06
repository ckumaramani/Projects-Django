from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField
    actualsalary=models.DecimalField(max_digits=10, decimal_places=2)
    designation=models.CharField(max_length=30)
    shift=models.CharField(max_length=30)
    loans=models.DecimalField(max_digits=10, decimal_places=2)
    netsalary=models.DecimalField(max_digits=10, decimal_places=2)