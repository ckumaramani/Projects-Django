from django.db import models

class employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    salalry=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='employees/')
