from django.db import models

class staff(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class user(models.Model):

    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField
    designation=models.CharField(max_length=30)
    Address=models.TextField
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/')
    def _str_(self):
        return self.name