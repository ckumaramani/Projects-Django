from django.db import models

class ArjunStaff(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField()
    designation=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


