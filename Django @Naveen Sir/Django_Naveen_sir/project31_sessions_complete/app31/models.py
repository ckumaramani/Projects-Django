from django.db import models

class Staff(models.Model):
    name=models.CharField(max_length=30)
    contactno=models.IntegerField()
    username=models.CharField(max_length=30, primary_key=True)
    password=models.CharField(max_length=30)

