from django.db import models

class Employee(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    date=models.DateField()
    def __str__(self):
        return self.name