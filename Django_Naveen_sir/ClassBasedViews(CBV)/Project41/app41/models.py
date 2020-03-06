from django.db import models

class Arjun(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    contactno=models.IntegerField()

